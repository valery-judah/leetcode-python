import json
import re
import requests
import time
import os
import random


def get_problem_data(slug):
    """Fetches all data for a given problem slug."""
    url = "https://leetcode.com/graphql"
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        content
        difficulty
        isPaidOnly
        likes
        dislikes
        stats
        solution {
          content
        }
        similarQuestions
        topicTags {
          name
          slug
        }
        codeSnippets {
          lang
          langSlug
          code
        }
        companyTagStats
        metaData
      }
    }
    """
    variables = {"titleSlug": slug}

    with open(".leetcode.creds/csrftoken", "r") as f:
        csrftoken = f.read().strip()
    with open(".leetcode.creds/LEETCODE_SESSION", "r") as f:
        leetcode_session = f.read().strip()

    cookies = {
        "csrftoken": csrftoken,
        "LEETCODE_SESSION": leetcode_session,
    }

    headers = {
        "x-csrftoken": csrftoken,
        "Referer": f"https://leetcode.com/problems/{slug}/",
    }

    retries = 3
    for attempt in range(retries):
        try:
            response = requests.post(
                url,
                json={"query": query, "variables": variables},
                cookies=cookies,
                headers=headers,
                timeout=10,
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                wait_time = 10 * (attempt + 1)
                print(f"Rate limited for {slug}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Error fetching data for {slug}: {response.status_code} {response.text}")
                return None  # Don't retry on other errors
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {slug}: {e}. Attempt {attempt + 1} of {retries}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
            else:
                return None
    return None


def get_company_stats_for_problem(slug):
    """Fetches and extracts company-specific statistics for a given problem."""
    problem_data = get_problem_data(slug)
    if problem_data and "data" in problem_data and problem_data["data"]["question"]:
        question_data = problem_data["data"]["question"]
        if question_data.get("companyTagStats"):
            return json.loads(question_data["companyTagStats"])
    return None


def parse_python_snippet(code_string, sample_test_case):
    """Parses the LeetCode Python snippet into a structured format."""

    imports = "from typing import List"

    class_match = re.search(r"class\s+(\w+):", code_string, re.DOTALL)
    class_name = class_match.group(1) if class_match else "Solution"

    def_match = re.search(r"def\s+(.+?\(.+?\)):", code_string, re.DOTALL)
    if not def_match:
        return None

    signature_line = def_match.group(0)
    method_name = def_match.group(1).split("(")[0].strip()

    # Clean up the signature for the object
    signature = signature_line

    example_call = (
        f"solution = {class_name}()\\n"
        f"result = solution.{method_name}({sample_test_case})\\n"
        f"print(result)"
    )

    return {
        "imports": imports,
        "class_name": class_name,
        "method_name": method_name,
        "signature": signature,
        "body_placeholder": "        # Your code here\\n        pass",
        "example_call": example_call,
    }


def main():
    problem_files = os.listdir("archive/problems")
    for i in range(1, 3700):
        problem_id = str(i).zfill(4)
        problem_file = None
        for f in problem_files:
            if f.startswith(problem_id) and f.endswith(".json"):
                problem_file = os.path.join("archive/problems", f)
                break

        if not problem_file:
            print(f"No problem file found for ID {problem_id}")
            continue

        try:
            with open(problem_file, "r") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Could not decode JSON from {problem_file}. Skipping.")
            continue

        # Manually define the code definition for simplicity
        code_definition = {
            "value": "python3",
            "text": "Python3",
            "defaultCode": "class Solution:\n    def containsDuplicate(self, nums: List[int]) -> bool:\n        ",
        }

        new_data = existing_data.copy()

        if code_definition.get("value") == "python3" and "sampleTestCase" in new_data:
            structured_snippet = parse_python_snippet(
                code_definition["defaultCode"], new_data["sampleTestCase"]
            )
            if structured_snippet:
                new_data["python3_snippet"] = structured_snippet

        problem_data = get_problem_data(new_data.get("slug"))
        if problem_data and "data" in problem_data and problem_data["data"]["question"]:
            question_data = problem_data["data"]["question"]

            # Store original fields to preserve them
            original_id = new_data.get("id")
            original_leetcode_url = new_data.get("leetcode_url")
            # Enrich with all new data
            new_data.update(question_data)

            # Restore original fields
            if original_id:
                new_data["id"] = original_id
            if original_leetcode_url:
                new_data["leetcode_url"] = original_leetcode_url

            # The stats, similarQuestions, and metaData fields are returned as strings, so they need to be parsed
            if new_data.get("stats"):
                new_data["stats"] = json.loads(new_data["stats"])
            if new_data.get("similarQuestions"):
                similar_questions_list = json.loads(new_data["similarQuestions"])
                for question in similar_questions_list:
                    if "translatedTitle" in question:
                        del question["translatedTitle"]
                    if "titleSlug" in question:
                        question["slug"] = question.pop("titleSlug")
                new_data["similar_questions"] = similar_questions_list
                del new_data["similarQuestions"]
            if new_data.get("metaData"):
                new_data["metaData"] = json.loads(new_data["metaData"])
            
            if new_data.get("companyTagStats"):
                company_stats = json.loads(new_data["companyTagStats"])
                filtered_stats = {}
                for key, companies in company_stats.items():
                    filtered_companies = [
                        company
                        for company in companies
                        if company.get("timesEncountered", 0) > 10
                    ]
                    if filtered_companies:
                        filtered_stats[key] = filtered_companies
                
                if filtered_stats:
                    new_data["company_tag_stats"] = filtered_stats
                del new_data["companyTagStats"]

            if "solution" in new_data:
                del new_data["solution"]
            if "codeSnippets" in new_data:
                del new_data["codeSnippets"]

            if question_data.get("solution") and question_data["solution"]["content"]:
                solution_content = question_data["solution"]["content"]
                output_file = f"archive/problems/{problem_id}-{new_data.get('slug')}.solution.md"
                with open(output_file, "w") as f:
                    f.write(solution_content)
                print(f"Successfully saved solution to {output_file}")
            else:
                print(f"No solution content available for problem {new_data.get('id')}")
        else:
            print(f"Could not retrieve problem data for problem {new_data.get('id')}")

        with open(problem_file, "w") as f:
            json.dump(new_data, f, indent=2)
        print(f"Successfully enriched {problem_file}")

        # Add a longer sleep every 50 requests
        if i > 0 and i % 50 == 0:
            sleep_time = random.uniform(30, 60)
            print(f"Taking a long break for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
        else:
            time.sleep(random.uniform(5, 10))


if __name__ == "__main__":
    main()
