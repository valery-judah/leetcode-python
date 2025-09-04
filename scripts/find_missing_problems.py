import json

def find_missing_problems():
    """
    Finds problems in leetcode_prep_150.json that are not in neetcode_250.json.
    """
    with open('data/leetcode_prep_150.json', 'r') as f:
        leetcode_prep_data = json.load(f)

    with open('data/neetcode_250.json', 'r') as f:
        neetcode_data = json.load(f)

    leetcode_problem_slugs = {problem['slug'] for problem in leetcode_prep_data['problems']}
    neetcode_problem_slugs = {problem['slug'] for problem in neetcode_data['problems']}

    missing_slugs = leetcode_problem_slugs - neetcode_problem_slugs

    missing_problems = [
        problem for problem in leetcode_prep_data['problems']
        if problem['slug'] in missing_slugs
    ]

    with open('data/neetcode_250_similars.json', 'r') as f:
        neetcode_similars_data = json.load(f)

    neetcode_similars_slugs = {problem['slug'] for problem in neetcode_similars_data['problems']}

    present_in_similars = [
        problem for problem in missing_problems
        if problem['slug'] in neetcode_similars_slugs
    ]

    not_present_in_similars = [
        problem for problem in missing_problems
        if problem['slug'] not in neetcode_similars_slugs
    ]

    with open('data/neetcode_all.json', 'r') as f:
        neetcode_all_data = json.load(f)
    neetcode_all_slugs = {problem['slug'] for problem in neetcode_all_data['problems']}

    not_present_in_either = [p for p in not_present_in_similars if p['slug'] not in neetcode_all_slugs]

    # --- Cluster Analysis ---
    clusters = {}
    for problem in not_present_in_either:
        category = problem.get('category', 'Uncategorized')
        if category not in clusters:
            clusters[category] = []
        clusters[category].append(problem)

    # --- Generate Markdown Output ---
    analysis_output = ["# LeetCode Prep 150 Gap Analysis & Recommendations\n"]
    analysis_output.append("This analysis identifies problems from the 'LeetCode Prep 150' list that are not present in any of the NeetCode lists (250, All, or Similars), suggesting they represent unique challenges not covered in the NeetCode curriculum.\n")
    analysis_output.append("## Recommended Order of Study\n")
    analysis_output.append("To efficiently cover these gaps, I recommend tackling the problems grouped by category, starting with the easiest difficulty first.\n")

    difficulty_order = ['Easy', 'Medium', 'Hard']
    
    for category in sorted(clusters.keys()):
        analysis_output.append(f"### {category}\n")
        
        sorted_problems = sorted(clusters[category], key=lambda x: difficulty_order.index(x.get('difficulty', 'Hard')))
        
        for problem in sorted_problems:
            analysis_output.append(f"- **{problem['name']}** (ID: {problem['id']}, Difficulty: {problem['difficulty']})")
        analysis_output.append("") # Add a newline for spacing

    # --- Read existing analysis and prepend new content ---
    try:
        with open('data/analysis.md', 'r') as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = ""

    final_output = "\n".join(analysis_output) + "\n\n" + existing_content

    with open('data/analysis.md', 'w') as f:
        f.write(final_output)
    
    print("Analysis complete. Results have been prepended to 'data/analysis.md'.")


if __name__ == "__main__":
    find_missing_problems()
