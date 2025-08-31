from __future__ import annotations

import runpy
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from common.testutil import norm_subsets

NS = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
CLASSES = NS.get("ALL_SOLUTIONS", []) or [NS["Solution"]]


@settings(max_examples=60, deadline=None)
@pytest.mark.parametrize("CLS", CLASSES)
@given(nums=st.lists(st.integers(min_value=-6, max_value=6), min_size=0, max_size=8, unique=True))
def test_subsets_invariants(CLS, nums: list[int]):
    sol = CLS()
    out = sol.solve(nums)
    # Count check
    assert len(out) == (1 << len(nums))
    # Elements only from input
    allowed = set(nums)
    for subset in out:
        assert isinstance(subset, list)
        assert set(subset).issubset(allowed)
    # Uniqueness of subsets (order-insensitive)
    canon = {tuple(sorted(s)) for s in out}
    assert len(canon) == len(out)
    # Contains empty subset
    assert [] in out


@settings(max_examples=40, deadline=None)
@given(nums=st.lists(st.integers(min_value=-6, max_value=6), min_size=0, max_size=8, unique=True))
def test_subsets_equivalence_across_impls(nums: list[int]):
    # Compare all implementations' outputs for equality (order-insensitive)
    import runpy
    from pathlib import Path

    ns = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
    classes = ns.get("ALL_SOLUTIONS", []) or [ns["Solution"]]

    outs = []
    for cls in classes:
        out = cls().solve(nums)
        outs.append(norm_subsets(out))
    for o in outs[1:]:
        assert o == outs[0]


@settings(max_examples=50, deadline=None)
@pytest.mark.parametrize("CLS", CLASSES)
@given(
    nums=st.lists(st.integers(min_value=-6, max_value=6), min_size=0, max_size=8, unique=True),
    a=st.sampled_from([-1, 1]),
    b=st.integers(min_value=-5, max_value=5),
)
def test_subsets_metamorphic_affine(CLS, nums: list[int], a: int, b: int):
    """Applying an affine bijection x -> a*x + b to all elements maps
    each subset accordingly; normalized outputs are preserved.
    """
    sol = CLS()
    out = sol.solve(nums)

    def f(x: int) -> int:
        return a * x + b

    nums2 = [f(x) for x in nums]
    out2 = sol.solve(nums2)

    mapped = [[f(x) for x in subset] for subset in out]
    assert norm_subsets(mapped) == norm_subsets(out2)
