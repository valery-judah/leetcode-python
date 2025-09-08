# 0621. Task Scheduler

## Quick Facts

- URL: [Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- Function: `leastInterval`
- Signature: `(tasks: list[str], n: int)  -> int`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i] is an uppercase English letter.`
- `0 <= n <= 100`

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
- Run: `pytest -q -k "0621"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0358 | Hard | [Rearrange String k Distance Apart](../0358-rearrange-string-k-distance-apart/readme.md) | [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) |
| 0767 | Medium | [Reorganize String](../0767-reorganize-string/readme.md) | [Reorganize String](https://leetcode.com/problems/reorganize-string/) |
| 1953 | Medium | [Maximum Number of Weeks for Which You Can Work](../1953-maximum-number-of-weeks-for-which-you-can-work/readme.md) | [Maximum Number of Weeks for Which You Can Work](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/) |
| 2323 | Medium | [Find Minimum Time to Finish All Jobs II](../2323-find-minimum-time-to-finish-all-jobs-ii/readme.md) | [Find Minimum Time to Finish All Jobs II](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/) |
| 2365 | Medium | [Task Scheduler II](../2365-task-scheduler-ii/readme.md) | [Task Scheduler II](https://leetcode.com/problems/task-scheduler-ii/) |

## Examples

None

## References

- LeetCode problem and editorial links
