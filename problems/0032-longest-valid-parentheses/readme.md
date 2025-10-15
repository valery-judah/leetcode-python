# 0032. Longest Valid Parentheses

## Quick Facts

- URL: [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
- Function: `longestValidParentheses`
- Signature: `(s: str)  -> int`
- Primary pattern: **Stack**

## Constraints

- `0 <= s.length <= 3 * 10^4`
- `s[i] is '(', or ')'.`

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
- Run: `pytest -q -k "0032"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                     | LeetCode                                                              |
| ------ | ---------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| 0020   | Easy       | [Valid Parentheses](../0020-valid-parentheses/readme.md) | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |

## Examples

### Example 1

```text
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

### Example 2

```text
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

### Example 3

```text
Input: s = ""
Output: 0
```

## References

- LeetCode problem and editorial links
