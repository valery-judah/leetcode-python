# 0209. Minimum Size Subarray Sum

## Quick Facts

- URL: [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- Function: `minSubArrayLen`
- Signature: `(target: int, nums: list[int])  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

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
- Run: `pytest -q -k "0209"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0076 | Hard | [Minimum Window Substring](../0076-minimum-window-substring/readme.md) | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| 0325 | Medium | [Maximum Size Subarray Sum Equals k](../0325-maximum-size-subarray-sum-equals-k/readme.md) | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) |
| 0718 | Medium | [Maximum Length of Repeated Subarray](../0718-maximum-length-of-repeated-subarray/readme.md) | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) |
| 1776 | Medium | [Minimum Operations to Reduce X to Zero](../1776-minimum-operations-to-reduce-x-to-zero/readme.md) | [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |
| 2211 | Medium | [K Radius Subarray Averages](../2211-k-radius-subarray-averages/readme.md) | [K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) |
| 2329 | Medium | [Maximum Product After K Increments](../2329-maximum-product-after-k-increments/readme.md) | [Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/) |
| 3381 | Easy | [Shortest Subarray With OR at Least K I](../3381-shortest-subarray-with-or-at-least-k-i/readme.md) | [Shortest Subarray With OR at Least K I](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) |
| 3644 | Easy | [Minimum Positive Sum Subarray](../3644-minimum-positive-sum-subarray/readme.md) | [Minimum Positive Sum Subarray](https://leetcode.com/problems/minimum-positive-sum-subarray/) |

## Examples

### Example 1

```text
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

### Example 2

```text
Input: target = 4, nums = [1,4,4]
Output: 1
```

### Example 3

```text
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## References

- LeetCode problem and editorial links
