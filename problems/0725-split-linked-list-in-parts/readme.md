# 0725. Split Linked List in Parts

## Quick Facts

- URL: [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)
- Function: `splitListToParts`
- Signature: `(head: ListNode | None, k: int)  -> list[ListNode | None]`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the list is in the range [0, 1000].`
- `0 <= Node.val <= 1000`
- `1 <= k <= 50`

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
- Run: `pytest -q -k "0725"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0061 | Medium | [Rotate List](../0061-rotate-list/readme.md) | [Rotate List](https://leetcode.com/problems/rotate-list/) |
| 0328 | Medium | [Odd Even Linked List](../0328-odd-even-linked-list/readme.md) | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) |
| 2674 | Medium | [Split a Circular Linked List](../2674-split-a-circular-linked-list/readme.md) | [Split a Circular Linked List](https://leetcode.com/problems/split-a-circular-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
```

### Example 2

```text
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```

## References

- LeetCode problem and editorial links
