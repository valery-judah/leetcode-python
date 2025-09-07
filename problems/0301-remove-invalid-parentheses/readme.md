# 0301. Remove Invalid Parentheses

## Quick Facts

- URL: [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
- Function: `removeInvalidParentheses`
- Signature: `(s: str)  -> list[str]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= s.length <= 25`
- `s consists of lowercase English letters and parentheses '(' and ')'.`
- `There will be at most 20 parentheses in s.`

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
- Run: `pytest -q -k "0301"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0020 | Easy | [Valid Parentheses](../0020-valid-parentheses/readme.md) | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |
| 2095 | Medium | [Minimum Number of Swaps to Make the String Balanced](../2095-minimum-number-of-swaps-to-make-the-string-balanced/readme.md) | [Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) |

## Examples

### Example 1

```text
Input: s = "()())()"
Output: ["(())()","()()()"]
```

### Example 2

```text
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
```

### Example 3

```text
Input: s = ")("
Output: [""]
```

## References

- LeetCode problem and editorial links
