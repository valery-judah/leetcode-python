# 0416. Partition Equal Subset Sum

## Quick Facts

- URL: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- Function: `canPartition`
- Signature: `(nums: list[int])  -> bool`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

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
- Run: `pytest -q -k "0416"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0698 | Medium | [Partition to K Equal Sum Subsets](../0698-partition-to-k-equal-sum-subsets/readme.md) | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |
| 2108 | Medium | [Minimize the Difference Between Target and Chosen Elements](../2108-minimize-the-difference-between-target-and-chosen-elements/readme.md) | [Minimize the Difference Between Target and Chosen Elements](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/) |
| 2135 | Hard | [Maximum Number of Ways to Partition an Array](../2135-maximum-number-of-ways-to-partition-an-array/readme.md) | [Maximum Number of Ways to Partition an Array](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) |
| 2162 | Hard | [Partition Array Into Two Arrays to Minimize Sum Difference](../2162-partition-array-into-two-arrays-to-minimize-sum-difference/readme.md) | [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) |
| 2480 | Easy | [Find Subarrays With Equal Sum](../2480-find-subarrays-with-equal-sum/readme.md) | [Find Subarrays With Equal Sum](https://leetcode.com/problems/find-subarrays-with-equal-sum/) |
| 2601 | Hard | [Number of Great Partitions](../2601-number-of-great-partitions/readme.md) | [Number of Great Partitions](https://leetcode.com/problems/number-of-great-partitions/) |
| 2650 | Easy | [Split With Minimum Sum](../2650-split-with-minimum-sum/readme.md) | [Split With Minimum Sum](https://leetcode.com/problems/split-with-minimum-sum/) |

## Examples

### Example 1

```text
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

### Example 2

```text
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## References

- LeetCode problem and editorial links
