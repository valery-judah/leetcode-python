# 0128. Longest Consecutive Sequence

## Quick Facts

- URL: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- Function: `longestConsecutive`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

Brute-force would be O(n!) where we have to scan input array for each of elements in the sequence.
Ok, let's start with: 'if we have some element as current' What operation do we want to do? Check if (nums[i] + 1) (or minus) is presented in the input array. So we want a structure that could allow us to conduct a search by value with minimal time. What information do we want to save? Just membership? How we can scan

My initial plan was to scan the array once to build a hash set of all its elements. The next step would be to find the overall minimum element and start checking for the length of its consecutive sequence. However, a problem arises after reaching the end of one sequence: how to find the start of the next one? Given the large range of possible values (-10^9 \<= nums[i] \<= 10^9), simply iterating through all numbers to find the next sequence is not feasible.

A more effective strategy (that is gemini provided, but I've stuck) is to use a unique property that the hash set enables us to identify quickly: is the current element the start of a sequence? An element is the start of a new sequence if and only if its predecessor (element - 1) is not in the hash set.

Given that we can use another iteration / looping strategy. (for me it's important - you can correct me) So, we can iterate not through all values diapason but through the original numbers and only trigger the full sequence-length calculation for elements that are confirmed to be starting points. This avoids redundant computations for elements in the middle of a sequence.

#reflection

Of course. This is an excellent question because it moves beyond finding _the_ solution and into understanding _how to invent_ such a solution. Your analysis of your own thought process is very clear and provides the perfect foundation for this exploration.

Let's break down your logic and identify the specific mental tools and technical strategies that bridge the gap between your initial plan and the optimal one.

### 1. Analysis of Your Initial (and Very Common) Thought Process

Your initial plan was logical and demonstrates a solid understanding of the problem's core needs.

- **Correct Instinct:** You correctly identified that an `O(n)` solution requires fast lookups, leading you to the hash set. This is the most critical first step.

- The Mental Trap: The Search for a "Global Order"

  Your plan to "find the overall minimum element and start checking" is a natural human tendency. We are comfortable with linear, ordered processes. You tried to impose a familiar structure (start at the absolute beginning and work your way up) onto the problem.

- **The Sticking Point:** You correctly identified why this fails: the sequences are sparse and independent. After processing the sequence starting at `min(nums)`, there is no efficient way to find the start of the \_next_disjoint sequence because the values can be billions of integers apart. You can't just scan from where you left off.

This sticking point is the precise location where a new mental model is needed.

### 2. The Mental Shift: From "What's Next?" to "What's Special?"

The breakthrough comes from changing the fundamental question you are asking.

- Your initial question was: "After I process one sequence, how do I find the **next one** to process?" This implies a sequential, ordered search.

- The optimal question is: "For any given number `n` from the input, how do I know if it's **special**? Specifically, is it the **start** of a sequence?"

This shift moves you from a stateful search across a vast number range to a stateless check on the properties of the numbers you actually have. This is the key insight.

### 3. Toolkit to Invent the "Start of Sequence" Approach

Here are the specific techniques and mental models that would have helped you invent this "start of a sequence" check.

#### **Technique 1: The "Redundant Work" Audit**

This is a powerful optimization heuristic. After you develop a brute-force or semi-optimized approach, perform a mental trace and ask: **"What work am I doing more than once?"**

- **Your thought process could have been:**

  1. "My first idea is to iterate through every number `n` in my set and, for each one, check for `n+1`, `n+2`, etc., to find the sequence length."

  1. "Let's trace `[100, 4, 200, 1, 3, 2]`. When I get to `n=1`, I'll find the sequence `1-2-3-4` (length 4). Later, when my loop gets to `n=2`, I'll find `2-3-4` (length 3). When I get to `n=3`, I'll find `3-4` (length 2)."

  1. **Audit Result:** "I am repeatedly calculating the length of the _tails_ of sequences I've already fully explored. This is redundant. How can I ensure I only ever calculate the length of a given sequence _exactly once_?"

This audit naturally leads to the conclusion that you must only perform the calculation from a single, canonical starting point.

#### **Technique 2: The "Start of a Work Unit" Heuristic**

This is the generalization of the previous point. For many problems that require processing groups, clumps, or sequences, the key to an `O(n)` solution is to define what uniquely identifies the **start of a work unit**.

- **Your thought process could have been:**

  1. "The redundant work audit shows I need to process each sequence only once. To do that, I must only trigger my calculation when I'm at the beginning of a sequence."

  1. "How do I define 'the beginning of a sequence' using only the data I have (the hash set)?"

  1. **Property Definition:** "A number `n` is the start of a sequence _if and only if_ its predecessor, `n-1`, is not available."

  1. "My hash set can check for the existence of `n-1` in `O(1)` time. This is the perfect tool to implement this check."

This heuristic transforms the problem from "find all sequences" to "find all sequence-starters."

#### **Technique 3: Shifting the Iteration Domain**

This technical strategy is about being very precise about _what_ you are looping over.

- **Your initial plan's iteration domain:** The vast, continuous range of integers from `min(nums)` upwards. This domain is too large.

- **The optimal plan's iteration domain:** The small, discrete set of numbers provided in the `nums` array itself.

The mental tip is to always ask: **"Is my loop iterating over indices, the input values themselves, or a continuous range of numbers?"** The problem's constraints (`-10^9 <= nums[i] <= 10^9`) are a massive hint that you absolutely cannot iterate over the continuous range. You _must_ iterate only over the `N` elements you are given.

### A Revised Thought Process (Applying the Toolkit)

Here is how you could have systematically arrived at the solution:

1. **Analyze Constraints:** "The problem demands `O(n)` time. This immediately disqualifies sorting (`O(n log n)`). I need a method that relies on `O(1)` operations."

1. **Select Data Structure:** "For fast lookups (`is this number present?`), a hash set is the ideal tool. My first step will be to put all numbers from `nums` into a `set`."

1. **Formulate Initial (Slightly Inefficient) Loop:** "I can iterate through each `num` in my new set. For each `num`, I'll start a `while` loop to check for `num+1`, `num+2`, etc., to find the length of the sequence starting there."

1. **Perform "Redundant Work" Audit:** "Wait. If I do that, I'll be re-checking the tails of sequences. That feels inefficient, possibly `O(n²)` in the worst case (a single long sequence)."

1. **Apply "Start of a Work Unit" Heuristic:** "To eliminate the redundancy, I need to ensure I only run my `while` loop once per sequence. I will only run it from the very first element of any given sequence. What property does a first element `n` have? Its predecessor, `n-1`, is not in the set."

1. **Refine the Algorithm:** "My final algorithm is:

   - Create the hash set.

   - Loop through each `num` in the set.

   - **Add a gate:** `if num - 1 not in my_set:`

   - Inside this `if` block, and only inside it, run the `while` loop to count the full sequence length.

   - Keep track of the maximum length found."

This structured process, especially the **Redundant Work Audit** and the **Start of a Work Unit Heuristic**, provides a reliable path from a correct-but-slow idea to the efficient, optimal solution. #heuristics

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
- Run: `pytest -q -k "0128"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0298 | Medium | [Binary Tree Longest Consecutive Sequence](../0298-binary-tree-longest-consecutive-sequence/readme.md) | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) |
| 2177 | Medium | [Find Three Consecutive Integers That Sum to a Given Number](../2177-find-three-consecutive-integers-that-sum-to-a-given-number/readme.md) | [Find Three Consecutive Integers That Sum to a Given Number](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/) |
| 2274 | Medium | [Maximum Consecutive Floors Without Special Floors](../2274-maximum-consecutive-floors-without-special-floors/readme.md) | [Maximum Consecutive Floors Without Special Floors](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/) |
| 2414 | Medium | [Length of the Longest Alphabetical Continuous Substring](../2414-length-of-the-longest-alphabetical-continuous-substring/readme.md) | [Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) |
| 3020 | Medium | [Find the Maximum Number of Elements in Subset](../3020-find-the-maximum-number-of-elements-in-subset/readme.md) | [Find the Maximum Number of Elements in Subset](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/) |

## Examples

### Example 1

```text
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2

```text
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

### Example 3

```text
Input: nums = [1,0,1,2]
Output: 3
```

## References

- LeetCode problem and editorial links
