### 1) Canonical Metadata

- **Identifier:** LC-0128

- **Title:** Longest Consecutive Sequence

- **Aliases/Patterns:** Hash Set, Unordered Set, Sequence Building

- **Category:** arrays, hash-table

- **Difficulty:** medium

### 2) Contract

- **Signature:** `longestConsecutive(nums: list[int]) -> int`

- **Input:** `nums`: An unsorted list of integers.

- **Output:** An integer representing the length of the longest consecutive elements sequence.

- **Constraints:**
    - `0 <= nums.length <= 10^5`

    - `-10^9 <= nums[i] <= 10^9`

    - The problem explicitly requires an **O(n) time complexity** solution.

### 3) Assumptions to Clarify

- **Input Validity:** The input will be a list of integers, conforming to the constraints.

- **Duplicates:** Duplicates should be ignored. For example, in `[1, 2, 2, 3]`, the longest consecutive
  sequence is `[1, 2, 3]`, with a length of 3.

- **Empty Input:** An empty list `[]` should result in a length of 0.

### 4) Core Representation / Invariant

- **Representation:** The core data structure is a **hash set** (a `set` in Python). This provides O(1)
  average time complexity for insertion, deletion, and lookups, which is essential for meeting the O(n) time
  constraint.

- **Invariant:** The algorithm's efficiency relies on the invariant that we only attempt to build a sequence
  starting from its true beginning. A number `n` is the start of a sequence if and only if `n-1` is not
  present in the input. By only initiating our search from these starting points, we guarantee that each
  number is visited as part of a sequence-building check at most once.

### 5) Discovery Path

- **Step 1: The Intuitive Sorting Approach.** The most direct way to find consecutive numbers is to have them
  in order. The first idea is to sort the input array `nums`. After sorting, we can iterate through the array
  in a single pass and count the length of the current consecutive sequence, updating a global maximum.

- **Step 2: Analyzing the Failure Mode.** The sorting approach is correct and relatively simple to implement.
  However, its time complexity is dominated by the sort, which is `O(n log n)`. The problem explicitly demands
  an `O(n)` solution. Therefore, this approach is not acceptable. This constraint is the primary driver for
  finding a different algorithm.

- **Step 3: The "Aha!" Moment — Identifying the Bottleneck.** The `O(n log n)` bottleneck is sorting. Why do
  we need to sort? To make it easy to check if the next consecutive number (`current_num + 1`) exists. This
  suggests the core problem is about efficient lookups. What data structure gives us O(1) lookups? A **hash
  set**.

- **Step 4: Formulating a Hash Set Approach.** We can start by converting the input list `nums` into a hash
  set to eliminate duplicates and enable fast lookups. Then, we can iterate through each number `n` in our
  set. For each `n`, we can check if `n+1`, `n+2`, `n+3`, etc., exist in the set, and count how long we can
  extend this sequence.

- **Step 5: Identifying the Redundancy.** Let's trace this idea with `nums = [100, 4, 200, 1, 3, 2]`.
    - When our loop gets to `n=100`, we check for `101` (not found). Sequence length 1.

    - When `n=4`, we check for `5` (not found). Sequence length 1.

    - When `n=1`, we check for `2`, then `3`, then `4`. Sequence length 4.

    - When `n=3`, we check for `4`. Sequence length 2.

    - When n=2, we check for 3, then 4. Sequence length 3.

        This works, but notice the massive redundant effort. The sequence 1-2-3-4 was fully or partially
        re-checked multiple times. In the worst case (a list of n consecutive numbers), this approach degrades
        to O(n²) time complexity.

- **Step 6: The Optimization — Finding Sequence Starts.** The redundant work comes from starting our counting
  process from the middle of a sequence. How can we ensure we only count each sequence once? By only starting
  our count from the absolute beginning of a sequence. How do we identify a number `n` as a "start"? A
  number `n` is a start if and only if `n-1` is not in the set.
    - By adding this simple check—`if n - 1 not in num_set`—we transform the algorithm. Now,
      for `[100, 4, 200, 1, 3, 2]`, the inner counting loop will *only* run for `n=100`, `n=200`, and `n=1`.
      The numbers `2`, `3`, and `4` will be skipped by the `if` condition, as their predecessors exist in the
      set. This eliminates all redundant work and achieves the desired O(n) performance.

### 6) Algorithms & Trade-offs

|                 |                                                                                                                                      |            |              |                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ------------ | -------------------------------------------------------------------------------- |
| **Method**      | **Idea**                                                                                                                             | **Time**   | **Space**    | **Notes**                                                                        |
| **A: Sorting**  | Sort the array, then iterate through it to find the longest run of consecutive numbers.                                              | O(n log n) | O(1) or O(n) | Fails to meet the problem's time complexity requirement. Simple to reason about. |
| **B: Hash Set** | Use a hash set for O(1) lookups. For each number, only start counting if it's the beginning of a sequence (`n-1` is not in the set). | O(n)       | O(n)         | Optimal solution. Meets all constraints. Requires extra space for the hash set.  |

### 7) Correctness Outline

The correctness of the optimized hash set approach relies on the fact that every number in `nums` belongs to
exactly one consecutive sequence (even if that sequence has a length of 1). The algorithm partitions the
numbers into these disjoint sequences.

- The outer loop iterates through every unique number `n` in the input.

- The `if n - 1 not in num_set` condition correctly identifies `n` as the smallest element (the "start") of
  its unique consecutive sequence.

- The inner `while` loop starts *only* for these starting elements and counts the length of that specific
  sequence.

- Since each sequence has only one starting element, the inner `while` loop will execute exactly once for each
  disjoint consecutive sequence in the input.

- Therefore, every number `n` is visited by the outer loop once, and it is part of the inner `while` loop's
  check (`current_num + 1`) at most once. This ensures the total work is proportional to `n`, and since we
  track the maximum length found, the final result is correct.

### 8) Complexity

- **Time:** O(n).
    - Building the initial hash set from the list `nums` takes O(n) time.

    - The outer loop runs `n` times (or fewer, if there are duplicates). Inside the loop, the `if` condition
      is an O(1) hash set lookup.

    - The inner `while` loop appears to make the algorithm O(n²), but it is amortized O(n). A number enters
      the `while` loop's check only if it is part of a sequence being counted. Since each number can only be
      part of one sequence, the total number of `while` loop increments across the entire algorithm is bounded
      by `n`.

    - Total complexity is O(n) + O(n) = O(n).

- **Space:** O(n). In the worst case, all numbers in the input list are unique, and we need to store all of
  them in the hash set.

### 9) Edge Cases

- **Empty list:** `[]` -> should return `0`.

- **Single element list:** `[100]` -> should return `1`.

- **List with duplicates:** `[1, 2, 0, 1]` -> should return `3`. The set will store `{0, 1, 2}`.

- **Negative numbers:** `[-2, -3, -4, 0, 1]` -> `[-4, -3, -2]` is the longest sequence, length `3`.

- **All elements consecutive:** `[1, 2, 3, 4]` -> should return `4`.

- **No consecutive elements:** `[10, 30, 50]` -> should return `1`.

### 10) Test Plan

- **General case:** `[100, 4, 200, 1, 3, 2]` → `4`.

- **Edge cases:**
    - `[]` → `0`

    - `[42]` → `1`

    - `[1, 1, 1, 1]` → `1`

    - `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` → `9`

### 11) Pitfalls Checklist

- [ ] **Violating Complexity:** Submitting the `O(n log n)` sorting solution.

- [ ] **Inefficient Hashing:** Using the unoptimized hash set approach that results in O(n²) checks. The key
  is to only check from sequence starts.

- [ ] **Duplicate Handling:** Incorrectly handling duplicates. Using a `set` automatically resolves this.

- [ ] **Off-by-one Errors:** Incorrectly calculating the length of the sequence inside the loop.

### 12) Interview Talk-Track (≤30s)

"A simple approach is to sort, but that's `O(n log n)`, which violates the `O(n)` constraint. To achieve
linear time, we need `O(1)` lookups, so I'll use a hash set. After populating a set with all the numbers, I'll
iterate through them. To avoid redundant work, I'll only start counting a sequence when I find its starting
number—which I can identify by checking that `num-1` is not in the set. This ensures we check each consecutive
sequence only once, giving us `O(n)` time with `O(n)` space."

### 13) Transfer / Adjacent Problems

- **Find First and Last Position of Element in Sorted Array (LC-34):** Involves finding the bounds of a
  "sequence" of identical numbers.

- **First Missing Positive (LC-41):** A hard problem that also deals with finding gaps in sequences of
  integers, often solved with clever in-place hashing.

- **Missing Number (LC-268):** Another problem that relies on properties of consecutive numbers.

### 14) Extensions

- **Find the Sequence:** Modify the function to return the longest consecutive sequence itself, not just its
  length.

- **2D Matrix Version:** Given a matrix of integers, find the longest path of consecutive numbers (allowing
  movement horizontally, vertically, and diagonally). This is a much harder problem requiring DFS/BFS with
  memoization.

- **Streaming Data:** How would you approach this problem if the numbers arrived in a stream and you have
  limited memory? (This would require probabilistic data structures or different approaches).

### 15) Decision Tree

```
Problem requires O(n) time?
  ├─ Yes: O(n log n) sorting is not allowed.
  │   └─ Need fast (O(1)) lookups to check for consecutive numbers.
  │       ├─ Data Structure Choice: Hash Set is ideal.
  │       │   └─ How to implement the check?
  │       │       ├─ Check every number for n+1, n+2... → Leads to O(n²) worst case.
  │       │       └─ Optimize: Only check from the start of a sequence.
  │       │           └─ How to find a start? → `if n-1 not in set`. This is the key.
  └─ No (or n is small): Sorting is a simple and acceptable solution.
```

### 16) Reflections & Guiding Questions

- **Conceptual Questions:**
    - "What is the specific operation that makes the sorting solution `O(n log n)`? And what operation in the
      optimal solution allows us to beat that?"

    - "Explain the concept of 'amortized analysis' in the context of the optimal solution's `while` loop. Why
      isn't it a true O(n²) algorithm?"

    - "If memory were extremely constrained (e.g., O(1) space allowed), but the `O(n log n)` time was
      acceptable, which algorithm would you choose and why?"

- **Process Reflection:**
    - "What was the most significant piece of information in the problem description that guided your entire
      algorithmic approach?" (The O(n) constraint).

    - "Describe the evolution of your thought process from the most naive solution to the most optimal one.
      What was the critical insight that bridged the gap?"

- **Generalization:**
    - "This problem uses a hash set to optimize lookups. What other categories of problems are often solved
      efficiently by converting a list to a hash set as a first step?" (e.g., Two Sum, checking for
      duplicates, set intersection/union).
