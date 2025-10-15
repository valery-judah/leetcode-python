# 0930. Binary Subarrays With Sum

## Quick Facts

- URL: [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)
- Function: `numSubarraysWithSum`
- Signature: `(nums: list[int], goal: int)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `nums[i] is either 0 or 1.`
- `0 <= goal <= nums.length`

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
- Run: `pytest -q -k "0930"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                     | LeetCode                                                                                                              |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 2302   | Hard       | [Count Subarrays With Score Less Than K](../2302-count-subarrays-with-score-less-than-k/readme.md)       | [Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/)       |
| 2750   | Medium     | [Ways to Split Array Into Good Subarrays](../2750-ways-to-split-array-into-good-subarrays/readme.md)     | [Ways to Split Array Into Good Subarrays](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/)     |
| 3129   | Medium     | [Find All Possible Stable Binary Arrays I](../3129-find-all-possible-stable-binary-arrays-i/readme.md)   | [Find All Possible Stable Binary Arrays I](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/)   |
| 3130   | Hard       | [Find All Possible Stable Binary Arrays II](../3130-find-all-possible-stable-binary-arrays-ii/readme.md) | [Find All Possible Stable Binary Arrays II](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/) |

## Examples

### Example 1

```text
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
```

### Example 2

```text
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
```

## References

- LeetCode problem and editorial links
