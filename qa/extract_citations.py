"""Extract citations from a writeup markdown file.

Parses:
  - [^N] footnote definitions -> quoted text + URL
  - Inline blockquote citations -> quoted text + URL

Flags citations missing URLs or missing quoted text.
Footnotes starting with "[Note]" are treated as commentary and exempt
from URL/quote requirements.

Usage:
    python qa/extract_citations.py <path_to_md>

Writes JSON to outputs/qa_reports/{stem}_citations_extracted.json
"""

import json
import re
import sys
from pathlib import Path

# Footnote definition: [^N]: "quoted text" URL
# or [^N]: text with URL somewhere
_FOOTNOTE_DEF = re.compile(
    r"^\[\^(\d+)\]:\s*(.+?)(?:\n(?!\[\^).*)*",
    re.MULTILINE
)

# URL pattern
_URL = re.compile(r"https?://[^\s\)>\]]+")

# Quoted text: "..." or "..." (smart quotes) or «...»
_QUOTED = re.compile(r'["\u201c](.+?)["\u201d]', re.DOTALL)


def extract_footnotes(text: str) -> list[dict]:
    """Extract [^N] footnote definitions with their content."""
    citations = []

    # Split text to find footnote definitions at the end
    # Footnotes are typically at the bottom, each starting with [^N]:
    footnote_blocks = re.findall(
        r"^\[\^(\d+)\]:\s*(.*?)(?=\n\[\^\d+\]:|\Z)",
        text,
        re.MULTILINE | re.DOTALL
    )

    for num, body in footnote_blocks:
        body = body.strip()
        is_note = body.lower().startswith("[note]")
        urls = _URL.findall(body)
        quotes = _QUOTED.findall(body)

        issues = []
        if not is_note:
            if not urls:
                issues.append("missing_url")
            if not quotes:
                issues.append("missing_quote")

        citations.append({
            "type": "note" if is_note else "footnote",
            "number": int(num),
            "body": body,
            "urls": urls,
            "quotes": [q.strip() for q in quotes],
            "issues": issues,
        })

    return citations


def extract_blockquote_citations(text: str) -> list[dict]:
    """Extract blockquote citations (lines starting with >)."""
    citations = []

    # Find blockquote blocks
    blocks = re.findall(r"((?:^>.*\n?)+)", text, re.MULTILINE)

    for block in blocks:
        # Strip > prefix from each line
        content = "\n".join(
            line.lstrip(">").strip() for line in block.strip().split("\n")
        ).strip()

        urls = _URL.findall(content)
        quotes = _QUOTED.findall(content)

        issues = []
        if not urls:
            issues.append("missing_url")
        if not quotes:
            issues.append("missing_quote")

        citations.append({
            "type": "blockquote",
            "body": content,
            "urls": urls,
            "quotes": [q.strip() for q in quotes],
            "issues": issues,
        })

    return citations


def extract(md_path: str) -> dict:
    """Extract all citations from a markdown file."""
    path = Path(md_path)
    if not path.exists():
        return {
            "file": str(path),
            "status": "error",
            "citations": [],
            "issues": [{"message": f"File not found: {path}"}]
        }

    text = path.read_text(encoding="utf-8")

    footnotes = extract_footnotes(text)
    blockquotes = extract_blockquote_citations(text)

    all_citations = footnotes + blockquotes

    # Summary issues
    issues = []
    missing_url = [c for c in all_citations if "missing_url" in c.get("issues", [])]
    missing_quote = [c for c in all_citations if "missing_quote" in c.get("issues", [])]

    if missing_url:
        for c in missing_url:
            label = f"footnote {c['number']}" if c["type"] in ("footnote", "note") else "blockquote"
            issues.append({
                "severity": "error",
                "citation": label,
                "message": f"Citation ({label}) has no URL."
            })

    if missing_quote:
        for c in missing_quote:
            label = f"footnote {c['number']}" if c["type"] in ("footnote", "note") else "blockquote"
            issues.append({
                "severity": "warning",
                "citation": label,
                "message": f"Citation ({label}) has no verbatim quote in quotation marks."
            })

    if not all_citations:
        issues.append({
            "severity": "error",
            "message": "No citations found in document."
        })

    has_errors = any(i.get("severity") == "error" for i in issues)
    has_warnings = any(i.get("severity") == "warning" for i in issues)

    return {
        "file": str(path),
        "status": "fail" if has_errors else ("warn" if has_warnings else "pass"),
        "total_citations": len(all_citations),
        "citations": all_citations,
        "issues": issues,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python qa/extract_citations.py <path_to_md>", file=sys.stderr)
        sys.exit(2)

    md_path = sys.argv[1]
    report = extract(md_path)

    # Determine output path
    stem = Path(md_path).stem
    project_root = Path(__file__).resolve().parent.parent
    out_dir = project_root / "outputs" / "qa_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{stem}_citations_extracted.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Print summary
    print(f"Citation extraction: {report['status'].upper()}")
    print(f"  Total citations found: {report['total_citations']}")
    if report["issues"]:
        for issue in report["issues"]:
            sev = issue.get("severity", "info")
            print(f"  [{sev.upper()}] {issue['message']}")
    else:
        print("  All citations have quotes and URLs.")

    print(f"Report: {out_path}")
    has_errors = any(i.get("severity") == "error" for i in report["issues"])
    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
