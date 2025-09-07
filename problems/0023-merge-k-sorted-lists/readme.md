# 0023. Merge k Sorted Lists

## Quick Facts

- URL: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- Function: `mergeKLists`
- Signature: `(lists: list[ListNode | None])  -> ListNode | None`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i] is sorted in ascending order.`
- `The sum of lists[i].length will not exceed 10^4.`

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
- Run: `pytest -q -k "0023"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0021 | Easy | [Merge Two Sorted Lists](../0021-merge-two-sorted-lists/readme.md) | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |
| 0264 | Medium | [Ugly Number II](../0264-ugly-number-ii/readme.md) | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) |
| 2498 | Medium | [Smallest Subarrays With Maximum Bitwise OR](../2498-smallest-subarrays-with-maximum-bitwise-or/readme.md) | [Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) |

## Examples

### Example 1

```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

### Example 2

```text
Input: lists = []
Output: []
```

### Example 3

```text
Input: lists = [[]]
Output: []
```

## References

- LeetCode problem and editorial links
