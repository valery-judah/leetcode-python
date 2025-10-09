from __future__ import annotations


class Baseline:
    def solve(self, nums: list[int] | None = None) -> int:
        if nums is None or len(nums) == 0:
            return 0

        allowed_duplicates = 1

        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
                allowed_duplicates = 1
            elif allowed_duplicates == 1:
                nums[write_index] = nums[read_index]
                write_index += 1
                allowed_duplicates -= 1
        return write_index


class CounterBasedRefactor:
    def solve(self, nums: list[int] | None = None) -> int:
        if not nums:
            return 0
        write_index = 0
        remaining_writes = 0
        for num in nums:
            is_new_number = (write_index == 0) or (num != nums[write_index - 1])
            if is_new_number or remaining_writes > 0:
                if is_new_number:
                    remaining_writes = 1
                else:
                    remaining_writes -= 1
                nums[write_index] = num
                write_index += 1
        return write_index


class LookBehind:
    def solve(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # Boundary conditions: we can always keep the first two elements
        write_pointer = 2

        for read_pointer in range(2, len(nums)):
            # The core condition: if the current element is not the same as the
            # element two positions before the write_pointer, it's safe to write.
            # This elegantly handles both new numbers and the second occurrence of a number.
            if nums[read_pointer] != nums[write_pointer - 2]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        return write_pointer


class LookBehindLoop:
    def solve(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write_index = 0
        for num in nums:
            # We can place the current number if:
            # 1. We are filling the first two spots in the array (write_index < 2).
            # 2. The current number is NOT the same as the number two spots
            #    behind the write pointer. This prevents a third duplicate.
            if write_index < 2 or num != nums[write_index - 2]:
                nums[write_index] = num
                write_index += 1
        return write_index


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, LookBehind, CounterBasedRefactor, LookBehindLoop]

TEST_CASES = [
    ("types", ([0, 0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5],), 9),
    ("empty_list", ([],), 0),
]


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
