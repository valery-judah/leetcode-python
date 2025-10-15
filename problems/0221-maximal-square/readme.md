# 0221. Maximal Square

## Quick Facts

- URL: [Maximal Square](https://leetcode.com/problems/maximal-square/)
- Function: `maximalSquare`
- Signature: `(matrix: list[list[str]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j] is '0' or '1'.`

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
- Run: `pytest -q -k "0221"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                             | LeetCode                                                                                                      |
| ------ | ---------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| 0085   | Hard       | [Maximal Rectangle](../0085-maximal-rectangle/readme.md)                                         | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)                                         |
| 0764   | Medium     | [Largest Plus Sign](../0764-largest-plus-sign/readme.md)                                         | [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/)                                         |
| 2201   | Medium     | [Count Artifacts That Can Be Extracted](../2201-count-artifacts-that-can-be-extracted/readme.md) | [Count Artifacts That Can Be Extracted](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/) |
| 2132   | Hard       | [Stamping the Grid](../2132-stamping-the-grid/readme.md)                                         | [Stamping the Grid](https://leetcode.com/problems/stamping-the-grid/)                                         |
| 2943   | Medium     | [Maximize Area of Square Hole in Grid](../2943-maximize-area-of-square-hole-in-grid/readme.md)   | [Maximize Area of Square Hole in Grid](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/)   |

## Examples

### Example 1

```text
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

### Example 2

```text
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

### Example 3

```text
Input: matrix = [["0"]]
Output: 0
```

## References

- LeetCode problem and editorial links
