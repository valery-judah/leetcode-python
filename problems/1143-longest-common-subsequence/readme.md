# 1143. Longest Common Subsequence

## Quick Facts

- URL: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- Function: `longestCommonSubsequence`
- Signature: `(text1: str, text2: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1 and text2 consist of only lowercase English characters.`

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
- Run: `pytest -q -k "1143"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                         | LeetCode                                                                                                                  |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 0516   | Medium     | [Longest Palindromic Subsequence](../0516-longest-palindromic-subsequence/readme.md)                         | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)                         |
| 0583   | Medium     | [Delete Operation for Two Strings](../0583-delete-operation-for-two-strings/readme.md)                       | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)                       |
| 1092   | Hard       | [Shortest Common Supersequence](../1092-shortest-common-supersequence/readme.md)                             | [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)                             |
| 2207   | Medium     | [Maximize Number of Subsequences in a String](../2207-maximize-number-of-subsequences-in-a-string/readme.md) | [Maximize Number of Subsequences in a String](https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/) |
| 2565   | Hard       | [Subsequence With the Minimum Score](../2565-subsequence-with-the-minimum-score/readme.md)                   | [Subsequence With the Minimum Score](https://leetcode.com/problems/subsequence-with-the-minimum-score/)                   |

## Examples

### Example 1

```text
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

### Example 2

```text
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

### Example 3

```text
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## References

- LeetCode problem and editorial links
