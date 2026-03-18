"""Run all QA checks for a given intervention.

Usage:
    python qa/run_qa.py <intervention_name>

Runs:
  1. validate_botec.py on outputs/botecs/{name}.xlsx
  2. validate_structure.py on the intervention
  3. extract_citations.py on outputs/writeups/{name}.md

Exit code 0 = all clean, 1 = errors found.
"""

import json
import sys
from pathlib import Path

# Add qa/ to path so we can import sibling modules
sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_botec import validate as validate_botec
from validate_structure import validate as validate_structure
from extract_citations import extract as extract_citations


def run_qa(intervention_name: str) -> dict:
    """Run all QA checks and return combined report."""
    project_root = Path(__file__).resolve().parent.parent
    out_dir = project_root / "outputs" / "qa_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    botec_path = project_root / "outputs" / "botecs" / f"{intervention_name}.xlsx"
    writeup_path = project_root / "outputs" / "writeups" / f"{intervention_name}.md"

    results = {}

    # 1. BOTEC validation
    print("=" * 60)
    print(f"QA for: {intervention_name}")
    print("=" * 60)

    print("\n--- BOTEC Validation ---")
    botec_report = validate_botec(str(botec_path))
    results["botec"] = botec_report
    with open(out_dir / f"{intervention_name}_botec_qa.json", "w", encoding="utf-8") as f:
        json.dump(botec_report, f, indent=2)
    _print_report(botec_report)

    # 2. Structure validation
    print("\n--- Structure Validation ---")
    structure_report = validate_structure(intervention_name, project_root)
    results["structure"] = structure_report
    with open(out_dir / f"{intervention_name}_structure_qa.json", "w", encoding="utf-8") as f:
        json.dump(structure_report, f, indent=2)
    _print_report(structure_report)

    # 3. Citation extraction
    print("\n--- Citation Extraction ---")
    citation_report = extract_citations(str(writeup_path))
    results["citations"] = citation_report
    with open(out_dir / f"{intervention_name}_citations_extracted.json", "w", encoding="utf-8") as f:
        json.dump(citation_report, f, indent=2)
    print(f"  Status: {citation_report['status'].upper()}")
    print(f"  Citations found: {citation_report.get('total_citations', 0)}")
    if citation_report.get("issues"):
        for issue in citation_report["issues"]:
            sev = issue.get("severity", "info")
            print(f"  [{sev.upper()}] {issue['message']}")

    # Overall summary
    all_statuses = [r.get("status", "pass") for r in results.values()]
    has_fail = "fail" in all_statuses or "error" in all_statuses
    has_warn = "warn" in all_statuses

    overall = "FAIL" if has_fail else ("WARN" if has_warn else "PASS")

    print("\n" + "=" * 60)
    print(f"OVERALL: {overall}")
    print("=" * 60)

    total_errors = sum(len(r.get("errors", [])) for r in results.values())
    total_errors += sum(1 for i in results.get("citations", {}).get("issues", [])
                        if i.get("severity") == "error")
    total_warnings = sum(len(r.get("warnings", [])) for r in results.values())
    total_warnings += sum(1 for i in results.get("citations", {}).get("issues", [])
                          if i.get("severity") == "warning")

    if total_errors:
        print(f"  Total errors: {total_errors}")
    if total_warnings:
        print(f"  Total warnings: {total_warnings}")
    if not total_errors and not total_warnings:
        print("  All checks passed.")

    print(f"\nReports written to: {out_dir}")

    return {
        "intervention": intervention_name,
        "overall_status": overall.lower(),
        "results": results,
    }


def _print_report(report: dict):
    """Print a sub-report summary."""
    print(f"  Status: {report.get('status', 'unknown').upper()}")
    for e in report.get("errors", []):
        print(f"  [ERROR] {e['message']}")
    for w in report.get("warnings", []):
        print(f"  [WARN]  {w['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python qa/run_qa.py <intervention_name>", file=sys.stderr)
        sys.exit(2)

    intervention_name = sys.argv[1]
    result = run_qa(intervention_name)

    sys.exit(1 if result["overall_status"] == "fail" else 0)


if __name__ == "__main__":
    main()
