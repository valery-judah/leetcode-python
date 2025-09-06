# 0127. Word Ladder

## Quick Facts

- URL: https://leetcode.com/problems/word-ladder/
- Signature: `beginWord: str`, `endWord: str`, `wordList: list[str]` → `int`
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
- Run: `pytest -q -k "0127"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0126 | Hard | [Word Ladder II](../0126-word-ladder-ii/readme.md) | [link](https://leetcode.com/problems/word-ladder-ii/) |
| 0433 | Medium | [Minimum Genetic Mutation](../0433-minimum-genetic-mutation/readme.md) | [link](https://leetcode.com/problems/minimum-genetic-mutation/) |
| 2452 | Medium | [Words Within Two Edits of Dictionary](../2452-words-within-two-edits-of-dictionary/readme.md) | [link](https://leetcode.com/problems/words-within-two-edits-of-dictionary/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
