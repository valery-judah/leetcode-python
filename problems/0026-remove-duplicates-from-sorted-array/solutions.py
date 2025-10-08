from __future__ import annotations


class Baseline:
    """
    This solution uses a two-pointer approach to remove duplicates in-place.
    'write_ptr' indicates the position for the next unique element.
    'read_ptr' iterates through the array to find unique elements.
    """

    def solve(self, nums: list[int]) -> int:
        # Handle the edge case of an empty list.
        if not nums:
            return 0

        # 'write_ptr' marks the position where the next unique element should be placed.
        # It starts at 1 because the first element (at index 0) is always
        # considered unique and is already in its correct place.
        write_ptr = 1

        # 'read_ptr' scans the array from the second element onwards to find unique elements.
        for read_ptr in range(1, len(nums)):
            # We've found a new unique element if it's different from the last
            # unique element we recorded. The last unique element is at 'write_ptr - 1'.
            if nums[read_ptr] != nums[write_ptr - 1]:
                # Place the new unique element at the write_ptr's position.
                nums[write_ptr] = nums[read_ptr]
                # Increment the write_ptr to prepare for the next unique element.
                write_ptr += 1

        # 'write_ptr' now holds the count of unique elements, which is the
        # length of the modified part of the array.
        return write_ptr


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

TEST_CASES = [
    (
        "example1",
        ([1, 1, 2],),
        {"k": 2, "nums": [1, 2]},
    ),
    (
        "example2",
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
        {"k": 5, "nums": [0, 1, 2, 3, 4]},
    ),
    ("types", ([0, 0, 0, 1, 1, 3],), {"k": 3, "nums": [0, 1, 3]}),
    ("empty_list", ([],), {"k": 0, "nums": []}),
    ("no_duplicates", ([1, 2, 3],), {"k": 3, "nums": [1, 2, 3]}),
]

#


# Optional: when all default tests pass, auto-mark this problem as optimal in stats.json
# Uncomment to enable once you are satisfied with your solution quality.
# TEST_MARK_OPTIMAL_ON_PASS = True

if __name__ == "__main__":
    import subprocess
    from pathlib import Path

    problem_dir = Path(__file__).parent
    problem_name = problem_dir.name
    spec_path = problem_dir.parent / "all_problems_spec.py"

    subprocess.run(
        ["pytest", "-q", str(spec_path), "-k", problem_name],
        check=False,
    )
