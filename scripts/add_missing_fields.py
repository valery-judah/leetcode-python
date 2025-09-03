import json
import os


def add_missing_fields():
    # Construct absolute paths to the JSON files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    neetcode_path = os.path.join(base_dir, "data", "neetcode_250_complete.json")
    leetcode_path = os.path.join(base_dir, "data", "leetcode_questions.json")

    # Load the source JSON data
    with open(leetcode_path, "r") as f:
        leetcode_data = json.load(f)

    # Create a lookup map from the LeetCode data
    leetcode_map = {}
    for item in leetcode_data:
        question = item.get("data", {}).get("question", {})
        if question and "questionId" in question and "topicTags" in question:
            slug = None
            if "titleSlug" in question:
                slug = question["titleSlug"]
            elif "url" in question:
                url = question["url"]
                slug = url.strip("/").split("/")[-1]

            if slug:
                leetcode_map[slug] = {
                    "id": question["questionId"],
                    "tags": [tag["name"] for tag in question["topicTags"]],
                }

    # Load the target JSON data
    with open(neetcode_path, "r") as f:
        neetcode_data = json.load(f)

    # Update the NeetCode data with fields from the LeetCode data
    found_count = 0
    missing_slug_in_neetcode_count = 0
    unmatched_slugs = []
    for problem in neetcode_data.get("problems", []):
        slug = problem.get("slug")
        if not slug:
            missing_slug_in_neetcode_count += 1
            continue
        if slug in leetcode_map:
            problem["id"] = leetcode_map[slug]["id"]
            problem["tags"] = leetcode_map[slug]["tags"]
            found_count += 1
        else:
            unmatched_slugs.append(slug)

    print("\n--- Statistics ---")
    print(f"Total problems in neetcode_250_complete.json: {len(neetcode_data.get('problems', []))}")
    print(f"Matched problems: {found_count}")
    print(f"Problems missing a slug in neetcode_250_complete.json: {missing_slug_in_neetcode_count}")
    print(f"Unmatched slugs: {len(unmatched_slugs)}")

    if unmatched_slugs:
        print("\nThe following slugs were not found in the leetcode data:")
        for slug in unmatched_slugs:
            print(f"  - {slug}")

    # Save the updated data back to the file
    with open(neetcode_path, "w") as f:
        json.dump(neetcode_data, f, indent=2)


if __name__ == "__main__":
    add_missing_fields()
