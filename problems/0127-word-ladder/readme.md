# 0127. Word Ladder

## Quick Facts

- URL: [Word Ladder](https://leetcode.com/problems/word-ladder/)
- Function: `ladderLength`
- Signature: `(beginWord: str, endWord: str, wordList: list[str])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord, endWord, and wordList[i] consist of lowercase English letters.`
- `beginWord != endWord`
- `All the words in wordList are unique.`

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
- Run: `pytest -q -k "0127"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                           | LeetCode                                                                                                    |
| ------ | ---------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 0126   | Hard       | [Word Ladder II](../0126-word-ladder-ii/readme.md)                                             | [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)                                             |
| 0433   | Medium     | [Minimum Genetic Mutation](../0433-minimum-genetic-mutation/readme.md)                         | [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)                         |
| 2452   | Medium     | [Words Within Two Edits of Dictionary](../2452-words-within-two-edits-of-dictionary/readme.md) | [Words Within Two Edits of Dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/) |

## Examples

### Example 1

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
```

### Example 2

```text
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

## References

- LeetCode problem and editorial links
