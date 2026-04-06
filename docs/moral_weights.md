# GiveWell's 2020 Moral Weights

Source: [2020 update on GiveWell's moral weights](https://docs.google.com/document/d/1hOQf6Ug1WpoicMyFDGoqH7tmf3Njjc15Z1DGERaTbnI/)
Tool (spreadsheet): [Moral weights [2020, Tool]](https://docs.google.com/spreadsheets/d/1YiZmHQb-JsDIDJF_tKKVte2x5NOL0CGUTndJNoB0iHo/)

---

## Age-specific moral weights (UoV per death averted)

One unit of value (UoV) = doubling consumption for one person for one year.

| Age bracket | Moral weight |
|---|---|
| -1 month (stillbirth) | 33.4 |
| Early Neonatal | 83.6 |
| Late Neonatal | 84.5 |
| Post Neonatal (1mo–1yr) | 100.7 |
| 1 to 4 | 127.3 |
| 5 to 9 | 134.3 |
| 10 to 14 | 133.1 |
| 15 to 19 | 126.3 |
| 20 to 24 | 118.0 |
| 25 to 29 | 112.7 |
| 30 to 34 | 106.3 |
| 35 to 39 | 99.7 |
| 40 to 44 | 86.4 |
| 45 to 49 | 75.7 |
| 50 to 54 | 65.2 |
| 55 to 59 | 54.8 |
| 60 to 64 | 39.6 |
| 65 to 69 | 31.4 |
| 70 to 74 | 21.2 |
| 75 to 79 | 16.5 |
| 80 to 84 | 12.4 |
| 85 plus | 12.4 |

## Other key units

| Outcome | Value (UoV) |
|---|---|
| Doubling consumption for one person for one year | 1.0 |
| One year lived with disability (YLD) | 2.3 |

## Headline results (2021 update)

| Outcome | Value |
|---|---|
| Preventing one under-5 death from malaria | 116.3 |
| Preventing one 5-and-over death from malaria | 73.2 |
| Preventing one under-5 death from vitamin A deficiency | 118.7 |
| Averting one stillbirth (1 month before birth) | 33.4 |
| Averting one neonatal death from syphilis | 84.0 |

## Methodology summary

The 2020 weights combine three inputs:
- **60% weight** on donor survey responses (~70 large donors)
- **30% weight** on years of life lost (YLLs), also used as a proxy for IDinsight survey results
- **10% weight** on James Snowden's 2018 GiveWell staff weights

The absolute scale is anchored so that the average of [value of averting under-5 malaria death] and [value of averting 5-and-over malaria death] equals 100, maintaining the same relative value of consumption vs. lives saved as in 2019.

Key properties of the resulting curve:
- Values rise steeply from stillbirth (33.4) through early childhood, peaking at ages 5–14 (~134)
- A "bump" from ages 10–60 (most pronounced 20–40) reflects the value of preventing deaths of people likely to have dependents
- Values decline through older ages as remaining life expectancy falls

## How to use in BOTECs

For any intervention, look up the age brackets relevant to the target population and compute a **weighted average** based on the expected age distribution of deaths averted. Do not use a single blanket number for "under-5" or "adult" deaths — the weights vary substantially by age.

**Example — under-5 pneumonia deaths (excluding neonates):**
If ~40% of deaths are post-neonatal (1mo–1yr) and ~60% are age 1–4:
→ 0.40 × 100.7 + 0.60 × 127.3 = **116.7 UoV per death averted**

**Example — adult hospital patients (mix of maternal, surgical, respiratory):**
Assuming a distribution centered around ages 25–40:
→ Weighted average across relevant brackets ≈ **100 UoV per death averted**
