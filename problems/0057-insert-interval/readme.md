# 0057. Insert Interval

## Quick Facts

- URL: [Insert Interval](https://leetcode.com/problems/insert-interval/)
- Function: `insert`
- Signature: `(intervals: list[list[int]], newInterval: list[int])  -> list[list[int]]`
- Primary pattern: **Array**

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^5`
- `intervals is sorted by starti in ascending order.`
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

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
- Run: `pytest -q -k "0057"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0056 | Medium | [Merge Intervals](../0056-merge-intervals/readme.md) | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) |
| 0715 | Hard | [Range Module](../0715-range-module/readme.md) | [Range Module](https://leetcode.com/problems/range-module/) |
| 2276 | Hard | [Count Integers in Intervals](../2276-count-integers-in-intervals/readme.md) | [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/) |

## Examples

### Example 1

```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

### Example 2

```text
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## References

- LeetCode problem and editorial links
