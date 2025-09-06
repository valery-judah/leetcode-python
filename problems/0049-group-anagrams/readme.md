# 0049. Group Anagrams

## Quick Facts

- URL: https://leetcode.com/problems/group-anagrams/
- Signature: `strs: list[str]` → `list[list[str]]`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
| 0242 | Easy | [Valid Anagram](../0242-valid-anagram/readme.md) | [link](https://leetcode.com/problems/valid-anagram/) |
| 0249 | Medium | [Group Shifted Strings](../0249-group-shifted-strings/readme.md) | [link](https://leetcode.com/problems/group-shifted-strings/) |
| 2273 | Easy | [Find Resultant Array After Removing Anagrams](../2273-find-resultant-array-after-removing-anagrams/readme.md) | [link](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) |
| 2514 | Hard | [Count Anagrams](../2514-count-anagrams/readme.md) | [link](https://leetcode.com/problems/count-anagrams/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
