# 0005. Longest Palindromic Substring

## Quick Facts

- URL: https://leetcode.com/problems/longest-palindromic-substring/
- Signature: `s: str` → `str`
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
- Run: `pytest -q -k "0005"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0214 | Hard | [Shortest Palindrome](../0214-shortest-palindrome/readme.md) | [link](https://leetcode.com/problems/shortest-palindrome/) |
| 0266 | Easy | [Palindrome Permutation](../0266-palindrome-permutation/readme.md) | [link](https://leetcode.com/problems/palindrome-permutation/) |
| 0336 | Hard | [Palindrome Pairs](../0336-palindrome-pairs/readme.md) | [link](https://leetcode.com/problems/palindrome-pairs/) |
| 0516 | Medium | [Longest Palindromic Subsequence](../0516-longest-palindromic-subsequence/readme.md) | [link](https://leetcode.com/problems/longest-palindromic-subsequence/) |
| 0647 | Medium | [Palindromic Substrings](../0647-palindromic-substrings/readme.md) | [link](https://leetcode.com/problems/palindromic-substrings/) |
| 2472 | Hard | [Maximum Number of Non-overlapping Palindrome Substrings](../2472-maximum-number-of-non-overlapping-palindrome-substrings/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:45Z: Created scaffold.
