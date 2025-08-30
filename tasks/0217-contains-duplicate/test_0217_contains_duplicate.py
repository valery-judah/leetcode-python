from __future__ import annotations

import runpy
from collections.abc import Callable
from pathlib import Path

import pytest
from _pytest.mark.structures import ParameterSet


def _discover_solution_classes() -> list[ParameterSet]:
    """Discover solution classes for this task.

    Priority order:
    1) A consolidated `solutions.py` file in the task folder
    2) A consolidated `variants.py` file in the task folder
    3) Any modules under a `solutions/` folder (legacy layout)

    Each module supports two export styles:
    - `ALL_SOLUTIONS`: iterable of classes implementing `.solve(...)`
    - `Solution`: a single class implementing `.solve(...)`
    """
    base = Path(__file__).parent
    params: list[ParameterSet] = []

    # 1) Prefer consolidated file `solutions.py`
    for fname in ("solutions.py", "variants.py"):
        path = base / fname
        if not path.exists():
            continue
        ns = runpy.run_path(str(path))
        if "ALL_SOLUTIONS" in ns:
            for cls in ns["ALL_SOLUTIONS"]:
                if hasattr(cls, "solve"):
                    params.append(pytest.param(cls, id=f"{path.stem}:{cls.__name__}"))
            if params:
                return params
        if "Solution" in ns:
            params.append(pytest.param(ns["Solution"], id=path.stem))
            return params

    # 2) Fallback to legacy `solutions/` directory with one class per file
    sols_dir = base / "solutions"
    for path in sorted(sols_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        ns = runpy.run_path(str(path))
        if "ALL_SOLUTIONS" in ns:
            for cls in ns["ALL_SOLUTIONS"]:
                if hasattr(cls, "solve"):
                    params.append(pytest.param(cls, id=f"{path.stem}:{cls.__name__}"))
            continue
        if "Solution" in ns:
            cls: type = ns["Solution"]
            params.append(pytest.param(cls, id=path.stem))

    if not params:
        raise RuntimeError("No solutions found: add solutions.py, variants.py, or solutions/*.py")
    return params


@pytest.fixture(params=_discover_solution_classes())
def S(request) -> Callable[[], object]:
    """Parametrized factory for each solution variant."""
    cls: type = request.param
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
