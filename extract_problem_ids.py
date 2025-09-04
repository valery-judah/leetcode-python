import json


def extract_ids_from_file(filename):
    """Extracts problem IDs from a JSON file."""
    with open(filename) as f:
        data = json.load(f)

    ids = set()
    if "problems" in data:
        for problem in data["problems"]:
            if "id" in problem:
                ids.add(problem["id"])
    return ids


def main():
    """Main function to extract unique problem IDs from multiple files."""
    files = [
        "archive/lists/leetcode_prep_150.json",
        "archive/lists/neetcode_all.json",
    ]

    all_ids = set()
    for file in files:
        all_ids.update(extract_ids_from_file(file))

    sorted_ids = sorted(list(all_ids), key=int)

    print(f"Found {len(sorted_ids)} unique problem IDs.")
    print(sorted_ids)


if __name__ == "__main__":
    main()
