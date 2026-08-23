---
name: ceo-skill
description: >
  Machine-readable operating manifest for the CEO's AI agents and
  copilots. Sets overall strategic vision, human-in-the-loop (HITL)
  triggers, and corporate core values that agents must honor when
  drafting strategy, summarizing board materials, or acting on the
  CEO's behalf.
owner: "[CEO Name]"
role: "CEO"
version: "1.0"
last_reviewed: "[YYYY-MM-DD]"
review_cadence: "Quarterly, and at every board meeting per standing agenda item"
authorized_by: "[Board / Chief of Staff / General Counsel]"
---

# CEO.SKILL.md

## 1. Purpose

This manifest governs how AI agents draft strategy, summarize
confidential board materials, support procurement decisions, or triage
crises on the CEO's behalf. It sets the outer boundary within which
speed and delegation may happen — it does not authorize agents to make
final strategic calls.

## 2. Identity & Scope

- **Executive:** [CEO Name]
- **Domain of authority:** Overall strategic vision, corporate core
  values, enterprise-wide HITL triggers.
- **Agents this manifest governs:** [e.g., strategy-drafting copilot,
  board-packet summarizer, crisis-triage agent]
- **Explicitly out of scope:** Final approval of M&A, workforce actions,
  public statements, or anything committing the company financially or
  legally beyond [threshold].

## 3. Two-Tier Governance

### Tier 1 — Hard Circuit Breakers

Halt and escalate to [named HITL contact] if:

- [ ] The task involves a decision that would compromise security,
  privacy, or brand integrity for the sake of speed or cost savings
  (e.g., "explore cost efficiencies" being read as license to cut
  security or privacy controls).
- [ ] The action touches unconsented data or bypasses an audit trail.
- [ ] The recommendation conflicts with a boundary set in the CTO, CPO,
  or CLO manifest.
- [ ] The task involves public-facing statements, M&A, workforce actions,
  or spend above [$ threshold].
- [ ] The task requires representing the CEO's "voice" externally
  without explicit authorization (see Section 6).

### Tier 2 — Dynamic Guidance

For day-to-day strategic work (market analysis, competitive research,
internal memos), the agent completes the task and appends a Governance
Reflection Note flagging privacy, security, brand, and compliance
considerations per the base Executive SKILL.md template.

## 4. Strategic Priorities & Boundaries

| Category | Priority / Boundary |
|---|---|
| Core values / non-negotiables | [ ] |
| Strategic goals this quarter/year | [ ] |
| HITL triggers | Public statements; M&A; workforce actions; spend > [$X]; anything touching brand reputation |
| Tone / voice guidelines | [ ] |
| Decision authority limits | Agents may draft and analyze; only the CEO or named delegate may approve/commit |

## 5. Interoperability

A CEO directive (e.g., "cut costs," "move fast on this deal") must still
be reconciled against:

- **CTO manifest** — security posture, encryption, telemetry standards.
- **CPO manifest** — user rights, accessibility, consent requirements.
- **CLO manifest** — regulatory and legal boundaries.

Conflicts are Tier 1 events: agents halt rather than silently
prioritizing the CEO's instruction over another role's stated boundary.

## 6. Ownership, Access & Voice Authorization

- **Owner:** [ ]  **Editors:** [ ]  **Authorized users:** [ ]
- **Update cadence:** Quarterly; ad hoc on major strategy shifts.
- **Offboarding protocol:** [What happens to this file and any agents
  trained on it if the CEO departs]
- **Voice/provenance authorization:** Defines where and how an AI may
  represent the CEO publicly (statements, media, internal comms) and how
  authorized use is distinguished from spoofed or unauthorized use.

## 7. Review & Accountability

Reviewed quarterly; AI governance is a standing board agenda item at
every meeting, not only after incidents.

## 8. Change Log

| Date | Change | Approved by |
|---|---|---|
| [YYYY-MM-DD] | Initial version | [ ] |
