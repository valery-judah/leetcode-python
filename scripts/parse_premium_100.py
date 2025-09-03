import json
import re

def parse_premium_md():
    md_file_path = 'data/leetcode_premium_100.md'
    json_file_path = 'data/leetcode_premium_100.json'

    problems = []
    current_category = ""

    with open(md_file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('# '):
            current_category = line.lstrip('# ').strip()
            i += 1
            continue

        # This is a problem entry
        if i + 3 < len(lines):
            name = lines[i]
            
            solution_line = lines[i+1]
            match = re.search(r'\[Solution\]\((.*?)\)', solution_line)
            if not match:
                i += 1
                continue
            
            url = match.group(1)
            problem_url_match = re.search(r'(https://leetcode.com/problems/[^/]+/)', url)
            if problem_url_match:
                leetcode_url = problem_url_match.group(1)
                slug = leetcode_url.strip('/').split('/')[-1]
            else:
                leetcode_url = ""
                slug = ""

            difficulty = lines[i+2]
            
            info_line = lines[i+3]
            if info_line.startswith('#'):
                info = info_line.lstrip('#\xa0') # handle non-breaking space
                
                id_match = re.match(r'(\d+)', info)
                if id_match:
                    problem_id = id_match.group(1)
                    tags_str = info[len(problem_id):]
                    tags = re.findall('[A-Z][^A-Z]*', tags_str)
                    # A post-processing step for tags like "Depth-First"
                    j = 0
                    while j < len(tags) -1:
                        if tags[j+1] == "First":
                            tags[j] = tags[j] + "-" + tags[j+1]
                            tags.pop(j+1)
                        j += 1

                else:
                    problem_id = ""
                    tags = []
                
                problem = {
                    "category": current_category,
                    "name": name,
                    "difficulty": difficulty,
                    "leetcode_url": leetcode_url,
                    "slug": slug,
                    "id": problem_id,
                    "tags": tags,
                }
                problems.append(problem)
                i += 4
            else:
                # If the info line is missing, skip this block
                i += 3
        else:
            i += 1

    output_data = {
        "problems": problems
    }

    with open(json_file_path, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully parsed {len(problems)} problems and saved to {json_file_path}")

if __name__ == "__main__":
    parse_premium_md()
