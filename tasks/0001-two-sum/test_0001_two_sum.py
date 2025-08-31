import runpy
from pathlib import Path

import pytest


def _load_solution_cls():
    ns = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
    # Prefer ALL_SOLUTIONS if present, otherwise single Solution class
    if "ALL_SOLUTIONS" in ns:
        # Use the first as default for this single-solution style test
        return ns["ALL_SOLUTIONS"][0]
    return ns["Solution"]


@pytest.fixture
def solution():
    """Provides a Solution instance for each test case without importing the module."""
    return _load_solution_cls()()


@pytest.mark.parametrize(
    ("label", "nums", "target", "expected"),
    [
        ("base", [2, 7, 11, 15], 9, [0, 1]),
        ("mid", [3, 2, 4], 6, [1, 2]),
        ("dupes", [3, 3], 6, [0, 1]),
        ("negative", [-10, 7, 19, 15], 9, [0, 2]),
        ("zero", [0, 4, 3, 0], 0, [0, 3]),
    ],
)
def test_solve(solution, label: str, nums: list[int], target: int, expected: list[int], run_summary):
    """
    Tests the solve method with various inputs.

    The problem statement allows returning indices in any order, so we sort
    both the result and the expected list to ensure the comparison is
    order-independent.
    """
    result = solution.solve(nums, target)
    ok = isinstance(result, list) and len(result) == 2 and sorted(result) == sorted(expected)
    run_summary[solution.__class__.__name__].append((label, ok))
    assert ok

