# 0072. Edit Distance

## Quick Facts

- URL: [Edit Distance](https://leetcode.com/problems/edit-distance/)
- Function: `minDistance`
- Signature: `(word1: str, word2: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1 and word2 consist of lowercase English letters.`

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
- Run: `pytest -q -k "0072"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0161 | Medium | [One Edit Distance](../0161-one-edit-distance/readme.md) | [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) |
| 0583 | Medium | [Delete Operation for Two Strings](../0583-delete-operation-for-two-strings/readme.md) | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| 0712 | Medium | [Minimum ASCII Delete Sum for Two Strings](../0712-minimum-ascii-delete-sum-for-two-strings/readme.md) | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |
| 1105 | Medium | [Uncrossed Lines](../1105-uncrossed-lines/readme.md) | [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) |
| 2311 | Hard | [Minimum White Tiles After Covering With Carpets](../2311-minimum-white-tiles-after-covering-with-carpets/readme.md) | [Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/) |
| 3808 | Hard | [Longest Palindrome After Substring Concatenation II](../3808-longest-palindrome-after-substring-concatenation-ii/readme.md) | [Longest Palindrome After Substring Concatenation II](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/) |
| 3866 | Hard | [Minimum Steps to Convert String with Operations](../3866-minimum-steps-to-convert-string-with-operations/readme.md) | [Minimum Steps to Convert String with Operations](https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/) |

## Examples

### Example 1

```text
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

### Example 2

```text
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## References

- LeetCode problem and editorial links
