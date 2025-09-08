import argparse
import json
import sys
from pathlib import Path

# When running as a script, we need to add the package to the path
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from leetcode_index._build import build
    from leetcode_index import get_id, get_slug, ID_TO_SLUG, SLUG_TO_ID
else:
    from ._build import build
    from . import get_id, get_slug, ID_TO_SLUG, SLUG_TO_ID


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    build_parser = sub.add_parser("build")
    lu = sub.add_parser("lookup")
    g = lu.add_mutually_exclusive_group(required=True)
    g.add_argument("--id", type=int)
    g.add_argument("--slug")
    sub.add_parser("dump-id-to-slug")
    sub.add_parser("dump-slug-to-id")
    a = p.parse_args()

    if a.cmd == "build":
        build()
        return

    if a.cmd == "lookup":
        print(get_slug(a.id) if a.id is not None else get_id(a.slug))
        return
    if a.cmd == "dump-id-to-slug":
        print(json.dumps(ID_TO_SLUG, sort_keys=True))
        return
    if a.cmd == "dump-slug-to-id":
        print(json.dumps(SLUG_TO_ID, sort_keys=True))
        return


if __name__ == "__main__":
    main()
