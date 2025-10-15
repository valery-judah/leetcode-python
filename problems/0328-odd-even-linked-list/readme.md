# 0328. Odd Even Linked List

## Quick Facts

- URL: [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)
- Function: `oddEvenList`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the linked list is in the range [0, 10^4].`
- `-10^6 <= Node.val <= 10^6`

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
- Run: `pytest -q -k "0328"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                       | LeetCode                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 0725   | Medium     | [Split Linked List in Parts](../0725-split-linked-list-in-parts/readme.md) | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) |
| 3467   | Easy       | [Transform Array by Parity](../3467-transform-array-by-parity/readme.md)   | [Transform Array by Parity](https://leetcode.com/problems/transform-array-by-parity/)   |

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

### Example 2

```text
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

## References

- LeetCode problem and editorial links
