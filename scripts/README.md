# Scripts

This directory contains various utility scripts for maintaining and managing the project.

## Script Descriptions

### `add_missing_fields.py`

**Purpose:** Enriches the `data/neetcode_250_complete.json` file with additional data from `data/leetcode_questions.json`. It adds fields like `id`, `tags`, and `similar_questions`.

**Usage:** `python3 scripts/add_missing_fields.py`

### `build_pages.py`

**Purpose:** This script likely generates documentation pages, possibly for a static site generator like MkDocs.

**Usage:** `python3 scripts/build_pages.py`

### `check_vscode_shell_integration.py`

**Purpose:** Checks if the VS Code shell integration is properly set up.

**Usage:** `python3 scripts/check_vscode_shell_integration.py`

### `clean_json.py`

**Purpose:** Cleans and formats JSON files in the project, ensuring consistent styling.

**Usage:** `python3 scripts/clean_json.py`

### `count_unique_questions.py`

**Purpose:** Counts the number of unique similar questions in `data/neetcode_250_complete.json` that are not already in the main problem list.

**Usage:** `python3 scripts/count_unique_questions.py`

### `extract_similar_questions.py`

**Purpose:** Extracts the unique similar questions from `data/neetcode_250_complete.json`, formats them, and saves them to `data/similar_questions.json`. It also adds a `backlink_questions` field to each question.

**Usage:** `python3 scripts/extract_similar_questions.py`

### `new_task.py`

**Purpose:** A script to assist in creating a new task or problem structure within the project.

**Usage:** `python3 scripts/new_task.py`

### `normalize_notes_refs.py`

**Purpose:** Normalizes references in the notes files to ensure consistency.

**Usage:** `python3 scripts/normalize_notes_refs.py`

### `setup_terminal.sh`

**Purpose:** A shell script to set up the terminal environment for the project.

**Usage:** `bash scripts/setup_terminal.sh`

### `test_new_task.py`

**Purpose:** Contains tests for the `new_task.py` script.

**Usage:** `pytest scripts/test_new_task.py`

### `update_leetcode_slugs.py`

**Purpose:** Updates the LeetCode slugs in the project data files.

**Usage:** `python3 scripts/update_leetcode_slugs.py`

### `verify_leetcode_urls.py`

**Purpose:** Verifies that the LeetCode URLs in the project data are valid and accessible.

**Usage:** `python3 scripts/verify_leetcode_urls.py`

### `whitespace_fix.py`

**Purpose:** Fixes whitespace issues in the project files to maintain consistent formatting.

**Usage:** `python3 scripts/whitespace_fix.py`
