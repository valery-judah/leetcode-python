
# LeetCode Python Workspace

Minimal, test-first workflow for coding interview practice in VS Code.

## Quick start
```bash
# 1) Create a new problem skeleton
python scripts/new_task.py two-sum 1 --difficulty easy --tags array,hash-map --url https://leetcode.com/problems/two-sum/

# 2) Run tests and style checks
make test          # pytest
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

### Cline Assistant Workflow

This project is configured with a `.clinerules` file that enables a proactive assistant workflow with Cline. You can ask Cline to review your work, and it will act as an automated code reviewer to ensure your solution meets the project's standards.

#### How to Use

1.  **Implement Your Solution**: Complete your solution in the `solution.py` file and update the `README.md` with your approach and complexity analysis.
2.  **Request a Review**: In the chat, ask Cline to review your work. You can say something like:
    *   "Cline, please review my solution for the two-sum problem."
    *   "Can you check my work for `0001-two-sum`?"
3.  **Review the Feedback**: Cline will perform the following checks and provide you with a summary of the results.

#### Review Criteria

When you request a review, I will check your solution against the following criteria:

1.  **Code Quality**: I will run the project's quality gates to ensure the code is clean and well-formatted.
    *   `make fmt`: Checks for and fixes any formatting issues.
    *   `make lint`: Checks for any linting errors.
    *   `make type`: Performs static type checking.

2.  **Correctness**: I will run the test suite to ensure that your solution is correct and passes all test cases.
    *   `make test`: Executes the `pytest` test suite.

3.  **Complexity Analysis**: I will check the `README.md` to ensure that you have provided a clear and accurate analysis of the time and space complexity of your solution.

4.  **Documentation**: I will verify that the solution is well-documented.
    *   **Solution Docstring**: I will check for a comprehensive docstring in the `solve` method in `solution.py`.
    *   **Approach Documentation**: I will check that the `README.md` contains a clear explanation of your approach.

5.  **Pattern Recognition**: I will remind you to consider if the solution uses a common pattern that should be added to the `memory-bank/patterns.md` file to help you build your collection of reusable patterns.

This workflow helps maintain code quality and ensures that all necessary documentation and logging are completed for each problem.
