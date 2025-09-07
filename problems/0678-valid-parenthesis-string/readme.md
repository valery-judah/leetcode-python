# 0678. Valid Parenthesis String

## Quick Facts

- URL: [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)
- Function: `checkValidString`
- Signature: `(s: str)  -> bool`
- Primary pattern: **Stack**

## Constraints

- `1 <= s.length <= 100`
- `s[i] is '(', ')' or '*'.`

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
- Run: `pytest -q -k "0678"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0763 | Hard | [Special Binary String](../0763-special-binary-string/readme.md) | [Special Binary String](https://leetcode.com/problems/special-binary-string/) |
| 2221 | Medium | [Check if a Parentheses String Can Be Valid](../2221-check-if-a-parentheses-string-can-be-valid/readme.md) | [Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) |

## Examples

### Example 1

```text
Input: s = "()"
Output: true
```

### Example 2

```text
Input: s = "(*)"
Output: true
```

### Example 3

```text
Input: s = "(*))"
Output: true
```

## References

- LeetCode problem and editorial links
