# 0392. Is Subsequence

## Quick Facts

- URL: [Is Subsequence](https://leetcode.com/problems/is-subsequence/)
- Function: `isSubsequence`
- Signature: `(s: str, t: str)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s and t consist only of lowercase English letters.`

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
- Run: `pytest -q -k "0392"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                     | LeetCode                                                                                                                              |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| 0792   | Medium     | [Number of Matching Subsequences](../0792-number-of-matching-subsequences/readme.md)                                     | [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)                                     |
| 1055   | Medium     | [Shortest Way to Form String](../1055-shortest-way-to-form-string/readme.md)                                             | [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/)                                             |
| 2486   | Medium     | [Append Characters to String to Make Subsequence](../2486-append-characters-to-string-to-make-subsequence/readme.md)     | [Append Characters to String to Make Subsequence](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/)     |
| 2825   | Medium     | [Make String a Subsequence Using Cyclic Increments](../2825-make-string-a-subsequence-using-cyclic-increments/readme.md) | [Make String a Subsequence Using Cyclic Increments](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/) |

## Examples

### Example 1

```text
Input: s = "abc", t = "ahbgdc"
Output: true
```

### Example 2

```text
Input: s = "axc", t = "ahbgdc"
Output: false
```

## References

- LeetCode problem and editorial links
