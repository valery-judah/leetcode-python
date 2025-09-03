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
        if question and "title" in question and "questionId" in question and "topicTags" in question:
            title = question["title"]
            leetcode_map[title] = {
                "id": question["questionId"],
                "tags": [tag["name"] for tag in question["topicTags"]],
            }

    # Load the target JSON data
    with open(neetcode_path, "r") as f:
        neetcode_data = json.load(f)

    # Update the NeetCode data with fields from the LeetCode data
    found_count = 0
    missing_titles = []
    for problem in neetcode_data.get("problems", []):
        title = problem.get("title")
        if not title:
            continue
        if title in leetcode_map:
            problem["id"] = leetcode_map[title]["id"]
            problem["tags"] = leetcode_map[title]["tags"]
            found_count += 1
        else:
            missing_titles.append(title)

    print(f"Found {found_count} matching problems.")
    if missing_titles:
        print("The following titles were not found in the leetcode data:")
        for title in missing_titles:
            print(f"  - {title}")

    # Save the updated data back to the file
    with open(neetcode_path, "w") as f:
        json.dump(neetcode_data, f, indent=2)


if __name__ == "__main__":
    add_missing_fields()
