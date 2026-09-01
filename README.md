# Alps technical training — Swiss AI Initiative Annual Meeting 2026


> This repository has been written for the Swiss AI Initiative Annual meeting of 
> (Wednesday 26 August 2026).
>
> Do not cite anything from this repository as CSCS guidance.
> [`docs.cscs.ch`](https://docs.cscs.ch) is the authority.

Material for the Alps technical training that CSCS delivers at the Swiss AI Initiative
Annual Meeting: 90 minutes, roughly 60 of presentation and 30 of open discussion, two
days before the [CSCS User Day](https://www.cscs.ch).

The session follows **one project** end to end — from "we need compute" to "the model is
trained and being served" — so that everyone leaves knowing *where the authoritative
documentation is* for the next step they personally have to take.

## Preview

The built deck is published from `main` on every push:

**→ [View the slides](https://eth-cscs.github.io/2026-swiss-ai-yearly-meeting/)**

Press `p` in the deck for presenter view: speaker notes, next slide and a timer.

## Modules

| # | Module | Budget | Status |
|---|---|---|---|
| 0 | Alps, the ML Platform, and the next hour | 5 min | scaffold |
| 1 | Project lifecycle and access | 14 min | on budget |
| 2 | Data and storage | 13 min | scaffold |
| 3 | A concrete ML use case | 30 min | Uenv, Containers, Workflow, RL example |
| 4 | Where to go from here | 3 min | scaffold |
| — | Backup, shown on request | — | HPC Console block ready |

Budgets, hand-offs between modules and the pre-agreed cuts are in
[`notes/agenda.md`](notes/agenda.md).

## Building

Slides are Markdown compiled with [Marp](https://marp.app). One source, three outputs,
speaker notes carried into all of them.

```bash
make all        # PPTX, HTML and PDF
make pptx       # PowerPoint, notes in the speaker-notes pane
make html       # self-contained HTML, press "p" for presenter view
make pdf        # PDF, notes as annotations
make handout    # the one-page A4 cheat sheet
make runsheet   # timing sheet: when each module starts, what it cuts if late
make public     # the same deck with the speaker notes stripped
make site       # build/site/ — exactly what gets published, and nothing else
make check      # slide count, speaking time, and no notes in build/site/
make M=01 module   # build one module on its own, for rehearsal
```

Requires Node.js — `npx` fetches Marp — and a Chromium that Marp can drive.

Optionally `pip install python-pptx`. With it, `make pptx` sets the speaker notes to 20pt
instead of PowerPoint's 12pt, which is the difference between glancing at them and reading
them. Without it the build says so and carries on. The HTML presenter view is enlarged
either way.

Nothing in `slides/` should contain an HTML comment that is not a speaker note or a Marp
directive: Marp turns every other comment into a presenter note, so a `TODO` in the source
ends up on stage next to the lines you have to say. Open questions and provenance live in
[`notes/open-questions.md`](notes/open-questions.md).

### What is published, and what is not

The speaker notes are written for the person on stage — the running order, the timings,
the "cut this if late" decisions — and they are not published. `make public` assembles
the deck a second time from the same sources with the notes stripped, rather than trying
to remove them from three finished outputs: notes reach the HTML presenter view, the
PowerPoint notes pane and the PDF annotations by three separate routes, and three
removals are three chances to miss one.

`make site` then copies the handful of files that may go out into `build/site/`, which is
what CI publishes. It is a list, not a sweep: `build/` also holds the assembled source,
the run sheet and the deck *with* notes, and publishing the directory wholesale is how
all three ended up on a public URL. `make check` fails if a speaker note is found in
`build/site/`.

Note that `slides/*.md` in this public repository still contain the notes in plain text.
Stripping them from the published site keeps them out of what a reader is handed; it does
not make them unreadable to someone who opens the repository.

## Working in this repository

Read [`CLAUDE.md`](CLAUDE.md) first. It is the brief: language policy, content rules,
the slide style guide and the module budgets. Two rules matter more than the rest.

1. **Never invent CSCS facts.** Every path, quota, command, flag, hostname and role name
   must be traceable to `docs.cscs.ch` or to material someone provided. If you cannot
   verify it, write `<!-- TODO(verify): ... -->` and say so.
2. **Everything in this repository is in English** — slides, notes, handouts, commit
   messages, file names. Contributors may work in whatever language they prefer; that
   never changes what lands in the repository.

Own a module? Rewrite the scaffolding rather than defending it. It exists to save you
the blank page, not to constrain you.

## Layout

```
slides/            one Marp file per module, plus backup slides
slides/theme/      the shared CSCS theme
handout/           the one-page A4 cheat sheet and its theme
notes/             agenda, source provenance, documentation gaps
assets/            logos, and the list of screenshots still to capture
tools/             build helpers: assemble, inline assets, slide count, run sheet
build/             generated output, git-ignored, never edited by hand
```
