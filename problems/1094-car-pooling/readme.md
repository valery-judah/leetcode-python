# 1094. Car Pooling

## Quick Facts

- URL: [Car Pooling](https://leetcode.com/problems/car-pooling/)
- Function: `carPooling`
- Signature: `(trips: list[list[int]], capacity: int)  -> bool`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengersi <= 100`
- `0 <= fromi < toi <= 1000`
- `1 <= capacity <= 10^5`

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
- Run: `pytest -q -k "1094"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                   | LeetCode                                                            |
| ------ | ---------- | ------------------------------------------------------ | ------------------------------------------------------------------- |
| 0253   | Medium     | [Meeting Rooms II](../0253-meeting-rooms-ii/readme.md) | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) |

## Examples

### Example 1

```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

### Example 2

```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

## References

- LeetCode problem and editorial links
