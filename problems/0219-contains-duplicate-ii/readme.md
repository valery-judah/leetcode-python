# 0219. Contains Duplicate II

## Quick Facts

- URL: [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)
- Function: `containsNearbyDuplicate`
- Signature: `(nums: list[int], k: int)  -> bool`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

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
- Run: `pytest -q -k "0219"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                               | LeetCode                                                                        |
| ------ | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| 0217   | Easy       | [Contains Duplicate](../0217-contains-duplicate/readme.md)         | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)         |
| 0220   | Hard       | [Contains Duplicate III](../0220-contains-duplicate-iii/readme.md) | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3,1], k = 3
Output: true
```

### Example 2

```text
Input: nums = [1,0,1,1], k = 1
Output: true
```

### Example 3

```text
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## References

- LeetCode problem and editorial links
