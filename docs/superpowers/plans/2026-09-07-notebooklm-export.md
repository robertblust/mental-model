# NotebookLM export implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `companygraph-export` produces a second artifact, `dist/mental-model-notebooklm/`, carrying the whole model in a shape NotebookLM can cite — eleven Markdown sources, every entity reproduced exactly as it is written on disk — and verified against the model by a script.

**Architecture:** One walk, two renderers. The existing skill already walks `model/` and counts entities; it gains a second rendering and a second output. The second rendering is `.claude/skills/companygraph-export/build.py`, a script rather than a procedure followed by hand, because the failure this artifact exists to catch is a bundle that went quietly stale and a rendering nobody can re-run cheaply will be stale again. It cuts the model by root type — one source per type folder under `model/`, one for `meta/`, one for each singular entity — which is the cut the agent bundle already makes, so a reader moving between the two artifacts meets the same names. Two documents ship beside those sources: the bundle's `AGENTS.md`, written here as `export/notebooklm-AGENTS.md`, and the repository's own `README.md`. A new `export/notebooklm-verify` asserts that the bundle is the model whole — that is the test, and it is written before the bundle exists.

**Tech Stack:** Markdown, `sh`, `python3` (stdlib only — numpy is not installed on this machine). The export is a Claude skill procedure and `SKILL.md` is its implementation, with the NotebookLM rendering delegated to the one script inside it.

**Spec:** `docs/specs/2026-09-07-notebooklm-export.md`

## Global constraints

- Branch `notebooklm-export`, already carrying the spec at `84db93f`. Everything here lands on it so it can be tested as one thing.
- `sh conventions/conventions-check` must pass before every commit. `docs/superpowers/` is excluded from it; `docs/specs/` and `export/` are not.
- Run the mechanical validation before every commit — vendored hashes, one H1 per entity, R12 filenames. Nothing here touches `model/` or `meta/`, so the schema and reference rules cannot change state.
- `dist/` is gitignored. Neither artifact is ever committed.
- Coverage is identical in both artifacts. Cutting content from the NotebookLM bundle is out of scope by decision of the spec.
- **Nothing below the source title is rewritten.** The rendering decides the grouping, the file names and the sentence that opens each file; an entity travels from disk byte for byte — frontmatter fence, its own H1, body. This reader parses Markdown, so a page translated on the way out is a second version of the model that has to be kept true, and it answers from it less well than from the page itself.
- No declaration file ships. This instance takes the root-type cut, and `export/notebooklm-sources.md` stays a mechanism `build.py` carries for an instance that has a narrative to make. A grouping keyed to anything the instance has not declared for every entity is a cut made by whatever a pattern happens to match.
- Prose in `export/*.md` follows `conventions/WRITING.md`: sentence case headings, spaced em-dash, curly quotes, no serial comma, American English, a reason beside every rule.
- mental-model is the handmade reference instance. Nothing here is proposed to `companygraph/meta-model` until the export has run and its output has been read.

---

### Task 1: The verifier, failing

**Files:**
- Create: `export/notebooklm-verify`
- Create: `export/README.md`

**Interfaces:**
- Produces: `export/notebooklm-verify [bundle-dir]`, default `dist/mental-model-notebooklm`. Exit 0 on pass, 1 on failure, printing one line per finding. Task 3 runs it as its green step.

- [ ] **Step 1: Write the verifier**

```python
#!/usr/bin/env python3
"""Assert that a NotebookLM bundle is the model, whole.

Coverage is the whole point of the second artifact, and it is checkable only because each
inlined entity keeps its `<!-- entity: <path> -->` marker: NotebookLM strips the comment, and
this script reads the file from disk where it survives.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUNDLE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist/mental-model-notebooklm"
SOURCE_CAP, WORD_CAP = 50, 500_000          # NotebookLM, free tier, per notebook and per source

# Two sources carry documents about the model rather than entities of it: the reading guide the
# bundle ships as `AGENTS.md` and the repository's own `README.md`. They count against the source
# cap like any other file and hold no marker, so they are not read for coverage — a stray
# `<!-- entity: ... -->` in either would otherwise be reported as an entity the model does not
# have.
DOCUMENTS = {"AGENTS.md", "README.md"}

def model_entities():
    """Every file the export walks: model entities, plus the vendored meta it carries.

    A README is excluded on both halves of the walk. `meta/` carries none today, so leaving it
    in matched nothing and the asymmetry was invisible — until a core release adds one, when
    the bundle would have to claim it to pass.
    """
    out = {str(p.relative_to(ROOT)) for p in (ROOT / "model").rglob("*.md") if p.name != "README.md"}
    out |= {str(p.relative_to(ROOT)) for p in (ROOT / "meta").rglob("*.md") if p.name != "README.md"}
    return out

def bundle_entities(files):
    seen = {}
    for f in files:
        if f.name in DOCUMENTS:
            continue
        for m in re.finditer(r"<!--\s*entity:\s*(\S+?)\s*-->", f.read_text(encoding="utf-8")):
            seen.setdefault(m.group(1), []).append(f.name)
    return seen

def main():
    if not BUNDLE.is_dir():
        print(f"FAIL  no bundle at {BUNDLE}"); return 1
    files = sorted(BUNDLE.glob("*.md"))
    if not files:
        print(f"FAIL  {BUNDLE} holds no .md source"); return 1

    want, seen = model_entities(), bundle_entities(files)
    missing = sorted(want - set(seen))
    extra = sorted(set(seen) - want)
    twice = sorted(p for p, w in seen.items() if len(w) > 1)
    bad = False

    for p in missing: print(f"FAIL  not in the bundle: {p}"); bad = True
    for p in extra:   print(f"FAIL  in the bundle, not in the model: {p}"); bad = True
    for p in twice:   print(f"FAIL  claimed by {len(seen[p])} sources: {p} — {', '.join(seen[p])}"); bad = True

    if len(files) > SOURCE_CAP:
        print(f"FAIL  {len(files)} sources, cap is {SOURCE_CAP}"); bad = True
    for f in files:
        n = len(f.read_text(encoding="utf-8").split())
        if n > WORD_CAP:
            print(f"FAIL  {f.name} is {n:,} words, cap is {WORD_CAP:,}"); bad = True

    print(f"{'FAIL' if bad else 'PASS'}  {len(files)} sources, {len(want)} entities, "
          f"largest {max(len(f.read_text(encoding='utf-8').split()) for f in files):,} words")
    return 1 if bad else 0

sys.exit(main())
```

Two of the bundle's files carry a document about the model rather than entities of it, so
`DOCUMENTS` names them and the coverage scan skips them: they hold no marker, and a stray
`<!-- entity: … -->` in either would otherwise be reported as an entity the model does not
have. They still count against the source cap, because NotebookLM counts them.

A README is excluded on both halves of the walk. `meta/` carries none today, so leaving it in
matched nothing and the asymmetry was invisible — until a core release adds one, when the
bundle would have to claim it to pass.

- [ ] **Step 2: Make it executable and run it to verify it fails**

```bash
cd ~/git/robertblust/mental-model && chmod +x export/notebooklm-verify && ./export/notebooklm-verify
```

Expected: `FAIL  no bundle at .../dist/mental-model-notebooklm`, exit 1. This is the red state the rest of the plan turns green.

- [ ] **Step 3: Write `export/README.md`**

```markdown
# Export inputs

What `companygraph-export` reads from the instance when it builds the two artifacts. The skill
holds the procedure; this folder holds what is true of this instance and not of CompanyGraph.

- `SKILL-intro.md` — the paragraph that opens the agent skill, in the instance's own voice.
- `notebooklm-AGENTS.md` — the reading guide the NotebookLM bundle ships as its `AGENTS.md`:
  what the notebook is, what each source holds, that references between entities are by name,
  and what a claim in the model rests on. A reader who opens a notebook cold has no other way
  to learn any of it. Every count it states is a `{{...}}` token the build substitutes with what
  it counted, so the guide cannot tell a reader 36 experiences beside a bundle holding 37.
- `notebooklm-verify` — asserts a built bundle is the model, whole. Run it after every export;
  a bundle is worth nothing if it is quietly short, which is how the first one went stale.

A `notebooklm-sources.md` beside these would group the entities into sources of the instance's
own naming, one `##` heading per source. This instance writes none, so the export cuts the
model by its own root types: a grouping keyed to anything the model has not declared for every
entity is a cut made by whatever a pattern happens to match.
```

The guide bullet names `export/notebooklm-AGENTS.md`, which Task 2 writes. The folder's README
says what the folder holds, and the guide is the next thing to arrive in it.

- [ ] **Step 4: Check the prose and commit**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add export/notebooklm-verify export/README.md
git commit -m "The bundle gets a verifier before it gets a builder"
```

---

### Task 2: The reading guide

**Files:**
- Create: `export/notebooklm-AGENTS.md`

**Interfaces:**
- Consumes: nothing on disk. Every count it states is a `{{…}}` token that Task 3's build substitutes from what it counted on the run that ships the file.
- Produces: the document the build copies into the bundle as `AGENTS.md`.

NotebookLM strips comments, so the entity marker that tells an agent where a page begins says
nothing to this reader, and it has no convention to be told. What a reader who opens the
notebook cold needs to know — that a source is a stack of whole pages, that an entity's H1 is
its name, that references between entities are by name and not by link, and what a claim in
this model rests on — has to be in the notebook, because a guide that lives outside the bundle
is a guide that reader never sees. So the guide is a source.

It is the instance's own file rather than something the export writes, because the mastership
rules it carries are this repository's, drawn from its own `AGENTS.md`. What the export owns is
the arithmetic: a count stated in prose is a count nothing checks, since a document holds no
marker and the verifier has no opinion about it, so a guide could say 36 experiences beside a
bundle holding 37 and pass. Every number is therefore a token.

- [ ] **Step 1: Write the guide**

```markdown
# Robert Blust — mental model

> One person described in CompanyGraph: a profile and the {{count:model/profiles/robert-blust/experiences}} experiences it owns, the {{count:Skills}}
> skills those experiences evidence, the values the work is held to and the schema underneath
> all of it. This notebook is that model whole — {{entities}} entities across {{sources}} sources, every page
> as it is written in the repository it is mastered in.

The model answers questions about one working life. What he built and where, what a period
contained and what came out of it, which capability a piece of work shows, at what level a skill
is claimed and on what evidence, why a career break is filed as an experience rather than a gap,
and what he holds to while deciding. A question about a claim is the one this model is shaped
for: every skill claimed names the work that shows it, and every experience names the skills it
evidences, so the answer to “on what basis” is in the model rather than in a summary of it.

What is not here is not withheld and not hidden. There is no salary, no assessment written by
anyone else and no scan of a diploma or an employment reference, for the reason the last section
gives.

## The sources

Two of these sources carry documents about the model — this guide and the repository's README.
The rest carry its {{entities}} entities.

| File | Contains | Read it when you need to |
| --- | --- | --- |
| `AGENTS.md` | this guide | Read anything else here |
| `README.md` | the repository's README | See how the model is laid out and licensed |
| `Profiles.md` | the profile and its {{count:model/profiles/robert-blust/experiences}} experiences, {{count:Profiles}} entities | Ask what he did, where, when and what it produced |
| `Skills.md` | {{count:Skills}} skills, one per capability | Look up what a capability is and what practicing it looks like |
| `Values.md` | {{count:Values}} values | Ask how he decides and what he refuses |
| `Experience kinds.md` | the {{count:Experience kinds}} kinds an experience can be | Understand why a break, a talk or a degree is filed as it is |
| `Proficiency levels.md` | the {{count:Proficiency levels}} rungs a skill is claimed on | Weigh what Expert or Competent means here |
| `Sources.md` | the {{count:Sources}} source the pages are mastered in | Check where a fact would be corrected |
| `Identity.md` | who the model is about | Find the name, the location and the public addresses |
| `Vision.md` | the future the model works toward | Ask what the work is building toward |
| `Meta.md` | CompanyGraph core: its conventions and its schemas, {{count:Meta}} entities | Check what a page must carry and how a reference resolves |

## How to read the model

A source is a stack of whole pages. Each one begins at a line reading
`<!-- entity: model/skills/java.md -->`, which names the file it comes from; then comes the
page, unchanged. Its frontmatter fence carries the fields a validator reads — the kind of
experience, the organization, the start and end dates, the group a skill belongs to, the skills
an experience evidences. The `#` heading under the fence is the entity's name, and that name is
the handle everything else uses.

**References between entities are by name, not by link.** An experience's `skills:` list names
skill entities that live in `Skills.md`, spelled exactly as their headings spell them. The
Skills table in the profile in `Profiles.md` claims each of those skills at a level and gives an
Evidence cell naming the experiences that show it, one sentence per experience, in the order
they happened. A skill page itself claims nothing about him: it defines the capability and says
what practicing it looks like, because the level and the evidence are one person's and belong in
the profile. To follow a claim, take the name and find the heading.

`Meta.md` holds the rules every entity obeys — which fields a page of each type must carry, how
a date is written, and the rule that a reference naming something that does not exist is an
error rather than a note. Read it when an answer turns on whether the model is allowed to say
something, not on what it says.

## What a claim rests on

Every page here is mastered in this repository. There is no upstream system to correct first: a
fact that is wrong is corrected here and nowhere else, which is why every page carries
`source: Local`.

A fact enters from Robert Blust or from a document — a record, a deck, a published page. A
document that is public is linked, in a `url` field or a `## References` row: a talk's
recording, a published case study, a commercial register entry. **A document that is private is
deliberately not held here.** Employment references, diplomas and certifications are the source
of dates and of what a period contained, they are read when a page is written, and they stay in
his own vault and are shown on request. So an entry whose evidence is private carries the fact
and no link, and that missing link is a decision rather than a gap: read it as a claim its
author can produce a document for, not as a claim with nothing behind it.
```

- [ ] **Step 2: Check that every token names something the build can count**

```bash
cd ~/git/robertblust/mental-model && grep -o '{{[^}]*}}' export/notebooklm-AGENTS.md | sort -u
```

Expected, ten distinct tokens:

```
{{count:Experience kinds}}
{{count:Meta}}
{{count:Proficiency levels}}
{{count:Profiles}}
{{count:Skills}}
{{count:Sources}}
{{count:Values}}
{{count:model/profiles/robert-blust/experiences}}
{{entities}}
{{sources}}
```

Seven of them name a source by the title the export will give it, which is the folder name with
its first letter raised. One names a path under the repository root, and it exists for the one
number no source holds: `Profiles.md` carries 37 entities, and the guide says a profile and the
36 experiences it owns. The remaining two are the totals. A misspelled title is not caught by
this grep and is not meant to be — it is caught in Task 3, where the build refuses to write a
bundle with a token nothing resolves.

- [ ] **Step 3: Check the prose and commit**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add export/notebooklm-AGENTS.md
git commit -m "The bundle carries the guide a stripped reader cannot do without"
```

---

### Task 3: The export builds both artifacts

**Files:**
- Create: `.claude/skills/companygraph-export/build.py`
- Modify: `.claude/skills/companygraph-export/SKILL.md`

**Interfaces:**
- Consumes: `export/notebooklm-AGENTS.md` from Task 2 and the repository's `README.md` as the two documents, `export/notebooklm-verify` from Task 1 as the green step, and `export/notebooklm-sources.md` when an instance writes one — this one does not.
- Produces: `dist/mental-model-skill.zip` unchanged, and `dist/mental-model-notebooklm/` — a flat folder of `.md` files, one per source, no archive.

The script lives with the skill rather than in `export/`, because shape belongs to the tool and
`export/` holds the instance's own inputs.

- [ ] **Step 1: Write the renderer**

The renderer is `.claude/skills/companygraph-export/build.py`, 377 lines, and it is not copied
here. A plan that pastes a file the repository already holds is a second copy nothing keeps in
step, which is the drift this whole branch was written to close. Read it there. What it must do,
and what a reviewer holds it to:

- Cut by root type when no declaration exists: one source per type folder under `model/`, one
  for `meta/`, one per singular entity, plus `AGENTS.md` and `README.md` as documents.
- Precede every entity with `<!-- entity: <path from the repository root> -->` and reproduce it
  verbatim after that — frontmatter fence, its own H1, body, nothing dropped, reordered or
  demoted. The marker is the boundary because a bare `---` is not: 69 skills carry 207 of them
  and nothing says which 69 are boundaries.
- Treat a folder's `README.md` as context and never as an entity, so it carries no marker, and
  drop its H1 where that repeats the source's own title.
- Substitute every `{{…}}` token in the reading guide from what the walk counted, and fail
  before writing anything if a token survives.
- Fail on a declaration pattern that matches nothing, and on two sources wanting one file name.
- Sort nothing by filesystem enumeration order, so two consecutive builds are byte-identical.

- [ ] **Step 2: Rewrite the skill's frontmatter and its opening paragraph**

Replace the `description` line with:

```
description: Package this CompanyGraph instance twice — dist/<instance>-skill.zip for an agent, dist/<instance>-notebooklm/ for NotebookLM. One walk, two renderings, the same entity count asserted against both.
```

And the paragraph under the `# companygraph-export` heading with:

```markdown
Two artifacts from one walk of the model, because the two readers want the same facts in
different shapes. `dist/mental-model-skill.zip` is uploadable as an organization or personal
skill: `SKILL.md` at the root, `model/<type>.md` per root type folder, `model/meta.md`.
`dist/mental-model-notebooklm/` is a flat folder of Markdown sources, one per content area,
carrying the model's own pages as they are written.
```

Steps 1 to 6 of the procedure are untouched. The agent bundle is unchanged by this plan, and
its own reasoning about the `<!-- entity: … -->` marker in step 3 is where it was.

- [ ] **Step 3: Add the NotebookLM rendering as a new step 7, before the current step 7**

```markdown
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
   source's file name, the paths under it claim entities and may glob, the paragraph under it
   opens the file, and an entity no heading claims goes to a source named for the folder it
   sits in — `experiences` and never `profiles`, because `model/profiles/` is the one folder
   the walk recurses into, so the root type there is not the entity's type. This instance ships
   no declaration.

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

   - `# <the file's name without .md>`, and one sentence saying what the source holds and when
     to read it. That sentence is what NotebookLM's per-source summary is built from and the
     first thing a reader of the source list sees. Where the instance declares its own grouping
     the sentence is the one the declaration wrote;
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
```

- [ ] **Step 4: Renumber the old step 7 to 8 and extend its verification**

```markdown
8. Remove the staging directory. `dist/` is gitignored; neither artifact is ever committed.
   The two artifacts carry the same entity count as each other and as the repository:
   `find model -name '*.md' ! -name README.md | wc -l` plus
   `find meta -name '*.md' ! -name README.md | wc -l`. The README is excluded on both halves
   because it is never an entity on either, and the core vendored under `meta/` carries none
   today: the day a release ships one, a count without the exclusion disagrees with both
   artifacts and the hand-run check is the thing that looks wrong.
   A difference is the failure this design exists to catch — a bundle built two days ago and
   five experiences short reads as correct and is not.
```

- [ ] **Step 5: Run the build**

```bash
cd ~/git/robertblust/mental-model && python3 .claude/skills/companygraph-export/build.py
```

Expected, one line per file and the totals last:

```
     document  AGENTS.md
     document  README.md
   5 entities  Experience kinds.md
   1 entity    Identity.md
  10 entities  Meta.md
   4 entities  Proficiency levels.md
  37 entities  Profiles.md
  69 entities  Skills.md
   1 entity    Sources.md
   5 entities  Values.md
   1 entity    Vision.md
 133 entities  in 11 sources under /Users/rob/git/robertblust/mental-model/dist/mental-model-notebooklm
```

- [ ] **Step 6: Run the verifier and expect it to pass**

```bash
cd ~/git/robertblust/mental-model && ./export/notebooklm-verify; echo "exit=$?"
```

Expected: `PASS  11 sources, 133 entities, largest 15,383 words`, exit 0. 133 is 123 model entities plus the 10 Markdown files under `meta/`, and both numbers are `find model -name '*.md' ! -name README.md | wc -l` and `find meta -name '*.md' ! -name README.md | wc -l` on the day this was written. A different total is not a failure by itself — it means the model grew, and the verifier is asserting the new number against the bundle, which is its job. The word count moves with the model too.

- [ ] **Step 7: Check the build is a function of the model and nothing else**

```bash
cd ~/git/robertblust/mental-model && cp -R dist/mental-model-notebooklm /tmp/nb-first
python3 .claude/skills/companygraph-export/build.py > /dev/null && diff -r /tmp/nb-first dist/mental-model-notebooklm && rm -rf /tmp/nb-first
```

Expected: no output. A rendering that differs between two runs over an unchanged model is a rendering whose output nobody can compare, which is the whole apparatus of this plan defeated.

- [ ] **Step 8: Check that no token reached the bundle, and that the guide arrived whole**

```bash
cd ~/git/robertblust/mental-model && grep -rn '{{' dist/mental-model-notebooklm/ ; echo "tokens=$?"
sed -n '1,12p' dist/mental-model-notebooklm/AGENTS.md
```

Expected: `tokens=1`, grep finding nothing, and the guide's opening blockquote reading 36, 69, 133 and 11 as numbers. Then prove the failure works, because a check nobody has seen fail is a check nobody knows the state of:

```bash
cd ~/git/robertblust/mental-model && printf '\n{{count:Skils}}\n' >> export/notebooklm-AGENTS.md
python3 .claude/skills/companygraph-export/build.py; echo "exit=$?"
git checkout export/notebooklm-AGENTS.md
```

Expected: ``FAIL  export/notebooklm-AGENTS.md: nothing counts `{{count:Skils}}` ``, exit 1, and the bundle on disk untouched — the substitution and its check both run before the old folder is removed, so a failed build leaves the last good bundle in place.

- [ ] **Step 9: Read one source end to end**

```bash
cd ~/git/robertblust/mental-model && sed -n '1,40p' dist/mental-model-notebooklm/Profiles.md
```

The file opens `# Profiles`, then the export's own sentence saying what the source holds and when to read it, then `model/profiles/README.md` as context with its repeated `# Profiles` dropped, then the first marker and `model/profiles/robert-blust/robert-blust.md` exactly as it is on disk: the `---` fence, `source: Local`, the `# Robert Blust` H1, the `>` tagline, the Skills table. The profile leads the 36 experiences it owns because entities are ordered shallowest path first. If any of that is false, fix the script and re-run rather than patching the output.

- [ ] **Step 10: Commit**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add .claude/skills/companygraph-export/build.py .claude/skills/companygraph-export/SKILL.md
git commit -m "The export renders the model twice, for two readers"
```

---

### Task 4: Settle the spec and the brief

**Files:**
- Modify: `docs/specs/2026-09-07-notebooklm-export.md`
- Modify: `../communication/posts/2026-09-15-blust-ch/wip/notebooklm-context.md`
- Modify: `../communication/posts/2026-09-15-blust-ch/wip/README.md`

**Interfaces:**
- Consumes: the bundle from Task 3.

- [ ] **Step 1: Hold the spec against what shipped**

The spec is the authority the rest of this plan argues from, and it is correct. Read it and confirm it still says each of these, because every one of them is a decision the build would quietly reverse if it drifted:

- the difference between the two artifacts is the container and the grouping, and the coverage assertion is identical for both;
- the export cuts the model by root type, and a grouping keyed to anything the instance has not declared for every entity is a cut made by whatever a pattern happens to match;
- an entity is preceded by its marker and reproduced exactly as it is written on disk, no field dropped or reordered and no heading moved;
- the marker is kept and is the only thing between two entities, because on disk it is an unambiguous boundary where a bare `---` is not and it is what makes coverage checkable;
- the declaration mechanism stays for an instance with a narrative to make, in `export/notebooklm-sources.md` and not `.json`, because the export is a procedure an agent follows rather than a program parsing config and Markdown lets each source carry the sentence saying why it is one source;
- two documents ship as sources of their own, and every count a document states is generated on the run that ships it.

No edit is expected. If one is needed, the spec is what changes and the code follows it.

- [ ] **Step 2: Point the timeline brief at the sources the export makes**

The brief at `../communication/posts/2026-09-15-blust-ch/wip/notebooklm-context.md` steers NotebookLM by naming sources, so a name that no longer exists is a source the hosts cannot open. Replace the paragraph naming sources with one naming the eleven this bundle holds, and keep the instruction that the source on how the model is built is quoted rather than summarized — that source is now `Meta.md`, with the kinds and the levels in `Experience kinds.md` and `Proficiency levels.md` beside it. `communication` is private, has no remote and never gets one.

- [ ] **Step 3: Replace the staleness check in the post's README**

The two-command check in `../communication/posts/2026-09-15-blust-ch/wip/README.md` compares the skill bundle's experience count against the model. Replace it with `./export/notebooklm-verify`, which asserts the same thing and more, and now exists. Check the same file for source names the export no longer makes.

- [ ] **Step 4: Commit both repositories**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add docs/specs/2026-09-07-notebooklm-export.md
git commit -m "The entity marker stays, because coverage has to be checkable"
cd ~/git/robertblust/communication
git add posts/2026-09-15-blust-ch/wip
git commit -m "The timeline brief names the sources the export now makes"
```

- [ ] **Step 5: Upload the bundle and read the source list**

Drag every file from `dist/mental-model-notebooklm/` into a new notebook, `AGENTS.md` and `README.md` included. The test is whether the source list reads as a list of subjects a brief can steer with, and whether a host asked how a claim is evidenced follows a skill's name from `Skills.md` to the Evidence cell in `Profiles.md`. A host that cannot make that hop has met the failure the guide exists to prevent, and the fix is `export/notebooklm-AGENTS.md`.

- [ ] **Step 6: Report the branch and stop**

`gh pr view 98` for the check, and stop. Merging is the owner's word, and the meta-model tooling spec is proposed only after this export has run and its output has been read.
