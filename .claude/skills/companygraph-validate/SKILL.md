---
name: companygraph-validate
description: Validate this CompanyGraph instance against meta/CONVENTIONS.md, rule by rule, and report what was not checked. Run before every commit.
---

# companygraph-validate

The R0 agent pass. `companygraph check` — the CLI — does not exist in this instance, so the
mechanical rules it would cover are done here by hand as well.

## Procedure

1. Read `meta/core/CONVENTIONS.md` in full. The rules it states are what is being checked —
   R1–R15 at core 0.13.2 — and nothing it does not state. The count is read from the file, not
   from here: a core upgrade adds rules and this list goes stale.
2. Read `.companygraph/manifest.json`. Every folder under `meta/` is a vendored unit —
   `core` always, a pack beside it — and each carries its own `manifest.json` naming the
   release it is. For every path in `files`, compute its sha256 and compare. Report a mismatch — it is not a failure (upgrade's business), but it is said.
   Report the core version too: the rest of the pass is against that release.
3. Walk every `*-schema.md` in every unit under `meta/` and check the R9 shape, in order: H1 `# <Type> Schema`,
   `>` tagline, `**Owner:**` line if owned, `## File Location`, `## Frontmatter` with one table
   (`Field | Required | Type | Description`) or `No YAML frontmatter.`, `## Sections` opening
   with a `Section | Required | Description` table, then `## Purpose` and `## Writing rules`
   where the type has them — as a pair or not at all, never one alone. Every `Table.` section
   has a column table introduced by `` `## X` is a table with these columns: `` and vice versa;
   no list type in a column table; no `:---`. Under `## File Location` the last folder named is
   the type's own, and what precedes it is the owner's path (R10) or nothing.
4. List what sits directly under `model/`. Every entry is a folder a schema names, a file a
   singular schema names, or `README.md` (R6, R13) — there is no allow-list to keep, because
   the container is what makes the rule closed: nothing outside `model/` is content and
   nothing inside it is anything else. Every schema's File Location resolves (R7). No schema
   file sits inside a type folder (R9).
5. For every entity file (every `.md` in a type folder except `README.md`): exactly one H1
   (R1, R2); a folder-form entity's own file is named for its folder (R6). Filenames are R12 —
   slugging is lower-case, every run outside `a-z0-9` becomes one `-`, leading and trailing `-`
   dropped, non-ASCII letters dropped rather than transliterated. A file is named for the slug
   of its H1 unless its schema states another derivation, and two do: an experience is its
   start year, a `-`, and a slug naming the period; a singular type's file is named for the
   type, which leaves its H1 free to be a name or a sentence.
6. For every entity, against its schema: every required frontmatter field present, and no
   frontmatter field the schema does not declare (R15); every
   field typed `enum` holds a listed value (R8); every `ref → <type>` and
   `array of ref → <type>` value equals the H1 of an entity of that type (R3, R4); every
   list-valued field written as a block sequence, one entry per line, never a flow sequence
   in brackets (R11); every required section present; for a `Table.` section, the header row
   equals the column table's columns and every `ref → <type>` cell resolves (R4).
7. Owned types: every `experience` sits under `profiles/<profile>/experiences/` and nowhere
   else (R5, R10).
8. Read each schema's `## Writing rules` and judge every entity of that type against them, one
   rule at a time. Nothing mechanical reaches these — they are written to be checkable by an
   agent reading an entity, and this pass is the only thing that checks them.

## Report

Per rule, `R1 ✓` or `R4 ✗ <file>: <reference> resolves to no <type>` — one line per failure,
citing the rule. Then the writing rules per type, cited as the rule's own words and the file
that breaks it. Then the lines nothing else reaches and this pass judged by reading: whether
each `Evidence` cell is a concrete fact, whether `## In practice` prose says what following and
breaking the value looks like. End with **Not checked:** naming anything above that was
skipped, so a clean report is never read as more than it is.
