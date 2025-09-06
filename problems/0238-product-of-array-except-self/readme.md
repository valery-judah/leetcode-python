# 0238. Product of Array Except Self

## Quick Facts

- URL: https://leetcode.com/problems/product-of-array-except-self/
- Signature: `nums: list[int]` → `list[int]`
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
- Run: `pytest -q -k "0238"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0042 | Hard | [Trapping Rain Water](../0042-trapping-rain-water/readme.md) | [link](https://leetcode.com/problems/trapping-rain-water/) |
| 0152 | Medium | [Maximum Product Subarray](../0152-maximum-product-subarray/readme.md) | [link](https://leetcode.com/problems/maximum-product-subarray/) |
| 0265 | Hard | [Paint House II](../0265-paint-house-ii/readme.md) | [link](https://leetcode.com/problems/paint-house-ii/) |
| 2163 | Hard | [Minimum Difference in Sums After Removal of Elements](../2163-minimum-difference-in-sums-after-removal-of-elements/readme.md) | [link](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) |
| 2906 | Medium | [Construct Product Matrix](../2906-construct-product-matrix/readme.md) | [link](https://leetcode.com/problems/construct-product-matrix/) |
| 3539 | Hard | [Find Sum of Array Product of Magical Sequences](../3539-find-sum-of-array-product-of-magical-sequences/readme.md) | [link](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
