# 0582. Kill Process

## Quick Facts

- URL: [Kill Process](https://leetcode.com/problems/kill-process/)
- Function: `killProcess`
- Signature: `(pid: list[int], ppid: list[int], kill: int)  -> list[int]`
- Primary pattern: **Tree**

## Constraints

- `n == pid.length`
- `n == ppid.length`
- `1 <= n <= 5 * 10^4`
- `1 <= pid[i] <= 5 * 10^4`
- `0 <= ppid[i] <= 5 * 10^4`
- `Only one process has no parent.`
- `All the values of pid are unique.`
- `kill is guaranteed to be in pid.`

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
- Run: `pytest -q -k "0582"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.
```

### Example 2

```text
Input: pid = [1], ppid = [0], kill = 1
Output: [1]
```

## References

- LeetCode problem and editorial links
