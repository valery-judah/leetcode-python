# 0560. Maximum Size Subarray Sum Equals k

## Quick Facts

- URL: [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- Function: `maxSubArrayLen`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `-10^9 <= k <= 10^9`

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
- Run: `pytest -q -k "0560"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0209 | Medium | [Minimum Size Subarray Sum](../0209-minimum-size-subarray-sum/readme.md) | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 0303 | Easy | [Range Sum Query - Immutable](../0303-range-sum-query-immutable/readme.md) | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) |
| 0525 | Medium | [Contiguous Array](../0525-contiguous-array/readme.md) | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) |
| 0713 | Medium | [Subarray Product Less Than K](../0713-subarray-product-less-than-k/readme.md) | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) |
| 2779 | Medium | [Maximum Beauty of an Array After Applying Operation](../2779-maximum-beauty-of-an-array-after-applying-operation/readme.md) | [Maximum Beauty of an Array After Applying Operation](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/) |
| 3097 | Medium | [Shortest Subarray With OR at Least K II](../3097-shortest-subarray-with-or-at-least-k-ii/readme.md) | [Shortest Subarray With OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/) |

## Examples

### Example 1

```text
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

### Example 2

```text
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

## References

- LeetCode problem and editorial links
