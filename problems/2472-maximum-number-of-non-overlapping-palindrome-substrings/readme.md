# 2472. Maximum Number of Non-overlapping Palindrome Substrings

## Quick Facts

- URL: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
- Signature: `s: str`, `k: int` → `int`
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
- Run: `pytest -q -k "2472"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0005 | Medium | [Longest Palindromic Substring](../0005-longest-palindromic-substring/readme.md) | [link](https://leetcode.com/problems/longest-palindromic-substring/) |
| 0131 | Medium | [Palindrome Partitioning](../0131-palindrome-partitioning/readme.md) | [link](https://leetcode.com/problems/palindrome-partitioning/) |
| 0132 | Hard | [Palindrome Partitioning II](../0132-palindrome-partitioning-ii/readme.md) | [link](https://leetcode.com/problems/palindrome-partitioning-ii/) |
| 1278 | Hard | [Palindrome Partitioning III](../1278-palindrome-partitioning-iii/readme.md) | [link](https://leetcode.com/problems/palindrome-partitioning-iii/) |
| 1520 | Hard | [Maximum Number of Non-Overlapping Substrings](../1520-maximum-number-of-non-overlapping-substrings/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) |
| 1745 | Hard | [Palindrome Partitioning IV](../1745-palindrome-partitioning-iv/readme.md) | [link](https://leetcode.com/problems/palindrome-partitioning-iv/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:03Z: Created scaffold.
