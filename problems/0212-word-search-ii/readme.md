# 0212. Word Search II

## Quick Facts

- URL: [Word Search II](https://leetcode.com/problems/word-search-ii/)
- Function: `findWords`
- Signature: `(board: list[list[str]], words: list[str])  -> list[str]`
- Primary pattern: **Backtracking**

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j] is a lowercase English letter.`
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i] consists of lowercase English letters.`
- `All the strings of words are unique.`

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
- Run: `pytest -q -k "0212"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                         | LeetCode                                                                                  |
| ------ | ---------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 0079   | Medium     | [Word Search](../0079-word-search/readme.md)                                 | [Word Search](https://leetcode.com/problems/word-search/)                                 |
| 0980   | Hard       | [Unique Paths III](../0980-unique-paths-iii/readme.md)                       | [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)                       |
| 2227   | Hard       | [Encrypt and Decrypt Strings](../2227-encrypt-and-decrypt-strings/readme.md) | [Encrypt and Decrypt Strings](https://leetcode.com/problems/encrypt-and-decrypt-strings/) |

## Examples

### Example 1

```text
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

### Example 2

```text
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## References

- LeetCode problem and editorial links
