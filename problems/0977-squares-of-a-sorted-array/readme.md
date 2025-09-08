# 0977. Squares of a Sorted Array

## Quick Facts

- URL: [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
- Function: `sortedSquares`
- Signature: `(nums: list[int])  -> list[int]`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums is sorted in non-decreasing order.`

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
- Run: `pytest -q -k "0977"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0088 | Easy | [Merge Sorted Array](../0088-merge-sorted-array/readme.md) | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) |
| 0360 | Medium | [Sort Transformed Array](../0360-sort-transformed-array/readme.md) | [Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) |

## Examples

### Example 1

```text
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

### Example 2

```text
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## References

- LeetCode problem and editorial links
