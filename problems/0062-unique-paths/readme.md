# 0062. Unique Paths

## Quick Facts

- URL: https://leetcode.com/problems/unique-paths/
- Signature: `m: int`, `n: int` → `int`
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
- Run: `pytest -q -k "0062"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0063 | Medium | [Unique Paths II](../0063-unique-paths-ii/readme.md) | [link](https://leetcode.com/problems/unique-paths-ii/) |
| 0064 | Medium | [Minimum Path Sum](../0064-minimum-path-sum/readme.md) | [link](https://leetcode.com/problems/minimum-path-sum/) |
| 0174 | Hard | [Dungeon Game](../0174-dungeon-game/readme.md) | [link](https://leetcode.com/problems/dungeon-game/) |
| 2304 | Medium | [Minimum Path Cost in a Grid](../2304-minimum-path-cost-in-a-grid/readme.md) | [link](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |
| 2087 | Medium | [Minimum Cost Homecoming of a Robot in a Grid](../2087-minimum-cost-homecoming-of-a-robot-in-a-grid/readme.md) | [link](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/) |
| 2400 | Medium | [Number of Ways to Reach a Position After Exactly k Steps](../2400-number-of-ways-to-reach-a-position-after-exactly-k-steps/readme.md) | [link](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) |
| 2435 | Hard | [Paths in Matrix Whose Sum Is Divisible by K](../2435-paths-in-matrix-whose-sum-is-divisible-by-k/readme.md) | [link](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:48Z: Created scaffold.
