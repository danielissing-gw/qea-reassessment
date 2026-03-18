# Review: QEA of Antenatal Corticosteroids (ACS) for Preterm Birth

- Link to original QEA: [Antenatal Corticosteroids QEA](https://docs.google.com/document/d/1bPXDLhRKFxWvHiS0tLjhxzUGUJ75pg4EtUk89Md9dvk/edit)
- Link to original BOTEC: [ACS BOTEC](https://docs.google.com/spreadsheets/d/11mTRJz38hbuohmhFaTSCtTWAdDRxngwP3zavAZP2wrY/edit)
- Year the original analysis was conducted: 2020

## What is this (basic context)

- **What is the problem?** Preterm birth (before 37 weeks' gestation) is the leading cause of neonatal mortality globally. Sub-Saharan Africa has a neonatal mortality rate of 27 per 1,000 live births, the highest in the world and responsible for 43% of all infant deaths.[^1] Among preterm neonates, respiratory distress syndrome (RDS) caused by immature lung development is a primary cause of death.
- **What is the program?** Antenatal corticosteroids (ACS) — typically dexamethasone, given as four 6mg intramuscular injections at 12-hour intervals — are administered to women at risk of imminent preterm birth before 34 weeks' gestation. ACS accelerate fetal lung maturation and reduce neonatal mortality and respiratory morbidity. The drug costs approximately $0.51 per course.[^2]
- **Why did we deprioritize this?** The original QEA (2020) recommended "Postpone" because the only LMIC trial at the time — the ACT trial (Althabe et al. 2015) — found that a strategy to promote ACS use in low-resource settings led to a significant *increase* in neonatal mortality, attributed to widespread overtreatment of women who did not actually deliver preterm.[^3] Two follow-up trials were ongoing, and the QEA recommended revisiting once they reported.

## Key updates

- **WHO ACTION-I trial (NEJM 2020): ACS reduces neonatal death by 16% when properly targeted in LMIC hospitals.** The ACTION-I trial (n=2,852 women in 29 secondary/tertiary hospitals across Bangladesh, India, Kenya, Nigeria, and Pakistan) found that dexamethasone reduced neonatal death compared with placebo among women at risk of early preterm birth (26–34 weeks).[^4] The trial was stopped early for benefit at the second interim analysis. Critically, 90% of enrolled women actually delivered preterm, confirming the targeting was effective — in contrast to the ACT trial where only 16% of treated women delivered a preterm infant. No increase in maternal bacterial infection was observed.[^5]

- **WHO updated ACS guidelines (2022): Now recommended for LMICs under specific conditions.** WHO updated its antenatal corticosteroid recommendations in 2022 based on the ACTION-I evidence, superseding the 2015 guidelines.[^6] The updated recommendation maintains the requirement for: (1) accurate gestational age assessment, (2) imminent preterm birth, (3) no clinical maternal infection, (4) adequate childbirth care available, and (5) adequate newborn care capacity including resuscitation, thermal care, feeding support, infection treatment, and safe oxygen use.

- **Cost-effectiveness analysis: ACS is cost-saving in all 5 trial countries.** A CEA using ACTION-I data found that ACS administration averted 38 neonatal deaths and 1,132 DALYs per 1,000 woman–baby units. The intervention was cost-saving in all five countries, ranging from savings of $1,778 per 1,000 units in Nigeria to $53,681 in Kenya, because reduced neonatal ICU costs outweighed drug costs.[^7]

- **Massive implementation gap persists.** A 2025 multi-country study found that only a median of 10.7% (range 6.7–35.2%) of health facilities had provided ACS across eight LMIC countries with comparable sampling strategies.[^8] This represents a very large gap between evidence and practice.

## New CE estimate

My best guess is **~14x cash at $30/woman treated, with a range of ~6x at $100/woman to ~39x at $10/woman.** The CE is highly sensitive to program implementation costs, which are the pivotal unknown. See [antenatal_corticosteroids_preterm_birth BOTEC](../botecs/antenatal_corticosteroids_preterm_birth.xlsx).

The drug itself is extremely cheap ($0.51/course), so the cost question is really about what it takes to implement a program that ensures proper targeting and adequate neonatal care capacity. The ACTION-I trial protocol required ultrasound dating, trained obstetric physicians, and hospitals with a minimum package of newborn care — these conditions define both the eligible hospital population and the per-woman cost. At $30/woman (my best guess for a program that trains staff and ensures drug supply in hospitals that already have adequate neonatal care), the CE is ~14x after IV/EV adjustments. Even at $100/woman (which would include more substantial capacity building), the CE is ~6x — below the 8x bar but close enough to warrant investigation.

The original BOTEC estimated 28x, but used the HIC effect size (31% reduction from the Cochrane review) with no IV/EV adjustment and a cost of only $5/woman. The ACTION-I LMIC effect is about half (16% reduction), but this is now anchored to a rigorous LMIC trial rather than extrapolated from HIC data.

## Remaining uncertainties

- **Program implementation costs are the pivotal unknown.** The drug is $0.51, but the cost of a program to identify women at risk of early preterm birth (requiring ultrasound), train staff in proper ACS administration, ensure drug supply, and maintain adequate neonatal care is uncertain. I haven't found any published estimates of the total per-woman cost of an ACS scale-up program in LMICs. The ACTION-I trial's implementation lessons paper describes the components needed but not their costs.
- **ACTION-III trial results (expected ~2026-2027).** The ACTION-III trial is testing ACS for late preterm birth (34–36 weeks) in 24 hospitals across the same 5 countries. If ACS is also effective for late preterm births, the eligible population roughly triples and the CE improves substantially. Enrollment started July 2022 and is expected to complete by December 2026.
- **Fraction of LMIC hospitals that already meet the WHO prerequisites.** ACS only works in hospitals with adequate neonatal care. I haven't been able to determine what fraction of LMIC facility births occur in hospitals that would meet the WHO criteria but currently don't provide ACS. This determines the addressable market for a scale-up program.
- **Early stopping bias.** The ACTION-I trial was stopped early for benefit at the second interim analysis. Trials stopped early for benefit tend to overestimate treatment effects. A more conservative estimate of the effect size might be warranted.

## Who is implementing / funding this?

- **WHO** is the primary driver through the ACTION trial series (ACTION-I, ACTION-III) and the 2022 guideline update. WHO is also conducting implementation research in Burkina Faso, India, Rwanda, and Zambia.
- **No at-scale philanthropic program identified.** I'm not aware of any organization running an ACS scale-up program at scale in LMICs that a philanthropist could fund. Save the Children has historically advocated for ACS scale-up and estimated it could save 340,000 lives per year, but I haven't found evidence of an active STC implementation program.
- **Government programs** exist in some LMIC countries but coverage is very low (~10% of facilities). India and Pakistan have national ACS guidelines but implementation remains poor.

## Recommended next steps

- **Obtain implementation cost estimates for ACS scale-up in LMIC hospitals.** This is the single most important unknown. I'd recommend reaching out to **Dr. Fernando Althabe's team at WHO's Department of Sexual and Reproductive Health** (who designed and managed both the ACT and ACTION-I trials and are currently running ACTION-III), or **Dr. Marion Koopmans at the WHO Implementation Research platform** — they are conducting ACS implementation research in 4 countries and would have the best sense of what scale-up costs in practice.
- **Determine the addressable facility population.** Understanding what fraction of LMIC births occur in hospitals that meet the WHO prerequisites (adequate neonatal care) but don't currently provide ACS would clarify the potential impact. The **2025 JOGH multi-country study** authors (Brizuela et al.) conducted the most recent facility-level assessment and could provide granular data on which facility types are ready vs. need capacity building.
- **Monitor ACTION-III results.** If ACS is effective for late preterm births (34–36 weeks), the eligible population would roughly triple. This would substantially change the CE arithmetic and could make ACS one of the highest-CE neonatal interventions available. Results are expected by late 2027.

---

[^1]: "Sub-Saharan Africa has a neonatal mortality rate of 27/1000 live births, the highest rate in the world and is responsible for 43% of all infant fatalities." ([Asaye et al., PLOS ONE 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306297))

[^2]: [Note] Save the Children's 2013 State of the World's Mothers report stated ACS costs "as little as 51 cents per treatment." The drug (dexamethasone) is on the WHO Essential Medicines List and is widely available. The $0.51 figure likely covers only the drug cost, not delivery.

[^3]: "Furthermore, despite nearly half of the less-than-5th-percentile infants receiving antenatal corticosteroids, neonatal mortality did not decrease in this subgroup. Among the entire population, the intervention resulted in a significant increase in neonatal deaths of 3.5 per 1000 livebirths and an increase in perinatal deaths of 5.1 per 1000 births." ([Althabe et al., Lancet 2015](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(14)61651-2/fulltext))

[^4]: "Neonatal death occurred in 278 of 1417 infants (19.6%) in the dexamethasone group, as compared with 331 of 1406 infants (23.5%) in the placebo group (relative risk, 0.84; 95% CI, 0.72 to 0.97; P=0.03)." ([WHO ACTION-I Investigators, NEJM 2020](https://www.nejm.org/doi/full/10.1056/NEJMoa2022398))

[^5]: "Possible maternal bacterial infection occurred in 68 of 1416 women (4.8%) in the dexamethasone group and 89 of 1412 women (6.3%) in the placebo group (relative risk, 0.76; 95% CI, 0.56 to 1.03; P=0.002 for noninferiority)." ([WHO ACTION-I Investigators, NEJM 2020](https://www.nejm.org/doi/full/10.1056/NEJMoa2022398))

[^6]: [Note] WHO updated its ACS recommendations in September 2022, superseding the 2015 guidelines. The updated recommendation is based on 27 efficacy trials plus the ACTION-I trial, and maintains the requirement for gestational age assessment, imminent preterm birth, no maternal infection, and adequate childbirth and newborn care. Source: WHO recommendations on antenatal corticosteroids for improving preterm birth outcomes (2022).

[^7]: "Administration of dexamethasone averted 38 neonatal deaths per 1000 woman–baby units and 1132 DALYs per 1000 woman–baby units [...] dexamethasone was more effective and cost less compared with no treatment, making antenatal dexamethasone for early preterm birth cost-saving when used in hospitals in low-resource countries." ([Salehi et al., Lancet Global Health 2022](https://www.sciencedirect.com/science/article/pii/S2214109X22003400))

[^8]: "Only a median of 10.7% (range = 6.7–35.2%) of facilities had provided ACS across eight countries with comparable sampling strategies." ([Brizuela et al., JOGH 2025](https://jogh.org/2025/jogh-15-04149/))
