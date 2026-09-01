#!/usr/bin/env python3
"""Concatenate the per-module Marp files into a single deck, images and all.

Each ``slides/NN-*.md`` file is a standalone Marp deck so that a module owner can
build and rehearse their own part. For the full 60-minute session we need one
document, so this script keeps the YAML front matter of the first module and
drops it from the others, joining the modules with a slide separator.

It also inlines local images as data URIs, which is not cosmetic. A slide writes
``![](../assets/screenshots/x.png)``, a path relative to ``slides/``. Marp copies that
path into the HTML untouched — it inlines the theme but not image tags — and the deck is
written to ``build/``, from where the same relative path still happens to resolve. So the
local HTML looks correct. What is published to GitHub Pages is ``build/`` alone, and
there ``../assets/`` points outside the site root: the image 404s and the reader gets the
alt text on a blank slide. The PDF hides the problem too, because Chromium reads the file
at render time. Inlining here makes the HTML genuinely self-contained, which is what the
Makefile has always claimed it was.

With ``--no-notes`` the speaker notes are removed as well. Marp writes presenter notes
as HTML comments, which means they travel into every output: the HTML embeds them for the
presenter view, ``--pdf-notes`` attaches them as annotations, and PowerPoint gets them in
the notes pane. That is what you want on stage and not what you want on a public link —
the notes carry the running order, the timings and the "cut this if late" decisions.
Marp *directives* are HTML comments too, so they are matched by name and kept; anything
unrecognised is treated as a note and dropped, because failing towards dropping is the
only safe direction here.

Usage: python3 tools/assemble.py slides/00-intro.md slides/01-... -o build/deck.md
       python3 tools/assemble.py --no-notes ... -o build/deck-public.md
"""

from __future__ import annotations

import argparse
import base64
import mimetypes
import pathlib
import re
import sys

FRONT_MATTER_DELIM = "---"

# ![alt](path) — but not ![alt](https://...) or an already-inlined data: URI.
MARKDOWN_IMAGE = re.compile(r"(!\[[^\]]*\]\()(?!\w+:)([^)\s]+)(\))")

HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.S)

# Every Marp directive, global and per-slide. A comment is kept only if every line in it
# names one of these; everything else is a speaker note. The list is the whole contract:
# a directive missing from it gets dropped and the slide visibly breaks, which is a
# failure you see. The reverse — a note mistaken for a directive — is a failure you
# publish.
DIRECTIVES = {
    "marp", "theme", "style", "headingdivider", "paginate", "header", "footer", "class",
    "backgroundcolor", "backgroundimage", "backgroundposition", "backgroundrepeat",
    "backgroundsize", "color", "size", "transition", "math", "lang",
}
DIRECTIVE_LINE = re.compile(r"^\s*_?([A-Za-z][A-Za-z0-9]*)\s*:")


def is_directive(comment: str) -> bool:
    """True if the comment is Marp configuration rather than a speaker note."""
    lines = [line for line in comment.splitlines() if line.strip()]
    if not lines:
        return False
    return all((match := DIRECTIVE_LINE.match(line)) is not None
               and match.group(1).lower() in DIRECTIVES for line in lines)


def strip_notes(body: str) -> str:
    """Drop every speaker note, keeping Marp directives."""
    return HTML_COMMENT.sub(
        lambda m: m.group(0) if is_directive(m.group(1)) else "", body)


def inline_images(body: str, source: pathlib.Path) -> str:
    """Replace local image paths with data URIs, resolved relative to the slide file."""

    def replace(match: re.Match[str]) -> str:
        asset = (source.parent / match.group(2)).resolve()
        if not asset.is_file():
            print(f"assemble.py: warning: {source}: missing image {match.group(2)}",
                  file=sys.stderr)
            return match.group(0)
        mime = mimetypes.guess_type(asset.name)[0] or "application/octet-stream"
        payload = base64.b64encode(asset.read_bytes()).decode("ascii")
        return f"{match.group(1)}data:{mime};base64,{payload}{match.group(3)}"

    return MARKDOWN_IMAGE.sub(replace, body)


def split_front_matter(text: str) -> tuple[str, str]:
    """Return (front_matter, body). Front matter is empty if the file has none."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONT_MATTER_DELIM:
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONT_MATTER_DELIM:
            return "\n".join(lines[: i + 1]), "\n".join(lines[i + 1 :])
    # Unterminated front matter: treat the whole file as body rather than guessing.
    return "", text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="+", type=pathlib.Path)
    parser.add_argument("-o", "--output", required=True, type=pathlib.Path)
    parser.add_argument("--no-notes", action="store_true",
                        help="drop the speaker notes: for anything published publicly")
    args = parser.parse_args()

    missing = [str(p) for p in args.sources if not p.is_file()]
    if missing:
        print(f"assemble.py: no such file: {', '.join(missing)}", file=sys.stderr)
        return 1

    front_matter = ""
    bodies: list[str] = []

    for index, source in enumerate(args.sources):
        fm, body = split_front_matter(source.read_text(encoding="utf-8"))
        if index == 0:
            front_matter = fm
        elif not fm:
            print(f"assemble.py: warning: {source} has no front matter", file=sys.stderr)
        # No provenance comment here on purpose: Marp turns every non-directive HTML
        # comment into a presenter note, so a "source:" marker would land in the
        # speaker-notes pane of the first slide of each module.
        body = strip_notes(body) if args.no_notes else body
        bodies.append(inline_images(body.strip(), source))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    parts = [front_matter] if front_matter else []
    parts.append(f"\n\n{FRONT_MATTER_DELIM}\n\n".join(bodies))
    args.output.write_text("\n".join(parts) + "\n", encoding="utf-8")

    kept = "without speaker notes" if args.no_notes else "with speaker notes"
    print(f"assemble.py: wrote {args.output} from {len(args.sources)} module(s), {kept}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
