import glob
import yaml
import re


def extract_slugs_from_file(filepath):
    """Extracts slugs from a single YAML track file."""
    slugs = []
    with open(filepath, "r") as f:
        try:
            data = yaml.safe_load(f)
            if data and "problems" in data:
                for problem in data["problems"]:
                    if "slug" in problem:
                        slugs.append(problem["slug"])
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {filepath}: {e}")
    return slugs


def main():
    """Main function to find files and extract slugs."""
    all_slugs = []
    file_pattern = "archive/track_*.yaml"

    for filepath in glob.glob(file_pattern):
        # Extract the number from the filename to filter
        match = re.search(r"track_(\d+)_", filepath)
        if match:
            track_num = int(match.group(1))
            if 1 <= track_num <= 10:
                all_slugs.extend(extract_slugs_from_file(filepath))

    for slug in sorted(list(set(all_slugs))):
        print(slug)


if __name__ == "__main__":
    main()
