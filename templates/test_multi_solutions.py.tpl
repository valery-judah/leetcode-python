from __future__ import annotations

import runpy
from pathlib import Path
from typing import Callable, Type

import pytest
from _pytest.mark.structures import ParameterSet


def _discover_solution_classes() -> list[ParameterSet]:
    """Load each `solutions/*.py` and return its exported `Solution` class.

    Each param is labeled by filename stem, e.g., `set_based`, `sorting`.
    """
    sols_dir = Path(__file__).with_name("solutions")
    params: list[ParameterSet] = []
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
