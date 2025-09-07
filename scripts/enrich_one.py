import json
import os
import sys

from scripts.enrich_problem import _simplify_discussion_comments, get_discussion_data, get_problem_data


def enrich_file(problem_file: str) -> None:
    with open(problem_file) as f:
        data = json.load(f)

    slug = data.get("slug")
    if not slug:
        print(f"No slug in {problem_file}")
        return

    problem_data = get_problem_data(slug)
    if problem_data and "data" in problem_data and problem_data["data"].get("question"):
        question_data = problem_data["data"]["question"]

        original_id = data.get("id")
        original_leetcode_url = data.get("leetcode_url")
        data.update(question_data)
        if original_id:
            data["id"] = original_id
        if original_leetcode_url:
            data["leetcode_url"] = original_leetcode_url

        if data.get("stats"):
            data["stats"] = json.loads(data["stats"])
        if data.get("similarQuestions"):
            similar_questions_list = json.loads(data["similarQuestions"])
            for q in similar_questions_list:
                if "translatedTitle" in q:
                    del q["translatedTitle"]
                if "titleSlug" in q:
                    q["slug"] = q.pop("titleSlug")
            data["similar_questions"] = similar_questions_list
            del data["similarQuestions"]
        if data.get("metaData"):
            data["metaData"] = json.loads(data["metaData"])
        if data.get("companyTagStats"):
            company_stats = json.loads(data["companyTagStats"])
            filtered = {}
            for key, companies in company_stats.items():
                keep = [c for c in companies if c.get("timesEncountered", 0) > 10]
                if keep:
                    filtered[key] = keep
            if filtered:
                data["company_tag_stats"] = filtered
            del data["companyTagStats"]
        if "solution" in data:
            del data["solution"]
        if "codeSnippets" in data:
            del data["codeSnippets"]
    else:
        print(f"Could not retrieve problem data for {slug}")

    discussion_data = get_discussion_data(slug)
    if discussion_data and "data" in discussion_data and discussion_data["data"].get("topicComments"):
        comments = discussion_data["data"]["topicComments"].get("data", [])
        data["discussion_posts"] = _simplify_discussion_comments(comments)
        print(f"Fetched {len(comments)} discussion comments for {slug}")
    else:
        print(f"Could not retrieve discussion data for {slug}")

    with open(problem_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Enriched {problem_file}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/enrich_one.py <problem_json_path>")
        sys.exit(1)
    problem_file = sys.argv[1]
    if not os.path.exists(problem_file):
        print(f"File not found: {problem_file}")
        sys.exit(1)
    enrich_file(problem_file)


if __name__ == "__main__":
    main()
