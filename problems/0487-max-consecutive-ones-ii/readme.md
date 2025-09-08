# 0487. Max Consecutive Ones II

## Quick Facts

- URL: [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/)
- Function: `findMaxConsecutiveOnes`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i] is either 0 or 1.`

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
- Run: `pytest -q -k "0487"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0485 | Easy | [Max Consecutive Ones](../0485-max-consecutive-ones/readme.md) | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) |
| 1004 | Medium | [Max Consecutive Ones III](../1004-max-consecutive-ones-iii/readme.md) | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) |
| 2155 | Medium | [All Divisions With the Highest Score of a Binary Array](../2155-all-divisions-with-the-highest-score-of-a-binary-array/readme.md) | [All Divisions With the Highest Score of a Binary Array](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/) |

## Examples

### Example 1

```text
Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
```

### Example 2

```text
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
```

## References

- LeetCode problem and editorial links
