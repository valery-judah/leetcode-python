# 0024. Swap Nodes in Pairs

## Quick Facts

- URL: [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- Function: `swapPairs`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the list is in the range [0, 100].`
- `0 <= Node.val <= 100`

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
- Run: `pytest -q -k "0024"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0025 | Hard | [Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group/readme.md) | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) |
| 0528 | Medium | [Swapping Nodes in a Linked List](../0528-swapping-nodes-in-a-linked-list/readme.md) | [Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) |

## Examples

None

## References

- LeetCode problem and editorial links
