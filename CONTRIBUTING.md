# Contributing to Exec-Skills

This repo governs how AI agents act on behalf of specific executives.
Changes here aren't just documentation edits — they change what an
agent is and isn't allowed to do. Treat every PR accordingly.

## Before you open a PR

- **Know which manifest you're touching.** `_base/TheExecutiveSKILL.md`
  is the shared template; changes there ripple into every role.
  `ceo/`, `cto/`, `cpo/`, and `clo/` are role-scoped — only touch the
  one relevant to the change you're making.
- **Don't loosen a Tier 1 boundary casually.** If you're removing or
  weakening a Hard Circuit Breaker (Section 3, Tier 1 in any manifest),
  say so explicitly in the PR description and tag the accountable
  owner directly, even though CODEOWNERS will already require their
  approval.
- **No placeholder text in a merged file.** Anything in `[brackets]`
  is a placeholder. The CI validator will flag frontmatter placeholders
  automatically, but body-text placeholders (inside tables, boundary
  descriptions) aren't checked by the linter — review for those
  manually before requesting approval.

## Making a change

1. Create a branch off `main` — direct pushes to `main` are blocked by
   branch protection.
2. Edit the relevant `SKILL.md` file(s). Keep the existing section
   headings intact (`## Tier 1 — Hard Circuit Breakers`, etc.) —
   the CI check and any agent parsing these files by heading will
   break if a section is renamed or removed.
3. If you're changing anything meaningful (not a typo fix), update
   that file's frontmatter:
   - bump `version`
   - update `last_reviewed` to today's date
   - add a row to the `## 8. Change Log` table at the bottom of the
     file: date, what changed, who approved it
4. Open a PR. Include in the description:
   - **What changed and why** (a new regulatory requirement, an org
     change, a routine quarterly review, etc.)
   - **Who this affects** — which agents or workflows consume this
     manifest
5. `.github/CODEOWNERS` will automatically request review from the
   right owner(s) for the path you touched. Do not merge without that
   approval, even if you have permissions to.

## What CI checks (and doesn't)

The `validate-skill-files` workflow runs `scripts/validate_skill.py`
on every PR touching a `SKILL.md` file. It checks:

- YAML frontmatter parses and required fields aren't empty or
  placeholders
- `last_reviewed` isn't stale (default: 100 days)
- Required sections (Tier 1, Tier 2, Ownership & Lifecycle, Review &
  Accountability) are present by heading

**It does not check** whether a boundary is well-reasoned, whether a
Tier 1 trigger is set at the right threshold, or whether the change is
consistent with actual company policy. That judgment call belongs to
the human reviewer(s) required by CODEOWNERS — CI passing is a
necessary condition for merge, not a sufficient one.

## Quarterly reviews

Every manifest should be reviewed at least quarterly, even when nothing
changes:

1. Open a PR against the file (or files) due for review.
2. If no content changes are needed, still update `last_reviewed` and
   add a Change Log row: `"Reviewed, no changes"` with the reviewer's
   name.
3. Get the standard CODEOWNERS approval and merge.

This keeps a defensible, timestamped record that review actually
happened — useful for the board-level AI governance accountability
this framework is meant to support, and for reconstructing what rules
an agent was operating under on any given date.

## Adding a new role manifest

If the organization adds a new C-suite role that needs its own
manifest (e.g., a Chief AI Officer):

1. Create a new folder (e.g., `cao/`) with a file following the
   `_base/TheExecutiveSKILL.md` structure.
2. Add an entry to `.github/CODEOWNERS` mapping the new folder to its
   owner.
3. Update `README.md`'s "What's in here" table.
4. Open a PR as usual — this itself should go through review from
   whoever owns `.github/` (currently Legal + Security per
   CODEOWNERS).

## Questions or disagreements

If you're unsure whether a proposed change weakens a boundary it
shouldn't, or whether something belongs in Tier 1 vs. Tier 2, raise it
as a PR comment or an issue before merging rather than resolving it
unilaterally — that's the same escalate-don't-resolve principle these
manifests ask of the agents that consume them.