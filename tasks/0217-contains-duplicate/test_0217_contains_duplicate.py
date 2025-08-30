from __future__ import annotations

import runpy
from collections.abc import Callable
from pathlib import Path

import pytest
from _pytest.mark.structures import ParameterSet

# Aggregate results per solution for a verbose, grouped summary
# Summary recording provided by this package's conftest.py via `run_summary` fixture


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
    ("label", "nums", "expected"),
    [
        ("dupe_simple", [1, 2, 3, 1], True),
        ("no_dupe", [1, 2, 3, 4], False),
        ("multi_dupes", [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ("empty", [], False),
        ("single", [5], False),
        ("zeros", [0, 0], True),
        ("negatives", [-1, -2, -1], True),
    ],
)
def test_contains_duplicate(S, label: str, nums: list[int], expected: bool, run_summary):
    sol = S()
    ok = sol.solve(nums) is expected
    # Record per-solution outcome for verbose grouped reporting
    run_summary[S.__name__].append((label, ok))
    assert ok
