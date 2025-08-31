from __future__ import annotations

import runpy
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

NS = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
CLASSES = NS.get("ALL_SOLUTIONS", []) or [NS["Solution"]]


def _pair_exists(nums: list[int], target: int) -> bool:
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False


@settings(max_examples=60, deadline=None)
@given(
    nums=st.lists(st.integers(min_value=-50, max_value=50), min_size=0, max_size=40),
    target=st.integers(min_value=-100, max_value=100),
)
def test_equivalence_across_implementations(nums: list[int], target: int):
    if len(CLASSES) < 2:
        pytest.skip("Equivalence fuzz requires at least two implementations in ALL_SOLUTIONS")

    decisions: list[bool] = []
    for cls in CLASSES:
        out = cls().solve(nums, target)
        # Normalize to decision: found pair or not
        has = bool(out)
        decisions.append(has)
        if has:
            assert isinstance(out, list)
            assert len(out) == 2
            i, j = out
            assert i != j
            assert 0 <= i < len(nums)
            assert 0 <= j < len(nums)
            assert nums[i] + nums[j] == target
        else:
            # If all claim no pair exists, ensure the oracle agrees
            pass

    # All implementations should agree on existence of a solution
    assert len(set(decisions)) == 1
    # And their shared decision should match the oracle
    assert decisions[0] is _pair_exists(nums, target)
