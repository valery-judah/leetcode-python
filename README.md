
# LeetCode Python Workspace

![Coverage](docs/badges/coverage.svg)

> This repository is a work in progress. I have only a few LeetCode tasks solved so far, and I hope to add more in the future.

This repository contains solutions to LeetCode tasks and materials I find interesting. All leetcode tasks are in the [tasks](/tasks/) directory.

Each task has separate directory which includes task description, solutions, reasoning, and sometimes the solution flow. For example, see the [Majority Element task](/tasks/0169-majority-element/readme.md).

This section will include NeetCode category-based task set descriptions and navigation. (TODO: paste from Obsidian notes)

## Quick start


What do you want? 

- Read information about tasks:
- Run tests and get additional info (?)
- Create new task


```bash
# 1) Create a new problem skeleton
python scripts/new_task.py two-sum 1 --difficulty easy --tags array,hash-map --url https://leetcode.com/problems/two-sum/

# 2) Run tests and style checks
make test          # pytest (no __pycache__ written)
make lint          # ruff + black --check
make type          # mypy

# 3) Open in VS Code
code .
```

Folders are created under `tasks/NNNN-slug/`. Each contains:

- `readme.md` with clarifying questions, examples, approach, and complexity
- `solutions.py` starter (exports `Solution`, optionally `ALL_SOLUTIONS`)

CI, pre-commit, and VS Code configs are included.

## Chat aliases (for this assistant)

To reference a task’s files in chat without typing full paths, you can use simple aliases. I will resolve these when you use them in messages here (no symlinks needed):

- `@NNNN` → `tasks/NNNN-*/readme.md`
  - Example: `@0169` → `tasks/0169-majority-element/readme.md`
- `@slug` → `tasks/*-slug/readme.md`
  - Example: `@two-sum` → `tasks/0001-two-sum/readme.md`
- `@NNNN/<file>` or `@slug/<file>` to point to another file in that task directory
  - Example: `@0169/solutions.py` → `tasks/0169-majority-element/solutions.py`

If an alias maps to multiple folders, I’ll ask you to clarify which one you meant.

### Optional alias files (local convenience)

- Prefer a symlink alias which is resides in taks folder per task, e.g. `0169.readme.md` → `readme.md`.
- Create with: `ln -s readme.md 0169.readme.md`.

### Multi-variant mode (compare approaches)

If you want to implement and compare multiple approaches for a problem:

```bash
python scripts/new_task.py contains-duplicate 217 --multi
```

This scaffolds a consolidated `tasks/0217-contains-duplicate/solutions.py` where you can define multiple classes (e.g., `BruteForce`, `SetBased`) and list them in `ALL_SOLUTIONS = [BruteForce, SetBased]`. The test file auto-discovers each class and runs the same cases for all variants. You can also optionally set `Solution = SetBased` as a default alias.

### Task file conventions

- Header docstring at top of `solutions.py` for consistency:

  ```python
  """
  Problem 1: Two Sum
  https://leetcode.com/problems/two-sum/
  Difficulty: easy
  Tags: array,hash-map
  """
  ```

- Quick-run tests from a task file directly (runs generic spec filtered to that task):

  ```python
  if __name__ == "__main__":
      import subprocess, sys
      from pathlib import Path
      task_dir = Path(__file__).parent
      root = task_dir.parent
      task_name = task_dir.name
      subprocess.run([sys.executable, "-m", "pytest", "-q", str(root), "-k", task_name], check=False)
  ```

- Canonical test cases live in `solutions.py` as `TEST_CASES`:
  - Implemented tasks: `(label, arg1, ..., expected)`
  - Stub tasks: `(label, args_tuple, kwargs_dict)` and `TEST_EXPECT_EXCEPTION = NotImplementedError`

## Developer workflow

- Lint: `make lint` (runs `ruff check .` and `black --check .`).
- Auto-fix: `make fmt` (runs `ruff check . --fix` and `black .`).
- Type check: `make type` (mypy on `tasks/`).
- Tests: `make test` (runs `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q`).
  - To run manually without cache files: `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q`.
- Pre-commit: `make precommit` to install hooks; `pre-commit run --all-files` to run manually.
- VS Code Tasks: Command Palette → “Tasks: Run Task” → `Test`, `Test: Active File`, or `New problem` (see `.vscode/tasks.json`).
- Python Test Explorer: Enabled for pytest; discovery is configured in `.vscode/settings.json`.

Notes on multi-variant tests:

- Tests load `solutions.py` and read `ALL_SOLUTIONS` to parametrize variants. If `ALL_SOLUTIONS` is absent, they will use a single exported `Solution` class from `solutions.py`.

Key configs:

- Ruff/Black/Mypy: `pyproject.toml`.
- Pytest defaults: `pytest.ini`.
- Git hooks: `.pre-commit-config.yaml`.
- Editor tasks/settings: `.vscode/tasks.json`, `.vscode/settings.json`.
- Terminal bootstrap: `scripts/setup_terminal.sh` (creates venv, installs deps).

CI:

- GitHub Actions runs lint, type check, and tests on push/PR (`.github/workflows/ci.yml`).
- GitHub Pages: on pushes to `main`, CI builds `site/` (includes coverage under `/coverage`) and deploys it via Pages. Enable once in Settings → Pages → Build and deployment → Source: GitHub Actions. Site URL: `https://<your-username>.github.io/<this-repo>/` (or see Actions → Deployments → Pages for the exact link).

## Project Architecture

- Overview of structure, testing, and conventions: `docs/architecture.md`
- Workflow templates: `docs/cline-workflow-template.md`
- Patterns and active notes: `memory-bank/`

### Cline Assistant Workflow

This project is configured with a `.clinerules` file that enables a proactive assistant workflow with Cline. You can ask Cline to review your work, and it will act as an automated code reviewer to ensure your solution meets the project's standards.

#### How to Use

1. **Implement Your Solution**: Complete your solution in the `solution.py` file and update the task `readme.md` with your approach and complexity analysis.
2. **Request a Review**: In the chat, ask Cline to review your work. You can say something like:
    - "Cline, please review my solution for the two-sum problem."
    - "Can you check my work for `0001-two-sum`?"
3. **Review the Feedback**: Cline will perform the following checks and provide you with a summary of the results.

#### Review Criteria

When you request a review, I will check your solution against the following criteria:

1. **Code Quality**: I will run the project's quality gates to ensure the code is clean and well-formatted.
    - `make fmt`: Checks for and fixes any formatting issues.
    - `make lint`: Checks for any linting errors.
    - `make type`: Performs static type checking.

2. **Correctness**: I will run the test suite to ensure that your solution is correct and passes all test cases.
    - `make test`: Executes the `pytest` test suite.

3. **Complexity Analysis**: I will check the task `readme.md` to ensure that you have provided a clear and accurate analysis of the time and space complexity of your solution.

4. **Documentation**: I will verify that the solution is well-documented.
    - **Solution Docstring**: I will check for a comprehensive docstring in the `solve` method in `solution.py`.
    - **Approach Documentation**: I will check that the task `readme.md` contains a clear explanation of your approach.

5. **Pattern Recognition**: I will remind you to consider if the solution uses a common pattern that should be added to the `memory-bank/patterns.md` file to help you build your collection of reusable patterns.

This workflow helps maintain code quality and ensures that all necessary documentation and logging are completed for each problem.
