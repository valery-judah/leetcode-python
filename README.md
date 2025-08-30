
# LeetCode Python Workspace

Minimal, test-first workflow for coding interview practice in VS Code.

Baseline runtime: Python 3.11 (matches LeetCode’s runtime).

## Quick start

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

- `README.md` with clarifying questions and plan checklist
- `solution.py` starter
- `test_solution.py` scaffold

CI, pre-commit, and VS Code configs are included.

### Multi-variant mode (compare approaches)

If you want to implement and compare multiple approaches for a problem:

```bash
python scripts/new_task.py contains-duplicate 217 --multi
```

This scaffolds a consolidated `tasks/0217-contains-duplicate/solutions.py` where you can define multiple classes (e.g., `BruteForce`, `SetBased`) and list them in `ALL_SOLUTIONS = [BruteForce, SetBased]`. The test file auto-discovers each class and runs the same cases for all variants. You can also optionally set `Solution = SetBased` as a default alias.

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
- Tests will first look for `solutions.py` and read `ALL_SOLUTIONS` to parametrize variants. If absent, they fall back to `variants.py` or legacy `solutions/*.py` modules.

Key configs:

- Ruff/Black/Mypy: `pyproject.toml`.
- Pytest defaults: `pytest.ini`.
- Git hooks: `.pre-commit-config.yaml`.
- Editor tasks/settings: `.vscode/tasks.json`, `.vscode/settings.json`.
- Terminal bootstrap: `scripts/setup_terminal.sh` (creates venv, installs deps).

CI:

- GitHub Actions runs lint, type check, and tests on push/PR (`.github/workflows/ci.yml`).

## Project Architecture

- Overview of structure, testing, and conventions: `docs/architecture.md`
- Workflow templates: `docs/cline-workflow-template.md`
- Patterns and active notes: `memory-bank/`

### Cline Assistant Workflow

This project is configured with a `.clinerules` file that enables a proactive assistant workflow with Cline. You can ask Cline to review your work, and it will act as an automated code reviewer to ensure your solution meets the project's standards.

#### How to Use

1. **Implement Your Solution**: Complete your solution in the `solution.py` file and update the `README.md` with your approach and complexity analysis.
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

3. **Complexity Analysis**: I will check the `README.md` to ensure that you have provided a clear and accurate analysis of the time and space complexity of your solution.

4. **Documentation**: I will verify that the solution is well-documented.
    - **Solution Docstring**: I will check for a comprehensive docstring in the `solve` method in `solution.py`.
    - **Approach Documentation**: I will check that the `README.md` contains a clear explanation of your approach.

5. **Pattern Recognition**: I will remind you to consider if the solution uses a common pattern that should be added to the `memory-bank/patterns.md` file to help you build your collection of reusable patterns.

This workflow helps maintain code quality and ensures that all necessary documentation and logging are completed for each problem.
