# 0229. Majority Element II

## Quick Facts

- URL: [Majority Element II](https://leetcode.com/problems/majority-element-ii/)
- Function: `majorityElement`
- Signature: `(nums: list[int])  -> list[int]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

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
- Run: `pytest -q -k "0229"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0169 | Easy | [Majority Element](../0169-majority-element/readme.md) | [Majority Element](https://leetcode.com/problems/majority-element/) |
| 1150 | Easy | [Check If a Number Is Majority Element in a Sorted Array](../1150-check-if-a-number-is-majority-element-in-a-sorted-array/readme.md) | [Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) |
| 2404 | Easy | [Most Frequent Even Element](../2404-most-frequent-even-element/readme.md) | [Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/) |

## Examples

### Example 1

```text
Input: nums = [3,2,3]
Output: [3]
```

### Example 2

```text
Input: nums = [1]
Output: [1]
```

### Example 3

```text
Input: nums = [1,2]
Output: [1,2]
```

## References

- LeetCode problem and editorial links
