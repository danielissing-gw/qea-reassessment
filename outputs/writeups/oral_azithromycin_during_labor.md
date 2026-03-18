# Review: QEA of Oral Azithromycin During Labor

- Link to original QEA: [QEAthon: Oral azithromycin during labor](https://docs.google.com/document/d/1rdNToIRCSfux7pcgUdjOdfhv7MDYJssqD-hBVwVsF3s/edit)
- Link to original BOTEC: [Oral AZT threshold analysis](https://docs.google.com/spreadsheets/d/171kRw2c0D5glTLNrGDGLuQTlM0gEMXxNnP7ibj1lEp0/edit)
- Year the original analysis was conducted: 2022

## What is this (basic context)

- **What is the problem?** Maternal sepsis is a leading cause of maternal death in low- and middle-income countries, with approximately 11% of maternal deaths globally attributable to sepsis and other infections.[^1] Neonatal infection is also a major contributor to the 2.4 million neonatal deaths that occur annually.[^2]
- **What is the program?** A single 2g oral dose of azithromycin (an inexpensive, widely available antibiotic costing ~$0.91/dose) given to women in labor at health facilities as prophylaxis against maternal and neonatal infections.
- **Why did we deprioritize this?** Not deprioritized — flagged as "revisit once trial results come in" (promisingness 7.5). The original assessment was a threshold analysis based on the PregnAnZi proof-of-concept trial (n=829); large mortality-powered trials (A-PLUS, PregnAnZI-2, SANTE) were ongoing. The threshold was ≥7% reduction in neonatal + maternal mortality for >12x cash.

## Key updates

- **A-PLUS trial results (NEJM 2023): Strong maternal benefit, no neonatal benefit.** The A-PLUS trial (n=29,278 women planning vaginal births across 7 LMICs) found that a single 2g oral dose of azithromycin during labor reduced maternal sepsis or death by 33% compared to placebo.[^3] However, there was no effect on neonatal outcomes — stillbirth, neonatal sepsis, or death occurred at similar rates in both groups.[^4] This fundamentally changes the CE arithmetic: the original threshold analysis was driven 66–86% by neonatal mortality, which is now null.

- **PregnAnZI-2 trial confirms neonatal null (JAMA 2023).** The PregnAnZI-2 trial (n=~12,000 in The Gambia and Burkina Faso) found no effect of intrapartum azithromycin on neonatal sepsis or mortality.[^5] The trial did find reduced neonatal skin infections (0.8% vs 1.7%, p<0.001) but concluded that "the results of this trial do not support the routine introduction of oral intra-partum azithromycin in sub-Saharan Africa to decrease neonatal sepsis and mortality."

- **Lancet Global Health 2025 CEA: cost-saving from health system perspective.** A modeling analysis using A-PLUS data found the intervention cost-saving overall — $0.91/dose offset by $0.33/pregnancy in averted healthcare costs from reduced maternal infections.[^6] In Africa, the cost per DALY averted was ~$983, well below the WHO cost-effectiveness threshold. This confirms the maternal benefit is real and cheap, but the analysis is from a health system perspective (not a philanthropic one), and the DALYs averted per 100,000 pregnancies are modest (13.2) because the absolute maternal mortality rate, while high, translates to relatively few deaths averted per pregnancy covered.

## New CE estimate

My best guess is **~4x cash in a representative high-MMR country (Nigeria) at $3/pregnancy, or ~9x at $1.50/pregnancy**. The CE is highly sensitive to both the delivery cost and the baseline maternal mortality ratio. See [oral_azithromycin_during_labor BOTEC](../botecs/oral_azithromycin_during_labor.xlsx).

The key driver of CE uncertainty is the incremental delivery cost. The drug itself costs $0.91/dose, and since it is given to women already presenting at a health facility for delivery, the incremental cost could be very low (perhaps $1–2 total) if integrated into routine facility care. At $1.50/pregnancy the CE in Nigeria reaches ~9x; at $3/pregnancy it falls to ~4x. The original QEA assumed $7/pregnancy based on analogy to other facility-based interventions, but this may overstate incremental costs since no new patient visits are required.

The maternal effect (RR 0.67) is much larger than the original threshold assumed (RR 0.92), but it applies to a relatively small number of deaths per pregnancy covered — even in Nigeria (MMR 735/100k), that is ~0.7% of women. The volume effect of covering many pregnancies cheaply is what could push this above the bar.

## Remaining uncertainties

- **Incremental delivery cost is the pivotal unknown.** The drug cost ($0.91) is well-established, but the cost of integrating a single oral dose into facility-based delivery care is uncertain. If delivery programs like Unitaid's AMPLI-PPHI or similar maternal health platforms could add azithromycin as a bundled intervention, costs could be very low. Actual programmatic cost data would resolve whether CE clears 8x.
- **WHO recommendation status.** No WHO recommendation for intrapartum azithromycin as of March 2026, I haven't verified this but I'm not aware of one. A WHO recommendation would dramatically accelerate scale-up and potentially enable government co-funding. The evidence base (large multicenter RCT, RR 0.67) seems strong enough to warrant consideration.
- **Antimicrobial resistance.** The A-PLUS trial did not fully characterize AMR impact; the PregnAnZI AMR substudy found increased azithromycin-resistant E. coli at days 6 and 28 post-delivery, though it waned by 12 months.[^7] Mass prophylactic use of a key antibiotic raises legitimate stewardship concerns that could limit WHO endorsement.
- **SANTE trial intrapartum component.** The SANTE trial (n=50,000+ in Mali) included an intrapartum azithromycin arm, but the specific results for this component have not yet been published (the infant MDA component showed no effect).[^8] These results could confirm or modify the A-PLUS findings.
- **Vaginal births only.** A-PLUS enrolled only women planning vaginal births. The effect for cesarean deliveries is unknown. In high-facility-birth settings, a substantial share of deliveries may be cesarean.

## Who is implementing / funding this?

- **No at-scale implementation exists.** I'm not aware of any country implementing intrapartum azithromycin as routine policy, which is expected given the lack of a WHO recommendation.
- **A-PLUS trial consortium** (University of Alabama at Birmingham, UNC, NICHD Global Network) — key academic group with multi-country implementation experience.
- **Bill & Melinda Gates Foundation** has funded azithromycin research broadly (SANTE trial, coordination with GiveWell on azithromycin MDA).
- **Potential bundling with existing maternal health platforms** — Unitaid's AMPLI-PPHI (scaling heat-stable carbetocin for PPH in 6 countries) or similar platforms could provide a delivery mechanism.

## Recommended next steps

- **Obtain programmatic cost estimates for adding oral azithromycin to facility-based delivery care.** This is the single most important unknown. The drug is $0.91; the question is what the incremental program cost of adding one oral tablet to existing delivery protocols would be. I'd recommend talking to **Dr. Alan Tita** (PI of A-PLUS trial, University of Alabama at Birmingham), who has direct experience with the delivery logistics across 7 LMIC sites and would have the best sense of what integration would cost in practice.
- **Monitor WHO guideline development.** The A-PLUS evidence (RR 0.67 from a large multicenter RCT) is the type that typically triggers WHO guideline review. A WHO recommendation would be a major inflection point for scale-up feasibility and government co-funding. The **WHO Department of Maternal, Newborn, Child and Adolescent Health** would be the relevant body to track.
- **Consider bundling with PPH intervention package.** Both intrapartum azithromycin and heat-stable carbetocin (from the PPH QEA) are single-dose facility-based interventions given during labor. If delivered together, shared infrastructure could reduce per-intervention costs. This is particularly relevant if GiveWell investigates the AMPLI-PPHI delivery platform.

---

[^1]: "Globally, 10·7% (5·9–18·6) of maternal deaths were attributable to maternal sepsis and other maternal infections." ([Say et al., Lancet Global Health 2014](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(14)70227-X/fulltext))

[^2]: [Note] UNICEF estimate cited in the original QEA; I have not independently verified the most recent figure. The 2019 estimate was 2.4 million neonatal deaths.

[^3]: "The incidence of the primary outcome of maternal sepsis or death was lower in the azithromycin group than in the placebo group (1.6% vs. 2.4%; relative risk, 0.67; 95% CI, 0.56 to 0.79; P<0.001)." ([Tita et al., NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2212111))

[^4]: "The incidence of the co-primary outcome of neonatal sepsis, stillbirth, or death was similar in the azithromycin group and placebo group (10.5% vs. 10.3%; relative risk, 1.02; 95% CI, 0.95 to 1.09)." ([Tita et al., NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2212111))

[^5]: "The overall incidence of the primary composite endpoint was similar in the azithromycin and in the placebo arm (2.0% vs 1.9%, p=0.70); as was the incidence of neonatal mortality (0.8% vs 0.8%, p=0.80) and neonatal sepsis (1.3% vs 1.3%, p=0.92)." ([Roca et al., JAMA 2023](https://pubmed.ncbi.nlm.nih.gov/36881034/))

[^6]: "Using mean health-care costs across the A-PLUS sites, intrapartum azithromycin resulted in net savings of US$32,661 [...] per 100,000 pregnancies and 13.2 disability-adjusted life-years (DALYs) averted." ([Swanson et al., Lancet Global Health 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11950424/))

[^7]: "Prevalence of azithromycin-resistant E. coli was higher in the azithromycin arm at day 6 and day 28." ([Getanda et al., Clin Infect Dis 2024](https://academic.oup.com/cid/article/79/6/1338/7674988))

[^8]: [Note] The SANTE trial enrolled 50,000+ pregnant women with a 2×2 factorial design testing antenatal/intrapartum azithromycin and infant azithromycin. The infant MDA component (published NEJM 2025) found no effect on infant mortality. The intrapartum component results have not been separately published as of March 2026.
