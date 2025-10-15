# 0763. Partition Labels

## Quick Facts

- URL: [Partition Labels](https://leetcode.com/problems/partition-labels/)
- Function: `partitionLabels`
- Signature: `(s: str)  -> list[int]`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 500`
- `s consists of lowercase English letters.`

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
- Run: `pytest -q -k "0763"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                         | LeetCode                                                                                  |
| ------ | ---------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 0056   | Medium     | [Merge Intervals](../0056-merge-intervals/readme.md)                         | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                         |
| 2405   | Medium     | [Optimal Partition of String](../2405-optimal-partition-of-string/readme.md) | [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) |

## Examples

### Example 1

```text
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

### Example 2

```text
Input: s = "eccbbbbdec"
Output: [10]
```

## References

- LeetCode problem and editorial links
