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

## Session: 2026-03-18 (continued)

### Processing 10 new QEAs from expanded master list (batch 1 of 4: QEAs 1–3)

### QEA 4: Ponseti method clubfoot treatments — COMPLETE

- Original QEA: https://docs.google.com/document/d/17GKIUCZDOJk5Lg2JzUbooReZcqR6DXIqcIyHoY2wMBM/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1-4IdGmqCboxOD_Loc2QXUPnGnZ32i4qZ3sTkCcGtEms/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: GiveWell already investigated this in depth and awarded a $5.2M grant to MiracleFeet in Jan 2023, estimating CE at ~8x (slightly below their 10x bar). Cost per case ($530) is higher than the QEA assumed ($414). Evidence quality hasn't improved — still no RCTs, Cochrane 2020 remains the benchmark. ~47% relapse at 10+ years still a concern. GiveWell's M&E study ($600k, May 2023) is underway — results expected ~2027 are the next inflection point. No new WHO guidelines on clubfoot.

### QEA 5: Diabetes prevention programs (K-DPP) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1IWsjrRw7_B3x9kH2FF7LH6ssEuUDOzy5XOYRTAutI_M/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1h4eW98HLh_yDcBEavE9ucB4v0Nv-9SMQui2SaD9-Fys/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: CE at 0.62x cash — an order of magnitude below the 8x bar. The sole RCT (K-DPP 2018, n=1,007) found a non-significant 12% reduction in diabetes incidence (RR 0.88, p=0.36). The DALY estimate (1 per case prevented) is acknowledged as speculative. A 9-year follow-up study protocol was published in March 2023 but results are not yet available. GBD 2021 confirms growing diabetes burden in LMICs but this doesn't help the CE arithmetic. Even generous DALY assumptions (10/case) would only reach ~6x. Not worth revisiting.

### QEA 6: Flood-tolerant rice in South Asia — COMPLETE

- Original QEA: https://docs.google.com/document/d/1BC0YFgXxDQYb6wVf82UuN187N05C-yiRRcE8ljjeGTg/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1V9MUdXAsEwHI35_xQ4kE8aX6pmbNfdRO15LNTTSD4nA/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: Standalone CE (3.7x) is far below 8x bar. Platform delivery via PxD reaches 9.9x in threshold analysis but barely clears bar and depends on PxD cost assumptions. Some favorable updates: (1) no yield penalty in non-flood years confirmed; (2) PxD is actively distributing Swarna-Sub1 in West Bengal; (3) climate change increasing flood frequency. But GiveWell is already investigating PxD separately via a $540k scoping grant (March 2022). Flood-tolerant rice bundling is really part of the broader PxD evaluation, not an independent intervention worth pursuing. Next-gen varieties (3+ weeks submergence tolerance) in development but not yet deployed.

---

**Batch 1 complete (QEAs 4–6). All three rated Low. Session should be refreshed before batch 2.**

## Session: 2026-03-18 (batch 2 of 4: QEAs 7–9)

### QEA 7: Legislation for road traffic safety — COMPLETE

- Original QEA: https://docs.google.com/document/d/1Lv8syz1787saZMlqviGE8lSfec9N8jWLjBEg8UVVPPQ/
- Original BOTEC: https://docs.google.com/spreadsheets/d/179IER-AnmGpLYxf-bvuusNmyjJ-NncI4MPNVMmHzhJc/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: Policy advocacy model (not direct delivery), CE median 13x across 5 countries but highly speculative — parameters borrowed from alcohol policy model. Bloomberg Philanthropies has doubled commitment to $240M for 2020-2025, covering 16 countries including all 5 modeled in the QEA. India drives most of the CE (38x) but Bloomberg already active there. Government enforcement costs were likely underestimated. Rethink Priorities found some niche remaining opportunities (Pakistan, Thailand) but overall space is well-funded. Not worth independent investigation given limited counterfactual impact.

### QEA 8: Oral azithromycin during labor — COMPLETE

- Original QEA: https://docs.google.com/document/d/1rdNToIRCSfux7pcgUdjOdfhv7MDYJssqD-hBVwVsF3s/
- Original BOTEC: https://docs.google.com/spreadsheets/d/171kRw2c0D5glTLNrGDGLuQTlM0gEMXxNnP7ibj1lEp0/
- Year: 2022 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/oral_azithromycin_during_labor.md`
  - `outputs/botecs/oral_azithromycin_during_labor.xlsx`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 8 citations)
- Key notes: A-PLUS trial (NEJM 2023, n=29,278) found strong maternal benefit (RR 0.67 for maternal sepsis/death) but null neonatal result (RR 1.02). PregnAnZI-2 confirmed neonatal null. This fundamentally changes the CE arithmetic — neonatal mortality drove 66-86% of original benefits. Maternal effect is 4x larger than assumed but applies to few deaths per pregnancy. CE in high-MMR Nigeria: ~4x at $3/pregnancy, ~9x at $1.50. Drug costs only $0.91/dose. Lancet Global Health 2025 CEA finds cost-saving from health system perspective. Pivotal unknown: incremental delivery cost. Could potentially be bundled with PPH interventions (HSC/TXA) on same facility platform.

### QEA 9: Phone audits to improve government service delivery — COMPLETE

- Original QEA: https://docs.google.com/document/d/1QNc2qrqzrKtbtNbL33S5u22CeG1W2N7_P7fpx57GQDQ/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1wi8lG2luvq8IMmFY2cMuOvM1OAXvW8wyAkFhoK2VfTA/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: CE at 0.15x — far below bar. The underlying cash transfer program is in middle-income India (Telangana per capita income $2,817 vs. $212 for GD recipients). Even the leverage framing yields negative CE by standard assumptions. The concept of phone monitoring for more cost-effective programs (health, SSA) is interesting but speculative — no evidence, no implementer identified. Research team has expanded to Pakistan/Paraguay via J-PAL but no new published results. Not worth revisiting.

---

**Batch 2 complete (QEAs 7–9). Two rated Low (road safety, phone audits), one rated Medium (oral azithromycin). Session should be refreshed before batch 3.**

## Session: 2026-03-18 (batch 3 of 4: QEAs 10–12)

### QEA 10: CCTs for antenatal care, facility delivery and postnatal care — COMPLETE

- Original QEA: https://docs.google.com/document/d/1RvONr5ZRzqb-GUdOLoi8-3BD51TZEKmbZfdeY9tl3H8/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1w-lmXJyXIFT5h4NfXg_zwfKShse3RxoAkc3iL3A4Kmk/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: CE at ~4x (full package) or ~7x (ANC-only) — both below 8x bar. Based on single Nigerian RCT (Okeke & Abubakar 2020, n=10,852). Most optimistic BOTEC scenario (with neonatal mortality adjustment + leverage) gives 4.4x. Afya trial in Kenya (2022) found CCTs for maternal health not cost-effective (INT$1,035 per additional ANC visit). No new RCTs with mortality outcomes. New Incentives demonstrates CCTs work for immunization (9-38x) but different mechanism. Costs highly uncertain ($85/woman for full package).

### QEA 11: Antenatal corticosteroids (ACS) for preterm birth — COMPLETE

- Original QEA: https://docs.google.com/document/d/1bPXDLhRKFxWvHiS0tLjhxzUGUJ75pg4EtUk89Md9dvk/
- Original BOTEC: https://docs.google.com/spreadsheets/d/11mTRJz38hbuohmhFaTSCtTWAdDRxngwP3zavAZP2wrY/
- Year: 2020 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/antenatal_corticosteroids_preterm_birth.md`
  - `outputs/botecs/antenatal_corticosteroids_preterm_birth.xlsx`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 8 citations)
- Key notes: Evidence has shifted dramatically. The original QEA said "Postpone" pending trial results from follow-up to the ACT trial (which showed harm). The WHO ACTION-I trial (NEJM 2020, n=2,852 across 5 LMICs) found ACS reduced neonatal death by 16% (RR 0.84; 95% CI 0.72-0.97) when properly targeted in hospital settings. WHO updated guidelines in 2022. Cost-saving in all 5 trial countries. But implementation gap is massive (~10% of facilities provide ACS). CE at $30/woman: ~14x; at $100/woman: ~6x. Program implementation cost is the pivotal unknown. No clear philanthropic implementer or at-scale program. ACTION-III (late preterm, expected ~2027) could triple eligible population.

### QEA 12: Rabies dog vaccination (MDV + PEP) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1XF_7oeNT1CEZpqOf_Gh5PSgWH9CGWts2dxLAVeQuZLY/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1xhZNL7D7SwveYrzctyN3c2MyxqLKIlhC-DYUTuhHwGY/
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: Original CE ~9x average over 13 years, but heavily back-loaded (Phase I: ~3x, Phase III: ~11x). No RCTs — evidence entirely from models and retrospective evaluations. Major update: GAVI announced PEP support in 50+ countries (June 2024), reducing early-year costs by ~60%. 2023 Nature Communications analysis confirms $9.5B welfare gains from coordinated African vaccination. But still no experimental evidence, 13-year commitment required, Phase I CE remains marginal, and Zero by 30 progress is slow. RFMF has decreased with GAVI/GARC/WHO activity. Per-dog costs may be lower than assumed ($2.70-2.85 vs $4.43).

---

**Batch 3 complete (QEAs 10–12). One rated Low (ANC CCTs), one rated Medium (ACS for preterm birth), one rated Low (rabies). Session should be refreshed before batch 4 (QEA 13: LPG cookstoves + summary update).**

## Session: 2026-03-18 (batch 4 of 4: QEA 13 + final tasks)

### QEA 13: LPG cookstoves — COMPLETE

- Original QEA: https://docs.google.com/document/d/18gRBcs9KDaYal6H4YLrUAdj7staiQOi7g4hsPeALNhw/ (inaccessible — Google auth expired during session)
- Original BOTEC: https://docs.google.com/spreadsheets/d/1DWZtnJcsFqE8baA3NnH1FHMps4donbgJrFyLbs2YA3o/ (inaccessible — same)
- Year: 2022 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: Two large RCTs have definitively shown that LPG cookstove interventions do not reduce child health outcomes. The HAPIN trial (NEJM 2024, n=3,200 across Guatemala/India/Peru/Rwanda) found no effect on severe infant pneumonia, birthweight, or stunting. The GRAPHS trial (Ghana) similarly found no significant effects. GiveWell has independently investigated clean cookstoves and concluded it is not a priority program. Implementation barriers include low adoption, inadequate air quality improvements (PM2.5 still above WHO standards even with LPG), and low sustained usage. No plausible pathway to CE.

---

**All 13 QEAs complete (3 original + 10 new). Final summary: H=1, M=4, L=8.**
