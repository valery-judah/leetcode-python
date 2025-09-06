# 0256. Paint House

## Quick Facts

- URL: https://leetcode.com/problems/paint-house/
- Signature: `costs: list[list[int]]` → `int`
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
- Run: `pytest -q -k "0256"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0198 | Medium | [House Robber](../0198-house-robber/readme.md) | [link](https://leetcode.com/problems/house-robber/) |
| 0213 | Medium | [House Robber II](../0213-house-robber-ii/readme.md) | [link](https://leetcode.com/problems/house-robber-ii/) |
| 0265 | Hard | [Paint House II](../0265-paint-house-ii/readme.md) | [link](https://leetcode.com/problems/paint-house-ii/) |
| 0276 | Medium | [Paint Fence](../0276-paint-fence/readme.md) | [link](https://leetcode.com/problems/paint-fence/) |
| 2304 | Medium | [Minimum Path Cost in a Grid](../2304-minimum-path-cost-in-a-grid/readme.md) | [link](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:54Z: Created scaffold.
