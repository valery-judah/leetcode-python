# 0068. Text Justification

## Quick Facts

- URL: https://leetcode.com/problems/text-justification/
- Signature: `words: list[str]`, `maxWidth: int` → `list[str]`
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
- Run: `pytest -q -k "0068"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1592 | Easy | [Rearrange Spaces Between Words](../1592-rearrange-spaces-between-words/readme.md) | [link](https://leetcode.com/problems/rearrange-spaces-between-words/) |
| 2138 | Easy | [Divide a String Into Groups of Size k](../2138-divide-a-string-into-groups-of-size-k/readme.md) | [link](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/) |
| 2468 | Hard | [Split Message Based on Limit](../2468-split-message-based-on-limit/readme.md) | [link](https://leetcode.com/problems/split-message-based-on-limit/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:48Z: Created scaffold.
