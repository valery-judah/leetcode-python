# 0210. Course Schedule II

## Quick Facts

- URL: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- Function: `findOrder`
- Signature: `(numCourses: int, prerequisites: list[list[int]])  -> list[int]`
- Primary pattern: **Graph**

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- `All the pairs [ai, bi] are distinct.`

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
- Run: `pytest -q -k "0210"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0207 | Medium | [Course Schedule](../0207-course-schedule/readme.md) | [Course Schedule](https://leetcode.com/problems/course-schedule/) |
| 0269 | Hard | [Alien Dictionary](../0269-alien-dictionary/readme.md) | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) |
| 0310 | Medium | [Minimum Height Trees](../0310-minimum-height-trees/readme.md) | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) |
| 0444 | Medium | [Sequence Reconstruction](../0444-sequence-reconstruction/readme.md) | [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/) |
| 0630 | Hard | [Course Schedule III](../0630-course-schedule-iii/readme.md) | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) |
| 1101 | Medium | [Parallel Courses](../1101-parallel-courses/readme.md) | [Parallel Courses](https://leetcode.com/problems/parallel-courses/) |
| 2220 | Medium | [Find All Possible Recipes from Given Supplies](../2220-find-all-possible-recipes-from-given-supplies/readme.md) | [Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) |
| 2472 | Hard | [Build a Matrix With Conditions](../2472-build-a-matrix-with-conditions/readme.md) | [Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/) |
| 2489 | Hard | [Sort Array by Moving Items to Empty Space](../2489-sort-array-by-moving-items-to-empty-space/readme.md) | [Sort Array by Moving Items to Empty Space](https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/) |

## Examples

### Example 1

```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

### Example 2

```text
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

### Example 3

```text
Input: numCourses = 1, prerequisites = []
Output: [0]
```

## References

- LeetCode problem and editorial links
