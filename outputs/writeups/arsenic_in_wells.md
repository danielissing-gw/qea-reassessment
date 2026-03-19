# Review: QEA of Arsenic in Wells (Bangladesh)

- Link to original QEA: No writeup exists
- Link to original BOTEC: [Arsenic BOTEC](https://docs.google.com/spreadsheets/d/1ATbZ61dmczX3GB3Mo-nwITfsMcTikpGmlzG-D83xu5Y/)
- Year the original analysis was conducted: 2021

## What is this (basic context)

- **What is the problem?** Naturally occurring arsenic contaminates shallow tube-well water across much of Bangladesh (and parts of India, Cambodia, and Nepal). An estimated 20 million Bangladeshis drink water with arsenic exceeding 50 ug/L — the Bangladesh standard — causing an estimated 24,000 adult deaths per year from cancer, cardiovascular disease, and other chronic conditions.[^1] Arsenic exposure is also associated with adverse pregnancy outcomes including stillbirth and infant mortality.[^2]
- **What is the program?** Testing wells for arsenic contamination using low-cost field kits (~$0.17–1.00/test) and informing households of results via placards and education. Households with high-arsenic wells are encouraged to switch to nearby safe wells. This is a behavioral intervention — the testing itself is cheap, and in many areas safe wells already exist nearby; the barrier is information, not infrastructure.
- **Why was there no writeup?** The original produced only a BOTEC — no writeup or further investigation notes. The BOTEC estimated ~18x cash transfers, which is high, but several parameters (moral weights of 106 for adults and 100 for infants) were labeled "guess" and the model used only observational evidence from the HEALS cohort. My guess is that it was deprioritized due to the lack of a clear implementer and the absence of experimental evidence on mortality.

## Key updates

- **HEALS 20-year follow-up confirms causal mortality effect (JAMA 2025).** The Health Effects of Arsenic Longitudinal Study — the same cohort used for the original BOTEC's hazard ratios — has now published a 20-year follow-up (10,977 adults, 1,401 chronic disease deaths). Participants whose arsenic exposure fell from high to low had a 54% reduced risk of death from chronic disease, 57% from cardiovascular disease, and 49% from cancer.[^3] This is the strongest evidence to date that reducing arsenic exposure causally reduces mortality — the key uncertainty in the original assessment.

- **Well-switching rates are consistently higher than assumed.** The original BOTEC used a 35% switching rate. Multiple studies find higher rates: 60% within one year in Araihazar (with placards and counseling),[^4] 53% in the Singair cluster RCT,[^5] and 37% even with a low-cost informational intervention alone.[^6] A central estimate of 45% is more appropriate and still conservative relative to the best-performing programs. Switching is also remarkably persistent — Araihazar data shows sustained switching over 8–15 years, with new switching continuing to occur years after initial testing.[^7]

- **The space is highly neglected.** Despite 20 million Bangladeshis still drinking high-arsenic water, there are no major current international programs focused on arsenic mitigation. The Bangladesh government's ARRP tested 6.3 million wells (2021–2023), but this used a national standard of 50 ug/L (5x the WHO guideline of 10 ug/L) and did not include sustained behavioral follow-up.[^8] UNICEF, World Bank, and WHO do not currently have large arsenic programs. This is one of the most neglected environmental health problems relative to its burden.

## New CE estimate

My best guess is **~8x cash at $5/well all-in cost (range ~3x at $10/well with heavy IV discount to ~13x at $3/well)**. The CE is driven by adult chronic disease mortality (the primary benefit) and infant mortality (a secondary benefit), and is sensitive to per-well cost and the moral weight assigned to adult deaths. See [arsenic_in_wells BOTEC](../botecs/arsenic_in_wells.xlsx).

The original BOTEC estimated ~18x using more favorable assumptions: $2.30/well, 35% switching, 5-year benefit duration, and moral weights of 106 (adult) and 100 (infant). My updated BOTEC uses more conservative moral weights (50 for adults 15–49, 20 for adults 50+, 52.5 for infants — all closer to GW standard values) but a higher switching rate (45%), longer benefit duration (8 years, supported by Araihazar persistence data), and an additional benefit stream for chronic disease mortality in adults 50+ (based on the 2025 JAMA HEALS results). The large drop from 18x to ~8x is driven primarily by the moral weight correction — the original's 106 UoV for adult deaths was far above GW's typical range of 30–50. At $3–4/well (plausible if integrated into existing community health worker networks like BRAC), CE rises to 10–13x.

The key caveat is that all mortality evidence is observational — there is no RCT on arsenic mitigation and mortality. The HEALS cohort provides very strong observational evidence (20-year follow-up, large sample, dose-response), but GW's standard framework would apply meaningful IV discounts. I'm applying a 70% IV adjustment to reflect this.

## Remaining uncertainties

- **All-in program cost per well is the pivotal unknown.** Field test kits cost $0.17–1.00, but a program includes labor, logistics, education, and placard materials. A comprehensive informational intervention costs ~$6–10/household.[^9] Van Geen et al. found a cost of $0.90/person whose exposure was reduced (equivalent to ~$10/well).[^10] My $5/well assumption is between bare-minimum testing and a full education program — actual costs would depend on program design.
- **No RCT on mortality from well-testing programs.** The HEALS study is a prospective cohort, not an RCT. The 2025 JAMA results are the strongest observational evidence available, but confounding cannot be fully ruled out (e.g., people who switch wells may also be healthier, wealthier, or more health-seeking). I apply a 70% IV adjustment for this, but the true discount could be larger.
- **Availability of safe wells nearby.** The intervention only works if households have access to an alternative safe water source within walking distance. In Araihazar (where most studies were conducted), safe wells are typically available because arsenic contamination is patchy — neighboring wells may be safe. This may not hold in all regions.
- **No clear implementer.** There is no NGO currently running a well-testing program at scale that GW could fund. Columbia University's research group (led by Alexander van Geen) has done the most extensive work but operates as a research program, not a service delivery organization. Building or identifying an implementer would be a prerequisite for GW funding.
- **Moral weights for adult chronic disease deaths.** Adults dying of arsenic-related cancer and cardiovascular disease are typically 40–70 years old. GW's standard framework values these deaths less than child deaths, but the appropriate weight is uncertain. I use 50 UoV for adults 15–49 and 20 UoV for adults 50+ — both conservative relative to the original BOTEC's 106 UoV.

## Who is implementing / funding this?

- **Bangladesh government** — The Arsenic Risk Reduction Program (ARRP) tested 6.3 million wells (2021–2023) using smartphone-based digital recording. However, this is testing infrastructure, not a sustained behavioral change program.
- **Columbia University / Lamont-Doherty Earth Observatory** — Alexander van Geen's research group has tested >10,000 wells in Araihazar and demonstrated the effectiveness of blanket testing at ~$0.90/person. This is the primary research group working on arsenic well-testing.
- **UNICEF** — Conducted demonstration projects in Bangladesh from 2006–2011 at $11/capita for safe water provision, but does not currently have a major arsenic mitigation program.
- **No major current international funder.** This is a striking gap given the burden (24,000 deaths/year in Bangladesh alone).

## Recommended next steps

- **Talk to Alexander van Geen (Columbia University / Lamont-Doherty) about a scalable well-testing program.** Van Geen has the most extensive operational experience with well-testing in Bangladesh and has demonstrated costs as low as $0.90/person for reducing arsenic exposure. The key question is whether this research-based model can be converted into a scalable service delivery program, and what the per-well cost would be at 100,000+ well scale. He could also identify local organizations (e.g., BRAC, which operates community health programs at massive scale in Bangladesh) that could deliver the intervention.

- **Assess whether BRAC or a similar Bangladeshi NGO could integrate well-testing into existing programs.** BRAC's community health worker network already covers most of rural Bangladesh. Adding arsenic well-testing to their existing door-to-door visits could dramatically reduce per-well costs. If the incremental cost is $2–3/well (test kit + brief education), CE could reach 15–20x. The question is whether BRAC has organizational interest and capacity to add this to their platform.

- **Verify availability of safe alternative wells.** The CE calculation assumes households can switch to a nearby safe well. This is supported by data from Araihazar (where arsenic is geographically patchy), but should be verified for the specific regions where a program would operate. The Arsenic 4M project (2023–2024) piloted digital mapping of arsenic levels in Bangladesh — their maps could help identify regions where safe alternatives are most accessible.[^11]

---

[^1]: "Arsenic exposures to concentrations >50 ug/L and 10–50 ug/L account for an annual 24,000 and perhaps as many as 19,000 adult deaths [...] representing about 5.6% of all deaths" in Bangladesh. ([Flanagan et al., Bulletin of the WHO 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3506399/))

[^2]: "Arsenic in groundwater (≥50 ug/L) was associated with: spontaneous abortion OR = 1.98, stillbirth OR = 1.77, neonatal mortality OR = 1.51, infant mortality OR = 1.35." ([Rahman et al., meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC4421764/))

[^3]: "People whose urinary arsenic levels fell from high to low had mortality rates that matched those who had consistently low exposure for the entire study [...] 54% reduced risk of death from any chronic disease, 57% reduction for cardiovascular disease, and 49% reduction for cancer." ([HEALS 20-year follow-up, JAMA 2025](https://www.nih.gov/news-events/nih-research-matters/arsenic-reduction-linked-lower-risk-death))

[^4]: "60% of the people who realized they were using contaminated well switched to a safe well within 1 year." ([Jameel et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8670558/))

[^5]: "Overall, 53% of respondents using As contaminated wells, relative to the Bangladesh As standard of 50 ug/L, at baseline switched after receiving the intervention." ([George et al. 2012, cluster RCT](https://pmc.ncbi.nlm.nih.gov/articles/PMC3506475/))

[^6]: "37% of households who received the intervention (Groups A1 and A2) reported changing their water source or treatment" vs. only 10% in the control group. ([Barnwal et al. 2023, PNAS Nexus](https://pmc.ncbi.nlm.nih.gov/articles/PMC10042277/))

[^7]: "Not only was 2003–2005 switching highly persistent, but also new switching by 2008 doubled the share of households at unsafe wells who had switched." ([Pfaff et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC6449151/))

[^8]: [Note] The Bangladesh ARRP (2021–2023) tested 6.3 million wells using a digital/smartphone system. However, the program used Bangladesh's national standard of 50 ug/L — 5x the WHO guideline of 10 ug/L — meaning many wells that are unsafe by international standards were classified as safe. The program was primarily a testing exercise, not a sustained behavioral change intervention.

[^9]: "Less than USD 10 per household" for a comprehensive informational intervention including lab testing, with potential to be "lowered by 30 to 40% if certain field test kits were used." ([Barnwal et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10042277/))

[^10]: "The most recent testing probably led about 132,000 inhabitants to switch away from their high As well. This remarkable change was obtained at a cost of US$0.90 per person." ([van Geen et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6535723/))

[^11]: [Note] The Arsenic 4M project (May 2023–April 2024) piloted the first rapid digital cloud-connected arsenic test in Bangladesh, producing real-time maps of contamination levels. This technology could enable targeted well-testing programs focused on areas with the highest contamination and the greatest density of nearby safe alternatives.
