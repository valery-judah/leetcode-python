import json
import os
import re


def add_missing_fields():
    # Construct absolute paths to the JSON files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    neetcode_path = os.path.join(base_dir, "data", "leetcode_premium_100.json")
    leetcode_path = os.path.join(base_dir, "data", "leetcode_questions.json")

    # Load the source JSON data
    with open(leetcode_path, "r") as f:
        leetcode_data = json.load(f)

    # Create a lookup map from the LeetCode data
    leetcode_map = {}
    leetcode_title_map = {} # For fuzzy matching by title
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
                    "similarQuestions": question.get("similarQuestions", "[]"),
                    "url": question.get("url"),
                    "title": question.get("title"), # Store title for fuzzy matching
                }
                # Add to fuzzy title map
                cleaned_title = question["title"].lower().replace(' ', '-').replace('.', '').replace('(', '').replace(')', '').replace(',', '')
                cleaned_title = re.sub(r'[^a-z0-9-]', '', cleaned_title)
                leetcode_title_map[cleaned_title] = leetcode_map[slug]

    # Process similar questions to include IDs
    for slug, data in leetcode_map.items():
        try:
            similar_questions_json = json.loads(data["similarQuestions"])
            processed_similar_questions = []
            for sq in similar_questions_json:
                similar_slug = sq.get("titleSlug")
                if similar_slug in leetcode_map:
                    processed_similar_questions.append(
                        {
                            "title": sq["title"],
                            "slug": similar_slug,
                            "id": leetcode_map[similar_slug]["id"],
                            "leetcode_url": leetcode_map[similar_slug]["url"],
                        }
                    )
            data["similarQuestions"] = processed_similar_questions
        except json.JSONDecodeError:
            data["similarQuestions"] = []

    # Load the target JSON data
    with open(neetcode_path, "r") as f:
        neetcode_data = json.load(f)

    # Update the NeetCode data with fields from the LeetCode data
    found_count = 0
    missing_slug_in_neetcode_count = 0
    unmatched_slugs = []
    for problem in neetcode_data.get("problems", []):
        matched = False
        
        # Try exact slug match first
        slug = problem.get("slug")
        if not slug:
            missing_slug_in_neetcode_count += 1
            continue

        if slug in leetcode_map:
            problem["id"] = leetcode_map[slug]["id"]
            problem["tags"] = leetcode_map[slug]["tags"]
            problem["leetcode_url"] = leetcode_map[slug]["url"]
            problem["similar_questions"] = leetcode_map[slug]["similarQuestions"]
            found_count += 1
            matched = True
        else:
            # Fallback to fuzzy title match
            name = problem.get("name")
            if name:
                cleaned_name = name.lower().replace(' ', '-').replace('.', '').replace('(', '').replace(')', '').replace(',', '')
                cleaned_name = re.sub(r'[^a-z0-9-]', '', cleaned_name)
                if cleaned_name in leetcode_title_map:
                    matched_data = leetcode_title_map[cleaned_name]
                    problem["id"] = matched_data["id"]
                    problem["tags"] = matched_data["tags"]
                    problem["leetcode_url"] = matched_data["url"]
                    problem["similar_questions"] = matched_data["similarQuestions"]
                    found_count += 1
                    matched = True
        
        if not matched:
            unmatched_slugs.append(slug)

    print("\n--- Statistics ---")
    print(f"Total problems in leetcode_premium_100.json: {len(neetcode_data.get('problems', []))}")
    print(f"Matched problems: {found_count}")
    print(f"Problems missing a slug in leetcode_premium_100.json: {missing_slug_in_neetcode_count}")
    print(f"Unmatched slugs: {len(unmatched_slugs)}")

    if unmatched_slugs:
        print("\nThe following slugs were not found in the leetcode data:")
        for slug in unmatched_slugs:
            print(f"  - {slug}")

    # Reorder fields and rename similarQuestions
    reordered_problems = []
    desired_order = [
        "category",
        "id",
        "name",
        "difficulty",
        "leetcode_url",
        "slug",
        "tags",
        "similar_questions",
        "neetcode_url",
    ]
    for problem in neetcode_data.get("problems", []):
        if "similarQuestions" in problem:
            problem["similar_questions"] = problem.pop("similarQuestions")

        reordered_problem = {}
        # Preserve existing category if it exists
        if "category" in problem:
            reordered_problem["category"] = problem["category"]
            
        for key in desired_order:
            if key in problem:
                reordered_problem[key] = problem[key]
        
        reordered_problems.append(reordered_problem)

    neetcode_data["problems"] = reordered_problems

    # Save the updated data back to the file
    with open(neetcode_path, "w") as f:
        json.dump(neetcode_data, f, indent=2)


if __name__ == "__main__":
    add_missing_fields()
