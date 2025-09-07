# Shim Modules

Problem folders are named with numeric prefixes and hyphens (e.g., `0217-contains-duplicate/`), which are not valid Python module identifiers. To feed these files into mkdocstrings, we provide thin shim modules under `docs/shims/` that dynamically load and re-export their classes.

- Example shim: `docs/shims/contains_duplicate.py`
- Usage in docs: `::: docs.shims.contains_duplicate`

This keeps the repo’s problem layout intact while enabling API documentation.
