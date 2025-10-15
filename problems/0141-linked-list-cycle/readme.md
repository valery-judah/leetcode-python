# 0141. Linked List Cycle

## Quick Facts

- URL: [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- Function: `hasCycle`
- Signature: `(head: ListNode | None, pos: int)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of the nodes in the list is in the range [0, 10^4].`
- `-10^5 <= Node.val <= 10^5`
- `pos is -1 or a valid index in the linked-list.`

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
- Run: `pytest -q -k "0141"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                           | LeetCode                                                                    |
| ------ | ---------- | -------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 0142   | Medium     | [Linked List Cycle II](../0142-linked-list-cycle-ii/readme.md) | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) |
| 0202   | Easy       | [Happy Number](../0202-happy-number/readme.md)                 | [Happy Number](https://leetcode.com/problems/happy-number/)                 |

## Examples

### Example 1

```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2

```text
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3

```text
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## References

- LeetCode problem and editorial links
