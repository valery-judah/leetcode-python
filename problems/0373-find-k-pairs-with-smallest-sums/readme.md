# 0373. Find K Pairs with Smallest Sums

## Quick Facts

- URL: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
- Signature: `nums1: list[int]`, `nums2: list[int]`, `k: int` → `list[list[int]]`
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
- Run: `pytest -q -k "0373"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0378 | Medium | [Kth Smallest Element in a Sorted Matrix](../0378-kth-smallest-element-in-a-sorted-matrix/readme.md) | [link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |
| 0719 | Hard | [Find K-th Smallest Pair Distance](../0719-find-k-th-smallest-pair-distance/readme.md) | [link](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) |
| 2040 | Hard | [Kth Smallest Product of Two Sorted Arrays](../2040-kth-smallest-product-of-two-sorted-arrays/readme.md) | [link](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:56Z: Created scaffold.
