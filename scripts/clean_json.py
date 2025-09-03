import json


def clean_leetcode_data(file_path):
    """
    Deletes 'content', 'stats', and 'solution' fields from each question in the
    given JSON file.
    """
    with open(file_path, "r") as f:
        data = json.load(f)

    for item in data:
        question = item.get("data", {}).get("question", {})
        if question:
            question.pop("content", None)
            question.pop("stats", None)
            question.pop("solution", None)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    clean_leetcode_data("data/leetcode_questions.json")
