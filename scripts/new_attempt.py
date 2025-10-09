#!/usr/bin/env python
from __future__ import annotations

import argparse
import ast
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


def clean_solution_file(problem_id: int, slug: str) -> None:
    """
    Finds the solution file and replaces the body of `solve` methods with `...`.
    This uses AST to find function body line numbers and then performs a text-based
    replacement to avoid reformatting the entire file.
    """

    class SolveVisitor(ast.NodeVisitor):
        def __init__(self):
            self.functions_to_clean: list[tuple[int, int, int]] = []

        def visit_FunctionDef(self, node: ast.FunctionDef):
            if node.name == "solve" and node.body:
                # Get start and end line numbers of the function body
                start_line = node.body[0].lineno
                # The end_lineno of the last statement in the body
                end_line = node.body[-1].end_lineno
                if end_line is None:
                    end_line = node.body[-1].lineno
                # Get indentation of the function definition itself
                indentation = node.col_offset
                self.functions_to_clean.append((start_line, end_line, indentation))
            self.generic_visit(node)  # Continue traversal

    problem_dir = ROOT / "problems" / f"{problem_id:04d}-{slug}"
    solution_path = next(
        (p for p in [problem_dir / "solution.py", problem_dir / "solutions.py"] if p.exists()),
        None,
    )

    if not solution_path:
        print(f"Warning: No solution file found for {slug}", file=sys.stderr)
        return

    try:
        source_code = solution_path.read_text()
        tree = ast.parse(source_code)

        visitor = SolveVisitor()
        visitor.visit(tree)

        lines = source_code.splitlines()

        # Process replacements from the bottom up to not affect line numbers
        for start, end, indent in sorted(visitor.functions_to_clean, key=lambda x: x[0], reverse=True):
            indent_str = " " * (indent + 4)  # Assume 4-space indent for the body
            # Replace the body lines with a single line containing '...'
            lines[start - 1 : end] = [f"{indent_str}..."]

        # Add a trailing newline if the original file had one
        if source_code.endswith("\n"):
            new_code = "\n".join(lines) + "\n"
        else:
            new_code = "\n".join(lines)

        solution_path.write_text(new_code)
        print(f"Cleaned solution file: {solution_path}")
    except Exception as e:
        print(f"Error processing {solution_path}: {e}", file=sys.stderr)
        sys.exit(1)


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
    new_branch_name = f"{branch_prefix}retry"

    print(f"Creating and checking out new branch: {new_branch_name}")

    try:
        subprocess.run(
            ["git", "checkout", "-B", new_branch_name],
            check=True,
            env={"VSCODE_TASK": "1"},
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating new branch: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Cleaning solution file for problem {problem_id}")
    clean_solution_file(problem_id, slug)

    print("Done.")


if __name__ == "__main__":
    main()
