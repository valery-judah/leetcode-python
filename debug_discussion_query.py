import json

import requests


def get_discussion_data(slug):
    """Fetches the top 10 discussion topics for a given problem slug."""
    url = "https://leetcode.com/graphql"
    query = """
    query questionDiscussionTopic($titleSlug: String!) {
      questionDiscussionTopic(questionSlug: $titleSlug) {
        id
        topLevelCommentCount
      }
    }
    """
    variables = {"titleSlug": slug}

    with open(".leetcode.creds/csrftoken") as f:
        csrftoken = f.read().strip()
    with open(".leetcode.creds/LEETCODE_SESSION") as f:
        leetcode_session = f.read().strip()

    cookies = {
        "csrftoken": csrftoken,
        "LEETCODE_SESSION": leetcode_session,
    }

    headers = {
        "x-csrftoken": csrftoken,
        "Referer": f"https://leetcode.com/problems/{slug}/discuss/",
    }

    try:
        # Step 1: get the discussion topic id for the question
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            cookies=cookies,
            headers=headers,
            timeout=10,
        )
        if response.status_code != 200:
            print(f"Error fetching discussion data for {slug}: {response.status_code} {response.text}")
            return None

        response_json = response.json()
        print("Topic lookup:")
        print(json.dumps(response_json, indent=2))
        if "errors" in response_json:
            print(f"GraphQL error for {slug} discussions: {response_json['errors']}")
            return None

        topic = response_json.get("data", {}).get("questionDiscussionTopic")
        if not topic or not topic.get("id"):
            print("No discussion topic id found")
            return response_json

        topic_id = topic["id"]

        # Step 2: fetch top 10 top-level comments sorted by most voted
        comments_query = """
        query topicComments($topicId: Int!, $orderBy: String!, $pageNo: Int!, $numPerPage: Int!) {
          topicComments(topicId: $topicId, orderBy: $orderBy, pageNo: $pageNo, numPerPage: $numPerPage) {
            totalNum
            data {
              id
              post {
                id
                content
                voteCount
                creationDate
                author {
                  username
                  profile { userAvatar reputation }
                }
              }
            }
          }
        }
        """
        comments_variables = {"topicId": topic_id, "orderBy": "most_votes", "pageNo": 1, "numPerPage": 10}

        comments_resp = requests.post(
            url,
            json={"query": comments_query, "variables": comments_variables},
            cookies=cookies,
            headers=headers,
            timeout=10,
        )
        if comments_resp.status_code != 200:
            print(f"Error fetching topic comments: {comments_resp.status_code} {comments_resp.text}")
            return response_json

        comments_json = comments_resp.json()
        print("Top comments:")
        print(json.dumps(comments_json, indent=2))
        return comments_json
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {slug} discussions: {e}.")
        return None


if __name__ == "__main__":
    get_discussion_data("two-sum")
