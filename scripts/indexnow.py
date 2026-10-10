"""Tell Bing (and other IndexNow engines) about new or updated pages.

Usage: python3 scripts/indexnow.py https://kseniiashermin.com/blog/some-post/ [more URLs]

Run it after a deploy is live. The key is public by design: IndexNow verifies it by
fetching public/<key>.txt from the live site, so the file name is the key.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

HOST = "kseniiashermin.com"
PUBLIC = Path(__file__).resolve().parent.parent / "public"


def find_key() -> str:
    keys = [p.stem for p in PUBLIC.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem)]
    if len(keys) != 1:
        sys.exit(f"Expected exactly one IndexNow key file in {PUBLIC}, found {len(keys)}")
    return keys[0]


def main(urls: list[str]) -> None:
    if not urls or any(not u.startswith(f"https://{HOST}/") for u in urls):
        sys.exit(f"Pass one or more full https://{HOST}/ URLs")
    key = find_key()
    body = json.dumps({
        "host": HOST,
        "key": key,
        "keyLocation": f"https://{HOST}/{key}.txt",
        "urlList": urls,
    }).encode()
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        print(f"IndexNow responded {resp.status} for {len(urls)} URL(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
