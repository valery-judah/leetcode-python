# 0862. Shortest Subarray with Sum at Least K

## Quick Facts

- URL:
  [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
- Function: `shortestSubarray`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

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
- Run: `pytest -q -k "0862"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                 | LeetCode                                                                                                          |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 3097   | Medium     | [Shortest Subarray With OR at Least K II](../3097-shortest-subarray-with-or-at-least-k-ii/readme.md) | [Shortest Subarray With OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/) |
| 3095   | Easy       | [Shortest Subarray With OR at Least K I](../3095-shortest-subarray-with-or-at-least-k-i/readme.md)   | [Shortest Subarray With OR at Least K I](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/)   |

## Examples

### Example 1

```text
Input: nums = [1], k = 1
Output: 1
```

### Example 2

```text
Input: nums = [1,2], k = 4
Output: -1
```

### Example 3

```text
Input: nums = [2,-1,2], k = 3
Output: 3
```

## References

- LeetCode problem and editorial links
