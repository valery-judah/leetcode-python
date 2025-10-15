# 0327. Count of Range Sum

## Quick Facts

- URL: [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)
- Function: `countRangeSum`
- Signature: `(nums: list[int], lower: int, upper: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`
- `The answer is guaranteed to fit in a 32-bit integer.`

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
- Run: `pytest -q -k "0327"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                         | LeetCode                                                                                                  |
| ------ | ---------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 0315   | Hard       | [Count of Smaller Numbers After Self](../0315-count-of-smaller-numbers-after-self/readme.md) | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 0493   | Hard       | [Reverse Pairs](../0493-reverse-pairs/readme.md)                                             | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)                                             |
| 2563   | Medium     | [Count the Number of Fair Pairs](../2563-count-the-number-of-fair-pairs/readme.md)           | [Count the Number of Fair Pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs/)           |
| 3468   | Medium     | [Find the Number of Copy Arrays](../3468-find-the-number-of-copy-arrays/readme.md)           | [Find the Number of Copy Arrays](https://leetcode.com/problems/find-the-number-of-copy-arrays/)           |

## Examples

### Example 1

```text
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
```

### Example 2

```text
Input: nums = [0], lower = 0, upper = 0
Output: 1
```

## References

- LeetCode problem and editorial links
