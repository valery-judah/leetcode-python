# 0049. Group Anagrams

## Quick Facts

- URL: [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- Function: `groupAnagrams`
- Signature: `(strs: list[str])  -> list[list[str]]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i] consists of lowercase English letters.`

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
- Run: `pytest -q -k "0049"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0242 | Easy | [Valid Anagram](../0242-valid-anagram/readme.md) | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |
| 0249 | Medium | [Group Shifted Strings](../0249-group-shifted-strings/readme.md) | [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) |
| 2273 | Easy | [Find Resultant Array After Removing Anagrams](../2273-find-resultant-array-after-removing-anagrams/readme.md) | [Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) |
| 2514 | Hard | [Count Anagrams](../2514-count-anagrams/readme.md) | [Count Anagrams](https://leetcode.com/problems/count-anagrams/) |

## Examples

None

## References

- LeetCode problem and editorial links
