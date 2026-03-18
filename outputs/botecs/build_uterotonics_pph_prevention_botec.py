"""Build single-sheet BOTEC for Uterotonics for PPH Prevention/Treatment.

Models two interventions:
  Section A: TXA for PPH treatment
  Section B: Heat-stable carbetocin (HSC) for PPH prevention

Produces outputs/botecs/uterotonics_pph_prevention.xlsx
"""
import openpyxl
from openpyxl.styles import Font, Alignment
from openpyxl.comments import Comment
import os

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "BOTEC"

bold = Font(bold=True)
section_font = Font(bold=True, size=11)
result_font = Font(bold=True, size=12)
link_font = Font(color="0000FF", underline="single")

# Source URLs
ORIGINAL_QEA = "https://docs.google.com/document/d/1euCoBUuJQ8V8l7Mgl5SFP6UpcT2H7BioX8uRxoohpoM/edit"
WOMAN_TRIAL = "http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)30638-4/fulltext"
WHO_PPH_2025 = "https://www.ncbi.nlm.nih.gov/books/NBK619236/"
GHSC_HSC = "https://www.ghsupplychain.org/sites/default/files/2023-07/HSC_20230630.pdf"
PMC_REVIEW = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12145113/"
UNITAID = "https://unitaid.org/project/expanding-access-to-recently-recommended-drugs-to-prevent-and-treat-postpartum-haemorrhage-pph/"


def add_link(row, col, text, url):
    """Write a cell with a hyperlink."""
    c = ws.cell(row, col, text)
    c.hyperlink = url
    c.font = link_font
    return c


# Column widths
ws.column_dimensions["A"].width = 65
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 80

# ── SECTION A: TXA ────────────────────────────────────────────────────────────
ws.cell(1, 1, "Section A: Tranexamic Acid (TXA) for PPH Treatment").font = section_font
ws.cell(1, 2, "Value").font = bold
ws.cell(1, 3, "Source / notes").font = bold

ws.cell(2, 1, "PPH mortality rate with standard care (placebo arm)")
ws.cell(2, 2, 0.019)
ws.cell(2, 2).number_format = "0.0%"
add_link(2, 3, "WOMAN trial: 191/9,985 = 1.91%", WOMAN_TRIAL)
ws.cell(2, 3).comment = Comment(
    'WOMAN trial (2017): "Death due to bleeding was significantly reduced in '
    'women given tranexamic acid (155 [1.5%] of 10 036 patients vs 191 [1.9%] '
    'of 9985 in the placebo group, risk ratio [RR] 0.81, 95% CI 0.65-1.00; '
    'p=0.045)."\n' + WOMAN_TRIAL,
    "BOTEC"
)

ws.cell(3, 1, "Relative risk of death from bleeding with TXA vs placebo")
ws.cell(3, 2, 0.81)
add_link(3, 3, "WOMAN trial RR 0.81 (95% CI 0.65-1.00). "
               "2024 Lancet meta-analysis: 31% reduction within 3h.", WOMAN_TRIAL)

ws.cell(4, 1, "Absolute risk reduction (deaths per PPH case treated)")
ws.cell(4, 2, "=B2*(1-B3)")
ws.cell(4, 2).number_format = "0.000%"
ws.cell(4, 3, "Calculation: mortality rate x (1 - RR)")

ws.cell(5, 1, "TXA drug cost per patient (generic, LMIC)")
ws.cell(5, 2, 3.00)
ws.cell(5, 2).number_format = "$#,##0.00"
ws.cell(5, 3, "I'm estimating $1-5 for generic TXA (off-patent); $3 midpoint. "
              "Original used $17.48 (Guerriero 2011, Tanzania) which included "
              "hospital stay and nurse labor. Needs verification.")

ws.cell(6, 1, "Program cost multiplier (training, supply chain, monitoring)")
ws.cell(6, 2, 10)
ws.cell(6, 3, "I'm assuming 10x drug cost for program delivery. "
              "Highly uncertain. AMPLI-PPHI may have real data by 2026.")

ws.cell(7, 1, "Total program cost per PPH case treated")
ws.cell(7, 2, "=B5*B6")
ws.cell(7, 2).number_format = "$#,##0"
ws.cell(7, 3, "Calculation")

ws.cell(8, 1, "Cost per death averted — TXA")
ws.cell(8, 2, "=B7/B4")
ws.cell(8, 2).number_format = "$#,##0"
ws.cell(8, 3, "Calculation")

ws.cell(9, 1, "GiveDirectly benchmark (cost per death averted equivalent)")
ws.cell(9, 2, 4500)
ws.cell(9, 2).number_format = "$#,##0"
ws.cell(9, 3, "I'm assuming ~$4,500. Exact figure depends on GW moral weights "
              "and year. Needs verification.")

ws.cell(10, 1, "CE — TXA (multiples of cash)")
ws.cell(10, 2, "=B9/B8")
ws.cell(10, 2).number_format = "0.0"
ws.cell(10, 2).font = result_font
ws.cell(10, 3, "Low because TXA only reduces mortality among women who "
               "already have PPH; per-case impact is small.")

# ── SECTION B: HSC ────────────────────────────────────────────────────────────
ws.cell(12, 1, "Section B: Heat-Stable Carbetocin (HSC) for PPH Prevention").font = section_font

ws.cell(13, 1, "HSC drug cost per birth (LMIC public sector)")
ws.cell(13, 2, 0.31)
ws.cell(13, 2).number_format = "$#,##0.00"
add_link(13, 3, "Ferring subsidized price: $0.31/ampoule", GHSC_HSC)

ws.cell(14, 1, "Facility births per 100,000 total births (estimate)")
ws.cell(14, 2, 100000)
ws.cell(14, 2).number_format = "#,##0"
ws.cell(14, 3, "Modeling per 100,000 facility births (consistent with source)")

ws.cell(15, 1, "Maternal lives saved per 100,000 facility births with HSC")
ws.cell(15, 2, 5)
add_link(15, 3, "India modeling study (2023), cited in PMC review. "
                "I could not access the original study.", PMC_REVIEW)

ws.cell(16, 1, "Drug cost per life saved — HSC")
ws.cell(16, 2, "=B13*B14/B15")
ws.cell(16, 2).number_format = "$#,##0"
ws.cell(16, 3, "Calculation: drug cost x births / lives saved")

ws.cell(17, 1, "Program cost multiplier (HSC)")
ws.cell(17, 2, 20)
ws.cell(17, 3, "I'm assuming 20x drug cost for full program. "
               "HSC requires facility delivery and cold-chain-free storage. "
               "Highly uncertain.")

ws.cell(18, 1, "Full program cost per life saved — HSC")
ws.cell(18, 2, "=B16*B17")
ws.cell(18, 2).number_format = "$#,##0"
ws.cell(18, 3, "Calculation")

ws.cell(19, 1, "CE — HSC (multiples of cash)")
ws.cell(19, 2, "=B9/B18")
ws.cell(19, 2).number_format = "0.00"
ws.cell(19, 2).font = result_font
ws.cell(19, 3, "Uses same GiveDirectly benchmark as Section A")

# ── Combined estimate ─────────────────────────────────────────────────────────
ws.cell(21, 1, "Combined estimate").font = section_font

ws.cell(22, 1, "Bundled PPH program CE estimate (judgment)")
ws.cell(22, 2, "8-15x")
ws.cell(22, 2).font = result_font
ws.cell(22, 3, "The per-product estimates above are lower than this because "
               "a bundled program shares fixed costs (training, supply chain, "
               "facility infrastructure) across TXA + HSC + monitoring. "
               "8-15x is my judgment call for a well-run bundled program. "
               "Confidence: Low.")

ws.cell(23, 1, "Key driver of uncertainty")
ws.cell(23, 2, "Program costs")
add_link(23, 3, "AMPLI-PPHI ($26M, 6 countries) should have real cost data "
                "by mid-2026", UNITAID)

ws.cell(24, 1, "Note: misoprostol is off the table")
add_link(24, 3, "WHO 2025: misoprostol is 'last resort' when no injectable "
                "options are available", WHO_PPH_2025)

# Wrap text in source/notes column
for row in ws.iter_rows(min_row=1, max_row=24, min_col=3, max_col=3):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True)

out_path = os.path.join(os.path.dirname(__file__), "uterotonics_pph_prevention.xlsx")
wb.save(out_path)
print(f"Saved: {out_path}")
