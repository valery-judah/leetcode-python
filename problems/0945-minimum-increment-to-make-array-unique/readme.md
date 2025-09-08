# 0945. Minimum Increment to Make Array Unique

## Quick Facts

- URL: [Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)
- Function: `minIncrementForUnique`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Greedy**

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

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
- Run: `pytest -q -k "0945"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1827 | Easy | [Minimum Operations to Make the Array Increasing](../1827-minimum-operations-to-make-the-array-increasing/readme.md) | [Minimum Operations to Make the Array Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/) |
| 2233 | Medium | [Maximum Product After K Increments](../2233-maximum-product-after-k-increments/readme.md) | [Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/) |
| 3396 | Easy | [Minimum Number of Operations to Make Elements in Array Distinct](../3396-minimum-number-of-operations-to-make-elements-in-array-distinct/readme.md) | [Minimum Number of Operations to Make Elements in Array Distinct](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/) |

## Examples

### Example 1

```text
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
```

### Example 2

```text
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
```

## References

- LeetCode problem and editorial links
