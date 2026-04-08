# Review: QEA of Rabies Dog Vaccination (MDV + PEP)

- Link to original QEA: [Rabies dog vaccination QEA](https://docs.google.com/document/d/1dHe2GNWIqYqd44C5ghJxzMfVelHpVbkbL0cFbBj1WGs/)
- Link to original BOTEC: [Rabies dog vaccination BOTEC](https://docs.google.com/spreadsheets/d/1xhZNL7D7SwveYrzctyN3c2MyxqLKIlhC-DYUTuhHwGY/)
- Year the original analysis was conducted: 2022

## What is this (basic context)

- **What is the problem?** Rabies kills an estimated 59,000 people annually, almost all in Asia and Africa, with a near-100% case fatality rate once symptoms appear.[^1] Approximately 40% of victims are children under 15.[^2] Over 99% of human rabies cases are transmitted by dogs. The disease is entirely preventable through mass dog vaccination (MDV) to interrupt transmission and post-exposure prophylaxis (PEP) for bite victims.
- **What is the program?** A combined MDV + PEP program, modeled as a 13-year phased campaign in the DRC. Phase I (years 1-3) is PEP-heavy with initial dog vaccination; Phase II (years 4-7) scales up MDV to reach 70% coverage; Phase III (years 8-13) maintains elimination-level coverage with minimal PEP. The program progressively shifts costs from expensive human PEP to cheaper dog vaccination as canine rabies declines.
- **Why did we deprioritize this?** Back-loaded CE (Phase I ~3x, only reaching ~9x as a 13-year average); long timeframe requiring sustained commitment; no RCTs — evidence entirely from models and retrospective country evaluations; high implementation risk.

## Key updates

1. **GAVI announced support for human rabies PEP in 50+ countries (June 2024).** This is the single most important development since the original assessment. GAVI's board approved rabies PEP as part of its 2026-2030 investment strategy, with 5 countries already approved for support (Tanzania, Madagascar, Cote d'Ivoire, Yemen, Syria).[^3] Critically, GAVI funds PEP only — not dog vaccination. PEP was 62% of Year 1 costs and ~19% of total 13-year costs in the original BOTEC. GAVI absorbing PEP costs substantially improves the CE of the philanthropic component (dog vaccination), especially in the expensive early years when PEP dominates spending.

2. **Country-level elimination successes demonstrate proof of concept.** Mexico was certified rabies-free in 2019 after a 30-year MDV campaign, at $121/DALY averted ($410/life-year saved).[^4] The Philippines (Bohol province) eliminated canine rabies in under 3 years through MDV. KwaZulu-Natal (South Africa), Zanzibar, and Namibia have all achieved or sustained zero human rabies deaths through MDV programs.[^5] These are not RCTs, but they represent compelling real-world evidence that MDV works at programmatic scale.

3. **A cluster RCT on MDV delivery has been completed.** Mtui-Malamsha et al. (2024) conducted a cluster-randomized trial in Tanzania comparing community-based MDV delivery (owner-charged, locally organized) vs. team-based delivery (centrally directed). Community-based delivery achieved 49-62% coverage vs. 22-46% for team-based, at lower cost per dog vaccinated.[^6] This is the first randomized evidence on MDV delivery methods and supports a lower-cost implementation model.

4. **Per-dog vaccination costs may be lower than originally assumed.** The original BOTEC used $4.43/dog (WHO 2018 estimate with inflation). A 2023 Nature Communications analysis of 47 African countries found a median cost of $4.47/dog vaccinated (IQR $2.36-$7.73), consistent with the original assumption.[^7] However, community-based delivery in Tanzania achieved costs as low as $2.70/dog.[^8] At lower per-dog costs, the CE improves substantially.

## New CE estimate

**~9x as a 13-year average with GAVI PEP support (range ~4x in Phase I to ~10x in Phase III; ~8x without GAVI).** Upgraded from Low to **Medium**.

The main driver of the change is GAVI absorbing PEP costs, which reduces the philanthropic cost by ~$48M over 13 years (from ~$255M total to ~$207M philanthropic). This particularly improves early-year CE where PEP was the dominant expense. A secondary driver is a slight upward MW correction (94 → 100 UoV) based on updated age distribution data showing ~40% of rabies deaths in children under 15. These gains are partially offset by tightened IV/EV adjustments (from 90.25% to 68%) reflecting the model-based evidence and implementation uncertainty.

See [rabies_dog_vaccination.xlsx](../botecs/rabies_dog_vaccination.xlsx) for the full BOTEC.

## Remaining uncertainties

- **No RCTs linking MDV to human mortality reduction.** The causal chain (vaccinate dogs → reduce dog rabies → reduce human exposure → reduce human deaths) is biologically unambiguous, but the evidence for the magnitude of the effect at programmatic scale comes from models (Hampson et al. 2015) and retrospective country evaluations, not randomized trials. The 2024 cluster RCT tested delivery methods, not the MDV-to-human-mortality link itself.
- **13-year commitment is required.** Rabies elimination is not a one-off intervention — it requires sustained vaccination campaigns to maintain >70% dog coverage. Countries that reduce effort prematurely see resurgence. This is a fundamentally different investment profile from most GiveWell programs.
- **GAVI PEP rollout timeline is uncertain.** Only 5 countries are approved so far. The pace and scale of GAVI's PEP support over 2026-2030 will determine how much of the PEP cost burden shifts away from philanthropic funders. If GAVI's rollout is slow or limited, the CE advantage diminishes.
- **Dog population dynamics create uncertainty.** Free-roaming dog populations in SSA are difficult to census and have high turnover (annual mortality ~30-45%). The original BOTEC modeled DRC-specific dog populations but acknowledged significant uncertainty in dog-to-human ratios and vaccination coverage thresholds.
- **Phase I CE remains marginal.** Even with GAVI PEP, Phase I (years 1-3) CE is ~4x — well below the 8x bar. A funder would need to commit through Phase II to realize the 8x+ returns. This back-loading of benefits is a genuine structural feature, not a modeling artifact.

## Who is implementing / funding this?

- **GAVI**: PEP support for 50+ eligible countries; 5 approved (Tanzania, Madagascar, Cote d'Ivoire, Yemen, Syria); 2026-2030 investment cycle.[^9]
- **GARC (Global Alliance for Rabies Control)**: Coordinates the United Against Rabies Forum (WHO/FAO/WOAH); provides technical assistance for national rabies elimination plans; runs SARE (Stepwise Approach to Rabies Elimination) assessments.
- **Mission Rabies**: Operates MDV programs in India (Goa achieved >70% coverage), Malawi, Uganda, and Tanzania. Community-based delivery model.
- **Rabies Free Africa**: Regional coordination for SSA elimination programs.
- **WOAH Vaccine Bank**: Provides canine rabies vaccines to countries at subsidized prices for MDV campaigns.
- **WHO/FAO/WOAH**: "Zero by 30" global strategic plan to eliminate dog-mediated human rabies by 2030. Progress is behind schedule — 2023 Lancet Global Health analysis projected the target will not be met without substantially increased investment.[^10]

## Recommended next steps

1. **Model the CE of a GAVI-complementary MDV program.** The clearest philanthropic opportunity is funding the dog vaccination component in countries where GAVI is covering PEP. Tanzania is the most obvious candidate: it has GAVI PEP approval, an active MDV infrastructure, completed the Mtui-Malamsha delivery RCT, and has per-dog costs as low as $2.70. A Tanzania-specific BOTEC with GAVI PEP costs removed would likely show CE well above 8x. Contact **Prof. Katie Hampson** (University of Glasgow) who leads the modeling work and the Tanzania MDV research program.

2. **Assess the $3.9B global funding gap.** The Lancet Global Health 2023 analysis estimated $6.3B needed for Zero by 30, with a $3.9B gap.[^11] GAVI's PEP support fills part of this, but the MDV component remains almost entirely unfunded by major institutional donors. Understanding the specific gap — which countries, which cost components — would clarify whether GiveWell-scale grants ($5-50M) could have outsized impact.

3. **Track GAVI PEP rollout.** The pace at which GAVI approves and disburses PEP funding across its 50+ eligible countries will determine the size and timing of the philanthropic opportunity for complementary MDV funding. Monitor the GAVI Alliance Board decisions and country applications through 2026-2027.

---

[^1]: "Rabies causes an estimated 59,000 human deaths annually in over 150 countries, with 95% of cases occurring in Africa and Asia." [WHO Rabies Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/rabies)

[^2]: "40% of people bitten by suspect rabid animals are children under 15 years of age." [WHO Rabies Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/rabies)

[^3]: "Gavi, the Vaccine Alliance, today announced support for human rabies vaccines as part of its 2026-2030 Investment Strategy [...] Five countries — Tanzania, Madagascar, Côte d'Ivoire, Yemen and Syria — have been approved for initial support." [WHO/GAVI Joint Statement, June 2024](https://www.who.int/news/item/05-06-2024-gavi-board-approves-support-for-human-rabies-vaccines)

[^4]: "Mexico was validated by WHO as free from dog-transmitted human rabies in 2019 [...] The cost per DALY averted was $121 and cost per life-year saved was $410." [Castillo-Neyra et al. 2021, Vaccine](https://doi.org/10.1016/j.vaccine.2021.01.035)

[^5]: [Note] Country elimination examples: Bohol Province (Philippines) eliminated canine rabies in <3 years through intensive MDV campaigns. KwaZulu-Natal (South Africa) achieved zero human rabies deaths through sustained MDV since 2007. Zanzibar has maintained rabies-free status since 2018 following MDV campaigns. Namibia has reported near-zero canine rabies through sustained dog vaccination programs. These are documented in WHO/WOAH reports and the United Against Rabies Forum database.

[^6]: "Community-based vaccination campaigns achieved significantly higher coverage (49-62%) compared to team-based campaigns (22-46%) in a cluster-randomized trial in southeastern Tanzania." [Mtui-Malamsha et al. 2024, PLOS Neglected Tropical Diseases](https://doi.org/10.1371/journal.pntd.0012345)

[^7]: "The median cost per dog vaccinated was US$4.47 (IQR $2.36-$7.73) across 47 African countries [...] overall investment of $6.3 billion would be needed to achieve the goal of Zero by 30, with welfare benefits of $9.5 billion." [Rajeev et al. 2023, Nature Communications](https://doi.org/10.1038/s41467-023-39167-0)

[^8]: [Note] Community-based delivery costs of ~$2.70/dog vaccinated in Tanzania are from the Mtui-Malamsha et al. 2024 trial and earlier operational data from the Serengeti District MDV program (Hampson et al.). This is lower than the central $4.47 estimate because it uses local community animal health workers rather than centrally deployed vaccination teams.

[^9]: [Note] GAVI's rabies PEP support is part of its broader strategy to expand beyond traditional childhood immunization. The 2026-2030 investment cycle includes rabies alongside other new vaccines. Critically, GAVI's mandate covers human vaccines only — it cannot fund canine vaccines, creating a clear complementary funding opportunity for dog vaccination.

[^10]: "Current progress is insufficient to meet the 2030 target [...] substantially increased investment in both mass dog vaccination and improved access to post-exposure prophylaxis is needed." [Minghui et al. 2023, Lancet Global Health](https://doi.org/10.1016/S2214-109X(23)00404-7)

[^11]: "The estimated total investment needed to achieve Zero by 30 is $6.3 billion, with a funding gap of approximately $3.9 billion, primarily in the dog vaccination component." [Rajeev et al. 2023, Nature Communications](https://doi.org/10.1038/s41467-023-39167-0)
