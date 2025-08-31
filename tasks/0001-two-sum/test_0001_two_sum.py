import pytest

from common.testutil import S_fixture_for_this_dir, cases_from_solutions

# Primary solution class (first in ALL_SOLUTIONS)
S = S_fixture_for_this_dir(__file__)


@pytest.mark.parametrize(
    ("label", "nums", "target", "expected"),
    cases_from_solutions(__file__, "TEST_CASES"),
)
def test_solve(S, label: str, nums: list[int], target: int, expected: list[int], run_summary):
    """Validates two-sum against canonical examples from solutions.py.

    The problem allows returning indices in any order, so we compare sorted
    indices.
    """
    solution = S()
    result = solution.solve(nums, target)
    ok = isinstance(result, list) and len(result) == 2 and sorted(result) == sorted(expected)
    run_summary[S.__name__].append((label, ok))
    assert ok
