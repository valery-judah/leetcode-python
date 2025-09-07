# 0772. Basic Calculator III

## Quick Facts

- URL: [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
- Function: `calculate`
- Signature: `(s: str)  -> int`
- Primary pattern: **Stack**

## Constraints

- `1 <= s <= 10^4`
- `s consists of digits, '+', '-', '*', '/', '(', and ')'.`
- `s is a valid expression.`

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
- Run: `pytest -q -k "0772"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0224 | Hard | [Basic Calculator](../0224-basic-calculator/readme.md) | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) |
| 0227 | Medium | [Basic Calculator II](../0227-basic-calculator-ii/readme.md) | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) |
| 0770 | Hard | [Basic Calculator IV](../0770-basic-calculator-iv/readme.md) | [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) |
| 1597 | Hard | [Build Binary Expression Tree From Infix Expression](../1597-build-binary-expression-tree-from-infix-expression/readme.md) | [Build Binary Expression Tree From Infix Expression](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/) |

## Examples

### Example 1

```text
Input: s = "1+1"
Output: 2
```

### Example 2

```text
Input: s = "6-4/2"
Output: 4
```

### Example 3

```text
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

## References

- LeetCode problem and editorial links
