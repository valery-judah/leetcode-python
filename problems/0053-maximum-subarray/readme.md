# 0053. Maximum Subarray

## Quick Facts

- URL: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- Function: `maxSubArray`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= nums.length <= 10^5`
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
- Run: `pytest -q -k "0053"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0121 | Easy | [Best Time to Buy and Sell Stock](../0121-best-time-to-buy-and-sell-stock/readme.md) | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 0152 | Medium | [Maximum Product Subarray](../0152-maximum-product-subarray/readme.md) | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) |
| 0697 | Easy | [Degree of an Array](../0697-degree-of-an-array/readme.md) | [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) |
| 0978 | Medium | [Longest Turbulent Subarray](../0978-longest-turbulent-subarray/readme.md) | [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) |
| 2321 | Hard | [Maximum Score Of Spliced Array](../2321-maximum-score-of-spliced-array/readme.md) | [Maximum Score Of Spliced Array](https://leetcode.com/problems/maximum-score-of-spliced-array/) |
| 1749 | Medium | [Maximum Absolute Sum of Any Subarray](../1749-maximum-absolute-sum-of-any-subarray/readme.md) | [Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) |
| 1746 | Medium | [Maximum Subarray Sum After One Operation](../1746-maximum-subarray-sum-after-one-operation/readme.md) | [Maximum Subarray Sum After One Operation](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/) |
| 2272 | Hard | [Substring With Largest Variance](../2272-substring-with-largest-variance/readme.md) | [Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/) |
| 2302 | Hard | [Count Subarrays With Score Less Than K](../2302-count-subarrays-with-score-less-than-k/readme.md) | [Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) |
| 2496 | Easy | [Maximum Value of a String in an Array](../2496-maximum-value-of-a-string-in-an-array/readme.md) | [Maximum Value of a String in an Array](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/) |
| 2606 | Medium | [Find the Substring With Maximum Cost](../2606-find-the-substring-with-maximum-cost/readme.md) | [Find the Substring With Maximum Cost](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) |
| 2600 | Easy | [K Items With the Maximum Sum](../2600-k-items-with-the-maximum-sum/readme.md) | [K Items With the Maximum Sum](https://leetcode.com/problems/k-items-with-the-maximum-sum/) |
| 3026 | Medium | [Maximum Good Subarray Sum](../3026-maximum-good-subarray-sum/readme.md) | [Maximum Good Subarray Sum](https://leetcode.com/problems/maximum-good-subarray-sum/) |
| 3410 | Hard | [Maximize Subarray Sum After Removing All Occurrences of One Element](../3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/readme.md) | [Maximize Subarray Sum After Removing All Occurrences of One Element](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) |

## Examples

### Example 1

```text
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

### Example 2

```text
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

### Example 3

```text
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

## References

- LeetCode problem and editorial links
