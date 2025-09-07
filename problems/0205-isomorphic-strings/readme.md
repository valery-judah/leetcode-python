# 0205. Isomorphic Strings

## Quick Facts

- URL: [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
- Function: `isIsomorphic`
- Signature: `(s: str, t: str)  -> bool`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s and t consist of any valid ascii character.`

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
- Run: `pytest -q -k "0205"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0290 | Easy | [Word Pattern](../0290-word-pattern/readme.md) | [Word Pattern](https://leetcode.com/problems/word-pattern/) |
| 0890 | Medium | [Find and Replace Pattern](../0890-find-and-replace-pattern/readme.md) | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) |

## Examples

None

## References

- LeetCode problem and editorial links
