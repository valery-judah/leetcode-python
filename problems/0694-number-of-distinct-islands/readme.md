# 0694. Number of Distinct Islands

## Quick Facts

- URL: https://leetcode.com/problems/number-of-distinct-islands/
- Signature: `grid: list[list[int]]` → `int`
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
- Run: `pytest -q -k "0694"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0200 | Medium | [Number of Islands](../0200-number-of-islands/readme.md) | [link](https://leetcode.com/problems/number-of-islands/) |
| 0711 | Hard | [Number of Distinct Islands II](../0711-number-of-distinct-islands-ii/readme.md) | [link](https://leetcode.com/problems/number-of-distinct-islands-ii/) |
| 1905 | Medium | [Count Sub Islands](../1905-count-sub-islands/readme.md) | [link](https://leetcode.com/problems/count-sub-islands/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:59Z: Created scaffold.
