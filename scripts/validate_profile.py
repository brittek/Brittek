#!/usr/bin/env python3
"""Validate the Brittek Digital GitHub profile README.

Checks:
- required profile assets exist
- local README image/link targets exist
- HTML container tags are balanced
- images have non-empty alt text
- required Brittek profile identity strings remain present
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "brittek-keys-logo.webp",
    ROOT / "profile" / "metrics.svg",
    ROOT / "profile" / "streak.svg",
)

REQUIRED_TEXT = (
    "Brittek Digital",
    "https://brittek.net",
    "hello@brittek.net",
    "AI is infrastructure, not identity.",
    "Machine-readable first. Human-legible always.",
)

TRACKED_TAGS = {
    "a",
    "div",
    "details",
    "summary",
    "picture",
    "table",
    "tr",
    "td",
}

VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}

REMOTE_SCHEMES = {"http", "https", "mailto", "tel", "data"}


class ReadmeHTMLValidator(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.local_targets: set[str] = set()

    def handle_starttag(self, tag: str, attrs) -> None:
        attributes = dict(attrs)

        if tag in TRACKED_TAGS and tag not in VOID_TAGS:
            self.stack.append(tag)

        if tag == "img":
            alt = attributes.get("alt")
            if alt is None or not alt.strip():
                self.errors.append("<img> element is missing a non-empty alt attribute.")

        for attribute in ("src", "href", "srcset"):
            value = attributes.get(attribute)
            if not value:
                continue

            candidates = [value]
            if attribute == "srcset":
                candidates = [
                    part.strip().split()[0]
                    for part in value.split(",")
                    if part.strip()
                ]

            for candidate in candidates:
                target = normalise_local_target(candidate)
                if target:
                    self.local_targets.add(target)

    def handle_startendtag(self, tag: str, attrs) -> None:
        self.handle_starttag(tag, attrs)
        if (
            tag in TRACKED_TAGS
            and tag not in VOID_TAGS
            and self.stack
            and self.stack[-1] == tag
        ):
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        if tag not in TRACKED_TAGS:
            return

        if not self.stack:
            self.errors.append(f"Unexpected closing </{tag}> tag.")
            return

        if self.stack[-1] == tag:
            self.stack.pop()
            return

        self.errors.append(
            f"Mismatched closing </{tag}> tag; expected </{self.stack[-1]}>."
        )

        if tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            if self.stack:
                self.stack.pop()


def normalise_local_target(value: str) -> str | None:
    value = value.strip()

    if not value or value.startswith("#"):
        return None

    parsed = urlsplit(value)

    if parsed.scheme.lower() in REMOTE_SCHEMES or parsed.netloc:
        return None

    path = unquote(parsed.path).strip()

    if not path or path.startswith("/"):
        return None

    return path


def markdown_local_targets(text: str) -> set[str]:
    targets: set[str] = set()

    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        raw = match.group(1).strip()

        if raw.startswith("<") and ">" in raw:
            raw = raw[1 : raw.index(">")]
        else:
            raw = raw.split(maxsplit=1)[0]

        target = normalise_local_target(raw)
        if target:
            targets.add(target)

    return targets


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"Required file is missing: {path.relative_to(ROOT)}")

    if not README.is_file():
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")

    for required in REQUIRED_TEXT:
        if required not in text:
            errors.append(f"Required profile text is missing: {required!r}")

    parser = ReadmeHTMLValidator()
    parser.feed(text)
    parser.close()

    errors.extend(parser.errors)

    if parser.stack:
        errors.append("Unclosed HTML container tags: " + " > ".join(parser.stack))

    local_targets = parser.local_targets | markdown_local_targets(text)

    for target in sorted(local_targets):
        candidate = (ROOT / target).resolve()

        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Local target escapes repository root: {target}")
            continue

        if not candidate.exists():
            errors.append(f"Broken local target in README.md: {target}")

    if errors:
        print("Brittek profile validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Brittek profile validation passed.")
    print(f"Checked {len(local_targets)} repository-local README target(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
