from __future__ import annotations

import re

# Basic ANSI codes
RED = "\x1b[31m"
GREEN = "\x1b[32m"
BOLD = "\x1b[1m"
RESET = "\x1b[0m"

# Regex to strip ANSI codes when measuring widths
_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def vis_len(s: str) -> int:
    """Visible length of a string (ANSI codes stripped)."""
    return len(_ANSI_RE.sub("", s))


def ljust_ansi(s: str, width: int) -> str:
    """Left-justify accounting for ANSI codes so columns align."""
    visible = vis_len(s)
    if visible >= width:
        return s
    return s + (" " * (width - visible))


def format_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    """Render a pipe-separated table aligned even with ANSI colors.

    Returns a list of lines ready to print.
    """
    col_widths = [vis_len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], vis_len(cell))
            else:
                col_widths.append(vis_len(cell))

    def fmt_row(cells: list[str]) -> str:
        parts = [ljust_ansi(cells[i], col_widths[i]) for i in range(len(col_widths))]
        return " | ".join(parts)

    sep = "-+-".join("-" * w for w in col_widths)
    out = [fmt_row(headers), sep]
    for r in rows:
        out.append(fmt_row(r))
    return out

