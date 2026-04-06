# Review: SCD Screening and Hydroxyurea Treatment

- Link to original analysis: CHAI memo and BOTEC (July 2023, shared internally; no formal QEA published)
- Year the original analysis was conducted: 2023

## What is this (basic context)

- **What is the problem?** Sickle cell disease (SCD) is the world's most common inherited blood disorder. In 2021, an estimated 515,000 babies were born with SCD globally, and ~81,100 children under 5 died from SCD — making it the 12th leading cause of under-5 mortality worldwide.[^1] Nigeria accounts for roughly one-third of the global burden, with ~100,000 SCD births and ~24,400 under-5 deaths annually.[^1] Without treatment, median survival in SSA is estimated at 5–18 years depending on genotype.
- **What is the program?** Newborn screening using point-of-care diagnostics integrated into delivery wards and EPI visits, followed by hydroxyurea (HU) treatment starting at 6 months, plus supporting therapies (folic acid, penicillin prophylaxis, PCV vaccine). The CHAI model proposed a 5-year program in Nigeria covering children 0–5, with a year-1 catch-up campaign for existing under-5s.

## Key updates

- **Hydroxyurea is now the only oral disease-modifying therapy for SCD.** Both crizanlizumab (Adakveo, Novartis) and voxelotor (Oxbryta, Pfizer) have been withdrawn globally — crizanlizumab after Phase III STAND trial failed to confirm benefit, and voxelotor due to an imbalance in fatal events.[^2][^3] This leaves HU as the sole affordable, scalable treatment option for SCD in LMICs, strengthening the case for HU-focused programs.

- **WHO added hydroxyurea to the core Essential Medicines List and Children's EML (September 2025).** HU was transferred from the complementary to the core list and added to the Children's EML for the first time, with a dedicated SCD sub-section created.[^4] This is a significant policy milestone: core EML listing facilitates government procurement, insurance reimbursement (e.g., Ghana's NHIS is actively costing HU inclusion), and regulatory approval in countries that reference the WHO list.

- **REACH trial 8-year follow-up confirms long-term safety and efficacy of HU in SSA children.** The extended follow-up (Lancet Haematology 2024) of 606 children across DRC, Uganda, Kenya, and Angola showed sustained benefit at maximum tolerated dose (MTD) over 4,340 patient-years: transfusion rates dropped 75% vs. pre-treatment, with no increase in toxicities.[^5] A 2025 meta-analysis also found HU decreases stroke risk (TCD velocity −30 cm/s), supporting it as an alternative to chronic transfusions for stroke prevention in resource-limited settings.[^6]

- **Gene therapy is not reaching SSA.** Casgevy (CRISPR-based) was approved by FDA and EMA but costs $2.2M per treatment and has only been administered to 64 patients globally as of 2025.[^7] No LMIC approvals or access programs exist. The NIH/BMGF $200M in vivo gene therapy collaboration has progressed to Phase 2 trials but is at least 5–10 years from LMIC deployment.[^8] Gene therapy will not resolve the treatment gap in the foreseeable future.

## New CE estimate

My best guess is **~3x cash with a 50% sustainability discount, or ~6x at face value** (no sustainability discount). The intervention could reach **~10x in a treatment-only setting (e.g., Uganda or Ghana) if lifelong treatment is ensured**. See [sickle_cell_disease BOTEC](../botecs/sickle_cell_disease.xlsx).

The original CHAI BOTEC estimated 7–11x over 5 years (Nigeria, full screening + treatment program). My estimate is lower for three reasons:

1. **Stricter IV/EV adjustments.** CHAI used 89% IV and 97.5% EV; I'm using 65% IV (pre-post study with increased monitoring, no RCT) and 80% EV (research sites vs. national implementation, plus CONSA data showing only 38.5% of screened babies had a documented clinical visit).

2. **Adherence discount (20%).** CHAI did not model adherence. HU requires daily oral administration by caregivers, with no widely available child-friendly liquid formulation. US studies show 60–80% adherence among children.[^9]

3. **Sustainability discount (50% on mortality benefits).** This is the most important adjustment. SCD requires lifelong treatment, but the proposed program only covers ages 0–5. Averting a death at age 2 has full value only if the child lives to normal life expectancy — but if HU access stops at 5, mortality risk rebounds. I'm assuming a 50% discount on the mortality moral weight, reflecting a mix of outcomes: ~30% chance of lifelong access (government uptake), ~30% survival to ~25 without treatment (milder genotypes), ~40% death before 20. Morbidity benefits (pain crises averted, stroke prevention) are realized during the program period and don't require this discount.

## Remaining uncertainties

- **Sustainability is the pivotal question.** The entire CE case hinges on whether children retain HU access after age 5. The CHAI memo discussed three models: (a) government takes over procurement, (b) an HU endowment for lifelong treatment, (c) gene therapy becomes available. Model (a) is now more plausible with WHO core EML listing, and Ghana is actively costing HU into its NHIS. But no SSA government currently provides routine HU for SCD children. Without a concrete plan for post-program treatment, the sustainability discount dominates the BOTEC.

- **No RCT for HU mortality reduction in SSA children.** The 70% mortality reduction (IRR 0.30) comes from the REACH trial, a pre-post design where children received substantially more care in the treatment period. The 8-year follow-up strengthens the case but does not resolve the confounding concern. A meta-analysis of 3 small RCTs (n=423) confirms HbF improvement but did not directly measure mortality.[^10] A well-powered RCT would resolve this, but is unlikely given HU's established efficacy in HICs.

- **Screening-to-treatment cascade is fragile.** CONSA data (158,736 babies screened across 7 SSA countries) shows 2,201 identified with SCD but only 847 (38.5%) had a documented initial clinical visit.[^11] Bridging screening to sustained treatment is a major implementation challenge that the CHAI model's coverage assumptions may understate.

- **Cost structure varies enormously by setting.** Full Nigeria program (screening + treatment + TA): ~$60/child-year. Treatment-only in Uganda or Ghana (where screening exists): ~$35/child-year. HU drug cost alone: ~$18/year. The CE swings from 3x to 10x across this cost range.

## Who is implementing / funding this?

- **CHAI** — Developed the original BOTEC and program design. Has SCD screening and treatment programs in Nigeria and other SSA countries.
- **Novartis Africa SCD Program** — Active in Ghana (since 2019), Uganda, Tanzania, Kenya, Angola, Zambia. Registered HU for SCD in multiple SSA countries. Provides child-friendly formulation (Siklos). >2,000 patients treated, >60,000 treatments delivered in Ghana.
- **ASH (American Society of Hematology)** — Funds the CONSA screening consortium across 7 countries. Established Center for SCD Initiatives (2024). Published 10-year impact report (2025).
- **NIH/NHLBI + BMGF** — $200M joint commitment for in vivo gene-based cures. Cure Sickle Cell Initiative Phase 2 trial launched 2024.
- **Unitaid/Global Fund** — Limited direct SCD engagement, but relevant as funders of diagnostic platforms that could integrate SCD screening.

## Recommended next steps

- **Investigate the treatment-only model in Uganda or Ghana.** These countries have existing screening infrastructure (CONSA sites, Novartis program) and HU regulatory approval. A program focused solely on ensuring HU access for already-diagnosed children would have much lower costs (~$35/child-year) and higher CE. **Dr. Isaac Odame** (Hospital for Sick Children, Toronto / SickleInAfrica consortium) leads NBS implementation research across SSA and could identify specific sites where screening is active but treatment access is the bottleneck.

- **Assess feasibility of an HU endowment or government co-funding model.** The sustainability problem is solvable if lifelong treatment can be financed. Ghana's progress on NHIS inclusion of HU is the most advanced example — understanding the timeline, cost, and replicability of this model would directly resolve the dominant uncertainty in the BOTEC. **Dr. Tsiri Agbenyega** (Kwame Nkrumah University of Science and Technology / Ghana SCD program) has led the Novartis partnership and would have direct insight into the government uptake pathway.

- **Monitor the in vivo gene therapy timeline.** The NIH/BMGF in vivo gene therapy program (aiming for a single-administration cure deliverable like a blood transfusion) could eventually make HU programs obsolete — but the timeline is 7–10+ years. If it accelerates, the sustainability discount shrinks dramatically. The Phase 2 trial results (expected ~2027) will be the key signal.

---

[^1]: "The total number of SCD-attributable deaths, including both SCD as a cause and a risk factor, was estimated at 376,000 in 2021 [...] 81,100 (95% UI: 58,800–108,000) SCD-attributable deaths occurred in children under 5 years of age, making SCD the 12th leading cause of under-5 mortality." ([GBD 2021 SCD study, Lancet Haematology 2023](https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(23)00118-7/fulltext))

[^2]: "MHRA revoked the marketing authorisation for crizanlizumab [...] The Phase III STAND trial did not confirm the clinical benefit." ([Sickle Cell Society, January 2024](https://www.sicklecellsociety.org/crizanlizumab-statement-january-2024/))

[^3]: "Pfizer has decided to voluntarily withdraw the global approvals for voxelotor (marketed as Oxbryta) [...] following an imbalance in vaso-occlusive crises and fatal events." ([Pharmaceutical Journal, September 2024](https://pharmaceutical-journal.com/article/news/manufacturer-withdraws-treatment-for-sickle-cell-disease-following-concern-over-deaths))

[^4]: [Note] WHO Essential Medicines List, 24th edition (September 2025): hydroxycarbamide transferred from complementary to core list; added to Children's EML for the first time; dedicated SCD sub-section created within Section 10.3. Source: [WHO EML](https://list.essentialmeds.org/medicines/93).

[^5]: "606 children received hydroxyurea; 522 (86%) were treated for a median of 93 months, accumulating 4,340 patient-years of treatment. [...] Transfusion rates dropped by 75% compared to pre-treatment during the MTD phase." ([REACH 8-year follow-up, Lancet Haematology 2024](https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(24)00078-4/abstract))

[^6]: "Hydroxyurea decreased transcranial Doppler velocity by a mean of −30 cm/s over 0.5–2.6 years, with TCD normalizing in most children." ([ASH Blood Global Hematology 2025](https://ashpublications.org/bloodglobal/article/1/1/100001/535647/Hydroxyurea-to-decrease-stroke-risk-in-children))

[^7]: [Note] Casgevy (exagamglogene autotemcel) FDA-approved Dec 2023, EU Feb 2024. Lists at $2.2M per treatment. Only 64 patients received infusions globally as of 2025 for SCD or TDT. No LMIC approvals. Source: [BioSpace](https://www.biospace.com/drug-development/sickle-cell-gene-therapies-casgevy-and-lyfgenia-still-lacking-traction-2-years-in).

[^8]: [Note] NIH/BMGF $200M joint commitment (2019) for in vivo gene-based cures. Phase 2 trial launched 2024. Target: single-administration cure deliverable in SSA settings without specialized infrastructure. Source: [NHLBI Cure SCI](https://www.nhlbi.nih.gov/science/cure-sickle-cell-initiative).

[^9]: [Note] Adherence data from US studies: one study of children 1–17 found median adherence ~70% by pharmacy refill data (PMID 37046404). Caregiver education is critical, especially for asymptomatic children receiving prophylactic treatment. No large-scale SSA adherence data for HU in children exists.

[^10]: "Included 3 RCTs (423 participants). Found significant improvement in fetal hemoglobin (HbF) with a mean difference of 9.45% (95% CI: 2.15–16.75)." ([Narra X 2024](https://narrax.org/main/article/view/164))

[^11]: "158,736 babies screened; 2,201 (1.39%) identified with SCD; 25,708 (16.20%) with sickle trait. Of identified SCD cases, only 847 (38.5%) had a documented initial clinical visit." ([ASH CONSA 2024](https://ashpublications.org/blood/article/146/Supplement%201/944/552274/The-ASH-consa-consortium-on-newborn-screening-in))
