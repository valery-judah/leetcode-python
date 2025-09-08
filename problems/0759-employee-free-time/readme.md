# 0759. Employee Free Time

## Quick Facts

- URL: [Employee Free Time](https://leetcode.com/problems/employee-free-time/)
- Function: `employeeFreeTime`
- Signature: `(schedule: int)  -> int`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= schedule.length , schedule[i].length <= 50`
- `0 <= schedule[i].start < schedule[i].end <= 10^8`

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
- Run: `pytest -q -k "0759"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0056 | Medium | [Merge Intervals](../0056-merge-intervals/readme.md) | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) |
| 0986 | Medium | [Interval List Intersections](../0986-interval-list-intersections/readme.md) | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) |

## Examples

### Example 1

```text
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
```

### Example 2

```text
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
```

## References

- LeetCode problem and editorial links
