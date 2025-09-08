# 0734. Sentence Similarity

## Quick Facts

- URL: [Sentence Similarity](https://leetcode.com/problems/sentence-similarity/)
- Function: `areSentencesSimilar`
- Signature: `(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]])  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= sentence1.length, sentence2.length <= 1000`
- `1 <= sentence1[i].length, sentence2[i].length <= 20`
- `sentence1[i] and sentence2[i] consist of English letters.`
- `0 <= similarPairs.length <= 1000`
- `similarPairs[i].length == 2`
- `1 <= xi.length, yi.length <= 20`
- `xi and yi consist of lower-case and upper-case English letters.`
- `All the pairs (xi, yi) are distinct.`

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
- Run: `pytest -q -k "0734"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0547 | Medium | [Number of Provinces](../0547-number-of-provinces/readme.md) | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) |
| 0721 | Medium | [Accounts Merge](../0721-accounts-merge/readme.md) | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) |
| 0737 | Medium | [Sentence Similarity II](../0737-sentence-similarity-ii/readme.md) | [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/) |

## Examples

### Example 1

```text
Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
```

### Example 2

```text
Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
Output: true
Explanation: A word is similar to itself.
```

### Example 3

```text
Input: sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
Output: false
Explanation: As they don't have the same length, we return false.
```

## References

- LeetCode problem and editorial links
