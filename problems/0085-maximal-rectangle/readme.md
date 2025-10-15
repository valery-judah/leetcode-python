# 0085. Maximal Rectangle

## Quick Facts

- URL: [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
- Function: `maximalRectangle`
- Signature: `(matrix: list[list[str]])  -> int`
- Primary pattern: **Stack**

## Constraints

- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= row, cols <= 200`
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
- Run: `pytest -q -k "0085"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                               | LeetCode                                                                                                                                        |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0084   | Hard       | [Largest Rectangle in Histogram](../0084-largest-rectangle-in-histogram/readme.md)                                                 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)                                                 |
| 0221   | Medium     | [Maximal Square](../0221-maximal-square/readme.md)                                                                                 | [Maximal Square](https://leetcode.com/problems/maximal-square/)                                                                                 |
| 3359   | Hard       | [Find Sorted Submatrices With Maximum Element at Most K](../3359-find-sorted-submatrices-with-maximum-element-at-most-k/readme.md) | [Find Sorted Submatrices With Maximum Element at Most K](https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/) |

## Examples

### Example 1

```text
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

### Example 2

```text
Input: matrix = [["0"]]
Output: 0
```

### Example 3

```text
Input: matrix = [["1"]]
Output: 1
```

## References

- LeetCode problem and editorial links
