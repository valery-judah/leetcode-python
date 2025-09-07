# 0001 – Testing Approach

- Status: Accepted
- Date: 2025-08-30

## Context

The repo contains a mix of ad-hoc tests, `unittest`, and pytest. We want a consistent, fast, and scalable testing setup for iterative problem solving.

## Decision

Adopt pytest with per-problem tests under `problems/NNNN-slug/`. Tests use parametrization and `runpy` to load `solutions.py` (single or multi via `ALL_SOLUTIONS`) without package imports.

## Consequences

- Pros: Concise tests, rich assertions, easy parametrization, great failure output, CI-friendly.
- Cons: Requires an extra file per problem (test file) unless using the multi-solution aggregate test.
