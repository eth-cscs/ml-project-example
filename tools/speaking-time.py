#!/usr/bin/env python3
"""Estimate how long each slide's speaker notes take to say out loud.

Counting slides tells you how many there are, not whether they fit. A slide with a
twelve-line note is a two-minute slide however short it looks. This counts the words a
presenter would actually speak and turns them into minutes.

120 words per minute is deliberately conservative: it is the pace of a technical talk
given in a second language, with pauses to point at things. Anything much over a minute
per slide will not fit, and the honest fix is to move the detail into the documentation
link rather than to talk faster.

Not counted: `DOCS:` lines, the `START AT` and `CUT IF LATE` lines on module dividers,
and TODO / verification comments — none of those are spoken.

Usage: python3 tools/speaking-time.py slides/*.md [--over N]
"""

from __future__ import annotations

import argparse
import pathlib
import re

WORDS_PER_MINUTE = 120
NOT_SPOKEN = ("DOCS:", "START AT", "CUT IF LATE")
NOT_A_NOTE = ("TODO", "Verified", "The <div>", "PLACEHOLDER")
TITLE = re.compile(r"^# (.+)$", re.MULTILINE)
COMMENT = re.compile(r"<!--\n((?:(?!-->).)*?)\n-->", re.DOTALL)


def split_slides(path: pathlib.Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    slides, current = [], []
    for line in "".join(lines[end + 1 :]).splitlines(keepends=True):
        if line.strip() == "---":
            slides.append("".join(current))
            current = []
        else:
            current.append(line)
    slides.append("".join(current))
    return slides


def spoken_words(slide: str) -> int:
    total = 0
    for block in COMMENT.findall(slide):
        if block.lstrip().startswith(NOT_A_NOTE):
            continue
        for line in block.splitlines():
            text = line.strip()
            if not text or text.startswith(NOT_SPOKEN):
                continue
            total += len(re.sub(r"[`*_]", "", text.lstrip("- ")).split())
    return total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sources", nargs="+", type=pathlib.Path)
    ap.add_argument("--over", type=float, default=1.35,
                    help="report slides longer than this many minutes (default 1.35)")
    args = ap.parse_args()

    rows = []
    for path in args.sources:
        for slide in split_slides(path):
            words = spoken_words(slide)
            if not words:
                continue
            title = TITLE.search(slide)
            rows.append((words, title.group(1) if title else "(divider)", path.name))

    total = sum(w for w, _, _ in rows)
    over = sorted((w for w, _, _ in rows if w / WORDS_PER_MINUTE > args.over), reverse=True)

    print(f"{'spoken notes':<40} {total:>4} words  ~{total / WORDS_PER_MINUTE:>3.0f} min "
          f"at {WORDS_PER_MINUTE} wpm")
    if over:
        print(f"{'slides over ' + format(args.over, '.2f') + ' min':<40} {len(over):>4}")
        for words, title, name in sorted(rows, reverse=True):
            if words / WORDS_PER_MINUTE > args.over:
                print(f"  {words / WORDS_PER_MINUTE:>4.1f} min  {words:>4}w  {title[:46]}")
    else:
        print(f"{'slides over ' + format(args.over, '.2f') + ' min':<40} {'none':>4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
