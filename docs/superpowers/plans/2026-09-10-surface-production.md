# Surface production Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A fifth skill, `companygraph-surface`, that produces the content of a surface into `dist/surfaces/` — a script for the facts and a procedure for the prose.

**Architecture:** `facts.py` walks `model/` once and writes `dist/surfaces/facts.json`, resolving only what any surface would want the same way: an entity's dates in the family's register, and — for a type whose entities name one somewhere in the model — its `organization` with the identity as the default. Everything else reaches the file as the entity's frontmatter and sections hold it, a `url` among them, carried and not resolved. It routes nothing and orders nothing. `SKILL.md` carries the procedure that applies a surface's own rules to those facts, writes each unit and checks the result against the surface's constraints.

**Tech Stack:** Python 3 standard library only, matching `companygraph-export`. No test framework in this repository: a script is checked by running it and asserting its output, which is what `verify.py` does for the export.

**Spec:** `docs/specs/2026-09-10-surface-production.md`

## Global Constraints

- Python 3 standard library only. No dependency, no network. `companygraph-export/build.py` is the style to match, including its habit of explaining a decision in the docstring where a reader will meet it.
- **The script routes nothing and orders nothing.** Which kinds reach which unit and in what order are the surface's rules and its file is their only home. The test before adding any resolution: could two surfaces of the same model reasonably want it different? If yes it belongs to the file.
- Output goes to `dist/surfaces/`, which is gitignored through `dist/`. Nothing this skill produces is ever committed, and the reason is R17 rather than the build directory.
- Prose in `SKILL.md` follows `conventions/WRITING.md`: American English, spaced em-dashes, sentence case in headings, no serial comma. `sh conventions/conventions-check` enforces the spelling and dash rules.
- Dates follow the family's register: `Oct 2012` for a month, `May 4, 2012` for a day, `2012` for a year and a range closed with an en-dash and no spaces, `May 2012–Oct 2016`.
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
assert e["sections"]["Achievements"].startswith("- Co-founder and Head of Technology of LIKE MAGIC AG.")
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
- Produces: on every entity that carries a `start`, a `dates` string in the family's register; on every entity of a type that names an organization anywhere, `organization` and `organization_from`.

- [ ] **Step 1: Write the date formatter**

Add above `main()`:

```python
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def when(value):
    """One date in the family's register: `2012`, `Oct 2012`, `May 4, 2012`.

    The register is `conventions/WRITING.md`'s and not any surface's, which is why it is
    resolved here rather than left to the surface's own file.
    """
    parts = value.split("-")
    if len(parts) == 1:
        return parts[0]
    month = MONTHS[int(parts[1]) - 1]
    if len(parts) == 2:
        return f"{month} {parts[0]}"
    return f"{month} {int(parts[2])}, {parts[0]}"


def span(fields):
    """A period as the register writes one: a closed en-dash, or the start alone when the
    period has no end.

    `fields` already carries whether the period is still running — `end` is present or it is
    not, and that absence is the fact a surface can read for itself. What a surface makes of an
    open period — a dash, the word "Present", nothing at all — is exactly the kind of choice two
    surfaces might reasonably make differently, so this hands back the formatted start alone and
    leaves that choice to the surface's file.
    """
    start = fields.get("start")
    if not start:
        return None
    end = fields.get("end")
    if not end:
        return when(start)
    return when(start) if end == start else f"{when(start)}–{when(end)}"
```

- [ ] **Step 2: Write the organization resolution and the gate on it**

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


def has_organization(entities):
    """Whether `organization` means anything for a type, decided from the type's own data.

    Only some entities carry `organization` in their frontmatter, and the fallback belongs
    beside them and nowhere else: handing every skill, value and vision an `organization` of
    "Robert Blust" is not a fact about a skill, it is noise a surface's file would have to learn
    to ignore. The line is drawn from what the type's own entities carry rather than from the
    type's name, so the script stays free of any knowledge of what an experience is — a type
    added to the model that starts naming organizations picks up the fallback the same way,
    with nothing here changed for it.
    """
    return any(e["fields"].get("organization") for e in entities)
```

- [ ] **Step 3: Apply both in `main()`**

Replace `types = walk()` in `main()` with:

```python
    types = walk()
    identity = types.get("identity", [{}])[0]
    for entities in types.values():
        for e in entities:
            e["dates"] = span(e["fields"])
        if has_organization(entities):
            for e in entities:
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
assert by["CompanyGraph"]["dates"] == "Aug 2026"
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
than in each surface's rules. A date is written the way the conventions write one, a closed
en-dash and months in three letters, because that rule belongs to the conventions and not to
any surface. And an experience nobody commissioned or hosted still has an answer for who it
was for: the instance describes a company, so the work was that company's own.

Neither is flattened. A period still running gets its start and no marker beside it, because
what a surface shows there — a dash, a word, nothing — is what two surfaces would reasonably
want differently, and the absence of `end` in the fields is the fact a surface reads for
itself. The organization says whether it came from the field or from the identity, and it is
resolved only for a type whose entities name one somewhere, so a skill carries no such field
rather than carrying the identity's name as noise.

Verified: four date shapes asserted against the model — a month range, a single day, a running
period and a year range — the seven experiences that fall back to the identity counted, and no
type but experience carrying the field at all.

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
by which the model becomes that place. This produces the place: one run produces one surface
entity into `dist/surfaces/`, named for that entity's own file and ready to paste.

## Procedure

1. Run `python3 .claude/skills/companygraph-surface/facts.py` from the instance root.
2. Name the surface this run produces, then read that entity whole — every unit its
   `## What it shows` names, every projection rule and every constraint. It is the brief and
   nothing here repeats it. `facts.json`'s `surfaces` lists every surface the model holds with
   its `name` and its `path`: produce the one the request names, and where the request names
   none and the list holds one, that one. A run produces a single surface, so a request naming
   none against a model holding several is a question for the owner rather than a choice to
   make.
3. Read `conventions/WRITING.md` for the register the surface's file names.
4. Produce each unit in the order `## What it shows` lists them, applying the projection rules
   to the facts. Write to `dist/surfaces/<stem>.md`, where `<stem>` is the file name of the
   entity's own `path` in the model without its extension — `model/surfaces/linkedin-profile.md`
   produces `dist/surfaces/linkedin-profile.md` — one section per unit, labeled with the
   unit's own name so a reader can match it against the editor in front of them. A rule is a
   stop and not a guess wherever it names something this run cannot settle: a source outside
   the model — a page this repository does not hold, a network's own editor — or a decision the
   surface's file leaves to the owner at each rebuild — which five skills the Skills unit
   shows, say. A stopped unit's section holds one line and nothing else, `STOP: <what the rule
   asks for> — <the source it would be read from, or whose decision it waits on>`, so nothing
   downstream can mistake it for content. `STOP: five skill names — the owner chooses them at
   each rebuild` is the form as much as a page outside the model is.
5. Hold the result against every constraint the file states, one at a time, and report each as
   passed or failed with its evidence measured rather than estimated. A constraint that governs
   a stopped unit is reported rather than tested, and it is never passed: a character count
   taken against a `STOP:` line is a real number measuring nothing, and a check that cannot
   tell the difference is not evidence. A produced surface missing a unit has to fail loudly
   rather than clear a gate.
6. Report every place the file did not determine an answer, and say what you did instead.

## What facts.json holds

`facts.json` carries `identity`, the identity entity whole; `surfaces`, each surface's `name`
and `path`; and `types`, one list per type — `experience`, `skill`, `value` and so on — each
entry an entity in the same shape: `name`, `path`, `tagline`, `fields` (its frontmatter as
written) and `sections` (its `##` bodies, keyed by heading). Where its type names an
organization anywhere, an entity also carries `organization` with `organization_from`.

Every entity carries `dates`, and on most of them it is null: only a `start` in the frontmatter
makes a period, so the key is always there and its value often is not. Where there is one,
`dates` is the period written for a reader, a bare date where the period is one unit long or
still running, and `fields.end` is the fact that tells those two apart: a period that ended in
the month it began and a period with no end read the same as prose, and only the frontmatter
says which is which. A rule that turns on whether a period is running reads `fields`, never
`dates`.

A type is not a kind. `types["experience"]` is one list holding every experience regardless of
what kind it is; `kind` is a field inside that entity's own `fields`, the value a rule in the
surface's file routes by. A rule naming a kind asks the procedure to filter one of these lists
on a field inside it, not to look for a list of its own.

## What the script decides, and what it must not

The script resolves two things: an entity's dates into the family's register, and — for a type
whose entities name one somewhere in the model — its `organization`, falling back to the
identity for an entity that names none itself. A type no entity of it ever names an
organization for carries no such field at all. Everything else reaches `facts.json` exactly as
the entity's frontmatter and sections hold it: a `url` is carried, not resolved, the same as
any other field. The script routes nothing and orders nothing.

Which kinds reach which unit; in what order entries run; what is left out and why; and what
register the prose takes: these are the surface's rules, and its file is their only home. A
rule that moved into the script would be the second copy of itself, and the second copy is the
one nobody reads. Before resolving anything new there, ask whether two surfaces of the same
model could reasonably want it different: if they could, it belongs to the file.

## Why this one is a procedure and not a program

`companygraph-export` is a single script and says why: one intent implemented twice drifts apart
one rule at a time, and a procedure followed by hand is a different program each time somebody
follows it. Both hold here, and neither makes this scriptable. No script writes a paragraph in a
register, chooses which skills a profile claims or cuts a body to the length its period earns.

So the line is not drawn by taste. Everything a machine can settle is the script's, and the
procedure begins at the first thing it cannot.

## The output is never committed

`dist/` is gitignored, so nothing this produces enters the repository. The reason is R17 rather
than the build directory: a file in the model records the rules by which something is made and
never the state of the thing made, and a produced surface is that state. It is produced, read,
pasted and thrown away, and the next production makes it again from the rules.

## Producing a surface is how a surface file gets checked

A file is written by somebody deciding what to omit, and it reads as complete until something
tries to use it. Producing a surface is that use: it is the check that finds what a surface's
file fails to state, in a way reading the file against the model does not.
`docs/specs/2026-09-10-surface-production.md` holds the evidence for that claim.

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

Expected: five skills listed, and the frontmatter's `name` matching the folder.

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

Expected: `facts.json` and `linkedin-profile.md` present, `git status` showing neither and
`check-ignore` naming the `dist/` line that ignores them.

- [ ] **Step 3: Check the two character limits, and fail on a unit that is not there**

```bash
python3 - <<'PY'
import pathlib, re, sys
LIMITS = {"Headline": 220, "About": 2600}
spec = pathlib.Path("model/surfaces/linkedin-profile.md").read_text()
shows = re.search(r"(?ms)^## What it shows[ \t]*$\n(.*?)(?=^## |\Z)", spec).group(1)
declared = re.findall(r"(?m)^- \*\*(.+?)\*\*", shows)
text = pathlib.Path("dist/surfaces/linkedin-profile.md").read_text()
produced = {m.group(1).strip(): m.group(2).strip()
            for m in re.finditer(r"(?ms)^## (.+?)[ \t]*$\n(.*?)(?=^## |\Z)", text)}
missing, stopped = [], []
for name in declared:
    body = produced.get(name)
    lines = [l for l in (body or "").splitlines() if l.strip()]
    if body is None:
        missing.append(name)
        print(f"{name}: missing — no section carries it")
    elif not lines:
        missing.append(name)
        print(f"{name}: missing — its section is empty")
    elif len(lines) == 1 and lines[0].startswith("STOP:"):
        stopped.append(name)
        print(f"{name}: not tested — {lines[0]}")
    elif name in LIMITS:
        print(f"{name}: {len(body)} of {LIMITS[name]}")
        assert len(body) <= LIMITS[name], f"{name} is {len(body)}, over {LIMITS[name]}"
print(f"{len(declared)} units declared, {len(missing)} missing, {len(stopped)} stopped")
sys.exit(1 if missing or stopped else 0)
PY
```

The unit names come from the surface entity's `## What it shows`, which is where they are
declared, so the check asks what should be there rather than counting what it finds. Expected on
a surface produced whole: a count for the headline and a count for the About text, both under
their limits, `8 units declared, 0 missing, 0 stopped`, and exit 0. Anything else exits 1. A
stopped unit prints `not tested` with its own `STOP:` line, because a character count taken
against a `STOP:` line is a real number measuring nothing; a unit the produced file has no
section for, or has an empty section for, prints `missing`, because the two are different
failures and the report in step 4 has to say which. The other three constraints are read by the
agent and reported in step 4, because a name pairing, a date agreeing with the model and a skill
name matching an H1 are readings rather than measurements.

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
