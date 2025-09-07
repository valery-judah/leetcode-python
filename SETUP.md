# Project Setup Instructions

To ensure that the project runs correctly and all modules are properly imported, please follow these setup steps after cloning the repository. This guide leverages the project's `Makefile` for a streamlined setup.

## 1. Create and Activate a Virtual Environment

Using a virtual environment is crucial for managing project dependencies and avoiding conflicts.

```bash
# Navigate to the project root directory
cd leetcode-python-project

# Create a virtual environment (e.g., named 'venv')
python -m venv venv

# Activate the virtual environment
# On macOS and Linux:
source venv/bin/activate
# On Windows:
# .\\venv\\Scripts\\activate
```

## 2. Install Dependencies

This project uses a `Makefile` to simplify the installation of dependencies.

With your virtual environment activated, run:

```bash
make install
```

This will install all the necessary packages listed in `requirements.txt` and `requirements-dev.txt`.

## 3. Install the Project in Editable Mode

To make sure that shared modules like `common` can be found by scripts and tests, you must install the project in "editable" mode. This links the project's source code to your Python environment, so imports work correctly.

Run the following command from the project's root directory:

```bash
pip install -e .
```

## 4. Set Up Pre-Commit Hooks

This project uses pre-commit hooks to automatically check and format your code before you commit. This helps maintain code quality and consistency.

To set up the hooks, run:

```bash
make precommit
```

After completing these steps, your development environment will be fully configured. You will be able to run scripts, tests, and linters without encountering import errors or configuration issues.
