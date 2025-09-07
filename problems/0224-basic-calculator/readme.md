# 0224. Basic Calculator

## Quick Facts

- URL: [Basic Calculator](https://leetcode.com/problems/basic-calculator/)
- Function: `calculate`
- Signature: `(s: str)  -> int`
- Primary pattern: **Stack**

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s consists of digits, '+', '-', '(', ')', and ' '.`
- `s represents a valid expression.`
- `'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).`
- `'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).`
- `There will be no two consecutive operators in the input.`
- `Every number and running calculation will fit in a signed 32-bit integer.`

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
- Run: `pytest -q -k "0224"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0150 | Medium | [Evaluate Reverse Polish Notation](../0150-evaluate-reverse-polish-notation/readme.md) | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |
| 0227 | Medium | [Basic Calculator II](../0227-basic-calculator-ii/readme.md) | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) |
| 0241 | Medium | [Different Ways to Add Parentheses](../0241-different-ways-to-add-parentheses/readme.md) | [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) |
| 0282 | Hard | [Expression Add Operators](../0282-expression-add-operators/readme.md) | [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) |
| 0785 | Hard | [Basic Calculator III](../0785-basic-calculator-iii/readme.md) | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) |
| 2019 | Hard | [The Score of Students Solving Math Expression](../2019-the-score-of-students-solving-math-expression/readme.md) | [The Score of Students Solving Math Expression](https://leetcode.com/problems/the-score-of-students-solving-math-expression/) |
| 2232 | Medium | [Minimize Result by Adding Parentheses to Expression](../2232-minimize-result-by-adding-parentheses-to-expression/readme.md) | [Minimize Result by Adding Parentheses to Expression](https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/) |

## Examples

### Example 1

```text
Input: s = "1 + 1"
Output: 2
```

### Example 2

```text
Input: s = " 2-1 + 2 "
Output: 3
```

### Example 3

```text
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## References

- LeetCode problem and editorial links
