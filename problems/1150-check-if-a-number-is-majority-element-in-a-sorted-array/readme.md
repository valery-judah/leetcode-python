# 1150. Check If a Number Is Majority Element in a Sorted Array

## Quick Facts

- URL:
  [Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)
- Function: `isMajorityElement`
- Signature: `(nums: list[int], target: int)  -> bool`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i], target <= 10^9`
- `nums is sorted in non-decreasing order.`

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
- Run: `pytest -q -k "1150"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                         | LeetCode                                                                  |
| ------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| 0169   | Easy       | [Majority Element](../0169-majority-element/readme.md)       | [Majority Element](https://leetcode.com/problems/majority-element/)       |
| 0229   | Medium     | [Majority Element II](../0229-majority-element-ii/readme.md) | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) |

## Examples

### Example 1

```text
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
```

### Example 2

```text
Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
```

## References

- LeetCode problem and editorial links
