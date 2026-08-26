---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 0 · ~5 min</span>

# Alps, the ML Platform, and the next hour

Where your project runs, and what we are about to walk through.

<!--
START AT T+00:00. Check the presenter timer now.
CUT IF LATE: Cut the Alps/vClusters slide. Say it in one sentence over the two-cluster slide.

- Welcome. This is the Alps technical training.
- About an hour from us, then open discussion.
- Two of us from CSCS. I take the first part, Fawzi the worked example.
- We cannot teach you everything today.
- We want to leave you a map, so you know where to look next.
- Next: one practical thing before we start.
-->

---
<div class="audience all">Everyone</div>

# Today is a maintenance day

Expect limitations. Nothing in this hour depends on the machine being up.

<div class="cols">
<div>

- Systems may be **unavailable or degraded** today
- If you try to log in during the session, it may not work
- That is expected. It is **not** your SSH key

</div>
<div class="card">

### So we planned around it

Everything you will see is a **screenshot or a recording**. There are no live demos.

Ask your question anyway — we will answer it, and show you for real afterwards.

</div>
</div>

<div class="accent">

Try the commands tomorrow, not now. They are all on the handout.

</div>

<!--
- Today is a maintenance day. Systems may be down or slow.
- If your login fails during this hour, that is expected. Not your key, not you.
- So no live demos. Everything you see is a screenshot.
- Conference wifi and MFA on stage are a bad pair anyway.
- The upside: this maintenance is what delivers the new datacache area. Module 2 shows it.
- Ask questions as they come. We can show you for real afterwards, or at the User Day on Friday.
- Next: what is the machine you are all using?
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/alps/' -->
<div class="audience all">Everyone</div>

# Alps is one machine with many faces

You do not get "an Alps account". You get a project on a **platform**.

<div class="cols">
<div>

### The infrastructure

**Alps** is a general-purpose compute and data research infrastructure, open to researchers in Switzerland and beyond.

It is **multi-tenant**: it creates versatile clusters, **vClusters**, tailored to different communities.

</div>
<div class="card">

### Three platforms

- **Machine Learning Platform** — you are here
- HPC Platform
- Climate and Weather Platform

Each has its own clusters, its own software stack and its own policies.

</div>
</div>

<div class="accent">

Everything in this hour is the **ML Platform**. Other platforms do some of it differently.

</div>

<!--
- Alps is one physical machine with many logical clusters.
- The logical ones are called vClusters, tailored per community.
- On top of them CSCS runs three platforms. You are on the Machine Learning Platform.
- This matters when you search the docs: the answer often depends on the platform.
- Everything today is the ML Platform.
- Next: so what is on the ML Platform?
DOCS: docs.cscs.ch/alps/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience all">Everyone</div>

# Two clusters, and they are not interchangeable

The ML Platform provides compute, storage and expertise to the machine learning communities on Alps.

<div class="cols">
<div class="card">

### Clariden

**Grace-Hopper GH200.** The main system.

This is where **production runs** go.

</div>
<div class="card">

### Bristen

**A100 nodes.** Smaller.

Data processing, development and x86 workloads. **Test and development**, best effort.

</div>
</div>

<div class="accent">

"It is **not** a cluster where to do the bulk of your computation." — the Bristen documentation, about Bristen.

</div>

<!--
- The ML Platform gives you compute, storage and expertise.
- Two clusters, and people mix them up.
- Clariden is GH200. The main system. Production runs go here.
- Bristen is A100 and smaller. Data processing, development, x86 work.
- Bristen is best effort. Read the red bar out loud — that is the docs talking.
- Next: what we cover in the next hour.
DOCS: docs.cscs.ch/platforms/mlp/ · /clusters/clariden/ · /clusters/bristen/
-->

---
<div class="audience all">Everyone</div>

# One project, from nothing to a trained model

One project, from "we need compute" to a model that is trained and being used.

<div class="cols">
<div>

| # | Module | Time |
|---|---|---|
| **1** | Project and access | ~10 min |
| **2** | Data and storage | ~10 min |
| **3** | A concrete ML use case | ~30 min |
| **4** | Wrap-up | ~2 min |
| | **Open discussion** | **what is left** |

</div>
<div class="card">

### How to follow this

**Interrupt us.** Ask as the question occurs to you, not at the end.

Each slide says in the top right corner who it is for — **PIs and deputies**, or **Everyone**.

There is a **handout**. Every command is on it.

</div>
</div>

<!--
- One story: from "we need compute" to a model people are using.
- Four modules, in order. The third is the centre: one worked example.
- The times are rough. Module three can run to forty minutes.
- The discussion takes what is left, and that is the part we want most.
- Please interrupt us. Say it when it happens, not at the end.
- We would rather answer three good questions and drop a slide.
- Every slide says in the corner who it is for.
- There is a handout with every command on it, so do not type.
- Next: how do you get a project at all?
-->

---
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Start here

- **Alps** — docs.cscs.ch/alps/
- **Machine Learning Platform** — docs.cscs.ch/platforms/mlp/
- **Clariden** — docs.cscs.ch/clusters/clariden/
- **Bristen** — docs.cscs.ch/clusters/bristen/

</div>
<div class="card dark">

### If you remember one thing

`docs.cscs.ch` is the answer to almost every question in this hour.

The deck is a **signpost**. The documentation is the destination.

</div>
</div>

<!--
- Four links, all on docs.cscs.ch. I will not read them out.
- This deck is a signpost, not a manual.
- Next: hand over to module 1.
-->
