# 0190. Reverse Bits

## Quick Facts

- URL: https://leetcode.com/problems/reverse-bits/
- Signature: `n: int` → `int`
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
- Run: `pytest -q -k "0190"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0007 | Medium | [Reverse Integer](../0007-reverse-integer/readme.md) | [link](https://leetcode.com/problems/reverse-integer/) |
| 0191 | Easy | [Number of 1 Bits](../0191-number-of-1-bits/readme.md) | [link](https://leetcode.com/problems/number-of-1-bits/) |
| 2119 | Easy | [A Number After a Double Reversal](../2119-a-number-after-a-double-reversal/readme.md) | [link](https://leetcode.com/problems/a-number-after-a-double-reversal/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
