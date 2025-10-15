# 0074. Search a 2D Matrix

## Quick Facts

- URL: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- Function: `searchMatrix`
- Signature: `(matrix: list[list[int]], target: int)  -> bool`
- Primary pattern: **Binary Search**

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

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
- Run: `pytest -q -k "0074"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                           | LeetCode                                                                                    |
| ------ | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0240   | Medium     | [Search a 2D Matrix II](../0240-search-a-2d-matrix-ii/readme.md)               | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)               |
| 2468   | Hard       | [Split Message Based on Limit](../2468-split-message-based-on-limit/readme.md) | [Split Message Based on Limit](https://leetcode.com/problems/split-message-based-on-limit/) |

## Examples

### Example 1

```text
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2

```text
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

## References

- LeetCode problem and editorial links
