# 0217. Contains Duplicate

## Quick Facts

- URL: https://leetcode.com/problems/contains-duplicate/
- Signature: `nums: list[int]` → `bool`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
| 0219 | Easy | [Contains Duplicate II](../0219-contains-duplicate-ii/readme.md) | [link](https://leetcode.com/problems/contains-duplicate-ii/) |
| 0220 | Hard | [Contains Duplicate III](../0220-contains-duplicate-iii/readme.md) | [link](https://leetcode.com/problems/contains-duplicate-iii/) |
| 2357 | Easy | [Make Array Zero by Subtracting Equal Amounts](../2357-make-array-zero-by-subtracting-equal-amounts/readme.md) | [link](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) |
| 3438 | Easy | [Find Valid Pair of Adjacent Digits in String](../3438-find-valid-pair-of-adjacent-digits-in-string/readme.md) | [link](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
