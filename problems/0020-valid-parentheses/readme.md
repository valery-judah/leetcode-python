# 0020. Valid Parentheses

## Quick Facts

- URL: https://leetcode.com/problems/valid-parentheses/
- Signature: `s: str` → `bool`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0020"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0022 | Medium | [Generate Parentheses](../0022-generate-parentheses/readme.md) | [link](https://leetcode.com/problems/generate-parentheses/) |
| 0032 | Hard | [Longest Valid Parentheses](../0032-longest-valid-parentheses/readme.md) | [link](https://leetcode.com/problems/longest-valid-parentheses/) |
| 0301 | Hard | [Remove Invalid Parentheses](../0301-remove-invalid-parentheses/readme.md) | [link](https://leetcode.com/problems/remove-invalid-parentheses/) |
| 1003 | Medium | [Check If Word Is Valid After Substitutions](../1003-check-if-word-is-valid-after-substitutions/readme.md) | [link](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) |
| 2116 | Medium | [Check if a Parentheses String Can Be Valid](../2116-check-if-a-parentheses-string-can-be-valid/readme.md) | [link](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) |
| 2337 | Medium | [Move Pieces to Obtain a String](../2337-move-pieces-to-obtain-a-string/readme.md) | [link](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
