from __future__ import annotations

import runpy
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

NS = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
CLS = (NS.get("ALL_SOLUTIONS", []) or [NS["Solution"]])[0]


def exists_nearby_duplicate(nums: list[int], k: int) -> bool:
    last = {}
    for i, v in enumerate(nums):
        if v in last and i - last[v] <= k:
            return True
        last[v] = i
    return False


@settings(max_examples=80, deadline=None)
@given(
    nums=st.lists(st.integers(min_value=-6, max_value=6), min_size=0, max_size=60),
    k=st.integers(min_value=0, max_value=60),
)
def test_nearby_duplicate_property(nums: list[int], k: int):
    sol = CLS()
    got = sol.solve(nums, k)
    expect = exists_nearby_duplicate(nums, k)
    assert got is expect
