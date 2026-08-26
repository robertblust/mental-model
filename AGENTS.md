# AGENTS.md

Guidance for agents working in this repository — the instance's own rules. Every modeling
rule lives in `meta/CONVENTIONS.md` and is not restated here; read it first.

## What this is

Robert Blust, described in CompanyGraph: one profile, its experiences, the skills and values
it claims and the ladder it claims them on. `meta/` is core 0.1.0, vendored and never edited
here; `.companygraph/manifest.json` records which release and a hash per file.

## Before every commit

Run the `companygraph-validate` skill. It reports per rule R1–R10 and names what it did not
check. A commit with an unresolved reference is not made.

## Mastership

- A page with `source: rob-cv` is mastered in the CV repository. Correct it there first, then
  copy the fact here. Editing it here alone is drift.
- A page with `source: Local` is mastered here.
- `source-id` on a `rob-cv` page is the CV entry's `id`. It is a pointer a person follows;
  there is no sync.

## House style

- American English — `organization`, `modeling`, `color`. Proper nouns and quotations stay as
  they are. (The schema fields are British — `organisation` — and are spelled as the schema
  spells them; a field name is not prose.)
- No Oxford comma.
- One idea per bullet, leading with the outcome or the decision. Active voice. Past tense for
  what ended.
- Claim only what the CV states. No invented metrics, dates, employers or partners.

## Sync slot

Instance-owned skills would live at `.claude/skills/mental-model-<source>/`. None exist: the
content was written once by hand. The `companygraph-*` skills are the portable ones from the
tooling spec, carried here until the tooling installs them.
