# 0017. Letter Combinations of a Phone Number

## Quick Facts

- URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- Signature: `digits: str` → `list[str]`
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
- Run: `pytest -q -k "0017"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0022 | Medium | [Generate Parentheses](../0022-generate-parentheses/readme.md) | [link](https://leetcode.com/problems/generate-parentheses/) |
| 0039 | Medium | [Combination Sum](../0039-combination-sum/readme.md) | [link](https://leetcode.com/problems/combination-sum/) |
| 0401 | Easy | [Binary Watch](../0401-binary-watch/readme.md) | [link](https://leetcode.com/problems/binary-watch/) |
| 2266 | Medium | [Count Number of Texts](../2266-count-number-of-texts/readme.md) | [link](https://leetcode.com/problems/count-number-of-texts/) |
| 3014 | Easy | [Minimum Number of Pushes to Type Word I](../3014-minimum-number-of-pushes-to-type-word-i/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/) |
| 3016 | Medium | [Minimum Number of Pushes to Type Word II](../3016-minimum-number-of-pushes-to-type-word-ii/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
