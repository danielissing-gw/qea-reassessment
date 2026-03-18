# Run Log

## Session: 2026-02-20

### QEA 1: Rheumatic Heart Disease Prevention — COMPLETE

- Original QEA: https://docs.google.com/document/d/1siZVFAA3E3SLWroQ_oQqTuxUBMfEYvM_z8tL6eOp2Y8/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1FVr6y-dke7kJUIDbEt5Bqah4zPsc7gaBEqFki08DKaA/
- Year: 2021 | Rating: **High**
- Outputs:
  - `outputs/writeups/rheumatic_heart_disease_prevention.md`
  - `outputs/botecs/rheumatic_heart_disease_prevention.xlsx`
  - Row appended to tracker CSV
- Key notes: WHO 2024 guidelines are a major development (first-ever RF/RHD-specific guidelines; strong recommendation for empirical antibiotic treatment in endemic LMIC). GBD 2021 shows India burden ~29% higher than assumed. 2023 Lancet India CEA finds secondary prevention at ~$30/QALY. Cost remains pivotal unknown — no new data found.

### QEA 2: Uterotonics for PPH — COMPLETE

- Original QEA: https://docs.google.com/document/d/1euCoBUuJQ8V8l7Mgl5SFP6UpcT2H7BioX8uRxoohpoM/
- Original BOTEC: https://docs.google.com/a/givewell.org/spreadsheets/d/1JL3dI9dS2MrtWsA1miIxMm1u9-3Bfbu-RYW7vWTYlGo/ (sparse; only TXA cost row accessible)
- Year: 2017 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/uterotonics_pph_prevention.md`
  - `outputs/botecs/uterotonics_pph_prevention.xlsx`
  - Row appended to tracker CSV
- Key notes: TXA now WHO-recommended for PPH treatment (2017 WOMAN trial + 2024 Lancet meta-analysis: 31% mortality reduction). Heat-stable carbetocin is a new product entirely absent from the 2017 QEA ($0.31/ampoule LMIC price; WHO-recommended where cold chain unavailable). Unitaid AMPLI-PPHI ($26M, 2022-2026) is scaling this up in 6 countries — room for more funding needs investigating. Original misoprostol focus is off the table (WHO 2025: last resort).

### QEA 3: ProCCM — COMPLETE

- Original QEA: None linked
- Original BOTEC: https://docs.google.com/spreadsheets/d/1nqy5INL2LAko2-ARrnBTYyanT-eAxGiPGbG58vvvv8s/
- Year: 2017 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: ProCCM = Muso Health's proactive CCM model in Mali. ProCCM RCT (2017-2020) found no mortality benefit from proactive home visits vs. control (both arms got professional CHWs + reinforced clinics). Muso observational data shows dramatic U5MR decline (154→7/1000 births) at $8/person/year, but no control group. GiveWell has reviewed iCCM and deprioritized. CE likely ~5-7x cash (below 8x bar).

---

## Session: 2026-03-17

### Changes: QA pipeline + format migration

- **Added QA scripts** (`qa/run_qa.py`, `qa/validate_botec.py`, `qa/validate_structure.py`, `qa/extract_citations.py`). QA now runs automatically after each Stage 2 output.
- **Migrated BOTEC format** from multi-sheet (Parameters + Calculation + Notes) to single-sheet (Parameter | Value | Source/notes), matching the example in `docs/examples/`.
- **Updated methodology.md**: new single-sheet BOTEC instructions, Stage 2b QA section, `[Note]` convention for commentary footnotes.
- **Updated CLAUDE.md**: QA step in execution rules, `qa/` and `outputs/qa_reports/` in file structure.

### QEA 1 (redo): Rheumatic Heart Disease Prevention — COMPLETE

- Regenerated writeup with proper `[^N]` footnotes (10 citations, including 1 `[Note]`)
- Regenerated BOTEC in single-sheet format (24 rows, formulas reference cell B values)
- QA: **PASS** (0 errors, 0 warnings)
- Old files preserved as `_old` suffix for comparison

### QEA 2 (redo): Uterotonics for PPH — COMPLETE

- Regenerated writeup with proper `[^N]` footnotes (12 citations, including 3 `[Note]`)
- Regenerated BOTEC in single-sheet format with two sections (TXA + HSC, 24 rows)
- QA: **PASS** (0 errors, 0 warnings)
- Old files preserved as `_old` suffix for comparison

### QEA 3: ProCCM — CSV VALIDATED

- Low rating, no writeup/BOTEC needed
- CSV row validated: PASS

---

## Session: 2026-03-18

### QA review feedback: methodology + RHD + PPH fixes

**Methodology updates** (`docs/methodology.md`):
- Added BOTEC best-guess requirement: BOTEC must represent best-guess CE; subjective adjustments go in the BOTEC, not as writeup overrides
- Added standard BOTEC calculation flow (10-step structure: grant → cost → burden → effect → IV/EV → deaths averted → UoV → ad-hoc adjustments → final CE)
- Tightened citation rules: verbatim means exact (use `[...]` for elisions); basic context claims need sources; CE ranges must be derivable from BOTEC
- Added vaccine/technology pipeline to "Search for updates" checklist

**RHD fixes** (`outputs/writeups/rheumatic_heart_disease_prevention.md`, `outputs/botecs/`):
- Fixed "first-ever" WHO guidelines → "first formal clinical guideline (GRADE methodology), superseding 1988 and 2004 Technical Reports"
- Sourced basic context claims (WHO fact sheet: ~360k deaths/year; World Heart Federation: leading acquired heart disease under 25)
- Fixed inexact quote in footnote [^2] (added missing parenthetical about POC testing)
- Added Strep A vaccine pipeline section (Griffith Phase 1 complete, SAVAC $10M from Wellcome/CEPI)
- Rebuilt BOTEC: added 3x subjective cost multiplier, +30% morbidity uplift, +15% perinatal uplift. CE: **~26x** (range 16-54x). Previous BOTEC was ~54x with no cost adjustment.
- Updated writeup CE section to reference BOTEC directly
- QA: PASS

**PPH fixes** (`outputs/writeups/uterotonics_pph_prevention.md`, `outputs/botecs/`):
- Rebuilt BOTEC from scratch using standard GW CE model structure ($1M grant → births covered → HSC + TXA deaths averted with explicit IV/EV → UoV → morbidity/treatment adjustments → CE)
- CE: **~3.3x** at $2/birth (range ~2x at $3/birth to ~6.5x at $1/birth). Previous claim of 8-15x was a judgment call not derivable from any BOTEC.
- Fixed TXA prevention clarification: not recommended for prevention in ANY delivery mode (not just vaginal birth)
- Fixed broken Ferring HSC link (now points to Ferring's official statement)
- Updated Lancet meta-analysis footnote with actual pooled OR (0.77) and sample size (54,404 women)
- Added E-MOTIVE trial as context (NEJM 2023, RR 0.40 for bundled detection + treatment)
- Updated recommended next steps (replaced "build separate HSC model" with E-MOTIVE implementation investigation)
- QA: PASS

**CSV tracker updated** for both interventions.

---

## Next session: Awaiting expanded master list.
