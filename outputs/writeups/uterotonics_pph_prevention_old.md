# Review: Uterotonics for Prevention/Treatment of Postpartum Hemorrhage QEA

**Link to original QEA:** https://docs.google.com/document/d/1euCoBUuJQ8V8l7Mgl5SFP6UpcT2H7BioX8uRxoohpoM/
**Link to original BOTEC:** https://docs.google.com/a/givewell.org/spreadsheets/d/1JL3dI9dS2MrtWsA1miIxMm1u9-3Bfbu-RYW7vWTYlGo/ (externally hosted; BOTEC was sparse — only one TXA cost row was visible)
**Year original analysis conducted:** 2017

---

## What is this (basic context)

- **Problem:** Postpartum hemorrhage (PPH — excessive bleeding after birth) causes roughly 25% of maternal deaths in LMICs, and is the single leading cause of maternal mortality globally. An estimated 300,000+ women die in childbirth each year, most from PPH.
- **Program:** The original QEA focused on misoprostol distribution (a cheap, heat-stable oral uterotonic) for PPH prevention in low-resource settings, particularly a PSI program in sub-Saharan Africa. A post-QEA update in the same document added early analysis of tranexamic acid (TXA) for PPH treatment following the 2017 WOMAN trial results.

## Why did we deprioritize this?

The original assessment focused on misoprostol, which was deprioritized because: (1) RCT evidence found no mortality effect; (2) misoprostol increased the risk of severe fevers 4× vs placebo; and (3) the evidence of effect on PPH incidence was weak. The post-QEA update on TXA concluded: "My best guess is that there isn't anything GiveWell should do with this now, but this is something we should keep an eye on in upcoming years."

---

## Key updates

### 1. Tranexamic acid for PPH treatment: now WHO-recommended and mortality evidence confirmed by a 2024 meta-analysis

At the time of the original QEA (mid-2017), the WOMAN trial had just published results. The original writeup already quoted the key finding: "Death due to bleeding was significantly reduced in women given tranexamic acid (155 [1·5%] of 10 036 patients vs 191 [1·9%] of 9985 in the placebo group, risk ratio [RR] 0·81, 95% CI 0·65–1·00; p=0·045), especially in women given treatment within 3 h of giving birth (89 [1·2%] in the tranexamic acid group vs 127 [1·7%] in the placebo group, RR 0·69, 95% CI 0·52–0·91; p=0·008)." ([Lancet, WOMAN trial, 2017](http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)30638-4/fulltext))

Since then, a 2024 Lancet individual patient data meta-analysis further confirmed that "early administration of TXA within three hours of PPH onset significantly reduces maternal mortality by 31%." ([Lancet 2024 TXA meta-analysis](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02102-0/fulltext); I could not access the full paper — this statistic is from a secondary source.) WHO added TXA to its PPH treatment guidelines in 2017 and confirmed its treatment role in the 2025 consolidated guidelines: "is not recommended for the prevention of postpartum haemorrhage at vaginal birth" but remains recommended for treatment within 3 hours. ([WHO Consolidated PPH Guidelines, 2025, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK619236/))

However, scale-up remains constrained by the 3-hour administration window, which requires rapid PPH diagnosis and TXA availability at the point of care.

### 2. Heat-stable carbetocin: a new WHO-recommended product not in the original QEA at all

The 2017 QEA discussed the oxytocin vs. misoprostol trade-off for settings lacking cold chain. A major new development is heat-stable carbetocin (HSC), which did not exist as a WHO-recommended option in 2017 and is now a significant alternative. The WHO 2025 consolidated guidelines state: "Heat-stable carbetocin (100 μg intramuscularly/intravenously) is the recommended choice for the prevention of postpartum haemorrhage in settings where the oxytocin cold chain cannot be consistently maintained." ([WHO Consolidated PPH Guidelines, 2025](https://www.ncbi.nlm.nih.gov/books/NBK619236/))

Ferring Pharmaceuticals makes HSC available at **$0.31 per ampoule** for LMIC public sector facilities. ([GHSC supply chain data, 2023](https://www.ghsupplychain.org/sites/default/files/2023-07/HSC_20230630.pdf)) A 2023 India modeling study found that HSC could "prevent about 5,500 additional PPH cases and save five maternal lives per 100,000 births when priced comparably to oxytocin." ([PMC review, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145113/)) I was unable to access the full India study — the $0.31 price and 5-lives-per-100,000 figures are from secondary sources; treating with medium confidence.

At $0.31/ampoule × 100,000 doses = $31,000 in drug costs to save 5 lives → $6,200/life from drug cost alone. This would be extremely cost-effective, though program implementation costs would raise this substantially.

### 3. Major implementers are now active at scale; funding landscape has changed

The space is no longer empty. Unitaid's AMPLI-PPHI project (2022–2026) is a **$26 million initiative** led by Jhpiego, with PATH and FIGO as partners, funded by Unitaid, the European Union (via Safe Birth Africa), and the Gates Foundation. It covers DRC, Guinea, India, and Kenya, expanding to Nigeria and Zambia in 2024. ([Unitaid AMPLI-PPHI](https://unitaid.org/project/expanding-access-to-recently-recommended-drugs-to-prevent-and-treat-postpartum-haemorrhage-pph/)) The program focuses on generating evidence and scaling up TXA, heat-stable carbetocin, and misoprostol.

This is both good news (proof of implementability) and a consideration for room for more funding — the question is whether gaps remain beyond what AMPLI-PPHI covers.

---

## Sense-check of original BOTEC

The original BOTEC for TXA (the most relevant intervention) is extremely sparse — only one cost row was visible: "Incremental cost per patient of administering TXA per patient in facility setting: $17.48 (Guerriero et al. 2011)" from a Tanzania study. This was not a full CE model — no deaths averted calculation, no multiples-of-cash output. The misoprostol CE was presented as a "naive" $700/life saved with the caveat that "we haven't seen any direct evidence that misoprostol reduces maternal mortality."

No errors in the cost data visible; the issue is the BOTEC is incomplete rather than wrong.

---

## New CE estimate

**~8–15x cash** (highly uncertain). See BOTEC at `./outputs/botecs/uterotonics_pph_prevention.xlsx`.

This estimate is based on TXA treatment rather than misoprostol (the original focus). Rough calculation: TXA costs ~$1–3/course drug cost in LMIC settings (it is off-patent and generic). Adding program costs (training, supply chain, monitoring), total program cost per PPH case treated might be ~$20–50. If RCT evidence suggests 0.4% of PPH cases die with placebo vs. 0.33% with TXA (RR 0.81), then cost per death averted from TXA = $20–50 / 0.0007 = $28,000–71,000 per death averted — which is 1–3x cash. That seems low-end. If heat-stable carbetocin prevents PPH at $0.31/birth and prevents 5 deaths per 100,000 births (facility births only), that's $6,200/life (drug only), rising to possibly $20,000–50,000 with full program costs, which is roughly 3–8x cash.

I'm assuming program costs are 10–50x drug costs, which is a wide range. The high end (5 deaths per 100k births at $50k/death) yields 3–5x; the low end of program cost (10x drug cost at $3.10 for carbetocin) yields ~60x. I'm settling on ~8–15x as a plausible central estimate for a well-run bundled PPH program, with Low confidence.

Note: the original misoprostol-focused program is effectively off the table — WHO 2025 designates it a "last resort." The relevant fundable intervention has shifted entirely to TXA + heat-stable carbetocin.

---

## Remaining uncertainties

1. **Is there room for more funding beyond AMPLI-PPHI?** Jhpiego/Unitaid/FIGO are actively scaling up exactly this intervention in 6 countries. The key question for GiveWell/CE is whether additional funding in different geographies (South Asia? francophone West Africa?) or different intervention components (last-mile supply chain? training?) would be high-value and not already funded. This should be verified with the AMPLI-PPHI program team.

2. **What are full program costs per birth?** The $17.48/patient TXA figure from 2011 Tanzania is old and doesn't reflect current generic TXA prices (likely much lower). A current cost estimate for a PPH bundle (TXA + HSC + training) per facility birth in a high-burden setting is needed to nail down the CE.

3. **Coverage rates at community level.** Both TXA (IV/IM required) and HSC (injectable) require facility or skilled birth attendant delivery. For the ~40% of births in LMICs outside facilities, neither product is deployable in current form. Misoprostol remains the only option for community-level prevention — and it's recommended by WHO for that setting. Is there a specific program funding community-level PPH prevention that is underfunded?

---

## Who is implementing / funding this?

- **Jhpiego / AMPLI-PPHI:** Lead implementer; active in DRC, Guinea, India, Kenya, Nigeria, Zambia (2022–2026)
- **PATH / FIGO:** Partners in AMPLI-PPHI; PATH focuses on supply chain and implementation science
- **Unitaid:** $26M funder; driving market access for TXA, HSC, misoprostol
- **Gates Foundation / European Union (Safe Birth Africa):** Additional funding for scale-up
- **Ferring Pharmaceuticals:** Supplies HSC at $0.31/ampoule to LMIC public sector
- **PSI:** Was operating misoprostol distribution in SSA at the time of the original QEA; unclear if this continues

---

## Recommended next steps

1. **Map funding gaps in the AMPLI-PPHI program.** The current program covers 6 countries. A conversation with **Jhpiego's PPH program lead** (reachable through [AMPLI-PPHI FIGO page](https://www.figo.org/about-us/figo-programmes/accelerating-measurable-progress-and-leveraging-investments-postpartum)) would reveal whether there are geographic or programmatic gaps that additional funding could fill. This directly answers the room-for-more-funding question.

2. **Get full program cost data from AMPLI-PPHI's implementation evidence.** The program is generating cost-effectiveness evidence as one of its explicit objectives (by July 2026). If early results are available, they would resolve the biggest uncertainty in the CE estimate. Requesting this from Jhpiego or PATH would be far more reliable than the 2011 Tanzania cost data.

3. **Build a separate CE model for heat-stable carbetocin** using the 2023 India modeling data and the $0.31/ampoule Ferring price. The original BOTEC focused on misoprostol/TXA and did not model HSC at all. Given WHO's recommendation and the $0.31 price point, HSC for cold-chain-deficient settings may be the most cost-effective component of the PPH bundle and deserves its own model.
