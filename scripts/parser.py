from __future__ import annotations

import json
import re
from html import unescape


def parse_meta(meta_raw: object) -> dict | None:
    """Return metaData as a dict when provided as dict or JSON string; else None."""
    meta: dict | None = None
    if isinstance(meta_raw, dict):
        meta = meta_raw
    elif isinstance(meta_raw, str):
        try:
            loaded = json.loads(meta_raw)
            if isinstance(loaded, dict):
                meta = loaded
        except Exception:
            meta = None
    return meta


def parse_examples_for_cases(
    meta: dict | None, content_html: str | None
) -> list[tuple[str, list[str], str | None]]:
    """Parse examples from HTML into TEST_CASES entries.

    Returns a list of tuples: (label, args_exprs, expected_expr_or_None).
    - args_exprs are Python expression strings matching the meta parameter order.
    - expected may be None when not found.
    """
    if not meta or not content_html:
        return []

    # Gather meta param names in order
    params_seq: list[str] = []
    params_raw = meta.get("params") if isinstance(meta, dict) else None
    if isinstance(params_raw, list):
        for it in params_raw:
            if isinstance(it, dict) and it.get("name"):
                params_seq.append(str(it["name"]))
    if not params_seq:
        return []

    # Find all <pre> blocks and attempt to extract Input/Output lines
    blocks = re.findall(r"<pre>(.*?)</pre>", content_html, re.IGNORECASE | re.DOTALL)
    cases: list[tuple[str, list[str], str | None]] = []
    for i, blob in enumerate(blocks, start=1):
        text = unescape(blob)
        text = re.sub(r"<[^>]+>", "", text)
        # Normalize spacing
        text = text.replace("\r", "")
        # Extract Input and Output sections
        input_match = re.search(r"Input:\s*(.*?)Output:", text, re.DOTALL | re.IGNORECASE)
        output_match = re.search(r"Output:\s*(.*?)(?:Explanation:|$)", text, re.DOTALL | re.IGNORECASE)

        if not input_match:
            input_match = re.search(r"Input:\s*(.*?)\nOutput:", text, re.DOTALL | re.IGNORECASE)
        if not output_match:
            output_match = re.search(r"Output:\s*(.*?)\n(?:Explanation:|$)", text, re.DOTALL | re.IGNORECASE)

        if not input_match or not output_match:
            continue

        input_part = input_match.group(1).strip()
        expected_raw = output_match.group(1).strip()

        def to_py(val: str) -> str:
            v = val.strip()
            # For multiline values, remove newlines and surrounding whitespace
            v = re.sub(r"\s*\n\s*", "", v)
            v = re.sub(r"\btrue\b", "True", v, flags=re.IGNORECASE)
            v = re.sub(r"\bfalse\b", "False", v, flags=re.IGNORECASE)
            v = re.sub(r"\bnull\b", "None", v, flags=re.IGNORECASE)
            v = re.sub(r"_", "None", v)
            return v

        args_exprs = []
        if len(params_seq) == 1:
            match = re.match(r"\w+\s*=\s*(.*)", input_part, re.DOTALL)
            if match:
                args_exprs.append(to_py(match.group(1).strip()))
            else:
                args_exprs.append(to_py(input_part.strip()))
        else:
            # Split by comma, but respect brackets
            parts = re.split(r",\s*(?![^\[]*\])", input_part)
            for part in parts:
                match = re.match(r"\w+\s*=\s*(.*)", part, re.DOTALL)
                if match:
                    args_exprs.append(to_py(match.group(1).strip()))
                else:
                    args_exprs.append(to_py(part.strip()))

        if len(args_exprs) != len(params_seq):
            continue

        expected_expr: str | None = None
        if expected_raw is not None:
            expected_expr = to_py(expected_raw)

        cases.append((f"ex{i}", args_exprs, expected_expr))

    return cases
