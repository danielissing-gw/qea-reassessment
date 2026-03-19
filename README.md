# QEA Reassessment

Reassesses GiveWell's past Quick Evidence Assessments (QEAs) to find interventions worth revisiting — where changes in evidence, costs, burden, funding, or technology could make an intervention more cost-effective than previously estimated.

## How it works

Each QEA goes through two stages:

1. **Stage 1 (all interventions):** Screen the intervention against new evidence and rate as High / Medium / Low promisingness. Append a row to the tracker CSV.
2. **Stage 2 (High and Medium only):** Write a structured writeup and build a BOTEC spreadsheet with updated parameters and formulas. Run automated QA checks before moving on.

See `docs/methodology.md` for full instructions.

## Key files

| Path | What it is |
|---|---|
| `docs/methodology.md` | Stage 1, Stage 2, and QA instructions |
| `docs/background.md` | Context on what QEAs are and why revisit them |
| `docs/examples/` | Reference outputs (vaginal rings / dapivirine example) |
| `outputs/qea_reassessment_tracker.csv` | Master tracker with one row per intervention |
| `outputs/writeups/{name}.md` | Per-intervention writeups (renders natively on GitHub) |
| `outputs/botecs/{name}.xlsx` | Per-intervention BOTEC spreadsheets (download or open in Google Drive to view) |
| `outputs/botecs/{name}.csv` | BOTEC summary with computed values (renders natively on GitHub) |
| `outputs/run_log.md` | Session-by-session progress log |
| `qa/run_qa.py` | Run all QA checks for an intervention |
| `CLAUDE.md` | Instructions for Claude Code sessions |

## Running QA

After producing Stage 2 outputs:

```
python qa/run_qa.py {intervention_name}
```

This validates the BOTEC (circular refs, formula errors, hyperlinks), checks output structure (required sections, CSV row, filenames), and extracts citations for verification.
