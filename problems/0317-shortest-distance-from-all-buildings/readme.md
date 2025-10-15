# 0317. Shortest Distance from All Buildings

## Quick Facts

- URL:
  [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/)
- Function: `shortestDistance`
- Signature: `(grid: list[list[int]])  -> int`
- Primary pattern: **Array**

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j] is either 0, 1, or 2.`
- `There will be at least one building in the grid.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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

| Number | Difficulty | Name                                                                           | LeetCode                                                                                    |
| ------ | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0286   | Medium     | [Walls and Gates](../0286-walls-and-gates/readme.md)                           | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/)                           |
| 0296   | Hard       | [Best Meeting Point](../0296-best-meeting-point/readme.md)                     | [Best Meeting Point](https://leetcode.com/problems/best-meeting-point/)                     |
| 1162   | Medium     | [As Far from Land as Possible](../1162-as-far-from-land-as-possible/readme.md) | [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) |

## Examples

### Example 1

```text
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
```

### Example 2

```text
Input: grid = [[1,0]]
Output: 1
```

### Example 3

```text
Input: grid = [[1]]
Output: -1
```

## References

- LeetCode problem and editorial links
