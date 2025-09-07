# 0242. Valid Anagram

## Quick Facts

- URL: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- Function: `isAnagram`
- Signature: `(s: str, t: str)  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s and t consist of lowercase English letters.`

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
- Run: `pytest -q -k "0242"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0049 | Medium | [Group Anagrams](../0049-group-anagrams/readme.md) | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| 0266 | Easy | [Palindrome Permutation](../0266-palindrome-permutation/readme.md) | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) |
| 0438 | Medium | [Find All Anagrams in a String](../0438-find-all-anagrams-in-a-string/readme.md) | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |
| 2273 | Easy | [Find Resultant Array After Removing Anagrams](../2273-find-resultant-array-after-removing-anagrams/readme.md) | [Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) |

## Examples

None

## References

- LeetCode problem and editorial links
