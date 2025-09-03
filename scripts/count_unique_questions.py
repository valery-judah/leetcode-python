import json

def count_unique_similar_questions(file_path):
    """
    Counts the number of unique similar questions that are not already in the main problem list.

    Args:
        file_path (str): The path to the JSON file containing the problem data.

    Returns:
        int: The number of unique similar questions not in the main list.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    main_problem_slugs = {problem['slug'] for problem in data['problems']}
    
    similar_questions = []
    for problem in data['problems']:
        similar_questions.extend(problem.get('similar_questions', []))

    unique_similar_slugs = set()
    for question in similar_questions:
        if question['slug'] not in main_problem_slugs:
            unique_similar_slugs.add(question['slug'])

    return len(unique_similar_slugs)

if __name__ == "__main__":
    count = count_unique_similar_questions('data/neetcode_250_complete.json')
    print(f"There are {count} unique similar questions not in the main list.")
