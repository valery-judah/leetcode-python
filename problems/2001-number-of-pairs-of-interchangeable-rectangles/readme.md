# 2001. Number of Pairs of Interchangeable Rectangles

## Quick Facts

- URL: https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
- Signature: `rectangles: list[list[int]]` → `int`
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
- Run: `pytest -q -k "2001"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1512 | Easy | [Number of Good Pairs](../1512-number-of-good-pairs/readme.md) | [link](https://leetcode.com/problems/number-of-good-pairs/) |
| 1814 | Medium | [Count Nice Pairs in an Array](../1814-count-nice-pairs-in-an-array/readme.md) | [link](https://leetcode.com/problems/count-nice-pairs-in-an-array/) |
| 2197 | Hard | [Replace Non-Coprime Numbers in Array](../2197-replace-non-coprime-numbers-in-array/readme.md) | [link](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:02Z: Created scaffold.
