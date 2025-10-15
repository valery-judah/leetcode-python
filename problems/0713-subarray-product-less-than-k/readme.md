# 0713. Subarray Product Less Than K

## Quick Facts

- URL: [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
- Function: `numSubarrayProductLessThanK`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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
- Run: `pytest -q -k "0713"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                         | LeetCode                                                                                                                  |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 0152   | Medium     | [Maximum Product Subarray](../0152-maximum-product-subarray/readme.md)                                       | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)                                       |
| 0325   | Medium     | [Maximum Size Subarray Sum Equals k](../0325-maximum-size-subarray-sum-equals-k/readme.md)                   | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)                   |
| 0325   | Medium     | [Subarray Sum Equals K](../0325-subarray-sum-equals-k/readme.md)                                             | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)                                             |
| 1099   | Easy       | [Two Sum Less Than K](../1099-two-sum-less-than-k/readme.md)                                                 | [Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/)                                                 |
| 2110   | Medium     | [Number of Smooth Descent Periods of a Stock](../2110-number-of-smooth-descent-periods-of-a-stock/readme.md) | [Number of Smooth Descent Periods of a Stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/) |
| 2302   | Hard       | [Count Subarrays With Score Less Than K](../2302-count-subarrays-with-score-less-than-k/readme.md)           | [Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/)           |

## Examples

### Example 1

```text
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

### Example 2

```text
Input: nums = [1,2,3], k = 0
Output: 0
```

## References

- LeetCode problem and editorial links
