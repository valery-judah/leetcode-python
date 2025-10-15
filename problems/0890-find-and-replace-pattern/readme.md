# 0890. Find and Replace Pattern

## Quick Facts

- URL: [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)
- Function: `findAndReplacePattern`
- Signature: `(words: list[str], pattern: str)  -> list[str]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= pattern.length <= 20`
- `1 <= words.length <= 50`
- `words[i].length == pattern.length`
- `pattern and words[i] are lowercase English letters.`

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
- Run: `pytest -q -k "0890"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                       | LeetCode                                                                |
| ------ | ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| 0205   | Easy       | [Isomorphic Strings](../0205-isomorphic-strings/readme.md) | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) |
| 0290   | Easy       | [Word Pattern](../0290-word-pattern/readme.md)             | [Word Pattern](https://leetcode.com/problems/word-pattern/)             |

## Examples

### Example 1

```text
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {{a -> m, b -> e, ...}}.
"ccc" does not match the pattern because {{a -> c, b -> c, ...}} is not a permutation, since a and b map to the same letter.
```

### Example 2

```text
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
```

## References

- LeetCode problem and editorial links
