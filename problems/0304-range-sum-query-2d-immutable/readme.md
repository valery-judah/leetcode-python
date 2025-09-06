# 0304. Range Sum Query 2D - Immutable

## Quick Facts

- URL: https://leetcode.com/problems/range-sum-query-2d-immutable/
- Signature: `inputs: list[int]`, `inputs: list[int]` → `list[str]`
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
- Run: `pytest -q -k "0304"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0303 | Easy | [Range Sum Query - Immutable](../0303-range-sum-query-immutable/readme.md) | [link](https://leetcode.com/problems/range-sum-query-immutable/) |
| 0308 | Medium | [Range Sum Query 2D - Mutable](../0308-range-sum-query-2d-mutable/readme.md) | [link](https://leetcode.com/problems/range-sum-query-2d-mutable/) |
| 3030 | Medium | [Find the Grid of Region Average](../3030-find-the-grid-of-region-average/readme.md) | [link](https://leetcode.com/problems/find-the-grid-of-region-average/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
