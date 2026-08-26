# Screenshots and recordings to capture

Claude cannot produce these. Each entry says exactly which view to capture. Save the
file under `assets/screenshots/` with the filename given, then replace the
`<div class="shot">` placeholder in the slide with a normal Markdown image.

Capture at 2x on a 16:9 window so the image still reads on a projector.

## Nothing is outstanding

There is no `<div class="shot">` placeholder left in the deck. The two module 1 captures
were taken on 25 August, and the JupyterLab spawner placeholder came off the slide on
26 August rather than being filled. Everything below is history and advice for the next
edition, not a list of work to do.

## Both module 1 captures are done

Neither used a purpose-built demo project, so read the note under each one before
recapturing. The advice below still stands for modules 2 to 4.

### Real people are in the Team capture

`portal-team-tab.png` comes from the test project `grtest3`, whose members are real CSCS
colleagues with real addresses. **The email column is blurred**, because this deck is
published to a public GitHub Pages site and their addresses would be scrapeable from it.
Names, usernames and roles are left readable — the slide is about the roles column.

If you recapture, either blur the same column or build the demo project below, which
avoids the question entirely.

## Set up a demo project first

Everything below is easier, and better, if there is a **dedicated demo project** in the
portal rather than a real one:

- No anonymisation. Nothing to blur, nothing to leak, no chance of a real colleague's
  address appearing on a projector in Bern.
- Invent the members. Two accounts are enough: one project administrator and one project
  member, so the roles column has something to show.
- It stays available afterwards, for the drop-in sessions and for the next edition.

One thing a demo project **cannot** give you: a consumption history. See capture 2.

## Module 1 — `slides/01-project-access.md`

| # | Filename | Source | View to capture |
|---|---|---|---|
| 1 | ~~`portal-team-tab.png`~~ | — | **Done.** Captured 25 August 2026 from the test project `grtest3`. Email column blurred — see below. |
| 2 | ~~`portal-consumption.png`~~ | — | **Done.** Captured 25 August 2026, on the slide. See below for what changed. |
| 3 | `portal-invite-dialog.png` | demo project | The **Invite Users** dialog with the role dropdown open, so the three role names are readable. Optional — use it if slide "Adding someone takes one email address" feels too abstract on the day. |
| 4 | ~~`user-account-sign-key.png`~~ | — | **No longer needed.** Key signing came off the slides on 25 August; it is handout-only now. |

### Capture 2 — done, and the portal changed under it

Captured 25 August 2026 from a real project, the day after two new panels went live. No
names or project ID are visible, so nothing needed blurring.

Two files are in `assets/screenshots/`:

- `portal-consumption.png` — the crop on the slide: **This month's credit consumption**
  and **Overall credit**.
- `portal-consumption-full.png` — the same capture with the third panel, **What happens
  next**, still on it. Not on any slide. It is kept because it is the only evidence we
  have in the repo for the grace period, the credit expiry and the deletion rule, which
  the next slide states as fact and the documentation does not cover.

The old plan was an annotated capture sharing its vocabulary with the timeline diagram on
"Spend it linearly, or you lose it". The new panels made that unnecessary: they already
say **minimum draw**, **expected** and **allocated** on screen. The one word that still
differs is the diagram's `minimal` against the portal's `minimum draw` — if you annotate
anything, annotate that.

If the capture needs retaking, use **a real project partway through its period**: an empty
chart argues the opposite of what the slide says.

## On showing it live

The style guide says avoid live demos, and that still holds **for the 12-minute slot**:

- Logging in on stage costs 30 to 60 seconds of dead air, minimum, and that is when it works.
- The invite flow sends a real email, so it needs a throwaway address prepared anyway.
- The module is already at 12 minutes against a 12-minute budget. A live demo adds two
  to three minutes and there is nothing left to take them from.

The good compromise, if the still images feel flat:

- **Record** the two flows from the demo project as short GIFs or asciinema clips —
  the invite, and navigating to the accounting view. Marp embeds them like any image,
  they always work, and they can be paused.
- Keep the portal **open in a second browser tab** as a fallback for the 30-minute
  discussion at the end. That is where a live click costs nothing if the wifi dies, and
  where somebody will almost certainly ask "can you show me where that is?".

## Modules 2–5

Not yet started. Owners: add your entries here when you draft your module. If the demo
project exists, reuse it rather than screenshotting production.
