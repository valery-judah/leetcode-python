#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import leetcode_index

ROOT = Path(__file__).resolve().parents[1]


def get_problem_id_from_path(path: Path) -> str | None:
    """Extracts the problem ID from a given file path by searching its parts."""
    for part in reversed(path.parts):
        match = re.search(r"^(\d{4})-", part)
        if match:
            return match.group(1)
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new attempt branch for a LeetCode problem.")
    parser.add_argument(
        "problem_path_or_id",
        nargs="?",
        help="The LeetCode problem ID (e.g., '1') or a path within the problem directory. "
        "If not provided, it will be inferred from the current directory.",
    )
    args = parser.parse_args()

    raw_input = args.problem_path_or_id
    problem_id_str = None

    if raw_input:
        problem_id_str = raw_input if raw_input.isdigit() else get_problem_id_from_path(Path(raw_input))

    if not problem_id_str:
        problem_id_str = get_problem_id_from_path(Path.cwd())

    if not problem_id_str:
        print(
            "Error: Could not determine problem ID from the input or current path. "
            "Please provide a valid problem ID or run from a problem directory.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        problem_id = int(problem_id_str)
    except ValueError:
        print(f"Error: Invalid problem ID '{problem_id_str}'.", file=sys.stderr)
        sys.exit(1)

    try:
        _, slug = leetcode_index.resolve(problem_id)
    except KeyError:
        print(f"Error: Problem with ID '{problem_id}' not found.", file=sys.stderr)
        sys.exit(1)

    branch_prefix = f"p/{problem_id:04d}-{slug}/"

    try:
        result = subprocess.run(
            ["git", "branch", "--list", f"{branch_prefix}*"],
            capture_output=True,
            text=True,
            check=True,
            env={"VSCODE_TASK": "1"},
        )
        branches = result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Error listing branches: {e}", file=sys.stderr)
        sys.exit(1)

    max_attempt = 0
    for branch in branches:
        branch = branch.strip()
        if match := re.search(r"/(\d+)$", branch):
            max_attempt = max(max_attempt, int(match.group(1)))

    new_attempt = max_attempt + 1
    new_branch_name = f"{branch_prefix}{new_attempt}"

    print(f"Creating and checking out new branch: {new_branch_name}")

    try:
        subprocess.run(
            ["git", "checkout", "-b", new_branch_name],
            check=True,
            env={"VSCODE_TASK": "1"},
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating new branch: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Running new_problem.py for problem {problem_id}")
    new_problem_script = ROOT / "scripts" / "new_problem.py"
    try:
        subprocess.run(
            [
                sys.executable,
                str(new_problem_script),
                str(problem_id),
                "--full-rewrite",
            ],
            check=True,
            env={"VSCODE_TASK": "1"},
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running new_problem.py: {e}", file=sys.stderr)
        sys.exit(1)

    print("Done.")


if __name__ == "__main__":
    main()
