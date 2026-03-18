"""Validate the structure of all outputs for a given intervention.

Checks:
  - Writeup (.md): required H2 sections, footnotes, URLs, header links
  - CSV row: all 8 columns populated, valid H/M/L fields, 4-digit year
  - BOTEC (.xlsx): file exists, at least one formula cell
  - Filenames: writeup, BOTEC, and build script share same stem

Usage:
    python qa/validate_structure.py <intervention_name>

Writes JSON report to outputs/qa_reports/{name}_structure_qa.json
"""

import csv
import json
import os
import re
import sys
from pathlib import Path

import openpyxl

REQUIRED_SECTIONS = [
    "What is this",
    "Key updates",
    "New CE estimate",
    "Remaining uncertainties",
    "Who is implementing",
    "Recommended next steps",
]

# Match H2 headers: ## Section Name
_H2_PATTERN = re.compile(r"^##\s+(.+)", re.MULTILINE)
# Footnote definition: [^N]: ...
_FOOTNOTE_DEF = re.compile(r"^\[\^(\d+)\]:", re.MULTILINE)
# Blockquote citation (line starting with >)
_BLOCKQUOTE = re.compile(r"^>\s+", re.MULTILINE)
# URLs
_URL_PATTERN = re.compile(r"https?://[^\s\)>\]]+")


def check_writeup(writeup_path: Path) -> list[dict]:
    """Validate writeup markdown structure."""
    errors = []

    if not writeup_path.exists():
        errors.append({
            "check": "writeup_missing",
            "severity": "error",
            "message": f"Writeup not found: {writeup_path}"
        })
        return errors

    text = writeup_path.read_text(encoding="utf-8")

    # Required sections
    h2_headers = [m.group(1).strip() for m in _H2_PATTERN.finditer(text)]
    h2_lower = [h.lower() for h in h2_headers]

    for section in REQUIRED_SECTIONS:
        found = any(section.lower() in h for h in h2_lower)
        if not found:
            errors.append({
                "check": "missing_section",
                "severity": "error",
                "section": section,
                "found_sections": h2_headers,
                "message": f"Required section '{section}' not found in writeup. "
                           f"Found: {h2_headers}"
            })

    # At least one footnote citation
    footnotes = _FOOTNOTE_DEF.findall(text)
    blockquotes = _BLOCKQUOTE.findall(text)
    if not footnotes and not blockquotes:
        errors.append({
            "check": "no_citations",
            "severity": "error",
            "message": "No footnote citations ([^N]:) or blockquote citations found in writeup."
        })

    # At least one URL
    urls = _URL_PATTERN.findall(text)
    if not urls:
        errors.append({
            "check": "no_urls",
            "severity": "error",
            "message": "No URLs found in writeup."
        })

    # Check for links to original QEA and BOTEC in the header area (first 20 lines)
    header_lines = "\n".join(text.split("\n")[:20])
    has_qea_link = bool(_URL_PATTERN.search(header_lines))
    if not has_qea_link:
        errors.append({
            "check": "no_header_links",
            "severity": "warning",
            "message": "No links found in the header area (first 20 lines). "
                       "Expected links to original QEA and/or BOTEC."
        })

    return errors


def check_csv_row(intervention_name: str, tracker_path: Path) -> list[dict]:
    """Validate that the tracker CSV has a valid row for this intervention."""
    errors = []

    if not tracker_path.exists():
        errors.append({
            "check": "tracker_missing",
            "severity": "error",
            "message": f"Tracker CSV not found: {tracker_path}"
        })
        return errors

    with open(tracker_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find matching row: substring match, or word-overlap match
    name_lower = intervention_name.lower().replace("_", " ")
    name_words = [w for w in name_lower.split() if len(w) >= 3]

    def _matches(csv_name: str) -> bool:
        csv_lower = csv_name.lower().replace("_", " ")
        # Direct substring match
        if name_lower in csv_lower:
            return True
        if not name_words:
            return False
        # First significant word must match
        if name_words[0] not in csv_lower:
            return False
        # At least half of the remaining significant words must appear
        other_words = name_words[1:]
        if not other_words:
            return True
        hits = sum(1 for w in other_words if w in csv_lower)
        return hits >= len(other_words) / 2
        return False

    matching = [r for r in rows if _matches(r.get("Intervention name", ""))]

    if not matching:
        errors.append({
            "check": "csv_no_row",
            "severity": "error",
            "message": f"No row found in tracker CSV for '{intervention_name}'."
        })
        return errors

    row = matching[0]
    expected_cols = [
        "Intervention name",
        "Year of original assessment",
        "Original CE estimate (x cash)",
        "Original reason deprioritized",
        "Likelihood worth revisiting (H/M/L)",
        "Updated rough CE estimate (x cash)",
        "Confidence in updated estimate (H/M/L)",
        "Reason",
    ]

    # All 8 columns have values
    for col in expected_cols:
        val = row.get(col, "").strip()
        if not val:
            errors.append({
                "check": "csv_empty_column",
                "severity": "error",
                "column": col,
                "message": f"CSV column '{col}' is empty for this intervention."
            })

    # H/M/L fields valid
    for col_name in ["Likelihood worth revisiting (H/M/L)",
                     "Confidence in updated estimate (H/M/L)"]:
        val = row.get(col_name, "").strip().upper()
        if val and val not in ("H", "M", "L", "HIGH", "MEDIUM", "LOW"):
            errors.append({
                "check": "csv_invalid_hml",
                "severity": "error",
                "column": col_name,
                "value": val,
                "message": f"CSV column '{col_name}' has invalid value '{val}'. "
                           f"Expected H, M, or L."
            })

    # Year is 4-digit number
    year_val = row.get("Year of original assessment", "").strip()
    if year_val and not re.match(r"^\d{4}$", year_val):
        errors.append({
            "check": "csv_invalid_year",
            "severity": "warning",
            "value": year_val,
            "message": f"Year '{year_val}' is not a 4-digit number."
        })

    return errors


def check_botec_exists(botec_path: Path) -> list[dict]:
    """Check BOTEC file exists and has at least one formula."""
    errors = []

    if not botec_path.exists():
        errors.append({
            "check": "botec_missing",
            "severity": "error",
            "message": f"BOTEC file not found: {botec_path}"
        })
        return errors

    try:
        wb = openpyxl.load_workbook(str(botec_path))
    except Exception as e:
        errors.append({
            "check": "botec_load_failed",
            "severity": "error",
            "message": f"Failed to load BOTEC: {e}"
        })
        return errors

    has_formula = False
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and cell.value.startswith("="):
                    has_formula = True
                    break
            if has_formula:
                break
        if has_formula:
            break

    if not has_formula:
        errors.append({
            "check": "botec_no_formulas",
            "severity": "error",
            "message": "BOTEC has no formula cells. Expected cell formulas for calculations."
        })

    return errors


def check_filenames(intervention_name: str, project_root: Path) -> list[dict]:
    """Check that writeup, BOTEC, and build script use consistent naming."""
    errors = []

    writeup = project_root / "outputs" / "writeups" / f"{intervention_name}.md"
    botec = project_root / "outputs" / "botecs" / f"{intervention_name}.xlsx"
    build_script = project_root / "outputs" / "botecs" / f"build_{intervention_name}_botec.py"

    expected = {
        "writeup": writeup,
        "botec": botec,
        "build_script": build_script,
    }

    missing = {k: v for k, v in expected.items() if not v.exists()}
    present = {k: v for k, v in expected.items() if v.exists()}

    if missing and present:
        errors.append({
            "check": "filename_mismatch",
            "severity": "warning",
            "present": {k: str(v) for k, v in present.items()},
            "missing": {k: str(v) for k, v in missing.items()},
            "message": f"Inconsistent filenames: present={list(present.keys())}, "
                       f"missing={list(missing.keys())}. "
                       f"Expected all files to use stem '{intervention_name}'."
        })

    return errors


def validate(intervention_name: str, project_root: Path | None = None) -> dict:
    """Run all structure checks for an intervention."""
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    writeup_path = project_root / "outputs" / "writeups" / f"{intervention_name}.md"
    botec_path = project_root / "outputs" / "botecs" / f"{intervention_name}.xlsx"
    tracker_path = project_root / "outputs" / "qea_reassessment_tracker.csv"

    all_issues = []
    all_issues.extend(check_writeup(writeup_path))
    all_issues.extend(check_csv_row(intervention_name, tracker_path))
    all_issues.extend(check_botec_exists(botec_path))
    all_issues.extend(check_filenames(intervention_name, project_root))

    errors = [i for i in all_issues if i["severity"] == "error"]
    warnings = [i for i in all_issues if i["severity"] == "warning"]

    return {
        "intervention": intervention_name,
        "status": "fail" if errors else ("warn" if warnings else "pass"),
        "errors": errors,
        "warnings": warnings,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python qa/validate_structure.py <intervention_name>",
              file=sys.stderr)
        sys.exit(2)

    intervention_name = sys.argv[1]
    report = validate(intervention_name)

    # Write report
    project_root = Path(__file__).resolve().parent.parent
    out_dir = project_root / "outputs" / "qa_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{intervention_name}_structure_qa.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Print summary
    print(f"Structure QA: {report['status'].upper()}")
    if report["errors"]:
        print(f"  {len(report['errors'])} error(s):")
        for e in report["errors"]:
            print(f"    - {e['message']}")
    if report["warnings"]:
        print(f"  {len(report['warnings'])} warning(s):")
        for w in report["warnings"]:
            print(f"    - {w['message']}")
    if not report["errors"] and not report["warnings"]:
        print("  All checks passed.")

    print(f"Report: {out_path}")
    sys.exit(1 if report["errors"] else 0)


if __name__ == "__main__":
    main()
