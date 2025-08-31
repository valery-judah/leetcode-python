from __future__ import annotations

import runpy
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

NS = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
CLASSES = NS.get("ALL_SOLUTIONS", []) or [NS["Solution"]]


def _normalize_pair(res: list[int]) -> tuple[int, int] | None:
    if not isinstance(res, list) or len(res) != 2:
        return None
    i, j = res
    return (i, j) if i <= j else (j, i)


@settings(max_examples=60, deadline=None)
@pytest.mark.parametrize("CLS", CLASSES)
@given(
    nums=st.lists(st.integers(min_value=-50, max_value=50), min_size=0, max_size=40),
    target=st.integers(min_value=-100, max_value=100),
    c=st.integers(min_value=-10, max_value=10),
)
def test_add_constant_preserves_solution(CLS, nums: list[int], target: int, c: int):
    sol = CLS()
    base = sol.solve(nums, target)
    shifted_nums = [x + c for x in nums]
    shifted_target = target + 2 * c
    shifted = sol.solve(shifted_nums, shifted_target)

    base_pair = _normalize_pair(base)
    shifted_pair = _normalize_pair(shifted)

    if base_pair is None:
        assert shifted_pair is None
    else:
        assert shifted_pair is not None
        assert shifted_pair == base_pair


@settings(max_examples=60, deadline=None)
@pytest.mark.parametrize("CLS", CLASSES)
@given(
    nums=st.lists(st.integers(min_value=-30, max_value=30), min_size=0, max_size=35),
    target=st.integers(min_value=-60, max_value=60),
    s=st.integers(min_value=-5, max_value=5).filter(lambda k: k not in (0,)),
)
def test_scale_constant_preserves_solution(CLS, nums: list[int], target: int, s: int):
    sol = CLS()
    base = sol.solve(nums, target)
    scaled_nums = [x * s for x in nums]
    scaled_target = target * s
    scaled = sol.solve(scaled_nums, scaled_target)

    base_pair = _normalize_pair(base)
    scaled_pair = _normalize_pair(scaled)

    if base_pair is None:
        assert scaled_pair is None
    else:
        assert scaled_pair is not None
        assert scaled_pair == base_pair
