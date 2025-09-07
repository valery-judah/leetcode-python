# 0266. Palindrome Permutation

## Quick Facts

- URL: [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)
- Function: `canPermutePalindrome`
- Signature: `(s: str)  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= s.length <= 5000`
- `s consists of only lowercase English letters.`

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
- Run: `pytest -q -k "0266"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0005 | Medium | [Longest Palindromic Substring](../0005-longest-palindromic-substring/readme.md) | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |
| 0242 | Easy | [Valid Anagram](../0242-valid-anagram/readme.md) | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |
| 0267 | Medium | [Palindrome Permutation II](../0267-palindrome-permutation-ii/readme.md) | [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/) |
| 0409 | Easy | [Longest Palindrome](../0409-longest-palindrome/readme.md) | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) |

## Examples

### Example 1

```text
Input: s = "code"
Output: false
```

### Example 2

```text
Input: s = "aab"
Output: true
```

### Example 3

```text
Input: s = "carerac"
Output: true
```

## References

- LeetCode problem and editorial links
