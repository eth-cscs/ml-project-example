---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 2 · ~10 min</span>

# Data and storage

You are in, with an empty home directory. Where do two terabytes of training data go?

<!--
START AT T+15:00. Check the presenter timer now.
CUT IF LATE: Cut "Project storage is what you asked for in the proposal". The mount-point table already shows it — say the default quota in one line.

- You are in, with an empty home directory on Clariden.
- Your first real question is where to put your data.
- This is the most expensive mistake on the platform.
- The wrong filesystem means slow training, or deleted data.
- Next: six places, and they are not interchangeable.
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/filesystems/' -->
<div class="audience all">Everyone</div>

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
- Six mount points, in three groups: home, scratch, project.
- Home is small. Fifty gigabytes, for code and configuration.
- Three scratch filesystems. The next slide says which is for what.
- Two project areas: the store is backed up, datacache is not.
- Now the cleanup column. This is the one that hurts people.
- It is not age, it is last access. Fourteen days on iopsstor, thirty on capstor.
- A dataset you keep reading survives. A checkpoint you wrote and forgot does not.
- Deleted, not archived. There are no backups on scratch.
- The model to remember: scratch is yours and not backed up. Store is the project's and is backed up.
- Next: which scratch, for what?
DOCS: docs.cscs.ch/storage/filesystems/ · docs.cscs.ch/platforms/mlp/
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/guides/storage/' -->
<div class="audience all">Everyone</div>

# NVMe for training data, HDD for writing checkpoints

The three scratch filesystems are built from different hardware. Match the workload.

<div class="cols-3">
<div class="card">

### `iopsstor` — NVMe

- Training and validation datasets read **frequently and non-sequentially**
- **Many small, random** I/O operations

Cleaned after **14 days**.

</div>
<div class="card">

### `capstor` — HDD

- **Model checkpoints**
- Outputs involving **large, contiguous** I/O

Cleaned after **30 days**.

</div>
<div class="card">

### `ritom` — VAST over NFS

- Many ranks writing **one shared file** — collective MPI-IO, parallel HDF5
- Checkpoints from many ranks into **few files** — little benefit for file-per-rank

Cleaned after **30 days**.

</div>
</div>

<div class="accent">

Nothing on scratch survives. Shared project data goes on the **store** or on **`datacache`** — next two slides.

</div>

<!--
- All three are called scratch, but they are different hardware.
- iopsstor is NVMe. Put your training data there — the thing you read constantly, in random order.
- capstor is spinning disk, for large sequential writes. Checkpoints go there.
- Get those two backwards and your training is slower for no reason.
- Ritom is VAST, for many ranks writing into one shared file. Read the tuning settings first.
- When a job ends, move what you care about to project storage.
- Next: how much have you actually got?
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
- The only place that is neither small nor temporary.
- The quota is what you asked for in the proposal. It is not negotiable afterwards.
- Small projects get a terabyte. Large projects get no default at all.
- Backed up to tape, three copies, every day. Scratch is not.
- At the end you get three months, then it goes.
- This is why module 1 asks for a data footprint up front.
- Next: from today there is a second project area.
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
- This one is new, from today. Nobody here has used it.
- The problem first. A dataset the whole team reads had two bad homes.
- Scratch is fast, but per user, and deleted after fourteen days.
- The store is shared and durable, but slow for random reads.
- So teams kept a copy each and re-staged it every two weeks.
- datacache is the third option. Fast NVMe, shared by the project, never cleaned.
- Two warnings. Not backed up, and nothing is deleted for you.
- Not created by default. Your PI opens a Service Desk ticket.
- Next: now get the data in.
DOCS: docs.cscs.ch/platforms/mlp/
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/transfer/' -->
<div class="audience all">Everyone</div>

# Globus from outside, `xfer` inside, S3 from either side

<div class="cols">
<div>

### From outside CSCS

The recommended route is the **CSCS Globus Online endpoint**.

### Between CSCS filesystems

Submit to the **`xfer`** Slurm partition, never interactively.

```bash
#!/bin/bash -l
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --partition=xfer
srun rsync -av $1 $2
```

</div>
<div class="card">

### `rclone` beats `rsync` at scale

`rclone` copies in parallel — many small files, or a few large ones.

**Many files**
`rclone copy --transfers=16 --checkers=32`

**Large files**
`rclone copy --multi-thread-streams=4 --multi-thread-cutoff=256M --transfers=4`

**1 TB in about 5 minutes** — roughly 3 GB/s.

</div>
</div>

<div class="accent">

**S3** as well: the object store at `rgw.cscs.ch`, and `rclone` speaks it too.

</div>

<!--
- Never move terabytes from a login node.
- From outside, use Globus. It handles restarts, which matters over hours.
- Between our filesystems, use the xfer partition. Not a login node, where you hurt everybody else.
- On the right, the thing people do not know: rclone is much faster than rsync, because it runs in parallel.
- Two flag sets. Many small files, or a few big ones.
- The number to give them: one terabyte from store to scratch in about five minutes.
- Raise the parallelism gradually and watch the metadata servers.
- Last line: we also have object storage, and it speaks S3, at rgw dot cscs dot ch.
- rclone is an S3 client too, so the same tool moves data between a bucket and the filesystems.
- Next: what about data that has to outlive the project?
DOCS: docs.cscs.ch/storage/transfer/ · docs.cscs.ch/storage/object/
-->


---
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Storage

- **Overview** — docs.cscs.ch/storage/
- **File systems and quotas** — docs.cscs.ch/storage/filesystems/
- **Data transfer** — docs.cscs.ch/storage/transfer/
- **Storage guide** — docs.cscs.ch/guides/storage/
- **Object storage** — docs.cscs.ch/storage/object/

### Platform specifics

- **ML Platform storage, incl. `datacache`** — docs.cscs.ch/platforms/mlp/

</div>
<div class="card dark">

### The three rules

- **Home** is for code. 50 GB, 500k inodes.
- **Scratch** is yours. Not backed up. Cleaned after 14 or 30 days.
- **Project** areas are shared. Store is backed up, `datacache` is not.

### And one habit

After every job, move the results off scratch.

</div>
</div>

<!--
- I will not read this out. Three rules.
- Home is for code. Scratch is yours and gets cleaned. The project areas are shared and do not.
- Of the two project areas, only the store is backed up.
- The habit: after every job, move results off scratch.
- Next: now you need software that can read it.
-->
