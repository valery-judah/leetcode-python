# 0729. My Calendar I

## Quick Facts

- URL: [My Calendar I](https://leetcode.com/problems/my-calendar-i/)
- Function: \`\`
- Signature: `(starts: list[int], ends: list[int])  -> list[bool]`
- Primary pattern: **Binary Search**

## Constraints

- `0 <= start < end <= 10^9`
- `At most 1000 calls will be made to book.`

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
- Run: `pytest -q -k "0729"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                             | LeetCode                                                                                                      |
| ------ | ---------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| 0731   | Medium     | [My Calendar II](../0731-my-calendar-ii/readme.md)                                               | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)                                               |
| 0732   | Hard       | [My Calendar III](../0732-my-calendar-iii/readme.md)                                             | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)                                             |
| 2446   | Easy       | [Determine if Two Events Have Conflict](../2446-determine-if-two-events-have-conflict/readme.md) | [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/) |

## Examples

### Example 1

```text
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

## References

- LeetCode problem and editorial links
