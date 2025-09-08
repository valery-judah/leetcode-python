# 0994. Rotting Oranges

## Quick Facts

- URL: [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- Function: `orangesRotting`
- Signature: `(grid: list[list[int]])  -> int`
- Primary pattern: **Array**

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j] is 0, 1, or 2.`

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
- Run: `pytest -q -k "0994"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0286 | Medium | [Walls and Gates](../0286-walls-and-gates/readme.md) | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) |
| 0419 | Medium | [Battleships in a Board](../0419-battleships-in-a-board/readme.md) | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) |
| 2101 | Medium | [Detonate the Maximum Bombs](../2101-detonate-the-maximum-bombs/readme.md) | [Detonate the Maximum Bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/) |
| 2258 | Hard | [Escape the Spreading Fire](../2258-escape-the-spreading-fire/readme.md) | [Escape the Spreading Fire](https://leetcode.com/problems/escape-the-spreading-fire/) |

## Examples

### Example 1

```text
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

### Example 2

```text
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

### Example 3

```text
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

## References

- LeetCode problem and editorial links
