---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 2 · 40 min</span>

# A concrete ML use case

Raw data in, a trained model out. Every step is something you will actually type.

<!--
START AT T+19:00. Check the presenter timer now.
CUT IF LATE: Cut "Four ways to make this slow" and "Post-training". Both are one spoken line.
SAY:
- The rest of the hour is one worked example, not four topics.
- We start with raw data on your laptop and end with a trained model you can serve.
- Each step names the thing you type and the page that documents it.
- Owners of the subsections take over from here.
NEXT: The first problem is where the data goes.
-->
---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/filesystems/' -->
<div class="audience all">Everyone</div>

<span class="tag">Import your data</span>

# Six mount points, and they are not interchangeable

Putting data in the wrong one is the most common and most expensive mistake here.

| | Path | For | Cleanup |
|---|---|---|---|
| **Home** | `/users/$USER` | code, scripts, config — 50 GB | none |
| **Scratch** `iopsstor` | `/iopsstor/scratch/cscs/$USER` | training data, random I/O | **14 days** |
| **Scratch** `capstor` | `/capstor/scratch/cscs/$USER` | checkpoints, sequential I/O | **30 days** |
| **Scratch** `ritom` | `/ritom/scratch/cscs/$USER` | VAST — parallel, shared-file I/O | **30 days** |
| **Project store** | `/capstor/store/cscs/swissai/<project>` | shared, medium term, backed up | none |
| **Project** `datacache` | `/iopsstor/datacache/cscs/swissai/<project>` | shared fast datasets — **on request** | none |

<div class="accent">

**Scratch** is per user and is **not** backed up. **Store** is per project and **is** backed up.

</div>

<!--
This is the slide of the module. Do not rush it.
SAY:
- Six mount points. Read the table, do not read it out loud.
- Three groups. Home, scratch, and project.
- Home is small. 50 gigabytes. Code and configuration, nothing else.
- Three scratch filesystems. The difference between the first two is the next slide.
- Ritom is the third, on VAST, for parallel I/O into a shared file.
- Its cleanup is also 30 days. Say it out loud, because it is not in the documentation
  yet — anyone who checks will not find it there.
- Then two project areas: the store, which is backed up, and datacache, which is not and which you have to ask for.
GIVE THEM THE MODEL FIRST. Two words, two properties:
- Scratch is yours. Per user. Not backed up.
- Store belongs to the project. Shared. Backed up.
- Everything else on this slide hangs off those two.
HOME SITS BETWEEN THEM, if anyone asks:
- No cleanup, and there are daily snapshots of the last seven days in $HOME/.snapshot.
- That has saved people who deleted their own code. Worth knowing it exists.
- Tape backups for Home are being implemented, so do not promise them yet.
THEN POINT AT THE CLEANUP COLUMN:
- This is the column that hurts people.
- Say the mechanism precisely, because it is not what they assume.
- It is not age. It is last access time.
- A file nobody has read for 14 days on iopsstor is deleted. 30 days on capstor.
- So a dataset you keep reading survives. A checkpoint you wrote and forgot does not.
- Not archived. Deleted.
- Ritom's cleanup is 30 days too, but that is not in the documentation yet.
NEXT: So which scratch, for what?
DOCS: docs.cscs.ch/storage/filesystems/ · docs.cscs.ch/platforms/mlp/
-->

<!-- Verified against cscs-docs-preview.svc.cscs.ch/442, both /storage/filesystems/ and
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
    drops that qualifier. This is a documentation error, not a gap — fix the page. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/guides/storage/' -->
<div class="audience all">Everyone</div>

# NVMe for reading data, HDD for writing checkpoints

The three scratch filesystems are built from different hardware. Match the workload.

<div class="cols-3">
<div class="card">

### `iopsstor` — NVMe

Use it for:

- Training and validation datasets read **frequently and non-sequentially**
- **Many small, random** I/O operations

Cleaned after **14 days**.

</div>
<div class="card">

### `capstor` — HDD

Use it for:

- **Model checkpoints**
- Outputs involving **large, contiguous** I/O

Cleaned after **30 days**.

</div>
<div class="card">

### `ritom` — VAST over NFS

Use it for:

- Many ranks writing **one shared file** — collective MPI-IO, parallel HDF5
- Checkpoints from many ranks into **few files**

Little benefit for file-per-rank I/O.

</div>
</div>

<div class="accent">

Nothing on scratch survives. Shared project data goes on the **store** or on **`datacache`** — next two slides.

</div>

<!--
SAY:
- All three are called scratch. They are different hardware and they behave differently.
- iopsstor is NVMe. It is good at IOPS. Put your dataset there, the thing you read from constantly in random order.
- capstor is spinning disks, optimised for large sequential reads and writes. Put your checkpoints there.
- Get those two backwards and your training is slower for no reason at all.
- Then the third one, because they just saw it in the table.
- Ritom is VAST, over NFS. It is the one for parallel I/O into a shared file.
- Collective MPI-IO, parallel HDF5 or NetCDF, and checkpoints written from many ranks into a small number of files.
- The documentation is clear that file-per-rank I/O sees little benefit there, so it is not a general-purpose replacement for the other two.
- If you do use it, read the tuning settings in the storage guide first — locking, collective buffering, data sieving. VAST behaves differently from Lustre and MPI-IO can get it wrong by default.
- Its cleanup is 30 days, same as capstor. That is not documented yet, so say it rather than letting them look for it.
READ THE RED BAR:
- And when the job finishes, move what you care about to project storage. Say it every time.
NEXT: How much have you actually used?
DOCS: docs.cscs.ch/guides/storage/ · docs.cscs.ch/platforms/mlp/ (Scratch Usage Recommendations)
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/filesystems/' -->
<div class="audience">PIs and deputies</div>

# Project storage is what you asked for in the proposal

`/capstor/store/cscs/swissai/<project>` — the only durable place, and the only backed-up one.

<div class="cols">
<div>

- Quota comes from the **initial resource request**
- Small projects: **1 TB, 1M inodes** by default
- Large projects: **no default** — you state it in the proposal
- **Backed up** to tape: three most recent copies, every 24 hours
- No cleanup policy

</div>
<div class="card">

### At the end

Contents are retained for **three months** after the project finishes.

Home is retained for three months after your **last** project finishes.

</div>
</div>

<div class="accent">

This is why the proposal asks for a data footprint. Storage is not elastic.

</div>

<!--
SAY:
- Project storage is the only place that is neither small nor temporary.
- The quota is not negotiable after the fact. It is what you asked for in the proposal.
- Small projects get a terabyte by default. Large projects get no default at all, you state it.
- It is backed up to tape, three copies, every 24 hours. Scratch is not.
- And at the end, three months, then it goes.
- That connects back to module 1: this is why we ask for a data footprint up front.
NEXT: And from today there is a second project area, which is new.
DOCS: docs.cscs.ch/storage/filesystems/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience all">Everyone</div>

<span class="tag">New — from 26 August</span>

# `datacache` is fast, shared, and does not disappear

Available from today, after the maintenance. It fills the gap between scratch and project store.

<div class="cols-wide">
<div>

| | Fast? | Survives? | Shared by the project? |
|---|---|---|---|
| Scratch `iopsstor` | **yes** | no — 14 days | no, per user |
| Project store | medium | **yes** | **yes** |
| **`datacache`** | **yes** | **yes** | **yes** |

`/iopsstor/datacache/cscs/swissai/<project>`

</div>
<div class="card">

### How to get one

It is **not** provisioned by default.

Your **PI** opens a Service Desk ticket with the use case, and the space and inodes needed. CSCS reviews it before creating the area.

</div>
</div>

<div class="accent">

Project-level like the store, but **not backed up**, like scratch. And nothing is ever deleted for you.

</div>

<!--
This is new. Nobody in the room has used it. Spend a moment.
SAY, start from the problem it solves:
- Until today you had two bad options for a dataset the whole team reads.
- Put it on scratch: fast, but it is per user, and it is deleted after 14 days.
- Put it on project store: shared and durable, but it is medium-performance, so random reads are slow.
- So teams kept a copy each, on scratch, and re-staged it every two weeks.
- datacache is the third option. Fast NVMe, shared across the project, and never cleaned automatically.
- One copy of the dataset. The whole project reads it. It is still there next month.
POINT AT THE RED BAR:
- Place it against the model from two slides ago. Scratch is yours and not backed up. Store is the project's and is backed up.
- datacache is the odd one: it belongs to the project, like the store, but it is not backed up, like scratch.
- And unlike both, nothing is ever deleted for you.
- Within your quota on capacity and inodes, the project owns its own space hygiene. That is a real responsibility.
HOW TO GET IT:
- It is not created by default. Your PI opens a Service Desk ticket saying what it is for and how much space and how many inodes.
- We review it before creating the area.
NEXT: Where to read more.
DOCS: docs.cscs.ch/platforms/mlp/
-->

<!-- TODO(verify): THIS SLIDE'S FOOTER DOES NOT YET BACK IT. The live
docs.cscs.ch/platforms/mlp/ does not mention datacache at all.
datacache is documented only on the preview at
cscs-docs-preview.svc.cscs.ch/442/platforms/mlp/ and goes live on 26 August after the
maintenance. Confirm on the morning of the session that it is actually available — if
the maintenance slips, this slide says "from today" and would be wrong on stage.
Re-point the DOCS line once the page is merged. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/guides/storage/' -->
<div class="audience all">Everyone</div>

# Inodes run out before terabytes do

A quota has two numbers, and people only remember one.

<div class="cols">
<div>

- Home is **50 GB** — and **500,000 inodes**
- One inode is roughly one file
- **One PyTorch virtual environment is about 22,800 inodes**
- So about twenty of those and Home is full, on a metric nobody was watching

</div>
<div class="card">

### The fix, and it is the same one as module 3

> "Lustre is not well suited to handling many small files."

Squash the environment into a **single squashfs image**. One file instead of twenty-two thousand.

That is exactly what a **uenv** already is.

</div>
</div>

<div class="accent">

Millions of small training files hurt the metadata servers, not just your quota.

</div>

<!--
SAY:
- A quota has two numbers and people only remember the gigabytes.
- Space, and inodes. An inode is roughly a file.
- Home gives you 50 gigabytes and five hundred thousand files.
- Now the number that surprises everyone: one PyTorch virtual environment is about
  twenty-two thousand eight hundred inodes.
- So roughly twenty environments and your home directory is full — not on size, on file count.
- The documentation is blunt about why: Lustre is not well suited to handling many small files.
- The fix is on the right, and it is the same trick module 3 will show you.
- Squash the whole environment into one squashfs image. One file, not twenty-two thousand.
- That is literally what a uenv is. Module 3 picks this up.
NEXT: Now get the data in.
DOCS: docs.cscs.ch/guides/storage/ · docs.cscs.ch/storage/filesystems/
-->

<!-- TODO(verify): the quota-checking command is in the "Checking quota" section of the
storage docs and was never captured here. Module 2 owner: quote it verbatim and put it
on this slide or say it out loud. The 22,800-inode figure and the Lustre quotation come
from cscs-docs-preview.svc.cscs.ch/442/guides/storage/. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/transfer/' -->
<div class="audience all">Everyone</div>

# Moving data in: Globus from outside, `xfer` from inside

Never move terabytes from a login node.

<div class="cols">
<div>

### From outside CSCS

The recommended route is the **CSCS Globus Online endpoint**. Authenticate with your CSCS credentials.

### Between CSCS filesystems

Submit to the **`xfer`** Slurm partition. Do not do it interactively.

```bash
#!/bin/bash -l
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --partition=xfer

command="rsync -av"
srun -n $SLURM_NTASKS $command $1 $2
```

</div>
<div class="card">

### `rclone` beats `rsync` at scale

For a directory with many files, or a few very large checkpoints, `rclone` copies in parallel.

**Many files**
`rclone copy --transfers=16 --checkers=32 --progress`

**Large files**
`rclone copy --multi-thread-streams=4 --multi-thread-cutoff=256M --transfers=4 --progress`

**1 TB in about 5 minutes** — roughly 3 GB/s.

</div>
</div>

<!--
SAY:
- Two directions, two tools.
- From outside CSCS, use Globus. It handles restarts, which matters when the transfer takes hours.
- Between CSCS filesystems, use the xfer partition. It is a Slurm partition dedicated to this.
- The point of xfer is that you are not doing it on a login node, where you would be hurting everybody else.
- On the right, the thing people do not know: rclone is often much faster than rsync, because it works in parallel.
- Two flag sets, one for many small files, one for a few big ones.
- Give them the concrete number: a one terabyte directory from store to scratch takes about five minutes. Roughly three gigabytes a second.
- Start with those values and raise the parallelism gradually, watching the effect on the metadata servers.
- If you need to chain transfers, xfer jobs take --dependency=afterok like any other Slurm job.
NEXT: What about data that has to outlive the project?
DOCS: docs.cscs.ch/storage/transfer/
-->

<!-- TODO(verify): the transfer guidance and the rclone flags come from the preview
cscs-docs-preview.svc.cscs.ch/442/storage/transfer/. Re-check once merged. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/services/inference/api/' -->
<span class="tag">Prepare it with inference</span>

<div class="audience all">Everyone</div>

# Use a model before you train one

The inference resource from module 1 is useful long before you have a model of your own.

<div class="cols">
<div>

- **Vet the raw data** — classify, filter and spot problems at scale
- **Build the training set** — rewrite, synthesise, label
- **Write the job scripts** — point a coding agent at the same endpoint

</div>
<div class="card">

### Same endpoint, same credit

`api.inference.cscs.ch/v1`

The docs show how to configure **Claude Code** and **OpenCode** against it.

</div>
</div>

<div class="accent">

You have raw data and no model yet. This is the step most people skip.

</div>

<!--
SAY:
- You have just landed raw data on scratch. You do not have a model yet.
- The inference resource from module 1 is already useful here, and this is the step most people skip.
- Vetting: run the raw data past a model to classify it, filter it, find what is broken.
- Building the training set: rewriting, synthesising, labelling.
- And writing the job scripts themselves — you can point a coding agent at the same endpoint.
- It is the same API and the same project credit. Nothing new to request.
NEXT: Now set up a place to work.
DOCS: docs.cscs.ch/services/inference/api/
-->

<!-- TODO(verify): the inference API is documented; using it for data vetting and
training-set preparation is our suggestion, not something docs.cscs.ch recommends.
Keep it framed as a suggestion. -->
---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/firecrest/' -->
<span class="tag">Set up your workflow</span>

<div class="audience all">Everyone</div>

# FirecREST: the cluster as an HTTP API

For CI pipelines, workflow engines and anything that cannot hold an SSH key.

<div class="cols">
<div>

**ML Platform endpoint**

`api.cscs.ch/ml/firecrest/v2`

Over HTTP:

- filesystem operations — `ls`, `mkdir`, `mv`, `chmod`
- Slurm — submit, query, cancel
- data transfers, internal and external

</div>
<div class="card">

### How it authenticates

A client ID and secret, exchanged for a short-lived **JWT access token**, valid **5 minutes**.

No passwords in a pipeline. This is what a **service account** is for.

</div>
</div>

<!--
SAY:
- If the work has to repeat, drive it over HTTP instead of by hand.
- One endpoint per platform. Yours is the ml one.
- List files, make directories, submit and cancel Slurm jobs, move data.
- Authentication is a client ID and secret exchanged for a five-minute token. No passwords in a pipeline.
- That is what the service accounts from module 1 are for.
NEXT: Or a notebook, if you would rather not script it.
DOCS: docs.cscs.ch/access/firecrest/ · eth-cscs.github.io/firecrest-v2/
-->
---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/jupyterlab/' -->
<div class="audience all">Everyone</div>

# JupyterLab: a notebook on a compute node

`jupyter-clariden.cscs.ch` — you pick the nodes, the time, the project and the environment.

<div class="cols-narrow">
<div>

- One URL per cluster: **`jupyter-clariden.cscs.ch`**
- The spawner form asks for node type and count, wall time, **project account**, and **uenv or container image**
- It runs on a compute node, so it spends project credit while it is open
- Startup should be under a few minutes

</div>
<div class="shot">

**SCREENSHOT**

The JupyterHub spawner options form on `jupyter-clariden.cscs.ch`, with the environment
and account fields visible.

</div>
</div>

<!--
SAY:
- If you would rather not think about sbatch, this is the way in.
- One URL per cluster. Clariden is jupyter dash clariden dot cscs dot ch.
- You get a form. Node type, how many, wall time, which project pays, and which environment — the same uenv or container from module 3.
- Two things people get wrong. It runs on a compute node, so leaving it open costs credit — close it when you stop. And "disk I/O error" when saving a notebook almost always means you are out of quota, not that Jupyter is broken.
NEXT: And for automation, there is an API.
DOCS: docs.cscs.ch/access/jupyterlab/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/firecrest/' -->
<div class="audience all">Everyone</div>

<span class="tag">Watch it from a browser</span>

# The HPC Console: the cluster in a browser

`console.mlp.cscs.ch` — nothing to install, and it needs no agent on the cluster.

<div class="cols">
<div>

- **Dashboard** — cluster health. It will stop you submitting to a degraded cluster
- **Jobs** — list, filter, submit, and inspect logs
- Every job has a **shareable URL**: send a colleague the failing job, not a screenshot
- **Files** — browse, preview, upload

</div>
<div class="card">

### The same API underneath

It runs on **FirecREST**, so anything the console does, your own script can do:

`api.cscs.ch/ml/firecrest/v2`

Client ID and secret, exchanged for a 5-minute token. No passwords in CI — this is what a **service account** is for.

</div>
</div>

<div class="accent">

Same login as everything else. Longer version in the backup slides, if you want it.

</div>

<!--
SAY:
- Third way in, and the one fewest of you will have seen.
- A browser pointed at the cluster. Nothing to install, and no agent running as you on the cluster.
- The dashboard shows cluster health, and it will refuse to submit to a degraded cluster. That alone saves a failed overnight run.
- Jobs: list, filter, submit, read the logs.
- The feature I would highlight is the shareable per-job URL. It replaces the screenshot-in-Slack workflow that most debugging conversations start with.
POINT AT THE CARD:
- It runs on FirecREST, and that is the useful part: anything the console can do, your script can do, because it is the same API.
- Client ID and secret for five-minute tokens. No passwords in a pipeline. That is what the service accounts from module 1 are for.
- We have five more slides on this in backup if the discussion wants them.
NEXT: One last thing, and it does not involve a cluster at all.
DOCS: docs.cscs.ch/access/firecrest/ · eth-cscs.github.io/firecrest-v2/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/uenv/' -->
<div class="audience all">Everyone</div>

<span class="tag">Train your own model</span>

# Two ways to get software, and they are not rivals

<div class="cols">
<div class="card">

### uenv

A **user environment**: scientific applications, libraries and tools, packaged as a single Squashfs file with its own module tree.

Built and maintained by CSCS for Alps.

</div>
<div class="card">

### Container Engine

Runs your job **inside a Linux container**, so you bring the userspace you already know.

Described by an **EDF**, an Environment Definition File.

</div>
</div>

<div class="accent">

For PyTorch, the documentation recommends the **Container Engine** route. Both are supported.

</div>

<!--
SAY:
- Two supported mechanisms. People ask which one is correct. Both are.
- A uenv is a CSCS-built environment, one Squashfs file containing the software and its modules.
- The Container Engine runs your job inside a container you describe with a small file.
- For PyTorch specifically, the docs recommend the container route, and that is what most of you will use.
- The honest difference: uenv is built for Alps; containers let you use portable environments built by third parties.
NEXT: uenv first, because it is three commands.
DOCS: docs.cscs.ch/software/uenv/ · docs.cscs.ch/software/container-engine/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/uenv/' -->
<div class="audience all">Everyone</div>

# A uenv is three commands

Find, pull, start.

```bash
uenv image find pytorch                        # what is available
uenv image pull pytorch/v2.8.0:v1              # download it
uenv start pytorch/v2.8.0:v1                   # a shell inside it
uenv run pytorch/v2.8.0:v1 -- python train.py  # or one command, then exit
```

<div class="cols">
<div>

- `uenv image ls` — what you have downloaded
- `uenv image inspect` — details
- Each uenv is a **single Squashfs file**

</div>
<div class="card">

### PyTorch is available as a uenv

**v2.9.1** and **v2.8.0** for **GH200** on Clariden, Daint and Santis. **v2.6.0** on Clariden and Daint.

</div>
</div>

<!--
SAY:
- Four commands, and note the shape: an image is always name, version and tag.
- Find shows you what exists. Pull downloads it. Start drops you into a shell inside it.
- If you want to run one thing and get out, uenv run.
- The whole environment is one file. That is why it starts fast on a parallel filesystem.
- And yes, PyTorch is available this way, several versions, for the Grace-Hopper nodes.
NEXT: Now the container route, which is the one the PyTorch docs recommend.
DOCS: docs.cscs.ch/software/uenv/
-->

<!-- Verified against docs.cscs.ch/software/uenv/ and /software/uenv/using/: images are
always referenced as name/version:tag, `uenv image find` is shown with an argument,
`uenv run` takes `--` before the command. The versions and their clusters come from the
Versioning table on docs.cscs.ch/software/ml/pytorch/. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/container-engine/' -->
<div class="audience all">Everyone</div>

# A container is described by one small file

The EDF uses the TOML format: minimal and straightforward.

```toml
image = "library/ubuntu:24.04"
mounts = ["${SCRATCH}:${SCRATCH}"]
workdir = "${SCRATCH}"
```

<div class="cols">
<div class="code-sm">

Save them in `$HOME/.edf`:

```bash
$ ls $HOME/.edf
ubuntu.toml
```

Then one flag on `srun` commands:

```bash
$ srun --environment=ubuntu cat /etc/os-release | grep PRETTY
PRETTY_NAME="Ubuntu 24.04 LTS"

$ srun --environment=ubuntu --pty bash
```

</div>
<div class="card">

### Three of the most used keys

- `image` — the container image to use (the only strictly required parameter)
- `mounts` — what of Alps to make visible inside
- `workdir` — where you land when the job step starts

</div>
</div>

<!--
SAY:
- This is the entire concept. A small TOML file names an image, says what to mount, says where to start.
- You give it a name, and then everywhere you would have run something, you add one flag.
- srun dash dash environment. That is it. It works in interactive jobs and in batch scripts identically.
- The mounts line is the one people forget. Inside the container, Alps filesystems are not there unless you say so.
NEXT: A realistic one, for PyTorch.
DOCS: docs.cscs.ch/software/container-engine/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/ml/pytorch/' -->
<div class="audience all">Everyone</div>

# A realistic PyTorch EDF

The NGC PyTorch container is a good base image: PyTorch is pre-installed with an optimised build.

<div class="cols">
<div class="code-sm">

```toml
image = "nvcr.io/nvidia/pytorch:26.06-py3"

mounts = [
    "/capstor:/capstor",
    "/iopsstor:/iopsstor"
]

workdir = "${SCRATCH}/my-project"

[env]
OMP_NUM_THREADS = "72"
TORCH_NCCL_ASYNC_ERROR_HANDLING = "1"
#NCCL_DEBUG = "INFO"

[annotations]
com.hooks.aws_ofi_nccl.enabled = "true"
```

</div>
<div class="stack">
<div class="card">

### The EDF as a blueprint

- Declaratively describes your job environment. The Container Engine instantiates it.
- Separates the *description* of the container from the *commands* you run inside it.

</div>
<div class="card">

### The annotations introduce HPC features

The **aws-ofi-nccl** hook makes multi-node NCCL use the Slingshot network.

Skip it and your multi-node training is quietly slow.

</div>
</div>
</div>

<!--
This is the slide to spend time on.
SAY:
- This is a realistic EDF to run generic PyTorch tasks.
- Top line: Enter the image by registry reference. The Container Engine downloads and caches it.
- The mounts bring in both scratch filesystems.
- Say what the EDF buys you: it separates what you want from how the container is managed, and the container description from the commands in your job script.
- Now the part that is specific to this machine, and the reason a laptop container is not enough.
POINT AT THE ANNOTATIONS BLOCK:
- Annotations are arbitrary metadata for the container. We use them to request custom features to the Container Engine.
- The AWS OFI NCCL hook connects NCCL to the Slingshot network through libfabric.
- If you leave it out, multi-node training still works. It is just quietly, badly slow.
- That is the single most common performance bug we see.
- There are more annotations and more features. The documentation lists them.
THE [env] BLOCK, only if asked:
- OMP_NUM_THREADS aligns with the number of cores of Grace CPU
- NCCL_DEBUG=INFO so you can see what the network actually did. EDF supports comments: comment out for cleaner outputs.
- The full block is on the PyTorch documentation page. Do not read it out.
NEXT: Where the images come from.
DOCS: docs.cscs.ch/software/ml/pytorch/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/ml/pytorch/' -->
<div class="audience all">Everyone</div>

# Where to get images

<div class="cols-3">
<div class="card">

### Alps Extended Images

CSCS-curated ML/AI images, specifically customized for Alps.

Robust and straightforward to use.

Use carefully as base for new images: they depend on host software compatibility.

</div>
<div class="card">

### NGC

NVIDIA GPU Cloud. PyTorch pre-installed, optimised build, most dependencies included.

A great all-around option for NVIDIA GPU systems.

</div>
<div class="card">

### Build your own

Extend a base image for specific needs.

Build on Alps with Podman: ARM64 arch, fast nodes, caching options through CSCS JFrog registry.

Push the image to a registry or convert it to a local SquashFS file.

</div>
</div>

<div class="accent">

Build on top of a base image that most suits your use case.

</div>

<!--
SAY:
- Three things to know about images.
- Alps Extended Images: curated by CSCS and tuned for this machine. Start here if one fits.
- NGC as the all-rounder. PyTorch is already there, already built well for these GPUs.
- And you can build your own on Alps, with Podman, on the right architecture.
READ THE RED BAR:
- Build on top of something that works. Starting from a bare Ubuntu on this machine is a huge effort (CUDA, DL libs, PyTorch, network...).
NEXT: The mistakes we see.
DOCS: docs.cscs.ch/software/ml/pytorch/ · docs.cscs.ch/software/container-engine/
-->

<!-- TODO(verify): the PR dropped com.hooks.aws_ofi_nccl.variant = "cuda12" from the
annotations block, keeping only .enabled. Ask Alberto whether the variant is no longer
needed or whether this was a simplification — if it is still required, the slide is
missing a line that decides whether multi-node training is fast.

TODO(verify): the exact import command (enroot / podman / the CSCS-recommended
route) was not captured and is NOT stated on the container-engine overview page. Module 3
owner: find it, quote it verbatim, and put it on this slide. Without a real command this
slide is advice, not instruction. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/running/slurm/' -->
<div class="audience all">Everyone</div>

# Every job is charged to a project

`--account` is not optional. It is how the GPU hours from module 1 get spent.

```bash
#!/bin/bash
#SBATCH --account=a-csstaff
#SBATCH --job-name=example-%j
#SBATCH --time=00:30:00
#SBATCH --nodes=4

srun --environment=my-pytorch python train.py
```

<div class="cols">
<div>

| Partition | Max nodes | Time limit |
|---|---|---|
| `debug` | 2 | 30:00 |
| `normal` | unlimited | 1-00:00:00 |
| `xfer` | 1 | 1-00:00:00 |

</div>
<div class="card">

### The link back to module 1

This is the line that draws down the credit. The **grace** and the **minimal** from module 1 are counted from these jobs.

</div>
</div>

<!--
SAY:
- One script. It is short on purpose.
- The account flag is how Slurm knows which project pays. It is not optional.
- This is the line that connects to module 1: every job here draws down the credit Anna was granted.
- Three partitions. Debug for quick turnaround, two nodes, thirty minutes. Normal for real work. Xfer for data, which module 2 covered.
- And the srun line carries the environment flag from module 3. That is the whole stack in one script.
NEXT: How to ask for GH200 nodes properly.
DOCS: docs.cscs.ch/running/slurm/
-->

<!-- TODO(verify): docs.cscs.ch/access/jupyterlab/ never states that a session is a
Slurm job charged to the project. It says notebook servers run on compute nodes and
references slurm-<jobid>.out, which strongly implies it, but the accounting is not
written down. Confirm, then say it plainly — it changes whether people leave sessions
open overnight.

TODO(verify): --account=a-csstaff is a placeholder. Module 4 owner: replace with a
realistic Swiss AI project account string, and confirm the partition table against
docs.cscs.ch/running/slurm/ for the ML Platform specifically — the partitions listed
there may differ per cluster. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/running/slurm/' -->
<div class="audience all">Everyone</div>

# A GH200 node is four GPUs and four sockets

Ask for it the way the hardware is built.

<div class="cols">
<div>

```bash
#SBATCH --ntasks-per-node=4
#SBATCH --gpus-per-task=1
```

One task per GPU. This is the shape almost every ML job wants.

For multiple job steps on one node:

```bash
#SBATCH --exclusive --mem=450G
```

</div>
<div class="card">

### Why this matters

Ask for the wrong shape and you get one process driving four GPUs badly, or four processes fighting over one.

Neither shows up as an error. Both show up as a bill.

</div>
</div>

<!--
SAY:
- A Grace-Hopper node is four GPUs and four CPU sockets. Ask for it that way.
- Four tasks per node, one GPU per task. That is the shape nearly every ML job wants.
- If you are running several job steps on the same node, take it exclusive.
- The reason to care is on the right: getting this wrong is not an error message. It is a slow job that still costs you the full node hours.
NEXT: Which brings us to efficiency.
DOCS: docs.cscs.ch/running/slurm/
-->

---
<div class="audience">PIs and deputies</div>

# You are billed for the node, not for the work

<!-- PLACEHOLDER — module 4 owner: this needs a real efficiency example or a tool name. -->

<div class="cols">
<div>

- A node reserved is a node **charged**, busy or idle
- 30% GPU utilisation means **70% of your credit** bought nothing
- Efficiency was a question in the proposal (module 1). It is the same question here
- Measure one run before scaling to a hundred

</div>
<div class="card">

### For the PIs

This is the other half of "check the consumption monthly".

Burning the budget on schedule and getting nothing out of it is **worse** than under-consuming.

</div>
</div>

<!--
SAY, and this one is aimed at the PIs:
- You are billed for the node you reserved, not for the work you did on it.
- If your GPUs sit at thirty per cent, seventy per cent of that credit bought nothing.
- Remember module 1 asked you for an expected efficiency in the proposal. This is where that promise is kept or not.
- The habit that fixes it: measure one run properly before you scale it to a hundred.
POINT AT THE CARD:
- And for the PIs specifically. Spending the budget on schedule while achieving nothing is worse than under-spending, because it is invisible.
NEXT: You do not have to do all of this from a terminal.
-->

<!-- TODO(verify): docs.cscs.ch/running/slurm/ does not document a job-efficiency tool.
Module 4 owner: name the tool you actually recommend (seff, a Grafana dashboard, the HPC
Console job view) and put a real number on this slide, or cut it to a spoken line. -->

---
<div class="audience all">Everyone</div>

# Four ways to make this slow

<div class="cols">
<div>

- **No NCCL hook** — multi-node training falls back and crawls
- **Dataset on the wrong scratch** — random reads from spinning disk
- **Imported image on home** — quickly eats into 50 GB quota

</div>
<div class="card">

### The good habit

One EDF per project, checked into your repository next to the code.

Then the environment is **reviewable** and **reproducible**, like everything else.

</div>
</div>

<!--
SAY:
- Four mistakes, all of which we see regularly.
- No NCCL hook, covered already, the big one.
- Dataset on capstor instead of iopsstor. Module 2's mistake showing up as a module 3 symptom.
- Image sitting on home, where you have 50 gigabytes.
- Rebuilding the image on every job instead of importing once.
- On the right, the habit that prevents most of this: commit the EDF next to your code.
- Then your environment is reviewed like code, and somebody else can reproduce your run.
NEXT: Where to read more.
-->

---

<span class="tag">Serving at scale</span>

<div class="audience all">Everyone</div>

# Serving your own model

<div class="accent">

**Placeholder — still to be decided.** Whether this is the inference service or a Slurm job is an open question for the presenters.

</div>

<!--
PLACEHOLDER. Andrea and Fawzi have not settled whether serving a model you trained
yourself goes through the inference service or through a Slurm job on the cluster.
Do not improvise this on stage: if it is still open on the day, say it is coming and
point at the tutorials.
NEXT: Post-training.
-->
---

<span class="tag">Post-training</span>

<div class="audience all">Everyone</div>

# After the first training run

<div class="accent">

**Placeholder — content still to be written.**

</div>

<!--
PLACEHOLDER. Nothing written yet. Fine-tuning, RLHF and evaluation would live here.
The ML tutorials cover fine-tuning already, so the cheapest version of this slide is a
pointer at docs.cscs.ch/tutorials/ml/.
NEXT: One last thing, and it is not on Alps.
-->
---

<span class="tag">Kubernetes</span>

<div class="audience all">Everyone</div>

# Swiss AI has its own Kubernetes cluster

Separate from Alps, and separate from how everything else in this hour is granted.

<div class="cols">
<div>

- A **dedicated cluster** for the Swiss AI Initiative
- Access is **managed by Imanol** — not through `portal.cscs.ch`
- Not the general Alps service: the documentation says that one is "only available for specific partners"

</div>
<div class="card">

### Why it is mentioned at all

Because people ask, and because the answer is not "no" — it is "yes, through a different door".

</div>
</div>

<!--
SAY:
- Thirty seconds, because it comes up every time.
- There is a dedicated Kubernetes cluster for the Swiss AI Initiative.
- It is not the general Alps Kubernetes service — the documentation is explicit that that one is only for specific partners and is not available to normal users on Alps.
- Access is arranged through Imanol, not through the portal.
- That is all we are saying about it today. If you want it, come and find us.
NEXT: Where to read more.
-->

<!-- TODO(verify): this is Andrea's, not the documentation's. Nothing on docs.cscs.ch
describes a Swiss AI Kubernetes cluster. Confirm Imanol's full name and the right way
to reach him before the session — "managed by Imanol" is not something a stranger in
the audience can act on. -->
---

<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Data

- **File systems and quotas** — docs.cscs.ch/storage/filesystems/
- **Data transfer** — docs.cscs.ch/storage/transfer/
- **Storage guide** — docs.cscs.ch/guides/storage/

### Software

- **uenv** — docs.cscs.ch/software/uenv/
- **Container Engine** — docs.cscs.ch/software/container-engine/
- **Building images on Alps** — docs.cscs.ch/build-install/containers/
- **PyTorch** — docs.cscs.ch/software/ml/pytorch/

</div>
<div class="card dark">

### Running and watching

- **Slurm** — docs.cscs.ch/running/slurm/
- **JupyterLab** — docs.cscs.ch/access/jupyterlab/
- **FirecREST** — docs.cscs.ch/access/firecrest/

### Worked examples

- **ML tutorials** — docs.cscs.ch/tutorials/ml/

### If you open one link tonight

Make it the tutorials.

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- Everything in the last forty minutes is on one of these pages.
- If you open one link tonight, make it the tutorials. They are complete worked examples.
NEXT: hand over to the wrap-up.
-->
