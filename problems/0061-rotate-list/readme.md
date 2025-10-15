# 0061. Rotate List

## Quick Facts

- URL: [Rotate List](https://leetcode.com/problems/rotate-list/)
- Function: `rotateRight`
- Signature: `(head: ListNode | None, k: int)  -> ListNode | None`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the list is in the range [0, 500].`
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

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
- Run: `pytest -q -k "0061"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                       | LeetCode                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 0189   | Medium     | [Rotate Array](../0189-rotate-array/readme.md)                             | [Rotate Array](https://leetcode.com/problems/rotate-array/)                             |
| 0725   | Medium     | [Split Linked List in Parts](../0725-split-linked-list-in-parts/readme.md) | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) |

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

### Example 2

```text
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

## References

- LeetCode problem and editorial links
