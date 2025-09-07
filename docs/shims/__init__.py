"""Shims to expose non-importable problem modules to mkdocstrings.

Problem folders use hyphens and numeric prefixes, which are not valid Python
module names. These shims load the corresponding files via importlib and
re-export classes for mkdocstrings to introspect.
"""
