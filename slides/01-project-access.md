---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 1 · 14 min</span>

# Project lifecycle and access

Getting a project, adding your team, watching the budget, and getting a shell.

<div class="split">

**First half — PIs and deputies.** Getting a project, the team, the budget.
**Second half — everyone.** Account, MFA, keys, logging in.

</div>

<!--
START AT T+05:00. Check the presenter timer now.
CUT IF LATE: Cut "What this module deliberately skipped", and "What a Swiss AI project comes with" if you must — the inference slide carries the point.

- This module is fourteen minutes. It is the plumbing part.
- The interesting part of the hour is modules 2 and 3.
- The first half is for PIs and deputy PIs: getting a project, adding people, watching the budget.
- The second half is for everybody who has to log in: account, MFA, keys, the jump host.
- Each slide says in the top right corner which one it is.
- So if the first half is not your job, you have a few minutes to read your email. I will not be offended.
- Every command I show is on the handout, so do not type. Just watch.
- And please interrupt me. Ask when the question comes to you, not at the end.
- Let us start at the beginning. How do you get a project at all?
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience">PIs and deputies</div>

# Small and large are two different processes

You choose which one to apply for. The Swiss AI Initiative decides. CSCS opens the project and runs it.

<div class="cols-wide">
<div>

|  | Small | Large |
|---|---|---|
| Typical budget | up to 32,000 GPUh | 500,000 GPUh and up |
| Duration | 6 months | 12 months |
| Review | rolling | two calls a year |
| Start | first day of the next month | 1 January or 1 July |
| Storage | 1 TB, 1M inodes by default | must be in the proposal |

</div>
<div class="card">

### Before asking for a large one

- GPU hours you **measured**
- The efficiency you expect
- The **data footprint**, and how long it stays

A weak large proposal is usually **made smaller**, not rejected.

</div>
</div>

<div class="accent">

The 4th call for large projects is open right now — **3 August to 14 September 2026**. `swiss-ai.org/compute-grants`

</div>

<!--
- First, who does what. You choose small or large, and you apply to the Swiss AI Initiative, not to us.
- They decide. We open the project and run it.
- Small: up to thirty-two thousand GPU hours, six months, reviewed all year. You can start next month.
- Large: five hundred thousand and up, twelve months. It starts only on the first of January or the first of July.
- Miss a call and you wait six months.
- The storage row is the one people forget. Small gets a terabyte by default. Large gets none — you state it in the proposal.
- Bring three things to a large proposal: GPU hours you measured, the efficiency you expect, and your data footprint.
- And a weak large proposal is usually made smaller, not rejected.
- The fourth call closes on the fourteenth of September. That is about three weeks.
- Next: you have a project. What is an account?
DOCS: docs.cscs.ch/platforms/mlp/ · swiss-ai.org/compute-grants
-->

<!-- TODO(verify): the small/large policy numbers come from the MLP policies page,
which is still a docs preview at cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/
and is being merged into docs.cscs.ch in the coming days. Swap the footer link and the
"Where to read more" entry to the final docs.cscs.ch URL before the session, and
re-check the numbers at that point. The call dates come from swiss-ai.org, not from
CSCS — re-check them the week before, they change per call. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience all">Everyone</div>

# Your account lives as long as one project does

An account can belong to several projects. It closes only when the last one closes.

<div class="cols">
<div>

### Three roles

- **Project administrator** — the PI
- **Project manager** — the deputy PI
- **Project member** — everyone else

Administrators and managers **invite people** and **assign roles**.

</div>
<div class="card">

### One account, many projects

- Your **email address** identifies you — one address, one account
- **Institutional addresses only** — and always the same one
- Open while **at least one** project is open
- An end date stops the **compute**, not the project — **90 days** of grace follow
- A later invitation **re-enables** the same account

</div>
</div>

<!--
- Three words the portal uses. Project administrator is the PI, project manager is the deputy, project member is everyone else.
- Only the first two invite people and set roles.
- Now the important part, and I will say it slowly.
- Your email address is your identity. One address, one account, and institutional addresses only.
- Always use the same one. A different address gives you a second account, not access to your old one.
- An account can belong to several projects, and stays open while one of them is open.
- The end date stops your compute, not the project. It stays active ninety more days for your data.
- Then it closes, and your account closes with the last of your projects.
- Good news: a later invitation switches the same account back on.
- Next: let us open the portal.
DOCS: docs.cscs.ch/accounts/
-->

<!-- TODO(verify): docs.cscs.ch/accounts/ backs only the middle of this card — "accounts
are bound to projects, and accounts will be closed with the project unless the account
is also part of another open project". The two ends do not appear there: that the email
address is the unique identity, and that a later invitation re-enables the same account
rather than creating a new one. Both come from Andrea as ML Platform service manager.
Confirm, then get them written into the docs page. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience">PIs and deputies</div>

# The portal is where the project lives

`portal.cscs.ch` — your team, your resources, and what they have spent.

<div class="cols-narrow">
<div>

- Log in with your CSCS account and MFA. Pick your **organisation**, then the **project**
- **Team** — everyone on the project and their role
- **Invitations** — where you add people
- **Resources** — what the project was granted, and where a PI adds an inference resource
- **Usage** — what has been spent, project-wide and inside each resource

</div>
<div class="shot">

**SCREENSHOT**

`portal.cscs.ch` — project page with the Team tab open, roles column visible.
Anonymise real names.

</div>
</div>

<!--
- If you are a PI and you have never opened this, the next few minutes are the ones to stay awake for.
- This is a tour, not a tutorial. One sentence per step.
- Log in — the same login as every other CSCS web application — then pick your organisation and your project.
- Then four things, and most PIs have seen none of them.
- Team: everyone on the project and what they can do. That is the question you email us about most.
- Invitations: where you add people, and we will do that on the next slide.
- Resources: what the project was actually granted. This is also where you add an inference resource.
- Usage: what has been spent, for the project as a whole and inside each resource. There is a slide on that shortly.
- Look at the roles column here.
- Next: your team is listed, but the new student is not on it yet. Let us add them.
DOCS: docs.cscs.ch/accounts/ (portal section)
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience">PIs and deputies</div>

# Adding someone takes one email address

One email address, or a CSV for a whole cohort. Either way the invitation carries the role.

<div class="cols">
<div>

### One person

Green **Invite Users** button, enter the email address, assign the role.

### A whole group

Upload a CSV with three columns:

```
Email,Role,Project
CragAlvarado@example.com,Project member,prj02
```

</div>
<div class="card dark">

### What they receive

- An email invitation
- **Already has a CSCS account** → accepts via the login page
- **New to CSCS** → follows the account creation procedure

</div>
</div>

<!--
- Two ways to do this, and both are fast.
- One person: the green Invite Users button, an email address, a role.
- A group: upload a CSV file. Three columns, exactly this header.
- That is what you want when ten students arrive in September.
- On the right is what they receive.
- If they already have a CSCS account, they log in and accept.
- If they are new, the invitation sends them to account creation, which is coming up.
- Someone will ask whether you can change a role afterwards.
- If the network is behaving, open the Team tab and show them.
- Do not promise anything you have not clicked yourself.
DOCS: docs.cscs.ch/accounts/ (portal section)
-->

<!-- TODO(verify): whether, and by whom, an existing member's role can be changed after
the invitation is NOT documented — docs.cscs.ch/accounts/waldur/ covers only the
invitation flow. Andrea's expectation is that a PI and a deputy PI can both do it from
the Team tab. Click it in the portal, then either put one line on this slide or get it
into the docs page. Until then the slide claims nothing either way. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience">PIs and deputies</div>

# What a Swiss AI project comes with

Compute and storage arrive with the project. One more resource is opt-in.

<div class="cols">
<div>

### By default

- **Compute** on **Clariden** and **Bristen**
- **Project storage** — `/store`, shared by the whole project

### On request

- **Inference** — an API resource the **PI or deputy** adds in the portal

</div>
<div class="card">

### They all draw on one credit

There is no separate inference budget you can overspend independently.

It is **one project credit**, and everything spends it.

</div>
</div>

<div class="accent">

The next slide is the one nobody expects: you can use a model without running a job at all.

</div>

<!--
SAY:
- A quick inventory, because most people do not know what they already have.
- By default your project gets compute on both clusters, Clariden and Bristen.
- And it gets project storage, the store area, which the whole project shares.
- Your home directory and your scratch are yours, not the project's. Module 2 covers those.
- One thing is opt-in: an inference resource. The PI or the deputy adds it in the portal.
- These are not separate pots. There is one project credit and everything spends it.
- That last one deserves its own slide, and it is next.
DOCS: docs.cscs.ch/platforms/mlp/
-->
---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/services/inference/api/' -->
<div class="audience all">Everyone</div>

# You can use a model without training one

`api.inference.cscs.ch/v1` — **new since 24 July**, OpenAI and Anthropic compatible. Change a base URL and your code works.

<div class="cols-wide">
<div class="code-sm">

- Open-weight models, served and managed for you — **Apertus 70B** and **8B**, among others
- The **PI or deputy PI** creates the inference resource in `portal.cscs.ch`; then **any project member** can create API keys
- Each key can carry a token budget — but **any member can make another key**

```bash
curl -X POST https://api.inference.cscs.ch/v1/chat/completions \
  -H "Authorization: Bearer $CSCS_INFERENCE_API_KEY" \
  -d '{"model": "swiss-ai/Apertus-70B-Instruct-2509", "messages": [...]}'
```

</div>
<div class="card">

### It is not free, it is yours

> "The credit for the inference resource is taken from your project's credit."

**There is no project-level cap.** To get one, the PI opens a Service Desk ticket.

</div>
</div>

<div class="accent">

The docs also show how to point **Claude Code** and **OpenCode** at it.

</div>

<!--
- This is new. It has been there since the twenty-fourth of July.
- A managed inference API. Open-weight models, served for you.
- It is OpenAI and Anthropic compatible, so change the base URL and your code works.
- And it serves Apertus, which is your own model.
- The PI or the deputy adds the resource in the portal. Then any member creates API keys.
- Let me read the quotation. The credit comes out of your project credit.
- And a budget on one key does not cap the project, because any member can make another key.
- Today there is no project-level cap. If you want one, that is a Service Desk ticket.
- Look at the curl. Three lines. If you know the OpenAI API, you already know this.
- Next: how you see what you have spent.
DOCS: docs.cscs.ch/services/inference/api/
-->

<!-- TODO(verify): model names and pricing move. Re-check the model list and the
"Available models and pricing" section the week before the session, and confirm the
Apertus tag swiss-ai/Apertus-70B-Instruct-2509 is still current if you quote it. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience all">Everyone</div>

# Check the consumption monthly, not in the last week

The portal shows what the project was granted and what it has burned.

<div class="cols-narrow">
<div>

- **Everyone on the project** sees the project total — not just the PI
- Per-user usage sits inside the detail of each resource
- There is **no per-user total** across the project

<div class="accent">

<span class="tag">In progress</span>
We are actively improving these views — compute, storage, and the new inference resources.

</div>

</div>
<div class="shot">

**SCREENSHOT**

`portal.cscs.ch` — the project resources view. Granted vs used, the per-user breakdown,
**and** expected, minimal, grace and the end date. Annotated with the same words as the
next slide.

</div>
</div>

<!--
- First let me correct something people assume.
- This view is not only for the PI. Every project member can see the total for the project.
- Open one resource and you see the usage per user inside it.
- What you cannot see is one total per user for the whole project. If you want that number you add it up yourself.
- Now the red bar, and I mean it as a promise rather than an excuse.
- We know these views are not good enough yet. We are working on them now.
- That covers compute, storage, and the new inference resources.
- If you have a request, raise it in the discussion at the end.
- Next: why every month, and not just at the end.
DOCS: docs.cscs.ch/accounts/ (portal section)
-->

<!-- TODO(verify): the consumption view is not documented on
docs.cscs.ch/accounts/waldur/. The visibility rules above come from Andrea as ML
Platform service manager, not from the docs — see notes/sources.md. Confirm the exact
tab name when capturing the screenshot, and consider getting this written into the
docs page. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience">PIs and deputies</div>

# Spend it linearly, or you lose it

Every project gets a credit in GPU hours, spent as your jobs run. Each month has an expected amount, and a minimal you must not fall below.

<!-- The <div> wrapper is load-bearing: CommonMark only treats a whitelisted set of tag
     names as HTML blocks, and <svg> is not one of them, so an unwrapped diagram is
     parsed as inline HTML and its text nodes are flattened into a paragraph. Keep the
     whole block free of blank lines, which would close the HTML block early. -->
<div class="diagram">
<svg viewBox="0 0 1160 320" width="100%" role="img"
     aria-label="Top: three example months of usage as bars against two thresholds, an expected line and a minimal line below it separated by the grace. Above expected is fine, in between rolls over, below the minimal the gap is lost. Bottom: the project timeline, 6 or 12 months, then compute stops, then a 90-day grace period in which the project stays active for data retrieval only, then it closes.">
  <g font-family="Inter, sans-serif">
    <!-- ── row 1: the monthly rule ───────────────────────────────────────── -->
    <text x="90" y="20" font-size="13" font-weight="600" fill="#888888" letter-spacing="0.6">IN ANY GIVEN MONTH</text>
    <!-- your usage -->
    <rect x="140" y="52"  width="100" height="128" fill="#9A9AA0"/>
    <rect x="320" y="90"  width="100" height="90"  fill="#9A9AA0"/>
    <rect x="500" y="148" width="100" height="32"  fill="#9A9AA0"/>
    <!-- the credit burned by falling short -->
    <rect x="500" y="112" width="100" height="36" fill="#F3E0E1" stroke="#D61F26" stroke-width="1.5" stroke-dasharray="4 3"/>
    <text x="550" y="136" font-size="13" font-weight="600" fill="#D61F26" text-anchor="middle">lost</text>
    <!-- thresholds -->
    <line x1="100" y1="70"  x2="800" y2="70"  stroke="#D61F26" stroke-width="2"   stroke-dasharray="7 5"/>
    <line x1="100" y1="112" x2="800" y2="112" stroke="#D61F26" stroke-width="1.5" stroke-dasharray="3 4"/>
    <line x1="100" y1="180" x2="820" y2="180" stroke="#E5E5E5" stroke-width="2"/>
    <text x="810" y="75"  font-size="15" font-weight="600" fill="#D61F26">expected</text>
    <text x="810" y="117" font-size="15" font-weight="600" fill="#D61F26">minimal</text>
    <!-- the grace between the two -->
    <line x1="990" y1="70" x2="990" y2="112" stroke="#D61F26" stroke-width="1.5"/>
    <line x1="984" y1="70" x2="996" y2="70"  stroke="#D61F26" stroke-width="1.5"/>
    <line x1="984" y1="112" x2="996" y2="112" stroke="#D61F26" stroke-width="1.5"/>
    <text x="1006" y="86"  font-size="13" font-weight="600" fill="#D61F26">grace</text>
    <text x="1006" y="104" font-size="12" fill="#555555">15–50%, by budget size</text>
    <!-- what each case means -->
    <g text-anchor="middle" fill="#1A1A1A">
      <text x="190" y="202" font-size="14" font-weight="600">you go faster</text>
      <text x="190" y="220" font-size="12" fill="#555555">fine — lower priority while ahead</text>
      <text x="370" y="202" font-size="14" font-weight="600">you go slower</text>
      <text x="370" y="220" font-size="12" fill="#555555">the rest rolls over</text>
      <text x="550" y="202" font-size="14" font-weight="600">you fall below</text>
      <text x="550" y="220" font-size="12" fill="#555555">that credit is gone</text>
    </g>
    <!-- ── row 2: the project timeline ───────────────────────────────────── -->
    <line x1="90" y1="240" x2="1140" y2="240" stroke="#F0F0F0" stroke-width="1"/>
    <text x="90" y="262" font-size="13" font-weight="600" fill="#888888" letter-spacing="0.6">OVER THE WHOLE PROJECT</text>
    <line x1="380" y1="288" x2="870" y2="288" stroke="#9A9AA0" stroke-width="5"/>
    <line x1="870" y1="288" x2="1060" y2="288" stroke="#D61F26" stroke-width="5"/>
    <line x1="870" y1="274" x2="870" y2="302" stroke="#1A1A1A" stroke-width="2"/>
    <line x1="1060" y1="278" x2="1060" y2="298" stroke="#1A1A1A" stroke-width="2"/>
    <text x="625" y="310" font-size="13" fill="#555555" text-anchor="middle">6 or 12 months</text>
    <text x="870" y="264" font-size="14" font-weight="600" text-anchor="middle">compute stops</text>
    <text x="965" y="310" font-size="13" font-weight="600" fill="#D61F26" text-anchor="middle">90 days grace — data only</text>
    <text x="1074" y="293" font-size="13" fill="#555555">closes</text>
  </g>
</svg>
</div>

<div class="accent">

Out of credit before the end? The `low` partition, capped at two months of your budget.
All the rules: **docs.cscs.ch/platforms/mlp/**

</div>

<!--
- This is the most useful slide for a PI, so I will not rush it.
- Your project has a credit in GPU hours. You spend it as your jobs run, roughly evenly, month by month.
- Every month has two numbers. Expected is what you should use. Minimal is that minus a grace of fifteen to fifty per cent, depending on your budget size.
- Left bar: you used more than expected. That is fine, you just run at lower priority while you are ahead.
- Middle: you used less but stayed above the minimal, so the rest rolls over.
- Right: you fell below it. The red box is credit you lost, and it does not come back.
- Now the timeline. Six or twelve months, then the end date stops your compute.
- The project stays active ninety more days, for data only. Then it closes.
- Out of credit early? The low partition, about two months of your budget.
- Every number here is on that one page. Take a photo of it.
- Next: that is the project. The rest is getting in.
DOCS: docs.cscs.ch/platforms/mlp/policies/
-->

<!-- TODO(verify): every number on this slide — the 15-50% grace, the two-month cap on
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
makes, so it is worth getting written down — see notes/docs-gaps.md. -->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/account-create/' -->
<div class="audience all">Everyone</div>

# No MFA means no SSH. There is no way around it

New accounts are usually opened within 48 hours — plan for it, do not do this the night before.

<div class="cols">
<div>

### Creating the account

- Scanned ID or passport
- **Institutional** email address
- Correct personal details
- Usually open within **48 hours**

</div>
<div class="card">

### Enrolling MFA

Log in to any CSCS web application, enter the code sent by email, scan the QR code, type the six-digit code.

Google Authenticator and FreeOTP are tested; any TOTP app works.

</div>
</div>

<div class="accent">

"It is not possible to log in to CSCS systems using SSH without registering a device and creating certified SSH keys."

</div>

<!--
- Now the part for everybody who has to log in.
- To create an account you need three things: a scan of your ID or passport, an institutional email address, and correct personal details.
- It usually takes up to forty-eight hours, so do not do this the night before a deadline.
- Then MFA, and it is not optional.
- Log in to any CSCS web page, type the code you get by email, scan the QR code, type the six digits.
- Any TOTP app works. We have tested Google Authenticator and FreeOTP.
- Let me read the red bar, because it is the exact sentence from the documentation.
- This prevents our most common ticket: someone tries SSH, gets permission denied, and never set up MFA.
- Next: you have an account. Now you need a key.
DOCS: docs.cscs.ch/accounts/account-create/ · docs.cscs.ch/access/mfa/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/ssh/' -->
<div class="audience all">Everyone</div>

# Signed keys expire after one day

Generate the key pair once. Sign it every day. Five signatures per day, maximum.

```bash
brew install eth-cscs/tap/cscs-key       # macOS, Linux — or download the release binary
ssh-keygen -t ed25519 -f ~/.ssh/cscs-key # once, ever
cscs-key sign                            # every day: signs ~/.ssh/cscs-key
ssh-add -t 1d ~/.ssh/cscs-key            # load it into the agent
```

<div class="cols">
<div>

- Keys are valid for **1 day** by default
- You can create up to **5 keys per day**
- `cscs-key list` and `cscs-key revoke` if something leaks

</div>
<div class="card">

### No CLI? Use the dashboard

`user-account.cscs.ch` → SSH Keys → Sign Key. Paste the public key, download the certificate.

</div>
</div>

<!--
- People photograph this slide, so I will pause here.
- Install cscs-key. One time.
- Create the key pair. One time, ever.
- Sign it. That is the daily step.
- Load it into the agent.
- A signed key lasts one day, and you can sign five a day. That is enough for normal work.
- If a key leaks, use cscs-key list and cscs-key revoke.
- If you cannot install the CLI on your machine, use the web page. Same result.
- All of this is on the handout, so nobody needs to type now.
- Next: you have a signed key. Where do you send it?
DOCS: docs.cscs.ch/access/ssh/
-->

---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/access/ssh/' -->
<div class="audience all">Everyone</div>

# Everything goes through ela.cscs.ch

Ela is the jump host. You never connect to Clariden or Bristen directly.

<div class="cols">
<div>

```
Host ela
    HostName ela.cscs.ch
    User cscsusername
    IdentityFile ~/.ssh/cscs-key

Host clariden
    HostName clariden.alps.cscs.ch
    User cscsusername
    ProxyJump ela
    IdentityFile ~/.ssh/cscs-key
    IdentitiesOnly yes
```

</div>
<div class="stack">
<div class="card">

### Then it is just

`ssh clariden` — add `-A` to forward your agent.

</div>
<div class="card">

### Bristen needs its own block

Copy the `clariden` block, change the alias and `HostName`. Ela is shared.

</div>
<div class="card code-sm">

### Tunnel to a compute node

```bash
ssh -N \
  -J ${MYUSER}@ela.cscs.ch,${MYUSER}@${CLUSTER}.alps.cscs.ch \
  -L ${PORT}:localhost:${PORT} ${MYUSER}@${NODE}
```

</div>
</div>
</div>

<!--
- Write this into your SSH config once and you never think about the jump host again.
- Two entries: Ela, and the cluster behind it with ProxyJump.
- Replace cscsusername with your real username.
- After that you just type: ssh clariden.
- Be careful with the middle box, because people get this wrong.
- Bristen is not a hostname you swap in. It is a second Host block of its own, and the Ela entry stays shared.
- Clariden is where production runs go. Bristen is for test and development, best effort.
- The last box is the question we get at every drop-in: how do I reach a dashboard or a notebook running on a compute node?
- That is the tunnel. It is on the handout and in the documentation, so I will not explain it here.
- Next: two things I am deliberately not covering.
DOCS: docs.cscs.ch/access/ssh/ · /clusters/clariden/ · /clusters/bristen/
-->

---
# What this module deliberately skipped

<div class="cols">
<div>

- **Password and MFA troubleshooting** — service desk, they are fast
- **Legacy key management** — `sshservice.cscs.ch` was retired in May 2026

</div>
<div>

- **Service accounts** — for pipelines. Scoped to one project, grant access to all its resources. The **PI** requests one by Service Desk ticket
- **The HPC Console** — a pointer only, see module 4
- **Everything you do once you are in** — modules 2 and 3

</div>
</div>

<div class="accent">

You now have an account, a project and a shell. The rest of the hour is what you do with them.

</div>

<!--
- One line each, ten seconds in total.
- Password and MFA problems: write to the service desk. They are fast.
- The old SSH service was switched off in May 2026. Some of you still have it in your notes.
- Service accounts exist. They are for pipelines, and one belongs to one project.
- The PI asks for one with a Service Desk ticket. It is not a self-service button.
- The HPC Console: only a pointer here. Module 3 shows it properly.
- If someone asks about Kubernetes: it exists at CSCS, but the documentation says it is only for specific partners and is not available for normal users on Alps. Do not promise it.
- Let me read the red bar: you now have an account, a project and a shell.
- Next: you have a shell and an empty home directory, and the first question is where two terabytes of training data go.
-->

---
<!-- _class: ref -->

# Where to read more

<div class="cols">
<div>

### Getting a project

- **MLP project policies** — docs.cscs.ch/platforms/mlp/policies/
- **Applying** — swiss-ai.org/compute-grants
- **Accounts, projects and the portal** — docs.cscs.ch/accounts/

### Getting in

- **Creating an account** — docs.cscs.ch/accounts/account-create/
- **MFA** — docs.cscs.ch/access/mfa/
- **SSH, key signing, Ela** — docs.cscs.ch/access/ssh/

</div>
<div class="card dark">

### Keep these three

- `portal.cscs.ch` — the project
- `user-account.cscs.ch` — the account and the keys
- `docs.cscs.ch` — everything else

### Stuck?

- **service-desk@cscs.ch**
- The handout has every command from this module

</div>
</div>

<!--
- I will not read this slide out.
- Three addresses to remember.
- portal.cscs.ch for your project.
- user-account.cscs.ch for your account and your keys.
- docs.cscs.ch for everything else.
- And the service desk when none of those help.
- Everything here is on the handout too.
- Handing over now.
-->
