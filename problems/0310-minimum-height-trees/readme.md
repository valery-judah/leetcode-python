# 0310. Minimum Height Trees

## Quick Facts

- URL: https://leetcode.com/problems/minimum-height-trees/
- Signature: `n: int`, `edges: list[list[int]]` → `list[int]`
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
- Run: `pytest -q -k "0310"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0207 | Medium | [Course Schedule](../0207-course-schedule/readme.md) | [link](https://leetcode.com/problems/course-schedule/) |
| 0210 | Medium | [Course Schedule II](../0210-course-schedule-ii/readme.md) | [link](https://leetcode.com/problems/course-schedule-ii/) |
| 2603 | Hard | [Collect Coins in a Tree](../2603-collect-coins-in-a-tree/readme.md) | [link](https://leetcode.com/problems/collect-coins-in-a-tree/) |
| 3067 | Medium | [Count Pairs of Connectable Servers in a Weighted Tree Network](../3067-count-pairs-of-connectable-servers-in-a-weighted-tree-network/readme.md) | [link](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) |
| 3203 | Hard | [Find Minimum Diameter After Merging Two Trees](../3203-find-minimum-diameter-after-merging-two-trees/readme.md) | [link](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
