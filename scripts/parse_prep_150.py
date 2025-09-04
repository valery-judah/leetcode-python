import json
import re


def parse_prep_150_md():
    md_file_path = "data/leetcode_prep_150.md"
    json_file_path = "data/leetcode_prep_150.json"

    problems = []
    current_category = ""

    with open(md_file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]
        # This is a problem entry if it's not a category
        if i + 2 < len(lines) and re.search(r"\[Solution\]", lines[i + 1]):
            name = lines[i]

            solution_line = lines[i + 1]
            match = re.search(r"\[Solution\]\((.*?)\)", solution_line)
            if not match:
                i += 1
                continue

            url = match.group(1)
            problem_url_match = re.search(r"(https://leetcode.com/problems/[^/]+/)", url)
            if problem_url_match:
                leetcode_url = problem_url_match.group(1)
                slug = leetcode_url.strip("/").split("/")[-1]
            else:
                leetcode_url = ""
                slug = ""

            difficulty = lines[i + 2]

            problem = {
                "category": current_category,
                "name": name,
                "difficulty": difficulty,
                "leetcode_url": leetcode_url,
                "slug": slug,
            }
            problems.append(problem)
            i += 3
        else:
            current_category = line
            i += 1

        # This is a problem entry if it's not a category
        if i + 2 < len(lines):
            name = lines[i]

            solution_line = lines[i + 1]
            match = re.search(r"\[Solution\]\((.*?)\)", solution_line)
            if not match:
                i += 1
                continue

            url = match.group(1)
            problem_url_match = re.search(r"(https://leetcode.com/problems/[^/]+/)", url)
            if problem_url_match:
                leetcode_url = problem_url_match.group(1)
                slug = leetcode_url.strip("/").split("/")[-1]
            else:
                leetcode_url = ""
                slug = ""

            difficulty = lines[i + 2]

            problem = {
                "category": current_category,
                "name": name,
                "difficulty": difficulty,
                "leetcode_url": leetcode_url,
                "slug": slug,
            }
            problems.append(problem)
            i += 3
        else:
            i += 1

    output_data = {"problems": problems}

    with open(json_file_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully parsed {len(problems)} problems and saved to {json_file_path}")


if __name__ == "__main__":
    parse_prep_150_md()
