# 0064. Minimum Path Sum

## Quick Facts

- URL: [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- Function: `minPathSum`
- Signature: `(grid: list[list[int]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

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
- Run: `pytest -q -k "0064"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0062 | Medium | [Unique Paths](../0062-unique-paths/readme.md) | [Unique Paths](https://leetcode.com/problems/unique-paths/) |
| 0174 | Hard | [Dungeon Game](../0174-dungeon-game/readme.md) | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) |
| 0741 | Hard | [Cherry Pickup](../0741-cherry-pickup/readme.md) | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) |
| 1394 | Medium | [Minimum Path Cost in a Grid](../1394-minimum-path-cost-in-a-grid/readme.md) | [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |
| 2067 | Medium | [Maximum Number of Points with Cost](../2067-maximum-number-of-points-with-cost/readme.md) | [Maximum Number of Points with Cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/) |
| 2192 | Medium | [Minimum Cost Homecoming of a Robot in a Grid](../2192-minimum-cost-homecoming-of-a-robot-in-a-grid/readme.md) | [Minimum Cost Homecoming of a Robot in a Grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/) |
| 2521 | Hard | [Paths in Matrix Whose Sum Is Divisible by K](../2521-paths-in-matrix-whose-sum-is-divisible-by-k/readme.md) | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |
| 2653 | Medium | [Check if There is a Path With Equal Number of 0's And 1's](../2653-check-if-there-is-a-path-with-equal-number-of-0s-and-1s/readme.md) | [Check if There is a Path With Equal Number of 0's And 1's](https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) |
| 2686 | Medium | [Minimum Cost of a Path With Special Roads](../2686-minimum-cost-of-a-path-with-special-roads/readme.md) | [Minimum Cost of a Path With Special Roads](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/) |

## Examples

### Example 1

```text
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```

### Example 2

```text
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

## References

- LeetCode problem and editorial links
