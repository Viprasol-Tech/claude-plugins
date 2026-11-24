#!/usr/bin/env python3
"""Validate the Viprasol marketplace manifest, optionally against GitHub.

Part of claude-plugins by Viprasol Tech Private Limited.

  python tests/validate_marketplace.py            # structure only, offline
  python tests/validate_marketplace.py --remote   # also fetch each plugin.json from GitHub

`claude plugin validate` checks structure but never fetches remote sources, so
a wrong url or path would only fail when someone installs. --remote catches it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REPO = re.compile(r"^[A-Za-z0-9-]+/[A-Za-z0-9._-]+$")


def fail(msg: str) -> None:
    print("FAIL", msg)
    sys.exit(1)


def check_structure(data: dict) -> list[dict]:
    for key in ("name", "owner", "plugins"):
        if key not in data:
            fail(f"marketplace.json: missing '{key}'")
    if not NAME.match(data["name"]):
        fail(f"marketplace name '{data['name']}' must be kebab-case")
    seen = set()
    for p in data["plugins"]:
        n = p.get("name", "")
        if not NAME.match(n) or n.startswith("claude-"):
            fail(f"plugin name '{n}' must be kebab-case and must not start with 'claude-'")
        if n in seen:
            fail(f"duplicate plugin name '{n}'")
        seen.add(n)
        if len(p.get("description", "")) < 40:
            fail(f"{n}: description missing or too short")
        src = p.get("source")
        if not isinstance(src, dict) or src.get("source") != "git-subdir":
            fail(f"{n}: source must be a git-subdir object")
        if not REPO.match(src.get("url", "")) or not src.get("path") or src["path"].startswith(("/", "..")):
            fail(f"{n}: git-subdir needs url 'owner/repo' and a relative path")
    return data["plugins"]


def check_remote(plugins: list[dict]) -> None:
    for p in plugins:
        s = p["source"]
        url = f"https://raw.githubusercontent.com/{s['url']}/{s.get('ref', 'HEAD')}/{s['path']}/.claude-plugin/plugin.json"
        try:
            with urllib.request.urlopen(url, timeout=20) as r:  # noqa: S310 - fixed https host
                manifest = json.load(r)
        except Exception as exc:  # network, 404, bad JSON
            fail(f"{p['name']}: cannot read {url}: {exc}")
        if manifest.get("name") != p["name"]:
            fail(f"{p['name']}: remote plugin.json is named '{manifest.get('name')}'")
        print(f"ok  {p['name']:24} {s['url']}/{s['path']}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--remote", action="store_true", help="Fetch each plugin.json from GitHub")
    a = ap.parse_args()
    data = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    plugins = check_structure(data)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for p in plugins:
        if f"{p['name']}@{data['name']}" not in readme:
            fail(f"README has no install line for {p['name']}@{data['name']}")
    if a.remote:
        check_remote(plugins)
    print(f"OK: marketplace '{data['name']}' with {len(plugins)} plugins")
    return 0


if __name__ == "__main__":
    sys.exit(main())
