import shutil
import subprocess
import sys
from pathlib import Path
from typing import Generator

import pytest

ROOT = Path(__file__).resolve().parents[1]
NEW_PROBLEM_SCRIPT = ROOT / "scripts" / "new_task.py"
PROBLEMS_DIR = ROOT / "problems"


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
    """Helper function to run the new_task.py script from the project root."""
    cmd = [sys.executable, str(NEW_PROBLEM_SCRIPT), *args]
    subprocess.run(cmd, check=True, cwd=ROOT)


def test_new_problem_creation_and_regeneration(test_problem_path: Path):
    """Tests that a new problem can be created and regenerated correctly."""
    slug = "test-problem-for-regeneration"
    number = "9997"
    expected_dir = test_problem_path

    # 1. Initial creation
    run_new_problem_script(slug, number)

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

    # 3. Regeneration
    run_new_problem_script(slug, number)

    # Assert regeneration
    assert expected_dir.is_dir()
    assert not (expected_dir / "dummy_file.txt").exists(), "Dummy file should be gone"
    assert (expected_dir / "readme.md").exists()
    assert symlink_path.is_symlink()
    solutions_content_after_regen = (expected_dir / "solutions.py").read_text()
    assert "ALL_SOLUTIONS" in solutions_content_after_regen
