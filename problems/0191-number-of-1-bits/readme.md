# 0191. Number of 1 Bits

## Quick Facts

- URL: https://leetcode.com/problems/number-of-1-bits/
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
- Run: `pytest -q -k "0191"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0190 | Easy | [Reverse Bits](../0190-reverse-bits/readme.md) | [link](https://leetcode.com/problems/reverse-bits/) |
| 0231 | Easy | [Power of Two](../0231-power-of-two/readme.md) | [link](https://leetcode.com/problems/power-of-two/) |
| 0338 | Easy | [Counting Bits](../0338-counting-bits/readme.md) | [link](https://leetcode.com/problems/counting-bits/) |
| 0401 | Easy | [Binary Watch](../0401-binary-watch/readme.md) | [link](https://leetcode.com/problems/binary-watch/) |
| 0461 | Easy | [Hamming Distance](../0461-hamming-distance/readme.md) | [link](https://leetcode.com/problems/hamming-distance/) |
| 0693 | Easy | [Binary Number with Alternating Bits](../0693-binary-number-with-alternating-bits/readme.md) | [link](https://leetcode.com/problems/binary-number-with-alternating-bits/) |
| 0762 | Easy | [Prime Number of Set Bits in Binary Representation](../0762-prime-number-of-set-bits-in-binary-representation/readme.md) | [link](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) |
| 3280 | Easy | [Convert Date to Binary](../3280-convert-date-to-binary/readme.md) | [link](https://leetcode.com/problems/convert-date-to-binary/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
