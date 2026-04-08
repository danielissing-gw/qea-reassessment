# Review: QEA of Cryptococcal Antigen Testing for People Living with HIV

- Link to original QEA: BOTEC only (no writeup produced)
- Year the original analysis was conducted: 2020

## What is this (basic context)

- **What is the problem?** Cryptococcal meningitis (CM) kills an estimated 112,000 people per year globally — 19% of all AIDS-related deaths — with 63% of deaths in sub-Saharan Africa.[^1] CM overwhelmingly affects people with advanced HIV disease (CD4 <100 cells/mm³). Despite being largely preventable through screening and pre-emptive treatment, only 57% of eligible patients are screened, and no country has fully adopted WHO's recommendations.[^2][^3]
- **What is the program?** Screen all ART-initiating patients with CD4 <100 cells/mm³ for cryptococcal antigen (CrAg) using a rapid lateral flow assay ($2.50/test). CrAg-positive patients receive pre-emptive fluconazole to prevent CM; those with confirmed CM receive treatment (now simplified by the AMBITION regimen). The Uganda national program demonstrated this at scale: $459 per death averted.[^4]

## Key updates

- **AMBITION trial (NEJM 2022) dramatically simplifies CM treatment.** The phase 3 trial (n=844 across 5 African countries) demonstrated that a single high dose of liposomal amphotericin B (10 mg/kg on day 1) is non-inferior to 7 days of conventional amphotericin B deoxycholate. Ten-week mortality was 24.8% vs. 28.7% (absolute difference -3.9%), with substantially fewer adverse events — grade 3/4 anemia was 13.3% vs. 39.1%, and blood transfusion needs were 7.6% vs. 18.0%.[^5] This is now the WHO first-line recommendation (2022 updated guidelines).[^6] The single-dose regimen eliminates the need for daily IV infusions for 7 days, dramatically reducing hospitalization requirements and nursing costs in resource-limited settings.

- **PEPFAR funding crisis (2025–2026) creates a massive gap in HIV services — and potentially in CrAg screening.** The Trump administration's foreign aid review froze PEPFAR funding in January 2025. While a limited waiver restored treatment services, the FY2026 budget request proposes cutting PEPFAR from $4.85B to $2.9B — a $1.9B reduction.[^7] UNAIDS estimates 2.5 million people lost PrEP access by October 2025, and modeling projects 6.6 million additional HIV infections and 4.2 million additional AIDS deaths by 2030 if funding ends.[^8] CrAg screening is particularly vulnerable because it falls under diagnostic and prevention services, which received narrower waivers than ART provision. This is a major shift since 2020 — the space was "dominated by PEPFAR" at the time of the original BOTEC, but that dominance is now collapsing.

- **Moral weight correction: the original 100 UoV was approximately correct; my previous "correction" to ~35 was wrong.** The median age of CM patients in sub-Saharan Africa is 33–36 years across multiple clinical studies.[^9] GiveWell's 2020 moral weights give: ages 30–34 = 106.3 UoV, ages 35–39 = 99.7 UoV. A weighted average across the age distribution of CM deaths (concentrated in ages 25–44) gives ~98 UoV per death averted[^10] — close to the original BOTEC's 100 UoV, and nearly 3x the ~35 UoV I used in the initial reassessment.

## New CE estimate

My best guess is **~9x cash at $10/person screened (range ~6x for new point-of-care programs at $20/person to ~14x for maintaining existing reflexed lab programs at $5/person)**. In high-burden settings (CrAg prevalence ~8%), CE rises to ~12x. See [cryptococcal_antigen_testing BOTEC](../botecs/cryptococcal_antigen_testing.xlsx).

The CE is driven by (1) low cost per death averted (~$3,500 in the BOTEC; Uganda's national program achieved $459), (2) appropriate moral weights for young-adult deaths (~98 UoV), and (3) large unmet need (only 57% screening uptake, 0/35 countries fully implementing WHO guidelines). The key parameter is program cost per person screened: reflexed laboratory screening (adding CrAg to existing CD4 samples) costs ~$5–7/person, while new point-of-care programs cost ~$15–20/person. The second key parameter is CrAg prevalence, which ranges from 1.4% (Uganda) to 6.2% (South Africa).

The original BOTEC estimated 27x but applied no IV/EV discounts and used a simpler cost model. My updated best guess of ~9x applies 80% IV and 85% EV discounts and uses more realistic all-in program costs. This is a downgrade from the original but still clears the 8x bar at best-guess parameters, and is a substantial correction from my previous (incorrect) estimate of ~8–10x, which was driven by a faulty moral weight assumption (~35 UoV instead of the correct ~98 UoV).

## Remaining uncertainties

- **Is there a specific, discrete philanthropic funding opportunity?** The PEPFAR cuts create a general gap, but GiveWell would need a concrete program to fund — e.g., maintaining a specific country's CrAg screening program that's losing PEPFAR support, or supporting CHAI's THRIVE project to expand screening to additional countries. Without a specific implementing partner and country, this remains theoretical.
- **Cost per death averted in a philanthropic program vs. government-run.** The Uganda figure ($459/death averted) is from a national government program integrated into existing lab infrastructure. A new philanthropic program would likely cost 2–3x more, depending on whether it uses reflexed lab testing or point-of-care. This is the pivotal parameter: at $500/death averted, CE is ~27x; at $1,500, it's ~15x; at $3,000, it's ~7x.
- **CrAg prevalence varies enormously by setting.** South Africa national data shows 6.2% at CD4 <100; Uganda's program found 1.4%.[^11] Higher prevalence means more deaths averted per person screened, improving CE. Target country selection would be important.
- **Sustainability of PEPFAR cuts.** The cuts could be reversed by a future administration. But even a 2–3 year gap in screening programs would lead to thousands of preventable deaths, and GW bridge funding during this period could be highly impactful regardless of longer-term PEPFAR restoration.

## Who is implementing / funding this?

- **CHAI** (Clinton Health Access Initiative) — Leads the Unitaid-funded THRIVE project for advanced HIV disease management, operating in 11 countries with implementation research in 5 countries.[^12] CHAI is the most likely implementing partner for a GW-funded program.
- **South Africa NHLS** — Operates the most established national reflexed CrAg screening program (since 2016), processing ~283,000 specimens/year at CD4 <100.[^13]
- **MSF** — Runs CrAg screening programs in 15 countries as part of its advanced HIV disease response.
- **PEPFAR** — Historically the dominant funder, now facing $1.9B in proposed cuts. Programs that lose PEPFAR funding would need alternative support.
- **Global Fund** — Includes CrAg tests on its procurement list, enabling bulk purchasing. But Global Fund grants are country-directed and may not fill PEPFAR-specific gaps quickly.
- **DNDi** — Published the 2023 report assessing 35 countries' WHO guideline adoption; plays an advocacy and monitoring role.

## Recommended next steps

- **Talk to CHAI's THRIVE project team about specific funding gaps created by PEPFAR cuts.** CHAI operates in 11 countries and would know which CrAg screening programs are most at risk and what the marginal cost of maintaining them would be. The key question: is there a $1–5M funding gap that GW could fill to maintain CrAg screening in a specific country for 2–3 years? **Dr. David Meya** (Infectious Diseases Institute, Makerere University, Uganda; co-PI on AMBITION and the Uganda national CrAg program) would be an ideal contact — he has deep knowledge of both the clinical evidence and program costs.

- **Investigate reflexed lab screening costs in 2–3 high-burden countries.** The CE estimate is highly sensitive to per-person screening costs. Reflexed lab screening (adding CrAg to existing CD4 samples) is dramatically cheaper than point-of-care, but requires existing lab infrastructure. Understanding which countries have this infrastructure and what the marginal cost would be to maintain CrAg screening could reveal very high-CE opportunities. South Africa (NHLS) and Uganda (national program) are the best-documented models.

- **Verify that CrAg screening programs are actually losing funding due to PEPFAR cuts.** The PEPFAR waiver explicitly covers "HIV testing" — it's unclear whether CrAg screening is covered under this waiver or falls outside it. If CrAg screening is maintained under the waiver, the philanthropic opportunity is smaller. The KFF PEPFAR tracker and CHAI country teams would be the best sources for this information.

---

[^1]: "In 2020, there were an estimated 152 000 incident cases (95% uncertainty interval 111 000–205 000) of cryptococcal meningitis in people living with HIV, resulting in an estimated 112 000 deaths (79 000–134 000) [...] The proportion of AIDS-related deaths attributable to cryptococcal meningitis was 19% (IQR 13–24%)." ([Rajasingham et al., Lancet Infectious Diseases 2022](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(22)00042-7/fulltext))

[^2]: "The pooled estimate of CrAg screening uptake was 57.1% (95% CI 41.4-72.7) [...] overall pooled estimates of uptake of CrAg screening, cryptococcal antigenemia and preemptive initiation of antifungal medications in these settings were 57%, 9% and 85%, respectively." ([Systematic review, PLOS ONE 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11761098/))

[^3]: "None of the 35 countries assessed had fully adopted WHO's recommendations for cryptococcal meningitis and advanced HIV disease (AHD)." ([DNDi press release, 2023](https://dndi.org/press-releases/2023/cryptococcal-meningitis-new-report-highlights-slow-uptake-guidelines-shown-reduce-deaths-africa/))

[^4]: "CrAg screening and treatment in the base case cost $3,356,724 compared to doing nothing, and saved 7,320 lives [...] cost of $459 per life saved." ([Michelow et al., PLOS ONE 2019 — Uganda national program evaluation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6328136/))

[^5]: "At 10 weeks, 101 of 407 patients (24.8%; 95% confidence interval [CI], 20.7 to 29.3) had died in the AmBisome group, as compared with 117 of 407 (28.7%; 95% CI, 24.4 to 33.4) in the control group [...] Grade 3 or 4 adverse events occurred in 50.0% of the patients in the AmBisome group and 62.3% in the control group. Grade 3 or 4 anemia occurred in 13.3% and 39.1%, respectively." ([Jarvis et al., NEJM 2022](https://www.nejm.org/doi/full/10.1056/NEJMoa2111904))

[^6]: "The 2022 WHO guidelines recommend a single high dose (10 mg/kg) of liposomal amphotericin B with 14 days of flucytosine and fluconazole as the preferred induction regimen for cryptococcal meningitis treatment." ([WHO Guidelines for Diagnosing, Preventing and Managing Cryptococcal Disease, 2022](https://www.who.int/publications/i/item/9789240052178/))

[^7]: "The FY 2025 Continuing Resolution that passed in March included level funding for PEPFAR's bilateral programming at USAID, State, CDC, and DoD of $4.85 billion [...] The administration's FY 2026 budget request includes $2.9 billion for bilateral PEPFAR activities, a decrease of $1.9 billion." ([KFF PEPFAR Status Tracker, 2026](https://www.kff.org/global-health-policy/the-trump-administrations-foreign-aid-review-status-of-pepfar/))

[^8]: "UNAIDS estimated that by October 2025, 2.5 million people who had been using PrEP in 2024 lost access to the medication solely because of funding cuts [...] If PEPFAR funding ends, there could be an additional 6.6 million HIV infections and over 4.2 million AIDS-related deaths by 2030." ([PMC — PEPFAR Funding Suspension Impact Analysis, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11959925/))

[^9]: "Majority of participants were male aged 32-36 years" across studies in the systematic review of CM mortality in Africa. ([Frontiers in Medicine, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9494297/))

[^10]: [Note] GiveWell's 2020 moral weights (see `docs/moral_weights.md`): 25–29yr = 112.7, 30–34yr = 106.3, 35–39yr = 99.7, 40–44yr = 86.4. Assuming an age distribution of CM deaths: 15% ages 25–29, 25% ages 30–34, 25% ages 35–39, 20% ages 40–44, 10% ages 45–49, 5% ages 20–24: weighted average = 0.05×118 + 0.15×112.7 + 0.25×106.3 + 0.25×99.7 + 0.20×86.4 + 0.10×75.7 = 98.8, rounded to ~98.

[^11]: "A cost per result of $5.897 was reported for reflexed CrAg testing for a count < 100 cells/uL" at national CrAg detection rate of 6.2% in South Africa. ([PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11538356/)) Uganda prevalence: 1.4% per Michelow et al. 2019.

[^12]: "Unitaid funds the CHAI-led THRIVE Project in collaboration with Afrocab and Penta to enable access to critical prevention, screening, and treatment commodities for advanced HIV disease [...] operating in 11 countries with implementation research in five countries." ([Unitaid AHD Project](https://unitaid.org/project/preventing-hiv-related-deaths-by-optimizing-advanced-hiv-disease-management/))

[^13]: [Note] South Africa NHLS processes approximately 283,240 specimens with CD4 <100 cells/uL annually. The reflexed screening model automatically tests all CD4 <100 samples for CrAg, with marginal cost of ~$5.90 per result. Source: PMC 2024 South Africa extended threshold analysis.
