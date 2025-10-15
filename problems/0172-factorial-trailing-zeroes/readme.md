# 0172. Factorial Trailing Zeroes

## Quick Facts

- URL: [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
- Function: `trailingZeroes`
- Signature: `(n: int)  -> int`
- Primary pattern: **Math**

## Constraints

- `0 <= n <= 10^4`

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
- Run: `pytest -q -k "0172"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                       | LeetCode                                                                                                                |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 0233   | Hard       | [Number of Digit One](../0233-number-of-digit-one/readme.md)                                               | [Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)                                               |
| 0793   | Hard       | [Preimage Size of Factorial Zeroes Function](../0793-preimage-size-of-factorial-zeroes-function/readme.md) | [Preimage Size of Factorial Zeroes Function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) |
| 2117   | Hard       | [Abbreviating the Product of a Range](../2117-abbreviating-the-product-of-a-range/readme.md)               | [Abbreviating the Product of a Range](https://leetcode.com/problems/abbreviating-the-product-of-a-range/)               |
| 2245   | Medium     | [Maximum Trailing Zeros in a Cornered Path](../2245-maximum-trailing-zeros-in-a-cornered-path/readme.md)   | [Maximum Trailing Zeros in a Cornered Path](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/)   |

## Examples

### Example 1

```text
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

### Example 2

```text
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

### Example 3

```text
Input: n = 0
Output: 0
```

## References

- LeetCode problem and editorial links
