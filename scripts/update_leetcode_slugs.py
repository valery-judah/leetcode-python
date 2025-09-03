import json
import re

def update_leetcode_slugs(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    updated_problems = []
    for problem in data['problems']:
        leetcode_url = problem.get('leetcode_url')
        if leetcode_url:
            # Extract the slug from the leetcode_url
            match = re.search(r'/problems/([^/]+)/?$', leetcode_url)
            if match:
                problem['slug'] = match.group(1)
            else:
                print(f"Warning: Could not extract slug from URL: {leetcode_url} for problem: {problem.get('name')}")
        else:
            # If leetcode_url is missing, try to derive from name (lowercase, replace spaces with hyphens)
            problem_name = problem.get('name')
            if problem_name:
                derived_slug = problem_name.lower().replace(' ', '-')
                # Remove any characters that are not alphanumeric or hyphens
                derived_slug = re.sub(r'[^a-z0-9-]', '', derived_slug)
                problem['slug'] = derived_slug
                print(f"Warning: 'leetcode_url' missing for problem '{problem_name}'. Derived slug: '{derived_slug}'")
            else:
                print(f"Warning: Problem entry missing 'name' and 'leetcode_url'. Cannot determine slug.")
        updated_problems.append(problem)

    data['problems'] = updated_problems

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    json_file_path = 'data/neetcode_250_complete.json'
    update_leetcode_slugs(json_file_path)
    print(f"Updated slugs in {json_file_path}")
