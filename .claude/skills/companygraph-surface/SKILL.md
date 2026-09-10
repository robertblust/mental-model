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
   unit's own name so a reader can match it against the editor in front of them. A rule is a
   stop and not a guess wherever it names something this run cannot settle: a source outside
   the model — a page this repository does not hold, a network's own editor — or a decision the
   surface's file leaves to the owner at each rebuild — which five skills the Skills unit
   shows, say. A stopped unit's section holds one line and nothing else, `STOP: <what the rule
   asks for> — <where it would have to be read from>`, so nothing downstream can mistake it for
   content.
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
written) and `sections` (its `##` bodies, keyed by heading). An entity also carries `dates` and,
where its type has one, `organization` with `organization_from`.

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
