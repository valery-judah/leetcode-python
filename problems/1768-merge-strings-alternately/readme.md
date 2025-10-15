# 1768. Merge Strings Alternately

## Quick Facts

- URL: [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)
- Function: `mergeAlternately`
- Signature: `(word1: str, word2: str)  -> str`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= word1.length, word2.length <= 100`
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
- Run: `pytest -q -k "1768"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                               | LeetCode                                                                                                        |
| ------ | ---------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 0281   | Medium     | [Zigzag Iterator](../0281-zigzag-iterator/readme.md)                                               | [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/)                                               |
| 2645   | Medium     | [Minimum Additions to Make Valid String](../2645-minimum-additions-to-make-valid-string/readme.md) | [Minimum Additions to Make Valid String](https://leetcode.com/problems/minimum-additions-to-make-valid-string/) |

## Examples

### Example 1

```text
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

### Example 2

```text
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
```

### Example 3

```text
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
```

## References

- LeetCode problem and editorial links
