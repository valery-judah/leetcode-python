# 0053. Maximum Subarray

## Quick Facts

- URL: https://leetcode.com/problems/maximum-subarray/
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
- Run: `pytest -q -k "0053"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0121 | Easy | [Best Time to Buy and Sell Stock](../0121-best-time-to-buy-and-sell-stock/readme.md) | [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 0152 | Medium | [Maximum Product Subarray](../0152-maximum-product-subarray/readme.md) | [link](https://leetcode.com/problems/maximum-product-subarray/) |
| 0697 | Easy | [Degree of an Array](../0697-degree-of-an-array/readme.md) | [link](https://leetcode.com/problems/degree-of-an-array/) |
| 0978 | Medium | [Longest Turbulent Subarray](../0978-longest-turbulent-subarray/readme.md) | [link](https://leetcode.com/problems/longest-turbulent-subarray/) |
| 2321 | Hard | [Maximum Score Of Spliced Array](../2321-maximum-score-of-spliced-array/readme.md) | [link](https://leetcode.com/problems/maximum-score-of-spliced-array/) |
| 1749 | Medium | [Maximum Absolute Sum of Any Subarray](../1749-maximum-absolute-sum-of-any-subarray/readme.md) | [link](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) |
| 1746 | Medium | [Maximum Subarray Sum After One Operation](../1746-maximum-subarray-sum-after-one-operation/readme.md) | [link](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/) |
| 2272 | Hard | [Substring With Largest Variance](../2272-substring-with-largest-variance/readme.md) | [link](https://leetcode.com/problems/substring-with-largest-variance/) |
| 2302 | Hard | [Count Subarrays With Score Less Than K](../2302-count-subarrays-with-score-less-than-k/readme.md) | [link](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) |
| 2496 | Easy | [Maximum Value of a String in an Array](../2496-maximum-value-of-a-string-in-an-array/readme.md) | [link](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/) |
| 2606 | Medium | [Find the Substring With Maximum Cost](../2606-find-the-substring-with-maximum-cost/readme.md) | [link](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) |
| 2600 | Easy | [K Items With the Maximum Sum](../2600-k-items-with-the-maximum-sum/readme.md) | [link](https://leetcode.com/problems/k-items-with-the-maximum-sum/) |
| 3026 | Medium | [Maximum Good Subarray Sum](../3026-maximum-good-subarray-sum/readme.md) | [link](https://leetcode.com/problems/maximum-good-subarray-sum/) |
| 3410 | Hard | [Maximize Subarray Sum After Removing All Occurrences of One Element](../3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/readme.md) | [link](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
