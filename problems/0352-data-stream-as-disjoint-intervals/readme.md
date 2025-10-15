# 0352. Data Stream as Disjoint Intervals

## Quick Facts

- URL: [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
- Function: \`\`
- Signature: `()  -> bool`
- Primary pattern: **Binary Search**

## Constraints

- `0 <= value <= 10^4`
- `At most 3 * 10^4 calls will be made to addNum and getIntervals.`
- `At most 10^2 calls will be made to getIntervals.`

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
- Run: `pytest -q -k "0352"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                         | LeetCode                                                                                  |
| ------ | ---------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 0228   | Easy       | [Summary Ranges](../0228-summary-ranges/readme.md)                           | [Summary Ranges](https://leetcode.com/problems/summary-ranges/)                           |
| 0436   | Medium     | [Find Right Interval](../0436-find-right-interval/readme.md)                 | [Find Right Interval](https://leetcode.com/problems/find-right-interval/)                 |
| 0715   | Hard       | [Range Module](../0715-range-module/readme.md)                               | [Range Module](https://leetcode.com/problems/range-module/)                               |
| 2276   | Hard       | [Count Integers in Intervals](../2276-count-integers-in-intervals/readme.md) | [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/) |

## Examples

### Example 1

```text
Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
```

## References

- LeetCode problem and editorial links
