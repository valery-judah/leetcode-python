import subprocess
import sys
from pathlib import Path

# Ensure the project root is in the path to import leetcode_index
sys.path.insert(0, str(Path(__file__).resolve().parent))

from leetcode_index import get_id, exists_slug


def get_slugs_from_script():
    """Runs the extract_slugs.py script and returns the output."""
    result = subprocess.run(["python3", "extract_slugs.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running extract_slugs.py: {result.stderr}")
        return []
    return result.stdout.strip().split("\n")


def main():
    """Maps slugs to IDs and prints the results."""
    slugs = get_slugs_from_script()
    if not slugs:
        print("No slugs to process.")
        return

    print("Slug to ID mapping:")
    for slug in slugs:
        if exists_slug(slug):
            problem_id = get_id(slug)
            print(f"{slug}: {problem_id}")
        else:
            print(f"{slug}: ID not found")


if __name__ == "__main__":
    main()
