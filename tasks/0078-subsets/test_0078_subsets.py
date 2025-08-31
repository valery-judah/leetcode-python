from __future__ import annotations

import pytest

from common.testutil import (
    SUBSETS_COUNT_CASES,
    S_fixture_for_this_dir,
    cases_from_solutions,
    norm_subsets,
)

# Shared discovery fixture and normalization helper
S = S_fixture_for_this_dir(__file__)
norm = norm_subsets


@pytest.mark.parametrize(("label", "nums", "expected"), cases_from_solutions(__file__, "TEST_CASES"))
def test_subsets_small(S, label: str, nums: list[int], expected: list[list[int]], run_summary):
    sol = S()
    got = sol.solve(nums)
    ok = norm(got) == norm(expected)
    run_summary[S.__name__].append((label, ok))
    assert ok


@pytest.mark.parametrize(("label", "nums"), SUBSETS_COUNT_CASES)
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

