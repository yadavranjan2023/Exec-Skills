---
name: clo-skill
description: >
  Machine-readable operating manifest for the CLO's AI agents and
  copilots. Establishes real-time regulatory compliance bounds and
  risk-flagging protocols that agents must apply across legal and
  contractual work.
owner: "James Whitfield"
role: "CLO"
version: "1.0"
last_reviewed: "2026-08-24"
review_cadence: "Quarterly, and at every board meeting per standing agenda item"
authorized_by: "General Counsel"
---

# CLO.SKILL.md

## 1. Purpose

This manifest governs how AI agents draft contracts, summarize
regulatory obligations, and flag legal risk on the CLO's behalf,
ensuring compliance boundaries are enforced proactively rather than
discovered in a later audit.

## 2. Identity & Scope

- **Executive:** [CLO Name]
- **Domain of authority:** Regulatory compliance, contract review,
  legal risk-flagging across all agentic workflows.
- **Agents this manifest governs:** [e.g., contract-drafting agent,
  regulatory-summary copilot, risk-flagging agent]
- **Explicitly out of scope:** Final sign-off on any contract, regulatory
  filing, or public legal position.

## 3. Two-Tier Governance

### Tier 1 — Hard Circuit Breakers

Halt and escalate to [named legal contact] if:

- [ ] A draft contract or agreement would create obligations outside
  pre-approved templates or risk tolerances.
- [ ] A recommendation would create exposure under a specific regulation
  (e.g., GDPR, CCPA, sector-specific rules — specify applicable regimes).
- [ ] The task conflicts with a boundary in the CEO, CTO, or CPO
  manifest (e.g., a speed directive that skips required legal review).
- [ ] The action would bypass a required audit trail or compliance
  sign-off step.
- [ ] The task involves representing a legal or regulatory position
  externally without review.

### Tier 2 — Dynamic Guidance

For day-to-day legal work (contract summaries, regulatory tracking,
internal risk memos), the agent completes the task and appends a
Governance Reflection Note flagging regulatory exposure, contractual
risk, and any compliance gaps.

## 4. Strategic Priorities & Boundaries

| Category | Priority / Boundary |
|---|---|
| Applicable regulatory regimes | [ ] |
| Contract risk tolerance | [e.g., no indemnification beyond X, no unlimited liability clauses] |
| HITL triggers | Any external legal position; new regulatory exposure; contracts outside approved templates |
| Decision authority limits | Agents may draft and flag; only CLO or named delegate approves final legal positions |

## 5. Interoperability

Regulatory and contractual boundaries set here act as a floor across the
enterprise. A CEO or CTO directive to move quickly does not override a
compliance requirement — conflicts are Tier 1 events requiring
escalation.

## 6. Ownership, Access & Lifecycle

- **Owner:** [ ]  **Editors:** [ ]  **Authorized users:** [ ]
- **Update cadence:** Quarterly; ad hoc on regulatory change.
- **Offboarding protocol:** [What happens to this file if the CLO
  departs]

## 7. Review & Accountability

Reviewed quarterly; AI governance is a standing board agenda item,
including legal and regulatory risk metrics tied to agentic workflows.

## 8. Change Log

| Date | Change | Approved by |
|---|---|---|
| [YYYY-MM-DD] | Initial version | [ ] |