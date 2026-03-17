# QEA Reassessment Project

## What this project does

Reassesses GiveWell's past quick evidence assessments (QEAs) to identify interventions worth revisiting — where changes in evidence, costs, burden, funding, or technology could make an intervention more cost-effective than previously estimated.

## Key references

- **CE bar:** 8x benchmark (1x = 0.003355 units of value per dollar spent)
- **QEA master list:** https://docs.google.com/spreadsheets/d/1lKoIEO4LAkJl5vMQXa5j2FWo8BLCkANKNiuOttb0dcI/edit?gid=0#gid=0
  - Col A: Intervention name | Col B: Writeup link (Google Doc) | Col C: BOTEC link (Google Sheet) | Col D: Year written
  - B or C may be empty

## How to access documents

- Read writeups and BOTECs from Google Drive via MCP
- If a doc is inaccessible, log in `run_log.md` and move on

## File structure

```
./docs/
    background.md          # GiveWell context, what makes a QEA worth revisiting
    methodology.md         # Stage 1 and Stage 2 instructions
    examples.md            # Example outputs (Low and Medium interventions)
./outputs/
    qea_reassessment_tracker.csv
    run_log.md
    summary.md
    writeups/{intervention_name}.md
    botecs/{intervention_name}.xlsx
```

## Execution rules

- Process QEAs **one at a time**. Finish all stages before starting the next.
- **Save after each QEA.** Append to the CSV and write any Stage 2 files immediately.
- Log progress to `run_log.md` after each QEA.
- **Start a new session every 3 QEAs** (or sooner if context feels degraded). Each QEA involves reading source documents, running web searches, and generating outputs — this fills the context window. Starting fresh avoids compression artifacts. Check `run_log.md` at the start of each session to see where to pick up.
- See `./docs/methodology.md` for Stage 1 and Stage 2 instructions.
- See `./docs/examples.md` for example outputs at each promisingness level.

## Core guidelines

- **Use web search actively** to find what's changed since the original assessment.
- **Check WHO guidelines** for every intervention — especially whether recommendations have been published or updated since the original QEA.
- **Be honest about uncertainty.** Don't fabricate numbers.
- **Err toward flagging things as worth revisiting.** False positives are cheap; false negatives are expensive.
- **Verbatim quotes required, in footnotes.** For every factual claim, add a footnote with the exact supporting text from the source in quotation marks, followed by the URL. Keep the body text readable — put the evidence in the footnote, not inline. A link alone is not sufficient. If no direct quote supports the claim, drop it or mark it unverified.
- **Flag assumptions explicitly.** Any value or claim not directly supported by a cited source must be labeled as such inline: "I'm assuming that...", "My estimate is...", "I haven't verified this, but...". Never present a guess as a fact.
- **Don't assume the original was correct.** Flag errors and missed benefit streams.

## Permissions

Pre-approved (no confirmation needed):
- Web search and web fetch
- Reading any Google Drive / Docs / Sheets / Gmail content
- Creating **new** files (.md, .xlsx, .csv)
- Running Python scripts (e.g., for .xlsx generation)

**Ask for confirmation before:**
- Editing or deleting an existing file
- Any Google Workspace action that creates, modifies, or deletes data (e.g., sending email, editing a Google Doc)