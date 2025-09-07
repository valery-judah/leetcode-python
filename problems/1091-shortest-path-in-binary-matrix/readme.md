# 1091. Shortest Path in Binary Matrix

## Quick Facts

- URL: [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
- Function: `shortestPathBinaryMatrix`
- Signature: `(grid: list[list[int]])  -> int`
- Primary pattern: **Array**

## Constraints

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j] is 0 or 1`

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
- Run: `pytest -q -k "1091"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2521 | Hard | [Paths in Matrix Whose Sum Is Divisible by K](../2521-paths-in-matrix-whose-sum-is-divisible-by-k/readme.md) | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) |

## Examples

### Example 1

```text
Input: grid = [[0,1],[1,0]]
Output: 2
```

### Example 2

```text
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

### Example 3

```text
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

## References

- LeetCode problem and editorial links
