# Source material

Everything the slides rest on that is **not** a live `docs.cscs.ch` page: documentation
previews, material from other repositories, and things that are true but written down
nowhere. Keep this file honest — if a claim in the slides comes from here rather than
from the public documentation, it must say so at the point of use, as a `TODO(verify)`.

## Storage documentation preview — `/442`

<https://cscs-docs-preview.svc.cscs.ch/442> — the storage and ML Platform pages as they
will be after the next merge. Module 2 is written from this, not from the live pages,
because the live ones are missing two mount points.

What is only here, and not yet on `docs.cscs.ch`:

- **`datacache`** — `/iopsstor/datacache/cscs/swissai/<project>`. A project-level working
  area on fast Iopsstor. "Like scratch, it is fast NVMe storage and is **not backed up**.
  Unlike scratch, it has **no cleanup policy**: files are never deleted automatically, and
  the project owns its data lifecycle and space hygiene within a project quota on capacity
  and inodes." Not provisioned by default: the PI opens a Service Desk ticket with the use
  case and the space and inodes required, and CSCS reviews it before creating the area.
  **Goes live on 26 August 2026, after the maintenance** — the day of the session. That
  timing is Andrea's, not the page's.
- **Ritom scratch** — "On Clariden, a further scratch path is available on Ritom (a VAST
  file system) at `/ritom/scratch/cscs/$USER`." The page says its cleanup policy "is being
  finalised". Andrea says it is **30 days**, the same as capstor, and the slide now states
  that: with the other two cards naming their cleanup, a card that stayed silent read as
  though ritom had none, which is the one wrong conclusion to leave an audience with. The
  number is his, not the page's — carry it into the docs when the preview merges.
- The scratch usage recommendations, and the instruction to move results to the project
  store after a job "for example with `rclone` on the `xfer` queue".

Re-point every module 2 link once this is merged, and re-check the numbers at that point.

### Full scan of the storage section, for whoever owns module 2

Four pages under `/storage/`, plus one guide outside it. Verified quotations:

- **`/storage/filesystems/`** — Home: "There is no cleanup policy on Home", 50 GB and
  500,000 inodes, "Daily snapshots for the last seven days ... in `$HOME/.snapshot`",
  and "Backups to tape storage are currently **being implemented** for Home directories"
  — so do not promise them. Capstor scratch: 150 TB, 1 million inodes, "a soft quota
  grace period of two weeks", files "not accessed in 30 days" deleted. Iopsstor scratch:
  files "not accessed in 14 days" deleted; **its quota is not stated anywhere**. Store:
  no cleanup, "the three most recent copies of every file backed up to tape every 24
  hours", retained three months after the project ends. The deletion criterion is **last
  access**, not age or modification.
- **`/storage/transfer/`** — Globus mount points are listed as `/iopsstor/scratch/cscs`,
  `/capstor/scratch/cscs`, **`/ritom/scratch/cscs`**, `/capstor/store/cscs` and
  `/vast/users/cscs`. Note ritom appears here with no Clariden qualifier, which supports
  Andrea's correction. Concrete figure: "copying a 1 TB directory from `/capstor/store`
  to `/iopsstor/scratch` ... takes on the order of 5 minutes on Alps (roughly 3 GB/s)".
  `xfer` jobs chain with `--dependency=afterok:$SLURM_JOB_ID`.
- **`/guides/storage/` is already live** and is the only public page that documents
  Ritom: "Ritom is a scratch space using the VAST Data filesystem accessed over NFS",
  with a "VAST tuning on Ritom" section covering file locking, collective buffering,
  data sieving and aggregation nodes. Ritom does **not** appear on the live
  `/platforms/mlp/` or `/storage/filesystems/` pages, which is why the scratch slide
  cites the guide rather than the platform page.
- **`/guides/storage/`** — the page module 2 most needs and the one easiest to miss,
  because it sits outside the storage section. Lustre striping
  (`lfs setstripe --stripe-count 32 --stripe-size 4M`, 4 MB block size "gives good
  throughput"), VAST/ROMIO tuning for Ritom, and "Lustre is not well suited to handling
  many small files" — demonstrated with a PyTorch virtual environment of **22,806
  inodes**, with the recommendation to squash it into a squashfs image. That example is
  now on the module 2 inodes slide and hands off to module 3.
- **`/storage/longterm/`** — **do not use this page.** Per Andrea, the Long Term Storage
  service has been **decommissioned entirely** and `lts.cscs.ch` no longer exists; a
  request to it does not reach a portal. The documentation page is nevertheless still
  live and still describes the service in the present tense, complete with a 10-year
  retention promise, a "2 TB ... free of charge per project" allocation and a price of
  "CHF 600.- for each terabyte". Nothing from it is used in this deck, and the link was
  removed from module 2's closing slide. See `notes/docs-gaps.md` — this is the most
  urgent item there.
- **`/storage/object/`** — also not on a slide. Ceph Object Gateway, S3-compatible, at
  `https://rgw.cscs.ch`. Works with the AWS CLI, s3cmd and Cyberduck; quota via the
  `/_quota` endpoint.

## Audit of 24 August 2026 — what was checked, and what was wrong

Triggered by a real error: the container module claimed the EDF `image` key was a local
squashfs on scratch rather than a registry reference, which is the opposite of what
`docs.cscs.ch/software/container-engine/` says. That was caught by Alberto Madonna's
pull request, not by us, so the rest of the deck was audited claim by claim.

**Wrong, now fixed:**

- **Kubernetes.** Both the wrap-up and module 1 offered it as a topic. The documentation
  says "Kubernetes is only available for specific partners" and "Kubernetes is not
  available for normal users on Alps". Removed from the slides; the honest answer lives
  in the speaker notes in case someone asks. It came from `CLAUDE.md`, not from the
  documentation — a reminder that the brief is not a source.
- **uenv commands.** `uenv image find` was shown with no argument and images were named
  without a version (`prgenv-gnu` rather than `prgenv-gnu/25.6:v2`). Neither form appears
  in the documentation. Now uses the PyTorch uenv, which is documented exactly.
- **PyTorch uenv versions.** v2.6.0 was listed as available on Santis. The Versioning
  table gives it for Clariden and Daint only.
- **JupyterLab accounting.** "It is a Slurm job. It is charged like one" is not stated
  anywhere. Softened, and recorded as a `TODO(verify)`.

**Checked and correct** — quoted verbatim where they appear: the Slurm partitions table,
`--ntasks-per-node=4` with `--gpus-per-task=1`, `--exclusive --mem=450G`, the JupyterLab
URL and its disk-quota error message, the Alps and platform descriptions, the Clariden
and Bristen roles, and all of module 2's storage figures.

**Sourced, but not from docs.cscs.ch** — legitimate, and labelled at the point of use:

- `service-desk@cscs.ch` comes from the ML Platform drop-in deck. There is no contact or
  support page on `docs.cscs.ch` — both `/contact/` and `/support/` return 404 — so this
  address cannot be verified from the documentation at all. Worth a page.
- The HPC Console behaviour comes from the CUG 2026 deck.
- Everything in the section below comes from Andrea.

## Not documented anywhere yet — Andrea, as ML Platform service manager

These are load-bearing claims in module 1 that no public page currently backs. They are
correct, but they are marked `TODO(verify)` in the slide source because a reviewer
cannot check them.

**See `notes/docs-gaps.md`** — the same list written up as a ready-to-paste issue for
the documentation repository. Add to it as modules 2 to 5 are written.

- **Who sees consumption in the portal.** Not a PI-only view. *Every* project member
  sees the project-level total. Per-user usage is visible inside the detail of each
  individual resource. There is **no** per-user total across the whole project.
- **The per-role permission matrix** is not written down. The portal documents the three
  role names and that administrators and managers can invite users and assign roles;
  everything beyond that is folklore.
- **Account identity and re-enabling.** The docs say an account is bound to projects and
  closes with the project "unless the account is also part of another open project".
  They do not say that the **email address is the unique identity** (one address, one
  account), nor that a **later invitation re-enables the same account** instead of
  creating a new one. Both are true and both are worth documenting — they are the
  difference between "my account was deleted" and "my account is dormant".
- **There is no project-level cap on inference spending — today.** The documentation
  describes the optional per-key token budget but never says what happens without one.
  Per Andrea: nothing. A single API key with no budget can consume the whole project
  credit. The slide therefore words it as an instruction — "set a token budget on every
  key, today it is the only limit there is" — rather than as an announcement that the
  guardrail is missing, and the speaker notes leave the presenter to judge how explicit
  to be. Expected to change: **re-check before the session**, and if a project-level
  limit has landed by then, the bullet should say so instead.
- **"We are actively improving these views"** on the consumption slide is a
  forward-looking statement, not a documented fact: better usage visualisation for
  compute, for storage, and for the new inference resources. It is Andrea's to make
  from the stage as service manager. Re-read it in the week before 26 August 2026 —
  roadmaps move, and a promise made to this particular room will be remembered.
- **Changing an existing member's role** is not documented at all —
  `docs.cscs.ch/accounts/waldur/` has exactly four sections (the tool, log in, select
  the organisation, invite users) and stops at the invitation. The expectation is that
  a PI and a deputy PI can both change a role from the Team tab, but nobody has written
  it down, so module 1 deliberately claims nothing either way. Click it, then fix the
  docs page.

## ML Platform project policies — still a docs preview

<https://cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/>

**This is the authority for the small/large slide in module 1** and for a good part of
module 2. It is being merged into `docs.cscs.ch` in the coming days, so every reference
to it is currently marked `TODO(verify)` in the slide source. Swap the links and
re-check the numbers once it lands.

What it says, for the record:

- **Small**: typical budget up to 32,000 GPUh, 6 months, rolling start ("as soon as
  they are accepted", default the first day of the following month, delayable by up to
  3 months on request), storage default 1 TB and 1,000,000 inodes.
- **Large**: typical budget from ~500,000 GPUh, 12 months, starts at the scheduled time
  of the call, normally 1 July or 1 January, storage must be stated in the proposal
  with no default applied.
- A large proposal can be **reduced to a small grant** rather than rejected.
- Credit is fixed for the whole duration, with monthly expected consumption targets.
  Exhausted projects can fall back to the low-priority partition.
- **90-day grace period** for data retrieval after the project ends — module 2 material.
- Section headings: project types · core project data · compute budget · storage budget ·
  other resources · start · duration · users and job priority · appendix on computing
  compute consumption.

## Swiss AI Initiative compute grants

<https://www.swiss-ai.org/compute-grants> — the application side, not CSCS.

- Large projects (>500k GPU hours): **4th call open 3 August to 14 September 2026**,
  twice a year. Contact `large-grants@swiss-ai.org`.
- Small projects (≤32k GPU hours): rolling reviews. Contact `small-grants@swiss-ai.org`.
- Roughly 10–20 million GPU hours to be distributed in 2026. Open to researchers in
  Europe and beyond.

The call dates are time-sensitive and live on swiss-ai.org, not on docs.cscs.ch —
**re-check them the week before the session**. Detailed submission instructions sit in
linked Google Drive documents that were not read.


## ML Platform drop-in repository

`~/Development/GitHub/ml-platform-drop-in` — Andrea's bi-weekly drop-in sessions.
Public at `github.com/candrea85/ml-platform-drop-in`.

**Reused here:**

- **Branding.** Palette (`#D61F26` red, `#1A1A1A` dark, `#F7F7F8` light), Inter,
  the header/footer band, and the card / accent-bar / URL-box vocabulary were ported
  into `slides/theme/cscs.css`.
- **Logos.** `assets/logos/cscs.png` and `assets/logos/eth.png` were extracted from the
  base64 blobs in `2026-04-08-ssh-service/presentation/slides.html`.
  `TODO(brand)`: confirm these are the current approved assets.

**Good for module 1, not yet used:**

- Service accounts turned out to be documented after all, on
  `docs.cscs.ch/accounts/account-create/`: scoped to a single project, grant access to
  all its resources, and the **project PI** requests one from a Platform Manager via a
  Service Desk ticket. Module 1 cites the docs for this, not the drop-in material.
  That same page describes exactly two account types — regular user and service
  account — and has no notion of "non-Swiss-AI account types", which is why that line
  was dropped from the out-of-scope slide.
- `2026-04-08-ssh-service/README.md` is the deep reference on the new SSH service:
  user-account vs service-account flows, the `hpc-ssh` / `api-ssh-service` endpoints,
  `1min` vs `1d` durations, IP-restricted and force-command keys, and how a PI gets a
  service account (support ticket, then the PI or deputy creates it in the portal).
  Too much detail for a 12-minute module — this is Q&A and backup-slide material.
- It also records that legacy `sshservice.cscs.ch` / `sshservice-cli` were retired in
  **May 2026**, which is why module 1 mentions them only in the "skipped" slide.

## CUG 2026 — "A Lightweight Web-UI for HPC and AI"

`~/Downloads/various/CUG26/CUG-26-a-lightweight-web-ui-for-hpc-and-ai.pptx`
(Pagnamenta, Ceriani, Palme, Dorsch — 29 April 2026, 20 slides with speaker notes.)

**This is module 4 material, not module 1.** It covers the HPC Console
(open-source as `firecrest-ui`) built on FirecREST: cluster-health dashboard, job
listing and filtering, job submission from the browser, log inspection with shareable
per-job URLs, Grafana integration, and the filesystem browser with large-file upload.
Whoever owns module 4 should mine it — the screenshots and the workflow framing are
already done and already approved for an external audience.

## CUG 2026 — "Transitioning User and Identity Management for Alps"

`~/Desktop/All/CUG2026/CUG-26-transitioning-user-and-identity-management-for-alps-30-04-2026.pptx`
(Ceriani et al. — 30 April 2026, 16 slides with speaker notes.)

**Background, not slide content.** Too internal for this audience, but it gives the
one sentence that explains the whole portal story if somebody asks in the discussion:

> Waldur (`portal.cscs.ch`) is where project and resource **workflows start**; the
> Identity Management Platform (IMP) **owns identity state and lifecycle**. The legacy
> User Management Portal (UMP) did both for over ten years and was migrated gradually,
> without a cut-over.

Also useful as scale context: roughly 14k managed users, 3–4k active, ~4k projects,
growth driven largely by AI workloads.

## The `low` partition cap

Andrea, 26 August 2026: the `low` partition is capped at the equivalent of **one month** of
the project budget, not two. The slide, its speaker note and the handout said two until
that morning. No CSCS page states the figure either way — see notes/docs-gaps.md.

## The consumption panels — `portal.cscs.ch`, 24 August 2026

Two panels went live on 24 August 2026, two days before the session:

- **This month's credit consumption** — drawn so far, projected month-end, last month
  drew, each against expected; and a pacing bar carrying **minimum draw** and an ideal
  for today.
- **Overall credit** — remaining against allocated, average daily draw, and an allocation
  bar split into **used**, **lost** and **remaining**.

Source: `assets/screenshots/portal-consumption-full.png`, captured by Andrea on 25 August
2026. Nothing about these panels is on docs.cscs.ch yet — see notes/docs-gaps.md.

The third panel in that capture, **What happens next**, is not on a slide but is the only
written evidence in this repo for what "Spend it linearly, or you lose it" claims. It
states, in the portal's own words: credit expiry sets whatever is left to zero and
forfeits it, and "the final month also waives the grace coefficient, so the minimum draw
is the full expected consumption"; at the project end date "resources are paused for the
grace period"; and when the grace period ends "every remaining resource is terminated. A
project left with no active resources is deleted." In the captured project the end date
and the end of grace are three months apart, consistent with the 90 days the slide says.

## Service accounts — the CUG 2026 IAM paper

Andrea Ceriani, Francesco Pagnamenta, Davide Mazzoleni, Narendra Challa, Marco Consoli,
Elia Palme, Maxime Martinasso, Stefano Schuppli, Viktor Mirieiev, Sergei Zaiaev and Ilja
Livenson. *Transitioning User and Identity Management for Alps.* Cray User Group (CUG
2026), Nice, 26–30 April 2026. <https://doi.org/10.1145/3837730.3837747> — CC BY 4.0.

Published, peer-reviewed and co-authored by Andrea, so it is a citable source for claims
the documentation does not yet carry. Used for the service-account slide:

- §4 — three identity categories: **user accounts** (long-lived human identities that may
  participate in multiple projects over time), **service accounts** (non-interactive
  workflows performed on behalf of a user, "automated pipelines that execute actions a
  user would otherwise perform manually") and **temporary accounts** (courses, webinars,
  short-lived collaborations).
- §4.1 — "Service accounts and temporary accounts are bound to a single project and
  inherit its validity period. When the project expires, these accounts are automatically
  closed and deprovisioned from LDAP and other credential stores." A **user** account, by
  contrast, "remains active as long as the user has at least one active project
  membership" — which independently confirms the account-lifecycle slide.
- §5.2 — "Where appropriate, service accounts are restricted in scope (e.g. limited
  filesystem entitlements or reduced role set) to reduce the risk of credential
  compromise." This **corrected** the slide, which claimed a service account reaches all
  the project's resources.
- §5.2 — service accounts "preserve an explicit association with an account and project
  context, enabling clearer accountability and auditability". That is the accent line.
- §4.2 — the legacy **secondary account** was "a user-like identity with username and
  password but without multi-factor authentication", used interchangeably for automation
  and courses. That is why the new model separates the types, and it is the speaker-note
  line for anyone who used one.

Deliberately not used:

- §5.2 — "Where appropriate, service accounts are restricted in scope (e.g. limited
  filesystem entitlements or reduced role set) to reduce the risk of credential
  compromise." True of the architecture, but whether a PI can ask for a narrower scope
  today is unsettled, and a slide that promises a control the portal does not expose is
  worse than a slide that says nothing. Revisit when it is offered.

From Andrea, not from the paper or the docs:

Confirmed by Andrea on 25 August 2026, and in no CSCS document (see notes/docs-gaps.md):

- A service account is normally **run by the project team**, and registered on a **shared
  team address** so the notifications about it reach the team rather than one person's
  inbox. This is why the slide's accent no longer says "not a shared login" — it is shared
  by design; what must not be shared is somebody's own account.
- It has a **username of its own** and authenticates with an **API key**, not a password,
  and it has **no MFA** because it never logs in interactively. Worth saying out loud: the
  rest of the session tells people there is no access without MFA.

Not used, but worth knowing:

- §3.3 / §4.1 — SSH certificates are "typically one day for standard user accounts, and
  extended validity (seven days or one year) available for specific use cases and user
  categories". The handout says one day flat. The paper does **not** say which categories
  get the longer validity, so nothing was written from it — ask Andrea whether the
  handout should mention that longer validity exists.
- §4 — **temporary accounts** for courses and workshops are a first-class type. Nothing
  in the session mentions them. Possible backup slide if PIs ask about training events.

The paper names the workflow platform by its product name throughout. That name never
reaches a slide, a note or the handout — see CLAUDE.md §7.
