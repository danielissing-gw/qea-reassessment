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

**Batches 1-4 complete (13 QEAs). Continuing with 9 additional QEAs from updated master list.**

## Session: 2026-03-18 (batch 5: QEAs 14–22 from expanded master list)

### QEA 14: Selenium supplementation for neonatal sepsis prevention — COMPLETE

- Original QEA: https://docs.google.com/document/d/1nnOiyVRr6-5QK4AnJ3cwIQOow8t7jzGIsYAloPw29vw/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1uFGPEd8eyJ3i6gPhTSuOYn6ZsccAGa7wWK48HpMK3gY/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: No new LMIC trials since Aggarwal 2016 (n=90). Cochrane review unchanged. Pooled RR 0.73 for sepsis episodes but not powered for mortality. No WHO recommendation. Gates research never materialized. CE at pooled estimate ($3/infant): ~5x.

### QEA 15: Radio campaigns for family planning (DMI) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1I1rGlx8uylSlFOencf-m3ME-JkVStRRUuoNNN9MMTas/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1coZGED1o1jnNJQJZIuh-pis8y_E7BeXWkVwCKQ_tnAg/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: CE 2.7-5.3x after adjustments, below 8x bar even at optimistic 2-year duration (~7.1x in Niger). GiveWell funded FEM RCT in Nigeria ($500k, March 2023); trial started mid-2024, no results yet. DMI scaled to 39 stations in Burkina Faso. CYP moral weight (0.67) would need >50% increase to approach bar.

### QEA 16: Cleft lip/palate surgery — COMPLETE

- Original QEA: https://docs.google.com/document/d/1lNSEBH_XURFiLJJZ8v_D361IdVrMki1EUTpzJif60V0/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1L5_0ui-mEGRW-0GgN4x5b9xXHO_n2uohngepJvLb7gU/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: CE at 3x (general), below bar. Severe-only (9x) faces ethical barriers. No new RCTs since Wydick 2020. Rural Kenya costs as low as $201 (vs $540) but uncertain. 93% of value from YLDs averted.

### QEA 17: HIV self-testing — COMPLETE

- Original QEA: https://docs.google.com/document/d/1-sjmWfafnZIUp2GEFzJS5XHaGEk_2YoKCzp-PSH49p0/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1rmHAC_ZL1RDH7NSn0pkxZ0xFbrawRW6VKiju-7yACqs/
- Year: 2018 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Space now massively funded by PEPFAR/Global Fund/UNITAID. WHO recommended since 2016 (updated 2022-23). Original CE of 10x explicitly excluded ART costs. Reduced neglectedness; GW comparative advantage limited.

### QEA 18: Non-pneumatic anti-shock garment (NASG) — COMPLETE

- Original QEA: https://docs.google.com/document/d/10ALE72O0VS6rkxrybbckYk_YBFNYAXnKdM0gAbobRBU/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1R9V-rtpUEtNRqoECtffF3y2PCvndTP0YNZpaswrtZak/
- Year: 2020 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/non_pneumatic_anti_shock_garment.md`
  - `outputs/botecs/non_pneumatic_anti_shock_garment.xlsx`
  - `outputs/botecs/non_pneumatic_anti_shock_garment.csv`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 11 citations)
- Key notes: CHAI Zimbabwe pilot (2019-2021) showed 50% fewer maternal deaths and zero PPH deaths across 34 facilities. Zimbabwe MOHCC adopted NASG for national rollout. Zambia also scaling (2023 process evaluation). CE ~10x at $12/woman (range 5-15x). Cost per woman is pivotal unknown. Complements E-MOTIVE PPH bundle and PPH uterotonics (HSC/TXA). Next step: get actual cost data from CHAI Zimbabwe.

### QEA 19: Adaptive education technology (Mindspark) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1cqPvh1kblakQkYzSxfe5UeCBQizV2tPG5rWz0tGMf50/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1SPToQYEqdlZMD2Gi-7HtUJJiANxQTsS1ZZaYEi5UMa4/
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: CE 2.2-9.1x depending on consumption estimation methodology. Scale-up showed lower effects (0.2 SD vs 0.37 SD) but also much lower costs (~$1.50/year vs $48/year). GW has no consensus on education-to-consumption methodology. India-focused; education not GW's primary domain.

### QEA 20: Drowning prevention (community daycare) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1cDOy--FY62-rPQ8179mqCoTF2Cm5A4yclk2WSnf0gi4/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1v4DRy2-q1DrKx0KORzwN8bGlhVAd3eKxKV7n30ngBeY/
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Bloomberg/Johns Hopkins PRECISE study now published. Crèche intervention reduced drowning 89% but costs $16/child/year — well above $2.50 breakeven. ICER: $17,008/life saved (~0.5x cash). Bangladesh government scaling with $32M program (2022). Not cost-effective by GW standards.

### QEA 21: Rape/sexual violence prevention (No Means No Worldwide) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1AYj52caPRcbTVbHR6uu2uOYmy5Z-okE4AckouApgxbo/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1ZSa7W5PWHTGAFNQsitc2kGSESYDhE4T7KcAZCweTpT0/
- Year: 2019 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Newer Kenya cluster-RCT (2016-2018, Prevention Science 2023) found null result (OR 1.21, p=0.63), contradicting earlier positive results. Validates methodological concerns from original QEA (experimenter demand effects). GW still has no moral weight for sexual violence prevention. Not worth revisiting.

### QEA 22: Antibiotic treatment of bacterial vaginosis in pregnancy — COMPLETE

- Original QEA: https://docs.google.com/document/d/1QgwzYYbrFfvO9EnT6gMdewYqMOUyJc4rM666LAKg1CQ/
- Original BOTEC: None (no BOTEC produced)
- Year: 2019 | Rating: **Low**
- Outputs: CSV row only
- Key notes: AuTop RCT (JAMA 2023, n=6,671) and Klebanoff 2023 IPD meta-analysis both confirm mass BV treatment doesn't prevent preterm birth. High-risk subgroup may benefit but not actionable in LMIC. Fundamental BV-PTB puzzle (association without treatment effect) persists.

---

**All 22 QEAs complete (13 original + 9 new). Final summary: H=1, M=5, L=16.**

## Session: 2026-03-18 (batch 6: QEAs 23–25 from expanded master list)

### QEA 23: Case finding and early treatment for leprosy — COMPLETE

- Original QEA: https://docs.google.com/document/d/1Ty85ryXokPQwkqmQ-bQR1al19LDr5MsDtla6E8te9Zo/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1a8GwQXE3TubI2w1Oe4RU4pQBaLfknaaGRcG_B5m-rcI/
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Leprosy is a morbidity-only disease with tiny global DALY burden (~30k DALYs/year) and near-zero mortality. GBD 2021 shows continued decline. Key new development is WHO-recommended SDR-PEP (single-dose rifampicin post-exposure prophylaxis): PEOPLE cluster-RCT (Lancet Global Health 2024) found IRR 0.55 (p=0.005); LPEP programme demonstrated feasibility in 7 countries. But even optimistic PEP scenarios yield only ~1-3x because no deaths to avert and disability weights are low (0.152). LepVax Phase 1b in Brazil (Oct 2024). Original BOTEC had #REF! errors.

### QEA 24: Striga control — COMPLETE

- Original QEA: https://docs.google.com/document/d/1vyEA8dM7tMrAuK2PLSuOQrAdxIsjX_Y35lQVU5BLIls/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1Ptd1McyTeRZhOEgyRzcsYr640kHh2eeNMHgDgyZKTEc/
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Agriculture/income intervention to control parasitic striga weed on maize in SSA. IITA ISMA evaluation showed 55% adoption and 46.8% income increase (non-randomized). Push-pull scaled to ~350k farmers across 18 countries by 2024. Striga-resistant maize breeding progressed but farm-level adoption low. Still no RCTs on program effectiveness. CE well below 8x — fundamentally limited by income-to-UoV conversion with no mortality channel.

### QEA 25: Pulse oximeter + safe surgery checklist training — COMPLETE

- Original QEA: https://docs.google.com/document/d/1T6Mdw8-ZAgVSIvUV_G1KZ4uRqQ3Mj_WB-Txg2r381-0/
- Original BOTEC: None (no BOTEC produced)
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Fundamental evidence gap not closed. Cochrane review still shows no RCT evidence of pulse oximetry reducing surgical mortality. SSC evidence improved somewhat (stepped-wedge cluster RCT; South Carolina DiD 22% mortality reduction; meta-analyses show 44% complication reduction). Lancet Global Health Oxygen Commission (2025) found 25% child death reduction with pulse oximetry + oxygen but for pneumonia broadly, not surgical use. Cost-effectiveness analysis ($115/DALY) depends on unverified 10% mortality assumption. Lifebox distributed 35k oximeters since 2011. Strong expert consensus but GW requires experimental evidence. Not GW's domain.

---

**Batch 6 complete (QEAs 23–25). All three rated Low. Session should be refreshed before batch 7 (QEAs 26–28).**

## Session: 2026-03-18 (batch 7: QEAs 26–28)

### QEA 26: Safe abortion (medical abortion provision) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1TUjzJfYK16FSnGkxxKRSzZahHt4Q7cYf_QkVT9QYGEY/
- Original BOTEC: N/A
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Evidence base strengthened (WHO 2022 recommends self-management of medical abortion for first time). But GW-internal blockers unchanged: (1) unresolved moral weight for safe abortion; (2) no program-level additionality evidence; (3) narrow mortality channel (CFR ~0.3-0.5%). CE could plausibly clear 8x in favorable scenarios but depends on methodological choices GW hasn't made. Not worth revisiting unless GW resolves its abortion moral weight framework.

### QEA 27: Sayana Press injectable contraceptive — COMPLETE

- Original QEA: https://docs.google.com/document/d/1LHkvhYKY3zfs8qBAxtbscRVarTHLxy850Wsd7Yorbeo/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1J-7saV7CfdhNt2VV0G9eQ8wB43oAe90_9oSinzCMgwo/
- Year: 2016 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/sayana_press.md`
  - `outputs/botecs/sayana_press.xlsx`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 9 citations)
- Key notes: GW published contraception valuation framework (April 2025): 0.7 UoV per woman-year. Self-injection approved in 35+ countries. Meta-analysis of 3 RCTs: self-injection increases 12-month continuation by 27% (RR 1.27). CE ~13x at $12/woman-year. Cost per woman-year is the pivotal unknown. GW is actively investigating family planning.

### QEA 28: Multi-micronutrient supplementation (MMS) during pregnancy — COMPLETE

- Original QEA: https://docs.google.com/document/d/1llIpGF1bVTQDmHM0RJ-lY0YcsA4FRpE_WuKb-ImReRk/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1uSnYDg1KZY1-iTQWuvBXZC4es7krjwPnYNH-bqxEgbg/
- Year: 2021 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/mms_during_pregnancy.md`
  - `outputs/botecs/mms_during_pregnancy.xlsx`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 13 citations)
- Key notes: WHO included UNIMMAP MMS on Essential Medicines List (2021). Kirk Humanitarian committed $125M, reached 75M women in 111 LMICs at $0.0118/dose. 2025 meta-analyses confirm benefits beyond birth: stunting (RR 0.86) and underweight (RR 0.86) through 24 months. Copenhagen Consensus 2023 named MMS one of 12 best investments. CE ~9x at $3/pregnancy (up from ~7x at $4 in original), driven by reduced commodity costs. Key uncertainties: programmatic costs and MW for LBW. TIME Best Inventions 2025.

---

**Batch 7 complete (QEAs 26–28). One rated Low (safe abortion), two rated Medium (Sayana Press, MMS). Next: batch 8 (QEAs 29–31) — large scale school feeding, community salt substitution, WASH for hospital infections.**

## Session: 2026-03-18 (batch 8: QEAs 29–31)

### QEA 29: Large scale school feeding programs — COMPLETE

- Original QEA: https://docs.google.com/document/d/1f_nZ1-DR2MIFYEkA_D5fQkJ231VbHUP8XOHjdOhWoqI/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1Ca5u32vXRj4seBPrYr1F_-RaECro-zD5Z-zvMG5qg_s/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: 2025 Cochrane review (40 studies, 91,885 students) confirms "modest but real" effects. New long-term evidence from China (+12.4% adult wages) is encouraging but external validity to SSA uncertain. Costs higher than assumed ($110/child/year in LICs vs $41 original). Space massively government-funded ($84B/year, 99% domestic). 466M children globally, 107 countries with national policies (up from 56 in 2020). GiveWell hasn't investigated. Minimal room for philanthropic impact.

### QEA 30: Community salt substitution — COMPLETE

- Original QEA: https://docs.google.com/document/d/16N0sNIZno43GAShIxIc6Rilkvk4LyGIxtdJ-ZlJ-5rk/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1qoO9JRFommavJPVS1LOl8j4dmbmsihV5NazGQUc_cwE/
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: SSaSS trial (NEJM 2021, n=20,995) found 14% stroke reduction, 13% MACE reduction, 12% all-cause mortality reduction — exactly the trial the original QEA was waiting for. WHO published first-ever salt substitution guideline (Jan 2025). 2024 meta-analysis: all-cause mortality RR 0.88. SSaSS CEA: cost-saving. Despite dramatic evidence improvement, CE by GW standards only rises to ~2-4x because (1) CVD deaths mainly in elderly (lower MW), (2) SSaSS population was high-risk (73% prior stroke), (3) Bloomberg/Resolve to Save Lives spending $215M already. Most evidence from China; generalizability limited.

### QEA 31: WASH to decrease hospital acquired infections — COMPLETE

- Original QEA: https://docs.google.com/document/d/1ZYTxQcvdOGT05dLKuNX1tPd9Kp4k48NHxXuCPqLJ-uk/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1DkPsdsL9AkFH6HVHR9cC98cblys59xHJlxG64GQ2xbs/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: APT-Sepsis trial (NEJM 2025, 59 facilities Malawi/Uganda, 431k births) found 32% reduction in severe maternal infection outcomes — strongest LMIC evidence to date. But APT-Sepsis is a broad IPC intervention (not just WASH). BASICS still has no published impact evaluation. WASH FIT has no rigorous evaluation despite billions invested. WHO 2024 IPC report estimates 3.5M annual HAI deaths, 821k avertable by 2050. Even applying APT-Sepsis effect size to the BOTEC only reaches ~7.6x in high-NNM countries. Strong policy momentum (UN GA resolution 2023) but no clear philanthropic entry point.

---

**Batch 8 complete (QEAs 29–31). All three rated Low. Next: batch 9 (QEAs 32–33) — digital tools for welfare programs, safe birth kits.**

## Session: 2026-03-18 (batch 9: QEAs 32–33)

### QEA 32: Digital tools to enhance take-up of welfare programs — COMPLETE

- Original QEA: https://docs.google.com/document/d/1BsbMrYxJ9x5yrTt2aW09dq9BPlXZ-TRiXGE9uQBMGpQ/
- Original BOTEC: https://docs.google.com/spreadsheets/d/15paqJucp56kORQo8HcSnjmMhDGz9ydo35VuXX5I2Qm0/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Evidence has weakened since 2022. DellaVigna & Linos (2022, Econometrica) found academic nudge effects 6x larger than at-scale (8.7pp vs 1.4pp across 126 RCTs, 23M individuals) — strongly suggesting the 12pp Blanco & Vargas effect wouldn't replicate. Hanna et al. (2024, REStat) found low enrollment may be due to low valuation, not information barriers. Page et al. (2023) found zero impact from national-scale FAFSA SMS nudges. J-PAL/CID 2024: information alone insufficient; enrollment assistance needed. No new direct RCT on SMS for welfare enrollment in LMICs. G2P infrastructure expanded (865M new accounts during COVID) but benefits digital delivery, not SMS nudges. CE likely ~1-3x.

### QEA 33: Safe birth kits — COMPLETE

- Original QEA: https://docs.google.com/document/d/15VAn_CD6v5sCNVapA1EDfJRIVUutndzaomaE5bEe5oY/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1_ej-0xGxLcHJqcyTl-RNx-KwKAE5Iwkj-6rhEFy_KAk/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Still no well-powered RCT showing mortality reduction from birth kits alone. Arowosegbe et al. 2023 (Nigeria cluster RCT, n=453) showed promising direction (neonatal infection RR 0.64) but underpowered (p=0.10). iNCK trial in Pakistan (~27k women) could be pivotal but results pending and tests bundled intervention. Gebeyehu et al. 2024 meta-analysis: CDK use associated with reduced mortality/sepsis but all observational evidence. Cost slightly favorable (JANMA kit ~$2.20 vs ~$10 original; iNCK CEA: $74/DALY averted). No new Cochrane review. WHO position unchanged. Trend toward facility-based care may shrink target population. CE ~2-4x, still well below 8x bar.

---

**Batch 9 complete (QEAs 32–33). Both rated Low. All 33 QEAs from the master list are now complete.**

**Final tally: H=1, M=6, L=26.**

| Rating | Count | Interventions |
|--------|-------|---------------|
| High | 1 | Rheumatic heart disease prevention |
| Medium | 6 | Uterotonics for PPH, Oral azithromycin during labor, Antenatal corticosteroids for preterm birth, Non-pneumatic anti-shock garment (NASG), Sayana Press injectable contraceptive, MMS during pregnancy |
| Low | 26 | All others |
