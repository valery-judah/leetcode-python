from dataclasses import dataclass
from typing import Any, List, Tuple


@dataclass
class Step:
    i: int  # index in nums
    x: Any  # current element
    prev_c: Any | None  # candidate before seeing x
    prev_s: int  # count before seeing x
    action: str  # "pick", "inc", "dec", or "reset->pick"
    c: Any | None  # candidate after processing x
    s: int  # count after processing x
    margin: int  # same as s; named to emphasize the invariant


def boyer_moore_with_trace(nums: List[Any]) -> Tuple[Any | None, List[Step]]:
    """
    One-pass Boyer–Moore with full trace.
    Returns (candidate, steps). A second pass is needed to verify majority.
    """
    c: Any | None = None
    s = 0
    steps: List[Step] = []

    for i, x in enumerate(nums):
        prev_c, prev_s = c, s
        if s == 0:
            # empty residue -> start a new phase with x
            c = x
            s = 1
            action = "reset->pick" if prev_s == 0 and prev_c is not None else "pick"
        elif x == c:
            s += 1
            action = "inc"
        else:
            s -= 1
            action = "dec"

        steps.append(
            Step(i=i, x=x, prev_c=prev_c, prev_s=prev_s, action=action, c=c, s=s, margin=s)
        )
    return c, steps


def verify_majority(nums: List[Any], candidate: Any) -> Tuple[int, bool]:
    """Second pass to confirm candidate is a true majority (> n/2)."""
    cnt = sum(1 for x in nums if x == candidate)
    return cnt, cnt > len(nums) // 2


def explain_trace(
    nums: List[Any],
    steps: List[Step],
    *,
    show_table: bool = True,
    show_prefix: bool = True,
    show_suffix_marker: bool = True,
) -> None:
    """
    Pretty-print the reasoning with two complementary views:
    - Table (vote view): how (candidate, margin) evolves per step.
    - Prefix (pairing view): show the discovered prefix with canceled items marked as 'X'.

    Notes / legend:
    - margin (s) = unpaired count of the candidate (vote margin invariant).
    - action: pick/inc/dec (reset->pick is treated as pick).
    - 'X' marks items canceled away by pair deletion (not important anymore).
    - A star '★' marks the dominant suffix (after the last tie s==0).
    """

    # Find the last index where margin becomes 0 — start of dominant suffix (A4)
    last_zero_idx = max((st.i for st in steps if st.s == 0), default=-1)

    if show_table:
        header = (
            f"{'idx':>3} {'val':>5} | {'prev(c,s)':>12} | "
            f"{'op':>12} || {'cand':>5} {'margin':>6} | {'phase':>5}  prefix … {'res':>30}"
        )
        print(header)
        print("-" * len(header))

    # Pairing-view state: indices of currently-unpaired occurrences of the candidate
    unpaired_stack: list[int] = []
    # Track phase count (A6 in notes: phase structure): increment when s goes 0 -> 1
    phase = 0
    # Alive mask to print prefix; lazily extended as we go
    alive = [False] * len(nums)

    for st in steps:
        # Maintain phase number
        if st.prev_s == 0 and (st.action == "pick" or st.action == "reset->pick"):
            phase += 1

        # Update pairing view state to reconstruct which items are canceled.
        if st.action in ("pick", "reset->pick"):
            # Start new residue with x
            unpaired_stack.clear()
            unpaired_stack.append(st.i)
            alive[st.i] = True
        elif st.action == "inc":
            unpaired_stack.append(st.i)
            alive[st.i] = True
        elif st.action == "dec":
            # Cancel current x with one unpaired candidate occurrence.
            # Use LIFO (stack) so the current opponent cancels with the most
            # recent unmatched candidate, matching the step-by-step intuition
            # in the notes (nearest-left pairing).
            if unpaired_stack:
                j = unpaired_stack.pop()
                alive[j] = False
            # Current item is also canceled
            alive[st.i] = False

        # Build inline prefix rendering and a single-row output
        prefix_repr = (
            "[" + " ".join((str(nums[j]) if alive[j] else "X") for j in range(st.i + 1)) + "]"
        )
        margin_bar = "|" * st.s  # quick visual for margin size
        suffix_mark = "★" if show_suffix_marker and st.i > last_zero_idx else " "

        if show_table and show_prefix:
            res_str = f"res: {str(st.c)} x{st.s} {margin_bar}"
            print(
                f"{st.i:3d} {str(st.x):>5} | "
                f"{(str(st.prev_c) + ',' + str(st.prev_s)):>12} | "
                f"{st.action:>12} || {str(st.c):>5} {st.s:6d} | {phase:5d}{suffix_mark}  "
                f"{prefix_repr} {res_str:>30}"
            )
        elif show_table:
            print(
                f"{st.i:3d} {str(st.x):>5} | "
                f"{(str(st.prev_c) + ',' + str(st.prev_s)):>12} | "
                f"{st.action:>12} || {str(st.c):>5} {st.s:6d} | {phase:5d}{suffix_mark}"
            )
        elif show_prefix:
            res_str = f"res: {str(st.c)} x{st.s} {margin_bar}"
            print(
                f"i={st.i:2d} val={st.x} op={st.action} cand={st.c} s={st.s} \
                    phase={phase}{suffix_mark} "
                f"{prefix_repr} {res_str:>20}"
            )


def majority_element(nums: List[Any], show_steps: bool = True) -> Any | None:
    """
    Full pipeline:
      1) Run Boyer–Moore to obtain a candidate and detailed trace.
      2) Verify in a second pass. If not majority, return None.
    """
    candidate, steps = boyer_moore_with_trace(nums)
    if show_steps:
        print("=== Boyer–Moore step-by-step (vote + pairing views) ===")
        print("Legend: action ∈ {pick, inc, dec}; 'X' = canceled; ★ = dominant suffix")
        explain_trace(nums, steps, show_table=True, show_prefix=True, show_suffix_marker=True)
        print("\nCandidate after first pass:", candidate)

    if candidate is None:
        if show_steps:
            print("No candidate found.")
        return None

    count, ok = verify_majority(nums, candidate)
    if show_steps:
        print(f"Verification: count({candidate}) = {count} / n = {len(nums)} -> majority? {ok}")
    return candidate if ok else None


if __name__ == "__main__":

    def check_case(nums: List[Any], expected: Any | None) -> None:
        print("\nCase:", nums)
        cand, steps = boyer_moore_with_trace(nums)
        # Step-level invariants from the notes (vote margin and updates)
        for st in steps:
            assert st.margin == st.s
            if st.prev_s == 0 and st.action in ("pick", "reset->pick"):
                # Starting a new phase picks x as candidate with s=1
                assert st.c == st.x
                assert st.s == 1
            elif st.action == "inc":
                assert st.c == st.prev_c
                assert st.s == st.prev_s + 1
            elif st.action == "dec":
                assert st.c == st.prev_c
                assert st.s == st.prev_s - 1

        # Full pipeline check with verification
        res = majority_element(nums, show_steps=True)
        if expected is None:
            assert res is None
        else:
            assert res == expected

        # Second-pass verification agrees with expectation
        if cand is not None:
            cnt, ok = verify_majority(nums, cand)
            if expected is None:
                assert not ok
            else:
                assert ok
                assert cnt > len(nums) // 2

    # Majority present (problem examples)
    check_case([3, 2, 3], 3)
    check_case([2, 2, 1, 1, 1, 2, 2], 2)

    # Single element
    check_case([1], 1)

    # All equal
    check_case([7, 7, 7, 7, 7], 7)

    # Majority with multiple phases and resets
    check_case([2, 1, 2, 3, 2, 1, 2, 2, 2], 2)

    # No majority (odd and even length)
    check_case([1, 2, 3, 1, 2, 3], None)
    check_case([1, 2, 1, 2], None)

    # Empty input (no candidate, no majority)
    check_case([], None)

    # Negative numbers
    check_case([-1, -1, -1, 2, 3, -1, 4, -1], -1)

    # Clear majority late in the array
    check_case([0, 1, 0, 1, 0, 1, 1, 1, 1], 1)
