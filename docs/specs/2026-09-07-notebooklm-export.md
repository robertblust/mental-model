# One walk, two bundles — design

> `companygraph-export` produces a loadable agent skill, and NotebookLM has been fed the same
> zip. It is the wrong shape for that reader: the delimiters that carry provenance are HTML
> comments and invisible to it, the frontmatter arrives as literal text, and 36 experiences
> land under a single citation label. This records what the second artifact is, why it comes
> out of the same export rather than a second skill, and the rule that keeps both of them
> whole.

## Two readers, and only one of them is a program

The skill bundle is read by an agent that was told to load it. It can be given a convention and
will hold to it: `<!-- entity: <path> -->` marks a boundary, an H1 is a name, `model/meta.md`
holds the rules. Consolidation by root type costs it nothing, because it reads the file it
needs and the path in the comment gives back the provenance consolidation threw away.

NotebookLM is read by two synthetic hosts and a person listening to them. It strips comments,
so every entity marker is gone before a host sees it. It has no convention to be told; what it
has is a source list, and a source's title is the name a citation carries and the handle a
prompt steers with. Its published caps are 500,000 words or 200 MB per source and 50 sources on
the free tier, against a model of 190 KB — so size decides nothing here, and everything is
decided by which text sits under which title. `profiles.md`, 88 KB and 36 experiences, is one
title. A listener never asks about profiles; they ask about the career break.

## Why one export and not a second skill

The walk is the same walk. Both artifacts visit every type folder, recurse into `model/profiles/`
so experiences travel with their profile, and count the entities as they go. A second skill
would repeat that traversal, and the day a root type is added one of the two would keep
forgetting it — silently, because neither would know what the other saw.

**Because they share a walk they can share a count, and a shared count is what stops them
drifting.** The export asserts the same number against both artifacts and against the
repository, and fails naming the difference. That failure is the one this design exists for: on
Sep 7 the committed bundle had been built on Sep 5 and held 31 experiences against the model's
36, with a skills table that disagreed too, and nothing anywhere said so. An episode recorded
from it would have been accurate to a model that no longer existed.

## Shape differs, coverage never does

Both artifacts carry the whole model, including `meta.md`. Cutting the schema from the
NotebookLM bundle was considered and refused: it is the model's own account of how it is built,
`experience-kinds.md` inside it holds the argument that a career break spent building products
is neither a role nor a project, and an artifact that drops it is no longer the model. Steering
a reader away from a source is the prompt's job, not the export's — a brief can say quote this
and do not summarize it, and an export that decides the same thing by omission decides it for
every future brief at once.

So the difference between the two is rendering and grouping, and the coverage assertion is
identical for both.

## The container is part of the optimization

A skill is uploaded as an archive. NotebookLM does not accept one — its list is Word, plain
text, Markdown, PDF, CSV, PowerPoint, ePub, images, audio and URLs, and an archive is not on
it. So the artifacts differ in the form they leave in:

- `dist/<instance>-skill.zip`, as now.
- `dist/<instance>-notebooklm/`, a plain folder of `.md` files, dragged in as they are.

Zipping the second and telling the reader to extract it would be a step that exists only
because the first one needed it.

## The grouping belongs to the instance

An export that ships with CompanyGraph cannot know that this model's experiences group by
employer. That is true of Robert Blust and not of a company graph, and a rule that reached into
the instance to guess would be wrong on the first instance that filed things differently.

The instance declares it, in `export/notebooklm-sources.json`, beside the `export/SKILL-intro.md`
the export already reads from the same folder. Each entry names a source title and a path
pattern, never a list of entity names: a list is a second place to add an experience and the
one everybody forgets. The title is the filename the reader sees:

```
Robert Blust — the short version
How this model works
Timeline — every experience in order
Skills, and the evidence for each
UBS, 1999–2015
3AP, 2015–2022
LIKE MAGIC, 2022–2026
The career break, 2026
CompanyGraph and GuestGraph
Talks, boards and published cases
Education and qualifications
```

Absent the file, the export falls back to one source per root type under a readable name, which
is the skill bundle's grouping with better titles. Present, it produces the list above: eleven
titles against a cap of fifty, each one a phrase a host would say out loud.

## Every entity lands in exactly one source

**An entity a declaration does not claim goes to its root type's source, and the export names
how many did.** Coverage is then true by construction rather than by discipline: there is
nowhere for an entity to fall out, and the count assertion holds whatever the declaration says.

Failing instead was the first draft of this rule and is wrong. What it would catch is a new
experience sitting in a general source rather than the era it belongs to, which is a grouping
that reads less well — not a hole. Blocking an export over it trains whoever meets the failure
to widen a pattern until it stops complaining, and the tripwire is then worth nothing. The
report is read once and acted on when it is worth acting on.

## Two instance shapes, one export

The eleven titles above are a model of one person, where profiles is not a question anyone asks
and the career break is. An instance of a company is a different shape and takes a different
grouping rather than a coarser one: one source per root type, which is what the skill bundle
already produces and what a company is actually asked about — who does what, how teams work,
what we measure, who we serve.

**A complete company graph in one notebook is the case this serves, not the case it survives.**
The reference instance holds 342 entities across 20 root types — 104 customers, 71 features, 42
KPIs, 27 roles, 26 people — and it fits with room nobody will use: 20 sources against a cap of
50 on the free tier, its largest source 23,563 words against a per-source cap of 500,000, a
twentieth of it. The room is worth naming because it says where the limit is not: an instance
twenty times the size of that one still has sources inside the cap, and would meet the source
count long before it met the word count.

So the declaration is a refinement for an instance small enough to have a narrative, not a rung
above a fallback. Absent it the export groups by root type, which is the right answer for a
company and a merely adequate one for a person. Where a declaration would produce more sources
than the tier allows, the export consolidates to root type and says it did, rather than
emitting a bundle that cannot be uploaded.

## What the rendering does

Per entity, as it is inlined into a source:

- The frontmatter becomes a dateline a person can read — `Role · UBS AG · Oct 2009 – Mar 2015` —
  because `source: Local` and `rank: 20` are instructions to a validator and noise to a host.
- The entity's H1 demotes to H2, so the file's own H1 is the source's subject and the entities
  are its parts.
- The `>` tagline stays directly under its heading. It is one sentence written to stand alone,
  which is what a host reads aloud.
- The entity comment is dropped. It is invisible to this reader, and the heading with its
  dateline carries what a listener could use of it.
- Each file opens with a paragraph saying what it holds, because that paragraph is what the
  per-source summary is built from and the first thing a reader of the source list sees.

## Not done

**A preset per notebook.** One bundle serves the whole instance in both shapes measured here,
and a brief already names the sources it wants worked from, so a mechanism that removes the
others would be a second place for the same decision.

Build it when a notebook is refused rather than when one is merely large: an instance past the
source cap, or a subject whose sources are so small a minority of the bundle that the rest
crowd it out. Neither has happened, and the numbers above say the first is a long way off.
