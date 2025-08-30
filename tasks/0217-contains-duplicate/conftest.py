from __future__ import annotations

from collections import defaultdict

import pytest

# Shared summary across tests in this task folder
_RUN_SUMMARY: dict[str, list[tuple[str, bool]]] = defaultdict(list)


@pytest.fixture(scope="session")
def run_summary() -> dict[str, list[tuple[str, bool]]]:
    return _RUN_SUMMARY


def pytest_terminal_summary(terminalreporter):  # type: ignore[no-untyped-def]
    if not _RUN_SUMMARY:
        return
    terminalreporter.write_line("")
    terminalreporter.write_line("=== 0217: Contains Duplicate — Results by Solution ===")
    for sol_name, entries in _RUN_SUMMARY.items():
        passed = sum(1 for _, ok in entries if ok)
        total = len(entries)
        terminalreporter.write_line(f"- {sol_name}: {passed}/{total} passed")
        for label, ok in entries:
            status = "PASS" if ok else "FAIL"
            terminalreporter.write_line(f"  • {label}: {status}")

