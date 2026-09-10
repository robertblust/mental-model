# Surface production Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A fifth skill, `companygraph-surface`, that produces the content of a surface into `dist/surfaces/` — a script for the facts and a procedure for the prose.

**Architecture:** `facts.py` walks `model/` once and writes `dist/surfaces/facts.json`, resolving only what any surface would want the same way: an entity's dates in the family's register, its `organization` with the identity as the default, its address and the sections a body could be written from. It routes nothing and orders nothing. `SKILL.md` carries the procedure that applies a surface's own rules to those facts, writes each unit and checks the result against the surface's constraints.

**Tech Stack:** Python 3 standard library only, matching `companygraph-export`. No test framework in this repository: a script is checked by running it and asserting its output, which is what `verify.py` does for the export.

**Spec:** `docs/specs/2026-09-10-surface-production.md`

## Global Constraints

- Python 3 standard library only. No dependency, no network. `companygraph-export/build.py` is the style to match, including its habit of explaining a decision in the docstring where a reader will meet it.
- **The script routes nothing and orders nothing.** Which kinds reach which unit and in what order are the surface's rules and its file is their only home. The test before adding any resolution: could two surfaces of the same model reasonably want it different? If yes it belongs to the file.
- Output goes to `dist/surfaces/`, which is gitignored through `dist/`. Nothing this skill produces is ever committed, and the reason is R17 rather than the build directory.
- Prose in `SKILL.md` follows `conventions/WRITING.md`: American English, spaced em-dashes, sentence case in headings, no serial comma. `sh conventions/conventions-check` enforces the spelling and dash rules.
- Dates follow the family's register: `Oct 2012` for a month, `May 4, 2012` for a day, `2012` for a year, and a range closed with an en-dash and no spaces, `May 2012–Oct 2016`.
- Nothing is committed unless the commands a task names have run and passed. Nothing is merged; each repository ends with a green pull request and stops.
- The design and this plan are on `robertblust/mental-model#105`. Implementation lands on that same branch, `surface-production`, at the owner's request.

---

### Task 1: The walk, the parse and the emit

**Files:**
- Create: `.claude/skills/companygraph-surface/facts.py`
- Test: run it and assert against the model

**Interfaces:**
- Produces: `dist/surfaces/facts.json` with the shape below. Task 2 adds resolutions to the same entity records, Task 3's procedure reads them.

```json
{
  "instance": "mental-model",
  "identity": { "name": "…", "tagline": "…", "fields": {…}, "sections": {"What it is": "…"} },
  "surfaces": [ { "name": "LinkedIn profile", "path": "model/surfaces/linkedin-profile.md" } ],
  "types": {
    "experience": [ { "name": "…", "path": "…", "tagline": "…",
                     "fields": { "kind": "Role", "start": "2022-04", "end": "2026-05", … },
                     "sections": { "Achievements": "…" } } ]
  }
}
```

- [ ] **Step 1: Write the script**

Create `.claude/skills/companygraph-surface/facts.py`:

```python
#!/usr/bin/env python3
"""The facts a surface is produced from, resolved once and decided nowhere.

A surface's file says which of the model's facts reach it, in what shape and in what order.
None of that is here. What is here is the reading a machine can do the same way for any
surface — open every entity, take its frontmatter, its H1, its tagline and its sections — so
that the procedure beside this file spends its attention on the rules rather than on parsing
Markdown.

The test for anything added below: could two surfaces of the same model reasonably want it
different? If yes it belongs in the surface's file, and putting it here would make the file's
rule the second copy — the one nobody reads.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(".")
OUT = ROOT / "dist" / "surfaces" / "facts.json"


def read(path):
    """Frontmatter, H1, tagline and sections of one entity file.

    The frontmatter these files carry is two shapes and no more: `key: value`, and a key whose
    value is a block sequence one entry per line (R11). A YAML library would read both and
    bring a dependency for it; this repository's other script has none and neither does this.
    """
    text = path.read_text(encoding="utf-8")
    fields, body = {}, text
    if text.startswith("---\n"):
        raw, _, body = text[4:].partition("\n---\n")
        key = None
        for line in raw.splitlines():
            if line.startswith("  - ") and key:
                fields.setdefault(key, []).append(line[4:].strip())
            elif ":" in line:
                key, _, value = line.partition(":")
                key, value = key.strip(), value.strip()
                if value:
                    fields[key] = value
    name = tagline = ""
    sections, current = {}, None
    for line in body.splitlines():
        if line.startswith("# ") and not name:
            name = line[2:].strip()
        elif line.startswith("> ") and name and not tagline and current is None:
            tagline = line[2:].strip()
        elif line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return {"name": name, "path": path.as_posix(), "tagline": tagline,
            "fields": fields,
            "sections": {k: "\n".join(v).strip() for k, v in sections.items()}}


def singular(folder):
    """R7: a type folder is the plural of its type."""
    if folder.endswith("ies"):
        return folder[:-3] + "y"
    return folder[:-1] if folder.endswith("s") else folder


def walk():
    """Every entity under `model/`, grouped by type, with the singular types the folders name.

    A folder's `README.md` describes the layout rather than a thing in the model and is not an
    entity, the same rule the export walks by. A file directly in the container is its own
    type — `identity.md` is the identity — because a type with one entity is a file (R6).

    The middle branch is R6's other half: an entity that owns collections is a folder holding a
    file named for itself, so `profiles/robert-blust/robert-blust.md` sits in a folder named for
    the entity and not for the type. Its type is the folder above that one. Taking the parent
    blindly would make a type called `robert-blust` with one member and lose the profile.
    """
    types = {}
    for path in sorted((ROOT / "model").rglob("*.md")):
        if path.name == "README.md":
            continue
        rel = path.relative_to(ROOT / "model")
        if len(rel.parts) == 1:
            kind = rel.stem
        elif rel.stem == rel.parts[-2]:
            kind = singular(rel.parts[-3])
        else:
            kind = singular(rel.parts[-2])
        types.setdefault(kind, []).append(read(path))
    return types


def main():
    types = walk()
    identity = types.pop("identity", [{}])[0]
    data = {
        "instance": pathlib.Path.cwd().name,
        "identity": identity,
        "surfaces": [{"name": s["name"], "path": s["path"]} for s in types.get("surface", [])],
        "types": types,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = ", ".join(f"{len(v)} {k}" for k, v in sorted(types.items()))
    print(f"  wrote {OUT}: {counts}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**

```bash
python3 .claude/skills/companygraph-surface/facts.py
```

Expected: a line naming the counts, and among them `36 experience`, `70 skill`, `5 value`, `4 proficiency-level`, `5 experience-kind`, `1 source`, `1 surface`, `1 vision`, `1 profile`.

- [ ] **Step 3: Assert the walk against the model**

```bash
python3 - <<'PY'
import json, pathlib, subprocess
d = json.loads(pathlib.Path("dist/surfaces/facts.json").read_text())
on_disk = len([p for p in pathlib.Path("model").rglob("*.md") if p.name != "README.md"])
in_facts = sum(len(v) for v in d["types"].values()) + 1  # + the identity, popped out
assert on_disk == in_facts, f"{on_disk} files on disk, {in_facts} in facts"
e = [x for x in d["types"]["experience"] if x["name"] == "Co-Founder & Head of Technology"][0]
assert e["fields"]["kind"] == "Role" and e["fields"]["start"] == "2022-04"
assert e["sections"]["Achievements"].startswith("- Owned technology direction")
assert d["identity"]["name"] == "Robert Blust"
assert d["surfaces"][0]["name"] == "LinkedIn profile"
s = [x for x in d["types"]["skill"] if x["name"] == "Java"][0]
assert s["path"] == "model/skills/java.md"
print("walk ok:", in_facts, "entities")
PY
```

Expected: `walk ok: 125 entities`. A failure here names what disagreed.

- [ ] **Step 4: Confirm nothing is committed**

```bash
git status --short
```

Expected: only `.claude/skills/companygraph-surface/facts.py` as untracked. `dist/` must not appear; it is ignored through the existing `dist/` line in `.gitignore`.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/companygraph-surface/facts.py
git commit -m "$(cat <<'MSG'
The facts a surface is produced from

A surface's file says which of the model's facts reach it and in what shape, and nothing read
the model for it, so producing one meant a person parsing Markdown by eye before reaching the
first rule. This walks the model once and hands over what it found: every entity by type, with
its frontmatter, its H1, its tagline and its sections.

It decides nothing. Which kinds reach which unit and in what order are the surface's rules and
its file is their only home, so a script that knew them would be the second copy and the one
nobody reads. What it may resolve, the next commit adds, and the test is written at the top of
the file: could two surfaces of the same model reasonably want it different.

Verified: the walk's count equals the entity files on disk, 125; a role, a skill, the identity
and the surface were each asserted field by field.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
MSG
)"
```

---

### Task 2: The two resolutions

**Files:**
- Modify: `.claude/skills/companygraph-surface/facts.py`
- Test: run it and assert both resolutions

**Interfaces:**
- Consumes: the entity records from Task 1.
- Produces: on every entity that carries a `start`, a `dates` string in the family's register; on every entity, `organization` and `organization_from`.

- [ ] **Step 1: Write the date formatter**

Add above `main()`:

```python
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def when(value):
    """One date in the family's register: `2012`, `Oct 2012`, `May 4, 2012`.

    The register is `conventions/WRITING.md`'s and not any surface's, which is why it is
    resolved here — and it is the rule a produced profile got wrong across twenty-eight ranges
    before the register was named in the surface's own file.
    """
    parts = value.split("-")
    if len(parts) == 1:
        return parts[0]
    month = MONTHS[int(parts[1]) - 1]
    if len(parts) == 2:
        return f"{month} {parts[0]}"
    return f"{month} {int(parts[2])}, {parts[0]}"


def span(fields):
    """A period as the register writes one: a closed en-dash, and nothing where there is no end.

    An entity with a `start` and no `end` is a period still running, and what a surface shows
    for that — a word, a dash, nothing — is the surface's business, so this leaves the right
    side empty rather than choosing one.
    """
    start = fields.get("start")
    if not start:
        return None
    end = fields.get("end")
    if not end:
        return when(start) + "–"
    return when(start) if end == start else f"{when(start)}–{when(end)}"
```

- [ ] **Step 2: Write the organization resolution**

Add below `span()`:

```python
def where(fields, identity):
    """Who an entity was done for, and where that answer came from.

    An experience nobody commissioned or hosted carries no `organization`, and the model still
    answers: this instance describes a company, so the work was that company's own. Both halves
    are returned because a surface may want them apart — one that shows a person's name where a
    company goes is making a choice, and this only supplies what the model holds.
    """
    named = fields.get("organization")
    if named:
        return named, "field"
    return identity.get("name", ""), "identity"
```

- [ ] **Step 3: Apply both in `main()`**

Replace `types = walk()` in `main()` with:

```python
    types = walk()
    identity = types.get("identity", [{}])[0]
    for entities in types.values():
        for e in entities:
            e["dates"] = span(e["fields"])
            e["organization"], e["organization_from"] = where(e["fields"], identity)
```

and leave the `identity = types.pop(...)` line that follows it as it is.

- [ ] **Step 4: Run and assert both resolutions**

```bash
python3 .claude/skills/companygraph-surface/facts.py && python3 - <<'PY'
import json, pathlib
d = json.loads(pathlib.Path("dist/surfaces/facts.json").read_text())
by = {x["name"]: x for x in d["types"]["experience"]}
assert by["Co-Founder & Head of Technology"]["dates"] == "Apr 2022–May 2026"
assert by["CamundaCon 2022"]["dates"] == "Oct 6, 2022"
assert by["CompanyGraph"]["dates"] == "Aug 2026–"
assert by["Business Information Systems UAS"]["dates"] == "2002–2006"
assert by["CompanyGraph"]["organization_from"] == "identity"
assert by["CompanyGraph"]["organization"] == "Robert Blust"
assert by["Co-Founder & CTO"]["organization_from"] == "field"
n = sum(1 for x in d["types"]["experience"] if x["organization_from"] == "identity")
assert n == 7, f"{n} experiences fall back, expected 7"
print("resolutions ok")
PY
```

Expected: `resolutions ok`. The seven are the career break, the three products, Flatland CDO Server,
the podcast episode and the application tooling — counted from the model rather than assumed, because
an earlier count of six was made by reading one unit's entries and missing the two outside it.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/companygraph-surface/facts.py
git commit -m "$(cat <<'MSG'
Dates in the family's register, and who the work was for

Two things every surface of this model wants the same way, so both are resolved here rather
than in each surface's rules. A date is written the way the conventions write one — a closed
en-dash, months in three letters — which is the rule a produced profile got wrong across
twenty-eight ranges before the register was named. And an experience nobody commissioned or
hosted still has an answer for who it was for: the instance describes a company, so the work
was that company's own.

Both are handed over with their provenance rather than flattened. A period still running leaves
its right side empty because what a surface shows there is the surface's business, and the
organization says whether it came from the field or from the identity, because a surface that
prints a person's name where a company goes is making a choice this script does not make for it.

Verified: four date shapes asserted against the model — a month range, a single day, a running
period and a year range — and the six experiences that fall back to the identity counted.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
MSG
)"
```

---

### Task 3: The procedure

**Files:**
- Create: `.claude/skills/companygraph-surface/SKILL.md`
- Test: `sh conventions/conventions-check`

**Interfaces:**
- Consumes: `dist/surfaces/facts.json` from Tasks 1 and 2.
- Produces: the procedure Task 4 follows.

- [ ] **Step 1: Read the two skills whose register this matches**

```bash
head -30 .claude/skills/companygraph-export/SKILL.md
head -20 .claude/skills/companygraph-validate/SKILL.md
```

Match their shape: YAML frontmatter with `name`, `description` and `allowed-tools`, then an H1, then a short paragraph saying what the skill is for, then `## Procedure` as a numbered list, then the sections that say why.

- [ ] **Step 2: Write it**

Create `.claude/skills/companygraph-surface/SKILL.md`:

```markdown
---
name: companygraph-surface
description: Produce the content of a surface into dist/surfaces/ — a script for the facts and a procedure for the prose, because half of a surface is a paragraph no script writes.
allowed-tools: Bash(*), Read, Write, Edit, Glob, Grep
---

# companygraph-surface

A surface is a place the company publishes that no script writes, and its file records the rules
by which the model becomes that place. This produces the place: one file per surface entity into
`dist/surfaces/`, ready to paste.

## Procedure

1. Run `python3 .claude/skills/companygraph-surface/facts.py` from the instance root.
2. Read the surface entity whole — every unit its `## What it shows` names, every projection
   rule and every constraint. It is the brief and nothing here repeats it.
3. Read `conventions/WRITING.md` for the register the surface's file names.
4. Produce each unit in the order `## What it shows` lists them, applying the projection rules
   to the facts. Write to `dist/surfaces/<surface>.md`, one section per unit, labeled with the
   unit's own name so a reader can match it against the editor in front of them.
5. Hold the result against every constraint the file states, one at a time, and report each as
   passed or failed with its evidence measured rather than estimated.
6. Report every place the file did not determine an answer, and say what you did instead.

## What the script decides, and what it must not

The script resolves what any surface of this model would want the same way: an entity's dates in
the family's register, its `organization` with the identity where the model names none, its
address, and the sections a body could be written from. It routes nothing and orders nothing.

Which kinds reach which unit, in what order entries run, what is left out and why, and what
register the prose takes are the surface's rules, and its file is their only home. A rule that
moved into the script would be the second copy of itself, and the second copy is the one nobody
reads. Before resolving anything new there, ask whether two surfaces of the same model could
reasonably want it different: if they could, it belongs to the file.

## Why this one is a procedure and not a program

`companygraph-export` is a single script and says why: one intent implemented twice drifts apart
one rule at a time, and a procedure followed by hand is a different program each time somebody
follows it. Both hold here, and neither makes this scriptable. No script writes a paragraph in a
register, chooses which skills a profile claims, or cuts a body to the length its period earns.

So the line is not drawn by taste. Everything a machine can settle is the script's, and the
procedure begins at the first thing it cannot.

## The output is never committed

`dist/` is gitignored, so nothing this produces enters the repository. The reason is R17 rather
than the build directory: a file in the model records the rules by which something is made and
never the state of the thing made, and a produced surface is that state. It is produced, read,
pasted and thrown away, and the next production makes it again from the rules.

## Producing a surface is how a surface file gets checked

Reading the reference instance's surface file against its model found nothing across two review
rounds. Producing the profile from it found a missing rule every time, six times running — the
register named nowhere, no order on the entries, no company for an experience without an
`organization`, no length for a body — and every one was a rule about what to put in rather than
what to leave out. A file is written by somebody deciding what to omit and reads that way until
something tries to use it.

So step 6 is not a courtesy. It is the only report that finds what a surface file lacks, and it
belongs in the pull request that changes the file.
```

- [ ] **Step 3: Run the prose checks**

```bash
sh conventions/conventions-check && sh conventions/conventions-sync check
```

Expected: both print a `✓` line and exit 0.

- [ ] **Step 4: Confirm the skill loads**

```bash
ls .claude/skills/ && head -5 .claude/skills/companygraph-surface/SKILL.md
```

Expected: four skills listed, and the frontmatter's `name` matching the folder.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/companygraph-surface/SKILL.md
git commit -m "$(cat <<'MSG'
The procedure that turns the facts into the surface

The script hands over what the model holds and stops at the first thing a machine cannot settle.
This is what happens after that: read the surface's file whole, produce each unit its rules
describe, and hold the result against every constraint the file states.

Step six is the one worth defending. Reading a surface file against the model finds nothing —
it did, twice — and producing the surface from it found a missing rule six times running, every
one about what to put in rather than what to leave out. So the report of what the file failed to
determine is not a courtesy at the end of a run; it is the only check a surface file gets, and
it belongs in the pull request that changes the file.

Verified: conventions-check and conventions-sync check pass; the skill's frontmatter name
matches its folder.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
MSG
)"
```

---

### Task 4: Produce the LinkedIn profile through the skill

The acceptance. Until a surface comes out of it, the skill is a claim.

**Files:**
- Writes: `dist/surfaces/linkedin-profile.md`, which is gitignored and committed by nothing
- Test: the surface's own five constraints

**Interfaces:**
- Consumes: everything the three previous tasks built.

- [ ] **Step 1: Follow the procedure**

Run the skill's own procedure end to end against `model/surfaces/linkedin-profile.md`. Do not
shortcut it by reading this plan for the answers: the point of the step is whether the procedure
as written is followable.

- [ ] **Step 2: Check the output exists and is not tracked**

```bash
ls -la dist/surfaces/ && git status --short && git check-ignore -v dist/surfaces/linkedin-profile.md
```

Expected: `facts.json` and `linkedin-profile.md` present, `git status` showing neither, and
`check-ignore` naming the `dist/` line that ignores them.

- [ ] **Step 3: Check the five constraints, measured**

```bash
python3 - <<'PY'
import pathlib, re
t = pathlib.Path("dist/surfaces/linkedin-profile.md").read_text()
head = re.search(r"(?ms)^## Headline\s*\n+(.+?)(?=\n#|\Z)", t).group(1).strip()
about = re.search(r"(?ms)^## About\s*\n+(.+?)(?=\n## )", t).group(1).strip()
print("headline", len(head), "of 220")
print("about", len(about), "of 2600")
assert len(head) <= 220 and len(about) <= 2600
PY
```

Expected: both counts printed and under their limits. The other three constraints are read by
the agent and reported in step 4, because a name pairing, a date agreeing with the model and a
skill name matching an H1 are readings rather than measurements.

- [ ] **Step 4: Report**

Write the report the procedure's step 6 asks for: every constraint passed or failed with its
evidence, and every place the surface's file did not determine an answer. This is the output the
owner reads, and it is what says whether the file or the skill needs the next change.

- [ ] **Step 5: Commit nothing, and say so**

There is nothing to commit. The produced surface is gitignored by design, and the three previous
tasks carry the skill. Confirm with `git status --short` and report the run instead.

---

## Out of scope

- **A verify script.** The export has one because its output is derivable and comparable; a produced surface is prose and two correct productions differ. The constraint check in the procedure stands in its place.
- **A second surface.** The instance holds one. The script is written against the model rather than against LinkedIn, and that claim is untested until a second exists.
- **A routing declaration in the schema.** It would let the script route and order, and it would put every rule in a table and in the prose explaining the table.
- **The tooling repository.** `companygraph/tooling` is designed and not built; this skill lives in the instance until it exists, exactly as the other three do. Its place in the tooling spec is companygraph/meta-model#67.
