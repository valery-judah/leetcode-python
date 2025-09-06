# 0200. Number of Islands

## Quick Facts

- URL: https://leetcode.com/problems/number-of-islands/
- Signature: `grid: list[list[str]]` → `int`
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
- Run: `pytest -q -k "0200"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0130 | Medium | [Surrounded Regions](../0130-surrounded-regions/readme.md) | [link](https://leetcode.com/problems/surrounded-regions/) |
| 0286 | Medium | [Walls and Gates](../0286-walls-and-gates/readme.md) | [link](https://leetcode.com/problems/walls-and-gates/) |
| 0305 | Hard | [Number of Islands II](../0305-number-of-islands-ii/readme.md) | [link](https://leetcode.com/problems/number-of-islands-ii/) |
| 0323 | Medium | [Number of Connected Components in an Undirected Graph](../0323-number-of-connected-components-in-an-undirected-graph/readme.md) | [link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |
| 0419 | Medium | [Battleships in a Board](../0419-battleships-in-a-board/readme.md) | [link](https://leetcode.com/problems/battleships-in-a-board/) |
| 0694 | Medium | [Number of Distinct Islands](../0694-number-of-distinct-islands/readme.md) | [link](https://leetcode.com/problems/number-of-distinct-islands/) |
| 0695 | Medium | [Max Area of Island](../0695-max-area-of-island/readme.md) | [link](https://leetcode.com/problems/max-area-of-island/) |
| 1905 | Medium | [Count Sub Islands](../1905-count-sub-islands/readme.md) | [link](https://leetcode.com/problems/count-sub-islands/) |
| 1992 | Medium | [Find All Groups of Farmland](../1992-find-all-groups-of-farmland/readme.md) | [link](https://leetcode.com/problems/find-all-groups-of-farmland/) |
| 2316 | Medium | [Count Unreachable Pairs of Nodes in an Undirected Graph](../2316-count-unreachable-pairs-of-nodes-in-an-undirected-graph/readme.md) | [link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) |
| 2658 | Medium | [Maximum Number of Fish in a Grid](../2658-maximum-number-of-fish-in-a-grid/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) |
| 3619 | Medium | [Count Islands With Total Value Divisible by K](../3619-count-islands-with-total-value-divisible-by-k/readme.md) | [link](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
