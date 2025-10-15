# 0931. Minimum Falling Path Sum

## Quick Facts

- URL: [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)
- Function: `minFallingPathSum`
- Signature: `(matrix: list[list[int]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
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
- Run: `pytest -q -k "0931"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                         | LeetCode                                                                                  |
| ------ | ---------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1289   | Hard       | [Minimum Falling Path Sum II](../1289-minimum-falling-path-sum-ii/readme.md) | [Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/) |

## Examples

### Example 1

```text
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

### Example 2

```text
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

## References

- LeetCode problem and editorial links
