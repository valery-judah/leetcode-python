import json
import os
import re


def convert_slug_from_url(url):
    """Extracts the problem slug from a LeetCode URL."""
    if not url:
        return None
    match = re.search(r"/problems/([^/]+)/?", url)
    return match.group(1) if match else None


def transform_question(question_data):
    """Transforms a single question object to the target format."""
    q = question_data["data"]["question"]

    # Basic fields
    transformed = {
        "category": "",
        "id": q["questionFrontendId"],
        "name": q["title"],
        "difficulty": q["difficulty"],
        "leetcode_url": q.get("url"),
        "slug": convert_slug_from_url(q.get("url")),
        "isPaidOnly": q.get("isPaidOnly", False),
    }

    # Tags
    tags = []
    if q.get("topicTags"):
        tags = [tag["name"] for tag in q["topicTags"]]
    transformed["tags"] = tags

    # Similar questions
    similar_questions = []
    if q.get("similarQuestions"):
        try:
            similar_list = json.loads(q["similarQuestions"])
            for sq in similar_list:
                slug = sq.get("titleSlug")
                similar_questions.append(
                    {
                        "title": sq["title"],
                        "slug": slug,
                        "id": None,  # ID is not available in the source for similar questions
                        "leetcode_url": f"https://leetcode.com/problems/{slug}/" if slug else None,
                    }
                )
        except (json.JSONDecodeError, TypeError):
            pass  # Ignore if the string is not valid JSON or not a string
    transformed["similar_questions"] = similar_questions

    return transformed


def main():
    """Main function to convert the JSON file."""
    try:
        with open("lists/leetcode_questions.json", encoding="utf-8") as f:
            source_data = json.load(f)
    except FileNotFoundError:
        print("Error: lists/leetcode_questions.json not found.")
        return
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from lists/leetcode_questions.json.")
        return

    transformed_problems = [transform_question(q) for q in source_data]

    output_data = {"problems": transformed_problems}

    with open("leetcode_all_converted.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print("Successfully converted to leetcode_all_converted.json")

    # Create individual problem files
    problems_dir = "lists/problems"
    os.makedirs(problems_dir, exist_ok=True)

    for problem in transformed_problems:
        problem_id = problem["id"].zfill(4)
        slug = problem["slug"]
        file_name = f"{problem_id}-{slug}.json"

        file_path = os.path.join(problems_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(problem, f, indent=2)

    print(f"Successfully created individual problem files in '{problems_dir}' directory.")


if __name__ == "__main__":
    main()
