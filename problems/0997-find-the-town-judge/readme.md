# 0997. Find the Town Judge

## Quick Facts

- URL: [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)
- Function: `findJudge`
- Signature: `(n: int, trust: list[list[int]])  -> int`
- Primary pattern: **Graph**

## Constraints

- `1 <= n <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `All the pairs of trust are unique.`
- `ai != bi`
- `1 <= ai, bi <= n`

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
- Run: `pytest -q -k "0997"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                       | LeetCode                                                                |
| ------ | ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| 0277   | Medium     | [Find the Celebrity](../0277-find-the-celebrity/readme.md) | [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) |

## Examples

### Example 1

```text
Input: n = 2, trust = [[1,2]]
Output: 2
```

### Example 2

```text
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

### Example 3

```text
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

## References

- LeetCode problem and editorial links
