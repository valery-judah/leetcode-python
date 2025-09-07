# 0439. Ternary Expression Parser

## Quick Facts

- URL: [Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser/)
- Function: `parseTernary`
- Signature: `(expression: str)  -> str`
- Primary pattern: **Stack**

## Constraints

- `5 <= expression.length <= 10^4`
- `expression consists of digits, 'T', 'F', '?', and ':'.`
- `It is guaranteed that expression is a valid ternary expression and that each number is a one-digit number.`

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
- Run: `pytest -q -k "0439"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0385 | Medium | [Mini Parser](../0385-mini-parser/readme.md) | [Mini Parser](https://leetcode.com/problems/mini-parser/) |
| 0722 | Medium | [Remove Comments](../0722-remove-comments/readme.md) | [Remove Comments](https://leetcode.com/problems/remove-comments/) |
| 0736 | Hard | [Parse Lisp Expression](../0736-parse-lisp-expression/readme.md) | [Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/) |

## Examples

### Example 1

```text
Input: expression = "T?2:3"
Output: "2"
Explanation: If true, then result is 2; otherwise result is 3.
```

### Example 2

```text
Input: expression = "F?1:T?4:5"
Output: "4"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
```

### Example 3

```text
Input: expression = "T?T?F:5:3"
Output: "F"
Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
```

## References

- LeetCode problem and editorial links
