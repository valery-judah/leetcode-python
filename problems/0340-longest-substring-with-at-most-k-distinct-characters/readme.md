# 0340. Longest Substring with At Most K Distinct Characters

## Quick Facts

- URL: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
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
- Run: `pytest -q -k "0340"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0003 | Medium | [Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/readme.md) | [link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 0159 | Medium | [Longest Substring with At Most Two Distinct Characters](../0159-longest-substring-with-at-most-two-distinct-characters/readme.md) | [link](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |
| 0424 | Medium | [Longest Repeating Character Replacement](../0424-longest-repeating-character-replacement/readme.md) | [link](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| 0992 | Hard | [Subarrays with K Different Integers](../0992-subarrays-with-k-different-integers/readme.md) | [link](https://leetcode.com/problems/subarrays-with-k-different-integers/) |
| 1004 | Medium | [Max Consecutive Ones III](../1004-max-consecutive-ones-iii/readme.md) | [link](https://leetcode.com/problems/max-consecutive-ones-iii/) |
| 2024 | Medium | [Maximize the Confusion of an Exam](../2024-maximize-the-confusion-of-an-exam/readme.md) | [link](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:56Z: Created scaffold.
