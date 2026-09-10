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
