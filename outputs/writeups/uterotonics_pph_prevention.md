# Review: Uterotonics for Prevention/Treatment of Postpartum Hemorrhage QEA

- Link to original QEA: [Prevention/treatment of postpartum hemorrhage](https://docs.google.com/document/d/1euCoBUuJQ8V8l7Mgl5SFP6UpcT2H7BioX8uRxoohpoM/edit)
- Link to original BOTEC: [TXA BOTEC](https://docs.google.com/a/givewell.org/spreadsheets/d/1JL3dI9dS2MrtWsA1miIxMm1u9-3Bfbu-RYW7vWTYlGo/edit) (sparse; only one TXA cost row was visible)
- Year the original analysis was conducted: 2017

## What is this (basic context)

- **What is the problem?** Postpartum hemorrhage (PPH — excessive bleeding after birth) causes roughly 25% of maternal deaths in LMICs and is the single leading cause of maternal mortality globally. An estimated 300,000+ women die in childbirth each year, most from PPH.
- **What is the program?** The original QEA focused on misoprostol distribution (a cheap, heat-stable oral uterotonic) for PPH prevention in low-resource settings, particularly a PSI program in sub-Saharan Africa. A post-QEA update in the same document added early analysis of tranexamic acid (TXA) for PPH treatment following the 2017 WOMAN trial results.
- **Why did we deprioritize this?** The original assessment focused on misoprostol, which was deprioritized because: (1) RCT evidence found no mortality effect; (2) misoprostol increased the risk of severe fevers 4x vs placebo; and (3) the evidence of effect on PPH incidence was weak. The post-QEA update on TXA concluded: "My best guess is that there isn't anything GiveWell should do with this now, but this is something we should keep an eye on in upcoming years."[^1]

## Key updates

### 1. Tranexamic acid for PPH treatment: now WHO-recommended with mortality evidence confirmed

At the time of the original QEA (mid-2017), the WOMAN trial had just published results showing that death due to bleeding was significantly reduced with TXA, with a risk ratio of 0.81 (95% CI 0.65–1.00), and a stronger effect when given within 3 hours (RR 0.69, 95% CI 0.52–0.91).[^2]

Since then, a 2024 Lancet individual patient data meta-analysis of 54,404 women from 5 RCTs found that TXA reduces life-threatening postpartum bleeding (a composite of death, laparotomy, embolisation, uterine compression sutures, or arterial ligation) with a pooled odds ratio of 0.77 (95% CI 0.63–0.93).[^3] WHO added TXA to its PPH treatment guidelines in 2017 and confirmed its treatment role in the 2025 consolidated guidelines. TXA is not recommended for PPH prevention in any delivery mode — a 2025 Cochrane review excluded all prior prevention trials on data integrity grounds, and the two largest cesarean prevention trials (TRAAP2 and Myles et al.) both failed to show benefit on clinically meaningful endpoints.[^4]

However, scale-up remains constrained by the 3-hour administration window, which requires rapid PPH diagnosis and TXA availability at the point of care.

### 2. Heat-stable carbetocin: a new WHO-recommended product not in the original QEA

The 2017 QEA discussed the oxytocin vs. misoprostol trade-off for settings lacking cold chain. A major new development is heat-stable carbetocin (HSC), which did not exist as a WHO-recommended option in 2017. The WHO 2025 consolidated guidelines now recommend HSC for PPH prevention in settings where the oxytocin cold chain cannot be consistently maintained.[^5]

Ferring Pharmaceuticals makes HSC available at $0.31 per ampoule for LMIC public sector facilities.[^6] A 2023 India modeling study found that HSC could prevent about 5,500 additional PPH cases and save five maternal lives per 100,000 births when priced comparably to oxytocin.[^7] I was unable to access the full India study — the $0.31 price and 5-lives-per-100,000 figures are from secondary sources; treating with medium confidence.

At $0.31/ampoule x 100,000 doses = $31,000 in drug costs to save 5 lives → $6,200/life from drug cost alone. This would be extremely cost-effective, though program implementation costs would raise this substantially.

### 3. Major implementers are now active at scale; funding landscape has changed

The space is no longer empty. Unitaid's AMPLI-PPHI project (2022–2026) is a $26 million initiative led by Jhpiego, with PATH and FIGO as partners, covering DRC, Guinea, India, Kenya, Nigeria, and Zambia.[^8] The program focuses on generating evidence and scaling up TXA, heat-stable carbetocin, and misoprostol.

This is both good news (proof of implementability) and a consideration for room for more funding — the question is whether gaps remain beyond what AMPLI-PPHI covers.

### Sense-check of original BOTEC

The original BOTEC for TXA is extremely sparse — only one cost row was visible: "Incremental cost per patient of administering TXA per patient in facility setting: $17.48 (Guerriero et al. 2011)" from a Tanzania study.[^9] This was not a full CE model — no deaths averted calculation, no multiples-of-cash output. The misoprostol CE was presented as a "naive" $700/life saved with the caveat that "we haven't seen any direct evidence that misoprostol reduces maternal mortality."[^10]

No errors in the cost data visible; the issue is the BOTEC is incomplete rather than wrong.

## New CE estimate

**~3x cash** (best guess; highly uncertain — range ~2x to ~7x depending on program costs). See BOTEC at `./outputs/botecs/uterotonics_pph_prevention.xlsx`.

The BOTEC models a bundled facility-based PPH program (HSC for prevention + TXA for treatment) using the standard GW CE model structure: $1M grant → births covered → deaths averted (with explicit IV and EV adjustments for each component) → UoV via moral weights → ad-hoc morbidity/treatment-cost adjustments → multiples of benchmark.

At an estimated $2 per facility birth covered (including drugs, training, supply chain, and monitoring), the grant covers 500,000 births. HSC averts ~19 deaths (5 per 100k, adjusted) and TXA averts ~88 deaths (from 6% PPH rate × 1.9% case fatality × 19% relative risk reduction, adjusted). With morbidity (+75%) and treatment cost (+25%) uplifts, the total yields ~3.3x cash.

The CE is extremely sensitive to the per-birth cost assumption — the single most important unknown:
- At $1/birth (marginal cost of adding HSC+TXA to existing facilities): ~6.5x
- At $2/birth (central estimate): ~3.3x
- At $3/birth (full program cost): ~2.2x

This is below the 8x bar on the central estimate. However, the E-MOTIVE trial (NEJM 2023) demonstrated that a bundled PPH detection + treatment approach can reduce severe PPH outcomes by 60% in LMIC facility settings,[^em] which suggests the bundled approach has substantial value. The AMPLI-PPHI program should produce real cost data by mid-2026 that would resolve the key uncertainty.

Note: the original misoprostol-focused program is effectively off the table — WHO 2025 designates it as a last resort when no injectable options are available.[^12]

## Remaining uncertainties

1. **Is there room for more funding beyond AMPLI-PPHI?** Jhpiego/Unitaid/FIGO are actively scaling up exactly this intervention in 6 countries. The key question is whether additional funding in different geographies (South Asia? francophone West Africa?) or different intervention components (last-mile supply chain? training?) would be high-value and not already funded.

2. **What are full program costs per birth?** The $17.48/patient TXA figure from 2011 Tanzania is old and doesn't reflect current generic TXA prices (likely much lower). A current cost estimate for a PPH bundle (TXA + HSC + training) per facility birth in a high-burden setting is needed to nail down the CE.

3. **Coverage rates at community level.** Both TXA (IV/IM required) and HSC (injectable) require facility or skilled birth attendant delivery. For the ~40% of births in LMICs outside facilities, neither product is deployable in current form. Misoprostol remains the only option for community-level prevention. Is there a specific program funding community-level PPH prevention that is underfunded?

## Who is implementing / funding this?

- **Jhpiego / AMPLI-PPHI:** Lead implementer; active in DRC, Guinea, India, Kenya, Nigeria, Zambia (2022–2026)
- **PATH / FIGO:** Partners in AMPLI-PPHI; PATH focuses on supply chain and implementation science
- **Unitaid:** $26M funder; driving market access for TXA, HSC, misoprostol
- **Gates Foundation / European Union (Safe Birth Africa):** Additional funding for scale-up
- **Ferring Pharmaceuticals:** Supplies HSC at $0.31/ampoule to LMIC public sector
- **PSI:** Was operating misoprostol distribution in SSA at the time of the original QEA; unclear if this continues

## Recommended next steps

1. **Map funding gaps in the AMPLI-PPHI program.** The current program covers 6 countries. A conversation with **Jhpiego's PPH program lead** (reachable through the [AMPLI-PPHI FIGO page](https://www.figo.org/about-us/figo-programmes/accelerating-measurable-progress-and-leveraging-investments-postpartum)) would reveal whether there are geographic or programmatic gaps that additional funding could fill. This directly answers the room-for-more-funding question.

2. **Get full program cost data from AMPLI-PPHI's implementation evidence.** The program is generating cost-effectiveness evidence as one of its explicit objectives (by July 2026). If early results are available, they would resolve the biggest uncertainty in the CE estimate. Requesting this from Jhpiego or PATH would be far more reliable than the 2011 Tanzania cost data.

3. **Investigate the E-MOTIVE bundle as a delivery model.** The E-MOTIVE trial (NEJM 2023) showed a 60% reduction in severe PPH outcomes using a bundled detection + treatment approach (calibrated drape + first-response treatment including TXA). WHO has incorporated the MOTIVE bundle into its 2025 guidelines. Understanding the per-birth cost of implementing MOTIVE at scale — particularly whether it reduces the effective cost below $2/birth assumed in our BOTEC — would substantially sharpen the CE estimate. **Dr. Ioannis Gallos** (University of Birmingham), the MOTIVE trial lead, would be the key contact.

---

[^1]: "My best guess is that there isn't anything GiveWell should do with this now, but this is something we should keep an eye on in upcoming years." https://docs.google.com/document/d/1euCoBUuJQ8V8l7Mgl5SFP6UpcT2H7BioX8uRxoohpoM/edit

[^2]: "Death due to bleeding was significantly reduced in women given tranexamic acid (155 [1.5%] of 10 036 patients vs 191 [1.9%] of 9985 in the placebo group, risk ratio [RR] 0.81, 95% CI 0.65–1.00; p=0.045), especially in women given treatment within 3 h of giving birth (89 [1.2%] in the tranexamic acid group vs 127 [1.7%] in the placebo group, RR 0.69, 95% CI 0.52–0.91; p=0.008)." http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)30638-4/fulltext

[^3]: "Life-threatening bleeding occurred in 178 (0.65%) of 27,300 women in the tranexamic acid group versus 230 (0.85%) of 27,093 women in the placebo group (pooled odds ratio [OR] 0.77 [95% CI 0.63–0.93]; p=0.008)." Individual patient data meta-analysis of 54,404 women from 5 RCTs. Note: endpoint is a composite (death + surgical interventions), not mortality alone. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02102-0/fulltext

[^4]: "Tranexamic acid is not recommended for the prevention of postpartum haemorrhage at vaginal birth." TXA is also not recommended for prevention at cesarean delivery — the 2025 Cochrane review excluded all prior vaginal-birth prevention trials on data integrity grounds, and the two largest cesarean prevention trials (TRAAP2, NEJM 2021; Myles et al., NEJM 2023) both failed to show benefit on clinically meaningful endpoints. TXA is recommended for treatment only. https://www.ncbi.nlm.nih.gov/books/NBK619236/

[^5]: "Heat-stable carbetocin (100 μg intramuscularly/intravenously) is the recommended choice for the prevention of postpartum haemorrhage in settings where the oxytocin cold chain cannot be consistently maintained." https://www.ncbi.nlm.nih.gov/books/NBK619236/

[^6]: "This price is a subsidised price of $0.31 +/- 10% per ampoule of 100 ug Carbetocin Ferring, Ex Works." https://www.ferring.com/ferring-statement-on-subsidised-pricing-of-heat-stable-carbetocin-for-the-prevention-of-postpartum-haemorrhage-in-low-and-lower-middle-income-countries/

[^7]: "prevent about 5,500 additional PPH cases and save five maternal lives per 100,000 births when priced comparably to oxytocin" — from a PMC review citing the 2023 India modeling study. I could not access the original study. https://pmc.ncbi.nlm.nih.gov/articles/PMC12145113/

[^8]: "Unitaid's AMPLI-PPHI project (2022–2026) is a $26 million initiative led by Jhpiego" https://unitaid.org/project/expanding-access-to-recently-recommended-drugs-to-prevent-and-treat-postpartum-haemorrhage-pph/

[^9]: [Note] The original BOTEC had only one cost row visible: "Incremental cost per patient of administering TXA per patient in facility setting: $17.48 (Guerriero et al. 2011)" from a Tanzania study. This was not a full CE model.

[^10]: [Note] The misoprostol CE in the original QEA was presented as a "naive" $700/life saved with the explicit caveat that there was no direct mortality evidence.

[^11]: [Note] The BOTEC models HSC and TXA as a bundled program with shared infrastructure costs ($2/birth). The per-component estimates are low individually (HSC saves ~3.8 lives per 100k after validity adjustments; TXA saves ~17.5 per 100k). The bundled program CE of ~3x reflects the combined benefit at realistic program costs.

[^em]: "A primary-outcome event occurred in 1.6% of the patients in the intervention group, as compared with 4.3% of those in the usual-care group (risk ratio, 0.40; 95% confidence interval [CI], 0.32 to 0.50; P<0.001)." E-MOTIVE trial (Gallos et al., NEJM 2023): bundled early detection + treatment approach, 210,132 women across 80 hospitals in Kenya, Nigeria, South Africa, and Tanzania. https://www.nejm.org/doi/full/10.1056/NEJMoa2303966

[^12]: "Misoprostol should be used as a last resort when other recommended uterotonics are not available." https://www.ncbi.nlm.nih.gov/books/NBK619236/
