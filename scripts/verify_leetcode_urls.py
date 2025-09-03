import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def verify_url(url):
    """Verify a single URL."""
    if not url:
        return url, False, "Missing URL"
    try:
        # Add a random delay to be less aggressive
        time.sleep(random.uniform(0.5, 1.5))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Use GET with stream=True to be less suspicious, and a shorter timeout
        response = requests.get(url, headers=headers, allow_redirects=True, timeout=5, stream=True)
        is_valid = response.status_code == 200
        reason = f"Status Code: {response.status_code}" if not is_valid else "OK"
        response.close() # close the connection
        return url, is_valid, reason
    except requests.RequestException as e:
        return url, False, str(e)

def verify_leetcode_urls(file_path):
    """
    Verify all LeetCode URLs in the given JSON file concurrently.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    urls_to_verify = [problem.get('leetcode_url') for problem in data['problems'] if problem.get('leetcode_url')]
    invalid_urls = []

    # Reduce the number of workers to be less aggressive
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(verify_url, url): url for url in urls_to_verify}
        for future in as_completed(future_to_url):
            url, is_valid, reason = future.result()
            if not is_valid:
                invalid_urls.append({'url': url, 'reason': reason})
            print(f"Checked URL: {url} - {'Valid' if is_valid else 'Invalid'}")

    if invalid_urls:
        print("\n--- Invalid URLs Found ---")
        for item in invalid_urls:
            print(f"URL: {item['url']}\nReason: {item['reason']}\n")
    else:
        print("\nAll LeetCode URLs are valid.")

if __name__ == "__main__":
    json_file_path = 'data/neetcode_250_complete.json'
    verify_leetcode_urls(json_file_path)
