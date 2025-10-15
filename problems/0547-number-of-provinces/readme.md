# 0547. Number of Provinces

## Quick Facts

- URL: [Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- Function: `findCircleNum`
- Signature: `(isConnected: list[list[int]])  -> int`
- Primary pattern: **Graph**

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j] is 1 or 0.`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

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
- Run: `pytest -q -k "0547"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                             | LeetCode                                                                                                                                      |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 0323   | Medium     | [Number of Connected Components in an Undirected Graph](../0323-number-of-connected-components-in-an-undirected-graph/readme.md) | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |
| 0657   | Easy       | [Robot Return to Origin](../0657-robot-return-to-origin/readme.md)                                                               | [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)                                                               |
| 0734   | Easy       | [Sentence Similarity](../0734-sentence-similarity/readme.md)                                                                     | [Sentence Similarity](https://leetcode.com/problems/sentence-similarity/)                                                                     |
| 0737   | Medium     | [Sentence Similarity II](../0737-sentence-similarity-ii/readme.md)                                                               | [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/)                                                               |
| 1101   | Medium     | [The Earliest Moment When Everyone Become Friends](../1101-the-earliest-moment-when-everyone-become-friends/readme.md)           | [The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/)           |
| 2101   | Medium     | [Detonate the Maximum Bombs](../2101-detonate-the-maximum-bombs/readme.md)                                                       | [Detonate the Maximum Bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/)                                                       |

## Examples

### Example 1

```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

### Example 2

```text
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## References

- LeetCode problem and editorial links
