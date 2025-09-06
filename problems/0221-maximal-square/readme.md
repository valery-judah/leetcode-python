# 0221. Maximal Square

## Quick Facts

- URL: https://leetcode.com/problems/maximal-square/
- Signature: `matrix: list[list[str]]` → `int`
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
- Run: `pytest -q -k "0221"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0085 | Hard | [Maximal Rectangle](../0085-maximal-rectangle/readme.md) | [link](https://leetcode.com/problems/maximal-rectangle/) |
| 0764 | Medium | [Largest Plus Sign](../0764-largest-plus-sign/readme.md) | [link](https://leetcode.com/problems/largest-plus-sign/) |
| 2201 | Medium | [Count Artifacts That Can Be Extracted](../2201-count-artifacts-that-can-be-extracted/readme.md) | [link](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/) |
| 2132 | Hard | [Stamping the Grid](../2132-stamping-the-grid/readme.md) | [link](https://leetcode.com/problems/stamping-the-grid/) |
| 2943 | Medium | [Maximize Area of Square Hole in Grid](../2943-maximize-area-of-square-hole-in-grid/readme.md) | [link](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
