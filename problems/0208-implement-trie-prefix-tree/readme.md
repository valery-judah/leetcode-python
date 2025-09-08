# 0208. Implement Trie (Prefix Tree)

## Quick Facts

- URL: [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- Function: ``
- Signature: `()  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word and prefix consist only of lowercase English letters.`
- `At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.`

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
- Run: `pytest -q -k "0208"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0211 | Medium | [Design Add and Search Words Data Structure](../0211-design-add-and-search-words-data-structure/readme.md) | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |
| 0642 | Hard | [Design Search Autocomplete System](../0642-design-search-autocomplete-system/readme.md) | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) |
| 0648 | Medium | [Replace Words](../0648-replace-words/readme.md) | [Replace Words](https://leetcode.com/problems/replace-words/) |
| 0676 | Medium | [Implement Magic Dictionary](../0676-implement-magic-dictionary/readme.md) | [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) |
| 2227 | Hard | [Encrypt and Decrypt Strings](../2227-encrypt-and-decrypt-strings/readme.md) | [Encrypt and Decrypt Strings](https://leetcode.com/problems/encrypt-and-decrypt-strings/) |
| 1804 | Medium | [Implement Trie II (Prefix Tree)](../1804-implement-trie-ii-prefix-tree/readme.md) | [Implement Trie II (Prefix Tree)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/) |
| 3045 | Hard | [Count Prefix and Suffix Pairs II](../3045-count-prefix-and-suffix-pairs-ii/readme.md) | [Count Prefix and Suffix Pairs II](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/) |
| 3042 | Easy | [Count Prefix and Suffix Pairs I](../3042-count-prefix-and-suffix-pairs-i/readme.md) | [Count Prefix and Suffix Pairs I](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/) |

## Examples

### Example 1

```text
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## References

- LeetCode problem and editorial links
