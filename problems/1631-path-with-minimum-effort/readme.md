# 1631. Path With Minimum Effort

## Quick Facts

- URL: [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
- Function: `minimumEffortPath`
- Signature: `(heights: list[list[int]])  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `rows == heights.length`
- `columns == heights[i].length`
- `1 <= rows, columns <= 100`
- `1 <= heights[i][j] <= 10^6`

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
- Run: `pytest -q -k "1631"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                 | LeetCode                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 0778   | Hard       | [Swim in Rising Water](../0778-swim-in-rising-water/readme.md)                       | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)                       |
| 1102   | Medium     | [Path With Maximum Minimum Value](../1102-path-with-maximum-minimum-value/readme.md) | [Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/) |
| 2812   | Medium     | [Find the Safest Path in a Grid](../2812-find-the-safest-path-in-a-grid/readme.md)   | [Find the Safest Path in a Grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)   |

## Examples

### Example 1

```text
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
```

### Example 2

```text
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
```

### Example 3

```text
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
```

## References

- LeetCode problem and editorial links
