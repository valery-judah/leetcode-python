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
    ("label", "nums", "k", "expected"),
    [
        ("basic_true", [1, 2, 3, 1], 3, True),
        ("adjacent_dup", [1, 0, 1, 1], 1, True),
        ("too_far", [1, 2, 3, 1, 2, 3], 2, False),
        ("empty", [], 1, False),
        ("single", [1], 1, False),
        ("k_zero", [1, 2, 1], 0, False),
        ("within_k", [99, 1, 99], 2, True),
        ("negatives", [-1, -2, -3, -1], 3, True),
        ("boundary_eq", [1, 2, 3, 1, 2, 3], 3, True),
        ("no_local_dup", [1, 2, 3, 1, 2, 3], 1, False),
        ("exact_k2", [1, 2, 1], 2, True),
        ("large_k", [1, 2, 3, 1], 100, True),
    ],
)
def test_contains_nearby_duplicate(
    S, label: str, nums: list[int], k: int, expected: bool, run_summary
):
    sol = S()
    ok = sol.solve(nums, k) is expected
    run_summary[S.__name__].append((label, ok))
    assert ok
