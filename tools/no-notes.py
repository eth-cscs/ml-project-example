#!/usr/bin/env python3
"""Refuse to publish anything that still carries the speaker notes.

The notes are written for the person on stage: the running order, the timings, the
"cut this slide if you are late" decisions, the asides you would say but not print. They
travel further than people expect. Marp writes them as HTML comments, and from there they
reach the presenter view embedded in the HTML, the PowerPoint notes pane, and — with
--pdf-notes — PDF annotations. Three outputs, three routes, three chances to forget one.

So this checks the built site rather than the sources: not "did we mean to strip the
notes" but "is there a copy of them in the directory we are about to publish". It is the
second line of defence. The first is assembling the public deck from sources with the
notes already removed, which is what --no-notes in assemble.py does.

The PDF check is best-effort — text inside a PDF may be compressed beyond a byte scan —
so it looks for the annotation structure that --pdf-notes creates as well as for the text
itself. The HTML and PPTX checks are exact.

Usage: python3 tools/no-notes.py build/site
"""

from __future__ import annotations

import pathlib
import re
import sys
import zipfile

# Phrases that only ever appear in a speaker note. Short and distinctive: a canary that
# also occurs in slide text would fail every build and be deleted within a week.
CANARIES = [b"CUT IF LATE", b"START AT T+", b"DOCS: docs.cscs.ch",
            b"Check the presenter timer"]

PDF_TEXT_ANNOTATION = re.compile(rb"/Subtype\s*/Text\b")


def check_html(path: pathlib.Path) -> list[str]:
    blob = path.read_bytes()
    return [f"{path}: contains {c.decode()!r}" for c in CANARIES if c in blob]


def check_pptx(path: pathlib.Path) -> list[str]:
    problems = []
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if not name.startswith("ppt/notesSlides/") or not name.endswith(".xml"):
                continue
            # A notes slide that only carries the page number is what PowerPoint writes
            # for every deck; one with prose in it is a speaker note.
            text = b"".join(re.findall(rb"<a:t>(.*?)</a:t>", archive.read(name), re.S))
            if len(text.strip()) > 24:
                problems.append(f"{path}: {name} carries {len(text)} characters of notes")
    return problems


def check_pdf(path: pathlib.Path) -> list[str]:
    blob = path.read_bytes()
    problems = [f"{path}: contains {c.decode()!r}" for c in CANARIES if c in blob]
    if PDF_TEXT_ANNOTATION.search(blob):
        problems.append(f"{path}: has text annotations — built with --pdf-notes?")
    return problems


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 2

    root = pathlib.Path(sys.argv[1])
    if not root.is_dir():
        print(f"no-notes.py: {root} is not a directory", file=sys.stderr)
        return 2

    checks = {".html": check_html, ".pptx": check_pptx, ".pdf": check_pdf}
    problems: list[str] = []
    checked = 0
    for path in sorted(root.rglob("*")):
        check = checks.get(path.suffix.lower())
        if path.is_file() and check:
            problems += check(path)
            checked += 1

    if problems:
        print("no-notes.py: speaker notes found in what is about to be published:",
              file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print(f"no-notes.py: {checked} file(s) checked, no speaker notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
