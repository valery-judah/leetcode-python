# 0012. Integer to Roman

## Quick Facts

- URL: [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- Function: `intToRoman`
- Signature: `(num: int)  -> str`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= num <= 3999`

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
- Run: `pytest -q -k "0012"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0013 | Easy | [Roman to Integer](../0013-roman-to-integer/readme.md) | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) |
| 0273 | Hard | [Integer to English Words](../0273-integer-to-english-words/readme.md) | [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) |

## Examples

### Example 1

```text
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
```

### Example 2

```text
50 = L
 8 = VIII
```

### Example 3

```text
1000 = M
 900 = CM
  90 = XC
   4 = IV
```

## References

- LeetCode problem and editorial links
