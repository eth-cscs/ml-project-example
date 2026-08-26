# Open questions and provenance, lifted out of the slides

Every one of these used to sit in the slide source as an HTML comment. Marp turns **every**
comment that is not a directive into a presenter note, so a `TODO(verify)` block was
landing in the speaker-notes pane next to the lines the presenter actually has to say.
They are here instead.

Add new ones here, not in `slides/`. If something must be visible while editing a slide,
it belongs in this file with the slide title as its heading.


## `00-intro.md`


### Today is a maintenance day

TODO(verify): confirm the exact maintenance window and which services are affected
before the session — the clusters, the portal, JupyterLab and the docs may not all be
down at the same time, or at all. If only some are affected, name them here rather than
saying "systems". If the maintenance moves, this slide comes out.


## `01-project-access.md`


### Small and large are two different processes

TODO(verify): the small/large policy numbers come from the MLP policies page,
which is still a docs preview at cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/
and is being merged into docs.cscs.ch in the coming days. Swap the footer link and the
"Where to read more" entry to the final docs.cscs.ch URL before the session, and
re-check the numbers at that point. The call dates come from swiss-ai.org, not from
CSCS — re-check them the week before, they change per call.


### Your user account lives as long as one project does

TODO(verify): docs.cscs.ch/accounts/ backs only the middle of this card — "accounts
are bound to projects, and accounts will be closed with the project unless the account
is also part of another open project". The two ends do not appear there: that the email
address is the unique identity, and that a later invitation re-enables the same account
rather than creating a new one. Both come from Andrea as ML Platform service manager.
Confirm, then get them written into the docs page.


### A service account runs the work you are not there for

Sourced from Ceriani et al., "Transitioning User and Identity Management for Alps",
CUG 2026, sections 4, 4.1 and 5.2 — on-behalf-of, single-project binding, inherited
validity period, automatic deprovisioning and the accountability argument are all stated
there. The paper's scope-restriction sentence is deliberately NOT on the slide: it describes
the architecture, and whether a PI can request a narrower scope today is unsettled.
Confirmed by Andrea as ML Platform service manager on 25 August 2026, and NOT in any
document: that service accounts are off until requested; that the project team runs the
account and registers it on a shared team address; and that it authenticates with an API
key under its own username, with no MFA. These are facts, not guesses — but a reader of
docs.cscs.ch cannot find any of them, which is a documentation gap rather than an open
question. Listed in notes/docs-gaps.md.


### The portal is where the project lives

Screenshot captured 25 August 2026 from the test project grtest3. The email column is
deliberately blurred: those are real colleagues and this deck is published to a public
GitHub Pages site. To use the unblurred capture, re-crop the original without the
GaussianBlur paste — see the commit that added this file.

TODO(verify): whether, and by whom, an existing member's role can be changed after the
invitation is not documented anywhere — the portal docs cover only the invitation flow.
Andrea's expectation is that a PI and a deputy PI can both do it from the Team tab. Click
it, then either put one line on this slide or get it into the docs page.

TODO(verify): the tab names are read straight off the capture, which is why the old
"Invitations" and "Usage" bullets are gone — neither is a tab. What is NOT verified is
what "Project dashboard" and "Audit logs" contain; the descriptions above are inferred
from their names and from where the consumption panels most likely live. Click both and
correct the two bullets.


### You can use a model without training one

TODO(verify): model names and pricing move. Re-check the model list and the
"Available models and pricing" section the week before the session, and confirm the
Apertus tag swiss-ai/Apertus-70B-Instruct-2509 is still current if you quote it.


### Check the consumption regularly

TODO(verify): the consumption view is not documented on
docs.cscs.ch/accounts/waldur/ at all, and these two panels shipped on 24 August 2026, so
nothing describes them yet. Both the panels and the visibility rule come from Andrea as
ML Platform service manager. Get them into the docs page — see notes/docs-gaps.md.


### Spend it linearly, or you lose it

The <div> wrapper is load-bearing: CommonMark only treats a whitelisted set of tag
     names as HTML blocks, and <svg> is not one of them, so an unwrapped diagram is
     parsed as inline HTML and its text nodes are flattened into a paragraph. Keep the
     whole block free of blank lines, which would close the HTML block early.


### Spend it linearly, or you lose it

── row 1: the monthly rule ─────────────────────────────────────────


### Spend it linearly, or you lose it

your usage


### Spend it linearly, or you lose it

the credit burned by falling short


### Spend it linearly, or you lose it

thresholds


### Spend it linearly, or you lose it

the grace between the two


### Spend it linearly, or you lose it

what each case means


### Spend it linearly, or you lose it

── row 2: the project timeline ─────────────────────────────────────


### Spend it linearly, or you lose it

TODO(verify): every number on this slide — the 15-50% grace, the two-month cap on
the low partition, the 90-day retrieval window — comes from the MLP policies page,
which is still a docs preview at cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/.
Re-check them once it is merged into docs.cscs.ch.
The slide now PRINTS the URL docs.cscs.ch/platforms/mlp/policies/, which does not resolve
yet. Load it in a browser before the session. If it is still not live on 26 August, fall
back to docs.cscs.ch/platforms/mlp/ here and on the "Where to read more" slide — a URL
that 404s on a projector costs more credibility than a less precise one.

Also: the policies page says only that a project "remains accessible for a grace period
of 90 days for data retrieval". That the end date stops COMPUTE while the project itself
stays active comes from Andrea, not from the page. It is the distinction the timeline now
makes, so it is worth getting written down — see notes/docs-gaps.md.


## `02-data-storage.md`


### Six mount points, and they are not interchangeable

Verified against cscs-docs-preview.svc.cscs.ch/442, both /storage/filesystems/ and
/platforms/mlp/, quoting them directly:
  home     "There is no cleanup policy on Home"; 50 GB and 500,000 inodes; daily
           snapshots of the last seven days in $HOME/.snapshot; tape backups "currently
           being implemented"; retained three months after your last project finishes.
  iopsstor "Files ... that have not been accessed in 14 days are automatically deleted."
  capstor  "Files ... that have not been accessed in 30 days are automatically deleted."
           150 TB, 1 million inodes, soft quota with a two-week grace period.
           "There are no backups on Scratch."
  store    "There is no cleanup policy on Store"; "the three most recent copies of every
           file backed up to tape every 24 hours"; quota from the initial resource
           request; retained three months after the project ends.
  ritom    the preview says the cleanup policy "is being finalised". Per Andrea it is
           30 days, the same as capstor. The slide states 30 days; the documentation
           does not, so it must be said out loud.
Note the criterion is LAST ACCESS, not age or modification time.

TODO(verify): THIS SLIDE'S FOOTER DOES NOT YET BACK IT. docs.cscs.ch/storage/filesystems/
is live but lists only Home, the two Lustre scratches and Store — no ritom, no datacache.
Both exist solely in the /442 preview. Until that merges, anyone who follows the citation
finds a page that does not mention two of the six rows. Re-check on the morning of the
session; if the merge has not happened, say so out loud rather than letting somebody
discover it afterwards. (Ritom itself IS live-documented, but on
docs.cscs.ch/guides/storage/, not on the filesystems page.)

TODO(verify): two things the preview does not settle.
 1. The iopsstor scratch quota is not stated anywhere. Find it, or leave it off.
 2. The preview labels ritom "(Clariden only)" and says "On Clariden, the cleanup policy
    ... is being finalised". Andrea says it is NOT mounted only on Clariden, so the slide
    drops that qualifier. This is a documentation error, not a gap — fix the page.


### NVMe for training data, HDD for writing checkpoints

TODO(verify): ritom's "Cleaned after 30 days" is Andrea's, not the documentation's —
the storage preview still says the policy "is being finalised". It is on the slide because
the other two cards state theirs, and a silent third card claims something worse than a
wrong number: that ritom is never cleaned. Confirm and get it written into the page.


### `datacache` is fast, shared, and does not disappear

TODO(verify): THIS SLIDE'S FOOTER DOES NOT YET BACK IT. The live
docs.cscs.ch/platforms/mlp/ does not mention datacache at all.
datacache is documented only on the preview at
cscs-docs-preview.svc.cscs.ch/442/platforms/mlp/ and goes live on 26 August after the
maintenance. Confirm on the morning of the session that it is actually available — if
the maintenance slips, this slide says "from today" and would be wrong on stage.
Re-point the DOCS line once the page is merged.


### Globus from outside, `xfer` inside, S3 from either side

TODO(verify): the transfer guidance and the rclone flags come from the preview
cscs-docs-preview.svc.cscs.ch/442/storage/transfer/. Re-check once merged. The job script is the
documented one with its `command=` indirection inlined into the `srun` — same job, three
lines shorter. The flags are verbatim except `--progress`, dropped from both: it prints a live
counter, which is worth nothing in a batch job whose output goes to a log file.

The S3 line, added at Fawzi's request on 25 August 2026: docs.cscs.ch/storage/object/ does
document the service — "CSCS offers a public cloud object storage service, based on the
Ceph Object Gateway. The service can be accessed from S3-compatible clients", endpoint
https://rgw.cscs.ch, path-style URLs. TODO(verify): two things it does NOT say. That you
reach it with rclone from the xfer queue is Fawzi's, not the page's — docs.cscs.ch/storage/
transfer/ covers only Globus and xfer between filesystems. And the object page opens with
"This page is currently incomplete and it is being updated following recent developments",
so re-read it before the session in case the endpoint or the access story has moved.


## `03-ml-use-case.md`


### Use a model before you train one

TODO(verify): the inference API is documented; using it for data vetting and
training-set preparation is our suggestion, not something docs.cscs.ch recommends.
Keep it framed as a suggestion.


### A uenv is three commands

Verified against docs.cscs.ch/software/uenv/ and /software/uenv/using/: images are
always referenced as name/version:tag, `uenv image find` is shown with an argument,
`uenv run` takes `--` before the command. The versions and their clusters come from the
Versioning table on docs.cscs.ch/software/ml/pytorch/.


### Where to get images

TODO(verify): the PR dropped com.hooks.aws_ofi_nccl.variant = "cuda12" from the
annotations block, keeping only .enabled. Ask Alberto whether the variant is no longer
needed or whether this was a simplification — if it is still required, the slide is
missing a line that decides whether multi-node training is fast.

TODO(verify): the exact import command (enroot / podman / the CSCS-recommended
route) was not captured and is NOT stated on the container-engine overview page. Module 3
owner: find it, quote it verbatim, and put it on this slide. Without a real command this
slide is advice, not instruction.


### Serving your own model

PLACEHOLDER. Andrea and Fawzi have not settled whether serving a model you trained
yourself goes through the inference service or through a Slurm job on the cluster.
Do not improvise this on stage: if it is still open on the day, say it is coming and
point at the tutorials.
- Next: Post-training.


### After the first training run

PLACEHOLDER. Nothing written yet. Fine-tuning, RLHF and evaluation would live here.
The ML tutorials cover fine-tuning already, so the cheapest version of this slide is a
pointer at docs.cscs.ch/tutorials/ml/.
- Next: One last thing, and it is not on Alps.


### Swiss AI has its own Kubernetes cluster

TODO(verify): this is Andrea's, not the documentation's. Nothing on docs.cscs.ch
describes a Swiss AI Kubernetes cluster. Confirm Imanol's full name and the right way
to reach him before the session — "managed by Imanol" is not something a stranger in
the audience can act on.


## `04-wrapup.md`


### Three places to get help, in order

TODO(verify): confirm the User Day date, venue and registration link, and add the
link here. Also confirm whether the ML Platform drop-in sessions are still running and
on what cadence before promising them from the stage.


## `05-backup.md`


### Backup slides




### Four things it does well

PLACEHOLDER: the CUG deck has approved screenshots of all four views. Whoever
presents this should pull two of them in — the dashboard and the job detail with the
shareable URL — rather than showing this as a bullet list.


### Still to write

PLACEHOLDER. These four were listed in CLAUDE.md as backup topics but have no slides yet.
If the discussion asks for one and there is nothing to show, say so plainly and offer to
follow up by email or at the User Day on Friday. Do not improvise a technical answer at
the whiteboard in front of this audience.

