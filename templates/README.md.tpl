
# {number}. {title}

**URL**: {url}
**Difficulty**: {difficulty}
**Tags**: {tags}

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

- If more than 4 solutions exist, the table flips to list solutions as rows.

## Test Cases Source
- Define canonical test cases in your `solutions.py` so tests stay minimal.
- Create a `TEST_CASES` list (imported by tests via `cases_from_solutions(__file__, "TEST_CASES")`).
- Format for generic templates: `(label: str, args: tuple, kwargs: dict)`.

Example in `solutions.py`:

```python
TEST_CASES = [
  ("example", (/* positional args */), { /* keyword args */ }),
]
```

- The test template uses a shared fixture `S = S_fixture_for_this_dir(__file__)` that yields the solution class. Instantiate with `S()` inside tests.
- For some problems, shared helpers exist in `common.testutil` (e.g., `SUBSETS_COUNT_CASES`, `subset_count_cases(...)` for LeetCode 78). You can parametrize tests with these, too.
