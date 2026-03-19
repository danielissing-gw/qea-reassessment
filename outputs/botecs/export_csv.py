"""Shared helper: export an openpyxl worksheet to a flat CSV (A/B/C columns).

Values in column B are evaluated (formulas resolved to numbers) so that the
CSV is human-readable on GitHub without needing Excel.

Usage (at the end of any build_*.py script):
    from export_csv import save_csv
    save_csv(ws, out_path.replace(".xlsx", ".csv"))
"""

import csv
import re


def _evaluate(ws):
    """Resolve column-B formulas to numeric values.

    Handles simple Excel formulas that reference other B-column cells
    (e.g. =B2/B7, =B8*B11*B13, =1-B12, =(B2/$8)*B10/B2/B22).
    Returns a dict mapping row number -> resolved float value.
    """
    resolved = {}

    # First pass: collect literal numeric values
    for row in ws.iter_rows(min_row=1, max_col=2, values_only=False):
        cell = row[1]  # column B
        v = cell.value
        if v is None:
            continue
        if isinstance(v, (int, float)):
            resolved[cell.row] = float(v)

    # Second pass: iteratively resolve formulas (may need multiple passes
    # for chains like B5 depends on B3-B4, B7 depends on B5+B6, etc.)
    max_iterations = 10
    for _ in range(max_iterations):
        progress = False
        for row in ws.iter_rows(min_row=1, max_col=2, values_only=False):
            cell = row[1]
            v = cell.value
            if v is None or cell.row in resolved:
                continue
            if not isinstance(v, str) or not v.startswith("="):
                continue

            expr = v[1:]  # strip leading =

            # Replace cell references (e.g. B12, $B$12, B$12, $B12) with
            # resolved values
            def _sub(m):
                ref_row = int(m.group(1))
                if ref_row in resolved:
                    return repr(resolved[ref_row])
                raise KeyError(ref_row)

            try:
                # Match B-column references like B12, $B12, B$12, $B$12
                numeric_expr = re.sub(
                    r'\$?B\$?(\d+)', _sub, expr
                )
                # Remove stray $ signs (Excel literal dollar amounts like $8)
                numeric_expr = re.sub(r'\$(\d)', r'\1', numeric_expr)
                # Evaluate the arithmetic expression safely
                result = eval(numeric_expr, {"__builtins__": {}}, {})  # noqa: S307
                resolved[cell.row] = float(result)
                progress = True
            except (KeyError, Exception):
                continue

        if not progress:
            break

    return resolved


def _fmt(value, cell):
    """Format a resolved numeric value using the cell's number_format."""
    fmt = cell.number_format or "General"

    if fmt in ("General", "@"):
        # For general format, show reasonable precision
        if value == int(value) and abs(value) >= 1:
            return str(int(value))
        return f"{value:.4g}"
    if "%" in fmt:
        return f"{value:.0%}"
    if fmt == "$#,##0":
        return f"${value:,.0f}"
    if "$#,##0.00" in fmt:
        return f"${value:,.2f}"
    if fmt == "#,##0":
        return f"{value:,.0f}"
    if "0.0" in fmt and "0.00" not in fmt:
        return f"{value:.1f}"
    if "0.00" in fmt:
        return f"{value:.2f}"
    if "0.000" in fmt:
        return f"{value:.3f}"
    # Fallback
    if value == int(value) and abs(value) >= 1:
        return str(int(value))
    return f"{value:.4g}"


def save_csv(ws, csv_path):
    """Write worksheet columns A-C to a CSV file.

    - Column A: Parameter label
    - Column B: Value (formulas resolved to computed numbers)
    - Column C: Source / notes (text only; comments and hyperlinks are omitted)
    """
    resolved = _evaluate(ws)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Parameter", "Value", "Source / notes"])
        for row in ws.iter_rows(min_row=1, max_col=3, values_only=False):
            a_cell, b_cell, c_cell = row[0], row[1], row[2]

            a_val = str(a_cell.value) if a_cell.value is not None else ""

            # Column B: use resolved value if available, else raw value
            if b_cell.row in resolved:
                b_val = _fmt(resolved[b_cell.row], b_cell)
            elif b_cell.value is not None:
                b_val = str(b_cell.value)
            else:
                b_val = ""

            c_val = str(c_cell.value) if c_cell.value is not None else ""

            # Skip completely empty rows
            if all(v == "" for v in (a_val, b_val, c_val)):
                continue
            writer.writerow([a_val, b_val, c_val])
    print(f"Saved: {csv_path}")
