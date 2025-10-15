# 1834. Single-Threaded CPU

## Quick Facts

- URL: [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)
- Function: `getOrder`
- Signature: `(tasks: list[list[int]])  -> list[int]`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `tasks.length == n`
- `1 <= n <= 10^5`
- `1 <= enqueueTimei, processingTimei <= 10^9`

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
- Run: `pytest -q -k "1834"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                       | LeetCode                                                                                                |
| ------ | ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| 2050   | Hard       | [Parallel Courses III](../2050-parallel-courses-iii/readme.md)                             | [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/)                             |
| 2589   | Hard       | [Minimum Time to Complete All Tasks](../2589-minimum-time-to-complete-all-tasks/readme.md) | [Minimum Time to Complete All Tasks](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) |

## Examples

### Example 1

```text
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows:
- At time = 1, task 0 is available to process. Available tasks = {{0}}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {{}}.
- At time = 2, task 1 is available to process. Available tasks = {{1}}.
- At time = 3, task 2 is available to process. Available tasks = {{1, 2}}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {{1}}.
- At time = 4, task 3 is available to process. Available tasks = {{1, 3}}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {{1}}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {{}}.
- At time = 10, the CPU finishes task 1 and becomes idle.
```

### Example 2

```text
Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {{0,1,2,3,4}}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {{0,1,2,3}}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {{0,1,2}}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {{0,1}}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {{1}}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {{}}.
- At time = 40, the CPU finishes task 1 and becomes idle.
```

## References

- LeetCode problem and editorial links
