# 1074. Number of Submatrices That Sum to Target

## Quick Facts

- URL: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
- Signature: `matrix: list[list[int]]`, `target: int` → `int`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| # | Idea | When to use | Correctness invariant | Time | Space |
|---|------|-------------|-----------------------|------|-------|
| A | [primary idea] | [scenario] | [invariant] | O(n) | O(n) |
| B | [alternative] | [scenario] | [invariant] | O(n log n) | O(1) |
| C | [reject] | [why not] | [violated invariant] | - | - |

## Edge Cases Checklist

- [case 1]
- [case 2]
- [case 3]

## Correctness Sketch

[state the invariant and why it guarantees correctness]

## Implementation

- `solutions.py` should expose:
  - `ALL_SOLUTIONS = {"...": fn, "...": fn}`
  - Short notes on tradeoffs and pitfalls.

## Tests

- Deterministic cases covering all edge cases above
- Optional fuzz/property checks as applicable
- Run: `pytest -q -k "1074"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2556 | Medium | [Disconnect Path in a Binary Matrix by at Most One Flip](../2556-disconnect-path-in-a-binary-matrix-by-at-most-one-flip/readme.md) | [link](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:00Z: Created scaffold.
