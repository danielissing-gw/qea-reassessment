# Review: QEA of Synbiotics to Prevent Neonatal Sepsis

- Link to original QEA: None (no writeup produced)
- Link to original BOTEC: [Synbiotics BOTEC](https://docs.google.com/spreadsheets/d/1zbPI3isnMJjYX2ANqpIuCxf1olE4zbSOJ6gkNHpEVMg/)
- Year the original analysis was conducted: 2018

## What is this (basic context)

- **What is the problem?** Neonatal sepsis kills approximately 206,000 newborns per year globally, concentrated in sub-Saharan Africa and South Asia.[^1] Treatment requires injectable antibiotics and hospital care that are often unavailable in rural LMIC settings.
- **What is the program?** A 7-day oral synbiotic course (Lactobacillus plantarum + fructooligosaccharide) given to healthy newborns in the first days of life to colonize the gut with protective bacteria, reducing the risk of sepsis.
- **Why did we deprioritize this?** Single unreplicated trial (Panigrahi et al. 2017); 5% CFR was a guess; no identified implementer.

## Key updates

1. **The neonatal sepsis CFR used in the original BOTEC (5%) is almost certainly 2-4x too low.** The original BOTEC author flagged this explicitly ("I am extremely uncertain about the case fatality rate for neonatal sepsis. I would investigate that further with more time."). A 2021 systematic review of 26 studies (2.8 million live births) found a pooled neonatal sepsis CFR of 17.6% (95% CI 10.3-28.6%).[^2] The BARNARDS study across 7 LMICs found 13.3% CFR for lab-confirmed sepsis.[^3] Even the most conservative estimate (pSBI at 9.8%) is nearly double the original 5% assumption.[^4] This is the single most important correction — it roughly triples the number of deaths averted per dollar spent.

2. **A Bangladesh replication trial failed to reproduce persistent gut colonization.** Pell et al. (2025, mSphere, n=519 neonates in Dhaka) found that LP202195 abundance "increased from day 14-60 but progressively declined and did not persist beyond 2 months of age," which is "inconsistent with a prior study of the same synbiotic regimen in India, in which LP202195 was shown to persist in the infant GI tract for up to 6 months."[^5] This is a significant red flag for external validity — if the mechanism depends on persistent colonization and that doesn't happen outside rural India, the clinical benefit may be context-specific. However, this was a Phase 2 colonization study (n=519), not a powered clinical efficacy trial, and measured a biomarker rather than clinical sepsis endpoints.

3. **Programmatic costs are now better understood, and are higher than assumed.** The PROSYNK trial cost study in Kenya found programmatic costs of $9.15 per infant for a 32-dose, 6-month regimen — substantially higher than the original $2/course assumption.[^6] However, the Panigrahi regimen was only 7 days, which would be much cheaper to deliver. I'm assuming $5/course as a central estimate that accounts for delivery costs in a scaled program with the shorter regimen (see BOTEC). The original $1/drug cost may still be reasonable; the key uncertainty is overhead and delivery.

## New CE estimate

**~12x at $5/course (range ~6x at $9/course to ~28x at $2/course).** This upgrades the intervention from Low to **Medium**.

The main driver of the change is the CFR correction: moving from 5% to 15% triples the value of preventing each sepsis case. Even with substantial discounts for the single-trial evidence base (30% IV discount) and external validity concerns from the Bangladesh colonization failure (40% EV discount), the CE remains above the 8x bar at central cost assumptions.

See [synbiotics_neonatal_sepsis.xlsx](../botecs/synbiotics_neonatal_sepsis.xlsx) for the full BOTEC.

## Remaining uncertainties

- **Whether the clinical effect replicates outside rural India.** The Bangladesh colonization failure is a genuine concern. The PROSYNK trial in Kenya (LSTM, n=600) has completed enrollment but results are not yet published — this is the most decision-relevant pending evidence.[^7] If PROSYNK shows persistent colonization AND conducts clinical follow-up, it would substantially increase confidence. If it fails, the intervention is likely India-specific.
- **Programmatic cost per course at scale.** The difference between $2/course (original) and $9/course (PROSYNK) is the difference between 28x and 6x. A 7-day regimen in India vs. 32-dose/6-month regimen in Kenya partly explains this gap, but the "right" protocol for a scaled program is unclear.
- **Whether FOS (the prebiotic component) is needed.** The Bangladesh trial found arms without FOS were "indistinguishable from the synbiotic in terms of colonization, safety, and tolerability."[^5] Removing FOS would simplify and cheapen the regimen.
- **The actual neonatal sepsis CFR in the target population.** The systematic review pooled estimate (17.6%) has wide confidence intervals (10.3-28.6%). The CE is sensitive to this parameter: at 10% CFR, CE drops to ~8x; at 20% CFR, it rises to ~16x.

## Who is implementing / funding this?

No organization is currently scaling synbiotic supplementation for neonatal sepsis prevention. The field remains in the research/replication phase:

- **Bill & Melinda Gates Foundation** is the primary funder. Gates Goalkeepers 2023 listed probiotics among "seven innovations that could save 2 million mothers and babies by 2030."[^8] Gates has funded $7.4M to GARDP for neonatal sepsis research (2024), the BARNARDS study, and invested in Infinant Health for B. infantis (a different organism).
- **Liverpool School of Tropical Medicine (LSTM)** is leading the PROSYNK trial in Kenya (Phase 2, n=600).
- **Hospital for Sick Children, Toronto** led the Bangladesh colonization trial.
- **Novonesis (formerly Chr. Hansen)** manufactures LP202195 (PPLP-217) and supplies the probiotic for research trials.
- **Panigrahi's group** at the University of Nebraska Medical Center conducted the original trial but has no scale-up program.

## Recommended next steps

1. **Track PROSYNK results from LSTM.** This Kenya-based Phase 2 trial is the most proximate evidence on whether colonization and clinical benefits replicate in SSA. Contact **Dr. Stephen Allen** (LSTM, principal investigator on PROSYNK) to learn the timeline for published results and whether clinical outcomes data (not just colonization) are being collected.

2. **Investigate the shortest effective regimen.** The 7-day Panigrahi regimen costs ~$2; the 6-month PROSYNK regimen costs ~$9. The Bangladesh data suggest FOS may not be needed. If a 7-day L. plantarum-only course achieves similar colonization and clinical benefit, programmatic costs would be dramatically lower. This is a question for Panigrahi's group (UNMC) or LSTM.

3. **Assess whether a GW-style funding opportunity exists conditional on replication.** If PROSYNK or another trial confirms clinical efficacy in a second setting, this intervention could be highly cost-effective ($2-5/course for ~12x). The Gates Foundation is the natural co-funder, but no one is planning a delivery trial or scale-up program. A GiveWell-funded implementation RCT (e.g., through BRAC in Bangladesh or a community health platform in SSA) could be high-value — but only after efficacy replication.

---

[^1]: "In 2021, globally, an estimated 206,451 neonates died from neonatal sepsis and other infections, with an age-standardized mortality rate of 2,117.8 per 100,000 live births." [GBD 2021 analysis, Frontiers in Medicine 2025](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1536948/full)

[^2]: "Pooled neonatal sepsis case fatality was 17.6% (95% CI 10.3-28.6%)." [Fleischmann et al. 2021, eClinicalMedicine](https://pmc.ncbi.nlm.nih.gov/articles/PMC8311109/)

[^3]: [Note] BARNARDS study (Lancet Global Health 2022, 7 LMIC countries): 183 deaths among 1,372 confirmed neonatal sepsis cases = 13.3% CFR. This is facility-based data from Bangladesh, Ethiopia, India, Pakistan, Nigeria, Rwanda, and South Africa.

[^4]: "Case fatality among young infants 0-59 days old with a possible serious bacterial infection (pSBI) was 9.8% (95% CI 7.4-12.2%)." [Lancet Infectious Diseases 2014 pooled estimate](https://pmc.ncbi.nlm.nih.gov/articles/PMC6340339/)

[^5]: "LP202195 abundance in LP-treated infants increased on day 14 and day 60, compared with control; however, it progressively declined over the study period. [...] This decline of LP202195 is inconsistent with a prior study of the same synbiotic regimen in India, in which LP202195 was shown to persist in the infant GI tract for up to 6 months." [Pell et al. 2025, mSphere](https://pubmed.ncbi.nlm.nih.gov/39992135/)

[^6]: "The mean financial cost per participant completing the intervention with direct oral administration was $8.62 [...] while the mean economic cost was $9.15." [PROSYNK cost study, medRxiv 2024](https://www.medrxiv.org/content/10.1101/2024.12.17.24319142v1.full)

[^7]: "PROSYNK is a four-arm, open-label, randomised phase II trial, in which 600 newborn infants in Homa Bay County, western Kenya, will be randomised 1:1:1:1 to receive two synbiotics, a probiotic, or no supplement." [Trial protocol, Trials 2022](https://trialsjournal.biomedcentral.com/articles/10.1186/s13063-022-06211-1)

[^8]: "The Gates Foundation's Goalkeepers 2023 report listed probiotics among 'seven innovations that could save 2 million mothers and babies by 2030.'" [Gates Foundation 2023](https://www.gatesfoundation.org/ideas/media-center/press-releases/2023/09/goalkeepers-report-maternal-child-mortality)
