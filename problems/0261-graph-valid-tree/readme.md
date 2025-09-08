# 0261. Graph Valid Tree

## Quick Facts

- URL: [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
- Function: `validTree`
- Signature: `(n: int, edges: list[list[int]])  -> bool`
- Primary pattern: **Graph**

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- `There are no self-loops or repeated edges.`

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
- Run: `pytest -q -k "0261"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0207 | Medium | [Course Schedule](../0207-course-schedule/readme.md) | [Course Schedule](https://leetcode.com/problems/course-schedule/) |
| 0323 | Medium | [Number of Connected Components in an Undirected Graph](../0323-number-of-connected-components-in-an-undirected-graph/readme.md) | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |
| 0841 | Medium | [Keys and Rooms](../0841-keys-and-rooms/readme.md) | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) |

## Examples

### Example 1

```text
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

### Example 2

```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## References

- LeetCode problem and editorial links
