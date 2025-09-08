# 0516. Longest Palindromic Subsequence

## Quick Facts

- URL: [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- Function: `longestPalindromeSubseq`
- Signature: `(s: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= s.length <= 1000`
- `s consists only of lowercase English letters.`

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
- Run: `pytest -q -k "0516"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0005 | Medium | [Longest Palindromic Substring](../0005-longest-palindromic-substring/readme.md) | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |
| 0647 | Medium | [Palindromic Substrings](../0647-palindromic-substrings/readme.md) | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) |
| 0730 | Hard | [Count Different Palindromic Subsequences](../0730-count-different-palindromic-subsequences/readme.md) | [Count Different Palindromic Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/) |
| 1143 | Medium | [Longest Common Subsequence](../1143-longest-common-subsequence/readme.md) | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) |
| 1682 | Medium | [Longest Palindromic Subsequence II](../1682-longest-palindromic-subsequence-ii/readme.md) | [Longest Palindromic Subsequence II](https://leetcode.com/problems/longest-palindromic-subsequence-ii/) |
| 1771 | Hard | [Maximize Palindrome Length From Subsequences](../1771-maximize-palindrome-length-from-subsequences/readme.md) | [Maximize Palindrome Length From Subsequences](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) |
| 2002 | Medium | [Maximum Product of the Length of Two Palindromic Subsequences](../2002-maximum-product-of-the-length-of-two-palindromic-subsequences/readme.md) | [Maximum Product of the Length of Two Palindromic Subsequences](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/) |

## Examples

### Example 1

```text
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

### Example 2

```text
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
```

## References

- LeetCode problem and editorial links
