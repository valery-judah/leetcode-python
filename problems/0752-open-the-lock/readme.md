# 0752. Open the Lock

## Quick Facts

- URL: [Open the Lock](https://leetcode.com/problems/open-the-lock/)
- Function: `openLock`
- Signature: `(deadends: list[str], target: str)  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= deadends.length <= 500`
- `deadends[i].length == 4`
- `target.length == 4`
- `target will not be in the list deadends.`
- `target and deadends[i] consist of digits only.`

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
- Run: `pytest -q -k "0752"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                     | LeetCode                                                                                              |
| ------ | ---------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 2368   | Medium     | [Reachable Nodes With Restrictions](../2368-reachable-nodes-with-restrictions/readme.md) | [Reachable Nodes With Restrictions](https://leetcode.com/problems/reachable-nodes-with-restrictions/) |

## Examples

### Example 1

```text
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
```

### Example 2

```text
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
```

### Example 3

```text
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
```

## References

- LeetCode problem and editorial links
