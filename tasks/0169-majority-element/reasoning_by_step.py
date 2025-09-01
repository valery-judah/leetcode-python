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
    c = None
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


def explain_trace(steps: List[Step]) -> None:
    """
    Pretty-print the reasoning. Each row shows how the invariant updates.
    - s/margin = vote margin (unpaired count of candidate)
    - When s hits 0, the processed prefix cancels to empty residue
    """
    header = f"{'i':>3} {'x':>6} | {'prev_c':>7} {'prev_s':>6} | {'action':>11} || {'c':>7} {'s/margin':>9}"
    print(header)
    print("-" * len(header))
    for st in steps:
        print(
            f"{st.i:3d} {str(st.x):>6} | {str(st.prev_c):>7} {st.prev_s:6d} | {st.action:>11} || {str(st.c):>7} {st.margin:9d}"
        )


def majority_element(nums: List[Any], show_steps: bool = True) -> Any | None:
    """
    Full pipeline:
      1) Run Boyer–Moore to obtain a candidate and detailed trace.
      2) Verify in a second pass. If not majority, return None.
    """
    candidate, steps = boyer_moore_with_trace(nums)
    if show_steps:
        print("=== Boyer–Moore step-by-step ===")
        explain_trace(steps)
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
    # Demo 1: has a majority (2 appears 4/7)
    arr1 = [2, 1, 2, 3, 2, 1, 2, 2, 2]
    print("\nDemo 1:", arr1)
    ans1 = majority_element(arr1, show_steps=True)
    print("Result:", ans1)

    # Demo 2: no majority
    arr2 = [1, 2, 3, 1, 2, 3]
    print("\nDemo 2:", arr2)
    ans2 = majority_element(arr2, show_steps=True)
    print("Result:", ans2)
