---
name: companygraph-export
description: Package this CompanyGraph instance as a loadable agent skill — dist/<instance>-skill.zip with SKILL.md and one consolidated file per root type.
allowed-tools: Bash(*)
---

# companygraph-export

Produces `dist/mental-model-skill.zip`, uploadable as an organization or personal skill:
`SKILL.md` at the root, `model/<type>.md` per root type folder, `model/meta.md`.

## Procedure

1. Read `.companygraph/manifest.json` for the core version. The instance name is the
   repository folder's name (`mental-model`); the description is the root `README.md`'s
   `>` line.
2. Stage in a temporary directory: `mental-model/SKILL.md` and `mental-model/model/`.
3. For every root type folder (every folder a schema in `meta/` names, plus `profiles/`
   recursively so experiences travel with their profile): write `model/<folder>.md` — the
   folder's `README.md` first, then every entity file in path order, separated by a line
   holding `---`. Count the entities per type as you go.
4. `model/meta.md`: `meta/CONVENTIONS.md`, then every `meta/*-schema.md`, separated by `---`.
5. `SKILL.md`: frontmatter `name: mental-model` and `description: <the README tagline>`; then
   `export/SKILL-intro.md` verbatim when it exists; then a table of `model/` files with the
   entity count per type and the core version; then one paragraph on how to read the model —
   H1 is the name, references are by name, `meta/meta.md` holds the rules.
6. `mkdir -p dist && zip -r dist/mental-model-skill.zip mental-model` from the staging root.
   Verify: `unzip -l` lists `SKILL.md`, `model/meta.md` and one file per folder; the counts in
   `SKILL.md` equal `find <folder> -name '*.md' ! -name README.md | wc -l` on disk.
7. Remove the staging directory. `dist/` is gitignored; the zip is never committed.
