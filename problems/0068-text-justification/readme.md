# 0068. Text Justification

## Quick Facts

- URL: [Text Justification](https://leetcode.com/problems/text-justification/)
- Function: `fullJustify`
- Signature: `(words: list[str], maxWidth: int)  -> list[str]`
- Primary pattern: **Array**

## Constraints

- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i] consists of only English letters and symbols.`
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`

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
- Run: `pytest -q -k "0068"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1592 | Easy | [Rearrange Spaces Between Words](../1592-rearrange-spaces-between-words/readme.md) | [Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) |
| 2138 | Easy | [Divide a String Into Groups of Size k](../2138-divide-a-string-into-groups-of-size-k/readme.md) | [Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/) |
| 2468 | Hard | [Split Message Based on Limit](../2468-split-message-based-on-limit/readme.md) | [Split Message Based on Limit](https://leetcode.com/problems/split-message-based-on-limit/) |

## Examples

### Example 1

```text
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

### Example 2

```text
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

### Example 3

```text
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

## References

- LeetCode problem and editorial links
