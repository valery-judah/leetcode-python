# 0238. Product of Array Except Self

## Quick Facts

- URL: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- Function: `productExceptSelf`
- Signature: `(nums: list[int])  -> list[int]`
- Primary pattern: **Prefix Sum**

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- `The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.`

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
- Run: `pytest -q -k "0238"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0042 | Hard | [Trapping Rain Water](../0042-trapping-rain-water/readme.md) | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |
| 0152 | Medium | [Maximum Product Subarray](../0152-maximum-product-subarray/readme.md) | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) |
| 0265 | Hard | [Paint House II](../0265-paint-house-ii/readme.md) | [Paint House II](https://leetcode.com/problems/paint-house-ii/) |
| 2267 | Hard | [Minimum Difference in Sums After Removal of Elements](../2267-minimum-difference-in-sums-after-removal-of-elements/readme.md) | [Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) |
| 3031 | Medium | [Construct Product Matrix](../3031-construct-product-matrix/readme.md) | [Construct Product Matrix](https://leetcode.com/problems/construct-product-matrix/) |
| 3851 | Hard | [Find Sum of Array Product of Magical Sequences](../3851-find-sum-of-array-product-of-magical-sequences/readme.md) | [Find Sum of Array Product of Magical Sequences](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2

```text
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## References

- LeetCode problem and editorial links
