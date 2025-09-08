# 0647. Palindromic Substrings

## Quick Facts

- URL: [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- Function: `countSubstrings`
- Signature: `(s: str)  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 1000`
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
- Run: `pytest -q -k "0647"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0005 | Medium | [Longest Palindromic Substring](../0005-longest-palindromic-substring/readme.md) | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |
| 0516 | Medium | [Longest Palindromic Subsequence](../0516-longest-palindromic-subsequence/readme.md) | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) |

## Examples

### Example 1

```text
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

### Example 2

```text
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## References

- LeetCode problem and editorial links
