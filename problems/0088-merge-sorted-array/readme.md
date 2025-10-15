# 0088. Merge Sorted Array

## Quick Facts

- URL: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- Function: `merge`
- Signature: `(nums1: list[int], m: int, nums2: list[int], n: int)  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

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
- Run: `pytest -q -k "0088"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                           | LeetCode                                                                                                                    |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 0021   | Easy       | [Merge Two Sorted Lists](../0021-merge-two-sorted-lists/readme.md)                                             | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)                                             |
| 0977   | Easy       | [Squares of a Sorted Array](../0977-squares-of-a-sorted-array/readme.md)                                       | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)                                       |
| 0986   | Medium     | [Interval List Intersections](../0986-interval-list-intersections/readme.md)                                   | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)                                   |
| 2516   | Medium     | [Take K of Each Character From Left and Right](../2516-take-k-of-each-character-from-left-and-right/readme.md) | [Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/) |

## Examples

### Example 1

```text
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

### Example 2

```text
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

### Example 3

```text
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## References

- LeetCode problem and editorial links
