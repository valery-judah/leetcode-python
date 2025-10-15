# 0249. Group Shifted Strings

## Quick Facts

- URL: [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/)
- Function: `groupStrings`
- Signature: `(strings: list[str])  -> list[list[str]]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= strings.length <= 200`
- `1 <= strings[i].length <= 50`
- `strings[i] consists of lowercase English letters.`

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
- Run: `pytest -q -k "0249"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                         | LeetCode                                                                                                  |
| ------ | ---------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 0049   | Medium     | [Group Anagrams](../0049-group-anagrams/readme.md)                                           | [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                                           |
| 2744   | Easy       | [Find Maximum Number of String Pairs](../2744-find-maximum-number-of-string-pairs/readme.md) | [Find Maximum Number of String Pairs](https://leetcode.com/problems/find-maximum-number-of-string-pairs/) |

## Examples

None

## References

- LeetCode problem and editorial links
