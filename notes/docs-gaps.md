# Documentation gaps found while writing this session

Every gap below was hit while writing this session and checking each claim against
`docs.cscs.ch`. In each case the behaviour is known and correct, but nothing on the
public documentation states it, so a slide asserting it cannot be reviewed by anyone
except the person who already knew.

The body of this file is written to be pasted into an issue on the documentation
repository. Keep adding to it as the remaining modules are finished — the list will grow.

Source of the corrections: Andrea Ceriani, ML Platform service manager.
Cross-referenced in `notes/sources.md`.

---

## Most urgent: a page documenting a service that no longer exists

- [ ] **`docs.cscs.ch/storage/longterm/` describes a decommissioned service.** The Long
      Term Storage service has been retired and `lts.cscs.ch` no longer resolves to a
      portal, but the page is still live and still written in the present tense. It
      promises 10-year retention and persistent identifiers, offers "2 TB of LTS storage
      quota (for 10 years) free of charge per project", and quotes a price of
      "CHF 600.- for each terabyte".

      This is not a gap and not an imprecision. It is a live page telling users that a
      dead service exists, at a price. Somebody planning where to keep data they must
      preserve for ten years will act on it. Take the page down or mark it retired, and
      say what replaces it — if anything does.

      Note that the same section's object storage page is fine: `rgw.cscs.ch` responds
      and the service is current.

---

## The portal — `docs.cscs.ch/accounts/waldur/`

The page currently has four sections: the tool, log in, select the organisation, invite
users. It stops at the invitation. Everything a PI does *after* that is undocumented.

- [ ] **Who can see consumption, and at what granularity.** Nothing on the page
      describes the usage view at all. The behaviour is:
      - every **project member** — not only the PI — sees the **project total**;
      - **per-user** usage is visible inside the detail of each individual resource;
      - there is **no per-user total** across the whole project.
      Worth stating explicitly, because the common assumption is that usage is a
      PI-only view.

- [ ] **Changing the role of an existing member.** The page documents assigning a role
      *at invitation time* only. It should say whether an existing member's role can be
      changed afterwards, by whom (project administrator, project manager, or both) and
      from where (the Team tab). This is a routine request and there is currently no
      page to point people at.

- [ ] **The Team tab.** Mentioned only in passing as part of the path to Invitations.
      It is the answer to "who is on my project and what can they do", which is the
      question PIs ask most often, and it deserves its own short section.

## Accounts — `docs.cscs.ch/accounts/`

The page states that "accounts are bound to projects, and accounts will be closed with
the project unless the account is also part of another open project". That is the middle
of the lifecycle. Both ends are missing.

- [ ] **The email address is the account identity.** One address, one account, however
      many projects. Not stated anywhere.

- [ ] **A later invitation re-enables the same account.** When the last project of an
      account closes, the account is closed — but a subsequent invitation switches the
      *same* account back on rather than creating a new one. This is the difference
      between a user believing their account was deleted and understanding that it is
      dormant, and it is worth one sentence.

## Service accounts — everything the slide says, and none of it documented

`docs.cscs.ch/accounts/account-create/` documents how to request a service account: the PI
submits the request, it is scoped to a single project, and after approval a Service Account
entry appears under the Team tab. Everything else on the module 1 slide was confirmed by
Andrea on 25 August 2026 and appears in no CSCS document:

- Service accounts are **not enabled by default** — the page describes the request but
  never says the feature is off until you ask.
- The account is **normally run by the project team**, and registered on a **shared team
  address**, so notifications reach the team rather than one person's inbox.
- It has a **username of its own** and authenticates with an **API key**, not a password.
  It has **no MFA**, because it does not log in interactively.

The last point is the one to write down first. Everywhere else we tell users that there is
no access without MFA, so an identity that deliberately has none needs its own paragraph,
or it reads as an inconsistency — or worse, as a loophole.

The CUG 2026 IAM paper (doi 10.1145/3837730.3837747) covers the lifecycle semantics and is
citable, but it is a conference paper, not user documentation.

## ML Platform policies — what the grace period actually suspends

- [ ] The policies page says a project "remains accessible for a grace period of 90 days
      for data retrieval". It does not say what stops at the end date and what does not.
      The behaviour is: the **end date stops the compute**, the project itself **stays
      active** for those 90 days, and only then does it close. Users read "the project
      ends" and assume everything goes at once, including their data. One sentence on
      that page would prevent a recurring panic.

## Storage — pending merge, plus one genuinely open question

- [ ] `datacache` and the Ritom scratch exist only on the `/442` preview. Nothing to fix
      here — a tracking entry, to be closed when the pages land and the module 2 links
      are re-pointed.
- [ ] **Ritom is documented as Clariden-only, and it is not.** The preview's table says
      `/ritom/scratch/cscs/$USER` "(Clariden only)" and the prose says "On Clariden, the
      cleanup policy ... is being finalised". Per Andrea it is mounted more widely than
      that. This is wrong information rather than missing information, so it matters
      more: someone will plan around a filesystem they think they do not have.

- [ ] **Ritom's cleanup policy is 30 days, and nowhere says so.** The preview still
      reads "is being finalised"; per Andrea it has been settled at 30 days, the same as
      capstor. Everything else about Ritom is documented — `docs.cscs.ch/guides/storage/`
      says what it is and which workloads benefit — so this is a single number that
      exists and is simply not written down. The session has to say it out loud, which
      is exactly the situation this file is for.

## ML Platform policies — pending merge

- [ ] The policies page is still only a preview at
      `cscs-docs-preview.svc.cscs.ch/463/platforms/mlp/policies/`. Module 1 depends on it
      for the small/large project comparison and for the whole linear-consumption slide
      (expected and minimal consumption, the 15% to 50% grace, the `low` partition cap,
      the 90-day retrieval window). Nothing to fix here — this is a tracking entry, to be
      closed when the page lands on `docs.cscs.ch` and the links in
      `slides/01-project-access.md` are switched over.

---

## Why this matters beyond the docs

The session is built on the rule that every technical claim must be traceable to
`docs.cscs.ch`. Where that fails, the deck either says nothing — which leaves the
audience without an answer they came for — or asserts something a reviewer cannot check.
The deck currently carries **16** `TODO(verify)` markers across seven files. Most of
them exist only because of the gaps above, and most would close on their own the day the
pending pages are merged. The ones that would not are the portal behaviours and the
project lifecycle — those need somebody to write a paragraph.
