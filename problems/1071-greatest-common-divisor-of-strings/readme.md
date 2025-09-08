# 1071. Greatest Common Divisor of Strings

## Quick Facts

- URL: [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
- Function: `gcdOfStrings`
- Signature: `(str1: str, str2: str)  -> str`
- Primary pattern: **Math**

## Constraints

- `1 <= str1.length, str2.length <= 1000`
- `str1 and str2 consist of English uppercase letters.`

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
- Run: `pytest -q -k "1071"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1979 | Easy | [Find Greatest Common Divisor of Array](../1979-find-greatest-common-divisor-of-array/readme.md) | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |
| 2413 | Easy | [Smallest Even Multiple](../2413-smallest-even-multiple/readme.md) | [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) |
| 3334 | Medium | [Find the Maximum Factor Score of Array](../3334-find-the-maximum-factor-score-of-array/readme.md) | [Find the Maximum Factor Score of Array](https://leetcode.com/problems/find-the-maximum-factor-score-of-array/) |

## Examples

### Example 1

```text
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

### Example 2

```text
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

### Example 3

```text
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

## References

- LeetCode problem and editorial links
