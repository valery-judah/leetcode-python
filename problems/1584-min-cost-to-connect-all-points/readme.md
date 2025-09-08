# 1584. Min Cost to Connect All Points

## Quick Facts

- URL: [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
- Function: `minCostConnectPoints`
- Signature: `(points: list[list[int]])  -> int`
- Primary pattern: **Graph**

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- `All pairs (xi, yi) are distinct.`

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
- Run: `pytest -q -k "1584"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2152 | Medium | [Minimum Number of Lines to Cover Points](../2152-minimum-number-of-lines-to-cover-points/readme.md) | [Minimum Number of Lines to Cover Points](https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/) |

## Examples

### Example 1

```text
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

### Example 2

```text
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## References

- LeetCode problem and editorial links
