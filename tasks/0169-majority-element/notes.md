
# 169. Majority Element

**URL**: <https://leetcode.com/problems/majority-element/>
**Difficulty**: easy
**Tags**: array,hash-table,divide-and-conquer,sorting,counting

## Clarifying Questions

- Input size, value ranges, and guarantee of a majority?
- Are negatives allowed? Are duplicates typical? Any empty input cases?
- Can we mutate the array? Is streaming or one-pass required?

## Examples

- `[3,2,3]` → `3`
- `[2,2,1,1,1,2,2]` → `2`
- `[1]` → `1`

## Approach (Overview)

- Recommended: Boyer–Moore majority vote (O(n) time, O(1) space).
- Alternatives: Counter/Hash Map (O(n) time, O(n) space), Sorting (O(n log n) time), Divide & Conquer (O(n log n)), Bit manipulation (O(n)).
- If majority is not guaranteed, add a verification pass to confirm the candidate.

## Checklist

- [ ] Restate problem
- [ ] Small example walkthrough
- [ ] Choose DS/algorithm
- [ ] Dry-run core loop
- [ ] Code cleanly
- [ ] Test edge cases

See also: `docs/interview-framework.md`.

# Flow

So, how should we start thinking about this problem?

The first thought that comes to mind is to calculate the count of all elements and choose the most frequent.

# todo use a hashmap/counter; use the library and also implement it yourself

If we want to optimize time or space, we need to understand what can be improved.

Now, #idea #todo formulate

We don't need to compute counts for every element. We just need to understand something about the most frequent element—some invariant related to it. How should we name this invariant?

What do we have from the problem statement? The majority element appears more than n/2 times.

Reflection: I can intuitively arrive at a vague idea of comparing frequencies between the most common element and the others.

An LLM proposed this when I asked about an invariant: Let's call the invariant the vote margin (a.k.a. surplus, balance, or unpaired majority count). It is the number of currently unpaired occurrences of the candidate.

Question: how do we arrive at the algorithm?

[??] --> algorithm

The algorithm proceeds in two main phases (in common case):

Finding a Candidate:

Initialize two variables: count to 0 and candidate to store a potential majority element.

Iterate through the input sequence.

If count is 0, set the current element as the candidate and increment count.

If the current element is the same as the candidate, increment count.

If the current element is different from the candidate, decrement count.

> [!note] The intuition behind this phase is that each non-candidate element effectively "cancels out" one instance of the candidate. If a true majority element exists, it will eventually emerge as the candidate at the end of this pass because its occurrences will outnumber the cancellations. <- this one is interesting

**Second Phase. Verifying the Candidate:**

- After the first pass, the `candidate` variable holds a potential majority element. However, this element is not guaranteed to be the majority element (e.g., if no majority element exists in the input).
- Perform a second pass through the input sequence.
- Count the actual occurrences of the `candidate` found in the first pass.
- If this count is greater than N/2, then the `candidate` is indeed the majority element. Otherwise, there is no majority element in the sequence.

Correctness can be found in the wiki article on the [Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm).

[visualization script](/tasks/0169-majority-element/reasoning_by_step.py).

Terminology. Let's call the invariant the **vote margin** (a.k.a. **surplus**, **balance**, or **unpaired majority count**). It is the number of currently **unpaired** occurrences of the candidate.

Your goal in the first phase is to find a value with the maximum margin (count).

After processing any prefix:

- All unpaired items are equal to `candidate`.
- `margin` equals the number of these unpaired items.

The intuition behind this phase is that each non-candidate element effectively "cancels out" one instance of the candidate. If a true majority element exists, it will eventually emerge as the `candidate` at the end of this pass because its occurrences will outnumber the cancellations.

# Why it works

**Pairing/cancellation view.** Each time you see a non-candidate while `count > 0`, you cancel it against one candidate vote. This simulates removing opposite votes in pairs. Since a true majority `m` satisfies `#m > n/2`, after maximal cancellation at least one `m` remains. The algorithm’s candidate at the end is exactly the element that survives this cancellation.

# Majority by Cancellation: a concise derivation of Boyer–Moore

## **0) Use-case summary**

Find an element occurring > n/2 times in a stream with O(1) memory and one pass, then verify. Pattern generalizes to “heavy hitters” > n/k.

---

## 1) Problem Model

- Input: sequence $x_1,\dots,x_n$.
- Goal: return m with \#(m) > n/2, or report none.
- Constraints: streaming, constant memory, adversarial order allowed.

## 2) Design target

Maintain a **state** that:

1. is sufficient to reconstruct the majority at the end if it exists,
2. fits in O(1) space,
3. updates in O(1) per item.

You cannot keep per-value counts. You must compress online.

## **3) From counting to cancellation**

Key equivalence on any multiset S:

**Delete unequal pairs in any order.** The residue is either `empty` or `k` copies of a single value.

Reason: each deletion reduces size by 2 without changing which value (if any) exceeds half. If a majority exists, it cannot be fully paired away.

**Target:** compute this residue **online**. If residue is non-empty, its value is the majority.

## **4) Minimal sufficient state**

For the current processed prefix, the residue is fully described by:

- candidate c: the surviving value if residue non-empty,
- count $s\ge 0$: the size of the residue.

No other information is needed. This is the **vote margin** (a.k.a. surplus/balance).

## **5) Update rule (derived)**

Let next item be x.

- If s=0: residue is empty. Start new residue with x. Set c:=x, s:=1.
- Else if x=c: residue grows. Set s:=s+1.
- Else: delete a mismatched pair (c,x). Set s:=s-1.

This exactly simulates pair deletion online.

## **6) Phase structure**

A **phase** runs from one time s becomes 0 to the next. While in a phase,

`s = n(candidate) - n(others)` over that phase’s items, and it is never negative. Hitting 0 ends the phase and forgets the past.

## **8) Correctness skeleton**

- **Lemma 1 (pair-deletion normal form):** Deleting unequal pairs is confluent; outcome is unique up to multiplicity.
- **Lemma 2 (state = residue):** The update rule maintains the pair-deletion residue online: after any prefix, (c,s) equals (value, size) of the residue.
- **Lemma 3 (majority survives):** If a majority exists on the whole sequence, the residue is non-empty and equals that majority.
- **Theorem:** Final candidate equals the majority.
- **Non-promise:** Verify candidate in a second pass.

## **9) What to remember for reuse**

**Pattern name:** majority by cancellation with a vote margin potential.

**Recipe:**

1. Identify a property invariant under deleting “opposite” pairs that preserves the target.
2. Show the normal form is either empty or one value repeated.
3. Maintain (candidate, margin) that equals that normal form online.
4. Add a verification pass when the property might not hold globally.

## **15) Checklist before using**

- Majority or heavy-hitter threshold known and fixed.
- Stream can be processed in one pass.
- Verification feasible.
- For > n/k, set k and use Misra–Gries.
- For weights, adjust increments.
- For distributed data, plan per-shard residues + reduction.

# Online Term

“Online” means: process each item as it arrives, update a small state, and move on. No full input in memory. No revisiting earlier items. One (or a few) passes.

Clarify the term in this context:

- **Model:** streaming input $x_1,x_2,\dots,x_n$. You maintain a tiny summary S_t and update S_{t+1}=f(S_t,x_{t+1}).

- **Constraints:** sublinear space (often O(1) or O(k)), O(1) work per item, order may be adversarial.

- **Implication:** you cannot keep per-value counts or sort. You **compress online** into invariants like the **vote margin** instead of storing full frequency tables.

- **Verification:** because you summarized aggressively, you often need a cheap second pass to confirm a claim (e.g., count the candidate).

# Interesting or Important Moments

- Not a frequency estimator — it returns only a candidate.
- If a majority may not exist, verification is required.
- Composition: summaries should be mergeable (e.g., combine residues across shards).
- Use when streaming, memory-constrained, or latency-sensitive with O(1) updates.

See also: `docs/interview-framework.md`.
