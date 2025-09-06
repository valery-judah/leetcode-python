# 0125. Valid Palindrome

## Quick Facts

- URL: https://leetcode.com/problems/valid-palindrome/
- Signature: `s: str` → `bool`
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
- Run: `pytest -q -k "0125"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0234 | Easy | [Palindrome Linked List](../0234-palindrome-linked-list/readme.md) | [link](https://leetcode.com/problems/palindrome-linked-list/) |
| 0680 | Easy | [Valid Palindrome II](../0680-valid-palindrome-ii/readme.md) | [link](https://leetcode.com/problems/valid-palindrome-ii/) |
| 2002 | Medium | [Maximum Product of the Length of Two Palindromic Subsequences](../2002-maximum-product-of-the-length-of-two-palindromic-subsequences/readme.md) | [link](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/) |
| 2108 | Easy | [Find First Palindromic String in the Array](../2108-find-first-palindromic-string-in-the-array/readme.md) | [link](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) |
| 2330 | Medium | [Valid Palindrome IV](../2330-valid-palindrome-iv/readme.md) | [link](https://leetcode.com/problems/valid-palindrome-iv/) |
| 3035 | Medium | [Maximum Palindromes After Operations](../3035-maximum-palindromes-after-operations/readme.md) | [link](https://leetcode.com/problems/maximum-palindromes-after-operations/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
