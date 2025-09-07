# 0133. Clone Graph

## Quick Facts

- URL: [Clone Graph](https://leetcode.com/problems/clone-graph/)
- Function: `cloneGraph`
- Signature: `(edges: list[list[int]])  -> bool`
- Primary pattern: **Graph**

## Constraints

- `The number of nodes in the graph is in the range [0, 100].`
- `1 <= Node.val <= 100`
- `Node.val is unique for each node.`
- `There are no repeated edges and no self-loops in the graph.`
- `The Graph is connected and all nodes can be visited starting from the given node.`

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
- Run: `pytest -q -k "0133"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0138 | Medium | [Copy List with Random Pointer](../0138-copy-list-with-random-pointer/readme.md) | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) |
| 1624 | Medium | [Clone Binary Tree With Random Pointer](../1624-clone-binary-tree-with-random-pointer/readme.md) | [Clone Binary Tree With Random Pointer](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/) |
| 1634 | Medium | [Clone N-ary Tree](../1634-clone-n-ary-tree/readme.md) | [Clone N-ary Tree](https://leetcode.com/problems/clone-n-ary-tree/) |

## Examples

### Example 1

```text
class Node {{
    public int val;
    public List<Node> neighbors;
}}
```

### Example 2

```text
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

### Example 3

```text
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

### Example 4

```text
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

## References

- LeetCode problem and editorial links
