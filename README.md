# Exec-Skills

Machine-readable governance manifests for executive AI agents and copilots.

This repo operationalizes the framework described in *"Why Every
Executive Needs a SKILL.md File"* by Rani Yadav-Ranjan: as AI agents take
on more autonomous work across the enterprise — drafting strategy,
summarizing confidential materials, supporting procurement, triaging
customer issues — leaders need a way to translate their judgment,
priorities, and boundaries into something machines can actually apply at
runtime. Static policy PDFs and slide decks aren't built for that;
this repo is.

## What's in here

| Path | Purpose |
|---|---|
| `_base/TheExecutiveSKILL.md` | The shared template every role-specific manifest is built from. Start here if you're onboarding a new executive role. |
| `ceo/CEO.SKILL.md` | Strategic vision, core values, HITL triggers, brand/cost trade-off boundaries. |
| `cto/CTO.SKILL.md` | Security posture, encryption requirements, telemetry standards. |
| `cpo/CPO.SKILL.md` | User rights, accessibility benchmarks (WCAG 2.1 AA), consent requirements. |
| `clo/CLO.SKILL.md` | Regulatory compliance bounds, contract risk tolerance, risk-flagging protocols. |
| `.github/CODEOWNERS` | Maps each folder to the person/team required to approve changes to it. |
| `.github/workflows/validate-skill-files.yml` | CI check that lints every SKILL.md file on each PR. |
| `scripts/validate_skill.py` | The linter itself — checks frontmatter, staleness, and required sections. |

## How the framework works

Each manifest follows the same **Two-Tier Governance Architecture**:

- **Tier 1 — Hard Circuit Breakers.** Binary, non-negotiable rules
  (e.g., no processing unconsented data, no bypassing audit trails, no
  action that conflicts with another executive's manifest). When
  triggered, an agent halts and escalates to a named human — it does
  not resolve the conflict itself.
- **Tier 2 — Dynamic Guidance.** For everyday work, the agent completes
  the task but appends a **Governance Reflection Note** flagging
  privacy, security, brand, and compliance considerations, so the
  executive retains visibility without reviewing every step.

Manifests are designed to be **reconciled against each other** before an
agent acts — a CEO directive to "cut costs" still has to clear the
CTO's security floor, the CPO's consent requirements, and the CLO's
regulatory bounds. A conflict between manifests is treated as a Tier 1
event, not a tie-breaker in any one role's favor.

## Using a manifest with an agent

Point your agent framework (Claude Code, an internal copilot, an MCP
server, etc.) at the raw file for the relevant role, e.g.:

```
https://raw.githubusercontent.com/yadavranjan2023/Exec-Skills/main/cto/CTO.SKILL.md
```

Load it as system context or a runtime-loaded skill at the start of a
session. Note that these files describe the *rules* — whether an agent
actually halts on a Tier 1 trigger depends on your agent runtime
enforcing that behavior (a pre-action check, a wrapper, etc.), not on
the file alone.

## Governance of this repo

- Every manifest requires sign-off from its named owner via
  `.github/CODEOWNERS` — no direct pushes to `main`.
- Every PR touching a `SKILL.md` file is linted by
  `scripts/validate_skill.py`, which checks that:
  - YAML frontmatter is present and required fields aren't empty or
    still placeholders,
  - `last_reviewed` isn't stale (default threshold: 100 days),
  - required sections (Tier 1, Tier 2, Ownership, Review &
    Accountability) haven't been renamed or deleted.
- Reviews happen **quarterly at minimum**. Log the review as a PR —
  even an empty diff with "reviewed, no changes, approved by [name]" —
  so there's a defensible record rather than relying on memory.
- AI governance tied to these manifests should be a **standing board
  agenda item**, reviewed at every meeting, not only after an incident.

## Setup checklist

- [ ] Replace every `@handle` placeholder in `.github/CODEOWNERS` with
      real GitHub usernames or team handles.
- [ ] Fill in the bracketed placeholders (`[Name]`, `[$ threshold]`,
      etc.) in each role's manifest with actual priorities and
      boundaries.
- [ ] Enable branch protection on `main`: require pull requests,
      require CODEOWNERS review, require the `validate-skill-files`
      status check to pass.
- [ ] Confirm the offboarding protocol in each manifest's Ownership
      section reflects your actual HR/IT process for role transitions.

## Background

This framework draws on the Two-Tier governance model and the
"rights-by-design" approach described in Rani Yadav-Ranjan's
*Constitutional Democracy in the Algorithmic Age* (Springer, 2026), and
is broadly consistent with NIST's AI Risk Management Framework emphasis
on clearly defined responsibilities, ongoing monitoring, and executive
accountability for AI-related risk decisions.

This repo is a governance starting structure, not legal or compliance
advice. Route final language through Legal, Security, and Risk before
deploying any manifest into a live agent workflow.