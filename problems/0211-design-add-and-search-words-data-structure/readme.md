# 0211. Design Add and Search Words Data Structure

## Quick Facts

- URL:
  [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- Function: \`\`
- Signature: `()  -> bool`
- Primary pattern: **String**

## Constraints

- `1 <= word.length <= 25`
- `word in addWord consists of lowercase English letters.`
- `word in search consist of '.' or lowercase English letters.`
- `There will be at most 2 dots in word for search queries.`
- `At most 10^4 calls will be made to addWord and search.`

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
- Run: `pytest -q -k "0211"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                     | LeetCode                                                                                              |
| ------ | ---------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 0208   | Medium     | [Implement Trie (Prefix Tree)](../0208-implement-trie-prefix-tree/readme.md)             | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)             |
| 0745   | Hard       | [Prefix and Suffix Search](../0745-prefix-and-suffix-search/readme.md)                   | [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)                   |
| 2301   | Hard       | [Match Substring After Replacement](../2301-match-substring-after-replacement/readme.md) | [Match Substring After Replacement](https://leetcode.com/problems/match-substring-after-replacement/) |
| 2416   | Hard       | [Sum of Prefix Scores of Strings](../2416-sum-of-prefix-scores-of-strings/readme.md)     | [Sum of Prefix Scores of Strings](https://leetcode.com/problems/sum-of-prefix-scores-of-strings/)     |
| 3045   | Hard       | [Count Prefix and Suffix Pairs II](../3045-count-prefix-and-suffix-pairs-ii/readme.md)   | [Count Prefix and Suffix Pairs II](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/)   |
| 3042   | Easy       | [Count Prefix and Suffix Pairs I](../3042-count-prefix-and-suffix-pairs-i/readme.md)     | [Count Prefix and Suffix Pairs I](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/)     |

## Examples

### Example 1

```text
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## References

- LeetCode problem and editorial links
