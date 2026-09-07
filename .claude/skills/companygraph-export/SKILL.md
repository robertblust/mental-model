---
name: companygraph-export
description: Package this CompanyGraph instance twice — dist/<instance>-skill.zip for an agent, dist/<instance>-notebooklm/ for NotebookLM. One walk, two renderings, the same entity count asserted against both.
allowed-tools: Bash(*)
---

# companygraph-export

Two artifacts from one walk of the model, because the two readers want the same facts in
different shapes. `dist/mental-model-skill.zip` is uploadable as an organization or personal
skill: `SKILL.md` at the root, `model/<type>.md` per root type folder, `model/meta.md`.
`dist/mental-model-notebooklm/` is a flat folder of Markdown sources, one per content area,
carrying the model's own pages as they are written.

## Procedure

1. Read `.companygraph/manifest.json` for the core version. The instance name is the
   repository folder's name (`mental-model`); the description is the root `README.md`'s
   `>` line.
2. Stage in a temporary directory: `mental-model/SKILL.md` and `mental-model/model/`.
3. For every type folder under `model/` (plus `model/profiles/` recursively so experiences
   travel with their profile): write `model/<folder>.md` in the bundle — the
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
   its references as it is inlined: `meta/<unit>/<type>-schema.md` becomes `model/meta.md`,
   a folder the bundle does not carry — `experiences/` — becomes the plain word, and a
   reference to anything the bundle holds no copy of is dropped rather than left dangling.
   The source keeps the paths that are correct where it lives; only the copy that travels is
   rewritten.
4. `model/meta.md`: `meta/core/CONVENTIONS.md`, then every `*-schema.md` in every unit under
   `meta/`, each preceded by its own `<!-- entity: meta/<unit>/<file> -->` line.

   The singular entities travel too: `model/identity.md` and `model/vision.md` are copied
   as they are, one file each, since there is nothing to consolidate.
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
7. The NotebookLM rendering, from the same walk, into `dist/<instance>-notebooklm/` — a folder
   and not an archive, because NotebookLM accepts Word, plain text, Markdown, PDF, CSV,
   PowerPoint, ePub, images, audio and URLs, and no archive among them.

   Run `python3 .claude/skills/companygraph-export/build.py` from the instance root. It is a
   script and not a procedure followed by hand because the failure the second artifact exists
   to catch is a bundle that went quietly stale, and a rendering nobody can re-run cheaply is
   a rendering that will be stale again. What it does, so a reader can hold it to this:

   One source per content area, named for the area — one per type folder under `model/`, one
   for `meta/`, one for each singular entity such as `model/identity.md`. That is the cut the
   agent bundle already makes, so the two artifacts are grouped alike, and it is the cut an
   instance gets until it says otherwise: a grouping keyed to anything the instance has not
   declared for every entity cuts by what a pattern happens to match rather than by what the
   model says, which is an editorial decision taken by a glob. A title raises the folder name's
   first letter and leaves the rest as the folder spells it, because the title is what a
   citation carries.

   An instance with a narrative to make declares its own grouping in
   `export/notebooklm-sources.md`, and the mechanism stays for it: each `##` heading is a
   source's title and its H1, the file name is that title lowercased with whitespace turned to
   dashes, so a `##` heading cannot reintroduce a capital any more than a folder name does, the
   paths under it claim entities and may glob, the paragraph under it opens the file, and an
   entity no heading claims goes to a source named for the folder it sits in — `experiences` and
   never `profiles`, because `model/profiles/` is the one folder the walk recurses into, so the
   root type there is not the entity's type. This instance ships no declaration.

   Two documents ship as sources beside the sources that carry entities:
   `export/notebooklm-AGENTS.md` as the bundle's `AGENTS.md`, and the repository's own
   `README.md`, both copied whole. The reading guide is what tells a reader that references
   between entities are by name and what a claim rests on, and a guide that lives outside the
   bundle is a guide this reader never sees. Neither is an entity, neither carries a marker,
   and a declared source may not take either name.

   A count a document states is generated and never typed. A document writes `{{entities}}`,
   `{{sources}}`, or `{{count:<source title>}}` and `{{count:<path under the root>}}` where a
   number goes, and the build substitutes what it counted on this run. A guide telling a reader
   36 experiences beside a bundle holding 37 is exactly the staleness the second artifact exists
   to catch, and nothing else would catch it: a document holds no marker, so the verifier has no
   opinion about it. A token that resolves to nothing is left standing and fails the build
   before anything is written, because `{{count:Skils}}` shipped to a reader is worse than a
   build that stops.

   Each source is then written as:

   - `# <the source's title>`, and one sentence saying what the source holds and when to read
     it. The title is what a citation carries and keeps its spaces and its capital,
     `Experience kinds`; the file name is that title lowercased, with every run of whitespace
     turned to a single dash, `experience-kinds.md`, because a space or a capital in a file name
     is awkward to type, to quote in a shell and to read in a directory listing. A name the
     export invents this way is spelled the way the folder it came from spells it, so the file
     name and that folder are the same string. The sentence is what NotebookLM's per-source
     summary is built from and the first thing a reader of the source list sees. Where the
     instance declares its own grouping the sentence is the one the declaration wrote;
   - the folder's `README.md` when there is one, less an opening H1 that only repeats the title
     the source has just written; a heading that differs is saying something and stays. It is
     context and never an entity — it says how the folder is laid out and against which schema
     each file is written — so it carries no marker and is counted by neither the build nor the
     verifier. Under `meta/` as much as under `model/`;
   - then every entity the source holds, each preceded by a line
     `<!-- entity: <path from the repository root> -->` and reproduced verbatim: the
     frontmatter fence, the entity's own H1 and the body, nothing dropped, reordered,
     demoted or rewritten. The marker is the separator; nothing else goes between two entities.

   Verbatim because every rewriting loses something a reader could have been answered from, and
   the frontmatter loses the most. Prose made from it dropped fields on the way out, and the 45
   skills the LIKE MAGIC role names became 1,012 characters of one sentence where the file has
   a list a reader can follow, entry by entry, to the skill that holds each claim. This reader
   handles Markdown; it does not need the model translated for it, and the model is the thing
   the bundle is for.

   Entities are ordered shallowest first and then by path, so a profile leads the experiences
   it owns rather than arriving 36 entities after the first of them.

   Two sources may not share a file name: one file would overwrite the other and the entities in
   the loser would leave the bundle with the run still reporting success, which is the way a
   bundle goes quietly short. The build fails instead, before it writes anything, and names the
   file both wanted. A declared pattern matching nothing on disk fails the same way and for the
   same reason: a renamed folder would empty a source and drop it without a word, and the
   verifier would still pass because it holds the bundle against the model and not against the
   declaration.

   Verify: `./export/notebooklm-verify` exits 0. It asserts every walked entity appears in
   exactly one source, no source exceeds 500,000 words and the folder holds at most 50 files.

8. Remove the staging directory. `dist/` is gitignored; neither artifact is ever committed.

   The assertion that both artifacts are the model, whole, is running
   `./export/notebooklm-verify`, not counting lines. A marker count cannot tell a file that
   carries no marker because it is copied whole from a file that carries no marker because an
   entity is missing, and it cannot tell a real `<!-- entity: … -->` from one a reading guide
   uses as a prose example of itself — a naive count of both artifacts against the repository
   raises exactly that false alarm on a correct export, and a check that cries wolf on a
   correct export is a check the next operator learns to skip. The verifier reads paths
   instead: every entity the zip and the bundle each carry, compared against the model's own
   and against each other. Its final line names what it checked —
   `PASS  11 sources, 133 entities, largest 15,383 words; zip agrees` when both artifacts hold,
   `zip not built` in its place when only the bundle was rebuilt, and a `FAIL` line naming the
   path that does not agree when one of them is wrong.

   A difference is the failure this design exists to catch — a bundle built two days ago and
   five experiences short reads as correct and is not.
