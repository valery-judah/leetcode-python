from __future__ import annotations

import runpy
from pathlib import Path
from typing import Callable, Type

import pytest
from _pytest.mark.structures import ParameterSet


def _discover_solution_classes() -> list[ParameterSet]:
    """Discover solution classes from `solutions.py`.

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
