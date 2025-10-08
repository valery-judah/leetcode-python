from __future__ import annotations
from itertools import chain


class Baseline:
    def solve(self, word1: str = "", word2: str = "") -> str:
        parts = []
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            parts.append(word1[i])
            parts.append(word2[i])
        parts.append(word1[min_len:])
        parts.append(word2[min_len:])
        return "".join(parts)


class PythonicWay:
    def solve(self, word1: str = "", word2: str = "") -> str:
        pairwise_chunks = (a + b for a, b in zip(word1, word2, strict=False))
        tails = (word1[len(word2) :], word2[len(word1) :])
        return "".join(chain(pairwise_chunks, tails))

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, PythonicWay]

TEST_CASES = [
    ("types", ("ab", "lm"), "albm"),
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
