# 0013. Roman to Integer

## Quick Facts

- URL: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- Function: `romanToInt`
- Signature: `(s: str)  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= s.length <= 15`
- `s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').`
- `It is guaranteed that s is a valid roman numeral in the range [1, 3999].`

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
- Run: `pytest -q -k "0013"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                   | LeetCode                                                            |
| ------ | ---------- | ------------------------------------------------------ | ------------------------------------------------------------------- |
| 0012   | Medium     | [Integer to Roman](../0012-integer-to-roman/readme.md) | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) |

## Examples

### Example 1

```text
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

### Example 2

```text
Input: s = "III"
Output: 3
Explanation: III = 3.
```

### Example 3

```text
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

### Example 4

```text
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## References

- LeetCode problem and editorial links
