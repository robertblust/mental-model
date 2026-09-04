<!-- conventions · v1.2.0 -->
Shared conventions of the robertblust, guestgraph and companygraph organizations live in
`conventions/`, vendored from robertblust/conventions at the release `conventions.json`
names. Read them before writing or committing anything here.

- `conventions/WRITING.md` — how we write: one voice, three registers, English and German.
- `conventions/WORKING.md` — how we work with git and GitHub.
- `conventions/REPOSITORIES.md` — the family: what each repository is and what pins what.

Everything below this block is this repository's own. `sh conventions/conventions-sync check`
says whether the copy matches the release; `sync` brings it to the release the pin names.
Edit a shared file in robertblust/conventions, never here.
<!-- end conventions -->

# AGENTS.md

Guidance for agents working in this repository — the instance's own rules. Every modeling
rule lives in `meta/core/CONVENTIONS.md` and is not restated here; read it first.

## What this is

Robert Blust, described in CompanyGraph: one profile, its experiences, the skills and values
it claims and the ladder it claims them on. `meta/core/` is core 0.13.1, vendored and never edited
here; `.companygraph/manifest.json` records which release and a hash per file.

## Before every commit

Run the `companygraph-validate` skill. It reports per rule R1–R15 and names what it did not
check. A commit with an unresolved reference is not made.

## Mastership

- Every page is mastered here. `source: Local` on all of them, and a correction is made in this
  repository and nowhere else. There is no upstream to correct first.
- No page carries a `source-id`. That field is for a source that issues identifiers, and a
  repository does not.

Why the model masters itself, and what that decided beyond the field value, is in
`docs/specs/2026-09-04-mastership-flip.md`.

## House style

- American English — `organization`, `modeling`, `color`. Proper nouns and quotations stay as
  they are. This is core's R14 as of 0.13.1, so it binds the schema's field names too.
- No Oxford comma.
- One idea per bullet, leading with the outcome or the decision. Active voice. Past tense for
  what ended.
- Claim only what Rob states or a document shows — a record, a deck, a published page. No
  invented metrics, dates, employers or partners. The guard is against invention by whoever is
  editing, never against first-hand testimony.

## Writing a skill

The rules are in `docs/superpowers/specs/2026-08-26-skills-reference-design.md` §3. In short:
the definition starts with the thing itself, never “The practice of”; `## In practice` is in
the imperative without a subject and names no person, employer, date or number; products
appear only in a closing `Typical tools:` clause. A skill is claimed in a profile's Skills
table — that is where one person's level and evidence live, never in the skill file.

## Sync slot

Instance-owned skills would live at `.claude/skills/mental-model-<source>/`. None exist: the
content was written once by hand. The `companygraph-*` skills are the portable ones from the
tooling spec, carried here until the tooling installs them.
