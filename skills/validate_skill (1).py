#!/usr/bin/env python3
"""
validate_skill.py

Lints executive SKILL.md files for the exec-skills repo.

Checks per file:
  1. YAML frontmatter exists and parses.
  2. Required frontmatter keys are present and non-empty
     (name, description, owner, role, version, last_reviewed,
     review_cadence, authorized_by).
  3. last_reviewed is a valid date and not stale relative to
     review_cadence (default staleness threshold: 100 days,
     override with --max-age-days).
  4. Required sections exist in the document body (by heading text):
     - Tier 1 (Hard Circuit Breakers)
     - Tier 2 (Dynamic Guidance)
     - Ownership / Access / Lifecycle
     - Review & Accountability

Exit code is non-zero if any file fails, so this can gate a PR via
GitHub Actions ("required status check").

Usage:
    python validate_skill.py ceo/CEO.SKILL.md cto/CTO.SKILL.md ...
    python validate_skill.py $(git ls-files '*.SKILL.md' '*SKILL.md')
"""

import argparse
import datetime as dt
import re
import sys

try:
    import yaml  # PyYAML
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(2)

REQUIRED_FRONTMATTER_KEYS = [
    "name",
    "description",
    "owner",
    "role",
    "version",
    "last_reviewed",
    "review_cadence",
    "authorized_by",
]

# Matched case-insensitively against markdown headings (## Section Name)
REQUIRED_SECTION_PATTERNS = [
    r"tier\s*1.*hard circuit breaker",
    r"tier\s*2.*dynamic guidance",
    r"ownership.*access.*lifecycle",
    r"review\s*&?\s*accountability",
]

PLACEHOLDER_TOKEN = re.compile(r"\[.*?\]")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


def parse_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, None, ["Missing or malformed YAML frontmatter (no '---' block at top of file)."]

    fm_text, body = match.group(1), match.group(2)
    errors = []

    try:
        frontmatter = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        return None, body, [f"Frontmatter did not parse as valid YAML: {e}"]

    return frontmatter, body, errors


def check_frontmatter_keys(frontmatter: dict):
    errors = []
    for key in REQUIRED_FRONTMATTER_KEYS:
        value = frontmatter.get(key)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"Missing or empty required frontmatter key: '{key}'")
        elif isinstance(value, str) and PLACEHOLDER_TOKEN.search(value):
            errors.append(
                f"Frontmatter key '{key}' still contains a placeholder "
                f"(e.g. '[Name]'): {value!r}"
            )
    return errors


def check_last_reviewed(frontmatter: dict, max_age_days: int):
    errors = []
    raw = frontmatter.get("last_reviewed")
    if not raw:
        return errors  # already flagged as missing above

    raw_str = str(raw)
    if PLACEHOLDER_TOKEN.search(raw_str):
        errors.append("'last_reviewed' still contains a placeholder date.")
        return errors

    try:
        reviewed_date = dt.date.fromisoformat(raw_str)
    except ValueError:
        errors.append(
            f"'last_reviewed' is not a valid ISO date (YYYY-MM-DD): {raw_str!r}"
        )
        return errors

    age_days = (dt.date.today() - reviewed_date).days
    if age_days > max_age_days:
        errors.append(
            f"'last_reviewed' ({reviewed_date.isoformat()}) is {age_days} days old, "
            f"exceeding the {max_age_days}-day staleness threshold. Review is overdue."
        )
    return errors


def check_required_sections(body: str):
    errors = []
    headings = "\n".join(
        line for line in body.splitlines() if line.strip().startswith("#")
    ).lower()

    for pattern in REQUIRED_SECTION_PATTERNS:
        if not re.search(pattern, headings, re.IGNORECASE):
            errors.append(
                f"Could not find a required section matching pattern: '{pattern}'. "
                f"Check that this heading wasn't renamed or deleted."
            )
    return errors


def validate(path: str, max_age_days: int):
    frontmatter, body, errors = parse_file(path)
    if frontmatter is None:
        return errors

    errors += check_frontmatter_keys(frontmatter)
    errors += check_last_reviewed(frontmatter, max_age_days)
    if body is not None:
        errors += check_required_sections(body)

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Path(s) to SKILL.md files to validate")
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=100,
        help="Flag last_reviewed as stale beyond this many days (default: 100, "
        "roughly one quarter plus buffer).",
    )
    args = parser.parse_args()

    had_failures = False

    for path in args.files:
        errors = validate(path, args.max_age_days)
        if errors:
            had_failures = True
            print(f"\n❌ {path}")
            for err in errors:
                print(f"   - {err}")
        else:
            print(f"✅ {path}")

    if had_failures:
        print("\nValidation failed. Fix the issues above before merging.")
        sys.exit(1)
    else:
        print("\nAll SKILL.md files passed validation.")


if __name__ == "__main__":
    main()
