# 0152. Maximum Product Subarray

## Quick Facts

- URL: [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- Function: `maxProduct`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- `The product of any subarray of nums is guaranteed to fit in a 32-bit integer.`

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
- Run: `pytest -q -k "0152"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0053 | Medium | [Maximum Subarray](../0053-maximum-subarray/readme.md) | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |
| 0198 | Medium | [House Robber](../0198-house-robber/readme.md) | [House Robber](https://leetcode.com/problems/house-robber/) |
| 0238 | Medium | [Product of Array Except Self](../0238-product-of-array-except-self/readme.md) | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |
| 0628 | Easy | [Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/readme.md) | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) |
| 0713 | Medium | [Subarray Product Less Than K](../0713-subarray-product-less-than-k/readme.md) | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) |

## Examples

### Example 1

```text
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

### Example 2

```text
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## References

- LeetCode problem and editorial links
