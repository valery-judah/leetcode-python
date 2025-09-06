# 0792. Number of Matching Subsequences

## Quick Facts

- URL: https://leetcode.com/problems/number-of-matching-subsequences/
- Signature: `s: str`, `words: list[str]` → `int`
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
- Run: `pytest -q -k "0792"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0392 | Easy | [Is Subsequence](../0392-is-subsequence/readme.md) | [link](https://leetcode.com/problems/is-subsequence/) |
| 1055 | Medium | [Shortest Way to Form String](../1055-shortest-way-to-form-string/readme.md) | [link](https://leetcode.com/problems/shortest-way-to-form-string/) |
| 2062 | Easy | [Count Vowel Substrings of a String](../2062-count-vowel-substrings-of-a-string/readme.md) | [link](https://leetcode.com/problems/count-vowel-substrings-of-a-string/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:59Z: Created scaffold.
