# 0463. Island Perimeter

## Quick Facts

- URL: [Island Perimeter](https://leetcode.com/problems/island-perimeter/)
- Function: `islandPerimeter`
- Signature: `(grid: list[list[int]])  -> int`
- Primary pattern: **Array**

## Constraints

- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 100`
- `grid[i][j] is 0 or 1.`
- `There is exactly one island in grid.`

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
- Run: `pytest -q -k "0463"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                       | LeetCode                                                                |
| ------ | ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| 0695   | Medium     | [Max Area of Island](../0695-max-area-of-island/readme.md) | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) |
| 0733   | Easy       | [Flood Fill](../0733-flood-fill/readme.md)                 | [Flood Fill](https://leetcode.com/problems/flood-fill/)                 |
| 1034   | Medium     | [Coloring A Border](../1034-coloring-a-border/readme.md)   | [Coloring A Border](https://leetcode.com/problems/coloring-a-border/)   |

## Examples

### Example 1

```text
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
```

### Example 2

```text
Input: grid = [[1]]
Output: 4
```

### Example 3

```text
Input: grid = [[1,0]]
Output: 4
```

## References

- LeetCode problem and editorial links
