# 0200. Number of Islands

## Quick Facts

- URL: [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- Function: `numIslands`
- Signature: `(grid: list[list[str]])  -> int`
- Primary pattern: **Array**

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j] is '0' or '1'.`

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
| 0130 | Medium | [Surrounded Regions](../0130-surrounded-regions/readme.md) | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) |
| 0286 | Medium | [Walls and Gates](../0286-walls-and-gates/readme.md) | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) |
| 0305 | Hard | [Number of Islands II](../0305-number-of-islands-ii/readme.md) | [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) |
| 0323 | Medium | [Number of Connected Components in an Undirected Graph](../0323-number-of-connected-components-in-an-undirected-graph/readme.md) | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |
| 0419 | Medium | [Battleships in a Board](../0419-battleships-in-a-board/readme.md) | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) |
| 0694 | Medium | [Number of Distinct Islands](../0694-number-of-distinct-islands/readme.md) | [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) |
| 0695 | Medium | [Max Area of Island](../0695-max-area-of-island/readme.md) | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) |
| 2035 | Medium | [Count Sub Islands](../2035-count-sub-islands/readme.md) | [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) |
| 2103 | Medium | [Find All Groups of Farmland](../2103-find-all-groups-of-farmland/readme.md) | [Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland/) |
| 2403 | Medium | [Count Unreachable Pairs of Nodes in an Undirected Graph](../2403-count-unreachable-pairs-of-nodes-in-an-undirected-graph/readme.md) | [Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) |
| 2764 | Medium | [Maximum Number of Fish in a Grid](../2764-maximum-number-of-fish-in-a-grid/readme.md) | [Maximum Number of Fish in a Grid](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) |
| 3823 | Medium | [Count Islands With Total Value Divisible by K](../3823-count-islands-with-total-value-divisible-by-k/readme.md) | [Count Islands With Total Value Divisible by K](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/) |

## Examples

### Example 1

```text
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2

```text
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## References

- LeetCode problem and editorial links
