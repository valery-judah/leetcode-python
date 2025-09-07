# 0323. Number of Connected Components in an Undirected Graph

## Quick Facts

- URL: [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- Function: `countComponents`
- Signature: `(n: int, edges: list[list[int]])  -> int`
- Primary pattern: **Graph**

## Constraints

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai <= bi < n`
- `ai != bi`
- `There are no repeated edges.`

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
- Run: `pytest -q -k "0323"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0200 | Medium | [Number of Islands](../0200-number-of-islands/readme.md) | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |
| 0261 | Medium | [Graph Valid Tree](../0261-graph-valid-tree/readme.md) | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) |
| 0547 | Medium | [Number of Provinces](../0547-number-of-provinces/readme.md) | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) |
| 2218 | Medium | [Paths in Maze That Lead to Same Room](../2218-paths-in-maze-that-lead-to-same-room/readme.md) | [Paths in Maze That Lead to Same Room](https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/) |
| 2793 | Medium | [Count the Number of Complete Components](../2793-count-the-number-of-complete-components/readme.md) | [Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components/) |

## Examples

### Example 1

```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

### Example 2

```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

## References

- LeetCode problem and editorial links
