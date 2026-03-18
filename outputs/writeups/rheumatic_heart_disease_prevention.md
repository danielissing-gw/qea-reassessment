# Review: Rheumatic Heart Disease Prevention QEA

- Link to original QEA: [Rheumatic heart disease prevention QEA](https://docs.google.com/document/d/1siZVFAA3E3SLWroQ_oQqTuxUBMfEYvM_z8tL6eOp2Y8/edit)
- Link to original BOTEC: [RHD Prevention BOTEC](https://docs.google.com/spreadsheets/d/1FVr6y-dke7kJUIDbEt5Bqah4zPsc7gaBEqFki08DKaA/edit)
- Year the original analysis was conducted: 2021

## What is this (basic context)

- **What is the problem?** Untreated Group A Streptococcus (GAS) pharyngitis can trigger acute rheumatic fever (ARF), which scars heart valves — a condition called rheumatic heart disease (RHD). RHD is the leading acquired heart disease among young people in LMICs and kills roughly 300,000–400,000 people per year globally, with India bearing the largest single-country share.
- **What is the program?** A combination of primary prevention (identifying and treating GAS pharyngitis with penicillin before it causes ARF) and secondary prevention (regular benzathine penicillin injections for people who have already had ARF, to prevent recurrence and further valve damage). Programs typically involve community and healthcare worker education, patient registries, and improved diagnosis.
- **Why did we deprioritize this?** The original investigation was paused before forming a full QEA-level opinion. The 2021 BOTEC showed 58.6x cash, but GiveWell was "extremely skeptical of its current output" due to: (1) program costs drawn from a Cuba academic study, likely a gross underestimate for India; (2) downstream medical costs excluded entirely; (3) uncertainty about what exactly was being modeled and whether it could be replicated.

## Key updates

### 1. WHO published its first-ever RF/RHD prevention guidelines (November 2024)

The WHO 2024 Guideline on the Prevention and Diagnosis of Rheumatic Fever and Rheumatic Heart Disease is the first WHO guideline specific to RF/RHD. On primary prevention, it makes a strong recommendation for treating confirmed GAS pharyngitis with antibiotics to prevent RF/RHD.[^1] Critically for LMIC settings without testing capacity, it also makes a strong recommendation for empirical treatment of clinically-suspected GAS in high-risk populations even without diagnostic confirmation.[^2] On secondary prevention, it recommends IM benzathine benzylpenicillin as the preferred first-line approach.[^3]

This is significant on two levels. First, it removes policy ambiguity: countries with endemic RHD now have WHO backing to implement empirical antibiotic treatment for clinically suspected GAS even without diagnostic confirmation — removing a major implementation barrier. Second, WHO endorsement can enable government co-financing and integration into national primary healthcare programs, which could substantially reduce marginal program costs versus a standalone intervention.

### 2. GBD 2021 estimates India's RHD burden substantially higher than the original BOTEC assumed

The original BOTEC used a GBD figure of ~129,000 deaths/year in India. A 2023 AHA abstract using GBD 2021 data reports India had an estimated 166,017 RHD deaths in 2021.[^4] A 2025 Frontiers in Public Health analysis of GBD 2021 reports that South Asia's age-standardized RHD mortality rate is 3.3 times the global average.[^5] This ~29% higher burden estimate (166k vs 129k) directly increases the number of deaths averted per dollar spent in the model.

I could not verify the 166,017 figure against the raw GBD 2021 database — this comes from an AHA conference abstract. I'm treating it as approximately correct but with medium confidence.

### 3. A 2023 India cost-effectiveness analysis finds secondary prevention highly cost-effective

A Lancet Global Health extended cost-effectiveness analysis of RF/RHD prevention strategies in India found that a combination of secondary and tertiary prevention strategies had an incremental cost of approximately $30 per QALY gained.[^6]

The original BOTEC modeled primary prevention only. Secondary prevention (regular BPG injections for known ARF/RHD patients) has a different cost structure — benzathine penicillin is very cheap — and may be the more fundable program. At $30/QALY, secondary prevention is approximately 100–150x our benchmark on a DALY-equivalent basis, though the modeling context and assumptions would need to be understood before relying on this figure.

### Sense-check of original BOTEC

The math is internally consistent (verified):[^7]

Major concerns:

- **Cost almost certainly underestimated.** The BOTEC itself says the cost estimate "may be an underestimate, possibly a gross one."[^8] The $0.09/person-year figure from Cuba is far below comparable health programs. Downstream treatment costs (drugs, consultations for identified cases, secondary prevention injections) are explicitly excluded. I'm assuming real-world costs in India would be 3–10x higher, though the original noted the intervention would still be 10x cash even at 6x cost increase.
- **89% effect from Cuba likely overstated for India context.** Cuba has universal free healthcare with strong primary care infrastructure. The original notes Pinar del Rio has "a well-structured medical assistance system with free and easy accessibility to medical care and treatment for the whole population."[^9] The 0.49 combined validity adjustment (0.7 x 0.7) may still be generous.
- **Missing benefit streams.** The original notes that RHD is "the principal heart disease seen in pregnant women" and causes significant perinatal morbidity and mortality — but this is excluded from the BOTEC.[^10] Including morbidity, perinatal outcomes, and treatment cost offsets would increase the CE estimate.

## New CE estimate

**~20–40x cash** (highly uncertain). See BOTEC at `./outputs/botecs/rheumatic_heart_disease_prevention.xlsx`.

Updated parameters: India burden revised to 166k deaths (GBD 2021) from 129k, increasing modeled deaths averted by ~29%. CPI adjustment updated from 2021 to 2026. All other parameters unchanged.

The updated BOTEC yields ~62x on the revised assumptions, but this is almost certainly too high due to cost underestimation. The key message is unchanged from 2021: even under significantly higher costs (3–6x), the intervention likely remains well above the 8x bar. The India secondary prevention CEA ($30/QALY ~ 100x benchmark) provides independent corroboration that RHD prevention is highly cost-effective in India.

Confidence: **Low** — cost remains the pivotal unknown and no new cost data was found.

## Remaining uncertainties

1. **What would a primary or secondary prevention program actually cost in India?** The Cuba cost estimate ($0.09/person-year) is the most important parameter to verify. A realistic India cost estimate — accounting for CHW labor, drug procurement, diagnostic infrastructure, and downstream treatment — is the single most important input to resolve.

2. **What does a fundable program look like, and who would implement it?** The original notes that programs have been "fully operationalized at scale" in Cuba, Costa Rica, New Zealand, and Guadeloupe, but there is no equivalent NGO-led program in South Asia. Whether any organization could implement this at scale in India — and at what cost — is unknown.

3. **Does WHO endorsement change the funding landscape?** The 2024 WHO guidelines could trigger national policy changes in India (NP-NCD integration) that would drastically reduce marginal program costs. This should be actively investigated given the 2024 publication timing.

## Who is implementing / funding this?

- **RHD Action** (coalition of Medtronic Foundation, World Heart Federation, RhEACH): focused on advocacy, technical assistance, and small grants. The original QEA notes they were "vague on what they actually do" — this may have changed since 2021.
- **World Heart Federation RHD Taskforce** (established 2018): three arms — surgery access, policy/advocacy, and prevention/control. I'm not sure of their current program footprint in South Asia.
- **RHD Australia**: active in Aboriginal communities; likely not relevant for India scale-up.
- No large-scale implementer in South Asia was identified. Most activity is advocacy and guideline work.

## Recommended next steps

1. **Get a realistic cost estimate for India context.** The $0.09/person-year Cuba figure is the pivotal uncertainty. The **WHO RHD team in Geneva** (who modeled costs for the 2024 guideline) or the team behind the 2023 Lancet India CEA (lead author of the paper at S2214109X22005526) would be the most direct sources. This would either confirm high CE or reveal the intervention is cost-prohibitive at India scale.

2. **Review the 2023 Lancet India CEA in full.** The $30/QALY finding for secondary prevention — if the assumptions are defensible — implies this could be one of the most cost-effective interventions GiveWell has ever considered. Understanding what drives that number (what costs are assumed, what population, what effect size) should be the next analytical step.

3. **Investigate whether Indian government policy has changed post-2024 WHO guidelines.** If India's NP-NCD or state health departments have incorporated GAS pharyngitis treatment into routine care since November 2024, this could mean government co-financing for the drug component and a dramatically lower marginal program cost. The **Indian Council of Medical Research** or **National Centre for Disease Control** would be the right entities to contact.

---

[^1]: "Children, adolescents and adults with sore throat and a positive diagnostic test for GAS pharyngitis should be treated with antibiotics to prevent RF/RHD." (Strong recommendation, moderate certainty evidence) https://www.ncbi.nlm.nih.gov/books/NBK609692/

[^2]: "In populations at moderate to high risk of RF and RHD and where diagnostic testing to confirm GAS (with either POC testing or microbial confirmation) is not available, children and adolescents with clinically-suspected GAS pharyngitis should be treated with antibiotics to prevent RF/RHD." (Strong recommendation, very low certainty evidence) https://www.ncbi.nlm.nih.gov/books/NBK609692/

[^3]: "IM benzathine benzylpenicillin is the preferred first-line approach to prevent recurrence of RF in patients with prior RF or RHD." (Strong recommendation, moderate certainty evidence) https://www.ncbi.nlm.nih.gov/books/NBK609692/

[^4]: "India had an estimated 166,017 RHD deaths in 2021" — reported in an AHA Circulation 2023 abstract on trends in RHD mortality in India using GBD 2021 data. I could not verify this against the raw GBD database. https://www.ahajournals.org/doi/10.1161/circ.150.suppl_1.4144731

[^5]: "South Asia experienced an age-standardized mortality rate of 14.88 per 100,000, representing 3.3 times the global average." https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1674434/full

[^6]: "A combination of secondary and tertiary prevention strategies, which had an incremental cost of ₹23,051 (US$30) per QALY gained, was the most cost-effective strategy for the prevention and control of rheumatic fever and rheumatic heart disease in India." I was unable to access the full paper — this quote is sourced from a secondary review. https://www.sciencedirect.com/science/article/pii/S2214109X22005526

[^7]: [Note] The original BOTEC math checks out: 89% effect x 0.7 IV x 0.7 EV = 43.6% reduction. 1,500 lifetime RHD deaths per 100k x 43.6% = 654 deaths averted. 654 x 52.5 units/death = 34,342 units of value. Cost per 100k = $170,277; units per $100k = 20,168; vs GiveDirectly 344 units/$100k → 58.6x.

[^8]: "I think the benefits estimate is plausible (although uncertain), but I am skeptical of the cost estimate." and "I am concerned that the cost estimate (from the academic lit) may be an underestimate, possibly a gross one" https://docs.google.com/document/d/1siZVFAA3E3SLWroQ_oQqTuxUBMfEYvM_z8tL6eOp2Y8/edit

[^9]: "a well-structured medical assistance system with free and easy accessibility to medical care and treatment for the whole population" — cited in original QEA from the Cuba intervention paper. https://docs.google.com/document/d/1siZVFAA3E3SLWroQ_oQqTuxUBMfEYvM_z8tL6eOp2Y8/edit

[^10]: "the principal heart disease seen in pregnant women" — from WHO RHD page, cited in the original QEA. https://docs.google.com/document/d/1siZVFAA3E3SLWroQ_oQqTuxUBMfEYvM_z8tL6eOp2Y8/edit
