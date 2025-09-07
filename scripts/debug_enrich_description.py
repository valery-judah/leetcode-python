import argparse
import logging
from pathlib import Path

from scripts.enrich_problem import _setup_logging, get_problem_data


def save_description(slug: str, out_dir: str, logger: logging.Logger) -> int:
    data = get_problem_data(slug, logger=logger)
    if not data or not data.get("data") or not data["data"].get("question"):
        logger.error(f"No question data for slug '{slug}'")
        return 1

    q = data["data"]["question"]
    content = q.get("content")
    qid = q.get("questionFrontendId") or q.get("questionId") or "0000"
    qslug = q.get("titleSlug") or slug

    if not content:
        logger.warning(f"Question has no 'content' for slug '{slug}'")
        return 2

    out_dir_path = Path(out_dir)
    out_dir_path.mkdir(parents=True, exist_ok=True)
    base = out_dir_path / f"{str(qid).zfill(4)}-{qslug}"
    md_path = base.with_suffix(".description.md")
    html_path = base.with_suffix(".description.html")
    md_path.write_text(content)
    html_path.write_text(content)
    logger.info(f"Saved descriptions to {md_path} and {html_path}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Fetch and save a problem description")
    parser.add_argument("slug", help="LeetCode problem slug, e.g. 'two-sum'")
    parser.add_argument(
        "--out-dir",
        default="archive/problems",
        help="Directory to write the description file",
    )
    parser.add_argument(
        "--log-file",
        default="enrich_debug.log",
        help="Path to a log file to write debug/info logs",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)",
    )
    args = parser.parse_args()

    logger = _setup_logging(args.log_file, args.log_level)
    rc = save_description(args.slug, args.out_dir, logger)
    raise SystemExit(rc)


if __name__ == "__main__":
    main()
