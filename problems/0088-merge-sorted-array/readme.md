# 0088. Merge Sorted Array

## Quick Facts

- URL: https://leetcode.com/problems/merge-sorted-array/
- Signature: `nums1: list[int]`, `m: int`, `nums2: list[int]`, `n: int` → `None`
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
- Run: `pytest -q -k "0088"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0021 | Easy | [Merge Two Sorted Lists](../0021-merge-two-sorted-lists/readme.md) | [link](https://leetcode.com/problems/merge-two-sorted-lists/) |
| 0977 | Easy | [Squares of a Sorted Array](../0977-squares-of-a-sorted-array/readme.md) | [link](https://leetcode.com/problems/squares-of-a-sorted-array/) |
| 0986 | Medium | [Interval List Intersections](../0986-interval-list-intersections/readme.md) | [link](https://leetcode.com/problems/interval-list-intersections/) |
| 2516 | Medium | [Take K of Each Character From Left and Right](../2516-take-k-of-each-character-from-left-and-right/readme.md) | [link](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:49Z: Created scaffold.
