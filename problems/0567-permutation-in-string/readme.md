# 0567. Permutation in String

## Quick Facts

- URL: [Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- Function: `checkInclusion`
- Signature: `(s1: str, s2: str)  -> bool`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1 and s2 consist of lowercase English letters.`

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
- Run: `pytest -q -k "0567"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                             | LeetCode                                                                                      |
| ------ | ---------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 0076   | Hard       | [Minimum Window Substring](../0076-minimum-window-substring/readme.md)           | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)           |
| 0438   | Medium     | [Find All Anagrams in a String](../0438-find-all-anagrams-in-a-string/readme.md) | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |

## Examples

### Example 1

```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2

```text
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## References

- LeetCode problem and editorial links
