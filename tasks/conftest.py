from __future__ import annotations

from collections import defaultdict

import pytest

from common.ansi import BOLD, GREEN, RED, RESET, format_table

# Shared summary across tests (opt-in via `run_summary` fixture)
_RUN_SUMMARY: dict[str, list[tuple[str, bool]]] = defaultdict(list)


@pytest.fixture(scope="session")
def run_summary() -> dict[str, list[tuple[str, bool]]]:
    """Session-scoped aggregator mapping solution name -> list of (case_label, pass?).

    Tests can append to this to participate in the matrix summary.
    """
    return _RUN_SUMMARY


def pytest_terminal_summary(terminalreporter):  # type: ignore[no-untyped-def]
    if not _RUN_SUMMARY:
        return

    solutions = sorted(_RUN_SUMMARY.keys())

    # Preserve first-seen order of case labels across solutions
    labels: list[str] = []
    seen = set()
    by_label: dict[str, dict[str, bool]] = {}
    for sol in solutions:
        mapping = {label: ok for label, ok in _RUN_SUMMARY[sol]}
        by_label[sol] = mapping
        for label in _RUN_SUMMARY[sol]:
            lab = label[0]
            if lab not in seen:
                seen.add(lab)
                labels.append(lab)

    terminalreporter.write_line("")
    terminalreporter.write_line("=== Results Matrix ===")

    use_solutions_as_columns = len(solutions) <= 4
    rows: list[list[str]] = []
    if use_solutions_as_columns:
        headers = ["Case"] + solutions
        for lab in labels:
            row = [lab]
            for sol in solutions:
                ok = by_label.get(sol, {}).get(lab)
                if ok is True:
                    row.append(f"{GREEN}PASS{RESET}")
                elif ok is False:
                    row.append(f"{RED}FAIL{RESET}")
                else:
                    row.append("-")
            rows.append(row)
    else:
        headers = ["Solution"] + labels
        for sol in solutions:
            row = [sol]
            for lab in labels:
                ok = by_label.get(sol, {}).get(lab)
                if ok is True:
                    row.append(f"{GREEN}PASS{RESET}")
                elif ok is False:
                    row.append(f"{RED}FAIL{RESET}")
                else:
                    row.append("-")
            rows.append(row)

    for line in format_table(headers, rows):
        terminalreporter.write_line(line)

    failing = {
        sol: [lab for lab, ok in _RUN_SUMMARY[sol] if not ok]
        for sol in solutions
        if any(not ok for _, ok in _RUN_SUMMARY[sol])
    }
    if failing:
        terminalreporter.write_line("")
        terminalreporter.write_line(f"{BOLD}{RED}Failing solutions details:{RESET}")
        for sol in solutions:
            if sol in failing:
                labs = ", ".join(failing[sol])
                total = len(_RUN_SUMMARY[sol])
                bad = len(failing[sol])
                terminalreporter.write_line(
                    f"- {RED}{sol}{RESET}:{BOLD}{RED}{bad}/{total} failed{RESET} -> {labs}"
                )

