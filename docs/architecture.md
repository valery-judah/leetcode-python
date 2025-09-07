# Repository Architecture & Conventions

This document captures how this workspace is structured and the patterns used for solving problems and testing solutions.

## Top-level Layout

- `problems/`: One folder per LeetCode problem (`NNNN-slug/`). Source of truth for current work.
- `templates/`: Scaffolding templates used by `scripts/new_problem.py`.
- `scripts/`: Utilities (e.g., `new_problem.py` for creating problem skeletons).
- `docs/`: Documentation (workflow, architecture, logs).
- `memory-bank/`: Cline memory notes (patterns, active context, progress).
- `old_leetcode/`: Legacy ad-hoc solutions not following current structure.

Key configs:

- Testing: `pytest.ini` → discovers tests in `problems/`.
- Lint/format/type: `pyproject.toml`.
- Make targets: `Makefile`.

## Problem Folder Structure

Default (single solution):

- `problems/NNNN-slug/readme.md` — clarifying questions, examples, approach, complexity.
- `problems/NNNN-slug/solutions.py` — export a `Solution` class with a `solve(...)` method. Optionally include `ALL_SOLUTIONS = [Solution]` for consistency.

Multi-solution pattern (recommended for comparing approaches):

- `problems/NNNN-slug/solutions.py` — consolidated module exporting multiple classes implementing the same `solve(...)` API. List them in `ALL_SOLUTIONS = [ClassA, ClassB, ...]`. Optionally set `Solution = ClassA` as a default alias.
- No per-problem test files are required. The generic spec `problems/all_problems_spec.py` auto-discovers the primary class (or the first class in `ALL_SOLUTIONS`) and runs the declared `TEST_CASES`.

Example: `problems/0217-contains-duplicate/solutions.py`.

### Example: Minimal `solutions.py` and Variant IDs

Create a consolidated `solutions.py` with multiple classes and export them via `ALL_SOLUTIONS`:

```python
from __future__ import annotations


class Baseline:
    def solve(self, *args, **kwargs):
        raise NotImplementedError


class SetBased:
    def solve(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


# Optional alias used when only a single class is exported
Solution = SetBased

# Explicit list used by tests to parametrize variants
ALL_SOLUTIONS = [Baseline, SetBased]
```

Running tests with `-vv` shows each class as a separate variant, labeled `module:ClassName`:

```bash
$ pytest problems/0217-contains-duplicate/test_0217_contains_duplicate.py -vv
test_0217_contains_duplicate.py::test_contains_duplicate[solutions:Baseline] PASSED
test_0217_contains_duplicate.py::test_contains_duplicate[solutions:SetBased] PASSED
```

## Testing Conventions

- Runner: `pytest` (see `Makefile: test`).
- Discovery: `pytest` finds `test_*.py` under `problems/`.
- Parametrization: Prefer `@pytest.mark.parametrize` for case coverage.
- Loading solutions: Tests use `runpy.run_path(...)` to load target modules without importing packages, avoiding `__init__.py` overhead.
- Multi-export discovery: Tests read `ALL_SOLUTIONS` (list of classes) when present; otherwise use a single `Solution` class from `solutions.py`. Variants are labeled as `module:ClassName` for clarity in `-vv` output.
- Fixture for multi-variant tests: Parametrize a factory/cls fixture with `pytest.param(cls, id="variant-name")` so `-vv` shows meaningful IDs.
- Verbosity: `make test` runs quiet (`-q`); use `pytest -vv` for detailed case/variant names.
- Optional marks: Mark slow or experimental variants with `@pytest.mark.slow` via param marks and filter with `-m 'not slow'`.

## Coding Conventions

- Public API: `class Solution: def solve(self, ...) -> ...` to keep tests consistent.
- Types: Use type hints; allow partial typing during exploration (`make type` tolerates stubs in `problems/`).
- Docs: Add a docstring to `solve(...)` and fill the problem `readme.md` with approach and complexity.
- No side effects: Avoid print/exec at import time; tests control execution.

## Scaffolding

- Create a new problem skeleton: `python scripts/new_problem.py <slug> <number> [--difficulty ... --tags ... --url ...]`.
- Templates live in `templates/`; the `--multi` scaffold creates `solutions.py` with `ALL_SOLUTIONS` and a discovery test that parametrizes each class.

## Decision Records (optional but recommended)

For notable choices (e.g., “Use pytest with per-problem tests”, “Adopt multi-solution discovery”), record brief ADRs:

- `docs/decisions/0001-testing-approach.md`
- `docs/decisions/0002-multi-solution-structure.md`

Each ADR should include: context, decision, consequences, and date.

## Patterns & Memory

- Algorithmic patterns: `memory-bank/patterns.md` — reusable solution strategies (e.g., two-pointer, sliding window, hash map).
- Active problem notes: `memory-bank/activeContext.md` — current focus, examples, TODOs.
- Progress log: `memory-bank/progress.md` — optional lightweight log of sessions/outcomes.

Use `docs/` for durable, repo-wide architecture/conventions; use `memory-bank/` for personal, evolving heuristics and active context.
