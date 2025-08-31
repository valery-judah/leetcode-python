#!/usr/bin/env python
from __future__ import annotations

import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"
HTMLCOV_DIR = ROOT / "htmlcov"
SITE_DIR = ROOT / "site"


@dataclass
class TaskMeta:
    number: int
    slug: str
    title: str
    url: str | None
    difficulty: str | None
    tags: list[str]
    readme_rel: str  # repo-relative path to README.md


MD_BOLD_FIELD = re.compile(r"^\*\*(?P<key>[^*]+)\*\*:\s*(?P<val>.*)")


def parse_task(task_dir: Path) -> TaskMeta | None:
    readme = task_dir / "README.md"
    if not readme.exists():
        return None

    title = task_dir.name
    number = int(task_dir.name.split("-", 1)[0])
    slug = task_dir.name.split("-", 1)[1] if "-" in task_dir.name else task_dir.name
    url = None
    difficulty = None
    tags: list[str] = []

    try:
        for line in readme.read_text(encoding="utf-8").splitlines():
            if line.startswith("# ") and ". " in line:
                # e.g., "# 78. Subsets"
                title = line[2:].strip()
            m = MD_BOLD_FIELD.match(line.strip())
            if m:
                key = m.group("key").strip().lower()
                val = m.group("val").strip()
                if key == "url":
                    url = val or None
                elif key == "difficulty":
                    difficulty = val or None
                elif key == "tags" and val:
                    tags = [t.strip() for t in re.split(r"[,|]", val) if t.strip()]
        return TaskMeta(number, slug, title, url, difficulty, tags, str(readme.relative_to(ROOT)))
    except Exception:
        return TaskMeta(number, slug, title, url, difficulty, tags, str(readme.relative_to(ROOT)))


def ensure_empty_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def build_site(tasks: list[TaskMeta]) -> None:
    """Build the Pages site.

    If an MkDocs config is present at the repo root (mkdocs.yml), prefer
    building the MkDocs site. Otherwise, fall back to generating a minimal
    static index with coverage using the legacy builder below.
    """
    mkdocs_yml = ROOT / "mkdocs.yml"
    if mkdocs_yml.exists():
        # Build MkDocs site into ./site
        # Use --clean to ensure old artifacts are removed
        subprocess.run(["mkdocs", "build", "--clean"], check=True)
        # Copy coverage into /site/coverage if present
        if HTMLCOV_DIR.exists():
            dest = SITE_DIR / "coverage"
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(HTMLCOV_DIR, dest)
        return

    # Legacy minimal site builder (no MkDocs)
    ensure_empty_dir(SITE_DIR)
    # Copy coverage under /coverage if present
    if HTMLCOV_DIR.exists():
        shutil.copytree(HTMLCOV_DIR, SITE_DIR / "coverage")

    # Write a tiny CSS
    assets = SITE_DIR / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    (assets / "style.css").write_text(
        """
        :root { --fg:#222; --muted:#666; --accent:#0b6; --chip:#eef; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;
            margin: 2rem auto;
            max-width: 900px;
            color: var(--fg);
        }
        a { color: var(--accent); text-decoration: none; }
        header h1 { margin: 0; }
        .muted { color: var(--muted); }
        .chips { display:flex; flex-wrap:wrap; gap:.5rem; margin:.5rem 0 1rem; }
        .chip {
            background: var(--chip);
            padding:.2rem .5rem;
            border-radius: .75rem;
            font-size: .9rem;
        }
        table { border-collapse: collapse; width: 100%; }
        th, td { border-bottom: 1px solid #ddd; padding: .5rem; text-align: left; }
        th { background: #f7f7f7; }
        .pill { padding:.1rem .4rem; border-radius:.5rem; background:#eee; font-size:.8rem; }
        nav { margin: .5rem 0 1.5rem; }
        nav a { margin-right: 1rem; }
        """,
        encoding="utf-8",
    )

    # Build tag stats
    tag_counts: dict[str, int] = {}
    for t in tasks:
        for tag in t.tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    top_tags = sorted(tag_counts.items(), key=lambda kv: (-kv[1], kv[0]))

    repo = os.environ.get("GITHUB_REPOSITORY", "")

    def gh_link(rel: str) -> str:
        if repo:
            return f"https://github.com/{repo}/blob/main/{rel}"
        return rel

    # Index HTML
    rows = []
    for t in sorted(tasks, key=lambda x: x.number):
        tags_html = (
            " ".join(f"<span class=chip>{tag}</span>" for tag in t.tags)
            or "<span class=muted>—</span>"
        )
        diff = f"<span class=pill>{t.difficulty or '?'}<span>"
        title_link = f"<a href='{gh_link(t.readme_rel)}'>{t.title}</a>"
        rows.append(
            f"<tr><td>{t.number:04d}</td><td>{title_link}</td><td>{diff}</td><td>{tags_html}</td></tr>"
        )

    tags_html = (
        " ".join(f"<span class=chip title='{c} tasks'>{tag}</span>" for tag, c in top_tags)
        or "<span class=muted>No tags yet</span>"
    )

    index = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>LeetCode Python Workspace</title>
  <link rel="stylesheet" href="assets/style.css" />
  <meta name="description"
        content="Interview prep workspace: problems, solutions, tests, coverage."
  />
  <meta name="robots" content="index,follow" />
  <meta name="color-scheme" content="light dark" />
</head>
<body>
  <header>
    <h1>LeetCode Python Workspace</h1>
    <p class="muted">
      Fast test-first practice with per-task coverage and multi-solution comparisons.
    </p>
  </header>
  <nav>
    <a href="coverage/index.html">Coverage Report</a>
    <a href="https://github.com/{repo}">Repository</a>
  </nav>
  <section>
    <h2>Tags</h2>
    <div class="chips">{tags_html}</div>
  </section>
  <section>
    <h2>Tasks</h2>
    <table>
      <thead><tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Tags</th></tr></thead>
      <tbody>
        {''.join(rows)}
      </tbody>
    </table>
  </section>
</body>
</html>
"""
    (SITE_DIR / "index.html").write_text(index, encoding="utf-8")


def main() -> None:
    tasks: list[TaskMeta] = []
    if TASKS_DIR.exists():
        for entry in sorted(TASKS_DIR.iterdir()):
            if entry.is_dir():
                meta = parse_task(entry)
                if meta:
                    tasks.append(meta)
    build_site(tasks)


if __name__ == "__main__":
    main()
