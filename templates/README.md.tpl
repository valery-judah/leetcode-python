
# {number}. {title}

**URL**: <{url}>
**Difficulty**: {difficulty}
**Tags**: {tags}

## Module Header

- Start `solutions.py` with a short docstring for consistency:

  ```python
  """
  Problem {number}: {title}
  {url}
  Difficulty: {difficulty}
  Tags: {tags}
  """
  ```

## Running Tests via solutions.py

- Running a task file directly executes the generic spec filtered to that task:

  ```python
  if __name__ == "__main__":
      import subprocess, sys
      from pathlib import Path
      task_dir = Path(__file__).parent
      root = task_dir.parent
      task_name = task_dir.name
      subprocess.run([sys.executable, "-m", "pytest", "-q", str(root), "-k", task_name], check=False)
  ```

## Clarifying questions

- Input shape, ranges, constraints?
- Duplicates, negatives, empty input?
- Mutations allowed? Sorted? Streaming?

## Examples

- Add 2–3 examples and edge cases.

## Approach

- Brute force -> improved -> optimal.
- Data structures considered.
- Proof of correctness sketch.

## Complexity

- Time: O(...)
- Space: O(...)

## Checklist

- [ ] Restate problem
- [ ] Small example walkthrough
- [ ] Choose DS/algorithm
- [ ] Dry-run core loop
- [ ] Code cleanly
- [ ] Test edge cases

See also: `docs/interview-framework.md`.

## Test Matrix Reporter

- Tests can opt into a colored PASS/FAIL matrix shown at the end of `pytest` by appending results to the shared `run_summary` fixture.
- For each assertion, append a tuple of `(label, ok)` where `label` is a short case name and `ok` is a boolean.
- Multi-solution tests should use the solution class name as the key. Example:

  ```python
  ok = S().solve(*args, **kwargs) == expected
  run_summary[S.__name__].append((label, ok))
  assert ok
  ```

- Single-solution tests (where `S` is an instance) should use the instance class name:

  ```python
  ok = S.solve(*args, **kwargs) == expected
  run_summary[S.__class__.__name__].append((label, ok))
  assert ok
  ```

## Test Cases Source

- Define canonical test cases in your `solutions.py` so tests stay minimal.
- Supported formats consumed by `tasks/all_problems_spec.py`:
  - Implemented tasks: `(label: str, arg1, ..., expected)`
  - Stub tasks: `(label: str, args: tuple, kwargs: dict)` with `TEST_EXPECT_EXCEPTION = NotImplementedError`

Examples in `solutions.py`:

```python
# Implemented task
TEST_CASES = [
  ("base", [2, 7, 11, 15], 9, [0, 1]),
]

# Stub task
TEST_CASES = [
  ("example", (), {{}}),
]
TEST_EXPECT_EXCEPTION = NotImplementedError
```

- Test templates import these via `cases_from_solutions(__file__, "TEST_CASES")`.
- Shared helpers exist in `common.testutil` (e.g., `SUBSETS_COUNT_CASES`, `subset_count_cases(...)`).
