# 0002 – Multi-solution Structure

- Status: Accepted
- Date: 2025-08-30

## Context

For some problems we want to compare multiple approaches (e.g., brute force, sorting, hash-set) and run the same tests across all.

## Decision

Introduce an optional `solutions/` folder inside a problem directory. Each file exports a `Solution` class with the same `solve(...)` API. A single pytest file discovers all variants and parametrizes tests over them.

## Consequences

- Pros: Easy comparison, consistent API, one place for cases, clear reporting (with `-vv`).
- Cons: Slightly more scaffolding; discovery requires consistent class export.

