# Review: QEA of Vaginal Rings w/Dapivirine (DPV) for HIV Prevention among Women

- Link to original QEA: [QEA for Vaginal Rings w/Dapivirine for HIV Prevention](https://docs.google.com/document/d/1EZU8ogduJC3kEh9NQvDloBNZBY0sXYz3SacfAZ1GKxI/edit?tab=t.0)
- Link to original BOTEC: [Dapivirine Rings for HIV preliminary CEA](https://docs.google.com/spreadsheets/d/1yJYR7g7V_O0hS8-rbBe7tHeDZCM-uUASi2PjFNFARiw/edit?gid=0#gid=0)
- Year the original analysis was conducted: 2018

## What is this (basic context)

- **What is the problem?** HIV infections among women, particularly in sub-Saharan Africa, remain high. Existing prevention methods (condoms, oral PrEP) can be difficult to adhere to or may not be within women's control.
- **What is the program?** Dapivirine rings are monthly vaginal rings containing the antiretroviral drug dapivirine, worn continuously and replaced each month. The ring delivers a sustained prophylactic dose of antiretrovirals to reduce the risk of HIV infection during vaginal sex.
- **Why did we deprioritize this?** A combination of low cost-effectiveness (1/4th as CE as VMMC, though I'm not sure what the CE estimate for VMMC was) and lack of concrete funding opportunities.

## Key updates

- **Cost updates:** Thanks to a subsidy announced by the Population Council, prices per ring dropped to $5.90/ring[^1] (compared to $7/ring that the current QEA assumes).[^2], which would net out to ~$71/year if used continuously.
- **Modeling updates:** The original BOTEC doesn't account for "infections averted that are merely delayed". It also doesn't model the different benefit streams for preventing an infection (mortality, morbidity, income effects, treatment costs averted..)
- **New trial results:** Two open-label extension studies of the initial RCTs (ASPIRE and RING) have been published, both of which suggest a larger effect (roughly 50% if averaging across both studies, compared to the 30% reduction we assumed in the old QEA) than the RCTs had detected:
  - DREAM study (2021) finds that "18 (1.9%) HIV-1 infections were confirmed during DVR use, resulting in an incidence of 1.8 (95% CI 1.1-2.6) per 100 person-years, 62% lower than the simulated placebo rate."[^3]
  - HOPE study (2022) finds that "HIV-1 incidence was 2.7 per 100 person-years (95% CI 1.9-3.8, n=35 infections), compared to an expected incidence of 4.4 per 100 person-years (95% CI 3.2-5.8) among a population matched on age, site, and presence of a sexually transmitted infection from the placebo group of ASPIRE." This suggests an effect size of ~39% (=1-2.7/4.4).
  - In 2021, the WHO officially recommended the dapivirine vaginal ring.[^4]
  - AVAC[^5] also indicates that 13 implementation studies for the ring are completed/ongoing/planned, though they don't link to them and I haven't tried to find them.[^6]
- **Changes in the PrEP landscape:** Since 2025, WHO has been recommending two long-acting injectables (CAB-LA and LEN)[^7] that may reduce the demand for the Dapivirine ring.

## New CE estimate

A very rough BOTEC, borrowing many assumptions from our oral PrEP/LEN CEA, estimates that this program might be around 5x our benchmark in high-risk populations, still below our 8x bar. Our previous BOTEC doesn't use moral weights, so it's hard to say how much our CE estimate changed, but twice as high as before is probably in the right ballpark.[^8]

See [vaginal_rings_dapivirine_botec.md](./vaginal_rings_dapivirine_botec.md) for the original BOTEC parameters.

## Remaining uncertainties

- Population Council working on a three-month ring that could bring costs down even further, especially since it requires fewer touchpoints with the healthcare system. A phase I open-label randomized crossover relative bioavailability trial (IPM 054), completed in 2024, suggests that the ring might be as effective as the one-month version.[^9]
- The effect of the ring depends heavily on adherence[^10], and we don't have a good understanding of how consistently women would use the ring (they need to change it every month[^11], but my guess is that they get refills every 3 months). We also don't know for how long they'd typically use the ring (persistence)
- It's very unclear what all-in costs for an actual program would look like, and it's possible that they are a lot higher than what we estimate here.
- Counterfactual incidence in the target population is hard to estimate, and they directly drive how many infections could be prevented by the ring.
- There may be offsetting effects: Women may believe that the ring also provides protection against other STIs, or reduce their likelihood of getting pregnant, and these are not modeled in the BOTEC. This is an assumption that I have not reviewed.

## Who is implementing / funding this?

- Population Council (the org who holds the rights to the ring[^12]) seems to be funding subsidies for the ring itself (see above). I'm not sure if they also implement programs.
- CIFF & Global Fund committed $2m over the 2024-25 period to purchase ~150,000 rings[^13]
- I'm not sure if anyone is implementing this at scale - PrEP Watch notes that the ring is "Not yet widely available outside of implementation studies."

## Recommended next steps

- **Review the new open-extension studies (DREAM and HOPE study)** - the current BOTEC just uses their headline results, but this may not be the best guess for the effectiveness of the ring
  - Consider reaching out to the lead authors of these studies, Jared Baeten (U of Washington) and Annalene Nel (Medinel)
- **Identify the completed (and published) implementation studies that AVAC keeps tabs on**, which could help inform real-world adherence and programmatic costs
- **Follow up with Population Council on the status of the 3-month ring.** If there are promising findings from more advanced clinical trials, this could mean that the ring might soon be close to our bar (assuming costs come down thanks to this ring)

---

[^1]: "The Population Council, an international non-profit research organization, announced today that it is subsidizing the price of its one-month Dapivirine Vaginal Ring for HIV prevention to $5.90 / ring -- a 54% price reduction from its current selling price." https://popcouncil.org/media/dapivirine-vaginal-ring-price-drops-by-over-50-bringing-more-affordable-hiv-prevention-options-to-women-and-adolescent-girls-in-africa-and-beyond/

[^2]: Our previous BOTEC already assumes that annual costs are only $84, or $7/ring, which is in contrast to Population Council's claim that they're reducing prices by 54%. It's possible that the price of the ring has increased since we conducted the last QEA, or that the source we used was not reliable.

[^3]: DREAM study, 2021. Full quote above in body text.

[^4]: "WHO today recommended that the dapivirine vaginal ring (DPV-VR) may be offered as an additional prevention choice for women at substantial risk of HIV infection as part of combination prevention approaches." https://www.who.int/news/item/26-01-2021-who-recommends-the-dapivirine-vaginal-ring-as-a-new-choice-for-hiv-prevention-for-women-at-substantial-risk-of-hiv-infection

[^5]: "AVAC is an international non-profit organization that leverages its independent voice and global partnerships to accelerate ethical development and equitable delivery of effective HIV prevention options, as part of a comprehensive and integrated pathway to global health equity." https://avac.org/about-us/

[^6]: See infographic here: https://avac.org/resource/dapivirine-vaginal-ring-implementation/

[^7]: "The World Health Organization (WHO) released today new guidelines recommending the use of injectable lenacapavir (LEN) twice a year as an additional pre-exposure prophylaxis (PrEP) option for HIV prevention...LEN joins other WHO-recommended PrEP options, including daily oral PrEP, injectable cabotegravir and the dapivirine vaginal ring, as part of a growing arsenal of tools to end the HIV epidemic." https://www.who.int/news/item/14-07-2025-who-recommends-injectable-lenacapavir-for-hiv-prevention

[^8]: Looking only at costs per infection prevented, we're guessing ~$4.7k now vs ~$9.5k then, which would suggest that our new CE estimate is about twice as high compared to our original estimate.

[^9]: "The trial found that a 3-month dapivirine vaginal ring delivers the active antiretroviral drug, dapivirine, at higher levels than the 1-month dapivirine vaginal ring. The trial, conducted among 124 women in South Africa, suggests that the longer-acting ring will be as effective as the 1-month ring, offering a more cost effective and convenient option to women who continue to seek options to prevent HIV infection during sex." 3-Month Dapivirine Vaginal Ring for HIV Prevention Demonstrates Superior Drug Release Compared to 1-Month Ring

[^10]: "The incidence of HIV-1 infection in the dapivirine group was lower by 27% (95% confidence interval [CI], 1 to 46; P=0.046) than that in the placebo group. In an analysis that excluded data from two sites that had reduced rates of retention and adherence, the incidence of HIV-1 infection in the dapivirine group was lower by 37% (95% CI, 12 to 56; P=0.007) than that in the placebo group. In a post hoc analysis, higher rates of HIV-1 protection were observed among women over the age of 21 years (56%; 95% CI, 31 to 71; P<0.001) but not among those 21 years of age or younger (-27%; 95% CI, -133 to 31; P=0.45), a difference that was correlated with reduced adherence." https://www.nejm.org/doi/full/10.1056/NEJMoa1506110

[^11]: "The ring must be in place for 24 hours before it can reduce the risk of HIV infection. Only reduces the risk of HIV while it is in place - it should not be removed during sex, and is rarely felt by either partner. Must be replaced after one month." https://www.prepwatch.org/products/dapivirine-vaginal-ring/

[^12]: "The International Partnership for Microbicides (IPM) developed the Dapivirine Vaginal Ring (DapiRing or DVR), a long-acting, user-controlled vaginal ring to reduce the risk of HIV transmission during vaginal sex. The Population Council acquired the DapiRing and other assets from IPM in 2022, including a key subset of the DapiRing development team." https://popcouncil.org/project/the-dapivirine-vaginal-ring-for-hiv-prevention/

[^13]: "The Children's Investment Fund Foundation (CIFF), in partnership with the Global Fund to Fight AIDS, Tuberculosis and Malaria (the Global Fund), announced on 21 July at the 25th International AIDS Conference an initiative of up to US$2 million over the 2024-2025 period for the purchase of approximately 150,000 dapivirine vaginal rings in countries that implement Global Fund grants to fight HIV and AIDS." https://www.theglobalfund.org/en/news/2024/2024-07-21-ciff-propel-prep-revolution-usd2-million-immediate-access-prep-rings/
