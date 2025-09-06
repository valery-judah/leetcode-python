# 0025. Reverse Nodes in k-Group

## Quick Facts

- URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
- Signature: `head: ListNode | None`, `k: int` → `ListNode | None`
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
- Run: `pytest -q -k "0025"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0024 | Medium | [Swap Nodes in Pairs](../0024-swap-nodes-in-pairs/readme.md) | [link](https://leetcode.com/problems/swap-nodes-in-pairs/) |
| 1721 | Medium | [Swapping Nodes in a Linked List](../1721-swapping-nodes-in-a-linked-list/readme.md) | [link](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) |
| 2074 | Medium | [Reverse Nodes in Even Length Groups](../2074-reverse-nodes-in-even-length-groups/readme.md) | [link](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
