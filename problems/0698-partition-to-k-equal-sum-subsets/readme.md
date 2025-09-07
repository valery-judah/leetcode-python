# 0698. Partition to K Equal Sum Subsets

## Quick Facts

- URL: [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
- Function: `canPartitionKSubsets`
- Signature: `(nums: list[int], k: int)  -> bool`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= k <= nums.length <= 16`
- `1 <= nums[i] <= 10^4`
- `The frequency of each element is in the range [1, 4].`

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
- Run: `pytest -q -k "0698"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0416 | Medium | [Partition Equal Subset Sum](../0416-partition-equal-subset-sum/readme.md) | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| 1418 | Medium | [Fair Distribution of Cookies](../1418-fair-distribution-of-cookies/readme.md) | [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/) |
| 2135 | Hard | [Maximum Number of Ways to Partition an Array](../2135-maximum-number-of-ways-to-partition-an-array/readme.md) | [Maximum Number of Ways to Partition an Array](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) |
| 2482 | Medium | [Maximum Rows Covered by Columns](../2482-maximum-rows-covered-by-columns/readme.md) | [Maximum Rows Covered by Columns](https://leetcode.com/problems/maximum-rows-covered-by-columns/) |
| | Medium | Maximum Product of Two Integers With No Common Bits | [Maximum Product of Two Integers With No Common Bits](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/) |

## Examples

### Example 1

```text
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

### Example 2

```text
Input: nums = [1,2,3,4], k = 3
Output: false
```

## References

- LeetCode problem and editorial links
