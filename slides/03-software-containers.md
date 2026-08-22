---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!--
DRAFT — owner TBD. Scaffolding, not a finished module. Budget: 15 minutes, the largest
in the session, so there is deliberate room left for the owner's own material —
especially a worked example they have actually run.
-->

<!-- _class: divider -->

<span class="tag">Module 3 · 15 min</span>

# Software and containers

Ben's data is in the right place. Now he needs an environment that can read it.

<!--
START AT T+30:00. Check the presenter timer now.
CUT IF LATE: Cut "Four ways to make this slow". Keep only the NCCL hook point, said over the EDF slide.
SAY:
- Ben has data on the right filesystem. Now he needs PyTorch.
- There is no "module load pytorch" here. There are two supported ways, and they are different in kind.
- This is the longest module of the hour, because this is where most of your time will actually go.
NEXT: The two ways.
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/uenv/' -->
<div class="audience all">Everyone</div>

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
- The honest difference: uenv is focused on Alps, containers allow to use portable environments built by 3rd parties.
NEXT: uenv first, because it is three commands.
DOCS: docs.cscs.ch/software/uenv/ · docs.cscs.ch/software/container-engine/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/software/uenv/' -->
<div class="audience all">Everyone</div>

# A uenv is three commands

Find, pull, start.

```bash
uenv image find                 # what exists
uenv image pull prgenv-gnu      # download it
uenv start prgenv-gnu           # interactive session inside it
uenv run  prgenv-gnu -- ./my.sh # or run one command and exit
```

<div class="cols">
<div>

- `uenv image ls` — what you have downloaded
- `uenv image inspect` — details
- Each uenv is a **single Squashfs file**

</div>
<div class="card">

### PyTorch is available as a uenv

Versions include **v2.9.1**, **v2.8.0**, **v2.6.0**, for **GH200** nodes on Clariden, Daint and Santis.

</div>
</div>

<!--
SAY:
- Three commands. Find, pull, start.
- Find shows you what exists. Pull downloads it. Start drops you into a shell inside it.
- If you want to run one thing and get out, uenv run.
- The whole environment is one file. That is why it starts fast on a parallel filesystem.
- And yes, PyTorch is available this way, several versions, for the Grace-Hopper nodes.
NEXT: Now the container route, which is the one the PyTorch docs recommend.
DOCS: docs.cscs.ch/software/uenv/
-->

<!-- TODO(verify): the uenv example on docs.cscs.ch uses NAMD, not prgenv-gnu. Module 3
owner: replace the image name above with one you have actually pulled on Clariden, and
confirm the PyTorch uenv names and versions against docs.cscs.ch/software/ml/pytorch/. -->

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
<div>
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

- Declaratively expresses the characteristics of your job environment. The Container Engine takes care of instantiating it.
- Separates the *description* of the container (reusable) from the *commands* you want to run inside it.

</div>
<div class="card">

### The annotations introduce HPC features

The **aws-ofi-nccl** hook is what makes multi-node NCCL use the Slingshot network properly.

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
- Highlight the abstractions enabled by the EDF: user intent from container tool management; container description from job script command
- Now the part that is specific to this machine, and the reason a laptop container is not enough.
POINT AT THE ANNOTATIONS BLOCK:
- Annotations are arbitrary metadata for the container. We use them to request custom features to the Container Engine.
- The AWS OFI NCCL hook connects NCCL to the Slingshot network through libfabric.
- If you leave it out, multi-node training still works. It is just quietly, badly slow.
- That is the single most common performance bug we see.
- Refer to documentation for more annotations and features
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

<!-- PLACEHOLDER — module 3 owner: this is the slide most in need of your real workflow. -->

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
- Alps extended images
- NGC as the all-arounder. PyTorch is already there, already built well for these GPUs.
- Point out possibility to build on Alps.
READ THE RED BAR:
- Build on top of something that works. Starting from a bare Ubuntu on this machine is a huge effort (CUDA, DL libs, PyTorch, network...).
NEXT: The mistakes we see.
DOCS: docs.cscs.ch/software/ml/pytorch/ · docs.cscs.ch/software/container-engine/
-->

<!-- TODO(verify): the exact import command (enroot / podman / the CSCS-recommended
route) was not captured and is NOT stated on the container-engine overview page. Module 3
owner: find it, quote it verbatim, and put it on this slide. Without a real command this
slide is advice, not instruction. -->

---
<div class="audience all">Everyone</div>

# Four ways to make this slow

<!-- PLACEHOLDER — module 3 owner: replace with the four you actually see in tickets. -->

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
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Software

- **uenv** — docs.cscs.ch/software/uenv/
- **Container Engine** — docs.cscs.ch/software/container-engine/
- **Building container images on Alps** - docs.cscs.ch/build-install/containers/
- **ML software stack** — docs.cscs.ch/software/ml/
- **PyTorch** — docs.cscs.ch/software/ml/pytorch/

### Worked examples

- **ML tutorials** — docs.cscs.ch/tutorials/ml/

</div>
<div class="card dark">

### If you remember one thing

The **EDF** is your environment, and it can be just one line.

Commit it next to your code.

### And one flag

`srun --environment=<name>`

</div>
</div>

<!--
Do not read this slide out loud.
SAY only:
- The EDF is your environment. Commit it next to your code.
- One flag to use it: srun dash dash environment.
- The tutorials link is the one to open tonight. It has complete working examples.
NEXT: hand over to module 4. Ben has data and an environment. Now he has to run it at scale.
-->
