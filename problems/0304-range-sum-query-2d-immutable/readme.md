# 0304. Range Sum Query 2D - Immutable

## Quick Facts

- URL: [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)
- Function: \`\`
- Signature: `(inputs: list[int], inputs: list[int])  -> list[str]`
- Primary pattern: **Prefix Sum**

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^4 <= matrix[i][j] <= 10^4`
- `0 <= row1 <= row2 < m`
- `0 <= col1 <= col2 < n`
- `At most 10^4 calls will be made to sumRegion.`

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
- Run: `pytest -q -k "0304"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                 | LeetCode                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 0303   | Easy       | [Range Sum Query - Immutable](../0303-range-sum-query-immutable/readme.md)           | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)           |
| 0308   | Medium     | [Range Sum Query 2D - Mutable](../0308-range-sum-query-2d-mutable/readme.md)         | [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/)         |
| 3030   | Medium     | [Find the Grid of Region Average](../3030-find-the-grid-of-region-average/readme.md) | [Find the Grid of Region Average](https://leetcode.com/problems/find-the-grid-of-region-average/) |

## Examples

### Example 1

```text
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
```

## References

- LeetCode problem and editorial links
