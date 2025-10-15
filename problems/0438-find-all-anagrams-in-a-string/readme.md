# 0438. Find All Anagrams in a String

## Quick Facts

- URL: [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- Function: `findAnagrams`
- Signature: `(s: str, p: str)  -> list[int]`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s and p consist of lowercase English letters.`

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
- Run: `pytest -q -k "0438"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                             | LeetCode                                                                      |
| ------ | ---------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 0242   | Easy       | [Valid Anagram](../0242-valid-anagram/readme.md)                 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                 |
| 0567   | Medium     | [Permutation in String](../0567-permutation-in-string/readme.md) | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) |

## Examples

### Example 1

```text
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

### Example 2

```text
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## References

- LeetCode problem and editorial links
