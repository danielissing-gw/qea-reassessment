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

**Tally after 33 QEAs: H=1, M=6, L=26.**

---

## Session: 2026-03-18 (batch 10: QEAs 34–36 from updated master list)

Master list updated with 9 new QEAs (8 new + 1 duplicate of QEA 9). Processing in batches of 3.

### QEA 34: Midwifery school support — COMPLETE

- Original QEA: https://docs.google.com/document/d/1Yv3Pz6MEYMgCEd2WoiSl710Bg1zONtEAMkYOrYiMpGo/
- Original BOTEC: https://docs.google.com/spreadsheets/d/13m0wqCbot8-GucjIWwqdEFGgFa6PDaAYUTESq0LE7hg/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: No new direct RCTs linking midwife training to mortality. Evidence gap from 2022 persists. WHO released midwifery models of care position paper (2024) and implementation guidance (2025) — policy signals, not clinical evidence. 2023 Morocco CBA found 16:1 BCR but LiST-based and implies ~$5,290/life saved (above GW bar). Africa midwife workforce nearly doubled 2013–2022 (173k→334k) but 750k shortage remains by 2030. Amref continues small-scale e-learning programs. No at-scale training program identified. Original CE ~5.3x (with leverage/funging) already below 8x bar.

### QEA 35: Manual water pumps for farming households — COMPLETE

- Original QEA: https://docs.google.com/document/d/1SxRXdCPb4RU31TpRLonyOHzG7Mhv6Ld8Gnd8WSpoiFU/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1qLK2QQdjQ3ucDfGcZuk1XjAlkXR0DyC5oSpgkH9O1cU/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Dyer & Shapiro study published in J Dev Econ (2023) — same results as working paper. Farm revenue +13% but offset by non-farm income loss → net negative. BOTEC: 1.7x (base), 4.2x (optimistic). No new RCTs on manual irrigation pumps. Solar irrigation gaining attention but different technology/price. Even optimistic 12yr lifespan scenario (5.6x) well below 8x bar.

### QEA 36: Genetically modified eggplants (Bt brinjal) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1Gz-tNr1rtvBwWhdc_H7-sa591J7C8bGHwCnrV9RZcS4/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1EwzC3O6h9qLF_0a0LWJ5S1FYreELU4v0W5-cZiCmayA/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: No new experimental evidence since Ahmed et al 2020. Bangladesh adoption declined from 11.9% peak (2021) to 5.3% (2023). Philippines approved 2022 but Court of Appeals cease-and-desist April 2024. India moratorium remains. USAID primary funder ($10M to Cornell/IREP). CE at 3.1x well below 8x bar. No clear philanthropic funding gap.

---

**Batch 10 complete (QEAs 34–36). All three rated Low. Session should be refreshed before batch 11 (QEAs 37–39).**

## Session: 2026-03-18 (batch 11: QEAs 37–39)

### QEA 37: Commodity acquisition for iCCM (ORS/zinc + amoxicillin) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1xISuSRUyaFdKanjkafHhqiOd68Nv8dHhhtD4vs9r5-Q/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1OHxvt_Jf9zwrzSoiKAH0G57N1IENi47OeTUwOO0SN-A/
- Year: 2022 | Rating: **Low** (already being pursued by GiveWell)
- Outputs: CSV row only
- Key notes: GiveWell has already validated and is funding this opportunity. CHAI received $8.07M (Sep 2023, increased) for ORS/zinc distribution in Bauchi, Nigeria (~1.5M children); GW estimates 17x cash (24x with RCT learning value). New Incentives received $4.8M (Oct 2024) for ORS/zinc alongside immunization. Clear Solutions pilot in Kano (Dec 2023). Active RCT measuring ORS usage impact; results expected mid-to-late 2025. The original QEA correctly identified the opportunity at 14x — close to GW's current 17x estimate. Notable success: one of the most validated QEA predictions across the entire set.

### QEA 38: Deworming pregnant people — COMPLETE

- Original QEA: https://docs.google.com/document/d/12O-jMYm3VNWHQyVfxt1MohJDt0mf0OwU0C--SrtgKEg/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1bvZSJpvLzeZEPKygUtrwIJA5AjNjab5TFmlA9t-Kb5A/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: No new RCTs since 2021 Cochrane review. Standalone CE (2-7x) below bar. Add-on scenario (28x at $0.10) attractive in theory but no implementer identified. Evidence Action pursued maternal syphilis in Liberia (exit grant April 2024) and expanded to Zambia/Cameroon but did not add deworming. A 2021 retrospective cohort found 14% NMR reduction from deworming during ANC but observational. The add-on question is operational, not evidence-based — needs a delivery platform to test.

### QEA 39: Unconditional cash transfers for pregnant people — COMPLETE

- Original QEA: https://docs.google.com/document/d/1EQPNi3lhr43O45jtDIoAVV4y0jWGNgqHaBft-4yCU_I/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1DYv4ASblHkUsEDfXiZxI8uzfzu6NR3onwikbPx7mfsg/
- Year: 2022 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Original CE ~1.7x. Major new evidence: 2025 Kenya GiveDirectly study (107,000+ births) found $1,000 UCT reduced infant mortality by 48%, neonatal by 63%. But this primarily raises GiveDirectly's baseline CEA (the comparison denominator), not the targeted pregnancy program's relative advantage. The original QEA predicted this: targeted UCTs would look even less relatively attractive if untargeted UCTs show mortality effects. Muralidharan India RCT (J-PAL) on UCTs for pregnant/lactating mothers still unpublished. Not worth revisiting.

---

**Batch 11 complete (QEAs 37–39). All three rated Low (though QEA 37 was a validated prediction — GiveWell already acting at 17x). Session should be refreshed before batch 12 (QEAs 40–41).**

## Session: 2026-03-18 (batch 12: QEAs 40–41 — final batch)

### QEA 40: Generic hepatitis C medication — COMPLETE

- Original QEA: https://docs.google.com/document/d/1nYKc4F4mjVW9eMHwir22CG0NEuSzNiMGvatpZaKp-vY/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1EXKFtx_KrmGrHIEG1E_U2XOBYXLo6XZrp1DTuVwOLKk/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Generic DAA prices continue falling ($39 India, $60 Rwanda vs $87-112 original). VIETNARMS trial (2024) validates cheapest regimen (SOF/DCV). WHO 2030 elimination targets off track. Even at $60/person, CE only ~2x in high-burden countries. Structural constraint: deaths concentrated in 60-69 age group (MW=54) + low annual mortality rate per infected person (~1%). Would need $15/person for 8x — not achievable.

### QEA 41: Antiviral procurement for COVID-19 — COMPLETE

- Original QEA: No writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1JojKTTfOeNRGFb9fM6jIkI9f97Ro4YMRGF2zLjvIS08/
- Year: 2022 | Rating: **Low** (obsolete)
- Outputs: CSV row only
- Key notes: Intervention is essentially obsolete. COVID emergency ended May 2023; populations have natural/vaccine immunity; mortality plummeted. Original BOTEC assumed pandemic-era conditions (4x death multiplier, high CFRs, no immunity) that no longer hold. 2023 Ghana/Rwanda/Zambia CEA found neither antiviral cost-effective for general adult population. UK PANORAMIC trial found molnupiravir ineffective in vaccinated populations. African governments largely declined to procure. Generic Paxlovid available under $25/course but demand minimal.

---

**Batch 12 complete (QEAs 40–41). Both rated Low. All 41 QEAs from both master lists are now complete.**

**FINAL TALLY: H=1, M=6, L=34 (+ 1 duplicate skipped).**

| Rating | Count | Interventions |
|--------|-------|---------------|
| High | 1 | Rheumatic heart disease prevention |
| Medium | 6 | Uterotonics for PPH, Oral azithromycin during labor, Antenatal corticosteroids for preterm birth, Non-pneumatic anti-shock garment (NASG), Sayana Press injectable contraceptive, MMS during pregnancy |
| Low | 34 | All others (including 1 already being pursued by GiveWell: iCCM commodity provision; and 1 obsolete: COVID antivirals) |

### Notable patterns from the expanded list (QEAs 34–41):
- **iCCM commodity provision (QEA 37)** was the standout: the original QEA correctly estimated 14x, and GiveWell is now funding the opportunity at an estimated 17x. Validates the QEA process.
- **Agriculture/income interventions** (water pumps, GM eggplants) consistently fall below bar due to the income-to-UoV conversion lacking a mortality channel.
- **Targeting UCTs to pregnant women** shows only modest incremental benefit over untargeted cash (~1.7x), even as the 2025 Kenya study demonstrates large mortality effects from untargeted UCTs.
- **Pandemic-era interventions** (COVID antivirals) are time-sensitive and can become obsolete rapidly.

## Session: 2026-03-18 (batch 13: QEAs 42–44 from updated master list)

Master list updated with 10 new QEAs. Processing in batches of 3.

### QEA 42: Community-based antibiotic delivery for PSBI management — COMPLETE

- Original QEA: https://docs.google.com/document/d/1yZaMJLCNuMrMuORVv88LQsRuRC9zAyVjRxYpt4nSenc/
- Original BOTEC: None (no BOTEC)
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Brief 2020 note said 4/5 Cochrane studies bundled antibiotics with other interventions; one standalone trial found no effect. Since then: WHO published comprehensive SBI guidelines (Dec 2024, 11 recommendations). Lancet Global Health 2025 RCT (n=7,001, 6 LMICs) showed outpatient non-inferior to inpatient for low-risk PSBI (7.7% vs 7.8% poor outcomes; significantly lower mortality in outpatient: 0.3% vs 0.7%). Treatment costs $20-43/infant; Ethiopia model $223/DALY averted. But CE by GW standards only ~2-4x. Program requires daily IM injections for 7 days. Space well-funded by WHO/UNICEF under ENAP. AMR growing concern.

### QEA 43: Lymphoedema management to prevent ADLA in podoconiosis — COMPLETE

- Original QEA: No writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1Fk84QD_Sj-jzE6PHyi6hoHMduDZeyxykEFjgOL1O0zQ/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Consumption-based model from GoLBeT RCT (Negussie et al 2018). Lymphoedema management reduced ALA incidence 19% (IRR 0.81). At $50/person/year, CE = 1.7x GD. No mortality channel — morbidity/income only. ~4M people affected globally. EnDPoINT study (2025) showed integrated NTD care effective. WHO NTD Roadmap includes podoconiosis. But income-to-UoV conversion inherently limits CE; gap from 1.7x to 8x unbridgeable.

### QEA 44: Cryptococcal antigen testing for people living with HIV — COMPLETE

- Original QEA: No writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1eg10obinxlz_gyN5WO6TDhoAclpL9vR2Yp3LePxrOsE/
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: BOTEC showed 27x (range 5-41x) but used 100 UoV per death averted — too high for adult HIV patients (~35 UoV appropriate). With corrected moral weights, CE drops to ~8-10x central, ~2x pessimistic. Cost per death averted $1,243. AMBITION trial (NEJM 2022) simplified CM treatment to single-dose liposomal amphotericin B. CrAg screening uptake only 57% in Africa. But space dominated by PEPFAR/Global Fund ($6.7B+/year). Target population (CD4<100) shrinking with ART expansion. PEPFAR 2025 freeze creates uncertainty but GW would be marginal funder.

---

**Batch 13 complete (QEAs 42–44). All three rated Low. Session should be refreshed before batch 14 (QEAs 45–47: oxygen therapy, statins/polypill, arsenic in wells).**

## Session: 2026-03-18 (batch 14: QEAs 45–47)

### QEA 45: Oxygen therapy for children — COMPLETE

- Original QEA: https://docs.google.com/document/d/1daY7xgIBgTYEzQSSC5AzOdxnqqiPKAcvHyow-TvJvzU/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1163LXJ5FhMT3DWjhJb4IKdHnuEOWNnTlIrkYaLv8jJE/
- Year: 2021 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/oxygen_therapy_for_children.md`
  - `outputs/botecs/oxygen_therapy_for_children.xlsx`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 8 citations)
- Key notes: Evidence dramatically strengthened since 2021. The Uganda stepped-wedge RCT (Lancet 2024, n=2,405 hypoxaemic children) is the first randomized trial demonstrating mortality benefit from improving oxygen access — 48.7% reduction in fatal outcomes (adjusted RR 0.51). Consistent with Lam et al. 2021 systematic review (pooled OR 0.52). Lancet Global Health Oxygen Commission (Feb 2025) documents massive unmet need: 70% oxygen coverage gap in LMICs, only 9% in SSA. Cost-effectiveness highly favorable ($25-62/DALY averted across multiple analyses). TIMCI trial (2025) shows primary care pulse oximetry alone doesn't reduce mortality without hospital strengthening — full ecosystem needed. CE: ~10x at $30/patient (range 6x at $50 to 20x at $15). RFMF uncertain: CHAI ($100M), Unitaid ($22M), Global Fund all active, but US aid cuts creating new gaps. 88% of needed $34B remains unfunded.

### QEA 46: Statins and/or polypill for CVD — COMPLETE

- Original QEA: https://docs.google.com/document/d/1JJT4ZL8xM2bA8LRbbXRuSDoyRRHrk5raUhZxYyxZLZs/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1__LEGsfKO0gLH2Zunved56ba-8f0Sed7_GHu3XpwqnM/
- Year: 2021 | Rating: **Low**
- Outputs:
  - CSV row only (Low rating)
- Key notes: WHO added polypills to Essential Medicines List (July 2023) — landmark policy milestone. SECURE trial (NEJM 2022) found 24% MACE reduction in secondary prevention but European-only. 2025 meta-analysis (30 studies, 35,833 participants): MACE RR 0.78, CV death RR 0.75, all-cause mortality RR 0.88. But CE still only ~1-3x by GW standards. Fundamental constraints: chronic daily medication at $128/year in LMICs (ICER $5,767/QALY — an order of magnitude above GW bar); CVD deaths mainly in elderly (low MW); no large-scale primary prevention program ever implemented despite WHO EML; zero public pharmacy availability even in countries with market authorization; no implementer.

### QEA 47: Arsenic in wells (Bangladesh) — COMPLETE

- Original QEA: No writeup exists
- Original BOTEC: https://docs.google.com/spreadsheets/d/1ATbZ61dmczX3GB3Mo-nwITfsMcTikpGmlzG-D83xu5Y/
- Year: 2021 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/arsenic_in_wells.md`
  - `outputs/botecs/arsenic_in_wells.xlsx`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 11 citations)
- Key notes: HEALS 20-year follow-up (JAMA 2025, n=10,977, 1,401 chronic disease deaths) provides strongest evidence yet that reducing arsenic exposure causally reduces mortality — 54% lower chronic disease mortality for those switching from high to low exposure. Original BOTEC's 18.4x was inflated by high moral weights (106 UoV for adults vs. GW standard ~50); with corrected MW, CE drops to ~8x at $5/well. Well-switching rates consistently higher than the original 35% (studies show 37-60%). Benefits persist 8-15 years (original assumed 5). Space is remarkably neglected — no major international programs despite 20M Bangladeshis still exposed to >50 ug/L. Key blockers: no implementer identified (Columbia University research group is main actor); all evidence observational (no mortality RCT); program cost uncertain ($3-10/well). If costs are $3-4/well (plausible via BRAC integration), CE rises to 10-13x.

---

**Batch 14 complete (QEAs 45–47). One rated Low (polypill), two rated Medium (oxygen therapy, arsenic in wells). Next: batch 15 (QEAs 48–50: aspirin for AMI, prophylactic antibiotics for C-sections, eggs for complementary feeding).**

## Session: 2026-03-18 (batch 15: QEAs 48–50)

### QEA 48: Aspirin for acute myocardial infarction — COMPLETE

- Original QEA: https://docs.google.com/document/d/1vBv06CaLAM3zHacROcn8BLfpsc24bxHE_XEVpDFljvk/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1_cmqFfA7U3HyXAfd5GBI8Lc2-qXs7ZesrPUxJPk3YFA/
- Year: 2021 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Original CE 3.8x, well below 8x bar. No new placebo-controlled RCTs — ~10% mortality reduction (ATT 2009) remains best estimate. 2023 JAMA study confirms massive aspirin underuse in LMICs (16.6% in LICs, 24.5% in LMICs) but this is an implementation gap, not a CE improvement. WHO added polypill to EML (2023). HEARTS initiative expanding but hypertension-focused. Drug cost trivial (~$0.08/day) but health system infrastructure for post-MI patient identification/retention is the real cost. Adult CVD deaths get low moral weight (~30 UoV). No implementer. CE arithmetic unchanged.

### QEA 49: Prophylactic antibiotics to reduce infections from caesarian sections — COMPLETE

- Original QEA: No writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1TqR7MmPN8QBKcHg_NnxhSZhzQz-U5rLlTE7qcBKiN1c/
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Original CE of 10.6x is substantially overstated. The BOTEC assumed zero counterfactual prophylaxis coverage, but WHO Multicountry Survey finds ~87% of C-sections globally already receive antibiotics. Adjusting for ~60% counterfactual coverage in target SSA areas reduces CE to ~3-5x. Additional concerns: MW 113 is at the upper end for maternal deaths; $5/patient is a guess (drug cost <$1-2); the intervention is about health system quality improvement not drug distribution; growing AMR concerns. Cochrane review (2014, 95 studies) not updated but evidence base solid. C-section rates rising in LMICs (33.5M/year projected by 2030). WHO 2021 guideline confirms single-dose cephalosporin. No clear philanthropic entry point.

### QEA 50: Eggs for early complementary feeding — COMPLETE

- Original QEA: No writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1N8wVlL_UL2On7ZekWvCx8siOjf01N8ifJ4pwNKFaZEE/
- Year: 2020 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Evidence has actually weakened. The Ecuador Lulun effect (0.63 SD HAZ) completely disappeared at 2-year follow-up (Iannotti 2020) — both groups at -2.07 HAZ with 50% stunting. WHO pooled estimate for egg-specific HAZ effect is only 0.06 SD (95% CI -0.10 to 0.22) — not significant and dramatically lower than the 0.35 SD in the original BOTEC. Burkina Faso trial found no stunting effect. Malawi near zero (0.07 SD). Using updated WHO estimate would reduce CE by ~83% below the already-low 1.63x. The 40-year earnings pathway (87% of BOTEC value) is not defensible if height gains don't persist. SQ-LNS offers much stronger evidence at comparable costs. No implementer doing egg supplementation at scale.

---

**Batch 15 complete (QEAs 48–50). All three rated Low. Processing final QEA (51: MDR-TB treatment) in same session.**

### QEA 51: Treatment for multi-drug resistant TB — COMPLETE

- Original QEA: https://docs.google.com/document/d/1Hx5Z7Me6qidxQnohv38Eor-ZKez4opc9zEgD2NTMkII/
- Original BOTEC: None (no BOTEC produced — evidence too thin)
- Year: 2017 | Rating: **Medium**
- Outputs:
  - `outputs/writeups/mdr_tb_treatment.md`
  - `outputs/botecs/mdr_tb_treatment.xlsx`
  - `outputs/botecs/mdr_tb_treatment.csv`
  - Row appended to tracker CSV
  - QA: **PASS** (0 errors, 12 citations)
- Key notes: The evidence gap that blocked the 2017 assessment has been comprehensively resolved. Multiple Phase 3 RCTs now demonstrate ~89-91% treatment success with BPaLM (6-month, all-oral): TB-PRACTECAL (Lancet Resp Med 2023, 89%), endTB (NEJM 2024, 90.4%), Nix-TB (NEJM 2020, 90%), ZeNix (NEJM 2022, 91%), STREAM Stage 2 (Lancet 2022, 91%). This replaces 18-24 month injectable regimens that had ~60% success. Drug costs dropped from $1,000+ to $310/course (BPaLM via Global Drug Facility). Total treatment costs: $996-$2,573 across 4 LMICs. 2025 US funding cuts creating acute gap (Global Fund cut $1.4B; USAID effectively ceased). 400,000 new cases/year, only 44% diagnosed/treated, ~150,000 deaths/year. CE at full programmatic cost ($1,500/patient) is only ~3x — below 8x bar. But at drug procurement cost ($310/patient, filling stockouts from US cuts), CE reaches ~15x. The pivotal question is whether there's a specific philanthropic entry point at the lower cost point.

---

**ALL 51 QEAs FROM THE MASTER LIST ARE NOW COMPLETE.**

**FINAL TALLY: H=1, M=9, L=41.**

| Rating | Count | Interventions |
|--------|-------|---------------|
| High | 1 | Rheumatic heart disease prevention |
| Medium | 9 | Uterotonics for PPH, Oral azithromycin during labor, Antenatal corticosteroids for preterm birth, Non-pneumatic anti-shock garment (NASG), Sayana Press injectable contraceptive, MMS during pregnancy, Oxygen therapy for children, Arsenic in wells (Bangladesh), MDR-TB treatment |
| Low | 41 | All others (including 1 already being pursued by GiveWell: iCCM commodity provision; 1 obsolete: COVID antivirals) |

### Notable patterns from the complete set:

- **Maternal/neonatal health cluster:** 5 of 9 Medium/High interventions are maternal or neonatal (uterotonics, azithromycin in labor, ACS for preterm birth, NASG, MMS). This is GiveWell's strongest domain for finding new opportunities.
- **Evidence transformations:** MDR-TB treatment went from "no BOTEC possible" to a fully modeled opportunity, driven by 5+ Phase 3 RCTs. Oxygen therapy for children gained its first mortality RCT. Arsenic in wells gained 20-year longitudinal evidence.
- **Funding crises create opportunities:** The 2025 US aid cuts may have created time-limited high-leverage opportunities in MDR-TB treatment (and potentially other Global Fund-dependent programs).
- **Moral weight is the key structural constraint for NCD interventions:** Aspirin for AMI (3.8x), polypill (1-3x), salt substitution (2-4x), and hepatitis C (0.5-2x) all have strong evidence but fail the CE bar because adult/elderly CVD deaths get low moral weights.
- **One validated prediction:** The iCCM commodity provision QEA (2022, estimated 14x) was validated by GiveWell's own investigation (estimated 17x) and subsequent $8M+ grant to CHAI. This suggests the QEA process can identify real opportunities.
- **Contraception is a new frontier:** Sayana Press (~13x) benefited from GiveWell's 2025 contraception valuation framework (0.7 UoV/woman-year). This resolved the key blocker for multiple family planning interventions.

## Session: 2026-03-18 (batch 16: QEAs 52–54 from final master list update)

Master list updated with 9 new QEAs. Processing in batches of 3.

### QEA 52: Conditional incentives to avert child marriage — COMPLETE

- Original QEA: https://docs.google.com/document/d/1--EsY5hThHBVDGki1ouLuTwEGWCnrWKAcyeqz6gQ3Uo/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1pYDMl5FAqRAvv4S42uPggiw3OWwI7RrfXssKsMRL7jE/
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Study published as Buchmann et al. 2023 in AER. Program gave $16/year cooking oil to delay marriage in rural Bangladesh. CE at 3.2x driven by consumption benefits and subjective child-marriage-averted valuation. No new RCTs. UNICEF reports child marriage declining globally but 12M girls/year still affected. CE far below 8x bar; no mortality channel; uncertain moral weight for child marriage; Bangladesh-specific.

### QEA 53: Schizophrenia antipsychotics or community-based care — COMPLETE

- Original QEA: no writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1vZVk9lUPhhCxHvaeSknBY-7yE1vXrfMKnndaDW0Q-Zk/
- Year: 2019 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Based on BasicNeeds model. CE at 1.2x ($721/DALY, 1.48 DALYs/patient at $1,067 cost). GBD 2021: 14.8M DALYs but zero attributed deaths. No new large LMIC RCTs. SAMARTH project (2025-2030) testing digital psychosocial rehab in India but results years away. An order of magnitude below 8x bar; no mortality channel; unresolved mental health moral weights.

### QEA 54: CBT and interpersonal therapy (StrongMinds) — COMPLETE

- Original QEA: https://docs.google.com/document/d/1K4W4vU8si5-ardbh7EShd81C5gqXC3U0ygXXaFXlG2k/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1-lCC1zQHVZlJS8f9OfqhzcZTetHMxuMkW7nT75QDGhk/ (DRK check-in, not a proper BOTEC)
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: StrongMinds cost dropped from ~$200 to $23/person; scale up to 426k clients/year (2024). HLI estimates 5.3x GD. GiveWell 2023 assessment: ~25% of marginal opportunities (~2-2.5x cash). Moral weight debate is the binding constraint. Even with 10x cost reduction, GW's framework puts this well below 8x bar.

---

**Batch 16 complete (QEAs 52–54). All three rated Low. Continuing with batch 17 (QEAs 55–57).**

### QEA 55: Synbiotics to prevent neonatal sepsis — COMPLETE

- Original QEA: no writeup
- Original BOTEC: https://docs.google.com/spreadsheets/d/1zbPI3isnMJjYX2ANqpIuCxf1olE4zbSOJ6gkNHpEVMg/
- Year: 2018 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Based on Panigrahi et al. 2017 (Nature, n=4,556, rural India). RR 0.6 for death/sepsis at $2/course. CE ~14x at 5% CFR but CFR is a guess. No replication after 8 years despite Nature publication — strong negative signal. Corrigendum published. No WHO recommendation for this synbiotic. Safety concerns with probiotics in neonates.

### QEA 56: Adolescent pregnancy prevention interventions — COMPLETE

- Original QEA: https://docs.google.com/document/d/1JlpTKkc7duc9PPIVS3yZfWTKKSRkwXL7NTv108RFSTY/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1G87GUhIeHZ7DnKe0zlMepD09gGlBdRzVoAmLUBLNZVs/
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: $2,000-3,000/pregnancy averted via CCTs or community programs. Now rendered obsolete by Sayana Press (~$17/pregnancy averted, 13x). Direct contraception provision is 40-170x cheaper per pregnancy averted than indirect approaches. GW's 2025 contraception framework makes the comparison even starker.

### QEA 57: Rural electrification — COMPLETE

- Original QEA: https://docs.google.com/document/d/19Yn54dyNZp0xjeX7LeKt0OoQ2b5qaMtkcLMdiFeb45g/
- Original BOTEC: none
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Infrastructure intervention with no mortality channel. Minigrids have scaled (11M connections, SSA electrification 17%→28%) but costs remain high ($300-1,000+/household). Income gains documented (50%+ increases) but income-to-UoV conversion yields ~1-2x by GW standards. Massive MDB/government funding. Not GW's domain.

---

**Batch 17 complete (QEAs 55–57). All three rated Low. Continuing with batch 18 (QEAs 58–60).**

### QEA 58: Broad behavior change program for adolescent girls in India (Saloni) — COMPLETE

- Original QEA: https://drive.google.com/open?id=1NG69Pjt3pQcWyvb76NZKfAJuATPWvm-shUkhDGowKVI
- Original BOTEC: none (no cost data)
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Single flawed RCT (Kapadia-Kundu 2014) with self-reported outcomes, baseline imbalances, and atypical events. No cost data. Program apparently discontinued after 2015. Nothing to revisit.

### QEA 59: CCTs to reduce deforestation (PES) — COMPLETE

- Original QEA: https://docs.google.com/document/d/123bGrnBYtGpxL20PTWeerjyPZhJzqAE1k39RwfyAxV0/
- Original BOTEC: none
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Jayachandran et al. 2017 (Science) showed 50% less deforestation at $2.60/tonne CO2. Follow-up found effects disappeared 4 years after program ended (permanent delay but not permanent behavior change). But this is a climate/environment intervention with no health/mortality channel — outside GW's framework entirely.

### QEA 60: Snakebite antivenom — COMPLETE

- Original QEA: https://docs.google.com/document/d/1bxP6BzMji2EB7lUPcuUfN-3ExHUW7A9--n5ZY4wrMPs/
- Original BOTEC: https://docs.google.com/spreadsheets/d/1OpO3mS4kzewYfvKynwaIe37q5yoKRKgkkwWvoH0S8D0/
- Year: 2017 | Rating: **Low**
- Outputs: CSV row only
- Key notes: Original CE 0.7-0.9x. WHO launched snakebite strategy (2019), Wellcome committed $100M. West African CEA found $83-281/DALY averted — better than original but still 2-9x under various assumptions. Next-gen recombinant antivenoms in development at 30+ institutions but years from market. Space now much better funded.

---

**Batch 18 complete (QEAs 58–60). All three rated Low.**

---

## ALL 60 QEAs FROM ALL MASTER LISTS NOW COMPLETE.

**FINAL TALLY: H=1, M=9, L=50.**

| Rating | Count | Interventions |
|--------|-------|---------------|
| High | 1 | Rheumatic heart disease prevention |
| Medium | 9 | Uterotonics for PPH, Oral azithromycin during labor, Antenatal corticosteroids for preterm birth, Non-pneumatic anti-shock garment (NASG), Sayana Press injectable contraceptive, MMS during pregnancy, Oxygen therapy for children, Arsenic in wells (Bangladesh), MDR-TB treatment |
| Low | 50 | All others |

### Notable patterns from the final 9 QEAs (52–60):

- **Moral weight constraints dominate:** Child marriage CCTs (3.2x), schizophrenia (1.2x), and StrongMinds/CBT (0.5-2.5x) all face the same structural constraint — GW has no standard moral weight for non-mortality outcomes (averting child marriage, mental health improvement). GW's 2023 StrongMinds assessment (~25% of marginal) makes this explicit.
- **Domain mismatch:** Three interventions (rural electrification, deforestation PES, adolescent behavior change) are outside GW's health-focused framework entirely. PES is a climate intervention; electrification is infrastructure; Saloni was a defunct school-based program.
- **Single-trial fragility:** Synbiotics (Panigrahi 2017) had a striking Nature result (RR 0.6) but no replication in 8 years — a strong negative signal. Similarly, the Saloni program had a single flawed RCT.
- **Snakebite as future potential:** Of the 9, snakebite antivenom has the most potential for future reassessment — next-gen recombinant antivenoms could dramatically cut costs, but are still years from deployment.
- **Adolescent pregnancy made redundant:** GW's 2025 contraception framework and Sayana Press at 13x make indirect pregnancy prevention via CCTs (~$3,000/pregnancy) obsolete as a GW-relevant intervention.

## Session: 2026-04-06

### Ad-hoc: Oxygen therapy for children — BOTEC REVISED

- Corrected moral weights (52.5 → 117 for children, 30 → 100 for adults) per GW's 2020 moral weights tool
- Increased cost per patient from $30 to $45 (total program cost, triangulated across multiple sources)
- New CE: ~15x at $45/patient (was 9.8x at $30/patient)
- Also created `docs/moral_weights.md` as local reference and updated `docs/methodology.md`

### Ad-hoc: Sickle cell disease screening and treatment — NEW ASSESSMENT

- Source: CHAI memo and BOTEC (July 2023, internal); no formal QEA
- Rating: **Medium**
- Outputs:
  - Writeup: `outputs/writeups/sickle_cell_disease.md`
  - BOTEC: `outputs/botecs/sickle_cell_disease.xlsx` / `.csv`
  - QA: PASS (1 expected warning — no QEA doc links for internal-only source)
- Key finding: CE ~3x with sustainability discount, ~6x face value, up to ~10x in treatment-only + lifelong access scenario. The sustainability issue (SCD is lifelong; program covers 0-5 only) is the dominant uncertainty. HU is now the only oral therapy (crizanlizumab and voxelotor withdrawn). WHO added HU to core EML + Children's EML (2025). No RCT exists — evidence still rests on REACH pre-post trial.
