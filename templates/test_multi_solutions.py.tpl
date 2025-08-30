from __future__ import annotations

import runpy
from pathlib import Path
from typing import Callable, Type

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

    # Prefer consolidated file in the task folder
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

    # Fallback to legacy directory
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
            cls: Type = ns["Solution"]
            params.append(pytest.param(cls, id=path.stem))

    if not params:
        raise RuntimeError("No solutions found: add solutions.py, variants.py, or solutions/*.py")
    return params


@pytest.fixture(params=_discover_solution_classes())
def S(request) -> Callable[[], object]:
    """Parametrized factory for each solution variant."""
    cls: Type = request.param
    return cls


# TODO: replace with true signature and cases
@pytest.mark.parametrize(
    "args, kwargs",
    [
        ((), {{}}),  # replace with concrete inputs
    ],
)
def test_example_raises_not_implemented(S, args, kwargs):
    """Template test that expects NotImplementedError until implemented."""
    with pytest.raises(NotImplementedError):
        S() .solve(*args, **kwargs)
