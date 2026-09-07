# NotebookLM export implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `companygraph-export` produces a second artifact, `dist/mental-model-notebooklm/`, carrying the whole model in a shape NotebookLM can cite, verified against the model by a script.

**Architecture:** One walk, two renderers. The existing skill already walks `model/` and counts entities; it gains a second rendering pass and a second output. A new `export/notebooklm-verify` asserts that the bundle is the model whole — that is the test, and it is written before the bundle exists. The instance declares its own source grouping in `export/notebooklm-sources.md`; absent a claim, an entity falls to its root type's source and the verifier says how many did.

**Tech Stack:** Markdown, `sh`, `python3` (stdlib only — numpy is not installed on this machine). The export is a Claude skill procedure, not a program: `SKILL.md` is the implementation and an agent following it is the runtime.

**Spec:** `docs/specs/2026-09-07-notebooklm-export.md`

## Global constraints

- Branch `notebooklm-export`, already carrying the spec at `84db93f`. Everything here lands on it so it can be tested as one thing.
- `sh conventions/conventions-check` must pass before every commit. `docs/superpowers/` is excluded from it; `docs/specs/` and `export/` are not.
- Run the mechanical validation before every commit — vendored hashes, one H1 per entity, R12 filenames. Nothing here touches `model/` or `meta/`, so the schema and reference rules cannot change state.
- `dist/` is gitignored. Neither artifact is ever committed.
- Coverage is identical in both artifacts. Cutting content from the NotebookLM bundle is out of scope by decision of the spec.
- Prose in `export/*.md` follows `conventions/WRITING.md`: sentence case headings, spaced em-dash, curly quotes, no serial comma, American English, a reason beside every rule.
- mental-model is the handmade reference instance. Nothing here is proposed to `companygraph/meta-model` until the export has run and its output has been read.

## Spec correction this plan makes

The spec's rendering rules say the `<!-- entity: <path> -->` marker is dropped from the NotebookLM bundle because that reader strips comments. **Keep it.** The reader strips it, so it costs the listener nothing; the verifier reads the file from disk, where the marker is the only thing that makes coverage checkable without re-deriving the grouping. Dropping it would leave the spec's central guarantee — the model, whole — provable only by counting words. Task 4 amends the spec section to say this.

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

def model_entities():
    """Every file the export walks: model entities, plus the vendored meta it carries."""
    out = {str(p.relative_to(ROOT)) for p in (ROOT / "model").rglob("*.md") if p.name != "README.md"}
    out |= {str(p.relative_to(ROOT)) for p in (ROOT / "meta").rglob("*.md")}
    return out

def bundle_entities(files):
    seen = {}
    for f in files:
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
- `notebooklm-sources.md` — how this instance's entities group into NotebookLM sources, and why
  each grouping is one source.
- `notebooklm-verify` — asserts a built bundle is the model, whole. Run it after every export;
  a bundle is worth nothing if it is quietly short, which is how the first one went stale.
```

- [ ] **Step 4: Check the prose and commit**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add export/notebooklm-verify export/README.md
git commit -m "The bundle gets a verifier before it gets a builder"
```

---

### Task 2: The instance declares its sources

**Files:**
- Create: `export/notebooklm-sources.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the declaration Task 3's procedure reads. Each `##` heading is a source's file name; the list under it is paths from the repository root, glob allowed.

- [ ] **Step 1: Write the declaration**

```markdown
# NotebookLM sources

> One heading per source, and the heading is the file name — which is the title a citation
> carries and the name a brief steers with, so it is written as a phrase a host would say. The
> paths under it are from the repository root and may glob. An entity no heading claims goes to
> its root type's source, which is the safe default and not a silent one: `notebooklm-verify`
> counts them.

## Robert Blust — the short version

Who the model is about, what it is for and what it holds to. A listener who reads one source
should read this one.

- `model/identity.md`
- `model/vision.md`
- `model/values/*.md`
- `model/profiles/robert-blust/robert-blust.md`

## How this model works

The five kinds an experience can be, the four rungs a skill is claimed at, and the schema
underneath both. The kinds argue for themselves — Independent says a career break spent
building products is neither a role nor a project — and that argument is the reason this is a
source rather than an appendix.

- `model/experience-kinds/*.md`
- `model/proficiency-levels/*.md`
- `model/sources/*.md`
- `meta/**/*.md`

## Skills, and the evidence for each

69 skills, each at a level, none of them claimed without an experience that shows it. Kept
whole and separate because the evidence column is the thing worth quoting.

- `model/skills/*.md`

## UBS, 1999–2015

Fifteen years and four roles at one employer, from the trainee program to the architect. One
source because the question a listener asks is about the fifteen years, not about one rung.

- `model/profiles/robert-blust/experiences/*-ubs-*.md`

## The career break, 2026

The four months, the tooling built during them and the two products that came out. The subject
of the first episode, and the reason a source is named for a period rather than a type.

- `model/profiles/robert-blust/experiences/2026-*.md`
```

- [ ] **Step 2: Check the declaration covers what it claims and nothing twice**

```bash
cd ~/git/robertblust/mental-model && python3 - <<'PY'
import re, pathlib, glob
txt = pathlib.Path("export/notebooklm-sources.md").read_text(encoding="utf-8")
blocks = re.split(r"^## ", txt, flags=re.M)[1:]
claimed, dup = {}, []
for b in blocks:
    title = b.splitlines()[0].strip()
    for pat in re.findall(r"^- `([^`]+)`", b, re.M):
        hits = [p for p in glob.glob(pat, recursive=True)
                if p.endswith(".md") and not p.endswith("README.md")]
        if not hits: print(f"DEAD PATTERN  {title}: {pat}")
        for h in hits:
            if h in claimed: dup.append((h, claimed[h], title))
            claimed[h] = title
for h, a, b_ in dup: print(f"CLAIMED TWICE  {h}: {a} and {b_}")
allm = {str(p) for p in pathlib.Path("model").rglob("*.md") if p.name != "README.md"}
allm |= {str(p) for p in pathlib.Path("meta").rglob("*.md")}
print(f"{len(claimed)} of {len(allm)} entities claimed; {len(allm - set(claimed))} fall back to their type")
PY
```

Expected: no `DEAD PATTERN`, no `CLAIMED TWICE`, and `107 of 133 entities claimed; 26 fall back to their type`. The 26 are the experiences no heading names. A README is not an entity — the verifier's entity set excludes `model/**/README.md`, so the pattern expansion here excludes it too, or the two disagree by the four READMEs sitting inside the globbed folders.

- [ ] **Step 3: Commit**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add export/notebooklm-sources.md
git commit -m "This instance says how its entities group into sources"
```

---

### Task 3: The export builds both artifacts

**Files:**
- Modify: `.claude/skills/companygraph-export/SKILL.md`

**Interfaces:**
- Consumes: `export/notebooklm-sources.md` from Task 2, `export/notebooklm-verify` from Task 1.
- Produces: `dist/mental-model-skill.zip` unchanged, and `dist/mental-model-notebooklm/` — a flat folder of `.md` files, one per source, no archive.

- [ ] **Step 1: Rewrite the skill's frontmatter and add the second output to step 6**

Replace the `description` line with:

```
description: Package this CompanyGraph instance twice — dist/<instance>-skill.zip for an agent, dist/<instance>-notebooklm/ for NotebookLM. One walk, two renderings, the same entity count asserted against both.
```

- [ ] **Step 2: Add the NotebookLM rendering as a new step 7, before the current step 7**

```markdown
7. The NotebookLM rendering, from the same walk, into `dist/<instance>-notebooklm/` — a folder
   and not an archive, because NotebookLM accepts Word, plain text, Markdown, PDF, CSV,
   PowerPoint, ePub, images, audio and URLs, and no archive among them.

   Read `export/notebooklm-sources.md` when it exists: each `##` heading is a source's file
   name, the paths under it claim entities, and an entity no heading claims goes to a source
   named for its root type. Absent the file, every source is a root type. Write
   `<title>.md` per source, the heading text verbatim, and nothing else in the folder.

   Each source opens with its heading as an H1 and the paragraph the declaration wrote under
   it, because that paragraph is what NotebookLM's per-source summary is built from and the
   first thing a reader of the source list sees. Then each entity it claims, in path order:

   - the `<!-- entity: <path> -->` marker, kept — this reader strips comments, so it costs the
     listener nothing and it is what `export/notebooklm-verify` reads coverage from. A folder's
     `README.md` is not an entity and never carries the marker: inline it as the source's
     opening context or leave it out, but do not claim it, or the bundle and the model disagree
     by every README a pattern happened to match;
   - the entity's H1 demoted to H2, so the file's own H1 is the source and the entities are
     its parts;
   - its `>` tagline directly under that heading, untouched: one sentence written to stand
     alone is what a host reads aloud;
   - a dateline in place of the frontmatter — `<Kind> · <organization> · <start> – <end>`,
     dropping a field the entity does not carry and writing `<start>` alone where start equals
     end. `source: Local` and `rank: 20` are instructions to a validator and noise to a host;
   - then the body as it is.

   Verify: `./export/notebooklm-verify` exits 0. It asserts every walked entity appears in
   exactly one source, no source exceeds 500,000 words and the folder holds at most 50 files.
```

- [ ] **Step 3: Renumber the old step 7 to 8 and extend its verification**

```markdown
8. Remove the staging directory. `dist/` is gitignored; neither artifact is ever committed.
   The two artifacts carry the same entity count as each other and as the repository:
   `find model -name '*.md' ! -name README.md | wc -l` plus `find meta -name '*.md' | wc -l`.
   A difference is the failure this design exists to catch — a bundle built two days ago and
   five experiences short reads as correct and is not.
```

- [ ] **Step 4: Run the export**

Invoke the `companygraph-export` skill from a session rooted in this repository, or follow its procedure by hand.

- [ ] **Step 5: Run the verifier and expect it to pass**

```bash
cd ~/git/robertblust/mental-model && ./export/notebooklm-verify
```

Expected: `PASS  6 sources, 133 entities, largest M words`, exit 0. 133 is 123 model entities plus the 10 Markdown files under `meta/`, and both numbers are `find model -name '*.md' ! -name README.md | wc -l` and `find meta -name '*.md' | wc -l` on the day this was written. A different total is not a failure by itself — it means the model grew, and the verifier is asserting the new number against the bundle, which is its job.

- [ ] **Step 6: Read one source end to end**

```bash
cd ~/git/robertblust/mental-model && sed -n '1,60p' "dist/mental-model-notebooklm/The career break, 2026.md"
```

The dateline reads as a sentence, the taglines survived, no YAML is visible, and the entity markers are present but say nothing to a reader. If any of those is false, fix step 2 and re-run rather than patching the output.

- [ ] **Step 7: Commit**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add .claude/skills/companygraph-export/SKILL.md
git commit -m "The export renders the model twice, for two readers"
```

---

### Task 4: Test it against real content, and settle the spec

**Files:**
- Modify: `docs/specs/2026-09-07-notebooklm-export.md`
- Modify: `../communication/posts/2026-09-15-blust-ch/wip/notebooklm-context.md`
- Modify: `../communication/posts/2026-09-15-blust-ch/wip/README.md`

**Interfaces:**
- Consumes: the bundle from Task 3.

- [ ] **Step 1: Upload the bundle to NotebookLM and read the source list**

Drag every file from `dist/mental-model-notebooklm/` into a new notebook. The test is whether the source list reads as a list of subjects: a title you would name in a brief, and a per-source summary that says what the source holds. A title that reads as a folder name is a failed grouping, and the fix is `export/notebooklm-sources.md`, not the brief.

- [ ] **Step 2: Amend the spec's rendering rules and its declaration format**

The spec drafts the declaration as `export/notebooklm-sources.json`. It is `.md` here, and the reason is the runtime: the export is a procedure an agent follows, not a program parsing config, and Markdown lets each source carry the sentence saying why it is one source — which is the sentence the rendering then uses as the file's opening paragraph. Replace `export/notebooklm-sources.json` with `export/notebooklm-sources.md` throughout the spec, and add that reason to the section that names it.

- [ ] **Step 2b: Amend the rendering rule about the marker**

Replace the bullet reading `The entity comment is dropped.` with:

```markdown
- The entity comment is kept. This reader strips comments, so it says nothing to a listener —
  and it is the only thing that makes coverage checkable from disk without re-deriving the
  grouping, which is the guarantee the second artifact exists to make.
```

- [ ] **Step 3: Point the timeline brief at the new source names**

In `notebooklm-context.md`, replace the paragraph beginning `The sources are the files of the mental-model skill bundle.` with this, so the brief steers with titles that exist:

```
The sources are the six of this notebook. Robert Blust — the short version says who the model
is about and what it is for. How this model works holds the five kinds an experience can be and
the four rungs a skill is claimed at, and it argues for them: quote it on how the model is
built, do not summarize it. Skills, and the evidence for each holds every claim with what shows
it. UBS, 1999–2015 and The career break, 2026 are the two periods named for themselves, and
Experiences holds the rest in the order they began. The timeline page is what these render
into: treat it as the model drawn, not as a source of its own.
```

- [ ] **Step 4: Replace the staleness check in the post's README**

The two-command check there compares the skill bundle's experience count against the model. Replace it with `./export/notebooklm-verify`, which asserts the same thing and more, and now exists.

- [ ] **Step 5: Commit both repositories**

```bash
cd ~/git/robertblust/mental-model && sh conventions/conventions-check
git add docs/specs/2026-09-07-notebooklm-export.md
git commit -m "The entity marker stays, because coverage has to be checkable"
cd ~/git/robertblust/communication
git add posts/2026-09-15-blust-ch/wip
git commit -m "The timeline brief names the sources the export now makes"
```

- [ ] **Step 6: Report the branch and stop**

`gh pr view 98` for the check, and stop. Merging is the owner's word, and the meta-model tooling spec is proposed only after this export has run and its output has been read.
