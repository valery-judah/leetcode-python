# 0300. Longest Increasing Subsequence

## Quick Facts

- URL: [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- Function: `lengthOfLIS`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

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
| 0334 | Medium | [Increasing Triplet Subsequence](../0334-increasing-triplet-subsequence/readme.md) | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) |
| 0354 | Hard | [Russian Doll Envelopes](../0354-russian-doll-envelopes/readme.md) | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) |
| 0646 | Medium | [Maximum Length of Pair Chain](../0646-maximum-length-of-pair-chain/readme.md) | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) |
| 0673 | Medium | [Number of Longest Increasing Subsequence](../0673-number-of-longest-increasing-subsequence/readme.md) | [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) |
| 0712 | Medium | [Minimum ASCII Delete Sum for Two Strings](../0712-minimum-ascii-delete-sum-for-two-strings/readme.md) | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |
| 1766 | Hard | [Minimum Number of Removals to Make Mountain Array](../1766-minimum-number-of-removals-to-make-mountain-array/readme.md) | [Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |
| 2096 | Hard | [Find the Longest Valid Obstacle Course at Each Position](../2096-find-the-longest-valid-obstacle-course-at-each-position/readme.md) | [Find the Longest Valid Obstacle Course at Each Position](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/) |
| 2234 | Hard | [Minimum Operations to Make the Array K-Increasing](../2234-minimum-operations-to-make-the-array-k-increasing/readme.md) | [Minimum Operations to Make the Array K-Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/) |
| 2444 | Medium | [Longest Ideal Subsequence](../2444-longest-ideal-subsequence/readme.md) | [Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence/) |
| 2490 | Hard | [Maximum Number of Books You Can Take](../2490-maximum-number-of-books-you-can-take/readme.md) | [Maximum Number of Books You Can Take](https://leetcode.com/problems/maximum-number-of-books-you-can-take/) |
| 2526 | Hard | [Longest Increasing Subsequence II](../2526-longest-increasing-subsequence-ii/readme.md) | [Longest Increasing Subsequence II](https://leetcode.com/problems/longest-increasing-subsequence-ii/) |
| 3452 | Hard | [Find the Maximum Length of a Good Subsequence II](../3452-find-the-maximum-length-of-a-good-subsequence-ii/readme.md) | [Find the Maximum Length of a Good Subsequence II](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/) |
| 3456 | Medium | [Find the Maximum Length of a Good Subsequence I](../3456-find-the-maximum-length-of-a-good-subsequence-i/readme.md) | [Find the Maximum Length of a Good Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/) |
| 3490 | Medium | [Find the Maximum Length of Valid Subsequence I](../3490-find-the-maximum-length-of-valid-subsequence-i/readme.md) | [Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/) |
| 3491 | Medium | [Find the Maximum Length of Valid Subsequence II](../3491-find-the-maximum-length-of-valid-subsequence-ii/readme.md) | [Find the Maximum Length of Valid Subsequence II](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/) |
| 3716 | Medium | [Longest Subsequence With Decreasing Adjacent Difference](../3716-longest-subsequence-with-decreasing-adjacent-difference/readme.md) | [Longest Subsequence With Decreasing Adjacent Difference](https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/) |

## Examples

### Example 1

```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

### Example 2

```text
Input: nums = [0,1,0,3,2,3]
Output: 4
```

### Example 3

```text
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## References

- LeetCode problem and editorial links
