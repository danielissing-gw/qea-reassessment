# Review: QEA of Multiple Micronutrient Supplementation (MMS) During Pregnancy

- Link to original QEA: [MMS in pregnancy QEA](https://docs.google.com/document/d/1llIpGF1bVTQDmHM0RJ-lY0YcsA4FRpE_WuKb-ImReRk/edit)
- Link to original BOTEC: [MMS BOTEC](https://docs.google.com/spreadsheets/d/1uSnYDg1KZY1-iTQWuvBXZC4es7krjwPnYNH-bqxEgbg/edit)
- Year the original analysis was conducted: 2021

## What is this (basic context)

- **What is the problem?** Micronutrient deficiencies are common among pregnant women in LMICs, contributing to low birthweight (LBW), preterm birth, and small-for-gestational-age births. In South Asia, approximately 28% of births are LBW.[^1] The standard of care — daily iron and folic acid (IFA) supplementation — addresses only two of many common deficiencies.
- **What is the program?** Replacing daily IFA with daily multiple micronutrient supplements (MMS) containing 15 vitamins and minerals (the UNIMMAP formulation), taken throughout pregnancy (~180 tablets). MMS includes iron (30mg vs. 60mg in standard IFA), folic acid, and 13 additional micronutrients including vitamins A, C, D, zinc, selenium, and iodine.[^2]
- **Why did we deprioritize this?** The original 2021 QEA estimated CE at ~7x (range 2-14x), with costs being the "huge uncertainty." The moral weight for averting an LBW birth (3 UoV) was a rough guess. WHO recommended MMS only "in the context of rigorous research," and there were concerns about reduced iron content (30mg vs. 60mg).

## Key updates

- **WHO included UNIMMAP MMS on the Essential Medicines List (2021) and upgraded its recommendation (2020).** WHO's 2020 guidance shifted MMS from "not recommended" to "recommended in the context of rigorous research."[^3] In 2021, UNIMMAP MMS was added to WHO's Model List of Essential Medicines — a major endorsement that facilitates government procurement and integration into national ANC programs.[^4]

- **Kirk Humanitarian has committed $125M and reached 75 million pregnant women in 111 LMICs.** Kirk Humanitarian has purchased and donated UNIMMAP MMS reaching 75 million pregnant women across 111 countries.[^5] Since 2024, Kirk Humanitarian committed $92 million to UNICEF and the Child Nutrition Fund, providing MMS to 43 million women.[^6] At their procurement scale, UNIMMAP MMS costs $0.0118/dose or $2.13/pregnancy for 180 tablets — comparable to IFA costs.[^7] This massive scale-up demonstrates feasibility and has driven commodity costs down substantially.

- **New meta-analyses (2024-2025) confirm and extend the evidence base.** A 2025 systematic review and meta-analysis found that prenatal MMS reduces stunting (RR 0.86, 95% CI 0.82-0.91), underweight (RR 0.86, 95% CI 0.81-0.90), and small head circumference (RR 0.84, 95% CI 0.79-0.90) at 3 months, with effects persisting through 24 months.[^8] A separate 2025 IPD meta-analysis (15 RCTs, 61,204 women) found that high adherence (≥90%) was associated with a 44g increase in birthweight and reduced LBW risk (RR 0.93), while low adherence (<75%) was associated with increased stillbirth risk (RR 1.43).[^9] The 2019 Cochrane review findings (RR 0.88 for LBW, I²=0%, high-quality evidence) remain confirmed and are now supported by this broader evidence base.

- **Copenhagen Consensus 2023 named MMS one of 12 best investments for global development.** The analysis estimated that replacing IFA with MMS costs just $84 million per year globally, while generating $3.16 billion in benefits — more than $37 return per dollar spent.[^10] UNIMMAP MMS was also named one of TIME's Best Inventions of 2025.[^11]

## New CE estimate

Using the original BOTEC framework with updated costs, the BOTEC estimates CE at **~9x** at a best-guess total incremental cost of $3/pregnancy (range: ~5x at $6/pregnancy to ~13x at $2/pregnancy). The improvement over the original (~7x at $4/pregnancy) is driven primarily by reduced commodity costs.

The key parameters are:
- **LBW reduction**: 12% (RR 0.88, unchanged from 2019 Cochrane; I²=0%, high quality)
- **LBW baseline**: 28% in South Asia
- **Moral weight for LBW**: 3 UoV (unchanged; rough estimate supported by new stunting evidence)
- **EV adjustment**: 0.75 (slightly increased from original 0.7, given Kirk Humanitarian's successful scale-up in 111 LMICs demonstrating real-world feasibility)
- **Total incremental cost**: $3/pregnancy (reduced from $4, reflecting lower commodity costs)

The CE is sensitive to the incremental cost of switching from IFA to MMS. At Kirk Humanitarian's procurement price ($2.13/pregnancy for commodity alone), the incremental cost over IFA is minimal (~$0.33/pregnancy), but programmatic/transition costs (training, logistics, adherence support) are the dominant component.

See `outputs/botecs/mms_during_pregnancy.xlsx` for the BOTEC.

## Remaining uncertainties

- **Incremental programmatic costs of IFA→MMS transition.** This remains the pivotal unknown. The original estimated $3/person for "programmatic costs of transition/TA per person, tablet waste, etc." and called it a guess. Kirk Humanitarian's massive scale-up ($92M to UNICEF) should yield real data on per-pregnancy delivery costs, but I haven't found disaggregated cost-per-pregnancy figures from their programs. UNICEF's Improving Maternal Nutrition Acceleration Plan should have this data.

- **Moral weight for averting an LBW birth.** The original used 3 UoV ("super rough guess, from syphilis CEA"). The 2025 meta-analysis showing MMS reduces stunting through 24 months supports a developmental benefit, but 3 UoV is still uncertain. GiveWell's early-life growth work (which the original recommended leaning on) could help anchor this. If MW is 2 instead of 3, CE drops to ~6x; if 4, CE rises to ~12x.

- **Iron content concern.** MMS contains 30mg iron vs. 60mg in standard IFA. The original QEA flagged this as a concern for areas with high anemia prevalence. The 2025 IPD meta-analysis found that low adherence was associated with increased maternal anemia risk (RR 1.26), suggesting this concern has some basis. I haven't seen a definitive resolution — the 2024 UNIMMAP product specification revision may address this.[^12]

- **Counterfactual IFA coverage.** The BOTEC models switching from IFA to MMS, but mean IFA coverage in LMICs is only ~31% for ≥90 days.[^13] For the ~69% of women not receiving IFA, MMS would be a new intervention, not a switch — potentially with higher absolute benefits but also higher costs (no existing delivery platform to piggyback on).

## Who is implementing / funding this?

- **Kirk Humanitarian** is the largest funder, having committed $125M and reached 75M women in 111 LMICs through product donations to UNICEF and the Child Nutrition Fund. Their procurement has driven costs to $0.0118/dose.
- **UNICEF** is the primary implementing partner, running the Improving Maternal Nutrition Acceleration Plan with Kirk Humanitarian funding.
- **Healthy Mothers Healthy Babies Consortium** (convened by the Micronutrient Forum and the New York Academy of Sciences) coordinates advocacy and evidence generation for MMS adoption.
- **Nutrition International** provides technical assistance for MMS introduction into national ANC programs (e.g., Pakistan's LHW program).
- **CIFF** has committed to the MMS Joint Challenge alongside multiple partners.
- **Multiple LMICs** are adopting MMS into national programs, though I haven't found a count of how many countries have formally transitioned from IFA to MMS.

## Recommended next steps

- **Request disaggregated cost-per-pregnancy data from UNICEF's Improving Maternal Nutrition Acceleration Plan.** Kirk Humanitarian's $92M commitment to UNICEF covers 43 million women — implying ~$2.14/pregnancy, but this is a commodity-only figure. The all-in programmatic cost (including training, logistics, integration into ANC, adherence monitoring) is the key missing parameter. **Suggested contact:** UNICEF's Nutrition Section, specifically the MMS program team working with Kirk Humanitarian, or Cristina Ajello at Kirk Humanitarian who has published on MMS product specifications and supply strategy.

- **Investigate whether GiveWell's early-life growth work can anchor the moral weight for LBW.** The original QEA recommended "leaning on our early-life growth work and explicitly modeling out effect on later-life income." The new 2025 meta-analysis showing MMS reduces stunting (RR 0.86) through 24 months provides direct evidence for a developmental pathway. If GW has developed a framework for valuing LBW or stunting reduction since 2021, applying it here could substantially narrow the CE range.

- **Assess GiveWell's existing position on MMS.** GiveWell was investigating family planning as of 2025 and has published valuations for contraception. It's unclear whether they've also assessed MMS — if so, our analysis should align with or build on their work. If not, MMS may represent a gap in their pipeline given the $37/$1 Copenhagen Consensus estimate and massive Kirk Humanitarian scale-up.

---

[^1]: "Deficiencies of micronutrients such as vitamin A, iron, iodine and folate are particularly common among during pregnancy, due to increased nutrient requirements of the mother and developing fetus. These deficiencies can negatively impact the health of the mother, her pregnancy, as well as the health of the newborn baby." (https://www.who.int/publications-detail-redirect/9789240007789) [Note] The 28% LBW rate in South Asia is from the original BOTEC, sourced to WHO GHO data on birth outcomes.

[^2]: "Supplementation with iron and folic acid during pregnancy has been found to be associated with reduction in the risk of maternal anaemia and infants with LBW [...] This UNIMMAP tablet provides one recommended daily allowance of vitamin A, vitamin B1, vitamin B2, niacin, vitamin B6, vitamin B12, folic acid, vitamin C, vitamin D, vitamin E, copper, selenium and iodine with 30 mg of iron and 15 mg of zinc for pregnant women." (https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD004905.pub6/full)

[^3]: "In 2020, the recommendation for multiple micronutrient supplements (MMS) in pregnancy was updated from 'not recommended' to 'recommended in the context of rigorous research'." (https://www.who.int/publications-detail-redirect/9789240007789)

[^4]: "In 2021, UNIMMAP MMS was included in the World Health Organization's Model List of Essential Medicines." (https://hmhb.micronutrientforum.org/mms/)

[^5]: [Note] Multiple sources report Kirk Humanitarian has reached 75 million pregnant women in 111 LMICs. Exact sourcing: "75 million pregnant women in 111 low- and middle-income countries have received UNIMMAP MMS purchased and donated by Kirk Humanitarian." (https://kirkhumanitarian.org/unimmap-mms-product-attributes/)

[^6]: "Kirk Humanitarian has committed a total of $92 million to UNICEF and the Child Nutrition Fund, which will provide UNIMMAP MMS product to 43 million women in low- and middle-income countries." (https://www.childnutritionfund.org/press-releases/kirk-humanitarian-commits-additional-us50-million-expand-unicefs-global-maternal)

[^7]: "UNIMMAP MMS is produced at $0.0118 per dose or $2.13 per woman per pregnancy when packaged in a 180-count bottle." (https://kirkhumanitarian.org/unimmap-mms-product-attributes/)

[^8]: "MMS reduced risk of stunting (RR: 0.86; 95% CI: 0.82, 0.91), underweight (RR: 0.86; 95% CI: 0.81, 0.90), small head circumference (RR: 0.84; 95% CI: 0.79, 0.90), and low MUAC (RR: 0.90; 95% CI: 0.82, 0.99) at 3 months and wasting (RR: 0.90; 95% CI: 0.85, 0.96) at birth." (https://www.sciencedirect.com/science/article/pii/S0002916525002382)

[^9]: "≥90% adherence was associated with increased birthweight (MD: 44 g; 95% CI: 31, 56 g) and lower risk of LBW (RR: 0.93; 95% CI: 0.88, 0.98) and small-for-gestational age (RR: 0.95; 95% CI: 0.93, 0.98). [...] <75% adherence was associated with greater risk of stillbirth (RR: 1.43; 95% CI: 1.12, 1.83) and maternal anemia (RR: 1.26; 95% CI: 1.11, 1.43)." (https://www.sciencedirect.com/science/article/pii/S2161831325000912)

[^10]: "The cost of replacing IFA supplements with MMS is just US$84 million per year, yet the benefits are worth US$3.16 billion, resulting in more than US$37 economic return for every one dollar spent." (https://hmhbconsortium.org/brief-mms-copenhagen-consensus/)

[^11]: [Note] UNIMMAP Multiple Micronutrient Supplements were named one of TIME's Best Inventions of 2025. (https://time.com/collections/best-inventions-2025/7318506/unimmap-multiple-micronutrient-supplements/)

[^12]: [Note] The 2024 UNIMMAP MMS product specification revision (Ajello et al., Annals of the NYAS 2024) may address the iron content concern, but I haven't reviewed the full text. (https://pubmed.ncbi.nlm.nih.gov/39167636/)

[^13]: "Coverage data from 59 low‐ and middle‐income countries indicate that the mean proportion of women who consume iron folic acid (IFA) supplements for at least 90 days during pregnancy is only 31%." (https://www.who.int/publications-detail-redirect/9789240007789)
