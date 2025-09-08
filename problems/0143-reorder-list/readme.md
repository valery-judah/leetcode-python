# 0143. Reorder List

## Quick Facts

- URL: [Reorder List](https://leetcode.com/problems/reorder-list/)
- Function: `reorderList`
- Signature: `(head: ListNode | None)  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the list is in the range [1, 5 * 10^4].`
- `1 <= Node.val <= 1000`

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
- Run: `pytest -q -k "0143"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2095 | Medium | [Delete the Middle Node of a Linked List](../2095-delete-the-middle-node-of-a-linked-list/readme.md) | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) |
| 2516 | Medium | [Take K of Each Character From Left and Right](../2516-take-k-of-each-character-from-left-and-right/readme.md) | [Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/) |

## Examples

### Example 1

```text
L0 → L1 → … → Ln - 1 → Ln
```

### Example 2

```text
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

### Example 3

```text
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

### Example 4

```text
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## References

- LeetCode problem and editorial links
