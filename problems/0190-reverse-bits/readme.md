# 0190. Reverse Bits

## Quick Facts

- URL: [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- Function: `reverseBits`
- Signature: `(n: int)  -> int`
- Primary pattern: **Bit Manipulation**

## Constraints

- `0 <= n <= 2^31 - 2`
- `n is even.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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

| Number | Difficulty | Name                                                                                   | LeetCode                                                                                            |
| ------ | ---------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 0007   | Medium     | [Reverse Integer](../0007-reverse-integer/readme.md)                                   | [Reverse Integer](https://leetcode.com/problems/reverse-integer/)                                   |
| 0191   | Easy       | [Number of 1 Bits](../0191-number-of-1-bits/readme.md)                                 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)                                 |
| 2119   | Easy       | [A Number After a Double Reversal](../2119-a-number-after-a-double-reversal/readme.md) | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) |

## Examples

None

## References

- LeetCode problem and editorial links
