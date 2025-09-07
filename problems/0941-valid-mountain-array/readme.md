# 0941. Valid Mountain Array

## Quick Facts

- URL: [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)
- Function: `validMountainArray`
- Signature: `(arr: list[int])  -> bool`
- Primary pattern: **Array**

## Constraints

- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^4`

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
- Run: `pytest -q -k "0941"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1766 | Hard | [Minimum Number of Removals to Make Mountain Array](../1766-minimum-number-of-removals-to-make-mountain-array/readme.md) | [Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |
| 2865 | Medium | [Beautiful Towers I](../2865-beautiful-towers-i/readme.md) | [Beautiful Towers I](https://leetcode.com/problems/beautiful-towers-i/) |

## Examples

### Example 1

```text
Input: arr = [2,1]
Output: false
```

### Example 2

```text
Input: arr = [3,5,5]
Output: false
```

### Example 3

```text
Input: arr = [0,3,2,1]
Output: true
```

## References

- LeetCode problem and editorial links
