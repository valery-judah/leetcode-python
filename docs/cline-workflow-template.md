# Cline TDD Workflow for LeetCode

This document outlines a standardized TDD workflow for solving LeetCode problems using Cline.

## 1. Understand the Problem

- **Read the task `readme.md`**: Carefully review the problem description, constraints, and examples.
- **Clarify Requirements**: If anything is unclear, add questions to the "Clarifying questions" section of the task `readme.md`.

## 2. Write Failing Tests

- Single-solution flow: open `tasks/<problem-slug>/test_solution.py`.
- Multi-variant flow (`--multi` scaffold): open `tasks/<problem-slug>/test_<slug>.py`.
- **Add Test Cases**: Use the `@pytest.mark.parametrize` decorator to add a comprehensive set of test cases, including:
  - The base case from the problem description.
  - Edge cases (e.g., empty lists, negative numbers, duplicates).
  - Cases that test different paths through the logic.
- **Run `make test`**: Execute the tests to confirm that they fail as expected with a `NotImplementedError`.

## 3. Implement the Solution

- Open `tasks/<problem-slug>/solutions.py`.
- Single solution: implement `Solution.solve(...)`.
- Multiple variants: add classes implementing `solve(...)` and list them in `ALL_SOLUTIONS = [...]`. Optionally set `Solution = <DefaultClass>`.
- **Implement the `solve` method**: Write the code to solve the problem, focusing on a clean and efficient implementation.
- **Add Docstrings**: Document the solution's approach, arguments, and return value.

## 4. Run and Pass Tests

- **Run `make test`**: Execute the tests again to confirm that the solution passes all test cases.
- **Run `make fmt` and `make lint`**: Format and lint the code to ensure it adheres to the project's style guidelines.

## 5. Document the Solution

- **Update the task `readme.md`**: Fill in the "Approach" and "Complexity" sections to document the solution's logic and its time and space complexity.

## 6. Log Actions

- **Create an Action Log**: Create a markdown file in the `docs` directory to log the steps taken to solve the problem. This is useful for tracking progress and for future reference.
