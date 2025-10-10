from __future__ import annotations


class Baseline:
    def solve(self, numbers: list[int], target: int) -> list[int]:
        if len(numbers) < 2:
            return [-1, -1]

        left, right = 0, len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return [-1, -1]


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

TEST_CASES = [
    ("types", ([1, 2, 3], 4), [1, 3]),
    ("empty_list", ([], 0), [-1, -1]),
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
