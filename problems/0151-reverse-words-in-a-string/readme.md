# 0151. Reverse Words in a String

## Quick Facts

- URL: [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- Function: `reverseWords`
- Signature: `(s: str)  -> str`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 10^4`
- `s contains English letters (upper-case and lower-case), digits, and spaces ' '.`
- `There is at least one word in s.`

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
- Run: `pytest -q -k "0151"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                           | LeetCode                                                                                    |
| ------ | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0186   | Medium     | [Reverse Words in a String II](../0186-reverse-words-in-a-string-ii/readme.md) | [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) |

## Examples

### Example 1

```text
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2

```text
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

### Example 3

```text
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

## References

- LeetCode problem and editorial links
