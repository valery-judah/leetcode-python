# 0191. Number of 1 Bits

## Quick Facts

- URL: [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- Function: `hammingWeight`
- Signature: `(n: int)  -> int`
- Primary pattern: **Bit Manipulation**

## Constraints

- `1 <= n <= 2^31 - 1`

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
- Run: `pytest -q -k "0191"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                     | LeetCode                                                                                                                              |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| 0190   | Easy       | [Reverse Bits](../0190-reverse-bits/readme.md)                                                                           | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                                                           |
| 0231   | Easy       | [Power of Two](../0231-power-of-two/readme.md)                                                                           | [Power of Two](https://leetcode.com/problems/power-of-two/)                                                                           |
| 0338   | Easy       | [Counting Bits](../0338-counting-bits/readme.md)                                                                         | [Counting Bits](https://leetcode.com/problems/counting-bits/)                                                                         |
| 0401   | Easy       | [Binary Watch](../0401-binary-watch/readme.md)                                                                           | [Binary Watch](https://leetcode.com/problems/binary-watch/)                                                                           |
| 0461   | Easy       | [Hamming Distance](../0461-hamming-distance/readme.md)                                                                   | [Hamming Distance](https://leetcode.com/problems/hamming-distance/)                                                                   |
| 0693   | Easy       | [Binary Number with Alternating Bits](../0693-binary-number-with-alternating-bits/readme.md)                             | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/)                             |
| 0762   | Easy       | [Prime Number of Set Bits in Binary Representation](../0762-prime-number-of-set-bits-in-binary-representation/readme.md) | [Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) |
| 3280   | Easy       | [Convert Date to Binary](../3280-convert-date-to-binary/readme.md)                                                       | [Convert Date to Binary](https://leetcode.com/problems/convert-date-to-binary/)                                                       |

## Examples

None

## References

- LeetCode problem and editorial links
