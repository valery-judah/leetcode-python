# 0174. Dungeon Game

## Quick Facts

- URL: [Dungeon Game](https://leetcode.com/problems/dungeon-game/)
- Function: `calculateMinimumHP`
- Signature: `(dungeon: list[list[int]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `m == dungeon.length`
- `n == dungeon[i].length`
- `1 <= m, n <= 200`
- `-1000 <= dungeon[i][j] <= 1000`

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
- Run: `pytest -q -k "0174"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                                   | LeetCode                                                                                                                                            |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0062   | Medium     | [Unique Paths](../0062-unique-paths/readme.md)                                                                                         | [Unique Paths](https://leetcode.com/problems/unique-paths/)                                                                                         |
| 0064   | Medium     | [Minimum Path Sum](../0064-minimum-path-sum/readme.md)                                                                                 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)                                                                                 |
| 0741   | Hard       | [Cherry Pickup](../0741-cherry-pickup/readme.md)                                                                                       | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)                                                                                       |
| 2304   | Medium     | [Minimum Path Cost in a Grid](../2304-minimum-path-cost-in-a-grid/readme.md)                                                           | [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/)                                                           |
| 2214   | Medium     | [Minimum Health to Beat Game](../2214-minimum-health-to-beat-game/readme.md)                                                           | [Minimum Health to Beat Game](https://leetcode.com/problems/minimum-health-to-beat-game/)                                                           |
| 2435   | Hard       | [Paths in Matrix Whose Sum Is Divisible by K](../2435-paths-in-matrix-whose-sum-is-divisible-by-k/readme.md)                           | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)                           |
| 2510   | Medium     | [Check if There is a Path With Equal Number of 0's And 1's](../2510-check-if-there-is-a-path-with-equal-number-of-0s-and-1s/readme.md) | [Check if There is a Path With Equal Number of 0's And 1's](https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) |

## Examples

### Example 1

```text
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
```

### Example 2

```text
Input: dungeon = [[0]]
Output: 1
```

## References

- LeetCode problem and editorial links
