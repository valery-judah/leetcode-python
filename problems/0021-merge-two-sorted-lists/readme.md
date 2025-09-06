# 0021. Merge Two Sorted Lists

## Quick Facts

- URL: https://leetcode.com/problems/merge-two-sorted-lists/
- Signature: `list1: ListNode | None`, `list2: ListNode | None` → `ListNode | None`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0021"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0023 | Hard | [Merge k Sorted Lists](../0023-merge-k-sorted-lists/readme.md) | [link](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 0088 | Easy | [Merge Sorted Array](../0088-merge-sorted-array/readme.md) | [link](https://leetcode.com/problems/merge-sorted-array/) |
| 0147 | Medium | [Sort List](../0147-sort-list/readme.md) | [link](https://leetcode.com/problems/sort-list/) |
| 0244 | Medium | [Shortest Word Distance II](../0244-shortest-word-distance-ii/readme.md) | [link](https://leetcode.com/problems/shortest-word-distance-ii/) |
| 1634 | Medium | [Add Two Polynomials Represented as Linked Lists](../1634-add-two-polynomials-represented-as-linked-lists/readme.md) | [link](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) |
| 1940 | Medium | [Longest Common Subsequence Between Sorted Arrays](../1940-longest-common-subsequence-between-sorted-arrays/readme.md) | [link](https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/) |
| 2570 | Easy | [Merge Two 2D Arrays by Summing Values](../2570-merge-two-2d-arrays-by-summing-values/readme.md) | [link](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
