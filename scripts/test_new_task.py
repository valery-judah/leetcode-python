import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NEW_TASK_SCRIPT = ROOT / "scripts" / "new_task.py"
TASKS_DIR = ROOT / "tasks"


@pytest.fixture
def test_task_path() -> Path:
    """Provides the path for a test task and ensures cleanup."""
    slug = "test-task-for-regeneration"
    number = "9997"
    task_path = TASKS_DIR / f"{int(number):04d}-{slug}"

    # Clean up before the test, in case of a previous failure
    if task_path.exists():
        shutil.rmtree(task_path)

    yield task_path

    # Clean up after the test
    if task_path.exists():
        shutil.rmtree(task_path)


def run_new_task_script(*args: str) -> None:
    """Helper function to run the new_task.py script from the project root."""
    cmd = [sys.executable, str(NEW_TASK_SCRIPT), *args]
    subprocess.run(cmd, check=True, cwd=ROOT)


def test_new_task_creation_and_regeneration(test_task_path: Path):
    """Tests that a new task can be created and regenerated correctly."""
    slug = "test-task-for-regeneration"
    number = "9997"
    expected_dir = test_task_path

    # 1. Initial creation
    run_new_task_script(slug, number)

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
    run_new_task_script(slug, number)

    # Assert regeneration
    assert expected_dir.is_dir()
    assert not (expected_dir / "dummy_file.txt").exists(), "Dummy file should be gone"
    assert (expected_dir / "readme.md").exists()
    assert symlink_path.is_symlink()
    solutions_content_after_regen = (expected_dir / "solutions.py").read_text()
    assert "ALL_SOLUTIONS" in solutions_content_after_regen
