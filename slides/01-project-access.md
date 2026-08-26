---
marp: true
theme: cscs
paginate: true
footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch'
---

<!-- _class: divider -->

<span class="tag">Module 1 · ~10 min</span>

# Project lifecycle and access

Getting a project, adding your team, managing its resources, and watching the budget.

<div class="split">

**Mostly for PIs and deputies** — getting a project, the team, the resources, the budget.
**Everyone** — the two kinds of account, the inference API, what you have spent.

</div>

<!--
START AT T+05:00. Check the presenter timer now.
CUT IF LATE: Cut "What a Swiss AI project comes with" — the inference slide carries the point.

- Most of you know this part already, so this is a quick pass, not a tutorial.
- But a few things are new, and those interesting to know.
- In broad terms: how you get access to a project, how you manage the team and its resources, and how you watch the usage.
- There is something here for PIs and something for ordinary users.
- If something is new to you, or not clear, stop us and ask.
- Next: how do you get a project at all?
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
- You apply to the Swiss AI Initiative, not to us. They decide, we run the project.
- Small: up to thirty-two thousand GPU hours, six months, reviewed all year.
- Large: five hundred thousand and up, twelve months, and it starts only in January or July.
- Miss a call and you wait six months.
- The storage row is the one people forget.
- Bring three things to a large proposal: measured GPU hours, expected efficiency, data footprint.
- A weak large proposal could be made smaller.
- The next call closes on the fourteenth of September.
- Next: you have a project. What is an account?
DOCS: docs.cscs.ch/platforms/mlp/ · swiss-ai.org/compute-grants
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience all">Everyone</div>

# Your user account lives as long as one project does

There are two kinds of account here. This one is a **person**, and it can sit in several projects.

<div class="cols">
<div>

### Three roles

- **Project administrator** — the PI
- **Project manager** — the deputy PI
- **Project member** — everyone else

Administrators and managers **invite people** and **assign roles**.

</div>
<div class="card">

### One user account, many projects

- **Institutional address only**, and always the **same one**
- Open while **at least one** project is open
- It closes with the **last** project you are on
- A later invitation **re-enables** the same account

</div>
</div>

<div class="accent">

Your email address **is** your identity. A different address gives you a **second account**, not access to your first.

</div>

<!--
- I expect everyone here already has a user account at CSCS.
- There is a second kind of account too, and it comes on the next slide.
- A user account is a person. It is for the work you do yourself, with a username, a password and MFA.
- One account can be in several projects, and it stays active while at least one of them is active.
- Inside a project there are three roles.
- Administrator is the PI, manager is the deputy, member is everyone else.
- Only the first two invite people and set roles.
- Now the important part, slowly.
- Every account is identified by one email address, and that address is unique.
- So if you invite someone who already has an account, but on a different address, you create a second account for them.
- Always use the same address.
- Next: that account has a person behind it. There is a second kind without one.
DOCS: docs.cscs.ch/accounts/
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/account-create/' -->
<div class="audience all">Everyone</div>

# A service account runs the work you are not there for

Your own account is for the work you do yourself. Automation needs a different kind.

<div class="cols">
<div>

- A **user account** is a person — interactive work, and it can sit in several projects
- A **service account** runs a workload **on behalf of** a person — pipelines, scheduled jobs, anything unattended
- It is **bound to one project** and inherits its validity period — project ends, account closed
- Normally **run by the project team**, with a **shared team address** for its notifications

</div>
<div class="card">

### How to get one

Not enabled by default. The **PI** opens a Service Desk ticket explaining the use case: what it is for, expected usage, who is responsible, and for how long.

Once approved, a **Service Account** entry appears under **Team** in the portal — the tab we open next.

</div>
</div>

<div class="accent">

Its own username, and an **API key** instead of a password. No MFA — it does not log in like a person.

</div>

<!--
- A service account is another kind of account, and it is not a user account.
- It is there to run automatic workloads.
- Unlike a user account, it is bound to a single project and follows that project's lifecycle.
- It is normally used for a CI/CD pipeline, or an automation script.
- It is shared by the project team, on a shared team address.
- It is not available by default. The PI asks for it with a Service Desk ticket.
- Then a Service Account entry appears under Team in the portal.
- Authentication is different too. No password and no MFA, the way your own account works.
- It has its own username and an API key, and that key is what reaches the HPC resources.
- Next: let us open the portal.
DOCS: docs.cscs.ch/accounts/account-create/
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience">PIs and deputies</div>

# The portal is where the project lives

`portal.cscs.ch` — your team, your resources, and what they have spent.

<div class="cols-narrow">
<div>

- Log in with MFA, then pick your **organisation** and your **project**
- **Project dashboard** — the credit, and what it has spent
- **Resources** — what the project was granted, and where a PI adds **inference**
- **Team** — who is on the project. **Invitations** beside it takes one address, or a **CSV** for a whole cohort
- **Audit logs** — what changed, and who changed it

</div>
<div class="screenshot">

![The portal showing a project. A header card with the project name and its start and end dates, a row of four tabs — Project dashboard, Resources, Team, Audit logs — and the Team card open on Active, beside Invitations and Service accounts. The table lists each member with their username, their role in the project and a role expiration column.](../assets/screenshots/portal-team-tab.png)

</div>
</div>

<!--
- If you are a PI who has never opened this, stay awake for the next two minutes.
- Log in, then pick your organisation and your project.
- The header gives you the two dates that matter: start and end.
- Then four tabs, and most PIs have seen none of them.
- Project dashboard: the credit and what you spent. A slide on that shortly.
- Resources: what you were granted, and where you add inference.
- Team: who is on the project. Look at the roles column.
- Inviting is one address and a role, or a CSV when ten students arrive.
- New to CSCS? The invitation sends them to account creation.
- Audit logs: what changed, and who changed it.
- Next: what does the project actually give them?
DOCS: docs.cscs.ch/accounts/
-->


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
- A quick inventory. Most people do not know what they already have.
- By default: compute on both clusters, and project storage that the whole project shares.
- Home and scratch are yours, not the project's. Module 2 covers those.
- One thing is opt-in: an inference resource, added by the PI or the deputy.
- These are not separate pots. One project credit, and everything spends it.
- Next: you can use a model without running a job at all.
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
- This is new, since the twenty-fourth of July.
- A managed inference API. Open-weight models, served for you.
- OpenAI and Anthropic compatible. Change the base URL and your code works.
- And it serves Apertus, which is your own model.
- The PI adds the resource, then any member creates API keys.
- The credit comes out of your project credit.
- A budget on one key does not cap the project. Any member can make another key.
- If you want a project cap, that is a Service Desk ticket.
- Three lines of curl. If you know the OpenAI API, you know this.
- Next: how you see what you have spent.
DOCS: docs.cscs.ch/services/inference/api/
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/accounts/' -->
<div class="audience all">Everyone</div>

# Check the consumption regularly

New since **24 August 2026**: two panels for the project, and a third view per resource.

<div class="cols-narrow">
<div>

- **This month** — drawn so far, projected month-end, and whether you are on pace
- **Overall credit** — allocated, used, **lost**, remaining
- **Per resource** — open one for the usage **per user** inside it

</div>
<div class="screenshot">

![Two portal panels. This month's credit consumption shows drawn so far, projected month-end, last month, and a pacing bar against the minimum draw. Overall credit shows what is allocated, used, lost and remaining, with the average daily draw.](../assets/screenshots/portal-consumption.png)

</div>
</div>

<div class="accent">

Every member of the project sees this, not only the PI.

</div>

<!--
- This changed two days ago. Even weekly users have not seen it.
- First panel: the month you are in. Drawn so far, projected month-end, last month.
- The pacing bar tells you in one look if you are ahead or behind for today.
- Second panel: the whole credit. Allocated, used, lost, remaining.
- Lost is the word to look at. Credit never spent, and not coming back.
- A third view is not in this picture. Open one resource for the usage per user.
- Everyone on the project sees this, not only the PI.
- We know these views were not good enough. This is the first part of the fix.
- Next: why regularly, and not just at the end.
DOCS: docs.cscs.ch/accounts/
-->


---
<!-- _footer: 'Alps technical training · Swiss AI Initiative Annual Meeting 2026 · docs.cscs.ch/platforms/mlp/' -->
<div class="audience">PIs and deputies</div>

# Spend it linearly, or you lose it

Every project gets a credit in GPU hours, spent as your jobs run. Each month has an expected amount, and a minimal you must not fall below.

<div class="diagram">
<svg viewBox="0 0 1160 320" width="100%" role="img"
     aria-label="Top: three example months of usage as bars against two thresholds, an expected line and a minimal line below it separated by the grace. Above expected is fine, in between rolls over, below the minimal the gap is lost. Bottom: the project timeline, 6 or 12 months, then compute stops, then a 90-day grace period in which the project stays active for data retrieval only, then it closes.">
  <g font-family="Inter, sans-serif">
        <text x="90" y="20" font-size="13" font-weight="600" fill="#888888" letter-spacing="0.6">IN ANY GIVEN MONTH</text>
        <rect x="140" y="52"  width="100" height="128" fill="#9A9AA0"/>
    <rect x="320" y="90"  width="100" height="90"  fill="#9A9AA0"/>
    <rect x="500" y="148" width="100" height="32"  fill="#9A9AA0"/>
        <rect x="500" y="112" width="100" height="36" fill="#F3E0E1" stroke="#D61F26" stroke-width="1.5" stroke-dasharray="4 3"/>
    <text x="550" y="136" font-size="13" font-weight="600" fill="#D61F26" text-anchor="middle">lost</text>
        <line x1="100" y1="70"  x2="800" y2="70"  stroke="#D61F26" stroke-width="2"   stroke-dasharray="7 5"/>
    <line x1="100" y1="112" x2="800" y2="112" stroke="#D61F26" stroke-width="1.5" stroke-dasharray="3 4"/>
    <line x1="100" y1="180" x2="820" y2="180" stroke="#E5E5E5" stroke-width="2"/>
    <text x="810" y="75"  font-size="15" font-weight="600" fill="#D61F26">expected</text>
    <text x="810" y="117" font-size="15" font-weight="600" fill="#D61F26">minimal</text>
        <line x1="990" y1="70" x2="990" y2="112" stroke="#D61F26" stroke-width="1.5"/>
    <line x1="984" y1="70" x2="996" y2="70"  stroke="#D61F26" stroke-width="1.5"/>
    <line x1="984" y1="112" x2="996" y2="112" stroke="#D61F26" stroke-width="1.5"/>
    <text x="1006" y="86"  font-size="13" font-weight="600" fill="#D61F26">grace</text>
    <text x="1006" y="104" font-size="12" fill="#555555">15–50%, by budget size</text>
        <g text-anchor="middle" fill="#1A1A1A">
      <text x="190" y="202" font-size="14" font-weight="600">you go faster</text>
      <text x="190" y="220" font-size="12" fill="#555555">fine — lower priority while ahead</text>
      <text x="370" y="202" font-size="14" font-weight="600">you go slower</text>
      <text x="370" y="220" font-size="12" fill="#555555">the rest rolls over</text>
      <text x="550" y="202" font-size="14" font-weight="600">you fall below</text>
      <text x="550" y="220" font-size="12" fill="#555555">that credit is gone</text>
    </g>
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

Out of credit before the end? The `low` partition, capped at one month of your budget.
All the rules: **docs.cscs.ch/platforms/mlp/**

</div>

<!--
- The most useful slide for a PI, so I will not rush it.
- A credit in GPU hours, spent as your jobs run, roughly evenly month by month.
- Two numbers each month. Expected is what you should use. Minimal is expected minus a grace of fifteen to fifty per cent.
- Left bar: over expected. Fine, you run at lower priority while ahead.
- Middle: under, but above minimal, so the rest rolls over.
- Right: below minimal, and the red box is credit that does not come back.
- Then the timeline. The end date stops compute, and ninety days of grace follow, for data only.
- Out of credit early? The low partition, about one month of your budget.
- Take a photo of this slide.
- Not on the slide, but say it: burning the budget and getting nothing out of it is worse than under-consuming.
- Next: here is where to read the detail.
DOCS: docs.cscs.ch/platforms/mlp/policies/
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
- **Service accounts** — docs.cscs.ch/accounts/account-create/

### Getting in — all of it on the handout

- **MFA** — docs.cscs.ch/access/mfa/
- **SSH and key signing** — docs.cscs.ch/access/ssh/

</div>
<div class="card dark">

### Keep these three

- `portal.cscs.ch` — the project
- `user-account.cscs.ch` — your account and your keys
- `docs.cscs.ch` — everything else

### The handout

Accounts, MFA, signing a key, the SSH config. We are not spending stage time on it — it is all on one page.

### Stuck?

**service-desk@cscs.ch**

</div>
</div>

<!--
- I will not read this out. Three addresses.
- portal.cscs.ch for the project, user-account.cscs.ch for your keys, docs.cscs.ch for the rest.
- One thing not on any slide, and it is our most common ticket.
- No MFA, no SSH. You cannot connect until you have registered a device.
- That, key signing and the SSH config are all on the handout. Take one.
- Next: you are in. Where do two terabytes of training data go?
-->
