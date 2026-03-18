"""Shared helper: export an openpyxl worksheet to a flat CSV (A/B/C columns).

Usage (at the end of any build_*.py script):
    from export_csv import save_csv
    save_csv(ws, out_path.replace(".xlsx", ".csv"))
"""

import csv


def save_csv(ws, csv_path):
    """Write worksheet columns A-C to a CSV file.

    - Column A: Parameter label
    - Column B: Value (number, formula string, or blank)
    - Column C: Source / notes (text only; comments and hyperlinks are omitted)
    """
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Parameter", "Value", "Source / notes"])
        for row in ws.iter_rows(min_row=1, max_col=3, values_only=False):
            vals = []
            for cell in row:
                v = cell.value
                if v is None:
                    vals.append("")
                else:
                    vals.append(str(v))
            # Skip completely empty rows
            if all(v == "" for v in vals):
                continue
            writer.writerow(vals)
    print(f"Saved: {csv_path}")
