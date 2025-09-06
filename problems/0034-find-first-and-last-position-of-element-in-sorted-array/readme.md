# 0034. Find First and Last Position of Element in Sorted Array

## Quick Facts

- URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- Signature: `nums: list[int]`, `target: int` → `list[int]`
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
- Run: `pytest -q -k "0034"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0278 | Easy | [First Bad Version](../0278-first-bad-version/readme.md) | [link](https://leetcode.com/problems/first-bad-version/) |
| 2055 | Medium | [Plates Between Candles](../2055-plates-between-candles/readme.md) | [link](https://leetcode.com/problems/plates-between-candles/) |
| 2089 | Easy | [Find Target Indices After Sorting Array](../2089-find-target-indices-after-sorting-array/readme.md) | [link](https://leetcode.com/problems/find-target-indices-after-sorting-array/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
