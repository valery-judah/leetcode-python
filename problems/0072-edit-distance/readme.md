# 0072. Edit Distance

## Quick Facts

- URL: https://leetcode.com/problems/edit-distance/
- Signature: `word1: str`, `word2: str` → `int`
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
- Run: `pytest -q -k "0072"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0161 | Medium | [One Edit Distance](../0161-one-edit-distance/readme.md) | [link](https://leetcode.com/problems/one-edit-distance/) |
| 0583 | Medium | [Delete Operation for Two Strings](../0583-delete-operation-for-two-strings/readme.md) | [link](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| 0712 | Medium | [Minimum ASCII Delete Sum for Two Strings](../0712-minimum-ascii-delete-sum-for-two-strings/readme.md) | [link](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |
| 1035 | Medium | [Uncrossed Lines](../1035-uncrossed-lines/readme.md) | [link](https://leetcode.com/problems/uncrossed-lines/) |
| 2209 | Hard | [Minimum White Tiles After Covering With Carpets](../2209-minimum-white-tiles-after-covering-with-carpets/readme.md) | [link](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/) |
| 3504 | Hard | [Longest Palindrome After Substring Concatenation II](../3504-longest-palindrome-after-substring-concatenation-ii/readme.md) | [link](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/) |
| 3579 | Hard | [Minimum Steps to Convert String with Operations](../3579-minimum-steps-to-convert-string-with-operations/readme.md) | [link](https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:48Z: Created scaffold.
