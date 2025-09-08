import re
import subprocess


def get_ids_from_script():
    """Runs the map_slugs_to_ids.py script and returns the IDs."""
    ids = set()
    result = subprocess.run(["python3", "map_slugs_to_ids.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running map_slugs_to_ids.py: {result.stderr}")
        return ids

    for line in result.stdout.strip().split("\n"):
        match = re.search(r": (\d+)$", line)
        if match:
            ids.add(int(match.group(1)))
    return ids


def get_ids_from_file(filepath):
    """Reads a file and returns a set of IDs."""
    ids = set()
    try:
        with open(filepath) as f:
            for line in f:
                if line.strip().isdigit():
                    ids.add(int(line.strip()))
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    return ids


def main():
    """Unions IDs from multiple sources and writes to a file."""
    script_ids = get_ids_from_script()
    union_file_ids = get_ids_from_file("ids_union.txt")
    tracks_file_ids = get_ids_from_file("ids_tracks.txt")

    all_ids = sorted(list(script_ids.union(union_file_ids, tracks_file_ids)))

    with open("ids_summ.txt", "w") as f:
        for problem_id in all_ids:
            f.write(f"{problem_id}\n")

    print(f"Successfully wrote {len(all_ids)} unique IDs to ids_summ.txt")


if __name__ == "__main__":
    main()
