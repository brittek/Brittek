#!/usr/bin/env python3
"""Validate the Brittek brand kit and its use in the presentation.

Checks:
- brand/marks.svg defines the canonical symbols (#brtk, #command, #asterisk)
- the presentation's inline sprite matches brand/marks.svg exactly
- every font the presentation declares exists under brand/fonts
- the presentation requests nothing from a third-party origin
- no retired mark ids (m-wm, m-rt, m-ast, m-cmd, lgpath) remain
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SPRITE = ROOT / "brand" / "marks.svg"
PAGE = ROOT / "presentation" / "index.html"
REQUIRED_SYMBOLS = ("brtk", "command", "asterisk")
RETIRED_IDS = ("m-wm", "m-rt", "m-ast", "m-cmd", "lgpath")


def defs(text: str) -> str:
    match = re.search(r"<defs>\n(.*?)\n</defs>", text, re.S)
    return match.group(1) if match else ""


def main() -> int:
    errors: list[str] = []
    sprite = SPRITE.read_text(encoding="utf-8")
    page = PAGE.read_text(encoding="utf-8")

    for symbol in REQUIRED_SYMBOLS:
        if f'<symbol id="{symbol}"' not in sprite:
            errors.append(f"brand/marks.svg: missing symbol #{symbol}")

    block = re.search(r"<!-- brand:marks:start.*?-->\n(.*?)<!-- brand:marks:end -->", page, re.S)
    if not block:
        errors.append("presentation: brand:marks block not found")
    elif defs(block.group(1)) != defs(sprite):
        errors.append("presentation: inline sprite differs from brand/marks.svg")

    for url in re.findall(r'url\("\.\./brand/fonts/([^"]+)"\)', page):
        if not (ROOT / "brand" / "fonts" / url).is_file():
            errors.append(f"presentation: font brand/fonts/{url} is missing")

    external = re.findall(r'(?:src|href)="(https?://[^"]+)"', page)
    hosts = {re.sub(r"^https?://([^/]+).*", r"\1", u) for u in external}
    allowed = {"brittek.net", "github.com"}
    for host in sorted(hosts - allowed):
        errors.append(f"presentation: references third-party origin {host}")
    if "fonts.googleapis.com" in page or "fonts.gstatic.com" in page:
        errors.append("presentation: Google Fonts reference found")

    for retired in RETIRED_IDS:
        if f'id="{retired}"' in page or f'#{retired}"' in page:
            errors.append(f"presentation: retired mark id {retired} is still used")

    if errors:
        print("Brand check failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Brand check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
