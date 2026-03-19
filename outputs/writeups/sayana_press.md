# Review: QEA of Sayana Press Injectable Contraceptive

- Link to original QEA: [Sayana Press injectable contraceptive](https://docs.google.com/document/d/1LHkvhYKY3zfs8qBAxtbscRVarTHLxy850Wsd7Yorbeo/edit)
- Link to original BOTEC: [Sayana Press CEA](https://docs.google.com/spreadsheets/d/1J-7saV7CfdhNt2VV0G9eQ8wB43oAe90_9oSinzCMgwo/edit)
- Year the original analysis was conducted: 2016

## What is this (basic context)

- **What is the problem?** An estimated 218 million women in developing countries have an unmet need for modern contraception, leading to approximately 111 million unintended pregnancies per year.[^1] Unintended pregnancies contribute to unsafe abortions (~25 million/year globally), maternal morbidity, and maternal mortality.
- **What is the program?** Sayana Press (DMPA-SC) is a subcutaneous injectable contraceptive in a prefilled single-use device ($1/dose under the Pfizer/Gates/CIFF agreement), administered every 3 months. It can be given by community health workers or self-injected — making it uniquely suited for community-based and self-care delivery in low-resource settings.[^2]
- **Why did we deprioritize this?** The original 2016 QEA found mortality outcomes "unlikely to affect the bottom line" (~$88,700/death averted) and the CE depended heavily on how GiveWell valued avoided unwanted pregnancies — a moral weight question that was unresolved at the time. Self-injection was flagged as promising but not yet approved.

## Key updates

- **GiveWell published a contraception valuation framework (April 2025).** GW now estimates that one year of modern contraception in LMICs generates approximately 0.7 units of value (25th-75th percentile range: 0.3-1.1), encompassing health benefits for women and children (~0.2 UoV), earnings increases (~0.1 UoV), resources for existing children (~0.2 UoV), and subjective well-being (~0.2 UoV).[^3] This directly resolves the moral weight blocker that stalled the 2016 QEA.

- **Self-injection is now approved and scaling.** Self-injection of DMPA-SC is approved in 35+ countries and available in 55+ countries total.[^4] A meta-analysis of three RCTs found self-injection increases 12-month continuation by 27% compared with provider-administered injection (RR 1.27, 95% CI 1.16-1.39).[^5] In Uganda, 12-month continuation was 81% for self-injectors vs 65% for provider-administered (n=1,161).[^6] Self-injection also reduces delivery costs by eliminating the need for a health worker at each injection.

- **GiveWell is actively investigating family planning.** GW funded a $500k grant to Family Empowerment Media for an RCT of radio-based family planning promotion in Nigeria (March 2023). GW published a podcast episode on "Advancing GiveWell's Work on Family Planning" (August 2025). The contraception valuation framework was developed as part of this broader effort.[^7]

## New CE estimate

Using GW's published contraception valuation (0.7 UoV per woman-year) and a range of delivery costs, the BOTEC estimates CE at **~13x** at a best-guess total cost of $12/woman-year (range: ~7x at $20/year to ~35x at $6/year). Even at relatively high program costs ($20/year including demand generation and training), CE is near or above the 8x bar.

The cost per woman-year is the pivotal parameter. Commodity costs are established ($4/year at $1/dose × 4 doses). Delivery costs for self-injection programs are likely $2-8/year depending on context; provider-administered programs cost more ($5-16/year). I'm assuming $8/year for delivery in a moderately lean self-injection program but I haven't verified this against actual program budgets.[^8]

See `outputs/botecs/sayana_press.xlsx` for the BOTEC.

## Remaining uncertainties

- **Actual program delivery costs**: The $12/year total is an estimate. Costs in the original Guttmacher analysis ($9.14/year) are from 2012 and may not reflect current self-injection program costs. PSI or PATH may have better data from their self-injection pilots in Uganda, Senegal, and Burkina Faso.
- **Additionality**: What fraction of women reached by a Sayana Press program would have otherwise accessed modern contraception anyway? GW's 0.7 UoV/year valuation assumes the contraception year is additional. The original BOTEC assumed 25% unmet need but this varies significantly by country (14% in Kenya to 36% in DRC).
- **GW's contraception valuation range is wide** (0.3-1.1 UoV/year). At the lower bound (0.3 UoV), CE drops to ~5.6x at $12/year — below the 8x bar.
- **Four-month dosing**: A Phase 3 trial showed Sayana Press is effective when injected every 4 months instead of 3, which would reduce commodity costs by 25%.[^9] I haven't seen this adopted in practice yet.

## Who is implementing / funding this?

- **PSI** is the largest implementer, delivering 9M+ doses per year across multiple African countries through CHW distribution and social marketing in pharmacies.
- **PATH** developed the Uniject delivery system and has led self-injection pilots in Uganda, Senegal, Burkina Faso, and other countries.
- **Pfizer** manufactures Sayana Press and offers the $1/dose price through the Gates/CIFF agreement.
- **FP2030** (formerly FP2020) coordinates global family planning commitments. Multiple countries (Uganda, Senegal, DRC, Ghana, Malawi, Nigeria) are scaling self-injection.
- **GiveWell** is actively investigating family planning and has published a contraception valuation framework. Status of their Sayana Press-specific investigation is unclear.

## Recommended next steps

- **Request program cost data from PSI or PATH's self-injection pilots.** The pivotal unknown is the all-in cost per woman-year of self-injected DMPA-SC in a real program setting. PSI has been delivering 9M+ doses per year and PATH has run self-injection pilots in 5+ countries — they should have this data. Specifically, ask for cost per woman-year disaggregated into commodity, training, supply chain, and demand generation. This would resolve the largest uncertainty in the BOTEC. **Suggested contact:** PSI's DMPA-SC program lead or Katy Schenck at PATH's reproductive health team, who has led the DMPA-SC self-injection evidence program.

- **Clarify GW's Sayana Press investigation status.** GW's interim report on Sayana Press (from ~2017) noted the program was "promising" but had gaps. GW has since published a contraception valuation and is actively investigating family planning. It's worth confirming whether GW has already updated their Sayana Press assessment or whether this represents a gap in their current pipeline. If they haven't revisited, the combination of their new valuation framework + self-injection evidence may warrant a fresh look.

- **Assess additionality in specific country contexts.** The CE is sensitive to what fraction of women reached are genuinely new contraception users. DHS data from target countries (Uganda, Senegal, Nigeria, DRC) can estimate the proportion of women with unmet need in areas where Sayana Press programs operate. Comparing contraceptive prevalence rates in program vs. non-program areas would help, though this requires careful analysis to avoid selection effects.

---

[^1]: "In 2019, an estimated 218 million women of reproductive age in developing countries had an unmet need for modern methods of family planning, and 111 million unintended pregnancies occurred in low- and middle-income countries." (https://www.guttmacher.org/fact-sheet/adding-it-up-investing-in-sexual-reproductive-health)

[^2]: "Sayana® Press is a three-month, progestin-only, all-in-one injectable contraceptive that combines the drug and needle in the Uniject™ injection system. Sayana Press is small, light, easy to use, and requires minimal training, making it especially suitable for community-based distribution — and for women to administer themselves through self-injection." (https://www.path.org/our-impact/articles/dmpa-sc/)

[^3]: "GiveWell estimates that providing one year of modern contraception in low- and middle-income countries generates approximately 0.7 units of value (with a 25th-75th percentile range of 0.3-1.1 units)." (https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/valuing-contraception)

[^4]: "The product is now available in nearly 55 countries worldwide, with nearly 35 countries offering self-injection." (https://launchandscalefaster.org/intervention/sayanar-press)

[^5]: [Note] Meta-analysis of three RCTs comparing self-injection with provider administration found RR 1.27 (95% CI 1.16-1.39) for 12-month continuation, and three cohort studies found RR 1.18 (95% CI 1.10-1.26). Summarized from multiple sources.

[^6]: "The 12-month continuation rate for 561 women self-injecting DMPA-SC was 0.81 (95% CI 0.78-0.84), and for 600 women receiving DMPA-IM from a health worker, it was 0.65 (95% CI 0.61-0.69)." (https://pubmed.ncbi.nlm.nih.gov/29654751/)

[^7]: [Note] GW's family planning investigation includes the FEM grant ($500k, March 2023), contraception valuation publication (April 2025), and a podcast episode (August 2025). These suggest an active pipeline, though the status of Sayana Press specifically is unclear from public materials.

[^8]: [Note] This is an assumption I have not verified against actual program data. The original Guttmacher estimate ($9.14/year including commodity and delivery) is from 2012. Self-injection should reduce the delivery cost component, but how much depends on program design. My estimate of $8/year for delivery assumes a moderately lean self-injection program with CHW training, supply chain, and minimal demand generation.

[^9]: "A multicenter, international Phase 3 study evaluated pharmacokinetics, efficacy, and safety of Sayana Press when administered subcutaneously at 4-month intervals... Contraceptive efficacy over the 12-month treatment period was 99.0% (95% CI: 97.5, 99.5)." (https://pmc.ncbi.nlm.nih.gov/articles/PMC8804165/)
