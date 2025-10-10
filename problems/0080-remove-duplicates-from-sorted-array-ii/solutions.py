from __future__ import annotations
import pytest

class Baseline:
    def solve(self, nums: list[int] | None = None) -> dict[str, int | list[int]]:
        if not nums:
            return {"k": 0, "nums": []}

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
        return {"k": write_index, "nums": nums[:write_index]}


class Optimized:
    def solve(self, nums: list[int] | None = None) -> dict[str, int | list[int]]:
        if not nums:
            return {"k": 0, "nums": []}
        
        write_index = 0
        for num in nums:
            if write_index < 2 or num != nums[write_index - 2]:
                nums[write_index] = num
                write_index += 1
        return {"k": write_index, "nums": nums[:write_index]}

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    (
        "types",
        ([0, 0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5],),
        {"k": 9, "nums": [0, 0, 1, 2, 2, 3, 4, 4, 5]},
    ),
    ("empty_list", ([],), {"k": 0, "nums": []}),
]

@pytest.mark.parametrize(
    ("_, args, expected"),
    TEST_CASES,
)
def test_solutions(_, args, expected):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Pass a copy of the list to prevent mutation across test runs
        args_copy = (list(args[0]),)
        actual = solution.solve(*args_copy)
        assert actual == expected


if __name__ == "__main__":
    pytest.main([__file__])
