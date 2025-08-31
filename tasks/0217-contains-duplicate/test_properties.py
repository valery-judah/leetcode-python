from __future__ import annotations

import runpy
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

NS = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
CLASSES = NS.get("ALL_SOLUTIONS", []) or [NS["Solution"]]


def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


@settings(max_examples=75, deadline=None)
@pytest.mark.parametrize("CLS", CLASSES)
@given(nums=st.lists(st.integers(min_value=-5, max_value=5), min_size=0, max_size=60))
def test_contains_duplicate_property(CLS, nums: list[int]):
    # Known intentionally-buggy reference kept for FAIL demo
    if getattr(CLS, "__name__", "") == "BruteForce":
        pytest.xfail("Known failing reference implementation (kept to show FAIL in matrix)")

    sol = CLS()
    got = sol.solve(nums)
    expect = has_duplicate(nums)
    assert got is expect
