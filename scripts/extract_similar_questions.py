import json
import os

def extract_unique_similar_questions():
    """
    Extracts unique similar questions from the neetcode_250_complete.json file,
    formats them, and saves them to a new JSON file.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    neetcode_path = os.path.join(base_dir, "data", "neetcode_250_complete.json")
    leetcode_path = os.path.join(base_dir, "data", "leetcode_questions.json")
    output_path = os.path.join(base_dir, "data", "similar_questions.json")

    with open(neetcode_path, "r") as f:
        neetcode_data = json.load(f)

    with open(leetcode_path, "r") as f:
        leetcode_data = json.load(f)

    leetcode_map = {}
    for item in leetcode_data:
        question = item.get("data", {}).get("question", {})
        if question and "titleSlug" in question:
            slug = question["titleSlug"]
            leetcode_map[slug] = {
                "difficulty": question.get("difficulty"),
                "tags": [tag["name"] for tag in question.get("topicTags", [])],
            }

    main_problem_slugs = {problem['slug'] for problem in neetcode_data['problems']}
    
    similar_questions = []
    for problem in neetcode_data['problems']:
        similar_questions.extend(problem.get('similar_questions', []))

    unique_similar_questions = {}
    for question in similar_questions:
        slug = question.get("slug")
        if slug and slug not in main_problem_slugs:
            if slug not in unique_similar_questions:
                new_question = {
                    "id": question.get("id"),
                    "name": question.get("title"),
                    "leetcode_url": question.get("leetcode_url"),
                    "slug": slug,
                    "difficulty": None,
                    "tags": [],
                    "similar_questions": []
                }
                if slug in leetcode_map:
                    new_question["difficulty"] = leetcode_map[slug].get("difficulty")
                    new_question["tags"] = leetcode_map[slug].get("tags", [])
                
                unique_similar_questions[slug] = new_question

    # Create a backlink map
    backlink_map = {}
    for problem in neetcode_data['problems']:
        for similar_question in problem.get('similar_questions', []):
            similar_slug = similar_question.get("slug")
            if similar_slug:
                if similar_slug not in backlink_map:
                    backlink_map[similar_slug] = []
                backlink_map[similar_slug].append({
                    "name": problem["name"],
                    "slug": problem["slug"]
                })

    # Add backlinks to the unique similar questions
    for slug, question_data in unique_similar_questions.items():
        question_data["backlink_questions"] = backlink_map.get(slug, [])

    # Convert the dictionary to a list
    formatted_questions = list(unique_similar_questions.values())

    # Create the final JSON structure
    output_data = {
        "problems": formatted_questions,
        "total_count": len(formatted_questions),
        "extracted_on": "2024"
    }

    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully extracted {len(formatted_questions)} unique similar questions to {output_path}")

if __name__ == "__main__":
    extract_unique_similar_questions()
