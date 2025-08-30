from __future__ import annotations

import runpy
from collections.abc import Callable
from pathlib import Path

import pytest
from _pytest.mark.structures import ParameterSet


def _discover_solution_classes() -> list[ParameterSet]:
    """Discover solution classes for this task from `solutions.py`.

    Supports two export styles:
    - `ALL_SOLUTIONS`: iterable of classes implementing `.solve(...)`
    - `Solution`: a single class implementing `.solve(...)`
    """
    base = Path(__file__).parent
    path = base / "solutions.py"
    if not path.exists():
        raise RuntimeError("Missing solutions.py in task folder")

    ns = runpy.run_path(str(path))
    params: list[ParameterSet] = []
    if "ALL_SOLUTIONS" in ns:
        for cls in ns["ALL_SOLUTIONS"]:
            if hasattr(cls, "solve"):
                params.append(pytest.param(cls, id=f"{path.stem}:{cls.__name__}"))
    elif "Solution" in ns:
        params.append(pytest.param(ns["Solution"], id=path.stem))

    if not params:
        raise RuntimeError("solutions.py must export ALL_SOLUTIONS or Solution")
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
