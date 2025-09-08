# 0732. My Calendar III

## Quick Facts

- URL: [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)
- Function: \`\`
- Signature: `(starts: list[int], ends: list[int])  -> list[bool]`
- Primary pattern: **Binary Search**

## Constraints

- `0 <= startTime < endTime <= 10^9`
- `At most 400 calls will be made to book.`

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
- Run: `pytest -q -k "0732"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0729 | Medium | [My Calendar I](../0729-my-calendar-i/readme.md) | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) |
| 0731 | Medium | [My Calendar II](../0731-my-calendar-ii/readme.md) | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) |
| 2276 | Hard | [Count Integers in Intervals](../2276-count-integers-in-intervals/readme.md) | [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/) |

## Examples

### Example 1

```text
Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15); // return 3
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
```

## References

- LeetCode problem and editorial links
