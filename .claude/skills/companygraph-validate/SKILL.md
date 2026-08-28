---
name: companygraph-validate
description: Validate this CompanyGraph instance against meta/CONVENTIONS.md, rule by rule, and report what was not checked. Run before every commit.
---

# companygraph-validate

The R0 agent pass. `companygraph check` — the CLI — does not exist in this instance, so the
mechanical rules it would cover are done here by hand as well.

## Procedure

1. Read `meta/CONVENTIONS.md` in full. Whatever rules it defines are what is being checked —
   read them out of the file, never from a list here. Do not check anything they do not state.
   A number written down in this procedure is wrong the first time core adds a rule, and says
   nothing about it.
2. Read `.companygraph/manifest.json`. For every path in `files`, compute its sha256 and
   compare. Report a mismatch — it is not a failure (upgrade's business), but it is said.
3. Walk every `*-schema.md` in `meta/` and check it against the fixed shape *as the conventions
   state it* — headings, their order, which tables each holds, the closed type vocabulary, the
   separator rows. Read the rule and check what it says; do not work from a copy of the shape
   written here. This procedure had one, and it went stale the release core added two sections
   to the shape.
4. List the root folders. Every schema's File Location folder exists (R7); every root folder
   is one a schema names or `meta/`, `.companygraph/`, `.claude/`, `docs/`, `export/`, `dist/`
   (R6, R7). No schema file sits inside a type folder (R9).
5. For every entity file (every `.md` in a type folder except `README.md`): exactly one H1
   (R1, R2); the filename is what the conventions' filename rule says, read from there rather
   than restated here, and the type's own schema where it names its own form; a folder-form
   entity's own file is named for its folder (R6). Every list-valued frontmatter field is
   written as the conventions require.
6. For every entity, against its schema: every required frontmatter field present; every
   field typed `enum` holds a listed value (R8); every `ref → <type>` and
   `array of ref → <type>` value equals the H1 of an entity of that type (R3, R4); every
   required section present; for a `Table.` section, the header row equals the column table's
   columns and every `ref → <type>` cell resolves (R4).
7. Owned types: every `experience` sits under `profiles/<profile>/experiences/` and nowhere
   else (R5, R10).
8. For every type whose schema carries `## Writing rules`, read them and judge every entity of
   that type against each one. These are the rules no script reaches, and they are the reason
   an entity can satisfy its whole schema and still be wrong.

## Report

Per rule, `R1 ✓` or `R4 ✗ <file>: <reference> resolves to no <type>` — one line per failure,
citing the rule, for every rule `meta/CONVENTIONS.md` defines.

Then the same per writing rule, cited by type and by the rule's own words:
`skill/person-neutral ✗ skills/x.md: names an employer`. Judge these by reading; nothing else
does. Do not paraphrase a writing rule into a shorter one — the schema's wording is the rule.

End with **Not checked:** naming anything above that was skipped, so a clean report is never
read as more than it is.
