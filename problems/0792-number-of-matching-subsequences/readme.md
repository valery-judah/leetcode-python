# 0792. Number of Matching Subsequences

## Quick Facts

- URL: [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)
- Function: `numMatchingSubseq`
- Signature: `(s: str, words: list[str])  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 50`
- `s and words[i] consist of only lowercase English letters.`

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
- Run: `pytest -q -k "0792"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0392 | Easy | [Is Subsequence](../0392-is-subsequence/readme.md) | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) |
| 1055 | Medium | [Shortest Way to Form String](../1055-shortest-way-to-form-string/readme.md) | [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/) |
| 2062 | Easy | [Count Vowel Substrings of a String](../2062-count-vowel-substrings-of-a-string/readme.md) | [Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/) |

## Examples

### Example 1

```text
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
```

### Example 2

```text
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```

## References

- LeetCode problem and editorial links
