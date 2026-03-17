# Examples

Two worked examples showing expected outputs at different promisingness levels. Local copies of each example output are in `docs/examples/`.

## Example 1: Low promisingness (CSV row only)

**Intervention:**  Sexual and reproductive health programs in refugee camps

- Original QEA: https://docs.google.com/document/d/1rh3rhDWNUJisksdPneudQE7XeuvVnGRHdDL0jIs45Z4/edit?tab=t.kpj5mu4f7jqf#heading=h.8q6nfqj792d
- Original BOTEC: https://docs.google.com/spreadsheets/d/1cP6RH_AffZzOTvaPapKplikTUsOgYLvKKqwanb_Pm7o/edit?gid=162466198#gid=162466198

**Local example output:** [`examples/sexual_reproductive_health_refugees_csv_row.csv`](examples/sexual_reproductive_health_refugees_csv_row.csv)

**What to notice:** No writeup is produced. The "Reason" column in the CSV gives a brief, intuitive explanation of why this doesn't look promising. That's the entire output for a Low intervention.

## Example 2: Medium promisingness (CSV row + writeup + BOTEC)

**Intervention:** Vaginal Rings w/Dapivirine for HIV Prevention

- Original QEA: https://docs.google.com/document/d/1EZU8ogduJC3kEh9NQvDloBNZBY0sXYz3SacfAZ1GKxI/edit?tab=t.0
- Original BOTEC: https://docs.google.com/spreadsheets/d/1yJYR7g7V_O0hS8-rbBe7tHeDZCM-uUASi2PjFNFARiw/edit?gid=0#gid=0

**Local example outputs:**
- CSV row: [`examples/vaginal_rings_dapivirine_csv_row.csv`](examples/vaginal_rings_dapivirine_csv_row.csv)
- Writeup: [`examples/vaginal_rings_dapivirine.md`](examples/vaginal_rings_dapivirine.md)
- BOTEC (readable reference): [`examples/vaginal_rings_dapivirine_botec.md`](examples/vaginal_rings_dapivirine_botec.md)
- BOTEC (build script): [`examples/build_vaginal_rings_dapivirine_botec.py`](examples/build_vaginal_rings_dapivirine_botec.py) — generates the `.xlsx`
- BOTEC (spreadsheet): [`examples/vaginal_rings_dapivirine_botec.xlsx`](examples/vaginal_rings_dapivirine_botec.xlsx)

**What to notice:**
- The "What is this" section is short — 2 bullets, not a full literature review. This is just to provide context for the reader!
- Footnotes can be used to flag specific discrepancies that came up during the review
- The writeup is honest about things it didn't evaluate / look into or is unsure about
- "Key updates" only include developments that would change our assessment of cost-effectiveness — not every paper published on the topic
- **Every factual claim in "Key updates" is backed by a verbatim quote from the source**, placed in a footnote rather than inline. The body text stays readable; the footnote contains the exact passage and URL so the reader can verify without opening the source.
- **Assumptions and guesses are flagged explicitly.** Phrases like "my guess is that...", "I'm not sure if...", "I haven't verified this, but...", and "This is an assumption I have not reviewed" appear throughout — making clear what is evidence-based and what is not.
- Next steps are specific, not just a laundry list of things a researcher might do for any reviewed QEA
- Each next step explains *why* it's recommended (what question it answers or what uncertainty it resolves)
- At least one next step names a specific person or organization to talk to, with a reason why they're the right source
