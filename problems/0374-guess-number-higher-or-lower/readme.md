# 0374. Guess Number Higher or Lower

## Quick Facts

- URL: [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
- Function: `guessNumber`
- Signature: `(n: int, pick: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= n <= 2^31 - 1`
- `1 <= pick <= n`

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
- Run: `pytest -q -k "0374"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                 | LeetCode                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 0278   | Easy       | [First Bad Version](../0278-first-bad-version/readme.md)                             | [First Bad Version](https://leetcode.com/problems/first-bad-version/)                             |
| 0375   | Medium     | [Guess Number Higher or Lower II](../0375-guess-number-higher-or-lower-ii/readme.md) | [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) |
| 0658   | Medium     | [Find K Closest Elements](../0658-find-k-closest-elements/readme.md)                 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)                 |

## Examples

### Example 1

```text
Input: n = 10, pick = 6
Output: 6
```

### Example 2

```text
Input: n = 1, pick = 1
Output: 1
```

### Example 3

```text
Input: n = 2, pick = 1
Output: 1
```

## References

- LeetCode problem and editorial links
