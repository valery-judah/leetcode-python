# 0138. Copy List with Random Pointer

## Quick Facts

- URL: [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
- Function: `copyRandomList`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Hash Table**

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random is null or is pointing to some node in the linked list.`

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
- Run: `pytest -q -k "0138"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0133 | Medium | [Clone Graph](../0133-clone-graph/readme.md) | [Clone Graph](https://leetcode.com/problems/clone-graph/) |
| 1624 | Medium | [Clone Binary Tree With Random Pointer](../1624-clone-binary-tree-with-random-pointer/readme.md) | [Clone Binary Tree With Random Pointer](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/) |
| 1634 | Medium | [Clone N-ary Tree](../1634-clone-n-ary-tree/readme.md) | [Clone N-ary Tree](https://leetcode.com/problems/clone-n-ary-tree/) |

## Examples

### Example 1

```text
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

### Example 2

```text
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

### Example 3

```text
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## References

- LeetCode problem and editorial links
