# 1143. Longest Common Subsequence

## Quick Facts

- URL: https://leetcode.com/problems/longest-common-subsequence/
- Signature: `text1: str`, `text2: str` → `int`
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
- Run: `pytest -q -k "1143"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0516 | Medium | [Longest Palindromic Subsequence](../0516-longest-palindromic-subsequence/readme.md) | [link](https://leetcode.com/problems/longest-palindromic-subsequence/) |
| 0583 | Medium | [Delete Operation for Two Strings](../0583-delete-operation-for-two-strings/readme.md) | [link](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| 1092 | Hard | [Shortest Common Supersequence](../1092-shortest-common-supersequence/readme.md) | [link](https://leetcode.com/problems/shortest-common-supersequence/) |
| 2207 | Medium | [Maximize Number of Subsequences in a String](../2207-maximize-number-of-subsequences-in-a-string/readme.md) | [link](https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/) |
| 2565 | Hard | [Subsequence With the Minimum Score](../2565-subsequence-with-the-minimum-score/readme.md) | [link](https://leetcode.com/problems/subsequence-with-the-minimum-score/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:01Z: Created scaffold.
