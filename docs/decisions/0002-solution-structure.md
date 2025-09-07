# 0002 – Solution Structure

- Status: Accepted
- Date: 2025-08-30

## Context

For some problems we want to compare multiple approaches (e.g., brute force, sorting, hash-set) and run the same tests across all.

## Decision

Adopt a consolidated `solutions.py` file in each problem directory when comparing approaches. The file exports multiple classes that implement the same `solve(...)` API and a list `ALL_SOLUTIONS = [ClassA, ClassB, ...]` for test discovery. Optionally expose `Solution = ClassA` as a default alias. Tests read `ALL_SOLUTIONS` and parametrize over each class (or a single `Solution`).

## Consequences

- Pros: Easy comparison, consistent API, single file to navigate, clear reporting (`-vv` shows `module:ClassName`).
- Cons: Requires maintaining `ALL_SOLUTIONS` list; minor boilerplate to add new classes.
