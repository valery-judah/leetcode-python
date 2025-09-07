# 0062. Unique Paths

## Quick Facts

- URL: [Unique Paths](https://leetcode.com/problems/unique-paths/)
- Function: `uniquePaths`
- Signature: `(m: int, n: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= m, n <= 100`

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
- Run: `pytest -q -k "0062"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0063 | Medium | [Unique Paths II](../0063-unique-paths-ii/readme.md) | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) |
| 0064 | Medium | [Minimum Path Sum](../0064-minimum-path-sum/readme.md) | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) |
| 0174 | Hard | [Dungeon Game](../0174-dungeon-game/readme.md) | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) |
| 1394 | Medium | [Minimum Path Cost in a Grid](../1394-minimum-path-cost-in-a-grid/readme.md) | [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |
| 2192 | Medium | [Minimum Cost Homecoming of a Robot in a Grid](../2192-minimum-cost-homecoming-of-a-robot-in-a-grid/readme.md) | [Minimum Cost Homecoming of a Robot in a Grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/) |
| 2477 | Medium | [Number of Ways to Reach a Position After Exactly k Steps](../2477-number-of-ways-to-reach-a-position-after-exactly-k-steps/readme.md) | [Number of Ways to Reach a Position After Exactly k Steps](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) |
| 2521 | Hard | [Paths in Matrix Whose Sum Is Divisible by K](../2521-paths-in-matrix-whose-sum-is-divisible-by-k/readme.md) | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## Examples

### Example 1

```text
Input: m = 3, n = 7
Output: 28
```

### Example 2

```text
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## References

- LeetCode problem and editorial links
