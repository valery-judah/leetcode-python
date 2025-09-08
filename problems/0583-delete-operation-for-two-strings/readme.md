# 0583. Delete Operation for Two Strings

## Quick Facts

- URL: [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
- Function: `minDistance`
- Signature: `(word1: str, word2: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= word1.length, word2.length <= 500`
- `word1 and word2 consist of only lowercase English letters.`

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
- Run: `pytest -q -k "0583"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0072 | Medium | [Edit Distance](../0072-edit-distance/readme.md) | [Edit Distance](https://leetcode.com/problems/edit-distance/) |
| 0712 | Medium | [Minimum ASCII Delete Sum for Two Strings](../0712-minimum-ascii-delete-sum-for-two-strings/readme.md) | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |
| 1143 | Medium | [Longest Common Subsequence](../1143-longest-common-subsequence/readme.md) | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) |
| 2937 | Easy | [Make Three Strings Equal](../2937-make-three-strings-equal/readme.md) | [Make Three Strings Equal](https://leetcode.com/problems/make-three-strings-equal/) |

## Examples

### Example 1

```text
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```

### Example 2

```text
Input: word1 = "leetcode", word2 = "etco"
Output: 4
```

## References

- LeetCode problem and editorial links
