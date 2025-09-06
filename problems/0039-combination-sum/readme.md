# 0039. Combination Sum

## Quick Facts

- URL: https://leetcode.com/problems/combination-sum/
- Signature: `candidates: list[int]`, `target: int` → `list[list[int]]`
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
- Run: `pytest -q -k "0039"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0017 | Medium | [Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/readme.md) | [link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| 0040 | Medium | [Combination Sum II](../0040-combination-sum-ii/readme.md) | [link](https://leetcode.com/problems/combination-sum-ii/) |
| 0077 | Medium | [Combinations](../0077-combinations/readme.md) | [link](https://leetcode.com/problems/combinations/) |
| 0216 | Medium | [Combination Sum III](../0216-combination-sum-iii/readme.md) | [link](https://leetcode.com/problems/combination-sum-iii/) |
| 0254 | Medium | [Factor Combinations](../0254-factor-combinations/readme.md) | [link](https://leetcode.com/problems/factor-combinations/) |
| 0377 | Medium | [Combination Sum IV](../0377-combination-sum-iv/readme.md) | [link](https://leetcode.com/problems/combination-sum-iv/) |
| 3183 | Medium | [The Number of Ways to Make the Sum](../3183-the-number-of-ways-to-make-the-sum/readme.md) | [link](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
