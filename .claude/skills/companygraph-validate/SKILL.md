---
name: companygraph-validate
description: Validate this CompanyGraph instance against meta/CONVENTIONS.md, rule by rule, and report what was not checked. Run before every commit.
---

# companygraph-validate

The R0 agent pass. `companygraph check` — the CLI — does not exist in this instance, so the
mechanical rules it would cover are done here by hand as well.

## Procedure

1. Read `meta/CONVENTIONS.md` in full. The rules R1–R10 are what is being checked; do not
   check anything they do not state.
2. Read `.companygraph/manifest.json`. For every path in `files`, compute its sha256 and
   compare. Report a mismatch — it is not a failure (upgrade's business), but it is said.
3. Walk every `*-schema.md` in `meta/` and check the R9 fixed shape: H1 `# <Type> Schema`,
   `>` tagline, `**Owner:**` line if owned, `## File Location`, `## Frontmatter` with one table
   (`Field | Required | Type | Description`) or `No YAML frontmatter.`, `## Sections` opening
   with a `Section | Required | Description` table; every `Table.` section has a column table
   introduced by `` `## X` is a table with these columns: `` and vice versa; no `:---`.
4. List the root folders. Every schema's File Location folder exists (R7); every root folder
   is one a schema names or `meta/`, `.companygraph/`, `.claude/`, `docs/`, `export/`, `dist/`
   (R6, R7). No schema file sits inside a type folder (R9).
5. For every entity file (every `.md` in a type folder except `README.md`): exactly one H1
   (R1, R2); filename is the kebab-case of the H1, or for an experience the start year plus a
   slug; a folder-form entity's own file is named for its folder (R6).
6. For every entity, against its schema: every required frontmatter field present; every
   field typed `enum` holds a listed value (R8); every `ref → <type>` and
   `array of ref → <type>` value equals the H1 of an entity of that type (R3, R4); every
   required section present; for a `Table.` section, the header row equals the column table's
   columns and every `ref → <type>` cell resolves (R4).
7. Owned types: every `experience` sits under `profiles/<profile>/experiences/` and nowhere
   else (R5, R10).

## Report

Per rule, `R1 ✓` or `R4 ✗ <file>: <reference> resolves to no <type>` — one line per failure,
citing the rule. Then the lines the script cannot reach and this pass judged by reading:
whether each `Evidence` cell is a concrete fact, whether `## In practice` prose says what
following and breaking the value looks like. End with **Not checked:** naming anything above
that was skipped, so a clean report is never read as more than it is.
