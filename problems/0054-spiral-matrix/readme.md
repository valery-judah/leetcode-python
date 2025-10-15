# 0054. Spiral Matrix

## Quick Facts

- URL: [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- Function: `spiralOrder`
- Signature: `(matrix: list[list[int]])  -> list[int]`
- Primary pattern: **Array**

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

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
- Run: `pytest -q -k "0054"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                     | LeetCode                                                              |
| ------ | ---------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| 0059   | Medium     | [Spiral Matrix II](../0059-spiral-matrix-ii/readme.md)   | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)   |
| 0885   | Medium     | [Spiral Matrix III](../0885-spiral-matrix-iii/readme.md) | [Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/) |
| 2326   | Medium     | [Spiral Matrix IV](../2326-spiral-matrix-iv/readme.md)   | [Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv/)   |

## Examples

### Example 1

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2

```text
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## References

- LeetCode problem and editorial links
