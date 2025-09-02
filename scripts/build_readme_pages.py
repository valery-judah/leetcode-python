#!/usr/bin/env python
from __future__ import annotations

import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
README_PATH = ROOT / "README.md"


def build_from_readme() -> None:
    """Builds the site from the main README.md."""
    if not README_PATH.exists():
        print("ERROR: README.md not found.")
        return

    content = README_PATH.read_text(encoding="utf-8")
    html_content = markdown.markdown(content)
    title_match = re.search(r"^#\s+(.*)", content)
    title = title_match.group(1) if title_match else "LeetCode Python Workspace"

    html = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
  <main>
    {html_content}
  </main>
</body>
</html>
"""

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "index.html").write_text(html, encoding="utf-8")
    print("Site built successfully from README.md.")


if __name__ == "__main__":
    build_from_readme()
