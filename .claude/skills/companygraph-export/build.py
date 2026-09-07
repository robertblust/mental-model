#!/usr/bin/env python3
"""Render a CompanyGraph instance into a NotebookLM bundle: dist/<instance>-notebooklm/.

The bundle is a flat folder of Markdown sources, because NotebookLM takes files and not an
archive. A source is one content area of the model, named for the area, and it carries the
model's own pages verbatim: an entity keeps the frontmatter, the H1 and the body it has on
disk, so nothing a reader could be answered from is rewritten on the way out.

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

# Two documents ship as sources of their own, beside the sources that carry entities: the
# reading guide the instance writes for this bundle, and the repository's own README. A
# reader who opens a notebook cold has no other way to learn that references between entities
# are by name, and a guide that lives outside the bundle is a guide that reader never sees.
# Neither is an entity and neither carries a marker; `export/notebooklm-verify` counts them as
# sources and looks for no coverage in them.
DOCUMENTS = (("AGENTS.md", "export/notebooklm-AGENTS.md"), ("README.md", "README.md"))

# A count a document states in prose is a count nothing checks: the guide would tell a reader
# 36 experiences while the bundle held 37, and the verifier would pass, because a document is
# not an entity and holds no marker. So a document writes `{{entities}}`, `{{sources}}` or
# `{{count:<source title>}}` / `{{count:<path under the root>}}` where a number goes, and the
# build substitutes what it counted on this run. A token that resolves to nothing is left
# standing and fails the build, because `{{count:Skils}}` shipped to a reader is worse than a
# build that stops.
TOKEN = re.compile(r"\{\{([a-z]+)(?::([^{}]+))?\}\}")


def entities():
    """Every file the export walks, shallowest first and then in path order.

    Shallowest first because a folder that owns another holds the entity the others belong to:
    `model/profiles/robert-blust/robert-blust.md` is the profile that owns everything under
    `experiences/`, and path order alone would open the source on the first experience and
    reach the profile 36 entities later.

    A folder's README.md describes the repository's layout rather than a thing in the model,
    so it is not an entity here and never carries an entity marker: claiming one would make
    the bundle disagree with the model by every README a pattern happened to match. Under
    `meta/` as much as under `model/` — the vendored core has no README today, and a rule that
    holds by accident is one a core release can break without anything saying so.
    """
    found = [p for p in pathlib.Path("model").rglob("*.md") if p.name != "README.md"]
    found += [p for p in pathlib.Path("meta").rglob("*.md") if p.name != "README.md"]
    return sorted(found, key=order)


def order(path):
    """The order entities are written in: depth, then path."""
    return (len(path.parts), path.as_posix())


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


def folder_of(paths, name=None):
    """The folder a source is named for, as a POSIX path.

    Its type folder where the source is one root type, because that is the folder whose README
    describes it and the path a reader would go to: `model/profiles/` and not
    `model/profiles/robert-blust/`, which is only where this instance's entities happen to
    share a parent. Otherwise the folder the entities do share.
    """
    if name:
        found = pathlib.Path("model") / name
        if found.is_dir():
            return found.as_posix()
    return os.path.commonpath([p.parent.as_posix() for p in paths])


def readme_of(paths, name=None):
    """The README that describes a source's folder, when there is one.

    It is context and never an entity: it says how the folder is laid out and what is written
    against which schema, which is what a reader needs before the first page and not a thing
    the model claims. So it carries no marker and is not counted.

    Only a folder under a root, never a root itself: `model/skills/README.md` describes the
    skills, where a README at `model/` would describe the whole model and say nothing about
    the one entity a source such as `Identity` holds.
    """
    folder = pathlib.Path(folder_of(paths, name))
    if len(folder.parts) < 2:
        return None
    found = folder / "README.md"
    return found if found.is_file() else None


def opening(name, paths):
    """One sentence: what the source holds and when a reader wants it.

    Written by the export rather than by the instance because this is the shape an instance
    gets before it has declared one, and a sentence the tool writes is a sentence that stays
    true as the model grows. An instance with a narrative to make writes its own, in
    `export/notebooklm-sources.md`.
    """
    topic = name.replace("-", " ").replace("_", " ")
    if len(paths) == 1:
        return (f"`{paths[0].as_posix()}`, reproduced whole — read this source when the "
                f"question is about {topic}.")
    return (f"The {len(paths)} entities under `{folder_of(paths, name)}/`, each reproduced "
            f"whole — read this source when the question is about {topic}.")


def assign(walked, sources):
    """Give every entity to the first heading that claims it, and the rest to a fallback.

    A source carries its entities in the order the declaration writes its globs, and inside one
    glob in the walk's own order, because the order a declaration writes is an argument. `How
    this model works` opens on the five kinds an experience can be and closes on the schema
    underneath them; path order alone would sort `meta/**` ahead of `model/**` and open it on
    the vendored schema instead, which is the reader meeting the appendix before the point.

    Where a declaration groups the model, a straggler goes to a source named for its own type
    folder — `experiences`, not `profiles` — because `model/profiles/` is the one folder the
    walk recurses into, so the root type there is not the entity's type.

    Where there is no declaration at all, which is the path an instance takes before it writes
    one and the path this instance stays on, the whole model is cut by root type instead: one
    source per type folder under `model/`, one for `meta/` and one for each singular entity.
    That is the cut the agent bundle already makes, so the two artifacts are grouped alike
    until the instance says otherwise — and it is the cut that survives a model growing,
    because it groups by what the instance has actually declared about every entity rather
    than by a pattern that happens to match some of them.

    A glob matching nothing on disk comes back as dead, with the source that wrote it, for the
    caller to fail on. A renamed folder would otherwise empty a whole source and drop it in
    silence, and the verifier would still pass: it holds the bundle against the model, and the
    model has no opinion about which heading an entity was meant to sit under.
    """
    left, dead = list(walked), []
    for source in sources:
        source["entities"] = []
        for pattern in source["globs"]:
            matched = {pathlib.Path(m) for m in glob.glob(pattern, recursive=True)}
            if not matched:
                dead.append((source["title"], pattern))
                continue
            source["entities"] += [p for p in left if p in matched]
            left = [p for p in left if p not in matched]
    if not left:
        return sources, dead

    declared = bool(sources)
    groups = {}
    for path in left:
        groups.setdefault(path.parent.name if declared else root_type(path), []).append(path)

    for name in sorted(groups):
        held = sorted(groups[name], key=order)
        if declared:
            prose = (f"The `{name}` entities that no heading in "
                     f"`export/notebooklm-sources.md` claims, gathered here so the bundle "
                     f"carries the model whole.")
        else:
            prose = opening(name, held)
        sources.append({
            "title": title_of(name),
            "prose": prose,
            "globs": [],
            "entities": held,
            "type": None if declared else name,
        })
    return sources, dead


def context(readme, title):
    """A folder README as it opens a source, less an H1 that only repeats the source's own.

    The source has already written `# Skills`, and `model/skills/README.md` opens by writing it
    again. A heading that differs is saying something and stays.
    """
    lines = readme.read_text(encoding="utf-8").strip("\n").splitlines()
    if lines and lines[0].strip() == f"# {title}":
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
    return "\n".join(lines).strip("\n")


def counted(text, sources, walked, written):
    """A document with every `{{...}}` token replaced by the count this run measured.

    A token nothing resolves is left as it is: `count_of` gives back 0 for a source title or a
    path that names nothing, and a zero is a typo rather than a fact worth printing.
    """
    def found(match):
        number = count_of(match.group(1), match.group(2), sources, walked, written)
        return str(number) if number else match.group(0)
    return TOKEN.sub(found, text)


def count_of(kind, arg, sources, walked, written):
    """What a token asks for: every entity, every source, or the entities one name holds."""
    if kind == "entities" and not arg:
        return len(walked)
    if kind == "sources" and not arg:
        return written
    if kind == "count" and arg:
        if "/" in arg:
            head = arg.rstrip("/") + "/"
            return len([p for p in walked if p.as_posix().startswith(head)])
        return sum(len(s["entities"]) for s in sources if s["title"] == arg)
    return 0


def render(path):
    """One entity, ready to be inlined: its marker, then the page exactly as it is on disk.

    Verbatim because every rewriting loses something a reader could have been answered from,
    and the frontmatter loses the most: a role naming 45 skills carries them as a YAML list one
    entry per line, which is a list a reader can follow to the skills that hold each claim, and
    prose made from it is a thousand characters nobody reads to the end of. The reader here
    handles Markdown; it does not need the model translated for it.

    The marker stays. NotebookLM strips comments, so it costs the reader nothing, and it is an
    unambiguous boundary where a bare `---` is not: the source holding 69 skills holds 138 lines
    reading `---`, two per entity, and an entity whose body carries a horizontal rule adds one
    that nothing tells apart from a fence. It is also what `export/notebooklm-verify` reads
    coverage from.
    """
    return f"<!-- entity: {path.as_posix()} -->\n\n" + path.read_text(encoding="utf-8").strip("\n")


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
    sources, dead = assign(walked, declaration(declared) if declared.is_file() else [])

    # A pattern that matches nothing is a source about to go missing: the folder it named was
    # renamed, its entities fall to the fallback, the emptied source is dropped on the next
    # line, and the verifier still passes because it holds the bundle against the model rather
    # than against the declaration. So the build says which pattern died and writes nothing.
    for title, pattern in dead:
        print(f"FAIL  {title}: nothing matches `{pattern}` in export/notebooklm-sources.md")
    if dead:
        return 1
    sources = [s for s in sources if s["entities"]]

    # Two sources cannot share a file name. One would overwrite the other, the entities in the
    # loser would leave the bundle, and the run would still exit 0 — which is the exact way a
    # bundle goes quietly short. The document names are taken first, so a declared source named
    # `README` cannot quietly replace the repository's own.
    names, clash = {name for name, _ in DOCUMENTS}, False
    for source in sources:
        name = source["title"].replace("/", "-") + ".md"
        if name in names:
            print(f"FAIL  two sources want {name}: give one a heading of its own in "
                  f"export/notebooklm-sources.md")
            clash = True
        names.add(name)
        source["file"] = name
    if clash:
        return 1

    # The documents are counted and checked before anything is written, so a token nobody
    # resolves stops the build with the old bundle still on disk rather than shipping a reader
    # a pair of braces.
    documents, stale = [], False
    for name, origin in DOCUMENTS:
        found = pathlib.Path(origin)
        if not found.is_file():
            print(f"{'':>4} {'missing':<8}  {name}: no {origin} in this instance")
            continue
        documents.append((name, origin, found.read_text(encoding="utf-8")))
    written = len(sources) + len(documents)
    for i, (name, origin, text) in enumerate(documents):
        text = counted(text, sources, walked, written)
        for match in TOKEN.finditer(text):
            print(f"FAIL  {origin}: nothing counts `{match.group(0)}`")
            stale = True
        documents[i] = (name, origin, text)
    if stale:
        return 1

    # Written from scratch every run: a renamed heading would otherwise leave its old file
    # behind, and a bundle claiming an entity twice is the failure the verifier reports.
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    for name, origin, text in documents:
        (out / name).write_text(text, encoding="utf-8")
        print(f"{'':>4} {'document':<8}  {name}")

    for source in sources:
        parts = [f"# {source['title']}"]
        if source["prose"]:
            parts.append(source["prose"])
        readme = readme_of(source["entities"], source.get("type"))
        if readme:
            parts.append(context(readme, source["title"]))
        parts += [render(p) for p in source["entities"]]
        (out / source["file"]).write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
        held = len(source["entities"])
        print(f"{held:4d} {'entity' if held == 1 else 'entities':<8}  {source['file']}")

    print(f"{len(walked):4d} {'entity' if len(walked) == 1 else 'entities':<8}  in {written} "
          f"{'source' if written == 1 else 'sources'} under {out}")
    return 0


sys.exit(main())
