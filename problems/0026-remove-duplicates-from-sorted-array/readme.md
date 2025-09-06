# 0026. Remove Duplicates from Sorted Array

## Quick Facts

- URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Signature: `nums: list[int]` → `int`
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
- Run: `pytest -q -k "0026"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0027 | Easy | [Remove Element](../0027-remove-element/readme.md) | [link](https://leetcode.com/problems/remove-element/) |
| 0080 | Medium | [Remove Duplicates from Sorted Array II](../0080-remove-duplicates-from-sorted-array-ii/readme.md) | [link](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) |
| 2460 | Easy | [Apply Operations to an Array](../2460-apply-operations-to-an-array/readme.md) | [link](https://leetcode.com/problems/apply-operations-to-an-array/) |
| 2615 | Medium | [Sum of Distances](../2615-sum-of-distances/readme.md) | [link](https://leetcode.com/problems/sum-of-distances/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
