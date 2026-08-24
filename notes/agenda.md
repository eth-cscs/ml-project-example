# Agenda — Alps technical training

**Swiss AI Initiative Annual Meeting 2026 · Wednesday 26 August 2026, Bern**
Slot: 90 minutes, around 13:30 (may shift slightly).
Structure: ~60 min presentation + ~30 min open discussion.

**The slot is 90 minutes.** The presentation aims for about 60 and the discussion takes
whatever is left. Sixty is a target, not a rule.

**We invite the audience to interrupt**, which makes overrunning the normal case rather
than the failure case. So the estimates — roughly a minute a slide — are the
*uninterrupted* time, and the real clock will be behind them. Absorb it with the
pre-agreed cut for your module rather than by talking faster: a rushed slide teaches
nobody anything, and the question that caused the delay was worth more than it was.

`make check` prints the minutes that would be left for discussion. Keep it above 20.

## Running story

One Swiss AI project, from "we need compute" to a model that is trained and being used.

The invented personas that used to carry this — a PI and a PhD student — were dropped on
24 August. They did two jobs and neither is theirs any more: the audience marker in the
corner of every slide says who a slide is for, and module 3 is a real worked example,
which is a far stronger thread than two people who do not exist. With several presenters,
characters also have to be maintained by everyone or they read as inconsistent.

Every module should still be able to say where we are in the story. Just say it in the
second person.

## Modules

| # | Module | Budget | Owner | Slides | Drafted | Status |
|---|---|---|---|---|---|---|
| 0 | Welcome — Alps, the ML Platform, what this hour covers | 5 min | TBD | `slides/00-intro.md` | 6 | scaffold |
| 1 | **Project lifecycle and access** — request, portal, invites, what a project comes with, inference, budget, first login | **14 min** | **Andrea** | `slides/01-project-access.md` | 14 | **on budget** |
| 2 | Data and storage — mount points, the three scratches, project store, `datacache`, inodes, moving data in | 13 min | TBD | `slides/02-data-storage.md` | 8 | scaffold |
| 3 | **A concrete ML use case** — one worked example, raw data to a trained model | **30 min** | Fawzi + owners per subsection | `slides/03-ml-use-case.md` | 19 | restructured, two placeholders |
| 4 | Wrap-up — support, User Day (28 Aug), what we did not cover | 3 min | TBD | `slides/04-wrapup.md` | 4 | scaffold |
| — | Open discussion | 25 min | all | — | — | — |
| — | Backup, shown on request only | — | — | `slides/05-backup.md` | 7 | HPC Console block done |

**65 minutes budgeted, 25 left for discussion.** Storage stays a module of its own before
the worked example; inside the example, importing data is a fifteen-second recap that
points back at it rather than repeating it.

### Module 3's subsections

Reviewed with Fawzi on 24 August. The old modules 2, 3 and 4 — storage, software and
containers, running jobs — are now one section built as a single worked example. The
subsections are marked with a kicker above the slide title rather than with divider
slides, which would have cost eight minutes of the thirty-eight.

| Subsection | State |
|---|---|
| Import your data | one recap slide — the content is module 2 |
| Prepare it with inference | **new** — vetting, building the training set, coding agents |
| Set up your workflow | FirecREST and JupyterLab |
| Watch it from a browser | the HPC Console |
| Train your own model | nine slides, from the old software and running modules |
| Serving at scale | **placeholder** — inference service or Slurm job is still undecided |
| Post-training | **placeholder** — nothing written |
| Kubernetes | **new** — a dedicated Swiss AI cluster, access through Imanol |

### What "scaffold" means

Modules 0 and 2 to 5 were drafted from `docs.cscs.ch` so that no owner starts from a
blank page. Every factual claim is sourced and every unsourced one carries a
`TODO(verify)`. They are **not finished modules**: the voice is generic, several slides
are marked `PLACEHOLDER`, and each one is missing the thing only its owner can supply —
a real command, a real screenshot, a real number from a real run. Owners should rewrite
freely rather than treat this as a draft to defend.

## Hand-offs between modules

- **1 → 2**: you have a shell on Clariden and an empty home directory. The first
  question is where two terabytes of training data go.
- **2 → 3**: the data is on the right filesystem — including the new `datacache`, which
  goes live the morning of the session. Now it needs an environment that can read it.
- **3 → 4**: the environment exists. Now it has to run at scale, repeatedly.
- **4 → 5**: the model trains. Where do you go when it breaks?

## Backup slides (after the wrap-up)

In `slides/05-backup.md`. Mentioned on the wrap-up slide, shown only if the discussion
asks for them:

- **HPC Console** — drafted, 5 slides, about 5 minutes. Ready.
- Kubernetes — not written
- Post-training and RLHF workflows — not written
- Advanced multi-node scaling — not written
- GPU-efficiency deep dive — not written

### Open decision: where the HPC Console block lives

It is drafted as backup so the placement decision stays open. Three options, and moving
between them costs nothing — cut the block and paste it:

1. **Backup** (where it is now). Zero budget impact. Shown only on request.
2. **Inside module 4**, whose owner would give up about 5 of their 12 minutes. Zero
   impact on the 60-minute total.
3. **A section of its own**, taking 5 minutes from the 30-minute discussion: 65 + 25.
   This changes the shape of the session and needs the agreement of all the presenters,
   not just one module owner.

Andrea's view is that the content is worth showing to this audience — many are
comfortable with PyTorch and not with Slurm, and a browser lowers that barrier — but
that option 3 is not one person's call to make.

## Storage: one thing lands the morning of the session

`datacache` — `/iopsstor/datacache/cscs/swissai/<project>` — goes live on **26 August**,
after the maintenance. Module 2 has a slide on it, marked as new, and module 0's
maintenance slide points forward to it so the outage has an upside.

Confirm on the morning that it is actually available. If the maintenance slips, the
module 2 slide says "from today" and would be wrong on stage.

## A trap in the handout

Marp **clips** whatever does not fit the A4 page rather than paginating it. The PDF
stays one page and the overflow is silently gone. This has already happened once: the
tunnel command and the sources line disappeared for several commits without anyone
noticing, because nothing failed and the page count never changed.

`make check` cannot catch it. After editing `handout/quickstart.md`, look at the bottom
of `build/quickstart.pdf` and confirm the last section is whole.

## Before the session: two documentation merges

This is the deck's biggest external dependency, and it is not in our hands.

| Preview | Covers | Slides that depend on it |
|---|---|---|
| `/463/platforms/mlp/policies/` | small vs large, expected/minimal consumption, the 15–50% grace, the `low` cap, the 90-day grace | module 1, slides 2 and 7 |
| `/442` storage and MLP pages | `datacache`, the Ritom scratch, cleanup and backup policies, the transfer figures | module 2, most of it |

Two different failure modes, and the second is the nastier one:

- `docs.cscs.ch/platforms/mlp/policies/` currently **404s**. The slide that used to print
  it now prints the parent page instead. Upgrade it once the merge lands.
- The storage URLs **already resolve** — but the live pages do not yet mention
  `datacache` or Ritom. So a slide can cite a working link whose content does not back
  what was just said. That is worse than a dead link, because it looks like we are wrong.

  Checked on 24 August, the live pages say:

  | Page | Has `ritom`? | Has `datacache`? |
  |---|---|---|
  | `docs.cscs.ch/platforms/mlp/` | no | no |
  | `docs.cscs.ch/storage/filesystems/` | no | no |
  | `docs.cscs.ch/guides/storage/` | **yes** — a "VAST tuning on Ritom" section | no |

  So exactly **two** slides carry a citation that does not yet support them: the
  six-mount-point table and the `datacache` slide. Both are marked in the source. Ritom
  itself is fine as long as the scratch slide cites the storage guide, which it now does.

Check both the morning of the session. If the storage merge has not happened, say so on
the slide rather than letting somebody discover it afterwards.

## Closing

End by pointing the audience at the **CSCS User Day, Friday 28 August 2026** — two
days later. Reuse and cross-reference User Day material rather than duplicating it.

## Module 1 detail

Twelve slides — a divider plus **eleven** content slides — so about 12 minutes against
a 12-minute budget. On time, but one slide over the "max 10 content slides" ceiling in
CLAUDE.md §6. The extra slide is "Spend it linearly, or you lose it": the expected /
minimal consumption rule with its 15–50% grace, the low partition, and the 90-day
retrieval window, drawn as a single timeline. It earns its place because it is the only
slide in the module that changes what a PI does on Monday morning. If the module has to
shrink, the cut order is: the "deliberately skipped" slide first (it can become a
sentence over the hand-off), then merge the portal tour into the invitations slide.

**The module is split by audience, and says so.** The divider announces it, and every
content slide carries a marker top-right: *PIs and deputies* for getting a project, the
portal, invitations and the budget; *Everyone* for the account lifecycle, MFA, keys and
the jump host. The order already groups them — administration first, then access — so
nobody has to track two threads at once. Worth copying in modules 2 to 5: the same
audience split runs through the whole session.

Speaker notes on every slide. Outstanding before the session:

- One screenshot, plus three optional ones — see `assets/screenshots/TODO.md`.
- Five `TODO(verify)` markers in `slides/01-project-access.md`: the portal consumption
  view, changing an existing member's role, the account identity and re-enabling, the
  MLP small/large numbers, and every number on the linear-consumption slide. Two of the
  five close on their own when the policies page is merged; the other three need somebody
  to write a paragraph on `docs.cscs.ch`. All of them are in `notes/docs-gaps.md`.
- The Swiss AI call dates on slide 2 are time-sensitive. Re-check them the week before.

Module 1 also carries the small/large project explanation, which arguably belongs in
module 0. If module 0's owner would rather cover it, module 1 drops slide 3 and gains
a minute of slack.
