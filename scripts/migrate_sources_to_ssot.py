import json
from pathlib import Path


def main():
    """
    Scans problem JSON files to create a canonical index file (SSOT).
    """
    root = Path(__file__).resolve().parents[1]
    problems_dir = root / "archive" / "problems"
    ssot_path = root / "data" / "problems.index.jsonl"

    records = []
    for f in sorted(problems_dir.glob("*.json")):
        data = json.loads(f.read_text())

        # Find the correct ID key
        problem_id = data.get("questionFrontendId") or data.get("questionId")
        if not problem_id:
            print(f"W_SKIP: Could not find problem ID in {f.name}")
            continue

        record = {
            "id": int(problem_id),
            "slug": data["titleSlug"],
            "title": data["title"],
            "aliases": [],
            "deprecated": False,
        }
        records.append(record)

    # Sort by ID for determinism
    records.sort(key=lambda r: r["id"])

    with ssot_path.open("w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

    print(f"Wrote {len(records)} records to {ssot_path}")


if __name__ == "__main__":
    main()
