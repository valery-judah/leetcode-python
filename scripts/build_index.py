import sys
from pathlib import Path

# Add the project root to the path to allow importing leetcode_index
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from leetcode_index._build import build

if __name__ == "__main__":
    build()
