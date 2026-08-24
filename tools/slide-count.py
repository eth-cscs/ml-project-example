#!/usr/bin/env python3
"""Report slides and estimated speaking time per module.

The booked slot is 90 minutes. The presentation aims for about 60 and the rest is open
discussion, so overrunning a little is fine — what is not fine is leaving no time to
talk. This reports what would be left for the discussion, which is the number that
actually matters. The estimate is the house rule from
CLAUDE.md: roughly one minute per content slide, so a module divider counts too and
demos are not modelled at all. Treat it as a smoke alarm, not a stopwatch.

Usage: python3 tools/slide-count.py slides/*.md
"""

from __future__ import annotations

import pathlib
import sys

TARGET_MINUTES = 60   # what the presentation aims for
SLOT_MINUTES = 90     # the booked slot; the remainder is open discussion


def count_slides(path: pathlib.Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    separators = sum(1 for line in lines if line.strip() == "---")
    # A YAML front matter block contributes two "---" lines that are not separators.
    front_matter = 2 if lines and lines[0].strip() == "---" else 0
    return separators - front_matter + 1


def main(argv: list[str]) -> int:
    paths = [pathlib.Path(a) for a in argv]
    if not paths:
        print("slide-count.py: no slide files yet", file=sys.stderr)
        return 0

    total = 0
    backup = 0
    for path in paths:
        slides = count_slides(path)
        # Backup slides sit after the wrap-up and are shown only on request, so they
        # must not count against the presented time.
        if "backup" in path.name:
            backup += slides
            print(f"{str(path):<40} {slides:>3} slides            (backup, not budgeted)")
            continue
        total += slides
        print(f"{str(path):<40} {slides:>3} slides  ~{slides:>3} min")

    discussion = SLOT_MINUTES - total
    print(f"{'TOTAL (presented)':<40} {total:>3} slides  ~{total:>3} min "
          f"(target {TARGET_MINUTES})")
    if discussion < 20:
        print(f"{'left for discussion':<40} {discussion:>3} min  "
              f"— TOO LITTLE, cut something")
    else:
        print(f"{'left for discussion':<40} {discussion:>3} min  of the "
              f"{SLOT_MINUTES}-minute slot")
    if backup:
        print(f"{'plus backup':<40} {backup:>3} slides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
