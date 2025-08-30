from __future__ import annotations

import runpy
from collections.abc import Callable
from pathlib import Path

import pytest
from _pytest.mark.structures import ParameterSet


def _discover_solution_classes() -> list[ParameterSet]:
    """Load each `solutions/*.py` and return its exported `Solution` class.

    Each param is labeled by filename stem, e.g., `hash_index`, `sliding_window`.
    """
    sols_dir = Path(__file__).with_name("solutions")
    params: list[ParameterSet] = []
    for path in sorted(sols_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        ns = runpy.run_path(str(path))
        if "Solution" not in ns:
            continue
        cls: type = ns["Solution"]
        params.append(pytest.param(cls, id=path.stem))
    if not params:
        raise RuntimeError("No solutions found in solutions/*.py")
    return params


@pytest.fixture(params=_discover_solution_classes())
def S(request) -> Callable[[], object]:
    """Parametrized factory for each solution variant."""
    cls: type = request.param
    return cls


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 2, 3, 1], 3, True),  # basic true
        ([1, 0, 1, 1], 1, True),  # adjacent duplicate
        ([1, 2, 3, 1, 2, 3], 2, False),  # too far
        ([], 1, False),  # empty
        ([1], 1, False),  # single element
        ([1, 2, 1], 0, False),  # k=0 cannot match
        ([99, 1, 99], 2, True),  # exactly within k
        ([-1, -2, -3, -1], 3, True),  # negatives
        ([1, 2, 3, 1, 2, 3], 3, True),  # boundary equal to k
        ([1, 2, 3, 1, 2, 3], 1, False),  # no local dup within k
        ([1, 2, 1], 2, True),  # distance exactly 2
        ([1, 2, 3, 1], 100, True),  # large k
    ],
)
def test_contains_nearby_duplicate(S, nums: list[int], k: int, expected: bool):
    sol = S()
    assert sol.solve(nums, k) is expected
