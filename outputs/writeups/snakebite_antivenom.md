# Review: QEA of Snakebite Antivenom

- Link to original QEA: [Snakebite antivenom QEA](https://docs.google.com/document/d/1bxP6BzMji2EB7lUPcuUfN-3ExHUW7A9--n5ZY4wrMPs/)
- Link to original BOTEC: [Snakebite antivenom BOTEC](https://docs.google.com/spreadsheets/d/1OpO3mS4kzewYfvKynwaIe37q5yoKRKgkkwWvoH0S8D0/)
- Year the original analysis was conducted: 2017

## What is this (basic context)

- **What is the problem?** Snakebite envenoming kills an estimated 63,400-138,000 people annually, concentrated in South Asia (86%) and sub-Saharan Africa.[^1] It is the deadliest neglected tropical disease. Most deaths are preventable with timely antivenom treatment, but access is severely limited — the WHO strategy to halve deaths by 2030 is deeply off track.[^2]
- **What is the program?** Procuring and distributing antivenom to health facilities in high-burden LMIC regions, primarily West Africa and South Asia. Treatment typically requires 3-10 vials of polyvalent or monospecific antivenom, plus supportive care.
- **Why did we deprioritize this?** CE below bar (0.7-0.9x) due to very high antivenom cost (~$900/5-vial dose); evidence base entirely observational (no RCTs); heavy IV/EV discounts.

## Key updates

1. **The moral weight used in the original BOTEC was substantially too low.** The original converted cost per adult life saved ($31,395) to an "under-5 equivalent" at 185% of adult value, implying a moral weight of roughly 40 UoV per death averted. However, snakebite deaths have a younger age distribution than assumed: 28% are children under 15 (MW 127-134), 17% are ages 15-29 (MW 112-126), 47% are ages 30-69 (MW ~40-106), and only 9% are 70+.[^3] The age-weighted average moral weight is approximately **95 UoV per death averted** — more than double the implicit original value. This alone roughly doubles the CE.

2. **West African cost-effectiveness analyses show much lower cost per death averted than the original BOTEC.** A 2016 CEA across 16 West African countries found cost per DALY averted of $83 (Benin) to $281 (Sierra Leone), and cost per death averted of $1,997 (Guinea-Bissau) to $6,205 (Sierra Leone/Liberia).[^4] These are dramatically lower than the original's $31,395/death averted, driven by cheaper antivenom products: EchiTAb-G (monospecific for carpet viper, ~1 vial initial dose) and EchiTAb Plus-ICP (~3 vials, ~$124/treatment average vs. $900 in the original BOTEC). A 2022 ASEAN analysis found full antivenom access was cost-**saving** from a societal perspective.[^5]

3. **Next-generation antivenoms are approaching clinical development.** Varespladib, an oral small-molecule sPLA2 inhibitor, completed Phase 2 (BRAVO trial, 95 patients) and has FDA Orphan Drug/Fast Track designations. The primary endpoint was not significant, but pre-specified subgroups showed benefit. FDA agreed to the Animal Rule pathway, and Ophirex targets NDA submission in 2027.[^6] Separately, a 2025 Nature paper demonstrated a nanobody-based antivenom covering 17 African snake species at "less than half" current antivenom costs.[^7] These are still years from availability but represent a realistic path to dramatically lower treatment costs within 3-5 years.

## New CE estimate

**~5x at $124/treatment with corrected moral weights (range ~1x at $900/treatment to ~8x in Benin); potentially ~12x with next-gen treatments.** Upgraded from Low to **Medium**.

The main drivers of the change are: (1) correcting the moral weight from ~40 to ~95 UoV (the original undervalued snakebite deaths because it didn't account for the young age distribution), and (2) incorporating West African cost data showing treatment is much cheaper with EchiTAb products than the $900/dose assumed in the original.

See [snakebite_antivenom.xlsx](../botecs/snakebite_antivenom.xlsx) for the full BOTEC.

## Remaining uncertainties

- **No RCTs on antivenom effectiveness.** The 75% mortality reduction (OR 0.25) comes from a meta-analysis of 4 observational studies (Habib & Warrell 2013). This is a consistent observational signal with strong biological plausibility but has never been tested in a randomized design. The evidence quality cannot improve — a placebo-controlled antivenom RCT would be unethical.
- **Varespladib timeline and efficacy.** The Phase 2 primary endpoint was not significant. NDA submission is targeted for 2027 via the Animal Rule pathway, but regulatory and clinical uncertainty remains. If varespladib works as hoped ($10-20/course, oral, broadly effective), it transforms the CE arithmetic entirely.
- **Antivenom supply crisis.** FAV-Afrique (the gold-standard SSA polyvalent) was discontinued in 2016; SAVP (South Africa) had stock-outs in 2024. The $51-66M annual cost to meet WHO targets in SSA is not currently funded.[^8] This creates both a need and a supply constraint.
- **India dominates the burden (86% of deaths) but has very different market dynamics** from SSA. Antivenom costs in India are different, and India's National Action Plan (launched March 2024) may change the landscape.

## Who is implementing / funding this?

- **Wellcome Trust**: ~$100M 7-year program (2019-2026) covering research, clinical trials (including varespladib), and manufacturing improvement. Program concluding in 2026; "Snakebite Beyond 2026" RFP published March 2024.[^9]
- **MSF**: Largest NGO provider. Treated 6,747 snakebite patients in 2023 across Central African Republic, Ethiopia, South Sudan, and Yemen. Provides antivenom free of charge.[^10]
- **WHO**: Global strategy (2019); Target Product Profiles for SSA antivenoms; snakebite listed as Category A NTD since 2017.
- **Instituto Clodomiro Picado (Costa Rica)**: Manufactures EchiTAb Plus-ICP for African markets.
- **MicroPharm (UK)**: Manufactures EchiTAb-G (monospecific for Echis ocellatus).
- **Ophirex (US)**: Developing varespladib (oral small-molecule); FDA Fast Track.
- **Global Snakebite Taskforce**: Launched May 2025 at World Health Assembly, co-chaired by Kenya MOH and LSTM.

## Recommended next steps

1. **Model the CE of a targeted West African antivenom procurement program.** The $83-281/DALY estimates from Habib et al. 2016 suggest CE at or near the 8x bar in the most favorable settings (Benin, Guinea-Bissau, Nigeria). A deeper dive into the specific cost structure — which antivenom products, what procurement volumes, which health facility distribution model — would clarify whether a concrete funding opportunity exists today. Contact **Prof. Abdulrazaq Habib** (Bayero University, Kano, Nigeria) who led both the West African CEA and the largest clinical datasets on carpet viper antivenom.

2. **Track varespladib regulatory progress.** If Ophirex submits an NDA in 2027 and receives approval, the cost structure changes fundamentally ($10-20/course oral vs. $124-900/course IV antivenom). This would push CE well above 8x. Contact **Matthew Lewin, MD** (Ophirex CEO) for timeline updates and LMIC access pricing plans.

3. **Assess the philanthropic gap post-Wellcome.** Wellcome's $100M program concludes in 2026. The "Beyond 2026" RFP suggests they're planning for continued engagement, but the scale and focus are uncertain. If Wellcome scales back, there may be a specific gap in antivenom procurement or clinical trial funding that GiveWell could fill. The Global Snakebite Taskforce (launched May 2025) would be the best source for understanding where the gaps are.

---

[^1]: "In 2019, there were an estimated 63,400 (95% uncertainty interval 38,900-78,600) deaths from snakebite envenoming globally [...] South Asia accounted for 54,600 (86.1%) of global snakebite deaths." [GBD 2019 analysis, Nature Communications 2022](https://www.nature.com/articles/s41467-022-33627-9)

[^2]: "By 2030, the model predicts only an 8.6% further decrease (95% UI: −9.6% to 20.1%)" in age-standardized snakebite mortality — far short of the WHO target of 50% reduction. [Nature Communications 2022](https://www.nature.com/articles/s41467-022-33627-9)

[^3]: [Note] Age distribution from GBD 2019 India data (which carries >80% of global burden): 28% under 15, 17% ages 15-29, 47% ages 30-69, 9% ages 70+. West African data consistently shows mean age of snakebite victims in the late twenties. I'm computing a weighted-average MW of ~95 UoV using GiveWell's 2020 moral weights table: 0.28 × 130 + 0.17 × 120 + 0.30 × 93 + 0.17 × 55 + 0.09 × 21 = 95.4.

[^4]: "The cost per death averted ranged from US$1,997 in Guinea-Bissau to US$6,205 in Sierra Leone and Liberia. [...] cost per DALY averted ranged from US$83 in Benin to US$281 in Sierra Leone and Liberia." [Hamza et al. 2016, PLOS NTDs](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0004568)

[^5]: "Improving antivenom access from current levels to full access: 9,362 deaths averted (−59%), 230,075 DALYs averted (−59%), cost savings of $1.3 billion (−53%)." [PLOS NTDs 2022, ASEAN analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC9668136/)

[^6]: "FDA agreed that varespladib can be developed under the Animal Rule [...] Ophirex's CEO stated the goal is to complete Animal Rule efficacy studies 'before the end of [2026]' and submit an NDA in 2027." [Ophirex December 2025 business update](https://www.globenewswire.com/news-release/2025/12/11/3203856/0/en/Ophirex-Announces-Business-Update-Advances-Toward-Food-and-Drug-Administration-FDA-Approval-for-Varespladib-as-Novel-Oral-Snakebite-Treatment.html)

[^7]: "A recombinant antivenom composed of eight nanobodies that provides broad protection against 17 African elapid snake species [...] can reportedly be produced at less than half the current cost of existing antivenoms." [Nature 2025](https://www.nature.com/articles/s41586-025-09661-0)

[^8]: [Note] Annual cost to meet WHO antivenom targets in SSA: $51.4-$66.2M for ~279,485 treatments, based on antivenom prices of $100-$153/treatment. From PLOS NTDs 2020 gap analysis.

[^9]: "Wellcome is running an innovation prize competition for creative approaches to tackling snakebite envenoming." The "Snakebite Beyond 2026" RFP was published in March 2024. [Wellcome 2024](https://cms.wellcome.org/sites/default/files/2024-03/Snakebite-beyond-2026-RFP.pdf)

[^10]: "MSF treated 6,747 snakebite patients in 2023." [MSF snakebite page](https://www.msf.org/snakebite)
