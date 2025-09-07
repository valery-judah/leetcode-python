# 0684. Redundant Connection

## Quick Facts

- URL: [Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- Function: `findRedundantConnection`
- Signature: `(edges: list[list[int]])  -> list[int]`
- Primary pattern: **Graph**

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= edges.length`
- `ai != bi`
- `There are no repeated edges.`
- `The given graph is connected.`

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
- Run: `pytest -q -k "0684"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0685 | Hard | [Redundant Connection II](../0685-redundant-connection-ii/readme.md) | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) |
| 0721 | Medium | [Accounts Merge](../0721-accounts-merge/readme.md) | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) |
| 2127 | Hard | [Maximum Employees to Be Invited to a Meeting](../2127-maximum-employees-to-be-invited-to-a-meeting/readme.md) | [Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/) |
| 2608 | Hard | [Shortest Cycle in a Graph](../2608-shortest-cycle-in-a-graph/readme.md) | [Shortest Cycle in a Graph](https://leetcode.com/problems/shortest-cycle-in-a-graph/) |

## Examples

### Example 1

```text
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

### Example 2

```text
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## References

- LeetCode problem and editorial links
