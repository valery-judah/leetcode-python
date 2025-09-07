# 0954. Array of Doubled Pairs

## Quick Facts

- URL: [Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/)
- Function: `canReorderDoubled`
- Signature: `(arr: list[int])  -> bool`
- Primary pattern: **Greedy**

## Constraints

- `2 <= arr.length <= 3 * 10^4`
- `arr.length is even.`
- `-10^5 <= arr[i] <= 10^5`

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
- Run: `pytest -q -k "0954"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2007 | Medium | [Find Original Array From Doubled Array](../2007-find-original-array-from-doubled-array/readme.md) | [Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) |

## Examples

### Example 1

```text
Input: arr = [3,1,3,6]
Output: false
```

### Example 2

```text
Input: arr = [2,1,2,6]
Output: false
```

### Example 3

```text
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
```

## References

- LeetCode problem and editorial links
