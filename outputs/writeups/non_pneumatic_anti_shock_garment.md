# Review: QEA of Non-Pneumatic Anti-Shock Garment (NASG)

- Link to original QEA: [NASG QEA](https://docs.google.com/document/d/10ALE72O0VS6rkxrybbckYk_YBFNYAXnKdM0gAbobRBU/edit)
- Link to original BOTEC: [NASG BOTEC](https://docs.google.com/spreadsheets/d/1R9V-rtpUEtNRqoECtffF3y2PCvndTP0YNZpaswrtZak/edit)
- Year the original analysis was conducted: 2020

## What is this (basic context)

- **What is the problem?** Obstetric hemorrhage is the leading cause of maternal mortality, accounting for approximately 35% of all maternal deaths worldwide.[^1] In sub-Saharan Africa, women experiencing hemorrhagic shock face long delays in transport to referral facilities and in receiving definitive treatment (blood transfusion, surgery). Without intervention, death from hemorrhage can occur within four hours of onset.[^2]
- **What is the program?** The NASG is a neoprene compression garment that applies circumferential counter-pressure to the lower body, legs, pelvis, and abdomen. It reverses hypovolemic shock, reduces blood loss, and stabilizes women during transport to higher-level facilities. The device costs $57–100, can be reused 40–72 times, and can be applied in less than 2 minutes by anyone with basic training.[^3] WHO, FIGO, and GLOWM recommend the NASG as a temporizing device for women with obstetric hemorrhage.
- **Why did we deprioritize this?** The original QEA rated this as "highly promising" (CE 5–15x depending on cost assumptions) but flagged high uncertainty about: (1) programmatic cost per woman treated ($8 was a guess), (2) the strength of the evidence base (one underpowered RCT + 5 observational studies), and (3) room for more funding. Next steps were to talk with CHAI about funding gaps and costs.

## Key updates

- **CHAI Zimbabwe pilot shows strong real-world results (2019–2021).** CHAI introduced the NASG in 34 health facilities in Hurungwe District, Mashonaland West Province. After a three-month evaluation, the device was used in 90% of potential applications and there were 50% fewer maternal deaths compared to the same period a year earlier — including zero deaths from postpartum hemorrhage.[^4] Following these results, the Zimbabwe Ministry of Health and Child Care adopted the NASG as part of the standard package for management of third-stage labor complications, and rolled out the device to 176 additional facilities in the province plus five central hospitals.[^5]

- **Zambia process evaluation confirms feasibility (2023).** A published process evaluation of NASG introduction in Northern Province, Zambia documented operational feasibility of integrating the device into the public health system.[^6] This addresses one of the original QEA's key implementation concerns — whether the return-and-exchange policy between primary and referral facilities would work in practice.

- **No new RCTs, and authors say none are feasible.** The evidence base has not changed since the original assessment. The sole RCT (Miller et al. 2013, Zambia/Zimbabwe, n=887, 15 deaths) remains underpowered with a non-significant but large effect (OR 0.36, 95% CI 0.08–1.53).[^7] The control group received NASG at referral hospitals, so the trial measured early vs. late application, not NASG vs. no NASG. The authors explicitly stated that an adequately powered RCT is unlikely to be repeated.[^8] The pooled non-experimental evidence (5 studies, n=2,330) shows RR 0.52 (95% CI 0.36–0.77) for mortality.[^9]

- **E-MOTIVE trial supports bundled PPH approach.** The E-MOTIVE trial (NEJM 2023, n=210,132 across Kenya/Nigeria/South Africa/Tanzania) found that a bundled early detection + treatment protocol for PPH reduced severe bleeding by 60% (RR 0.40).[^10] While E-MOTIVE's first-response bundle does not include the NASG directly, the NASG fits naturally into the escalation pathway for women who do not respond to initial treatment. E-MOTIVE's success demonstrates that bundled, protocol-driven PPH management works in SSA facility settings, which is the same delivery model NASG requires.

## New CE estimate

My best guess is **~10x cash at $12/woman treated (range ~5x at $25/woman to ~15x at $8/woman)**. The CE is highly sensitive to the cost per woman treated, which remains poorly characterized. See [non_pneumatic_anti_shock_garment BOTEC](../botecs/non_pneumatic_anti_shock_garment.xlsx).

The key parameters:
- Baseline mortality among women with obstetric hemorrhage: 1.6% (from RCT control group, adjusted for country-level mortality reductions since 2010)
- Pooled mortality reduction: 48% (RR 0.52), adjusted to 24% after 50% combined IV/EV adjustment
- Moral weight: 109.5 UoV per maternal death averted (average age 27–30)
- At $12/woman: ~83,333 women covered per $1M grant → ~320 deaths averted (adjusted) → ~35,000 UoV → ~10x cash

The CE is comparable to several other interventions near GiveWell's bar, and the intervention has the advantage of being extremely simple to implement and already adopted by at least one national health system.

## Remaining uncertainties

- **Cost per woman treated is the pivotal unknown.** The original BOTEC used $8/woman as a "guess for implementing NASG + training." The device cost is well-characterized (~$1/use after amortization), but training, supervision, logistics, and the return-and-exchange system add uncertainty. CHAI Zimbabwe estimated $750k for a 5-year national scale-up covering garment procurement and training, but this excluded broader programmatic activities and CHAI staff time.[^11] I'm assuming $12/woman as a best guess midpoint. Actual programmatic cost data from Zimbabwe or Zambia would resolve this.
- **Evidence quality remains weak.** The pooled RR 0.52 comes from observational studies with potential confounding. The 50% IV/EV adjustment attempts to account for this, but the true effect could be substantially smaller. The RCT point estimate (OR 0.36) is actually larger than the observational pooled estimate, which is somewhat reassuring, but it is far from significant.
- **Coverage among hemorrhaging women.** The BOTEC assumes NASG reaches all women with obstetric hemorrhage at participating facilities. In practice, some women may hemorrhage before reaching a facility, or the NASG may not be available at the moment of need. The Zimbabwe pilot's 90% usage rate is encouraging but may not be sustained at scale.
- **Return-and-exchange logistics.** If a woman receives NASG at a primary health center and is transferred to a referral hospital, the garment must be returned. Failure to return garments would dramatically increase per-use costs ($75/woman instead of ~$1). The Zambia process evaluation addresses this concern but long-term data is limited.

## Who is implementing / funding this?

- **CHAI** has been the primary implementer, with programs in Zimbabwe (national rollout underway), Ethiopia (661 health centers + 59 hospitals as of 2013), and pilot work in Zambia.
- **Pathfinder International** distributed 2,043 NASGs across 6 Indian states by 2012, with cost-sharing from Tamil Nadu state government.
- **UNFPA** supported scale-up in Nigeria (Sokoto and Kebbi states) following Pathfinder's advocacy.
- **Government of Zimbabwe** has adopted NASG as national policy and is leading scale-up with CHAI support.

## Recommended next steps

- **Obtain actual cost-per-woman data from CHAI Zimbabwe and Zambia.** This is the single most important unknown. CHAI has now implemented NASG across 176+ facilities in Mashonaland West and is expanding nationally — they should have real cost data. I'd recommend talking to **Andrew Storey at CHAI** (the contact mentioned in the original QEA correspondence with Teryn) who has direct experience with the Zimbabwe program.
- **Investigate whether NASG can be bundled with the E-MOTIVE protocol.** E-MOTIVE's first-response PPH bundle (drape + massage + oxytocin + TXA + IV fluids) reduced severe PPH by 60%. NASG could serve as the escalation device for non-responders. A bundled approach would share training, supervision, and facility infrastructure costs. The **WHO Department of Maternal, Newborn, Child and Adolescent Health** is leading E-MOTIVE's transition to implementation guidance and would be the relevant body to engage.
- **Consider alongside the uterotonics PPH QEA.** The NASG (treatment/stabilization for hemorrhagic shock) and heat-stable carbetocin (prevention of PPH) address different parts of the same problem. A comprehensive PPH package — prevention (HSC), treatment (TXA + NASG), and early detection (E-MOTIVE drape) — could be more fundable as a unified platform than individual components. Unitaid's AMPLI-PPHI program (scaling HSC in 6 countries, expected cost data mid-2026) could provide the delivery infrastructure.

---

[^1]: "Obstetric haemorrhage is the leading cause of maternal mortality. It constitutes 35% of all maternal deaths." ([WHO, Postpartum haemorrhage](https://www.who.int/docs/default-source/mca-documents/nbh/brief-postpartum-haemorrhage))

[^2]: "It takes less than four hours from the onset of hemorrhage, on average, to die, but the condition can only be treated in hospital." ([CHAI blog, Anti-shock garment prevents maternal deaths in rural Zimbabwe](https://www.clintonhealthaccess.org/blog/anti-shock-garment-prevents-maternal-deaths-in-rural-zimbabwe/))

[^3]: "The device costs USD 57.50 from one manufacturer in Hong Kong, and can be re-used at least 72 times." and "After training, any trained birth attendant can rapidly apply the NASG on a hemorrhaging woman." ([Barriers and facilitators to scaling up NASG, cited in original QEA](https://docs.google.com/document/d/10ALE72O0VS6rkxrybbckYk_YBFNYAXnKdM0gAbobRBU/edit))

[^4]: "CHAI introduced the NASG in 34 health facilities in the Hurungwe District in Mashonaland West Province and conducted a three-month evaluation. The results were significant: the NASG was used in 90 percent of potential applications and there were 50 percent fewer maternal deaths compared to the same time period a year earlier – including no deaths from postpartum hemorrhage." ([CHAI, Anti-shock garment prevents maternal deaths in rural Zimbabwe](https://www.clintonhealthaccess.org/blog/anti-shock-garment-prevents-maternal-deaths-in-rural-zimbabwe/))

[^5]: "Following these results, the MOHCC, with support from CHAI, used the results of the study to enable the roll out of the NASG to the rest of the 176 facilities in the province, as well as five central hospitals. The MOHCC has since adopted the NASG as part of the package for management of third stage labor complications, which will be rolled out nationally in the coming months." ([CHAI, Anti-shock garment prevents maternal deaths in rural Zimbabwe](https://www.clintonhealthaccess.org/blog/anti-shock-garment-prevents-maternal-deaths-in-rural-zimbabwe/))

[^6]: [Note] Published in BMC Health Services Research (2023): "Operational demonstration and process evaluation of non-pneumatic anti-shock garment (NASG) introduction to the public health system of Northern Province, Zambia" (PMC10687818). I have not read the full paper but the publication confirms operational feasibility was documented.

[^7]: "There was no evidence of statistically significant differences between earlier and later NASG application across mortality and morbidity outcomes. The odds of death in the early application group were 64% lower (OR 0.36 (95% CI: 0.08 – 1.53) than the later application group." ([Miller et al. 2013, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0076477))

[^8]: "Given the increasing global practice of prophylactic uterotonics and improved management of early PPH, we feel that obtaining a sample size adequate to demonstrate a statistically significant decrease in maternal mortality, even with the large effect size of the NASG, in a cluster randomized trial, is unattainable." ([Miller et al. 2013, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0076477))

[^9]: [Note] Random effects meta-analysis of Pileggi-Castro et al. 2015 systematic review: 5 non-experimental studies, pooled RR 0.52 (95% CI 0.36–0.77). Studies: Miller 2006, Miller 2010, Ojengbede 2011, Magwali 2012, Maknikar 2012.

[^10]: "The incidence of the primary outcome was lower in the E-MOTIVE group than in the usual-care group (5859 of 106,021 women [5.5%] vs. 9221 of 104,111 [8.9%]; relative risk, 0.60; 95% confidence interval [CI], 0.51 to 0.71; P<0.001)." ([Gallos et al., NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2303966))

[^11]: [Note] From original QEA correspondence with Andrew Storey at CHAI: "$750,000 for national scale-up of NASG in Zimbabwe. Does not include broader programmatic activities or CHAI staff time and expenses, and assumes that CHAI is able to layer activities onto existing projects." Duration: 5 years.
