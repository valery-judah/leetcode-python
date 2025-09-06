# 0033. Search in Rotated Sorted Array

## Quick Facts

- URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
- Signature: `nums: list[int]`, `target: int` → `int`
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
- Run: `pytest -q -k "0033"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0081 | Medium | [Search in Rotated Sorted Array II](../0081-search-in-rotated-sorted-array-ii/readme.md) | [link](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) |
| 0153 | Medium | [Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/readme.md) | [link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |
| 2137 | Medium | [Pour Water Between Buckets to Make Water Levels Equal](../2137-pour-water-between-buckets-to-make-water-levels-equal/readme.md) | [link](https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
