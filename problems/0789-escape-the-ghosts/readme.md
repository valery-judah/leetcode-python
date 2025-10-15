# 0789. Escape The Ghosts

## Quick Facts

- URL: [Escape The Ghosts](https://leetcode.com/problems/escape-the-ghosts/)
- Function: `escapeGhosts`
- Signature: `(ghosts: list[list[int]], target: list[int])  -> bool`
- Primary pattern: **Math**

## Constraints

- `1 <= ghosts.length <= 100`
- `ghosts[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- `There can be multiple ghosts in the same location.`
- `target.length == 2`
- `-10^4 <= xtarget, ytarget <= 10^4`

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
- Run: `pytest -q -k "0789"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                   | LeetCode                                                            |
| ------ | ---------- | ------------------------------------------------------ | ------------------------------------------------------------------- |
| 1728   | Hard       | [Cat and Mouse II](../1728-cat-and-mouse-ii/readme.md) | [Cat and Mouse II](https://leetcode.com/problems/cat-and-mouse-ii/) |

## Examples

### Example 1

```text
Input: ghosts = [[1,0],[0,3]], target = [0,1]
Output: true
Explanation: You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.
```

### Example 2

```text
Input: ghosts = [[1,0]], target = [2,0]
Output: false
Explanation: You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.
```

### Example 3

```text
Input: ghosts = [[2,0]], target = [1,0]
Output: false
Explanation: The ghost can reach the target at the same time as you.
```

## References

- LeetCode problem and editorial links
