# AGENTS.md

Guidance for agents working in this repository — the instance's own rules. Every modeling
rule lives in `meta/core/CONVENTIONS.md` and is not restated here; read it first.

## What this is

Robert Blust, described in CompanyGraph: one profile, its experiences, the skills and values
it claims and the ladder it claims them on. `meta/core/` is core 0.13.0, vendored and never edited
here; `.companygraph/manifest.json` records which release and a hash per file.

## Before every commit

Run the `companygraph-validate` skill. It reports per rule R1–R15 and names what it did not
check. A commit with an unresolved reference is not made.

## Mastership

- Every page is mastered here. `source: Local` on all of them, and a correction is made in this
  repository and nowhere else. There is no upstream to correct first.
- No page carries a `source-id`. That field is for a source that issues identifiers, and a
  repository does not.

Until September 2026 the profile and 23 of the 24 experiences read `source: rob-cv` and were
mastered in a private CV repository, written to generate tailored application dossiers and
copied down here. That repository is archived: the role it was written to find starts on
1 October 2026, and what it did — one source of facts, many rendered forms — is work this model
can carry itself. The flip lost nothing, because the prose here was already the copy. What it
changed is the direction of the arrow, and that is worth writing down, because every convention
above was drafted while it pointed the other way.

## House style

- American English — `organization`, `modeling`, `color`. Proper nouns and quotations stay as
  they are. This is core's R14 as of 0.13.0, so it binds the schema's field names too. It used
  to say the opposite here, and named `organisation` as the exception that proved it.
- No Oxford comma.
- One idea per bullet, leading with the outcome or the decision. Active voice. Past tense for
  what ended.
- Claim only what something outside this repository can confirm — a document, a record, a
  published page. No invented metrics, dates, employers or partners. This rule used to read
  "claim only what the CV states"; the CV is archived and the rule it stood for is not, so it
  now says what it always meant.

## Writing a skill

The rules are in `docs/superpowers/specs/2026-08-26-skills-reference-design.md` §3. In short:
the definition starts with the thing itself, never "The practice of"; `## In practice` is in
the imperative without a subject and names no person, employer, date or number; products
appear only in a closing `Typical tools:` clause. A skill is claimed in a profile's Skills
table — that is where one person's level and evidence live, never in the skill file.

## Sync slot

Instance-owned skills would live at `.claude/skills/mental-model-<source>/`. None exist: the
content was written once by hand. The `companygraph-*` skills are the portable ones from the
tooling spec, carried here until the tooling installs them.
