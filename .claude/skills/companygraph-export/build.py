#!/usr/bin/env python3
"""Render a CompanyGraph instance into a NotebookLM bundle: dist/<instance>-notebooklm/.

The bundle is a flat folder of Markdown sources, one file per heading in the instance's
`export/notebooklm-sources.md`, because NotebookLM takes files and not an archive.

This is a script rather than a procedure an agent follows by hand: the failure the second
artifact exists to catch is a bundle that went quietly stale, and a rendering nobody can
re-run cheaply is a rendering that will be stale again. Run it from the instance root, or
pass the root as the first argument.

Stdlib only. No third-party module is installed where this runs.
"""

import glob
import os
import pathlib
import re
import shutil
import sys

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# These four lead the dateline, in this order, because they are what a listener places an
# experience by. Every other field that carries a fact about the subject follows them labeled,
# so the two artifacts cover the same entities and the same claims about them.
DATELINE_FIELDS = ("kind", "organization", "start", "end")

# These never travel. They address a validator, not a listener: `source` and `source-id` say
# which system masters the page and `rank` orders the proficiency ladder, and a host reading
# `Source: Local` aloud on all 133 entities is reading bookkeeping. Coverage is of entities,
# which the entity marker carries, and not of frontmatter keys.
VALIDATOR_FIELDS = ("source", "source-id", "rank")


def entities():
    """Every file the export walks, in path order.

    A folder's README.md describes the repository's layout rather than a thing in the model,
    so it is not an entity here and never carries an entity marker: claiming one would make
    the bundle disagree with the model by every README a pattern happened to match. Under
    `meta/` as much as under `model/` — the vendored core has no README today, and a rule that
    holds by accident is one a core release can break without anything saying so.
    """
    found = [p for p in pathlib.Path("model").rglob("*.md") if p.name != "README.md"]
    found += [p for p in pathlib.Path("meta").rglob("*.md") if p.name != "README.md"]
    return sorted(found, key=lambda p: p.as_posix())


def declaration(path):
    """Read the instance's source declaration: title, opening paragraph and path globs."""
    sources, current = [], None
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = {"title": line[3:].strip(), "prose": [], "globs": []}
            sources.append(current)
        elif current is None:
            continue
        elif line.lstrip().startswith("- "):
            found = re.search(r"`([^`]+)`", line)
            if found:
                current["globs"].append(found.group(1))
        else:
            current["prose"].append(line)
    for source in sources:
        source["prose"] = paragraphs(source["prose"])
    return sources


def paragraphs(lines):
    """Join wrapped lines back into paragraphs, so the prose travels as the writer meant it."""
    out, buffer = [], []
    for line in lines + [""]:
        if line.strip():
            buffer.append(line.strip())
        elif buffer:
            out.append(" ".join(buffer))
            buffer = []
    return "\n\n".join(out)


def root_type(path):
    """The type a path answers to at the root: `profiles`, `skills`, `meta`, `identity`.

    A singular entity is its own type, because `model/identity.md` is its own file in the
    agent bundle too and folding it under a source called `Model` names nothing a reader is
    looking for.
    """
    parts = path.parts
    if parts[0] != "model":
        return parts[0]
    return parts[1] if len(parts) > 2 else path.stem


def title_of(name):
    """A folder name as a title, first letter raised and the rest left alone.

    Left alone because a title is what a citation carries: lowering it would turn a name the
    folder spells in capitals into one no reader recognizes.
    """
    text = name.replace("-", " ").replace("_", " ")
    return text[:1].upper() + text[1:]


def assign(walked, sources):
    """Give every entity to the first heading that claims it, and the rest to a fallback.

    Where a declaration groups the model, a straggler goes to a source named for its own type
    folder — `experiences`, not `profiles` — because `model/profiles/` is the one folder the
    walk recurses into, so the root type there is not the entity's type.

    Where there is no declaration at all, which is the path an instance takes before it writes
    one, the whole model is cut by root type instead: one source per type folder under
    `model/`, one for `meta/` and one for each singular entity. That is the cut the agent
    bundle already makes, so the two artifacts are grouped alike until the instance says
    otherwise.
    """
    left = list(walked)
    for source in sources:
        source["entities"] = []
        for pattern in source["globs"]:
            matched = {pathlib.Path(m) for m in glob.glob(pattern, recursive=True)}
            taken = [p for p in left if p in matched]
            source["entities"] += taken
            left = [p for p in left if p not in matched]
        source["entities"].sort(key=lambda p: p.as_posix())
    if not left:
        return sources

    declared = bool(sources)
    groups = {}
    for path in left:
        groups.setdefault(path.parent.name if declared else root_type(path), []).append(path)

    for name in sorted(groups):
        if declared:
            prose = (f"The `{name}` entities that no heading in "
                     f"`export/notebooklm-sources.md` claims, gathered here so the bundle "
                     f"carries the model whole.")
        else:
            prose = (f"Every `{name}` entity in the model. This instance declares no grouping "
                     f"in `export/notebooklm-sources.md`, so each root type is one source.")
        sources.append({
            "title": title_of(name),
            "prose": prose,
            "globs": [],
            "entities": sorted(groups[name], key=lambda p: p.as_posix()),
        })
    return sources


def frontmatter(text):
    """Split leading YAML from the rest, keeping the order the file wrote its fields in.

    A block sequence comes back as a list of its entries. Nothing else is expected here: R11
    says a list-valued field is written one entry per line, so there is no flow sequence to
    parse and no nesting under a key.
    """
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fields, key = {}, None
    for line in text[4:end].splitlines():
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and isinstance(fields.get(key), list):
            fields[key].append(item.group(1).strip().strip("\"'"))
            continue
        found = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if found:
            key = found.group(1)
            value = found.group(2).strip().strip("\"'")
            fields[key] = value if value else []
    rest = text[end + len("\n---"):]
    return fields, rest.split("\n", 1)[1] if "\n" in rest else ""


def readable(value):
    """A date a host can read aloud: 1999-10 becomes Oct 1999, 2012-05-04 May 4, 2012."""
    parts = str(value).split("-")
    if len(parts) == 1:
        return parts[0]
    month = MONTHS[int(parts[1]) - 1]
    if len(parts) == 2:
        return f"{month} {parts[0]}"
    return f"{month} {int(parts[2])}, {parts[0]}"


def label(key):
    """A frontmatter key as a reader meets it, sentence case, with the one initialism kept."""
    return "URL" if key == "url" else key.replace("-", " ").replace("_", " ").capitalize()


def dateline(fields):
    """`<Kind> · <organization> · <start> – <end>`, then every field a listener could use.

    A field the entity does not carry is dropped, and a start equal to its end is written
    once. What follows the four is labeled because `AI` says nothing standing on its own where
    `Group: AI` does. What is in VALIDATOR_FIELDS is dropped whatever the entity carries.
    """
    bits = [fields[key] for key in ("kind", "organization") if fields.get(key)]
    start, end = fields.get("start"), fields.get("end")
    if start and end and start != end:
        bits.append(f"{readable(start)}\u2013{readable(end)}")
    elif start or end:
        bits.append(readable(start or end))
    for key, value in fields.items():
        if key in DATELINE_FIELDS or key in VALIDATOR_FIELDS or not value:
            continue
        bits.append(f"{label(key)}: {', '.join(value) if isinstance(value, list) else value}")
    return " · ".join(bits)


def shift(lines):
    """Every heading one level down, so an entity's sections sit under its name, not beside it.

    A `#` inside a fenced code block is code and is left as it is, and an H6 stays where it is
    because there is no seventh level to move it to.
    """
    out, fenced = [], False
    for line in lines:
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
        elif not fenced:
            found = re.match(r"^(#{1,5}) (.*)$", line)
            if found:
                line = f"#{found.group(1)} {found.group(2)}"
        out.append(line)
    return out


def render(path):
    """One entity, ready to be inlined: marker, H2, tagline, dateline, body."""
    fields, body = frontmatter(path.read_text(encoding="utf-8"))
    lines = body.splitlines()

    name, cut = path.stem, 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            name, cut = line[2:].strip(), i + 1
            break
    lines = lines[cut:]

    while lines and not lines[0].strip():
        lines.pop(0)
    tagline = []
    while lines and lines[0].startswith(">"):
        tagline.append(lines.pop(0))

    out = [f"<!-- entity: {path.as_posix()} -->", "", f"## {name}"]
    if tagline:
        out += [""] + tagline
    line = dateline(fields)
    if line:
        out += ["", line]
    rest = "\n".join(shift(lines)).strip("\n")
    if rest:
        out += ["", rest]
    return "\n".join(out) + "\n"


def main():
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    root = pathlib.Path.cwd()
    out = root / "dist" / f"{root.name}-notebooklm"

    walked = entities()
    if not walked:
        print(f"FAIL  no entity under {root}/model")
        return 1

    declared = pathlib.Path("export/notebooklm-sources.md")
    sources = [s for s in assign(walked, declaration(declared) if declared.is_file() else [])
               if s["entities"]]

    # Two sources cannot share a file name. One would overwrite the other, the entities in the
    # loser would leave the bundle, and the run would still exit 0 — which is the exact way a
    # bundle goes quietly short. Two profiles each holding an unclaimed `experiences/` folder
    # is how it happens, so this is checked before anything is written.
    names, clash = {}, False
    for source in sources:
        name = source["title"].replace("/", "-") + ".md"
        if name in names:
            print(f"FAIL  two sources want {name}: give one a heading of its own in "
                  f"export/notebooklm-sources.md")
            clash = True
        names[name] = source
        source["file"] = name
    if clash:
        return 1

    # Written from scratch every run: a renamed heading would otherwise leave its old file
    # behind, and a bundle claiming an entity twice is the failure the verifier reports.
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    for source in sources:
        parts = [f"# {source['title']}"]
        if source["prose"]:
            parts.append(source["prose"])
        parts += [render(p) for p in source["entities"]]
        (out / source["file"]).write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
        print(f"{len(source['entities']):4d} entities  {source['file']}")

    print(f"{len(walked):4d} entities  in {len(list(out.glob('*.md')))} sources under {out}")
    return 0


sys.exit(main())
