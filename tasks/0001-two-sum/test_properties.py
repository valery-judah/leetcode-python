from __future__ import annotations

import runpy
from pathlib import Path

from hypothesis import Verbosity, event, given, settings
from hypothesis import strategies as st


def _pair_exists(nums: list[int], target: int) -> bool:
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False


NS = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
CLS = (NS.get("ALL_SOLUTIONS", []) or [NS["Solution"]])[0]


@settings(max_examples=75, deadline=None, verbosity=Verbosity.normal)
@given(
    nums=st.lists(st.integers(min_value=-50, max_value=50), min_size=0, max_size=40),
    target=st.integers(min_value=-100, max_value=100),
)
def test_two_sum_property(nums: list[int], target: int):
    sol = CLS()
    out = sol.solve(nums, target)

    # Record distribution metrics for Hypothesis statistics
    event(f"len={len(nums):02d}")
    event("pair_exists=yes" if _pair_exists(nums, target) else "pair_exists=no")

    if _pair_exists(nums, target):
        assert isinstance(out, list)
        assert len(out) == 2
        i, j = out
        assert isinstance(i, int)
        assert isinstance(j, int)
        assert 0 <= i < len(nums)
        assert 0 <= j < len(nums)
        assert i != j
        assert nums[i] + nums[j] == target
    else:
        # When no pair exists, solution returns empty list
        assert out == []
