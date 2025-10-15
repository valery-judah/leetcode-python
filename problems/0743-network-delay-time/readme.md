# 0743. Network Delay Time

## Quick Facts

- URL: [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- Function: `networkDelayTime`
- Signature: `(times: list[list[int]], n: int, k: int)  -> int`
- Primary pattern: **Graph**

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- `All the pairs (ui, vi) are unique. (i.e., no multiple edges.)`

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
- Run: `pytest -q -k "0743"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                   | LeetCode                                                                                                            |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| 2039   | Medium     | [The Time When the Network Becomes Idle](../2039-the-time-when-the-network-becomes-idle/readme.md)     | [The Time When the Network Becomes Idle](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/)     |
| 2045   | Hard       | [Second Minimum Time to Reach Destination](../2045-second-minimum-time-to-reach-destination/readme.md) | [Second Minimum Time to Reach Destination](https://leetcode.com/problems/second-minimum-time-to-reach-destination/) |

## Examples

### Example 1

```text
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

### Example 2

```text
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

### Example 3

```text
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## References

- LeetCode problem and editorial links
