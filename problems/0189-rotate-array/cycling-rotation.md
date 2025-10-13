**Coach:** We have our array `nums` of size `n`, and we want to rotate it by `k`. We already have the reversal method, which is great. But it moves each element three times. Let's challenge ourselves with a constraint: **Can we move each element exactly once, directly to its final destination?**

Let's start with the simplest possible case. Take the very first element, `nums[0]`. Where does it belong in the final rotated array?

**You (Student):** It should go to index `(0 + k) % n`, which is just `k`.

**Coach:** Exactly. So, we can say `nums[k] = nums[0]`. But wait, what's the problem with that simple assignment?

**You:** We just overwrote the original value of `nums[k]` without saving it.

**Coach:** Perfect. So, before we move `nums[0]`, we must save the element that's currently in the destination. Let's put `nums[k]` into a temporary variable.

Now we have this element from `nums[k]` sitting in our hand. Where does _it_ need to go?

**You:** It should go to index `(k + k) % n`, or `2k % n`.

**Coach:** You've got it. And what about the element at `2k % n`?

**You:** We have to save it first, and then move the element from `k` into its place. I see a pattern... it's a chain.

**Coach:** Precisely. We have a chain of replacements. We start at an index, say `start_idx`, and we chase the elements through the array: the element from `start_idx` moves to `start_idx + k`, whose element moves to `start_idx + 2k`, and so on (all modulo `n`).

When does this chain reaction stop?

**You:** It must stop when we eventually loop back to our starting index, `start_idx`.

**Coach:** Exactly. When we loop back, the "hole" in the array is now at `start_idx`. What do we fill that hole with?

**You:** The very first element that we saved at the beginning of the chain.

**Coach:** Excellent. Let's trace this with a concrete example: `nums = [A, B, C, D, E, F]` where `n=6`, and `k=2`.

1. We start at index `0`. We save `A` in a `temp` variable.

1. The element at index `(0+2)%6=2` (which is `C`) needs to move to index `0`. Now `nums` is `[C, B, C, D, E, F]`.

1. The element at index `(2+2)%6=4` (which is `E`) needs to move to index `2`. Now `nums` is `[C, B, E, D, E, F]`.

1. The element at index `(4+2)%6=0`... ah, we're back to our starting point. The chain is `0 -> 2 -> 4 -> 0`.

1. Now we fill the last "hole" (at index 4) with our saved `temp` value, `A`.

1. The array is `[C, B, E, D, A, F]`. The elements `A`, `C`, and `E` are in their correct final positions.

We've completed one cycle. But are we done? Look at the array.

**You:** No. The elements at indices 1, 3, and 5 (`B`, `D`, `F`) haven't been touched.

**Coach:** So what is the logical next step?

**You:** We need to start another chain from the first index that we haven't touched yet, which is index `1`.

**Coach:** Perfect. Let's trace that second cycle starting at index 1: `1 -> (1+2)%6=3 -> (3+2)%6=5 -> (5+2)%6=1`. The cycle is `1 -> 3 -> 5 -> 1`. We'd perform the same swap-and-chase logic for these elements.

After these two cycles, all 6 elements will have been moved. Now for the most important question: how did we know there would be exactly **2** starting points (`0` and `1`)? If `n=7, k=3`, you'd find it's one big cycle.

We can't just check if every element has been "visited"—that's inefficient. We need a predictable, mathematical way to determine how many cycles there are. Any ideas what property of `n` and `k` might control this?

**You:** It must have something to do with how `k` divides `n`.

**Coach:** You're on the right track. This is a classic number theory result. The number of disjoint cycles in this process is always equal to the **Greatest Common Divisor (GCD)** of `n` and `k`.

- For `n=6, k=2`, `gcd(6, 2) = 2`. We found 2 cycles.

- For `n=7, k=3`, `gcd(7, 3) = 1`. There will be only 1 cycle.

- For `n=12, k=8`, `gcd(12, 8) = 4`. There will be 4 cycles, starting at indices 0, 1, 2, and 3.

**Coach:** So, can you now outline the complete, high-level algorithm?

**You:** Yes.

1. First, handle edge cases and normalize `k` with `k %= n`.

1. Calculate `g = gcd(n, k)`.

1. We will have `g` cycles to process. So, we loop `g` times, from `i = 0` to `g - 1`.

1. Each `i` in this loop is the starting index of a new, independent cycle.

1. For each cycle, we save the starting element, then chase the pointers around the array as we discussed, moving elements until we get back to the start.

**Coach:** That is a perfect description of the Juggling algorithm. You've derived it from first principles.

### Step-by-Step Algorithm Summary

Here is the formal algorithm we just developed:

1. **Handle Edge Cases**: If `nums` is empty, return.

1. **Normalize `k`**: `k = k % n`. If `k` is 0, no rotation is needed, so return.

1. **Determine Cycle Count**: Calculate `num_cycles = gcd(n, k)`. This is the number of independent sets of elements to rotate.

1. **Outer Loop (Iterate through cycles)**: Loop a variable `start_idx` from `0` to `num_cycles - 1`. Each `start_idx` is the starting point of a distinct cycle.
   \`\`

1. Inner Loop (Process a single cycle):

   a. Save the value of the first element in the cycle: `temp = nums[start_idx]`.

   b. Initialize a "current" pointer for this cycle: current_idx = start_idx.

   c. Start a do-while or equivalent loop to perform the chain of replacements:

   i. Calculate the next destination: next_idx = (current_idx + k) % n.

   ii. Move the element from next_idx into the current_idx position: `nums[current_idx] = nums[next_idx]`.

   iii. Move the current pointer forward: current_idx = next_idx.

   iv. Continue this loop until the pointer returns to the start: current_idx == start_idx.

   d. The cycle is complete. The "hole" is now at the position just before the start. Place the saved value into it: nums[current_idx] = temp.

1. After the outer loop finishes, the rotation is complete.
