# 0680. Valid Palindrome II

## Quick Facts

- URL: [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- Function: `validPalindrome`
- Signature: `(s: str)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 10^5`
- `s consists of lowercase English letters.`

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
- Run: `pytest -q -k "0680"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0125 | Easy | [Valid Palindrome](../0125-valid-palindrome/readme.md) | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |
| 1216 | Hard | [Valid Palindrome III](../1216-valid-palindrome-iii/readme.md) | [Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/) |
| 2330 | Medium | [Valid Palindrome IV](../2330-valid-palindrome-iv/readme.md) | [Valid Palindrome IV](https://leetcode.com/problems/valid-palindrome-iv/) |

## Examples

### Example 1

```text
Input: s = "aba"
Output: true
```

### Example 2

```text
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

### Example 3

```text
Input: s = "abc"
Output: false
```

## References

- LeetCode problem and editorial links
