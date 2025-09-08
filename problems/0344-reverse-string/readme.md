# 0344. Reverse String

## Quick Facts

- URL: [Reverse String](https://leetcode.com/problems/reverse-string/)
- Function: `reverseString`
- Signature: `(s: list[str])  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 10^5`
- `s[i] is a printable ascii character.`

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
- Run: `pytest -q -k "0344"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0345 | Easy | [Reverse Vowels of a String](../0345-reverse-vowels-of-a-string/readme.md) | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) |
| 0541 | Easy | [Reverse String II](../0541-reverse-string-ii/readme.md) | [Reverse String II](https://leetcode.com/problems/reverse-string-ii/) |

## Examples

### Example 1

```text
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

### Example 2

```text
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## References

- LeetCode problem and editorial links
