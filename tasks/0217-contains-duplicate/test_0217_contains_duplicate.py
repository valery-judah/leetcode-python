from __future__ import annotations

import runpy
from pathlib import Path
from typing import Callable, Type
from _pytest.mark.structures import ParameterSet

import pytest


def _discover_solution_classes() -> list[ParameterSet]:
    """Load each `solutions/*.py` and return its exported `Solution` class.

    Each param is labeled by filename stem, e.g., `set_based`, `sorting`.
    """
    sols_dir = Path(__file__).with_name("solutions")
    params: list = []
    for path in sorted(sols_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        ns = runpy.run_path(str(path))
        if "Solution" not in ns:
            continue
        cls: Type = ns["Solution"]
        params.append(pytest.param(cls, id=path.stem))
    if not params:
        raise RuntimeError("No solutions found in solutions/*.py")
    return params


@pytest.fixture(params=_discover_solution_classes())
def S(request) -> Callable[[], object]:
    """Parametrized factory for each solution variant."""
    cls: Type = request.param
    return cls


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([5], False),
        ([0, 0], True),
        ([-1, -2, -1], True),
    ],
)
def test_contains_duplicate(S, nums: list[int], expected: bool):
    sol = S()
    assert sol.solve(nums) is expected
