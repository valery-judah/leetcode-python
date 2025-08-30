from __future__ import annotations

import runpy
from pathlib import Path

import pytest
from _pytest.mark.structures import ParameterSet


def _discover_solution_classes() -> list[ParameterSet]:
    base = Path(__file__).parent
    path = base / "solutions.py"
    ns = runpy.run_path(str(path))
    params: list[ParameterSet] = []
    if "ALL_SOLUTIONS" in ns:
        for cls in ns["ALL_SOLUTIONS"]:
            if hasattr(cls, "solve"):
                params.append(pytest.param(cls, id=cls.__name__))
    elif "Solution" in ns:
        params.append(pytest.param(ns["Solution"], id="Solution"))
    if not params:
        raise RuntimeError("solutions.py must export ALL_SOLUTIONS or Solution")
    return params


@pytest.fixture(params=_discover_solution_classes())
def S(request):
    """Parametrized factory yielding each solution class."""
    return request.param

# Helpers to compare subsets regardless of order
def norm(subsets: list[list[int]]) -> list[list[int]]:
    return sorted([sorted(x) for x in subsets])


@pytest.mark.parametrize(
    ("label", "nums", "expected"),
    [
        (
            "example_1",
            [1, 2, 3],
            [
                [],
                [1], [2], [3],
                [1, 2], [1, 3], [2, 3],
                [1, 2, 3],
            ],
        ),
        ("empty", [], [[]]),
        ("single", [0], [[], [0]]),
        ("two", [1, 2], [[], [1], [2], [1, 2]]),
        (
            "unsorted",
            [3, 1, 2],
            [
                [],
                [1], [2], [3],
                [1, 2], [1, 3], [2, 3],
                [1, 2, 3],
            ],
        ),
        (
            "negatives",
            [-1, 0, 1],
            [
                [],
                [-1], [0], [1],
                [-1, 0], [-1, 1], [0, 1],
                [-1, 0, 1],
            ],
        ),
    ],
)
def test_subsets_small(S, label: str, nums: list[int], expected: list[list[int]], run_summary):
    sol = S()
    got = sol.solve(nums)
    ok = norm(got) == norm(expected)
    run_summary[S.__name__].append((label, ok))
    assert ok


@pytest.mark.parametrize("label, nums", [("n4_count", [0, 1, 2, 3]), ("n10_count", list(range(10)))])
def test_counts_and_uniqueness(S, label: str, nums: list[int], run_summary):
    sol = S()
    got = sol.solve(nums)
    # Count check
    ok_count = len(got) == (1 << len(nums))
    # Uniqueness check (ignore order within subsets)
    as_set = {tuple(sorted(x)) for x in got}
    ok_unique = len(as_set) == (1 << len(nums))
    ok = ok_count and ok_unique and [] in got
    run_summary[S.__name__].append((label, ok))
    assert ok
