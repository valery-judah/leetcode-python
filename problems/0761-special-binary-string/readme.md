# 0761. Special Binary String

## Quick Facts

- URL: [Special Binary String](https://leetcode.com/problems/special-binary-string/)
- Function: `makeLargestSpecial`
- Signature: `(s: str)  -> str`
- Primary pattern: **String**

## Constraints

- `1 <= s.length <= 50`
- `s[i] is either '0' or '1'.`
- `s is a special binary string.`

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
- Run: `pytest -q -k "0761"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0678 | Medium | [Valid Parenthesis String](../0678-valid-parenthesis-string/readme.md) | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) |
| 2533 | Medium | [Number of Good Binary Strings](../2533-number-of-good-binary-strings/readme.md) | [Number of Good Binary Strings](https://leetcode.com/problems/number-of-good-binary-strings/) |

## Examples

### Example 1

```text
Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
```

### Example 2

```text
Input: s = "10"
Output: "10"
```

## References

- LeetCode problem and editorial links
