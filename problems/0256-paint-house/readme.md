# 0256. Paint House

## Quick Facts

- URL: [Paint House](https://leetcode.com/problems/paint-house/)
- Function: `minCost`
- Signature: `(costs: list[list[int]])  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `costs.length == n`
- `costs[i].length == 3`
- `1 <= n <= 100`
- `1 <= costs[i][j] <= 20`

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
- Run: `pytest -q -k "0256"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                         | LeetCode                                                                                  |
| ------ | ---------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 0198   | Medium     | [House Robber](../0198-house-robber/readme.md)                               | [House Robber](https://leetcode.com/problems/house-robber/)                               |
| 0213   | Medium     | [House Robber II](../0213-house-robber-ii/readme.md)                         | [House Robber II](https://leetcode.com/problems/house-robber-ii/)                         |
| 0265   | Hard       | [Paint House II](../0265-paint-house-ii/readme.md)                           | [Paint House II](https://leetcode.com/problems/paint-house-ii/)                           |
| 0276   | Medium     | [Paint Fence](../0276-paint-fence/readme.md)                                 | [Paint Fence](https://leetcode.com/problems/paint-fence/)                                 |
| 2304   | Medium     | [Minimum Path Cost in a Grid](../2304-minimum-path-cost-in-a-grid/readme.md) | [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |

## Examples

### Example 1

```text
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
```

### Example 2

```text
Input: costs = [[7,6,2]]
Output: 2
```

## References

- LeetCode problem and editorial links
