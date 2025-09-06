# 0424. Longest Repeating Character Replacement

## Quick Facts

- URL: https://leetcode.com/problems/longest-repeating-character-replacement/
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
- Run: `pytest -q -k "0424"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0340 | Medium | [Longest Substring with At Most K Distinct Characters](../0340-longest-substring-with-at-most-k-distinct-characters/readme.md) | [link](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| 1004 | Medium | [Max Consecutive Ones III](../1004-max-consecutive-ones-iii/readme.md) | [link](https://leetcode.com/problems/max-consecutive-ones-iii/) |
| 2009 | Hard | [Minimum Number of Operations to Make Array Continuous](../2009-minimum-number-of-operations-to-make-array-continuous/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) |
| 2024 | Medium | [Maximize the Confusion of an Exam](../2024-maximize-the-confusion-of-an-exam/readme.md) | [link](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) |
| 2213 | Hard | [Longest Substring of One Repeating Character](../2213-longest-substring-of-one-repeating-character/readme.md) | [link](https://leetcode.com/problems/longest-substring-of-one-repeating-character/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:57Z: Created scaffold.
