import json
import os


def get_ids_from_files(file_paths):
    """
    Reads a list of JSON files, extracts 'id' from each problem,
    and returns a sorted list of unique IDs.
    """
    all_ids = set()
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File not found at {file_path}")
            continue
        with open(file_path) as f:
            data = json.load(f)
            for problem in data.get("problems", []):
                if "id" in problem:
                    all_ids.add(problem["id"])
    return sorted(list(all_ids), key=int)


def main():
    """
    Main function to extract, sort, and write LeetCode problem IDs.
    """
    files = [
        "archive/lists/leetcode_prep_150.json",
        "archive/lists/leetcode_premium_100.json",
        "archive/lists/neetcode_250.json",
    ]

    unique_sorted_ids = get_ids_from_files(files)

    output_filename = "ids_to_create.txt"
    with open(output_filename, "w") as f:
        for problem_id in unique_sorted_ids:
            f.write(f"{problem_id}\n")

    print(f"Successfully wrote {len(unique_sorted_ids)} unique problem IDs to {output_filename}")


if __name__ == "__main__":
    main()
