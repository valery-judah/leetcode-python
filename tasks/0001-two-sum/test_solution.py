import runpy
from pathlib import Path

import pytest


def _load_solution_cls():
    ns = runpy.run_path(str(Path(__file__).with_name("solution.py")))
    return ns["Solution"]


@pytest.fixture
def solution():
    """Provides a Solution instance for each test case without importing the module."""
    return _load_solution_cls()()


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        # Base case from the problem description
        ([2, 7, 11, 15], 9, [0, 1]),
        # Case where the solution is not the first two elements
        ([3, 2, 4], 6, [1, 2]),
        # Case with duplicate numbers
        ([3, 3], 6, [0, 1]),
        # Case with negative numbers
        ([-10, 7, 19, 15], 9, [0, 2]),
        # Case with zero
        ([0, 4, 3, 0], 0, [0, 3]),
    ],
)
def test_solve(solution, nums: list[int], target: int, expected: list[int]):
    """
    Tests the solve method with various inputs.

    The problem statement allows returning indices in any order, so we sort
    both the result and the expected list to ensure the comparison is
    order-independent.
    """
    result = solution.solve(nums, target)
    assert isinstance(result, list)
    assert len(result) == 2
    assert sorted(result) == sorted(expected)
