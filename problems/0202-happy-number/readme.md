# 0202. Happy Number

## Quick Facts

- URL: https://leetcode.com/problems/happy-number/
- Signature: `n: int` → `bool`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0202"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0141 | Easy | [Linked List Cycle](../0141-linked-list-cycle/readme.md) | [link](https://leetcode.com/problems/linked-list-cycle/) |
| 0258 | Easy | [Add Digits](../0258-add-digits/readme.md) | [link](https://leetcode.com/problems/add-digits/) |
| 0263 | Easy | [Ugly Number](../0263-ugly-number/readme.md) | [link](https://leetcode.com/problems/ugly-number/) |
| 1945 | Easy | [Sum of Digits of String After Convert](../1945-sum-of-digits-of-string-after-convert/readme.md) | [link](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/) |
| 2457 | Medium | [Minimum Addition to Make Integer Beautiful](../2457-minimum-addition-to-make-integer-beautiful/readme.md) | [link](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/) |
| 2507 | Medium | [Smallest Value After Replacing With Sum of Prime Factors](../2507-smallest-value-after-replacing-with-sum-of-prime-factors/readme.md) | [link](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/) |
| 2520 | Easy | [Count the Digits That Divide a Number](../2520-count-the-digits-that-divide-a-number/readme.md) | [link](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
