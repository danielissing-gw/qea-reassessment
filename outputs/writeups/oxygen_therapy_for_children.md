# Review: QEA of Oxygen Therapy for Children

- Link to original QEA: [Oxygen QEA](https://docs.google.com/document/d/1daY7xgIBgTYEzQSSC5AzOdxnqqiPKAcvHyow-TvJvzU/)
- Link to original BOTEC: [Oxygen BOTEC](https://docs.google.com/spreadsheets/d/1163LXJ5FhMT3DWjhJb4IKdHnuEOWNnTlIrkYaLv8jJE/)
- Year the original analysis was conducted: 2021

## What is this (basic context)

- **What is the problem?** Hypoxemia (low blood oxygen) is a life-threatening complication of pneumonia, sepsis, malaria, and other conditions. An estimated 374 million people need medical oxygen annually, with 306 million in LMICs — yet only 30% receive it, a coverage gap worse than HIV (23%) or TB (25%).[^1] Children with pneumonia are particularly vulnerable: ~13% of hospitalized pneumonia cases are hypoxemic, and hypoxemia increases the odds of death roughly 5-fold.[^2]
- **What is the program?** Installing improved oxygen systems at health facilities — pulse oximeters for diagnosis, oxygen concentrators (or cylinders) for supply, and training for clinical staff. This allows health workers to identify hypoxemic patients who would otherwise go undiagnosed and provide oxygen therapy.
- **Why did we deprioritize this?** The original assessment found CE of ~7x (non-COVID scenario), driven by uncertain costs ($45/patient), heavy IV/EV discounts on pre/post evidence, and uncertain RFMF given CHAI's $100M 100&Change grant. The one RCT available at the time (Graham 2019, Nigeria) found that pulse oximetry reduced mortality among children with ALRI but oxygen supply on top of pulse oximetry showed no additional benefit — raising questions about whether oxygen itself was the active ingredient.

## Key updates

- **First RCT demonstrating mortality benefit from improving oxygen access (Lancet 2024).** A stepped-wedge cluster RCT at 20 rural health facilities in Uganda studied solar-powered oxygen systems for 2,405 hypoxemic children and found a 48.7% reduction in fatal outcomes.[^3] Cost-effectiveness was estimated at $25/DALY averted. This is the first randomized trial directly demonstrating that improving oxygen access at resource-limited hospitals reduces child mortality — resolving the key evidence gap from the original assessment. The effect is consistent with the pooled observational evidence (Lam et al. 2021 systematic review: pooled OR 0.52, 95% CI 0.39–0.70).[^4]

- **Lancet Global Health Oxygen Commission (February 2025) documents massive unmet need and favorable cost-effectiveness.** The Commission found that Sub-Saharan Africa has the lowest oxygen coverage at 9% — pulse oximetry is available at only 10% of primary facilities, and 93% experience oxygen stockouts.[^5] Oxygen therapy for childhood pneumonia was estimated to cost $59/DALY averted (range $21–$225), comparable to routine childhood immunization ($64/healthy life year gained).[^6] The Commission estimates $6.8B/year is needed to close acute oxygen coverage gaps in LMICs, of which 88% remains unfunded.

- **TIMCI trial (2025) demonstrates that pulse oximetry alone is insufficient.** A pragmatic cluster RCT across 172 primary care facilities in India and Tanzania (157,677 children) found that pulse oximetry and clinical decision support did not reduce mortality when implemented at the primary care level.[^7] Hypoxemia prevalence was low in primary care (0.3–0.5%), and referral completion was poor — among hypoxemic children referred, only 30–55% actually attended hospital. This is an important finding for program design: investment in pulse oximetry must be coupled with hospital-level oxygen supply and functional referral systems.

## New CE estimate

My best guess is **~15x cash at $45/patient (range ~7x at $100/patient to ~25x at $26/patient)**. The CE is driven primarily by deaths averted among children with pneumonia and is highly sensitive to per-patient costs. See [oxygen_therapy_for_children BOTEC](../botecs/oxygen_therapy_for_children.xlsx).

The original BOTEC estimated ~7x at $45/patient total. I'm updating upward primarily because (1) the Uganda RCT (adjusted RR 0.51) supports a larger and better-evidenced effect than the original's adjusted RR of ~0.81, and (2) the original BOTEC used incorrect moral weights — it appears to have used ~52.5 UoV per under-5 death averted, whereas GiveWell's actual 2020 moral weights give ~117 UoV for children in this age range (Post Neonatal 100.7, 1–4yr 127.3; see `docs/moral_weights.md`).[^9]

For cost per patient, I'm using $45 as the total program cost — matching the original BOTEC's all-in estimate ($15 CHAI + $15 government + $15 other). Bradley et al. 2021 modeled $26/patient for solar-powered systems, and the Malawi scale-up model finds $35/DALY averted.[^8][^10] But modeled costs often understate real-world implementation costs, particularly for new facility setups with solar infrastructure, so I'm using the higher estimate as my best guess.

The key caveat is that neonatal evidence remains null (Uganda RCT: IRR 1.11; Graham 2019: aOR 1.12; both NS), so benefits are concentrated in children aged 1 month to 5 years.

## Remaining uncertainties

- **Per-patient cost is the pivotal unknown.** Estimates range from $26/patient (Bradley et al. 2021 modeled cost for solar systems)[^10] to $45/patient (original CHAI BOTEC total cost). The Lancet Commission reports $59/DALY averted (range $21–225), suggesting substantial variation.[^6] Actual costs depend heavily on facility type, electricity availability, and oxygen supply chain. Solar-powered systems (as in the Uganda RCT) add significant upfront cost but solve the power reliability problem. Costs could vary 3–5x across settings. The BOTEC uses $45 as a central estimate; the intervention clears 8x at up to ~$75/patient.
- **RFMF is uncertain despite massive unmet need.** The Lancet Commission estimates $6.8B/year is needed, and 88% remains unfunded. Major funders are already active — CHAI ($100M), Unitaid ($22M EAPOA), Global Fund — but US foreign aid cuts (2025) have created new gaps. The specific RFMF for a discrete GW-type funding opportunity needs investigation.
- **Generalizability of the Uganda RCT.** The trial used solar-powered systems in rural Ugandan facilities — a specific (and expensive) configuration. Whether the same mortality effects apply with grid-powered concentrators in semi-urban facilities in other countries is untested. The TIMCI trial's null result in primary care (vs. positive hospital results) underscores that deployment context matters greatly.
- **No neonatal mortality benefit.** Multiple studies find no benefit for neonates (Uganda RCT IRR 1.11, Graham 2019 aOR 1.12 — both non-significant). Neonatal hypoxemia may require different interventions (e.g., CPAP, surfactant) rather than simple oxygen therapy. However, neonates represent only ~8% of the patient pool in the BOTEC.

## Who is implementing / funding this?

- **CHAI** — Dominant implementer, with a $100M MacArthur 100&Change grant covering Ethiopia, India, Kenya, Nigeria, and Uganda. Program has achieved a 431% increase in PSA plants and oxygen equipment across partner facilities.
- **Unitaid** — Invested $22M in the East African Program on Oxygen Access (EAPOA, October 2024), partnering with CHAI and PATH to expand regional liquid oxygen manufacturing in Kenya and Tanzania.
- **Global Oxygen Alliance (GO2AL)** — Coordinated by Unitaid, WHO, and UNICEF. Launched the Global Oxygen Strategic Framework (October 2024) calling for $4B by 2030, estimating each dollar invested delivers $21 in returns.
- **PATH** — Focused on community engagement and primary care integration.
- **WHA Resolution 76.3 (May 2023)** — First WHO resolution on medical oxygen; all 194 member states committed to improving access, though implementation varies.

## Recommended next steps

- **Assess concrete RFMF by talking to CHAI's oxygen team.** The question isn't whether oxygen is cost-effective (it clearly is), but whether there's a discrete funding gap that GW can fill. CHAI's 100&Change grant covers 5 countries — there may be room for expansion to additional high-burden countries (e.g., DRC, Mozambique, Pakistan) or for rural facility coverage within the 5 countries. **Dr. Hamish Graham** (University of Melbourne / MCRI, co-lead of CHAI's oxygen program and author of several key studies including the Nigeria RCT) would be the best person to identify specific funding gaps and the incremental cost of expanding oxygen systems.

- **Investigate the solar-oxygen model from the Uganda RCT for replicability.** The Uganda RCT is the strongest evidence to date and demonstrated feasibility at rural health facilities without reliable power. Understanding the cost breakdown (solar vs. oxygen equipment vs. training), maintainability, and potential for replication in other SSA countries would help assess whether this model could become a GW-funded program. **Dr. Felicity Fitzgerald Nabwire** (lead author, Queen Mary University of London) could provide implementation cost data and lessons learned.

- **Monitor US aid cut impact on oxygen funding.** US foreign aid provided approximately 60% of oxygen-related funding during COVID. Current aid cuts may create genuine gaps that GW could fill cost-effectively. The Global Fund's 8th replenishment and the GO2AL investment case (both due 2025–2026) will signal whether the funding landscape is tightening enough to create discrete philanthropic opportunities.

---

[^1]: "374 million people need medical oxygen annually (364 million acute, 9 million chronic) [...] In LMICs, only 30% of those needing acute oxygen receive it." ([Lancet Global Health Commission on Medical Oxygen, February 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11865010/))

[^2]: "The median hypoxaemia prevalence of children with severe pneumonia requiring hospitalization was 13.3% (IQR 9.3–37.5%). [...] Patients with hypoxaemia had 4.84 times higher odds of death (95% CI 4.11–5.69)." ([Hypoxaemia prevalence systematic review, Lancet Global Health 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11783038/))

[^3]: "After adjustment for clustering and confounding, the relative risk of a fatal outcome was 0·513 (95% CI 0·285–0·915), consistent with a 48·7% (8·5–71·5) reduction in risk of death." ([Nabwire et al., Lancet 2024](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(23)02502-3/abstract))

[^4]: "The pooled OR for oxygen systems reducing childhood pneumonia mortality was 0.52 (95% CI 0.39–0.70). Median cost-effectiveness: $62 per DALY averted (range $44–$225)." ([Lam et al., BMJ Global Health 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8689120/))

[^5]: "Sub-Saharan Africa has the lowest coverage at 9% [...] Pulse oximetry available at 83% of tertiary hospitals, 54% of general hospitals, only 10% of primary facilities [...] 93% of primary facilities and 45% of general hospitals experience oxygen stockouts." ([Lancet Global Health Commission, February 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11865010/))

[^6]: "Oxygen therapy for childhood pneumonia costs $59 per DALY averted (range $21–$225), matching routine childhood immunization ($64 per healthy life year gained)." ([Lancet Global Health Commission, February 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11865010/))

[^7]: [Note] The TIMCI trial (Tools for Integrated Management of Childhood Illness) enrolled 157,677 children across 172 primary care facilities in India and Tanzania. The null finding on mortality is critical for program design — it shows that pulse oximetry at primary care level does not translate into health impact without concurrent strengthening of referral systems and hospital oxygen availability. Source: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12271772/)

[^8]: "Full scale-up of pulse oximetry to 90% usage and oxygen to 80% availability would avert 71,000 DALYs per year [...] ICER of $35 per DALY averted ($33–$36), or $924 per death averted." ([Lin et al. 2025, Lancet Global Health](https://www.sciencedirect.com/science/article/pii/S2214109X25002025))

[^9]: [Note] GiveWell's 2020 moral weights (see `docs/moral_weights.md`) give age-specific values: Post Neonatal (1mo–1yr) = 100.7, 1–4yr = 127.3. For children dying of pneumonia (excluding neonates), a weighted average assuming ~40% post-neonatal and ~60% age 1–4 gives ~117 UoV per death averted. For adults, a weighted average across ages 20–50 gives ~100 UoV per death averted. Source: [GiveWell 2020 moral weights tool](https://docs.google.com/spreadsheets/d/1YiZmHQb-JsDIDJF_tKKVte2x5NOL0CGUTndJNoB0iHo/).

[^10]: "The ICER of solar-powered O2 delivery vs no O2 was $20 (95% CI, $2.83-$206) per DALY saved [...] $26 per patient treated [...] $542 per life saved." ([Bradley et al. 2021, JAMA Network Open](https://pubmed.ncbi.nlm.nih.gov/34165579/))
