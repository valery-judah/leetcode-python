# 0217. Contains Duplicate

## Quick Facts

- URL: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- Function: `containsDuplicate`
- Signature: `(nums: list[int])  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= nums.length <= 10^5`
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
- Run: `pytest -q -k "0217"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0219 | Easy | [Contains Duplicate II](../0219-contains-duplicate-ii/readme.md) | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) |
| 0220 | Hard | [Contains Duplicate III](../0220-contains-duplicate-iii/readme.md) | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) |
| 2357 | Easy | [Make Array Zero by Subtracting Equal Amounts](../2357-make-array-zero-by-subtracting-equal-amounts/readme.md) | [Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) |
| 3438 | Easy | [Find Valid Pair of Adjacent Digits in String](../3438-find-valid-pair-of-adjacent-digits-in-string/readme.md) | [Find Valid Pair of Adjacent Digits in String](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/) |

## Examples

None

## References

- LeetCode problem and editorial links
