from __future__ import annotations


class Baseline:
    def solve(self, nums: list[int] | None = None) -> int:
        max_length = 0
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            current_length = 1
            for j in range(i + 1, len(sorted_nums)):
                if sorted_nums[j] == sorted_nums[j - 1] + 1:
                    current_length += 1
                elif sorted_nums[j] != sorted_nums[j - 1]:
                    break
            max_length = max(max_length, current_length)
        return max_length


class Optimized:
    def solve(self, nums: list[int] | None = None) -> int:
        num_set = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 in num_set:
                continue
            else:
                # Start of a new sequence
                # Calculate its length
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("non-empty", ([100, 3, 10, 2, 4],), 3),
    ("empty_list", ([],), 0),
    ("single-element", ([2],), 1),
    ("with_negatives", ([0, -1, 1, 2, -2],), 5),
    ("with_duplicates", ([1, 2, 2, 3],), 3),
    ("large_range", (list(range(10000)),), 10000),
    ("unsorted_large_range", ([10, 5, 12, 3, 55, 4, 11, 2],), 4),
    ("no_consecutive", ([10, 20, 30],), 1),
    ("all_same", ([7, 7, 7, 7],), 1),
    ("mixed", ([1, 9, 3, 10, 4, 20, 2],), 4),
    ("negative_and_positive", ([-1, 0, 1, 2, -2, -3],), 6),
    ("large_with_gaps", (list(range(1, 1000)) + [2000, 3000, 4000],), 999),
    ("single_large_gap", ([1, 2, 3, 50, 51, 52],), 3),
    ("two_large_gaps", ([1, 2, 3, 100, 101, 102, 200, 201],), 3),
    ("negative_large_gap", ([-10, -9, -8, 0, 1, 2],), 3),
    ("mixed_with_negatives", ([5, 6, -1, -2, -3, 0],), 4),
    ("large_negative_range", (list(range(-1000, 0)),), 1000),
    ("large_positive_and_negative", (list(range(-500, 500)),), 1000),
    ("sparse_large_range", ([1, 100, 200, 300, 400, 500],), 1),
    ("consecutive_at_ends", ([1, 2, 3, 50, 51, 52, 100, 101, 102],), 3),
    ("long_consecutive_with_noise", ([10, 11, 12, 1, 2, 3, 20, 21],), 3),
    ("all_negatives", ([-5, -4, -3, -2, -1],), 5),
    ("negatives_with_gaps", ([-10, -9, -7, -6, -5],), 3),
    ("large_mixed", ([1000, -1000, 999, -999, 998, -998],), 3),
    ("complex_case", ([0, -1, -2, 2, 1, 3, -3],), 7),
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
