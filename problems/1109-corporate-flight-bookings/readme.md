# 1109. Corporate Flight Bookings

## Quick Facts

- URL: [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)
- Function: `corpFlightBookings`
- Signature: `(bookings: list[list[int]], n: int)  -> list[int]`
- Primary pattern: **Prefix Sum**

## Constraints

- `1 <= n <= 2 * 10^4`
- `1 <= bookings.length <= 2 * 10^4`
- `bookings[i].length == 3`
- `1 <= firsti <= lasti <= n`
- `1 <= seatsi <= 10^4`

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
- Run: `pytest -q -k "1109"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                             | LeetCode                                                                                      |
| ------ | ---------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 3356   | Medium     | [Zero Array Transformation II](../3356-zero-array-transformation-ii/readme.md)   | [Zero Array Transformation II](https://leetcode.com/problems/zero-array-transformation-ii/)   |
| 3362   | Medium     | [Zero Array Transformation III](../3362-zero-array-transformation-iii/readme.md) | [Zero Array Transformation III](https://leetcode.com/problems/zero-array-transformation-iii/) |

## Examples

### Example 1

```text
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]
```

### Example 2

```text
Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]
```

## References

- LeetCode problem and editorial links
