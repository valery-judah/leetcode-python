from __future__ import annotations

import runpy
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest


@dataclass(frozen=True)
class StubParam:
    task: str
    sol_name: str
    module_path: str
    exc: type[BaseException]
    label: str
    args: tuple[Any, ...]
    kwargs: dict[str, Any]


@dataclass(frozen=True)
class CaseParam:
    task: str
    sol_name: str
    module_path: str
    label: str
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    expected: Any


def _prefer_primary_class(ns: dict[str, Any]) -> Iterable[type]:
    """Yield the primary solution class to test.

    Preference order:
    1) `Solution` alias if present
    2) First class in `ALL_SOLUTIONS`
    """
    if "Solution" in ns and hasattr(ns["Solution"], "solve"):
        return [ns["Solution"]]
    classes = ns.get("ALL_SOLUTIONS") or []
    return classes[:1] if classes else []


def _is_exception_opt_in(ns: dict[str, Any]) -> type[BaseException] | None:
    exc = ns.get("TEST_EXPECT_EXCEPTION")
    try:
        if isinstance(exc, type) and issubclass(exc, BaseException):
            return exc
    except Exception:
        pass
    return None


def _parse_case_tuple(item: Any) -> tuple[str, tuple[Any, ...], dict[str, Any], Any] | None:
    """Supports two shapes:
    - (label, args_tuple, kwargs_dict, expected)
    - (label, arg1, ..., expected)
    Returns (label, args, kwargs, expected) or None if unsupported.
    """
    if not isinstance(item, tuple) or not item or not isinstance(item[0], str):
        return None
    # Shape 1
    if len(item) == 4 and isinstance(item[1], tuple) and isinstance(item[2], dict):
        label, args, kwargs, expected = item
        return label, args, kwargs, expected
    # Shape 2
    if len(item) >= 3:
        label = item[0]
        *mid, expected = item[1:]
        return label, tuple(mid), {}, expected
    return None


def _discover_stub_params() -> list[StubParam]:
    root = Path(__file__).parent
    params: list[StubParam] = []
    for task_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        sol_path = task_dir / "solutions.py"
        if not sol_path.exists():
            continue
        try:
            ns = runpy.run_path(str(sol_path))
        except Exception:
            continue

        exc = _is_exception_opt_in(ns)
        if not exc:
            continue

        classes = list(_prefer_primary_class(ns))
        if not classes:
            continue

        raw_cases = ns.get("TEST_CASES") or []
        cases: list[tuple[str, tuple[Any, ...], dict[str, Any]]] = []
        if isinstance(raw_cases, list):
            for item in raw_cases:
                if (
                    isinstance(item, tuple)
                    and len(item) == 3
                    and isinstance(item[0], str)
                    and isinstance(item[1], tuple)
                    and isinstance(item[2], dict)
                ):
                    cases.append((item[0], item[1], item[2]))
        if not cases:
            cases = [("default", tuple(), {})]

        for cls in classes:
            sol_name = getattr(cls, "__name__", "Solution")
            for label, args, kwargs in cases:
                params.append(
                    StubParam(
                        task=task_dir.name,
                        sol_name=sol_name,
                        module_path=str(sol_path),
                        exc=exc,
                        label=label,
                        args=args,
                        kwargs=kwargs,
                    )
                )
    return params


def _discover_case_params() -> list[CaseParam]:
    root = Path(__file__).parent
    params: list[CaseParam] = []
    for task_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        sol_path = task_dir / "solutions.py"
        if not sol_path.exists():
            continue
        try:
            ns = runpy.run_path(str(sol_path))
        except Exception:
            continue

        # Skip stub tasks
        if _is_exception_opt_in(ns):
            continue

        classes = list(_prefer_primary_class(ns))
        if not classes:
            continue

        raw_cases = ns.get("TEST_CASES")
        if not isinstance(raw_cases, list) or not raw_cases:
            continue

        for item in raw_cases:
            parsed = _parse_case_tuple(item)
            if not parsed:
                continue
            label, args, kwargs, expected = parsed
            sol_name = getattr(classes[0], "__name__", "Solution")
            params.append(
                CaseParam(
                    task=task_dir.name,
                    sol_name=sol_name,
                    module_path=str(sol_path),
                    label=label,
                    args=args,
                    kwargs=kwargs,
                    expected=expected,
                )
            )
    return params


def _normalize_generic(value: Any) -> Any:
    """Heuristic normalizer for common LeetCode outputs.

    - If value is a list of two ints, sort it (order-insensitive pair).
    - If value is list[list[Any]], sort inner lists and then sort outer list.
    Otherwise, return as-is.
    """
    try:
        if isinstance(value, list) and len(value) == 2 and all(isinstance(x, int) for x in value):
            return sorted(value)
    except Exception:
        pass

    if isinstance(value, list) and value and all(isinstance(x, list) for x in value):
        normalized_inner = [sorted(x) for x in value]
        try:
            return sorted(normalized_inner)
        except Exception:
            return sorted(normalized_inner, key=lambda x: str(x))
    return value


_STUB_PARAMS = _discover_stub_params()
_CASE_PARAMS = _discover_case_params()


@pytest.mark.parametrize(
    ("task", "sol_name", "module_path", "exc", "label", "args", "kwargs"),
    [(p.task, p.sol_name, p.module_path, p.exc, p.label, p.args, p.kwargs) for p in _STUB_PARAMS],
)
def test_stub_solutions_raise(
    task: str,
    sol_name: str,
    module_path: str,
    exc: type[BaseException],
    label: str,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    run_summary,
):
    ns = runpy.run_path(module_path)
    # Re-fetch the primary class by name
    classes = ns.get("ALL_SOLUTIONS") or [ns.get("Solution")]
    cls = next((c for c in classes if getattr(c, "__name__", "Solution") == sol_name), None)
    assert cls is not None, "Solution class disappeared during reload"

    ok = False
    try:
        with pytest.raises(exc):
            cls().solve(*args, **kwargs)
        ok = True
    finally:
        run_summary[sol_name].append((f"{task}:{label}", ok))
    assert ok


@pytest.mark.parametrize(
    ("task", "sol_name", "module_path", "label", "args", "kwargs", "expected"),
    [
        (p.task, p.sol_name, p.module_path, p.label, p.args, p.kwargs, p.expected)
        for p in _CASE_PARAMS
    ],
)
def test_default_cases(
    task: str,
    sol_name: str,
    module_path: str,
    label: str,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    expected: Any,
    run_summary,
):
    ns = runpy.run_path(module_path)
    classes = ns.get("ALL_SOLUTIONS") or [ns.get("Solution")]
    cls = next((c for c in classes if getattr(c, "__name__", "Solution") == sol_name), None)
    assert cls is not None, "Primary solution class not found"

    # Optional module-level normalizer hook
    normalizer = ns.get("TEST_NORMALIZE")
    if not callable(normalizer):
        normalizer = _normalize_generic

    sol = cls()
    out = sol.solve(*args, **kwargs)

    exp_norm = normalizer(expected)
    out_norm = normalizer(out)
    ok = out_norm == exp_norm
    run_summary[sol_name].append((f"{task}:{label}", ok))
    assert ok
