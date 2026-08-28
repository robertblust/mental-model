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
   folder's `README.md` first, then every entity file in path order, each preceded by a line
   `<!-- entity: <path from the repository root> -->` and a blank line. Count the entities per
   type as you go.

   Not a line holding `---`, which is what this produced before: every entity's frontmatter
   opens and closes with that same line, so a consolidated file of seventy-five skills holds
   two hundred and twenty-five of them and nothing says which seventy-five are boundaries. An
   entity whose body carries a horizontal rule is indistinguishable from a boundary, and no
   program can split the file at all. `<!--` collides with neither YAML nor Markdown's own
   rule, it does not render, and the path gives back the provenance consolidation throws away.

   A README describes the repository's layout and the bundle has a different one, so rewrite
   its references as it is inlined: `meta/<type>-schema.md` becomes `model/meta.md`, a folder
   the bundle does not carry — `experiences/` — becomes the plain word, and a reference to
   anything the bundle holds no copy of is dropped rather than left dangling. The source keeps
   the paths that are correct where it lives; only the copy that travels is rewritten.
4. `model/meta.md`: `meta/CONVENTIONS.md`, then every `meta/*-schema.md`, each preceded by its
   own `<!-- entity: meta/<file> -->` line.
5. `SKILL.md`: frontmatter `name: mental-model` and a `description` field built from the
   README tagline with Markdown link and emphasis syntax stripped to plain text (a link
   becomes its link text; bold/italic markers are dropped), written as a double-quoted YAML
   string with any inner double quotes escaped as `\"`; then `export/SKILL-intro.md` verbatim
   when it exists; then a table of `model/` files with the entity count per type and the core
   version; then one paragraph on how to read the model — each entity begins at its
   `<!-- entity: … -->` line, H1 is the name, references are by name, `model/meta.md` holds the
   rules.
6. `mkdir -p dist && zip -r dist/mental-model-skill.zip mental-model` from the staging root.
   Verify: `unzip -l` lists `SKILL.md`, `model/meta.md` and one file per folder; the counts in
   `SKILL.md` equal `find <folder> -name '*.md' ! -name README.md | wc -l` on disk.
7. Remove the staging directory. `dist/` is gitignored; the zip is never committed.
