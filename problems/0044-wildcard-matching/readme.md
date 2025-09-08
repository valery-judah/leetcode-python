# 0044. Wildcard Matching

## Quick Facts

- URL: [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
- Function: `isMatch`
- Signature: `(s: str, p: str)  -> bool`
- Primary pattern: **Greedy**

## Constraints

- `0 <= s.length, p.length <= 2000`
- `s contains only lowercase English letters.`
- `p contains only lowercase English letters, '?' or '*'.`

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
- Run: `pytest -q -k "0044"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0010 | Hard | [Regular Expression Matching](../0010-regular-expression-matching/readme.md) | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) |
| 3407 | Easy | [Substring Matching Pattern](../3407-substring-matching-pattern/readme.md) | [Substring Matching Pattern](https://leetcode.com/problems/substring-matching-pattern/) |

## Examples

### Example 1

```text
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2

```text
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

### Example 3

```text
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

## References

- LeetCode problem and editorial links
