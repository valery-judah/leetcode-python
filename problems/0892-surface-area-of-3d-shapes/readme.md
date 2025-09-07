# 0892. Surface Area of 3D Shapes

## Quick Facts

- URL: [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/)
- Function: `surfaceArea`
- Signature: `(grid: list[list[int]])  -> int`
- Primary pattern: **Math**

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] <= 50`

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
- Run: `pytest -q -k "0892"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: grid = [[1,2],[3,4]]
Output: 34
```

### Example 2

```text
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
```

### Example 3

```text
Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
```

## References

- LeetCode problem and editorial links
