# 0007. Reverse Integer

## Quick Facts

- URL: https://leetcode.com/problems/reverse-integer/
- Signature: `x: int` → `int`
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
- Run: `pytest -q -k "0007"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0008 | Medium | [String to Integer (atoi)](../0008-string-to-integer-atoi/readme.md) | [link](https://leetcode.com/problems/string-to-integer-atoi/) |
| 0190 | Easy | [Reverse Bits](../0190-reverse-bits/readme.md) | [link](https://leetcode.com/problems/reverse-bits/) |
| 2119 | Easy | [A Number After a Double Reversal](../2119-a-number-after-a-double-reversal/readme.md) | [link](https://leetcode.com/problems/a-number-after-a-double-reversal/) |
| 2442 | Medium | [Count Number of Distinct Integers After Reverse Operations](../2442-count-number-of-distinct-integers-after-reverse-operations/readme.md) | [link](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
