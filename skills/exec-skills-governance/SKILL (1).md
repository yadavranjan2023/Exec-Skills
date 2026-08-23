---
name: exec-skills-governance
description: >
  Apply Two-Tier AI governance to executive-facing work: drafting or
  reviewing what an AI agent may do on behalf of a CEO, CTO, CPO, or
  CLO, evaluating whether an agent's proposed action should halt and
  escalate to a human, or writing/updating an executive SKILL.md
  governance manifest. Trigger this whenever the user mentions
  executive AI governance, C-suite AI boundaries, agent circuit
  breakers, a "Governance Reflection Note," or asks to apply, review,
  or draft a CEO/CTO/CPO/CLO manifest — even if they don't use the
  words "governance" or "SKILL.md" explicitly (e.g. "should this agent
  be allowed to send this contract without approval" or "what should
  our AI copilot never be allowed to do").
---

# Exec-Skills governance

Operationalizes the Two-Tier governance model from Rani Yadav-Ranjan's
"Why Every Executive Needs a SKILL.md File" and the rights-by-design
framework in *Constitutional Democracy in the Algorithmic Age*
(Springer, 2026). Static policy PDFs don't govern autonomous agents —
this does.

## The Two-Tier model

**Tier 1 — Hard circuit breakers.** Binary, non-negotiable rules. If a
proposed agent action would process unconsented data, bypass a
required audit trail, or violate an established fairness, privacy, or
security boundary, the agent halts and escalates to a named human.
There is no agent-level resolution of a Tier 1 trigger — ever.
**Cross-functional manifest conflicts are always Tier 1 events**: a
CEO's "move fast" directive does not override a CTO's security floor
or a CPO's consent requirement. When two role boundaries conflict,
escalate; don't pick a winner.

**Tier 2 — Dynamic guidance.** For everyday work, the agent completes
the task but appends a **Governance Reflection Note** covering privacy
trade-offs, security implications, brand/strategic risk, and
compliance flags — giving the executive visibility without blocking
execution.

## Using this skill

1. **Identify which role's boundaries apply.** Read the matching
   reference file for the specifics of that role's Tier 1 triggers and
   priorities:
   - `references/ceo.md` — strategic vision, HITL triggers, brand/cost
     trade-off boundaries
   - `references/cto.md` — security posture, encryption, telemetry
     standards
   - `references/cpo.md` — user rights, accessibility (WCAG 2.1 AA),
     consent requirements
   - `references/clo.md` — regulatory compliance bounds, contract risk
     tolerance
   - `references/base.md` — the shared template underlying all four,
     useful when onboarding a new executive role or reviewing overall
     structure

2. **When asked "should this agent be allowed to do X"**: check the
   relevant role's Tier 1 list first. If it matches a hard trigger,
   answer that the action should halt and escalate — don't soften this
   into a recommendation. If it doesn't match Tier 1, treat it as Tier
   2: describe what the accompanying Governance Reflection Note should
   flag.

3. **When drafting or updating a manifest**: keep the same structure as
   the reference files (Two-Tier governance section, strategic
   priorities table, interoperability section, ownership/lifecycle,
   review cadence) so manifests stay comparable across roles. Don't
   invent placeholder facts about the executive — leave brackets for
   anything not provided.

4. **When reviewing a cross-functional conflict**: name it explicitly
   as a Tier 1 event and describe the escalation path, rather than
   suggesting which executive's directive should "win."

## Validating a manifest

`scripts/validate_skill.py` lints manifest files for required
frontmatter (owner, role, version, last_reviewed, review_cadence,
authorized_by), staleness of `last_reviewed`, and presence of the
required sections. Run it against any manifest before treating it as
finalized:

```
python scripts/validate_skill.py path/to/manifest.md
```

## Source and attribution

Full reference implementation, CI validation, and a runnable Docker
image live at github.com/yadavranjan2023/Exec-Skills. Grounded in
NIST's AI Risk Management Framework and *Constitutional Democracy in
the Algorithmic Age* (Springer, 2026) by Rani Yadav-Ranjan.
