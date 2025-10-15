# 1090. Largest Values From Labels

## Quick Facts

- URL: [Largest Values From Labels](https://leetcode.com/problems/largest-values-from-labels/)
- Function: `largestValsFromLabels`
- Signature: `(values: list[int], labels: list[int], numWanted: int, useLimit: int)  -> int`
- Primary pattern: **Greedy**

## Constraints

- `n == values.length == labels.length`
- `1 <= n <= 2 * 10^4`
- `0 <= values[i], labels[i] <= 2 * 10^4`
- `1 <= numWanted, useLimit <= n`

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
- Run: `pytest -q -k "1090"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                                 | LeetCode                                                                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3572   | Medium     | [Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values](../3572-maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/readme.md) | [Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values](https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/) |

## Examples

None

## References

- LeetCode problem and editorial links
