<!-- conventions · v1.21.0 -->
Shared conventions of the robertblust, guestgraph and companygraph organizations live in
`conventions/`, vendored from robertblust/conventions at the release `conventions.json`
names. Read them before writing or committing anything here.

- `conventions/WRITING.md` — how we write: one voice, three registers, English and German.
- `conventions/WORKING.md` — how we work with git and GitHub.
- `conventions/REPOSITORIES.md` — the family: what each repository is and what pins what.
- `conventions/WRITER.md`, `conventions/TRANSLATOR.md`, `conventions/GLOSSARY.md` — the two roles that
  make a text, and the terms they keep.

Everything below this block is this repository's own. `sh conventions/conventions-sync check`
says whether the copy matches the release, `sync` brings it to the release the pin names, and
`sh conventions/conventions-check` holds this repository's own Markdown to `WRITING.md`, and
`sh conventions/conventions-format` to its one form, which `fix` writes. Edit a shared file in
robertblust/conventions, never here.
<!-- end conventions -->

# AGENTS.md

Guidance for agents working in this repository — the instance's own rules. Every modeling
rule lives in `meta/core/CONVENTIONS.md` and is not restated here; read it first.

## What this is

Robert Blust, described in CompanyGraph: two profiles — the person, with its experiences, and the
agent that holds every seat in `model/roles/` but the Owner's — the skills and values they claim
and the ladder they claim them on. `meta/core/` is core, vendored and never edited here;
`.companygraph/manifest.json` records which release and a hash per file.

## Checks

Two jobs, both required by the ruleset on `main`: `companygraph`, which calls meta-model's
`instance-check.yml` at the release named in the workflow and is shown by GitHub as
`companygraph / companygraph`, and `conventions`, called from robertblust/conventions at the
pinned tag and shown as `conventions / conventions`. `meta/` is excluded from the prose check
because it is core, vendored and never edited here; its words are core's to hold.
`docs/superpowers/` is excluded too, as in every other member: its research quotes the taxonomy
labels it compares.

## Before every commit

Run the `companygraph-validate` skill. It reports per numbered rule and names what it did not
check. A commit with an unresolved reference is not made.

The skill lives in `.claude/skills/` here, so it loads only for a session rooted in this
repository. A session rooted above it — at `~/git/robertblust/`, say, where every member is a
subdirectory — sees no skill of this repository's at all, and the failure is silent: the skill is
simply absent rather than reported missing. Where that happens the pass is still owed, by hand
and against `meta/core/CONVENTIONS.md`, and the commit says which of the two ran. A `Verified:`
line naming a skill that did not load is the one outcome this paragraph exists to prevent.

## Numbers that move

A count or a version of something that still changes is not written down here: not the types,
releases or rules of core, not the release this repository vendors, not the experiences, skills,
values, seats or tools the model holds. Such a number is true on the day it is written, and
nothing in this repository fails when it stops being true, so it goes stale without a sound;
refreshing it only resets the clock, which is how the same entry went stale twice. Say where
the number is read instead — the manifest for the release, the folder for the entities, the list
the sentence sits beside — or say it without the number.

A number fixed by a closed period stays, because nothing will move it: 25 people at a company
the period ended with, 12 of 25 applications in a search that is over. Where a quantity that
still moves has to be said, a floor that stays true is the form, “over 25 years”. Before a
commit, read the diff for digits and number words and ask of each whether it can change.

## Mastership

- Every page is mastered here. `source: Local` on all of them, and a correction is made in this
  repository and nowhere else. There is no upstream to correct first.
- No page carries a `source-id`. That field is for a source that issues identifiers, and a
  repository does not.
- A fact enters from Robert Blust or from a document — a record, a deck, a published page.
  `WRITING.md` asks that a claim be measured or verifiable; in a model of one person the person
  is where the measurement comes from, so his own account of his work is a source and not a
  claim awaiting one. The guard is against invention by whoever is editing, never against
  first-hand testimony.
- A document that is public is linked; a document that is private is not held here. `url` and a
  `## References` row carry what a reader can open for themselves — a talk's recording, a
  published case study, a commercial register entry. Employment references, diplomas and
  certifications are a deliberate exception: they are the source of dates and of what a period
  contained, they are read when a page is written, and they stay in Robert Blust's own vault and
  are shown on request. So an entry whose evidence is private carries the fact and no link, and
  the missing link is the decision rather than a gap to fill.

Why the model masters itself, and what that decided beyond the field value, is in
`docs/specs/2026-09-04-mastership-flip.md`.

## Writing a skill

The rules are in `docs/superpowers/specs/2026-08-26-skills-reference-design.md` §3. In short:
the definition starts with the thing itself, never “The practice of”; `## In practice` is in
the imperative without a subject and names no person, employer, date or number; products
appear only in a closing `Typical tools:` clause. A skill is claimed in a profile's Skills
table and evidenced in the Evidence table under it — that is where one person's level and
evidence live, never in the skill file.

## Sync slot

Instance-owned skills live at `.claude/skills/mental-model-*/`, and one does:
`mental-model-evidence-coverage` checks the joins the profile schema leaves to whoever writes:
that the experience an Evidence row names lists the row's skill, and that every claim has a row
under it. That the experience is this profile's own is held by the instance checks. The skill
is here rather than in `companygraph-validate` because every check there cites a numbered rule
from `CONVENTIONS.md`, and the schema's own writing rules say that no rule checks these.

The `companygraph-*` skills are the portable ones from the tooling spec, carried here until the
tooling installs them. No skill syncs content into this repository; the content was written by
hand.
