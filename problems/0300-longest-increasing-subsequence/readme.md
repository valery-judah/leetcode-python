# 0300. Longest Increasing Subsequence

## Quick Facts

- URL: https://leetcode.com/problems/longest-increasing-subsequence/
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
- Run: `pytest -q -k "0300"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0334 | Medium | [Increasing Triplet Subsequence](../0334-increasing-triplet-subsequence/readme.md) | [link](https://leetcode.com/problems/increasing-triplet-subsequence/) |
| 0354 | Hard | [Russian Doll Envelopes](../0354-russian-doll-envelopes/readme.md) | [link](https://leetcode.com/problems/russian-doll-envelopes/) |
| 0646 | Medium | [Maximum Length of Pair Chain](../0646-maximum-length-of-pair-chain/readme.md) | [link](https://leetcode.com/problems/maximum-length-of-pair-chain/) |
| 0673 | Medium | [Number of Longest Increasing Subsequence](../0673-number-of-longest-increasing-subsequence/readme.md) | [link](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) |
| 0712 | Medium | [Minimum ASCII Delete Sum for Two Strings](../0712-minimum-ascii-delete-sum-for-two-strings/readme.md) | [link](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |
| 1671 | Hard | [Minimum Number of Removals to Make Mountain Array](../1671-minimum-number-of-removals-to-make-mountain-array/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |
| 1964 | Hard | [Find the Longest Valid Obstacle Course at Each Position](../1964-find-the-longest-valid-obstacle-course-at-each-position/readme.md) | [link](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/) |
| 2111 | Hard | [Minimum Operations to Make the Array K-Increasing](../2111-minimum-operations-to-make-the-array-k-increasing/readme.md) | [link](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/) |
| 2370 | Medium | [Longest Ideal Subsequence](../2370-longest-ideal-subsequence/readme.md) | [link](https://leetcode.com/problems/longest-ideal-subsequence/) |
| 2355 | Hard | [Maximum Number of Books You Can Take](../2355-maximum-number-of-books-you-can-take/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-books-you-can-take/) |
| 2407 | Hard | [Longest Increasing Subsequence II](../2407-longest-increasing-subsequence-ii/readme.md) | [link](https://leetcode.com/problems/longest-increasing-subsequence-ii/) |
| 3177 | Hard | [Find the Maximum Length of a Good Subsequence II](../3177-find-the-maximum-length-of-a-good-subsequence-ii/readme.md) | [link](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/) |
| 3176 | Medium | [Find the Maximum Length of a Good Subsequence I](../3176-find-the-maximum-length-of-a-good-subsequence-i/readme.md) | [link](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/) |
| 3201 | Medium | [Find the Maximum Length of Valid Subsequence I](../3201-find-the-maximum-length-of-valid-subsequence-i/readme.md) | [link](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/) |
| 3202 | Medium | [Find the Maximum Length of Valid Subsequence II](../3202-find-the-maximum-length-of-valid-subsequence-ii/readme.md) | [link](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/) |
| 3409 | Medium | [Longest Subsequence With Decreasing Adjacent Difference](../3409-longest-subsequence-with-decreasing-adjacent-difference/readme.md) | [link](https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
