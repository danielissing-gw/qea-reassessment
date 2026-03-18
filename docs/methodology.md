# Methodology

## Stage 1: Summary Assessment

Run for every QEA.

### 1. Extract key information
- Intervention name
- Original CE estimate (x cash transfers)
- Reasons deprioritized / deemed not cost-effective
- Key uncertainties or evidence gaps flagged
- Date of assessment

### Citation and honesty rules (apply to all stages and outputs)

- **Verbatim quotes required for factual claims, placed in footnotes.** For every factual claim, add a footnote containing the exact supporting sentence(s) from the source in quotation marks, followed by the URL. Do not embed long quotes inline — keep the body text readable and put the evidence in the footnote. A link alone is not enough; the quote is what allows the reader to verify without opening the source. If you cannot find a direct quote supporting the claim, either drop it or mark it unverified.
  - ✓ Good: *The DREAM study found a 62% reduction in HIV incidence.[^1]*
    *[^1]: "18 (1·9%) HIV-1 infections were confirmed during DVR use, resulting in an incidence of 1·8 per 100 person-years, 62% lower than the simulated placebo rate." ([DREAM study, 2021](url))*
  - ✗ Bad: *The DREAM study found a 62% reduction in HIV incidence. ([link](url))*
- **Verbatim means exact.** Do not omit parenthetical text, rephrase, or silently truncate. If you must shorten a quote, use `[...]` to mark elisions. The reader must be able to find the exact string in the source.
- **Source factual claims in "Basic context" too.** Specific numbers (e.g., "300,000 deaths per year") in the "What is this" section need a sourced footnote, just like "Key updates." Common-knowledge framing is OK for 1–2 sentence problem descriptions, but quantitative claims need sources.
- **Do not state a CE range in the writeup that isn't derivable from the BOTEC.** If you believe a bundled program is more cost-effective than individual components, build that into the BOTEC with explicit assumptions (e.g., a shared-infrastructure cost reduction factor). The writeup's CE estimate must come from the BOTEC, not from a separate judgment call.
- **Explicitly label assumptions and guesses.** Whenever a value, estimate, or claim is not directly backed by a cited source — including extrapolations, gap-fills, or judgment calls — flag it clearly inline: "I'm assuming that...", "My estimate is...", "I haven't verified this, but...", etc. Do not present guesses as established facts.
- **Commentary footnotes.** Not every footnote is a citation. For footnotes that contain commentary, calculations, or editorial notes (rather than sourced claims), start the footnote body with `[Note]`. These are exempt from the QA requirement for a URL and verbatim quote.
  - ✓ `[^8]: [Note] Looking only at costs per infection prevented, we're guessing ~$4.7k now vs ~$9.5k then.`

---

### 2. Sense-check the original assessment
Before searching for updates, review the writeup and/or BOTEC for issues:

- **Missing benefit streams:** Plausible effect pathways not modeled? (long-term income, mortality beyond direct mechanism, spillover/herd effects, mental health, fertility)
- **Calculation errors:** Do BOTEC numbers produce the stated result? Unit conversions correct? Parameters consistent with cited sources?
- **Misinterpreted evidence:** Does the writeup accurately characterize its sources? Effect sizes pulled correctly? Subgroup results applied to broader population?
- **Questionable assumptions:** Key assumptions notably conservative or aggressive vs. the evidence?

Flag any issues. An original BOTEC with a math error could flip the conclusion regardless of external changes.

### 3. Search for updates (use web search)
- **Evidence base:** RCTs, systematic reviews, meta-analyses published after the original assessment. Check Cochrane, PubMed Central, 3ie, NBER, major global health journals.
- **WHO guidelines:** Check whether WHO has published new or updated guidelines/recommendations on this intervention since the original assessment. New WHO endorsement, a change in recommendation strength, or inclusion in an Essential Medicines List update can materially shift cost-effectiveness (e.g., by enabling government co-funding or integration into existing delivery platforms).
- **Burden/epidemiology:** Most recent GBD estimates and WHO data. Has burden changed materially?
- **Costs and technology:** Input cost changes? New delivery technologies?
- **Funding landscape:** Funding increases or decreases? Major gaps from donor exits?
- **Implementation:** New large-scale evidence (government scale-ups, new delivery models)?
- **Vaccine and technology pipeline:** Check whether any vaccines, diagnostics, or delivery technologies are in clinical development (Phase I–III) that could materially change the intervention landscape within 5–10 years. A near-term vaccine for the underlying pathogen could make a prevention program obsolete or complementary.

### 4. Assess likelihood worth revisiting
- **High:** Multiple dimensions shifted favorably, OR one shifted dramatically (cost >50% drop, major new RCT with large effect). Likely clears the 8x bar on closer look.
- **Medium:** Some favorable shifts, uncertain if large enough. Worth a second look.
- **Low:** Little changed, or changes cut both directions. Original assessment likely holds, or the program appears even less promising.

### 5. Append row to tracker CSV
Columns: Intervention name | Year of original assessment | Original CE estimate (x cash) | Original reason deprioritized | Likelihood worth revisiting (H/M/L) | Updated rough CE estimate (x cash) | Confidence in updated estimate (H/M/L) | Reason (brief explanation for Low; "see writeup" for Medium/High)

- **Original reason deprioritized:** A brief phrase capturing why the intervention didn't move forward at the time (e.g., "not cost-effective", "lack of credible evidence", "small target population", "insufficient room for more funding", "weak external validity").
- **Confidence in updated estimate (H/M/L):** This is an *absolute* judgment about how close the updated estimate is likely to be to the truth, not a relative comparison to the original.
  - **High:** Key parameters are anchored to strong evidence (recent large RCTs, robust cost data); estimate unlikely to move much with further investigation.
  - **Medium:** Reasonable evidence for most parameters, but one or two key inputs rest on weaker data or extrapolation; estimate could shift meaningfully.
  - **Low:** Estimate is highly speculative — key parameters are guesses, based on indirect evidence, or drawn from very different contexts. Treat as directional only.

---

## Stage 2: Per-Intervention Writeup and BOTEC

Run only for High and Medium interventions. 

### Structure for Writeup

1. **What is this (basic context)**
   - What is the problem? (1-2 sentences)
   - What is the program? (1-2 sentences)

2. **Key updates:** The 2-3 most important changes since the original assessment *that would plausibly change our estimate of cost-effectiveness*. Only include developments that affect a parameter in the CE model (effect size, cost, coverage, burden, etc.) or that change the feasibility of funding the intervention. Do not list updates that are merely interesting but immaterial. For each update: include a verbatim quote from the source that supports the claim, followed by the URL (see citation rules above). Flag discrepancies between old and new data (see examples.md for the level of detail expected).

3. **New CE estimate:** State the bottom line (Xx benchmark), then reference the BOTEC file. Brief commentary on what drove the change.

4. **Remaining uncertainties:** What would we most need to investigate to firm up the estimate? Be specific — not "review the literature" but "the Phase III trial for [specific thing] reports in [timeframe] and would resolve [specific parameter]."

5. **Who is implementing / funding this?** Organizations running these programs, leading implementers, major funders. Note if the intervention isn't being delivered at scale yet.

6. **Recommended next steps:** 2-3 highest-value actions. For each, explain *why* it is recommended — what question it would answer, what uncertainty it would resolve, or what decision it would enable. Focus on what's specific to this intervention and non-obvious — not generic "talk to implementers" unless there's a specific implementer and a specific question.

   For at least one next step, **suggest a specific person or organization to talk to** — e.g., a lead author of a key study, a program manager at a known implementer, or a technical advisor at WHO/UNICEF. Briefly explain why they would be a good source (e.g., "led the largest RCT on this intervention", "runs the only at-scale program in SSA"). If you cannot identify a specific individual, name the most relevant organization and team (e.g., "the NTD team at WHO Geneva" or "PATH's vaccine delivery group").

Save to `./outputs/writeups/{intervention_name}.md`.

### Update BOTEC

What we want is a simple BOTEC, not a full model. Save to `./outputs/botecs/{intervention_name}.xlsx` using `openpyxl`.

#### The BOTEC must represent your best-guess CE estimate

Do not present a BOTEC you don't believe and then state a different number in the writeup. If you think a parameter is wrong (e.g., costs are underestimated), make a subjective adjustment in the BOTEC itself — clearly labeled as such (e.g., "Subjective cost multiplier: 5x — original Cuba estimate likely understates India costs"). If you think benefit streams are missing, model them with rough percentage additions (e.g., "+30% for morbidity averted"), clearly labeled as assumptions. The writeup's CE estimate should reference the BOTEC output, not override it.

#### Standard BOTEC calculation flow

Follow this structure unless there's a good reason to deviate. The goal is a consistent, auditable chain from grant dollars to multiples of benchmark.

1. **Grant amount** — Start with an arbitrary amount (typically $1M) to anchor the calculation.
2. **Cost per person reached** → **number of people reached** by the grant.
3. **Burden data** — Disease incidence/prevalence/mortality in the target population.
4. **Effect size** — From the best available evidence. If using multiple sources, state the weight given to each.
5. **Internal validity (IV) adjustment** — Discount for study quality (e.g., observational vs. RCT). Even if 0%, include the row explicitly.
6. **External validity (EV) adjustment** — Discount for extrapolation from study context to target context. Even if 0%, include the row explicitly.
7. **Deaths (or cases) averted** — From the above.
8. **Convert to units of value** — Deaths averted × moral weights. Use GiveWell's standard moral weights (currently 52.5 UoV per under-5 death averted, or the relevant age-specific weight).
9. **Ad-hoc adjustments for other benefit streams** — Morbidity (YLDs), income effects, treatment costs averted, etc. Model as explicit percentage additions, clearly labeled as assumptions.
10. **Final CE** — Total UoV ÷ grant amount ÷ benchmark (344 UoV per $100k, i.e., 0.00344 UoV per dollar).

#### Layout

Single sheet ("BOTEC") with three columns:

| A: Parameter | B: Value | C: Source / notes |

- **Column A:** Parameter labels, grouped under bold section headers (e.g., **Costs**, **Burden & effect**, **Benefits**, **Final CE**).
- **Column B:** Numeric inputs or cell formulas (e.g., `=B3*B4`, `=SUM(B17:B21)*B15`). Put numeric values as numbers, not text, so they can be referenced in formulas. Rows that compute derived quantities should use formulas, not pre-computed values.
- **Column C:** Source URL (as a hyperlink), "Calculation", or a brief note explaining the value. Add `openpyxl.comments.Comment` with verbatim quotes from sources for key assumptions.

See `docs/examples/build_vaginal_rings_dapivirine_botec.py` for the reference implementation.

---

### Stage 2b: Quality Assurance

Run after completing Stage 2 outputs (writeup + BOTEC) for each intervention.

```
python qa/run_qa.py {intervention_name}
```

This runs three checks:

1. **BOTEC validation** (`qa/validate_botec.py`): Detects circular references, formula errors (unbalanced parens, unknown functions, references to non-existent sheets), hyperlink issues, and structural problems (missing section headers, no formulas, no labels).

2. **Structure validation** (`qa/validate_structure.py`): Checks that the writeup has all required H2 sections, footnote citations, and URLs; that the CSV tracker row is complete with valid values; that the BOTEC file exists and contains formulas; and that filenames are consistent.

3. **Citation extraction** (`qa/extract_citations.py`): Parses all footnote and blockquote citations, extracts quoted text and URLs. Flags citations missing URLs or verbatim quotes. Outputs a JSON file for the main session to verify via WebFetch (comparing quoted text against fetched page content).

**Process:**
- Fix any errors flagged by the QA scripts. Re-run until the report is clean (exit code 0).
- After the deterministic checks pass, review the citation extraction report. For key claims, fetch the source URL and verify the quoted text appears on the page.
- Only proceed to the next QEA after QA passes.
