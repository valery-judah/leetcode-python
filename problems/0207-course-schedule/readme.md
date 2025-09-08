# 0207. Course Schedule

## Quick Facts

- URL: [Course Schedule](https://leetcode.com/problems/course-schedule/)
- Function: `canFinish`
- Signature: `(numCourses: int, prerequisites: list[list[int]])  -> bool`
- Primary pattern: **Graph**

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `All the pairs prerequisites[i] are unique.`

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
- Run: `pytest -q -k "0207"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0210 | Medium | [Course Schedule II](../0210-course-schedule-ii/readme.md) | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| 0261 | Medium | [Graph Valid Tree](../0261-graph-valid-tree/readme.md) | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) |
| 0310 | Medium | [Minimum Height Trees](../0310-minimum-height-trees/readme.md) | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) |
| 0630 | Hard | [Course Schedule III](../0630-course-schedule-iii/readme.md) | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) |
| 2392 | Hard | [Build a Matrix With Conditions](../2392-build-a-matrix-with-conditions/readme.md) | [Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/) |

## Examples

### Example 1

```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

### Example 2

```text
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## References

- LeetCode problem and editorial links
