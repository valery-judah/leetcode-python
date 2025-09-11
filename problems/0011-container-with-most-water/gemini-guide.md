### 1) Canonical Metadata

- **Identifier:** LC-0011

- **Title:** Container With Most Water

- **Aliases/Patterns:** two-pointer, greedy algorithm, window shrinking

- **Category:** arrays

- **Difficulty:** medium

### 2) Contract

- **Signature:** `maxArea(height: list[int]) -> int`

- **Input:** `height`: a list of non-negative integers representing vertical line heights.

- **Output:** An integer representing the maximum area of water the container can hold.

- **Constraints:** `n == height.length`, `2 <= n <= 10^5`, `0 <= height[i] <= 10^4`. These constraints imply that a solution with O(n²) time complexity will be too slow; an O(n) or O(n log n) solution is required.

- **Environment:** Python; standard library only.

### 3) Assumptions to Clarify

- **Input validity:** We assume the input list will always conform to the stated constraints. No special handling is needed for empty lists, lists with fewer than two elements, or lists with negative numbers, as these are ruled out by the problem definition.

### 4) Core Representation / Invariant

- **Representation:** The state of our algorithm is defined by two pointers, `l` and `r`, which start at the leftmost (`0`) and rightmost (`n-1`) indices of the `height` array, respectively. These represent the boundaries of the container being considered.

- **Invariant:** The key invariant is that the maximum possible area is either the largest area found so far, or it can be formed by a pair of lines within the current `[l, r]` window. We can safely and greedily shrink this window without discarding the optimal solution.

### 5) Discovery Path

- **Step 1: The Intuitive Brute-Force Approach.** The most straightforward way to solve this is to simply try every possible container. We can use one pointer `i` to fix the left wall and a second pointer `j` to try every possible right wall to the right of `i`. For each pair, we calculate the area and keep track of the maximum. This requires two nested loops.

- **Step 2: Analyzing the Failure Mode.** This O(n²) approach is correct, but the constraints tell us it will fail. With `n` up to `10^5`, `n²` is `10^10`, far too many operations for a typical 1-second time limit. This failure forces us to find a more intelligent way to search for the maximum area, one that doesn't require checking every single pair. We must find a way to eliminate large groups of candidate pairs at once.

- **Step 3: The "Aha!" Moment — From Brute Force to Greedy.** Let's reconsider the area formula: `Area = width * min(height[l], height[r])`. To get a large area, we need a large width and a large height. What if we start with the largest possible width? We can place our pointers `l` and `r` at the very ends of the array. This is our first candidate area. Now, to find a potentially better area, we must move one of the pointers inward. This will _always_ decrease the width. Therefore, the only way we can possibly find a larger area is if the new container's height is greater than the current one's.

- **Step 4: Formulating the Greedy Choice.** Suppose we are at `(l, r)` and `height[l]` is shorter than `height[r]`. The current area is limited by `height[l]`. If we move the right pointer `r` inward, the width will decrease, and the height will still be limited by `height[l]` (or an even shorter line at the new `r`). The area is guaranteed to not increase. But if we move the left pointer `l` inward, we abandon the shorter wall in hopes of finding a taller one. This is the only move that holds the _potential_ to increase the area. This insight is the core of the greedy strategy: at every step, eliminate the shorter of the two lines.

> #note (greedy logic) -> two pointer algorithm. So we don't just use two pointers out of thin air. But this is dictated by the logic of `max(V)` on more deeper level

- **Step 5: Choosing the Right Algorithm.** This greedy logic leads directly to the two-pointer algorithm. It processes the array in a single pass from the outside in, achieving the necessary O(n) time complexity.

### 6) Algorithms & Trade-offs

| **Method** | **Idea** | **Time** | **Space** | **Notes** |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------- | --------- | -------------------------------------------------------------------- |
| **A: Brute-force** | Use nested loops to check the area for all possible pairs of lines `(i, j)`. | O(n²) | O(1) | Simple to conceptualize but too slow for the given constraints. TLE. |
| **B: Two-pointer** | Start with pointers at `l=0` and `r=n-1`. At each step, calculate area and move the pointer of the shorter line inward. | O(n) | O(1) | Optimal. A greedy approach that correctly prunes the search space. |

### 7) Correctness Outline

The proof of correctness for the two-pointer algorithm rests on demonstrating that we never prematurely discard the pair of lines that form the optimal container.

- **Proof Idea:** Let the optimal container be formed by lines at indices `i*` and `j*`. We need to show that our algorithm eventually considers this pair or one with an equivalent area. The algorithm starts with `(l=0, r=n-1)`. Assume `height[l] < height[r]`. The algorithm moves `l` to `l+1`. We must prove that no discarded container `(l, k)` where `k < r` could have been optimal. Any such container would have area `(k - l) * min(height[l], height[k])`. This is strictly smaller than the area `(r - l) * height[l]` because both the width `(k-l < r-l)`and the height `(min <= height[l])` are smaller or equal. Thus, we can safely discard line `l`, knowing it cannot be the left boundary of the global optimal container. This logic applies symmetrically, guaranteeing the optimal solution is never discarded.

### 8) Complexity

- **Time:** O(n). In each step of the `while` loop, either `l` is incremented or `r` is decremented. The pointers start `n-1`steps apart and stop when they meet, resulting in a linear number of operations.

- **Space:** O(1). We only use a few variables to store the pointers and the max area.

### 9) Edge Cases

- **Minimum size input:** `[h1, h2]`.

- **Identical heights:** `[5, 5, 5, 5]`.

- **Sorted heights:** `[1, 2, 3, 4]` or `[4, 3, 2, 1]`.

- **U-shaped or V-shaped heights:** `[10, 1, 1, 10]`.

- **Heights including zero:** `[6, 0, 4]`.

### 10) Test Plan

- **General case:** `[1, 8, 6, 2, 5, 4, 8, 3, 7]` → 49.

- **Edge cases:** `[1, 1]` → 1; `[1, 2, 1]` → 2; `[4, 3, 2, 1, 4]` → 16.

- **Property tests:** The result must be non-negative. For any input `h`, `maxArea(h) == maxArea(reversed(h))`.

### 11) Pitfalls Checklist

- **Incorrect Complexity:** Implementing the O(n²) brute-force solution.

- **Incorrect Pointer Update:** Moving the pointer of the _taller_ line, which is a flawed greedy choice.

- **State Update Error:** Forgetting to update `max_area` inside the loop.

- **Loop Condition Error:** Using `l <= r` instead of `l < r`. A container needs positive width.

### 12) Interview Talk-Track (≤30s)

"A brute-force O(n²) solution is too slow. The optimal O(n) approach uses two pointers, starting at the ends to maximize width. The area is limited by the shorter line. To find a larger area, we must increase the limiting height, so we greedily discard the shorter line and move its pointer inward. This guarantees linear time and constant space."

### 13) Transfer / Adjacent Problems

- **Trapping Rain Water (LC-42):** Also uses a two-pointer approach, but the logic involves tracking left and right max heights.

- **Two Sum II - Input Array Is Sorted (LC-167):** The canonical two-pointer problem on a sorted array.

- **3Sum (LC-15):** Uses a two-pointer scan as an efficient inner loop after sorting.

### 14) Extensions

- **3D Version:** Find the maximum volume container from a 2D grid of heights.

- **Cost-based Optimization:** Maximize `area - cost[l] - cost[r]`.

- **Removal Allowed:** Maximize area after being allowed to remove up to `k` lines.

### 15) Decision Tree

```
Constraints n <= 10^5?
  ├─ Yes: O(n²) is too slow. Must find a near-linear time solution.
  │   └─ Does problem seek an optimal pair from opposite ends?
  │       ├─ Yes: The two-pointer pattern is a strong candidate.
  │       │   └─ Critical Step: Formulate the greedy choice. Prove which pointer to move (the one corresponding to the shorter, limiting line).
  └─ No (e.g., n <= 2000): O(n²) brute-force is acceptable.

```

### 16) Reflections & Guiding Questions

To foster a deeper understanding, one should reflect on the problem-solving process itself.

- **Conceptual Questions:**

  - "In your own words, what is the fundamental trade-off we are managing in this problem as we move the pointers?" (Answer: Width vs. Height).

  - "Why is the initial state with pointers at `l=0` and `r=n-1` the most logical starting point for our greedy algorithm?"

  - "Explain why moving the pointer of the _taller_ line is never a better decision than moving the pointer of the _shorter_ line."

- **Process Reflection:**

  - "What was the key piece of information in the problem statement that immediately told you a brute-force solution would be incorrect?" (The constraint `n <= 10^5`).

  - "Think back to the 'Aha!' moment. What was the specific insight that unlocked the O(n) solution for you?"

  - "Could this problem be solved using a different approach, like dynamic programming or divide and conquer? Why is the two-pointer method a more natural fit?"

- **Generalization:**

  - "Describe the 'two pointers from opposite ends' pattern in a general way. What characteristics of a problem suggest that this pattern might be applicable?"

# From ChatGPT

## 9) Pitfalls checklist (carried over from the anagram guide style)

- Move only the **shorter** side at each step.
- Compute and record area **before** advancing pointers.
- Width is `(j - i)`, not `(j - i + 1)`.
- Do not assume the optimal uses an endpoint; the sweep guarantees completeness.
- Avoid premature micro-optimizations; `O(n)` is already optimal.
- In non-Python languages, beware integer overflow.

______________________________________________________________________

## 10) Interview-ready summary (drop-in for README)

```md
**Model**: maximize `A(i,j) = (j - i) * min(h[i], h[j])`.

**Rule**: always advance the pointer at the **shorter** line.

**Why**: keeping the shorter side while shrinking width cannot increase the minimum; such pairs are dominated by the current pair.

**Correctness**: dominance + invariant over the shrinking window.

**Complexity**: `O(n)` time, `O(1)` space.
```

______________________________________________________________________
