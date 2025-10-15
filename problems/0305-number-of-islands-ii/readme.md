# 0305. Number of Islands II

## Quick Facts

- URL: [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)
- Function: `numIslands2`
- Signature: `(m: int, n: int, positions: list[list[int]])  -> list[int]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= m, n, positions.length <= 10^4`
- `1 <= m * n <= 10^4`
- `positions[i].length == 2`
- `0 <= ri < m`
- `0 <= ci < n`

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
- Run: `pytest -q -k "0305"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                       | LeetCode                                                                                                |
| ------ | ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| 0200   | Medium     | [Number of Islands](../0200-number-of-islands/readme.md)                                   | [Number of Islands](https://leetcode.com/problems/number-of-islands/)                                   |
| 2076   | Hard       | [Process Restricted Friend Requests](../2076-process-restricted-friend-requests/readme.md) | [Process Restricted Friend Requests](https://leetcode.com/problems/process-restricted-friend-requests/) |

## Examples

### Example 1

```text
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
```

### Example 2

```text
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

## References

- LeetCode problem and editorial links
