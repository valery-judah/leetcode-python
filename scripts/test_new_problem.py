import shutil
import subprocess
import sys
from pathlib import Path
from typing import Generator

import pytest

ROOT = Path(__file__).resolve().parents[1]
NEW_PROBLEM_SCRIPT = ROOT / "scripts" / "new_problem.py"
PROBLEMS_DIR = ROOT / "problems"
LISTS_DIR = ROOT / "lists"


@pytest.fixture
def test_problem_path() -> Generator[Path, None, None]:
    """Provides the path for a test problem and ensures cleanup."""
    slug = "test-problem-for-regeneration"
    number = "9997"
    problem_path = PROBLEMS_DIR / f"{int(number):04d}-{slug}"

    # Clean up before the test, in case of a previous failure
    if problem_path.exists():
        shutil.rmtree(problem_path)

    yield problem_path

    # Clean up after the test
    if problem_path.exists():
        shutil.rmtree(problem_path)


def run_new_problem_script(*args: str) -> None:
    """Helper function to run the new_problem.py script from the project root."""
    cmd = [sys.executable, str(NEW_PROBLEM_SCRIPT), *args]
    subprocess.run(cmd, check=True, cwd=ROOT)


def test_new_problem_creation_and_regeneration(test_problem_path: Path):
    """Tests that a new problem can be created and regenerated correctly."""
    slug = "test-problem-for-regeneration"
    number = "9997"
    expected_dir = test_problem_path

    # Create a temporary list entry so the script can find the problem
    temp_list = LISTS_DIR / "_temp_test_list.json"
    temp_list.write_text(
        "{\n"
        '  "problems": [\n'
        "    {\n"
        f'      "category": "Test",\n'
        f'      "id": "{number}",\n'
        f'      "name": "Temp Test Problem",\n'
        f'      "difficulty": "Easy",\n'
        f'      "leetcode_url": "https://leetcode.com/problems/{slug}/",\n'
        f'      "slug": "{slug}",\n'
        f'      "tags": ["Test"]\n'
        "    }\n"
        "  ]\n"
        "}\n"
    )

    # 1. Initial creation
    run_new_problem_script(number)

    # Assert initial creation
    assert expected_dir.is_dir()
    assert (expected_dir / "readme.md").exists()
    symlink_path = expected_dir / f"{int(number):04d}.readme.md"
    assert symlink_path.is_symlink()
    assert symlink_path.resolve() == (expected_dir / "readme.md").resolve()
    solutions_content = (expected_dir / "solutions.py").read_text()
    assert "ALL_SOLUTIONS" in solutions_content

    # 2. Add a dummy file to simulate user changes
    (expected_dir / "dummy_file.txt").write_text("dummy content")
    assert (expected_dir / "dummy_file.txt").exists()

    # 3. Regeneration (full rewrite to ensure cleanup)
    run_new_problem_script(number, "--full-rewrite")

    # Assert regeneration
    assert expected_dir.is_dir()
    assert not (expected_dir / "dummy_file.txt").exists(), "Dummy file should be gone"
    assert (expected_dir / "readme.md").exists()
    assert symlink_path.is_symlink()
    solutions_content_after_regen = (expected_dir / "solutions.py").read_text()
    assert "ALL_SOLUTIONS" in solutions_content_after_regen

    # Cleanup temp list file
    temp_list.unlink(missing_ok=True)
