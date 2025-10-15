# 0281. Zigzag Iterator

## Quick Facts

- URL: [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/)
- Function: `ZigzagIterator`
- Signature: `(v1: list[int], v2: list[int])  -> list[int]`
- Primary pattern: **Queue**

## Constraints

- `0 <= v1.length, v2.length <= 1000`
- `1 <= v1.length + v2.length <= 2000`
- `-2^31 <= v1[i], v2[i] <= 2^31 - 1`

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
- Run: `pytest -q -k "0281"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                           | LeetCode                                                                                    |
| ------ | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0173   | Medium     | [Binary Search Tree Iterator](../0173-binary-search-tree-iterator/readme.md)   | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)   |
| 0251   | Medium     | [Flatten 2D Vector](../0251-flatten-2d-vector/readme.md)                       | [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/)                       |
| 0284   | Medium     | [Peeking Iterator](../0284-peeking-iterator/readme.md)                         | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)                         |
| 0341   | Medium     | [Flatten Nested List Iterator](../0341-flatten-nested-list-iterator/readme.md) | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) |
| 1768   | Easy       | [Merge Strings Alternately](../1768-merge-strings-alternately/readme.md)       | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)       |

## Examples

### Example 1

```text
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
```

### Example 2

```text
Input: v1 = [1], v2 = []
Output: [1]
```

### Example 3

```text
Input: v1 = [], v2 = [1]
Output: [1]
```

### Example 4

```text
Input: v1 = [1,2,3], v2 = [4,5,6,7], v3 = [8,9]
Output: [1,4,8,2,5,9,3,6,7]
```

## References

- LeetCode problem and editorial links
