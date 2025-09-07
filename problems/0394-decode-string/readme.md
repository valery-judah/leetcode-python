# 0394. Decode String

## Quick Facts

- URL: [Decode String](https://leetcode.com/problems/decode-string/)
- Function: `decodeString`
- Signature: `(s: str)  -> str`
- Primary pattern: **Stack**

## Constraints

- `1 <= s.length <= 30`
- `s consists of lowercase English letters, digits, and square brackets '[]'.`
- `s is guaranteed to be a valid input.`
- `All the integers in s are in the range [1, 300].`

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
- Run: `pytest -q -k "0394"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0471 | Hard | [Encode String with Shortest Length](../0471-encode-string-with-shortest-length/readme.md) | [Encode String with Shortest Length](https://leetcode.com/problems/encode-string-with-shortest-length/) |
| 0726 | Hard | [Number of Atoms](../0726-number-of-atoms/readme.md) | [Number of Atoms](https://leetcode.com/problems/number-of-atoms/) |
| 1076 | Medium | [Brace Expansion](../1076-brace-expansion/readme.md) | [Brace Expansion](https://leetcode.com/problems/brace-expansion/) |

## Examples

### Example 1

```text
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

### Example 2

```text
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Example 3

```text
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## References

- LeetCode problem and editorial links
