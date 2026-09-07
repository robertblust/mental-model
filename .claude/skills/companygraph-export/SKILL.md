---
name: companygraph-export
description: Package this CompanyGraph instance twice — dist/<instance>-skill.zip for an agent, dist/<instance>-notebooklm/ for NotebookLM. One walk, two renderings, the same entity count asserted against both.
allowed-tools: Bash(*)
---

# companygraph-export

Two artifacts from one walk of the model, because the two readers want the same facts in
different shapes. `dist/mental-model-skill.zip` is uploadable as an organization or personal
skill: `SKILL.md` at the root, `model/<type>.md` per root type folder, `model/meta.md`.
`dist/mental-model-notebooklm/` is a flat folder of Markdown sources, grouped the way
`export/notebooklm-sources.md` says and rendered for a host who reads them aloud.

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

   It reads `export/notebooklm-sources.md` when it exists: each `##` heading is a source's file
   name, the paths under it claim entities, and an entity no heading claims goes to a source
   named for its own type folder — `experiences` and never `profiles`, because
   `model/profiles/` is the one folder the walk recurses into, so the root type there is not
   the entity's type. Absent the file entirely, which is where an instance starts, the cut is
   by root type instead: one source per type folder under `model/`, one for `meta/` and one
   for each singular entity such as `model/identity.md`, which is the cut the agent bundle
   already makes — so the two artifacts are grouped alike until the instance says otherwise.
   A fallback title raises the folder name's first letter and leaves the rest as the folder
   spells it, because the title is what a citation carries.

   It writes `<title>.md` per source, the heading text verbatim, and nothing else in the
   folder. Two sources may not share a title: one file would overwrite the other and the
   entities in the loser would leave the bundle with the run still reporting success, which is
   the way a bundle goes quietly short. The build fails instead, before it writes anything, and
   names the file both wanted. A pattern matching nothing on disk fails the same way and for the
   same reason: a renamed folder would empty a source and drop it without a word, and the
   verifier would still pass because it holds the bundle against the model and not against the
   declaration.

   Each source opens with its heading as an H1 and the paragraph the declaration wrote under
   it, because that paragraph is what NotebookLM's per-source summary is built from and the
   first thing a reader of the source list sees. Then each entity it claims, in the order the
   declaration writes its globs and, inside one glob, in path order — because the order a
   declaration writes is an argument. `How this model works` opens on the five kinds an
   experience can be and closes on the schema underneath them; path order alone sorts `meta/**`
   ahead of `model/**` and opens it on the schema, which is the appendix reaching the reader
   before the point:

   - the `<!-- entity: <path> -->` marker, kept — this reader strips comments, so it costs the
     listener nothing and it is what `export/notebooklm-verify` reads coverage from. A folder's
     `README.md` describes the repository's layout rather than a thing in the model, so it is
     left out of the bundle, under `meta/` as much as under `model/`. Claiming one would make
     the bundle and the model disagree by every README a pattern happened to match;
   - every heading in the entity shifted down one level, so the file's own H1 is the source,
     the entity's name is an H2 and the entity's own sections sit under it rather than beside
     it. Demoting the H1 alone would leave an entity's `## Achievements` a sibling of the
     entity it belongs to, which says the opposite of what the demotion is for. A `#` inside a
     fenced code block is code and stays where it is;
   - its `>` tagline directly under that heading, untouched: one sentence written to stand
     alone is what a host reads aloud;
   - a dateline in place of the frontmatter, leading with
     `<Kind> · <organization> · <start>–<end>` — dropping a field the entity does not carry
     and writing `<start>` alone where start equals end. A date is written the way
     `WRITING.md` writes one, Oct 1999 and May 4, 2012, and a range is closed the way
     `WRITING.md` closes one, Oct 1999–Mar 2001, because the source is read aloud and nobody
     says `1999-10`. Every other field that carries a fact about the subject follows on
     the same line, labeled and in the order the file wrote it — `Group: AI`, `URL: …`, a block
     sequence as a comma-separated list. Labeled because `AI` standing alone says nothing where
     `Group: AI` does, and carried at all because a fact the agent bundle holds and the folder
     drops is a listener answering from less than the model knows. `skills` is the one field
     that leaves the dateline for a line of its own directly under it: a role can claim
     forty-five of them, and a thousand characters on one line is neither read to the end nor
     read aloud. `source`, `source-id` and `rank` are the exception and never travel: they say
     which system masters the page and how the ladder is ordered, which is a validator's
     business, and `Source: Local` read aloud on every entity is bookkeeping. Coverage is of
     entities, which the marker carries, and not of frontmatter keys;
   - then the body as it is.

   Verify: `./export/notebooklm-verify` exits 0. It asserts every walked entity appears in
   exactly one source, no source exceeds 500,000 words and the folder holds at most 50 files.
8. Remove the staging directory. `dist/` is gitignored; neither artifact is ever committed.
   The two artifacts carry the same entity count as each other and as the repository:
   `find model -name '*.md' ! -name README.md | wc -l` plus
   `find meta -name '*.md' ! -name README.md | wc -l`. The README is excluded on both halves
   because it is never an entity on either, and the core vendored under `meta/` carries none
   today: the day a release ships one, a count without the exclusion disagrees with both
   artifacts and the hand-run check is the thing that looks wrong.
   A difference is the failure this design exists to catch — a bundle built two days ago and
   five experiences short reads as correct and is not.
