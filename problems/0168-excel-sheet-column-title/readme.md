# 0168. Excel Sheet Column Title

## Quick Facts

- URL: [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)
- Function: `convertToTitle`
- Signature: `(columnNumber: int)  -> str`
- Primary pattern: **Math**

## Constraints

- `1 <= columnNumber <= 2^31 - 1`

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
- Run: `pytest -q -k "0168"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0171 | Easy | [Excel Sheet Column Number](../0171-excel-sheet-column-number/readme.md) | [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) |
| 2194 | Easy | [Cells in a Range on an Excel Sheet](../2194-cells-in-a-range-on-an-excel-sheet/readme.md) | [Cells in a Range on an Excel Sheet](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/) |
| 3484 | Medium | [Design Spreadsheet](../3484-design-spreadsheet/readme.md) | [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/) |

## Examples

### Example 1

```text
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
```

### Example 2

```text
Input: columnNumber = 1
Output: "A"
```

### Example 3

```text
Input: columnNumber = 28
Output: "AB"
```

### Example 4

```text
Input: columnNumber = 701
Output: "ZY"
```

## References

- LeetCode problem and editorial links
