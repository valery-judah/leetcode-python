`LC-0001-guide.md`

# Algorithmic Guide: LC-0001 Two Sum

This guide provides a comprehensive analysis of the "Two Sum" problem, moving from initial intuition to an optimal, robust solution. The goal is not merely to provide an answer, but to illuminate the problem-solving journey, revealing the core patterns and trade-offs that define high-quality software engineering.

______________________________________________________________________

# 1. The Discovery Path: From Brute-Force to Optimal

The path to an elegant solution is rarely a straight line. It begins with the most direct interpretation of the problem and is refined through a critical analysis of its performance bottlenecks.

## Initial Analysis & Brute Force

The problem asks: given an array of integers `nums` and an integer `target`, find the indices of the two numbers that add up to `target`. The prompt guarantees exactly one solution and prohibits using the same element twice.

The most intuitive, straightforward approach is to simulate the request directly. We can pick a number, then iterate through all the other numbers to see if any of them form a valid pair. This translates directly into a nested loop structure.

1. Start with the first element, `nums[i]`.

1. Iterate through the rest of the array with a second pointer, `nums[j]`, where `j` starts from `i + 1`.

1. For each pair `(nums[i], nums[j])`, check if their sum equals `target`.

1. If `nums[i] + nums[j] == target`, we have found our solution. We return the indices `[i, j]`.

This brute-force algorithm is correct; it exhaustively checks every possible pair and is guaranteed to find the single valid solution.

## Bottleneck Analysis

Why is this approach suboptimal? The answer lies in its **time complexity**. The outer loop runs approximately `n` times, and for each of those iterations, the inner loop also runs approximately `n` times. This results in a time complexity of O(n2).

Let's consider the problem's constraints: `nums.length` can be up to 104. An O(n2) algorithm would require roughly (104)2=108 operations. While this might pass, many similar problems feature constraints up to 105, which would lead to 1010 operations—far too slow for a typical 1-second execution limit. The bottleneck is clear: for each element, we are repeatedly re-scanning the array, performing redundant work.

## The "Aha!" Moment - The Key Insight

The critical insight comes from re-framing the question. Instead of asking "Does `nums[i]` plus any _other_ number equal the target?", we can ask, "For the current number `x`, does its _required complement_ exist in the array?"

If our current number is `x` and we're looking for `target`, its complement must be `y = target - x`. The problem is now transformed from a two-variable search into a series of single-variable searches: for each `x` in `nums`, does `y` exist?

This reframing is powerful because searching for a single item is a much more optimized operation than searching for a pair. How can we perform this search for the complement efficiently? We need a data structure that offers near-instantaneous lookups. This immediately brings the **hash map** (or dictionary) to mind, which provides average-case O(1) time complexity for lookups.

## Developing the Optimal Algorithm

Using this insight, we can develop a new algorithm that trades space for time. We'll use a hash map to store the numbers we've already seen and their corresponding indices.

1. Initialize an empty hash map, let's call it `seen_map`. This map will store `{number: index}` pairs.

1. Iterate through the `nums` array with an index `i` from `0` to `n-1`.

1. For each element `current_num = nums[i]`, calculate its required complement: `complement = target - current_num`.

1. Now, perform the key step: check if `complement` exists as a key in `seen_map`.

   - **If it exists**, we have found our pair. The solution is the index of the complement, which is `seen_map[complement]`, and the index of the current number, which is `i`. We can immediately return `[seen_map[complement], i]`.

   - **If it does not exist**, it means we haven't encountered the complement yet. We should store the current number and its index in our map so that future elements can find it. We add the key-value pair `{current_num: i}` to `seen_map`.

This one-pass hash map approach is remarkably efficient. We traverse the list only once, and for each element, we perform constant-time hash map operations (one lookup, one insertion). This yields a time complexity of O(n) and a space complexity of O(n) (since, in the worst case, we might store all `n` elements in the map). This is a classic and highly favorable trade-off of space for a significant improvement in time.

______________________________________________________________________

# 2. Systematic Test Case Construction: An Adversarial Approach

Good engineers don't just test if their code works; they actively try to break it. This "adversarial mindset" helps uncover edge cases that a simple "happy path" test would miss. We can systematically generate these cases using a technique called **Equivalence Class Partitioning**.

- **The "Happy Path" Class:** The standard, expected input.

  - `nums = [2, 7, 11, 15]`, `target = 9`

  - _Purpose:_ Verifies the basic logic works correctly.

  - _Expected Output:_ `[0, 1]`

- **The "Zero-Element" & "Singleton" Classes:**

  - _Note:_ The problem constraints (`2 <= nums.length`) make these invalid inputs. However, in a real-world system without these guarantees, testing `nums = []` and `nums = [5]` would be critical to ensure the code doesn't crash.

- **The "Boundary" Class:** Inputs that test the limits.

  - Solution at the start: `nums = [3, 5, -4, 8]`, `target = 8`

  - _Purpose:_ Checks if the algorithm works when the pair is the first two elements.

  - _Expected Output:_ `[0, 1]`

  - Solution at the end: `nums = [8, -4, 5, 3]`, `target = 8`

  - _Purpose:_ Checks if the algorithm works when the pair is the last two elements.

  - _Expected Output:_ `[2, 3]`

- **Problem-Specific Classes:** Unique cases derived from the problem's logic.

  - **Negative Numbers:** `nums = [-1, -3, 5, 90]`, `target = 4`

  - _Purpose:_ Ensures the logic is sound with negative integers.

  - _Expected Output:_ `[0, 2]`

  - **Zero Involvement:** `nums = [5, 0, -2, 4]`, `target = 2`

  - _Purpose:_ Verifies correct handling of zero as a value and in calculations.

  - _Expected Output:_ `[2, 3]`

  - **Duplicate Numbers as a Solution:** `nums = [6, 5, 3, 3]`, `target = 6`

  - _Purpose:_ This is a critical test. It ensures the algorithm finds two _distinct_ elements that have the same value.

  - _Expected Output:_ `[2, 3]`

  - **No Solution Exists:** `nums = [1, 2, 3]`, `target = 7`

  - _Purpose:_ The prompt guarantees a solution, but robust code should handle this case gracefully (e.g., by returning an empty array or raising an error). This tests the code's behavior when the loop completes without finding a match.

______________________________________________________________________

# 3. Common Pitfalls and Error Analysis

Even with a solid algorithm, implementation details can lead to subtle bugs. For Two Sum, the most common errors revolve around handling indices and duplicate values.

## The Core Pitfall: The "Self-Match Bug"

This bug occurs when an element is incorrectly matched with itself. Consider the input `nums = [3, 2, 4]` and `target = 6`.

1. The algorithm processes `nums[0]`, which is `3`.

1. It calculates the complement: `complement = 6 - 3 = 3`.

1. If the implementation is flawed, it might look up `3` and find it at index `0`, thus incorrectly returning `[0, 0]`.

- **Root Cause Analysis:** This error arises from a faulty order of operations in the one-pass hash map solution. If you **add the current element to the map _before_** you check for the complement, you create the possibility of finding the very element you just added.

- Prevention Strategy: The "Check-Then-Store" Pattern

  The robust prevention is simple and elegant: within the loop, always check for the complement's existence first, and only then add the current element to the map. This guarantees that any match found must be with an element that appeared earlier in the array, making a self-match impossible.

## Other Common Mistakes

1. **Returning Values Instead of Indices:** The problem explicitly asks for indices. A frequent mistake is to return `[current_num, complement]` instead of their positions.

1. **Mishandling Duplicates in a Two-Pass Approach:** If one were to implement a two-pass solution (first pass populates the map, second pass checks for complements), it's crucial to ensure the index found for the complement is not the same as the index of the current number. This requires an explicit check like `if (complement_index != i)`. The one-pass approach avoids this extra check.

1. **Off-by-One in Brute-Force:** In the brute-force solution, initializing the inner loop with `for j in range(i)` instead of `range(i + 1)` would lead to using the same element twice and finding incorrect solutions.

______________________________________________________________________

# 4. Reflection and Deeper Connections

Solving a single problem is useful; understanding the underlying pattern is transformative. This allows you to solve entire classes of problems.

## Distill the Core Pattern: Lookup Acceleration

The fundamental pattern at play is **trading space for time using a hash map**. This can be thought of as a form of "caching" or "memoization." We are pre-processing the array by storing its elements in a structure that allows for O(1) lookups. This accelerates the core operation of finding the complement from a linear O(n) search to a constant time O(1) lookup. This pattern is one of the most common and powerful in algorithm design.

## Pattern Application

Recognizing this pattern is key to solving many other problems. The core idea of "I need to quickly check if I've seen something before" should immediately trigger the thought of using a hash map or hash set.

- **LC-217: Contains Duplicate:** The simplest form of this pattern. Iterate through the array, adding elements to a hash set. If you ever try to add an element that's already in the set, you've found a duplicate.

- **LC-128: Longest Consecutive Sequence:** A more advanced application. By first storing all numbers in a hash set, you can perform O(1) checks to see if `num + 1` exists, allowing you to efficiently build consecutive sequences.

- Many substring and subarray problems, like finding the first non-repeating character, also rely heavily on this pattern to keep track of character counts or positions.

## Trade-Off Analysis

A senior engineering perspective involves constantly weighing trade-offs. The "Two Sum" problem presents a classic choice:

- **Brute-Force Solution:**

  - **Time:** O(n2)

  - **Space:** O(1)

  - _Analysis:_ Extremely space-efficient but too slow for large inputs. It's simple to conceptualize but impractical.

- **Hash Map Solution:**

  - **Time:** O(n)

  - **Space:** O(n)

  - _Analysis:_ The optimal solution for typical constraints. It makes a conscious trade-off, sacrificing memory to gain a massive improvement in runtime. In most scenarios, time is a more valuable resource than memory, making this the preferred approach.

- **Sort + Two Pointers (Conditional):** If the array could be modified, another approach exists: sort the array first (O(nlogn)) and then use two pointers (one at the start, one at the end) moving inwards (O(n)). This would have a total time complexity of O(nlogn) and a space complexity of O(1) or O(n) depending on the sort implementation. However, this approach is invalid for the original problem because sorting loses the original indices. This illustrates a crucial point: the constraints and requirements of a problem (like preserving original indices) dictate which patterns and trade-offs are viable.
