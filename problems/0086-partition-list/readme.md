# 0086. Partition List

## Quick Facts

- URL: [Partition List](https://leetcode.com/problems/partition-list/)
- Function: `partition`
- Signature: `(head: ListNode | None, x: int)  -> ListNode | None`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the list is in the range [0, 200].`
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

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
- Run: `pytest -q -k "0086"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                   | LeetCode                                                                                                            |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| 2161   | Medium     | [Partition Array According to Given Pivot](../2161-partition-array-according-to-given-pivot/readme.md) | [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/) |

## Examples

### Example 1

```text
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

### Example 2

```text
Input: head = [2,1], x = 2
Output: [1,2]
```

## References

- LeetCode problem and editorial links
