# 0007. Reverse Integer

## Quick Facts

- URL: [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- Function: `reverse`
- Signature: `(x: int)  -> int`
- Primary pattern: **Math**

## Constraints

- `-2^31 <= x <= 2^31 - 1`

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
- Run: `pytest -q -k "0007"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                                       | LeetCode                                                                                                                                                |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0008   | Medium     | [String to Integer (atoi)](../0008-string-to-integer-atoi/readme.md)                                                                       | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)                                                                       |
| 0190   | Easy       | [Reverse Bits](../0190-reverse-bits/readme.md)                                                                                             | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                                                                             |
| 2119   | Easy       | [A Number After a Double Reversal](../2119-a-number-after-a-double-reversal/readme.md)                                                     | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/)                                                     |
| 2442   | Medium     | [Count Number of Distinct Integers After Reverse Operations](../2442-count-number-of-distinct-integers-after-reverse-operations/readme.md) | [Count Number of Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) |

## Examples

### Example 1

```text
Input: x = 123
Output: 321
```

### Example 2

```text
Input: x = -123
Output: -321
```

### Example 3

```text
Input: x = 120
Output: 21
```

## References

- LeetCode problem and editorial links
