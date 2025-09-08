# 0081. Search in Rotated Sorted Array II

## Quick Facts

- URL: [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
- Function: `search`
- Signature: `(nums: list[int], target: int)  -> bool`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums is guaranteed to be rotated at some pivot.`
- `-10^4 <= target <= 10^4`

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
- Run: `pytest -q -k "0081"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0033 | Medium | [Search in Rotated Sorted Array](../0033-search-in-rotated-sorted-array/readme.md) | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |

## Examples

### Example 1

```text
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

### Example 2

```text
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

## References

- LeetCode problem and editorial links
