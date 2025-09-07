# 0169. Majority Element

## Quick Facts

- URL: [Majority Element](https://leetcode.com/problems/majority-element/)
- Function: `majorityElement`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
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
- Run: `pytest -q -k "0169"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0229 | Medium | [Majority Element II](../0229-majority-element-ii/readme.md) | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) |
| 1150 | Easy | [Check If a Number Is Majority Element in a Sorted Array](../1150-check-if-a-number-is-majority-element-in-a-sorted-array/readme.md) | [Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) |
| 2404 | Easy | [Most Frequent Even Element](../2404-most-frequent-even-element/readme.md) | [Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/) |
| 2780 | Medium | [Minimum Index of a Valid Split](../2780-minimum-index-of-a-valid-split/readme.md) | [Minimum Index of a Valid Split](https://leetcode.com/problems/minimum-index-of-a-valid-split/) |
| 3065 | Easy | [Minimum Operations to Exceed Threshold Value I](../3065-minimum-operations-to-exceed-threshold-value-i/readme.md) | [Minimum Operations to Exceed Threshold Value I](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) |
| 3527 | Medium | [Find the Most Common Response](../3527-find-the-most-common-response/readme.md) | [Find the Most Common Response](https://leetcode.com/problems/find-the-most-common-response/) |
| 3438 | Easy | [Find Valid Pair of Adjacent Digits in String](../3438-find-valid-pair-of-adjacent-digits-in-string/readme.md) | [Find Valid Pair of Adjacent Digits in String](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/) |

## Examples

### Example 1

```text
Input: nums = [3,2,3]
Output: 3
```

### Example 2

```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## References

- LeetCode problem and editorial links
