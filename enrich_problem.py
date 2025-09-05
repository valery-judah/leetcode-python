import argparse
import json
import logging
import os
import random
import re
import time

import requests

# Track consecutive rate limit hits across requests
RATE_LIMIT_STATE = {"consecutive_429": 0}


def _setup_logging(log_file: str, log_level: str = "INFO") -> logging.Logger:
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger = logging.getLogger("enrich")
    logger.setLevel(level)
    # Avoid duplicate handlers on rerun in same interpreter
    if not logger.handlers:
        fmt = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(fmt)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger


def get_problem_data(slug, backoff_base=30, retries=3, logger: logging.Logger | None = None):
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
        "Referer": f"https://leetcode.com/problems/{slug}/",
    }

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
                # Reset global rate-limit counter on success
                RATE_LIMIT_STATE["consecutive_429"] = 0
                return response.json()
            elif response.status_code == 429:
                base = backoff_base
                jitter = random.uniform(0, 5)
                wait_time = base * (2**attempt) + jitter
                if logger:
                    logger.warning(
                        f"429 for problem {slug}. Backing off {wait_time:.1f}s "
                        f"(attempt {attempt+1}/{retries})"
                    )
                RATE_LIMIT_STATE["consecutive_429"] += 1
                time.sleep(wait_time)
            else:
                if logger:
                    logger.error(f"Error fetching problem {slug}: {response.status_code} {response.text}")
                return None  # Don't retry on other errors
        except requests.exceptions.RequestException as e:
            if logger:
                logger.warning(f"Request failed for {slug}: {e}. Attempt {attempt + 1} of {retries}")
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


def get_discussion_data(
    slug,
    micro_delay_min=1.5,
    micro_delay_max=3.5,
    backoff_base=30,
    retries=3,
    logger: logging.Logger | None = None,
):
    """Fetches the top 10 most-voted discussion comments for a given problem slug."""
    url = "https://leetcode.com/graphql"

    # Step 1: get the single discussion topic id for this question
    topic_query = """
    query questionDiscussionTopic($titleSlug: String!) {
      questionDiscussionTopic(questionSlug: $titleSlug) {
        id
        topLevelCommentCount
      }
    }
    """
    topic_vars = {"titleSlug": slug}

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
        # Use the Discussions tab as the referer to match the query context
        "Referer": f"https://leetcode.com/problems/{slug}/discuss/",
    }

    for attempt in range(retries):
        try:
            # Step 1 request: get topic id
            response = requests.post(
                url,
                json={"query": topic_query, "variables": topic_vars},
                cookies=cookies,
                headers=headers,
                timeout=10,
            )
            if response.status_code != 200:
                if response.status_code == 429:
                    base = backoff_base
                    jitter = random.uniform(0, 5)
                    wait_time = base * (2**attempt) + jitter
                    if logger:
                        logger.warning(
                            f"429 on topic for {slug}. Backing off {wait_time:.1f}s "
                            f"(attempt {attempt+1}/{retries})"
                        )
                    RATE_LIMIT_STATE["consecutive_429"] += 1
                    time.sleep(wait_time)
                    continue
                if logger:
                    logger.error(f"Error topic {slug}: {response.status_code} {response.text}")
                return None

            topic_json = response.json()
            if "errors" in topic_json:
                if logger:
                    logger.error(f"GraphQL error topic {slug}: {topic_json['errors']}")
                return None

            topic = topic_json.get("data", {}).get("questionDiscussionTopic")
            if not topic or not topic.get("id"):
                print(f"No discussion topic found for {slug}")
                return None

            topic_id = topic["id"]

            # Brief pause between related GraphQL calls to reduce burstiness
            time.sleep(random.uniform(micro_delay_min, micro_delay_max))

            # Step 2: fetch top comments for that topic
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
            comments_vars = {
                "topicId": topic_id,
                "orderBy": "most_votes",
                "pageNo": 1,
                "numPerPage": 10,
            }

            comments_resp = requests.post(
                url,
                json={"query": comments_query, "variables": comments_vars},
                cookies=cookies,
                headers=headers,
                timeout=10,
            )
            if comments_resp.status_code == 200:
                comments_json = comments_resp.json()
                if "errors" in comments_json:
                    if logger:
                        logger.error(f"GraphQL error comments {slug}: {comments_json['errors']}")
                    return None
                # Reset global rate-limit counter on success
                RATE_LIMIT_STATE["consecutive_429"] = 0
                return comments_json
            elif comments_resp.status_code == 429:
                base = backoff_base
                jitter = random.uniform(0, 5)
                wait_time = base * (2**attempt) + jitter
                if logger:
                    logger.warning(
                        f"429 on comments for {slug}. Backing off {wait_time:.1f}s "
                        f"(attempt {attempt+1}/{retries})"
                    )
                RATE_LIMIT_STATE["consecutive_429"] += 1
                time.sleep(wait_time)
            else:
                if logger:
                    logger.error(f"Error comments {slug}: {comments_resp.status_code} {comments_resp.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {slug} discussions: {e}. Attempt {attempt + 1} of {retries}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
            else:
                return None
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


def _simplify_discussion_comments(comments):
    """Reduce raw comment nodes to minimal fields."""
    simplified = []
    for item in comments or []:
        post = (item or {}).get("post", {})
        username = (post.get("author") or {}).get("username")
        ts = post.get("creationDate")
        year = None
        if isinstance(ts, int | float):
            try:
                year = time.gmtime(int(ts)).tm_year
            except Exception:
                year = None
        simplified.append(
            {
                "name": username,
                "year": year,
                "content": post.get("content"),
                "voteCount": post.get("voteCount"),
            }
        )
    return simplified


def parse_args():
    parser = argparse.ArgumentParser(description="Enrich LeetCode problems with GraphQL data")
    parser.add_argument("--start", type=int, default=1, help="Start problem ID (inclusive)")
    parser.add_argument("--end", type=int, default=3700, help="End problem ID (exclusive)")
    parser.add_argument(
        "--max-problems",
        type=int,
        default=None,
        help="Maximum number of problems to process this run",
    )
    parser.add_argument("--per-problem-sleep-min", type=float, default=12.0)
    parser.add_argument("--per-problem-sleep-max", type=float, default=20.0)
    parser.add_argument("--long-break-every", type=int, default=25)
    parser.add_argument("--long-break-sleep-min", type=float, default=120.0)
    parser.add_argument("--long-break-sleep-max", type=float, default=300.0)
    parser.add_argument("--micro-delay-min", type=float, default=1.5)
    parser.add_argument("--micro-delay-max", type=float, default=3.5)
    parser.add_argument("--backoff-base", type=float, default=30.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--cool-off-threshold",
        type=int,
        default=2,
        help="Consecutive 429s before global cool-off",
    )
    parser.add_argument("--cool-off-sleep-min", type=float, default=600.0, help="Cool-off minimum seconds")
    parser.add_argument("--cool-off-sleep-max", type=float, default=900.0, help="Cool-off maximum seconds")
    parser.add_argument("--log-file", type=str, default="enrich.log", help="Log file path")
    parser.add_argument(
        "--log-level", type=str, default="INFO", help="Logging level: DEBUG, INFO, WARNING, ERROR"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    logger = _setup_logging(args.log_file, args.log_level)
    logger.info(
        "Starting enrichment with settings: start=%s end=%s max=%s per_sleep=[%s,%s] "
        "long_every=%s long_sleep=[%s,%s] micro=[%s,%s] backoff=%s retries=%s "
        "cool_thr=%s cool_sleep=[%s,%s]",
        args.start,
        args.end,
        args.max_problems,
        args.per_problem_sleep_min,
        args.per_problem_sleep_max,
        args.long_break_every,
        args.long_break_sleep_min,
        args.long_break_sleep_max,
        args.micro_delay_min,
        args.micro_delay_max,
        args.backoff_base,
        args.retries,
        args.cool_off_threshold,
        args.cool_off_sleep_min,
        args.cool_off_sleep_max,
    )
    problem_files = os.listdir("archive/problems")

    processed = 0
    enriched_ok = 0
    problem_data_fail = 0
    discuss_ok = 0
    discuss_fail = 0
    solutions_saved = 0
    t0 = time.time()
    for i in range(args.start, args.end):
        if args.max_problems is not None and processed >= args.max_problems:
            print(f"Reached max problems for this run: {args.max_problems}")
            break
        problem_id = str(i).zfill(4)
        problem_file = None
        for f in problem_files:
            if f.startswith(problem_id) and f.endswith(".json"):
                problem_file = os.path.join("archive/problems", f)
                break

        if not problem_file:
            logger.info(f"No problem file found for ID {problem_id}")
            continue

        try:
            with open(problem_file) as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            logger.warning(f"Could not decode JSON from {problem_file}. Skipping.")
            continue

        # Manually define the code definition for simplicity
        code_definition = {
            "value": "python3",
            "text": "Python3",
            "defaultCode": (
                "class Solution:\n    def containsDuplicate(self, nums: List[int]) -> bool:\n        "
            ),
        }

        new_data = existing_data.copy()

        if code_definition.get("value") == "python3" and "sampleTestCase" in new_data:
            structured_snippet = parse_python_snippet(
                code_definition["defaultCode"], new_data["sampleTestCase"]
            )
            if structured_snippet:
                new_data["python3_snippet"] = structured_snippet

        problem_data = get_problem_data(
            new_data.get("slug"), backoff_base=args.backoff_base, retries=args.retries, logger=logger
        )
        if problem_data and "data" in problem_data and problem_data["data"]["question"]:
            question_data = problem_data["data"]["question"]
            enriched_ok += 1

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

            # The stats, similarQuestions, and metaData fields are returned as strings,
            # so they need to be parsed
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
                        company for company in companies if company.get("timesEncountered", 0) > 10
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
                solutions_saved += 1
            else:
                logger.info(f"No solution content available for problem {new_data.get('id')}")

            # Persist problem description/content as markdown as well
            # LeetCode returns HTML in the `content` field; markdown can render raw HTML.
            if new_data.get("content"):
                base = f"archive/problems/{problem_id}-{new_data.get('slug')}"
                desc_md = f"{base}.description.md"
                desc_html = f"{base}.description.html"
                try:
                    # Save raw HTML into both MD (for markdown renderers) and HTML file
                    with open(desc_md, "w") as df_md:
                        df_md.write(new_data["content"])  # markdown will render HTML
                    with open(desc_html, "w") as df_html:
                        df_html.write(new_data["content"])  # same payload as HTML fragment
                except OSError as e:
                    logger.warning(f"Failed saving descriptions for {new_data.get('slug')}: {e}")
        else:
            logger.warning(f"Could not retrieve problem data for problem {new_data.get('id')}")
            problem_data_fail += 1

        discussion_data = get_discussion_data(
            new_data.get("slug"),
            micro_delay_min=args.micro_delay_min,
            micro_delay_max=args.micro_delay_max,
            backoff_base=args.backoff_base,
            retries=args.retries,
            logger=logger,
        )
        if discussion_data and "data" in discussion_data and discussion_data["data"].get("topicComments"):
            comments = discussion_data["data"]["topicComments"].get("data", [])
            new_data["discussion_posts"] = _simplify_discussion_comments(comments)
            discuss_ok += 1
        else:
            logger.warning(f"Could not retrieve discussion data for problem {new_data.get('id')}")
            discuss_fail += 1

        with open(problem_file, "w") as f:
            json.dump(new_data, f, indent=2)
        logger.info(f"Enriched {problem_file}")
        processed += 1

        # Add a longer sleep periodically to avoid rate limits
        if i > 0 and i % args.long_break_every == 0:
            sleep_time = random.uniform(args.long_break_sleep_min, args.long_break_sleep_max)
            logger.info(f"Taking a long break for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
        else:
            time.sleep(random.uniform(args.per_problem_sleep_min, args.per_problem_sleep_max))

        # Global cool-off if too many consecutive 429s
        if RATE_LIMIT_STATE["consecutive_429"] >= args.cool_off_threshold:
            cool = random.uniform(args.cool_off_sleep_min, args.cool_off_sleep_max)
            logger.warning(
                f"Hit {RATE_LIMIT_STATE['consecutive_429']} consecutive 429s. "
                f"Cooling off for {cool:.1f} seconds..."
            )
            time.sleep(cool)
            RATE_LIMIT_STATE["consecutive_429"] = 0

    # Summary
    elapsed = time.time() - t0
    avg = (elapsed / processed) if processed else 0
    logger.info(
        "Summary: processed=%s enriched_ok=%s problem_fail=%s discuss_ok=%s "
        "discuss_fail=%s solutions_saved=%s elapsed=%.1fs avg_per_problem=%.1fs",
        processed,
        enriched_ok,
        problem_data_fail,
        discuss_ok,
        discuss_fail,
        solutions_saved,
        elapsed,
        avg,
    )


if __name__ == "__main__":
    main()
