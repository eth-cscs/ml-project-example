---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 3 · 30 min</span>

# A concrete ML use case

Raw data in, a trained model out. Every step is something you will actually type.

<!--
START AT T+32:00. Check the presenter timer now.
CUT IF LATE: Cut "Four ways to make this slow" and "The data is already here". Both are one spoken line.

- The rest of the hour is one worked example, not four topics.
- We start with raw data on your laptop and end with a trained model you can serve.
- Each step names the thing you type and the page that documents it.
- Owners of the subsections take over from here.
- Next: The first problem is where the data goes.
-->
---
<div class="audience all">Everyone</div>

# What we are going to do

Raw data on one side, a model you can call on the other. Everything in between is the next half hour.

<div class="diagram">
<svg viewBox="0 0 1160 350" width="100%" role="img"
     aria-label="A four-stage pipeline: import raw data, prepare it, train a model, serve it. Underneath, the four ways of driving the work: ssh, JupyterLab, the HPC Console and FirecREST.">
  <g font-family="Inter, sans-serif">
    <g fill="#F7F7F8" stroke="#E5E5E5">
      <rect x="26"  y="20" width="248" height="150" rx="14"/>
      <rect x="330" y="20" width="248" height="150" rx="14"/>
      <rect x="634" y="20" width="248" height="150" rx="14"/>
      <rect x="938" y="20" width="196" height="150" rx="14"/>
    </g>
    <g stroke="#D61F26" stroke-width="2.5" fill="none">
      <path d="M284 95 h36"/><path d="M310 85 l12 10 l-12 10"/>
      <path d="M588 95 h36"/><path d="M614 85 l12 10 l-12 10"/>
      <path d="M892 95 h36"/><path d="M918 85 l12 10 l-12 10"/>
    </g>
    <g font-size="15" font-weight="600" fill="#D61F26" letter-spacing="0.6">
      <text x="52"  y="58">1 · IMPORT</text>
      <text x="356" y="58">2 · PREPARE</text>
      <text x="660" y="58">3 · TRAIN</text>
      <text x="964" y="58">4 · SERVE</text>
    </g>
    <g font-size="21" fill="#1A1A1A">
      <text x="52"  y="99">Raw data onto the</text> <text x="52"  y="129">filesystem that fits it</text>
      <text x="356" y="99">Vet it, and build</text>   <text x="356" y="129">the training set</text>
      <text x="660" y="99">A container, Slurm,</text> <text x="660" y="129">and the GPUs</text>
      <text x="964" y="99">Make the model</text>     <text x="964" y="129">callable</text>
    </g>
    <line x1="26" y1="232" x2="1134" y2="232" stroke="#F0F0F0" stroke-width="1"/>
    <text x="26" y="268" font-size="15" font-weight="600" fill="#888888" letter-spacing="0.6">DRIVEN FROM WHICHEVER OF THESE FITS</text>
    <text x="26" y="304" font-size="21" fill="#1A1A1A">ssh · JupyterLab · the HPC Console · FirecREST</text>
    <text x="26" y="334" font-size="17" fill="#555555">All four spend the same project credit.</text>
  </g>
</svg>
</div>

<!--
- Before the details, here is the shape of the next half hour.
- Four steps. Import, prepare, train, serve.
- Step one is done: it was the previous module, and I will spend fifteen seconds on it.
- Step two is the one people skip. You have raw data and no model, and there is already something useful to do.
- Step three is the long one: a container, Slurm, and the GPUs.
- Step four is making the model callable by someone other than you.
- Underneath all of it, four ways of driving the work, and you pick whichever fits the task.
- They all spend the same project credit, which is the thread back to module 1.
- Two of these steps are still being written, and I will say so when we get there.
- Next: the data.
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/storage/transfer/' -->
<span class="tag">Import your data</span>

<div class="audience all">Everyone</div>

# The data is already here

You know this part — it was the previous module. One slide to place it in the story.

<div class="cols">
<div>

- From **outside CSCS**: the Globus endpoint
- **Between CSCS filesystems**: the `xfer` partition, with `rclone` for anything large
- It lands on **`iopsstor` scratch**, because you are about to read it in random order

</div>
<div class="card">

### Where we are

Raw data on scratch. No environment, no model, nothing trained.

Everything from here is what you do with it.

</div>
</div>

<!--
- Step one is already done, because we just spent a module on it.
- From outside, Globus. Between our own filesystems, the xfer partition, and rclone if it is large.
- It lands on iopsstor scratch, because the next thing you do is read it in random order.
- So: raw data on scratch, nothing else. That is the starting point.
- Next: And the first useful thing is not training.
DOCS: docs.cscs.ch/storage/transfer/
-->
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
- You have just landed raw data on scratch. You do not have a model yet.
- The inference resource from module 1 is already useful here, and this is the step most people skip.
- Vetting: run the raw data past a model to classify it, filter it, find what is broken.
- Building the training set: rewriting, synthesising, labelling.
- And writing the job scripts themselves — you can point a coding agent at the same endpoint.
- It is the same API and the same project credit. Nothing new to request.
- Next: Now set up a place to work.
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
- If the work has to repeat, drive it over HTTP instead of by hand.
- One endpoint per platform. Yours is the ml one.
- List files, make directories, submit and cancel Slurm jobs, move data.
- Authentication is a client ID and secret exchanged for a five-minute token. No passwords in a pipeline.
- That is what the service accounts from module 1 are for.
- Next: Or a notebook, if you would rather not script it.
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
- If you would rather not think about sbatch, this is the way in.
- One URL per cluster. Clariden is jupyter dash clariden dot cscs dot ch.
- You get a form. Node type, how many, wall time, which project pays, and which environment — the same uenv or container we come to in a moment.
- Two things people get wrong. It runs on a compute node, so leaving it open costs credit — close it when you stop. And "disk I/O error" when saving a notebook almost always means you are out of quota, not that Jupyter is broken.
- Next: And for automation, there is an API.
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
- Third way in, and the one fewest of you will have seen.
- A browser pointed at the cluster. Nothing to install, and no agent running as you on the cluster.
- The dashboard shows cluster health, and it will refuse to submit to a degraded cluster. That alone saves a failed overnight run.
- Jobs: list, filter, submit, read the logs.
- The feature I would highlight is the shareable per-job URL. It replaces the screenshot-in-Slack workflow that most debugging conversations start with.
- Look at CARD.
- It runs on FirecREST, and that is the useful part: anything the console can do, your script can do, because it is the same API.
- Client ID and secret for five-minute tokens. No passwords in a pipeline. That is what the service accounts from module 1 are for.
- We have five more slides on this in backup if the discussion wants them.
- Next: One last thing, and it does not involve a cluster at all.
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
- Two supported mechanisms. People ask which one is correct. Both are.
- A uenv is a CSCS-built environment, one Squashfs file containing the software and its modules.
- The Container Engine runs your job inside a container you describe with a small file.
- For PyTorch specifically, the docs recommend the container route, and that is what most of you will use.
- The honest difference: uenv is built for Alps; containers let you use portable environments built by third parties.
- Next: uenv first, because it is three commands.
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
- Four commands, and note the shape: an image is always name, version and tag.
- Find shows you what exists. Pull downloads it. Start drops you into a shell inside it.
- If you want to run one thing and get out, uenv run.
- The whole environment is one file. That is why it starts fast on a parallel filesystem.
- And yes, PyTorch is available this way, several versions, for the Grace-Hopper nodes.
- Next: Now the container route, which is the one the PyTorch docs recommend.
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
- This is the entire concept. A small TOML file names an image, says what to mount, says where to start.
- You give it a name, and then everywhere you would have run something, you add one flag.
- srun dash dash environment. That is it. It works in interactive jobs and in batch scripts identically.
- The mounts line is the one people forget. Inside the container, Alps filesystems are not there unless you say so.
- Next: A realistic one, for PyTorch.
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
- This is a realistic EDF to run generic PyTorch tasks.
- Top line: Enter the image by registry reference. The Container Engine downloads and caches it.
- The mounts bring in both scratch filesystems.
- Say what the EDF buys you: it separates what you want from how the container is managed, and the container description from the commands in your job script.
- Now the part that is specific to this machine, and the reason a laptop container is not enough.
- Look at ANNOTATIONS BLOCK.
- Annotations are arbitrary metadata for the container. We use them to request custom features to the Container Engine.
- The AWS OFI NCCL hook connects NCCL to the Slingshot network through libfabric.
- If you leave it out, multi-node training still works. It is just quietly, badly slow.
- That is the single most common performance bug we see.
- There are more annotations and more features. The documentation lists them.
THE [env] BLOCK, only if asked:
- OMP_NUM_THREADS aligns with the number of cores of Grace CPU
- NCCL_DEBUG=INFO so you can see what the network actually did. EDF supports comments: comment out for cleaner outputs.
- The full block is on the PyTorch documentation page. Do not read it out.
- Next: Where the images come from.
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
- Three things to know about images.
- Alps Extended Images: curated by CSCS and tuned for this machine. Start here if one fits.
- NGC as the all-rounder. PyTorch is already there, already built well for these GPUs.
- And you can build your own on Alps, with Podman, on the right architecture.
- Let me read the red bar.
- Build on top of something that works. Starting from a bare Ubuntu on this machine is a huge effort (CUDA, DL libs, PyTorch, network...).
- Next: The mistakes we see.
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
- One script. It is short on purpose.
- The account flag is how Slurm knows which project pays. It is not optional.
- This is the line that connects back to module 1: every job here draws down the project's credit.
- Three partitions. Debug for quick turnaround, two nodes, thirty minutes. Normal for real work. Xfer for data, which module 2 covered.
- And the srun line carries the environment flag from the container slides. That is the whole stack in one script.
- Next: How to ask for GH200 nodes properly.
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
- A Grace-Hopper node is four GPUs and four CPU sockets. Ask for it that way.
- Four tasks per node, one GPU per task. That is the shape nearly every ML job wants.
- If you are running several job steps on the same node, take it exclusive.
- The reason to care is on the right: getting this wrong is not an error message. It is a slow job that still costs you the full node hours.
- Next: Which brings us to efficiency.
DOCS: docs.cscs.ch/running/slurm/
-->

---
<div class="audience">PIs and deputies</div>

# You are billed for the node, not for the work

<!-- PLACEHOLDER — module 3 owner: this needs a real efficiency example or a tool name. -->

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
- You are billed for the node you reserved, not for the work you did on it.
- If your GPUs sit at thirty per cent, seventy per cent of that credit bought nothing.
- Remember module 1 asked you for an expected efficiency in the proposal. This is where that promise is kept or not.
- The habit that fixes it: measure one run properly before you scale it to a hundred.
- Look at CARD.
- And for the PIs specifically. Spending the budget on schedule while achieving nothing is worse than under-spending, because it is invisible.
- Next: You do not have to do all of this from a terminal.
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
- Four mistakes, all of which we see regularly.
- No NCCL hook, covered already, the big one.
- Dataset on capstor instead of iopsstor. Module 2's mistake showing up here as a slow job.
- Image sitting on home, where you have 50 gigabytes.
- Rebuilding the image on every job instead of importing once.
- On the right, the habit that prevents most of this: commit the EDF next to your code.
- Then your environment is reviewed like code, and somebody else can reproduce your run.
- Next: Where to read more.
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
- Next: Post-training.
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
- Next: One last thing, and it is not on Alps.
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
- Thirty seconds, because it comes up every time.
- There is a dedicated Kubernetes cluster for the Swiss AI Initiative.
- It is not the general Alps Kubernetes service — the documentation is explicit that that one is only for specific partners and is not available to normal users on Alps.
- Access is arranged through Imanol, not through the portal.
- That is all we are saying about it today. If you want it, come and find us.
- Next: Where to read more.
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
- I will not read this slide out.

- Everything in the last forty minutes is on one of these pages.
- If you open one link tonight, make it the tutorials. They are complete worked examples.
- Next: hand over to the wrap-up.
-->
