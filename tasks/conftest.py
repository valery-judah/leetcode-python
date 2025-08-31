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

    # Always render with solutions as columns, cases as rows
    rows: list[list[str]] = []
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

    for line in format_table(headers, rows):
        terminalreporter.write_line(line)

    # Coverage summary (scoped to requested paths) if pytest-cov is active
    try:
        pm = terminalreporter.config.pluginmanager
        cov_plugin = getattr(pm, "get_plugin", pm.getplugin)("cov")  # type: ignore[attr-defined]
    except Exception:
        cov_plugin = None

    if cov_plugin and hasattr(cov_plugin, "cov_controller"):
        try:
            cov = cov_plugin.cov_controller.cov  # type: ignore[attr-defined]
            data = cov.get_data()
            measured = list(data.measured_files())
            from pathlib import Path

            args = [str(a) for a in getattr(terminalreporter.config, "args", [])]
            targets = [Path(a).resolve() for a in args if Path(a).exists()]
            if not targets:
                targets = [Path(terminalreporter.config.rootdir)]  # type: ignore[arg-type]

            def in_scope(f: str) -> bool:
                p = Path(f).resolve()
                for t in targets:
                    try:
                        if p.is_relative_to(t):
                            return True
                    except Exception:
                        # Fallback for older Python; approximate using string startswith
                        if str(p).startswith(str(t)):
                            return True
                return False

            scoped = [f for f in measured if in_scope(f)]
            total_stmts = 0
            total_miss = 0
            for f in scoped:
                try:
                    _fname, statements, _excluded, missing, _ = cov.analysis2(f)
                    total_stmts += len(statements)
                    total_miss += len(missing)
                except Exception:
                    continue
            if total_stmts > 0:
                pct = 100.0 * (total_stmts - total_miss) / total_stmts
                color = GREEN if pct >= 90 else ("\x1b[33m" if pct >= 75 else RED)
                RESETC = RESET
                terminalreporter.write_line("")
                terminalreporter.write_line(
                    f"Coverage (scoped): {color}{pct:.1f}%{RESETC} "
                    f"({total_stmts - total_miss}/{total_stmts} lines)"
                )
        except Exception:
            pass

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
