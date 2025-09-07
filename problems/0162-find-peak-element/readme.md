# 0162. Find Peak Element

## Quick Facts

- URL: [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- Function: `findPeakElement`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1] for all valid i.`

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
- Run: `pytest -q -k "0162"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0882 | Medium | [Peak Index in a Mountain Array](../0882-peak-index-in-a-mountain-array/readme.md) | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |
| 1901 | Medium | [Find a Peak Element II](../1901-find-a-peak-element-ii/readme.md) | [Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/) |
| 2273 | Medium | [Pour Water Between Buckets to Make Water Levels Equal](../2273-pour-water-between-buckets-to-make-water-levels-equal/readme.md) | [Pour Water Between Buckets to Make Water Levels Equal](https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/) |
| 2210 | Easy | [Count Hills and Valleys in an Array](../2210-count-hills-and-valleys-in-an-array/readme.md) | [Count Hills and Valleys in an Array](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/) |
| 2951 | Easy | [Find the Peaks](../2951-find-the-peaks/readme.md) | [Find the Peaks](https://leetcode.com/problems/find-the-peaks/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2

```text
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

## References

- LeetCode problem and editorial links
