# 0317. Shortest Distance from All Buildings

## Quick Facts

- URL: https://leetcode.com/problems/shortest-distance-from-all-buildings/
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
- Run: `pytest -q -k "0317"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0286 | Medium | [Walls and Gates](../0286-walls-and-gates/readme.md) | [link](https://leetcode.com/problems/walls-and-gates/) |
| 0296 | Hard | [Best Meeting Point](../0296-best-meeting-point/readme.md) | [link](https://leetcode.com/problems/best-meeting-point/) |
| 1162 | Medium | [As Far from Land as Possible](../1162-as-far-from-land-as-possible/readme.md) | [link](https://leetcode.com/problems/as-far-from-land-as-possible/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
