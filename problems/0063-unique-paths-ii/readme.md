# 0063. Unique Paths II

## Quick Facts

- URL: [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
- Function: `uniquePathsWithObstacles`
- Signature: `(obstacleGrid: list[list[int]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j] is 0 or 1.`

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
- Run: `pytest -q -k "0063"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                         | LeetCode                                                                                                                  |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 0062   | Medium     | [Unique Paths](../0062-unique-paths/readme.md)                                                               | [Unique Paths](https://leetcode.com/problems/unique-paths/)                                                               |
| 0980   | Hard       | [Unique Paths III](../0980-unique-paths-iii/readme.md)                                                       | [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)                                                       |
| 2304   | Medium     | [Minimum Path Cost in a Grid](../2304-minimum-path-cost-in-a-grid/readme.md)                                 | [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/)                                 |
| 2435   | Hard       | [Paths in Matrix Whose Sum Is Divisible by K](../2435-paths-in-matrix-whose-sum-is-divisible-by-k/readme.md) | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## Examples

### Example 1

```text
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

### Example 2

```text
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

## References

- LeetCode problem and editorial links
