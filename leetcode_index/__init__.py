ID_TO_SLUG, SLUG_TO_ID, INDEX_VERSION = None, None, None

__all__ = [
    "get_slug",
    "get_id",
    "exists_id",
    "exists_slug",
    "resolve",
    "ID_TO_SLUG",
    "SLUG_TO_ID",
    "INDEX_VERSION",
]


def _ensure_maps_loaded():
    global ID_TO_SLUG, SLUG_TO_ID, INDEX_VERSION
    if ID_TO_SLUG is None:
        try:
            from ._maps import ID_TO_SLUG as ID_TO_SLUG_map
            from ._maps import INDEX_VERSION as INDEX_VERSION_map
            from ._maps import SLUG_TO_ID as SLUG_TO_ID_map

            ID_TO_SLUG = {int(k): v for k, v in ID_TO_SLUG_map.items()}
            SLUG_TO_ID = SLUG_TO_ID_map
            INDEX_VERSION = INDEX_VERSION_map
        except ImportError as err:
            raise RuntimeError("E300 index not built. Run: python -m leetcode_index build") from err


def get_slug(problem_id: int) -> str:
    _ensure_maps_loaded()
    return ID_TO_SLUG[problem_id]


def get_id(slug_or_alias: str) -> int:
    _ensure_maps_loaded()
    return SLUG_TO_ID[slug_or_alias.lower()]


def exists_id(problem_id: int) -> bool:
    _ensure_maps_loaded()
    return problem_id in ID_TO_SLUG


def exists_slug(slug_or_alias: str) -> bool:
    _ensure_maps_loaded()
    return slug_or_alias.lower() in SLUG_TO_ID


def resolve(x):
    _ensure_maps_loaded()
    if isinstance(x, int):
        return x, get_slug(x)
    pid = get_id(str(x))
    return pid, get_slug(pid)
