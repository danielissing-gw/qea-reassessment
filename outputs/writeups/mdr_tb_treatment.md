# Review: QEA of Treatment for Multi-Drug Resistant TB

- Link to original QEA: [MDR-TB QEA](https://docs.google.com/document/d/1Hx5Z7Me6qidxQnohv38Eor-ZKez4opc9zEgD2NTMkII/)
- Link to original BOTEC: None (no BOTEC was produced)
- Year the original analysis was conducted: 2017

## What is this (basic context)

- **What is the problem?** Multi-drug resistant tuberculosis (MDR-TB) is TB that does not respond to at least isoniazid and rifampicin, the two most important first-line drugs. An estimated 400,000 people develop MDR/RR-TB annually, and approximately 150,000 die from it — yet only 44% of cases are diagnosed and treated.[^1] India, the Philippines, Indonesia, China, and Pakistan account for the majority of the gap.
- **What is the program?** Diagnosis using drug susceptibility testing (GeneXpert, line probe assays) followed by a multi-drug treatment regimen. Since 2022, WHO recommends the BPaLM regimen (bedaquiline + pretomanid + linezolid + moxifloxacin) — a 6-month, all-oral treatment with ~89% success rates.[^2] This replaces the older 18-24 month injectable-based regimens that had ~60% success rates and severe side effects.
- **Why was there no BOTEC?** The 2017 assessment concluded the evidence base for treatment efficacy was "too thin" — only observational studies were available, and WHO's own recommendation was based on "very low quality evidence." The QEA flagged two upcoming RCTs (STREAM and NEXT) as potentially decision-relevant and recommended monitoring.

## Key updates

- **Multiple Phase 3 RCTs have now demonstrated ~89-91% treatment success with short-course oral regimens.** The evidence gap that blocked the 2017 assessment has been comprehensively resolved. The TB-PRACTECAL trial (Lancet Respiratory Medicine 2023, across Uzbekistan/Belarus/South Africa) found 89% treatment success with BPaLM vs. 52-75% for standard care, leading to early termination for benefit.[^3] The endTB trial (NEJM 2024, 754 patients across 7 countries) confirmed three 9-month all-oral regimens were non-inferior to standard care, with Regimen 2 achieving 90.4% success and demonstrating superiority.[^4] Nix-TB (NEJM 2020) showed 90% favorable outcomes with BPaL for XDR-TB — previously near-untreatable.[^5] ZeNix (NEJM 2022) optimized the linezolid dose, finding 91% success at 600mg for 26 weeks with substantially reduced toxicity.[^6] STREAM Stage 2 (Lancet 2022) found 91% success with a 6-month bedaquiline-containing regimen.[^7] These trials collectively represent a paradigm shift: from weak observational evidence of ~60% success with 18-24 month injectable regimens to strong RCT evidence of ~89-91% success with 6-month oral regimens.

- **Drug costs have dropped dramatically.** The full BPaLM drug regimen now costs $310 per treatment course through the Global Drug Facility — down from $588 in 2022 and far below the $1,000-5,000 range cited in the 2017 QEA.[^8] Total treatment costs (including health system costs) range from $996-$2,573 across Pakistan, Philippines, South Africa, and Ukraine — comparable to or less than the 2017 shorter regimen cost, while delivering dramatically better outcomes.[^9] Cost-effectiveness analyses consistently find BPaLM is dominant (cost-saving and more effective) compared to older regimens.

- **2025 US funding cuts have created an acute treatment gap.** The US previously provided approximately half of international TB donor funding. The Global Fund's grant cycle has been cut by $1.4 billion (11%), and USAID operations have been severely curtailed.[^10] Thirteen of 24 USAID priority countries depended on US bilateral funding for 20%+ of their TB programs. This is projected to result in 2.5 million additional pediatric TB cases and 340,000 additional pediatric TB deaths over 2025-2034.[^11] The combination of dramatically improved treatment regimens and collapsing international funding creates a potentially high-leverage moment for philanthropic dollars.

## New CE estimate

My best guess is **~3x cash at $1,500/patient all-in cost (range ~2x at $2,500/patient to ~15x at $310/patient for drug procurement only)**. See [mdr_tb_treatment BOTEC](../botecs/mdr_tb_treatment.xlsx).

The CE is driven by the large mortality reduction from treatment (~89% success vs. ~50% mortality if untreated over 5 years) applied to working-age adults (mean age ~39). The key constraint is cost per patient: at full programmatic cost ($1,500-2,500/patient including diagnosis, treatment, monitoring), the CE is 2-3x — below the 8x bar. However, if the philanthropic role is primarily drug procurement to close acute gaps created by US funding cuts ($310/patient for BPaLM drugs, with existing health systems covering diagnostics and monitoring), CE could reach ~15x. At an intermediate cost of $750/patient (drugs + basic support), CE is ~6x — still below the 8x bar but in striking distance.

The original 2017 assessment produced no CE estimate at all. The transformation is in the evidence base: from "very low quality" observational studies to multiple large Phase 3 RCTs demonstrating ~89-91% success with 6-month oral regimens. Drug costs have also fallen ~70% since 2017. The moral weight per death averted (~40 UoV for adults dying at mean age ~39) is moderate — lower than under-5 deaths (52.5 UoV) but higher than elderly CVD deaths (~20-30 UoV).

## Remaining uncertainties

- **Per-patient cost in a philanthropic program is the pivotal unknown.** The $310 drug cost is well-established (Global Drug Facility pricing). But total treatment costs ($996-2,573) vary enormously by country and depend on what the philanthropic funder covers vs. the government. If a GiveWell-funded program covers only drug procurement for patients who would otherwise go untreated due to drug stockouts from US funding cuts, the per-patient cost is low and CE is high. If the program must also fund diagnostic capacity, clinical monitoring, and adherence support, costs are much higher.
- **Counterfactual mortality without treatment is uncertain.** The 2017 QEA cited one estimate that 70% of TB patients die within 10 years without treatment (Tiemersma et al. 2011). For MDR-TB specifically, outcomes may be worse — but some patients would receive standard (ineffective) TB treatment rather than no treatment at all. I'm assuming 50% 5-year mortality without MDR-TB-specific treatment, which is conservative relative to the Tiemersma estimate.
- **Only 5,646 patients globally received BPaLM in 2023.** Despite WHO recommendation since 2022, rollout has been slow — only 58 countries were using BPaLM/BPaL by end of 2023.[^12] The gap between trial evidence and programmatic implementation is large. Scaled-up treatment success rates may be lower than the 89% achieved in trials.
- **No identified GiveWell-type funding opportunity.** The TB space is dominated by the Global Fund, PEPFAR (now severely cut), and the Gates Foundation. There is no clear equivalent of a "GiveWell top charity" delivering MDR-TB treatment at scale that could absorb a directed grant. The most relevant organizations are the endTB partnership (PIH/MSF/IRD, funded by Unitaid) and the Global Drug Facility (Stop TB Partnership). Identifying a specific fundable opportunity would require further investigation.
- **AMR risk.** Resistance to bedaquiline has already been detected in some settings. If BPaLM resistance spreads before rollout is complete, the CE calculation would change.

## Who is implementing / funding this?

- **Global Drug Facility (Stop TB Partnership)** — The primary mechanism for procurement of MDR-TB drugs at reduced prices. BPaLM pricing negotiated down to $310/course. Distributes to 150+ countries.
- **endTB partnership (Partners In Health / MSF / IRD)** — Funded by Unitaid. Conducted the endTB and endTB-Q clinical trials. Operating treatment programs in 17 countries. Leading the evidence generation for WHO guideline updates.
- **Global Fund** — Largest multilateral funder of TB programs. Grant cycle cut by $1.4B in 2025. Supports TB diagnosis and treatment infrastructure in high-burden countries.
- **Gates Foundation** — Largest philanthropic TB funder. Investments in drug development (through TB Alliance), diagnostics, and country-level programs.
- **USAID** (severely curtailed as of 2025) — Previously the largest bilateral TB donor. Operations effectively ceased in many priority countries.
- **WHO Global TB Programme** — Sets guidelines, coordinates response, monitors progress. Updated recommendations to BPaLM in 2022 and again in 2024 based on endTB results.

## Recommended next steps

- **Talk to the endTB partnership (Partners In Health / MSF) about acute drug procurement gaps from US funding cuts.** The endTB partnership operates MDR-TB treatment programs in 17 countries and has the most direct operational experience with BPaLM rollout. The key question is: are there specific countries where drug stockouts are imminent due to USAID/Global Fund cuts, and could a targeted drug procurement grant ($1-5M) fill the gap for a defined number of patients? PIH's Dr. Carole Mitnick or MSF's Access Campaign would be well-placed contacts. If drug procurement is the binding constraint (rather than diagnostic capacity or health worker availability), this could be a relatively low-cost, high-leverage opportunity — $310/patient for BPaLM drugs with existing health systems covering the rest.

- **Assess the Global Drug Facility's capacity to absorb additional philanthropic funding.** The GDF negotiates drug prices and distributes to 150+ countries. If US funding cuts are creating drug access gaps, GDF may be the most efficient channel for philanthropic dollars. The question is whether additional funding would actually translate to more patients treated (rather than substituting for government procurement). Dr. Brenda Waning at Stop TB / GDF would be a relevant contact.

- **Investigate whether the 2025 funding crisis is creating time-limited high-leverage opportunities.** The combination of (a) dramatically improved treatment with BPaLM, (b) very low drug costs ($310/course), and (c) sudden collapse of ~50% of international TB funding may create a window where philanthropic dollars have unusually high leverage — filling acute gaps before other funders can scale up. This is analogous to the "bridge funding" concept in humanitarian response. The window may be 1-3 years before funding stabilizes. WHO's Global TB Programme could provide country-specific data on where the gaps are most acute.

---

[^1]: "In 2023, about 400 000 (95% UI: 355 000–450 000) people developed multidrug-resistant or rifampicin-resistant TB (MDR/RR-TB) [...] In 2023, 175 923 people with MDR/RR-TB were enrolled on treatment globally (44% of the estimated 400 000 new cases)." ([WHO Global TB Report 2024 — Drug-Resistant TB Treatment](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024/tb-diagnosis-and-treatment/2-4-drug-resistant-tb-treatment))

[^2]: "A shorter all-oral bedaquiline-containing regimen of 6 months for treatment of MDR/RR-TB (the BPaLM/BPaL regimen) is recommended in eligible patients with MDR/RR-TB aged ≥14 years, in preference to 9-month and 18-month or longer regimens." ([WHO treatment guidelines for drug-resistant TB, 2022 update](https://www.who.int/publications/i/item/9789240063129))

[^3]: "Treatment success was achieved in 89% of participants randomised to BPaLM [...] compared with 52%-75% in the standard-of-care group [...] The study was terminated early on the recommendation of the independent data safety monitoring board for benefit." ([TB-PRACTECAL, Lancet Respiratory Medicine 2023](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(23)00389-2/fulltext))

[^4]: "Three of the five experimental regimens showed non-inferiority to the control in the per-protocol population [...] Regimen 2 [bedaquiline, delamanid, linezolid, levofloxacin] showed superiority in the modified intention-to-treat population, with 90.4% favourable outcomes." ([endTB trial, NEJM 2024](https://endtb.org/endtb-clinical-trial-results))

[^5]: "A favorable outcome at 6 months after the end of treatment occurred in 98 of 109 patients (90%) [...] including 63 of 71 patients (89%) with extensively drug-resistant tuberculosis." ([Nix-TB, NEJM 2020](https://www.nejm.org/doi/full/10.1056/NEJMoa1901814))

[^6]: "At 26 weeks of treatment, the proportion of participants with a favorable outcome was [...] 91% with linezolid at a dose of 600 mg for 26 weeks [...] with significantly reduced peripheral neuropathy and myelosuppression." ([ZeNix, NEJM 2022](https://www.nejm.org/doi/full/10.1056/NEJMoa2119430))

[^7]: "91.0% (95% CI 82.6-95.6) of participants had a favourable status [...] in the 6-month bedaquiline-containing regimen." ([STREAM Stage 2, Lancet 2022](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(22)02078-5/fulltext))

[^8]: "Stop TB's Global Drug Facility (GDF) announces [...] a 47% decrease in the price of the BPaLM regimen [...] The full BPaLM treatment course is now available for USD $310." ([Stop TB Partnership, GDF price announcement](https://www.stoptb.org/news/stop-tbs-global-drug-facility-announces-38-price-decrease-bpalm-regimen-and-newly-available))

[^9]: [Note] Total treatment costs (drug + health system costs) estimated at $996-$2,573 across Pakistan, Philippines, South Africa, and Ukraine, based on country-level costing studies. BPaLM was found to be cost-saving compared to older regimens in all four countries.

[^10]: "Thirteen of USAID's 24 priority countries for TB depended on U.S. bilateral funding for at least 20% of their respective TB programs [...] The Global Fund grant cycle was cut by $1.4 billion (11%)." ([WHO Global TB Report 2025 — Impact of Funding Cuts](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/featured-topics/Impact-of-2025-funding-cuts))

[^11]: "Modeling suggests that if all U.S. bilateral TB activities were discontinued in 2025 for the 15 months of the 2025 U.S. government fiscal year and then resumed at 2024 levels, an additional 2.5 million pediatric TB cases and 340,000 pediatric TB deaths could occur over the 2025-2034 decade." ([PMC — Deadly Equation of US Funding Cuts](https://pmc.ncbi.nlm.nih.gov/articles/PMC12422474/))

[^12]: [Note] WHO Global TB Report 2024 states that 58 countries were using BPaLM/BPaL by end of 2023, with 5,646 patients started on these regimens globally in 2023 — out of approximately 176,000 MDR/RR-TB patients enrolled in treatment that year.
