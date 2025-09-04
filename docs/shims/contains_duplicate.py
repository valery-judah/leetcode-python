from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

"""Shim for problems/0217-contains-duplicate/solutions.py.

This module dynamically loads the problem's solutions module so mkdocstrings can
document the classes even though the problem folder name is not a valid module
identifier.
"""


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "problems/0217-contains-duplicate/solutions.py"


def _load_module_from_path(name: str, path: Path) -> ModuleType:
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover (mkdocs runtime)
        raise RuntimeError(f"Cannot load module spec for {path}")
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[assignment]
    return mod


_task_mod = _load_module_from_path("task0217_contains_duplicate", SRC)

# Re-export for mkdocstrings
BruteForce = _task_mod.BruteForce
SetBased = _task_mod.SetBased
Sorting = _task_mod.Sorting

__all__ = ["BruteForce", "SetBased", "Sorting"]
