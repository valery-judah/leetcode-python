# Implementation Plan

[Overview]
This document outlines the plan to rename the `tasks` directory to `problems` and update all related scripts and configuration files to reflect this change. This change will improve the clarity of the project's structure and naming conventions.

[Types]
No new types will be introduced.

[Files]
The following file modifications will be made:
- Rename the `tasks` directory to `problems`.
- Modify `scripts/new_task.py` to create new problems in the `problems` directory.
- Modify `scripts/test_new_task.py` to use the `problems` directory for testing.
- Modify `problems/all_problems_spec.py` to refer to `problem` instead of `task`.
- Modify `Makefile` to use the `problems` directory for testing and type checking.
- Modify `pytest.ini` to look for tests in the `problems` directory.

[Functions]
No new functions will be introduced.

[Classes]
No new classes will be introduced.

[Dependencies]
No new dependencies will be introduced.

[Testing]
The existing tests will be updated to work with the new `problems` directory. No new tests will be added.

[Implementation Order]
1. Rename the `tasks` directory to `problems`.
2. Update `scripts/new_task.py` to create new problems in the `problems` directory.
3. Update `scripts/test_new_task.py` to use the `problems` directory.
4. Update `problems/all_problems_spec.py` to refer to `problem` instead of `task`.
5. Update `Makefile` to use the `problems` directory for testing and type checking.
6. Update `pytest.ini` to look for tests in the `problems` directory.
