# 0186. Reverse Words in a String II

## Quick Facts

- URL: [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
- Function: `reverseWords`
- Signature: `(s: list[str])  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 10^5`
- `s[i] is an English letter (uppercase or lowercase), digit, or space ' '.`
- `There is at least one word in s.`
- `s does not contain leading or trailing spaces.`
- `All the words in s are guaranteed to be separated by a single space.`

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
- Run: `pytest -q -k "0186"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                     | LeetCode                                                                              |
| ------ | ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| 0151   | Medium     | [Reverse Words in a String](../0151-reverse-words-in-a-string/readme.md) | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) |
| 0189   | Medium     | [Rotate Array](../0189-rotate-array/readme.md)                           | [Rotate Array](https://leetcode.com/problems/rotate-array/)                           |

## Examples

### Example 1

```text
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
```

### Example 2

```text
Input: s = ["a"]
Output: ["a"]
```

## References

- LeetCode problem and editorial links
