from __future__ import annotations

import runpy
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
from _pytest.mark.structures import ParameterSet


def discover_solution_classes(test_file: str | Path) -> list[ParameterSet]:
    """Discover solution classes from a `solutions.py` next to the given test file.

    Supports two export styles:
    - `ALL_SOLUTIONS`: iterable of classes implementing `.solve(...)`
    - `Solution`: a single class implementing `.solve(...)`
    Returns a list of pytest `ParameterSet`s for use with `params=`.
    """
    p = Path(test_file)
    path = p.with_name("solutions.py")
    if not path.exists():
        raise RuntimeError(f"Missing solutions.py next to {p}")
    ns = runpy.run_path(str(path))
    params: list[ParameterSet] = []
    if "ALL_SOLUTIONS" in ns:
        for cls in ns["ALL_SOLUTIONS"]:
            if hasattr(cls, "solve"):
                params.append(pytest.param(cls, id=getattr(cls, "__name__", "Solution")))
    elif "Solution" in ns:
        params.append(pytest.param(ns["Solution"], id="Solution"))
    if not params:
        raise RuntimeError("solutions.py must export ALL_SOLUTIONS or Solution")
    return params


def S_fixture_for_this_dir(test_file: str | Path) -> Callable:
    """Create a parametrized fixture named `S` for the current test file's folder."""
    params = discover_solution_classes(test_file)

    @pytest.fixture(params=params)
    def _S(request):  # type: ignore[no-redef]
        return request.param

    return _S


def norm_subsets(subsets: list[list[int]]) -> list[list[int]]:
    """Normalize a list of subsets for order-insensitive comparison."""
    return sorted([sorted(x) for x in subsets])


def cases_from_solutions(test_file: str | Path, name: str = "TEST_CASES") -> list[Any]:
    """Load a list of parametrize cases from the sibling solutions.py.

    The solutions.py next to `test_file` should define a variable with the
    given name (default 'TEST_CASES'). This function returns it as-is, so it
    can be fed into pytest.mark.parametrize.
    """
    p = Path(test_file)
    path = p.with_name("solutions.py")
    if not path.exists():
        raise RuntimeError(f"Missing solutions.py next to {p}")
    ns = runpy.run_path(str(path))
    if name not in ns:
        raise RuntimeError(f"{path.name} must define {name}")
    cases = ns[name]
    if not isinstance(cases, list):  # basic sanity check
        raise RuntimeError(f"{name} in {path.name} must be a list")
    return cases


# Common property-based cases for subsets (LeetCode 78)
# Default sizes focus on sanity/performance balance.
SUBSETS_COUNT_CASES: list[tuple[str, list[int]]] = [
    ("n4_count", [0, 1, 2, 3]),
    ("n10_count", list(range(10))),
]


def subset_count_cases(*sizes: int) -> list[tuple[str, list[int]]]:
    """Generate (label, nums) cases for subset count/uniqueness checks.

    Example: subset_count_cases(4, 10) -> [
      ("n4_count", [0,1,2,3]), ("n10_count", list(range(10)))
    ]
    """
    if not sizes:
        sizes = (4, 10)
    out: list[tuple[str, list[int]]] = []
    for n in sizes:
        out.append((f"n{n}_count", list(range(n))))
    return out
