# 0604. Design Compressed String Iterator

## Quick Facts

- URL: [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/)
- Function: \`\`
- Signature: `(inputs: list[int], inputs: list[int])  -> list[str]`
- Primary pattern: **Array**

## Constraints

- `1 <= compressedString.length <= 1000`
- `compressedString consists of lower-case an upper-case English letters and digits.`
- `The number of a single character repetitions in compressedString is in the range [1, 10^9]`
- `At most 100 calls will be made to next and hasNext.`

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
- Run: `pytest -q -k "0604"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                       | LeetCode                                                                |
| ------ | ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| 0146   | Medium     | [LRU Cache](../0146-lru-cache/readme.md)                   | [LRU Cache](https://leetcode.com/problems/lru-cache/)                   |
| 0443   | Medium     | [String Compression](../0443-string-compression/readme.md) | [String Compression](https://leetcode.com/problems/string-compression/) |

## Examples

### Example 1

```text
Input
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True
```

## References

- LeetCode problem and editorial links
