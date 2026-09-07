# One walk, two bundles — design

> `companygraph-export` produces a loadable agent skill, and NotebookLM has been fed the same
> zip. It is the wrong container for that reader, which takes files and no archive among them.
> This records what the second artifact is, why it comes out of the same export rather than a
> second skill, why it carries the model's pages exactly as they are written, and the rule that
> keeps both of them whole.

## Two readers, and only one of them is a program

The skill bundle is read by an agent that was told to load it. It can be given a convention and
will hold to it: `<!-- entity: <path> -->` marks a boundary, an H1 is a name, `model/meta.md`
holds the rules. Consolidation by root type costs it nothing, because it reads the file it
needs and the path in the comment gives back the provenance consolidation threw away.

NotebookLM is read by two synthetic hosts and a person listening to them. It strips comments,
so every entity marker is gone before a host sees it. It has no convention to be told; what it
has is a source list, and a source's title is the name a citation carries and the handle a
prompt steers with. Its published caps are 500,000 words or 200 MB per source and 50 sources on
the free tier, against a model of 190 KB — so size decides nothing here, and what a source is
named decides a great deal.

What it does not decide is what the pages under that title look like. This reader parses
Markdown and answers from what it finds, so a page rewritten on the way out is a page it
answers from less well than the one on disk. The rendering therefore changes nothing below the
source title, and the grouping is very nearly the whole of the difference between the two
artifacts.

## Why one export and not a second skill

The walk is the same walk. Both artifacts visit every type folder, recurse into `model/profiles/`
so experiences travel with their profile, and count the entities as they go. A second skill
would repeat that traversal, and the day a root type is added one of the two would keep
forgetting it — silently, because neither would know what the other saw.

**Because they share a walk they can be held to the same set of entity paths, and that is what
stops them drifting.** `export/notebooklm-verify` reads the paths each artifact actually
carries — a marker in a bundle source, and in the zip either a marker or, for the two singular
entities step 4 of the skill copies whole, the file's own path — and compares them against the
model's walk and against each other, failing by naming the path that is missing or extra
rather than a bare number that cannot say which entity moved. A raw count of `.md` files
cannot make that comparison: it cannot tell a file copied whole with no marker from one an
entity went missing from, and it cannot tell a real marker from the one `AGENTS.md` uses as a
prose example of itself, so it raises a false alarm on an export that is in fact correct: 131
marks in a correctly built zip, 134 in a correctly built bundle, 133 in the repository, three
different numbers from one walk and nothing wrong with any of them. Until the verifier read
the zip too, nothing checked the zip at all — a hand-run count was the only assertion the
procedure named there, and a check that cries wolf on a correct export is a check the next
operator learns to skip.

The failure the design exists for is a true one: on Sep 7 the committed bundle had been built
on Sep 5 and held 31 experiences against the model's 36, with a skills table that disagreed
too, and nothing anywhere said so. An episode recorded from it would have been accurate to a
model that no longer existed.

## Shape differs, coverage never does

Both artifacts carry the whole model, including `meta.md`. Cutting the schema from the
NotebookLM bundle was considered and refused: it is the model's own account of how it is built,
`experience-kinds.md` inside it holds the argument that a career break spent building products
is neither a role nor a project, and an artifact that drops it is no longer the model. Steering
a reader away from a source is the prompt's job, not the export's — a brief can say quote this
and do not summarize it, and an export that decides the same thing by omission decides it for
every future brief at once.

So the difference between the two is the container and the grouping, and the coverage
assertion is identical for both.

## The container is part of the optimization

A skill is uploaded as an archive. NotebookLM does not accept one — its list is Word, plain
text, Markdown, PDF, CSV, PowerPoint, ePub, images, audio and URLs, and an archive is not on
it. So the artifacts differ in the form they leave in:

- `dist/<instance>-skill.zip`, as now.
- `dist/<instance>-notebooklm/`, a plain folder of `.md` files, dragged in as they are.

Zipping the second and telling the reader to extract it would be a step that exists only
because the first one needed it.

## The grouping is the model's own

The export cuts the model by root type: one source per type folder under `model/`, one for
`meta/`, one for each singular entity. Eleven sources here with the two documents, each named
for a content area a reader can ask about, and it is the cut the agent bundle already makes —
so the two artifacts are grouped alike and a reader moving between them meets the same names.

**A grouping keyed to anything the instance has not declared for every entity is a cut made by
whatever a pattern happens to match.** The first bundle grouped experiences by employer and
gave UBS a source of its own because `*-ubs-*` globbed cleanly, while 3AP and LIKE MAGIC did
not glob that way and stayed in a general source of 26. The most recent role, which is what
most questions are about, was then the hardest one to cite, and nobody had decided to put it
there: the pattern language had. The model files an experience by year and kind, not by
employer, and a cut is only ever as good as what the model declares.

An instance with a narrative to make declares one anyway, in `export/notebooklm-sources.md`,
and the mechanism stays for it. It is Markdown and not JSON because the export is a procedure
an agent follows rather than a program parsing config, and Markdown lets each source carry the
sentence saying why it is one source — which is the sentence the rendering then uses to open
the file. The declaration sits beside the `export/SKILL-intro.md` the export already reads from
the same folder. Each entry names a source title and a path pattern, never a list of entity
names: a list is a second place to add an experience and the one everybody forgets. The title
is the source's own H1 and keeps its spaces; the file name is that title with every run of
whitespace turned to a single dash, because a space in a file name is awkward to type, to quote
in a shell and to read in a citation.

This instance writes no declaration, so the sentence that opens each of its sources is the
export's own: what the source holds, and when a reader wants it.

## Every entity lands in exactly one source

**An entity a declaration does not claim goes to a source named for the folder it sits in —
`Experiences` and never `Profiles` — and the export names how many did.** That is the rule
where a declaration exists: the folder rather than the root type, because `model/profiles/` is
the one folder the walk recurses into, so an experience's root type is the profile holding it
and the straggler source would be titled for the container instead of for what fell into it.
Where there is no declaration the root type is the whole cut and `Profiles` is the right title,
because that source holds the profile and everything the profile owns. Coverage is true by
construction either way rather than by discipline: there is nowhere for an entity to fall out,
and the count assertion holds whatever the declaration says.

Failing instead was the first draft of this rule and is wrong. What it would catch is a new
experience sitting in a general source rather than the era it belongs to, which is a grouping
that reads less well — not a hole. Blocking an export over it trains whoever meets the failure
to widen a pattern until it stops complaining, and the tripwire is then worth nothing. The
report is read once and acted on when it is worth acting on.

## Two instance shapes, one export

A model of one person and a model of a company take the same cut, and the numbers say it
scales. The company graph measured for this holds 342 entities across 20 root types — 104
customers, 71 features, 42 KPIs, 27 roles, 26 people — and ships as 20 sources against a cap of
50 on the free tier, its largest source 23,563 words against a per-source cap of 500,000, a
twentieth of it. It is in production use with NotebookLM in that shape. The room is worth
naming because it says where the limit is not: an instance twenty times the size of that one
still has sources inside the word cap, and would meet the source count long before it met it.

**A complete graph in one notebook is the case this serves, not the case it survives.** So the
declaration is a refinement for an instance that has a narrative and has decided what it is,
not a rung above a fallback. Where a declaration would produce more sources than the tier
allows, nothing consolidates it: `export/notebooklm-verify` refuses a bundle of more than 50
files, and the instance answers by rewriting its declaration. An export that regrouped on its
own would hand back a bundle grouped the way the instance did not write, which is a worse
answer than a build that stops and says the number.

## What the rendering does

The rendering is a script, `.claude/skills/companygraph-export/build.py`, run by the procedure
that also builds the skill bundle. It lives with the skill rather than in `export/`, because
shape belongs to the tool and `export/` holds the instance's own inputs — the reading guide and
the intro paragraph. It has to be a script and not a one-off pass: the failure this artifact
exists to catch is a bundle going quietly stale, and a rendering nobody can re-run cheaply will
be stale again.

A source opens with its own name as an H1 and one sentence saying what it holds and when to
read it, because that sentence is what the per-source summary is built from and the first thing
a reader of the source list sees. Then the folder's README where there is one, as context and
never as an entity: it says how the folder is laid out and against which schema each file is
written, so it carries no marker and is counted by nothing. Its own H1 goes where it only
repeats the title the source has just written and stays where it differs, because a heading that
differs is saying something. Then the entities, shallowest path first, so a profile leads the
experiences it owns.

**Each entity is preceded by its `<!-- entity: <path> -->` marker and then reproduced exactly
as it is written on disk** — frontmatter fence, its own H1, body, no field dropped or reordered
and no heading moved. Every rewriting loses something a reader could have been answered from,
and the frontmatter loses the most. A dateline built from it turned the 45 skills the LIKE
MAGIC role names into 1,012 characters of one sentence, where the file carries a list a reader
can follow entry by entry to the skill that holds each claim; and fields ruled to be a
validator's business left the bundle altogether, which is an artifact answering from less than
the model knows. This reader parses Markdown. It does not need the model translated for it, and
a translation is a second version of the model that has to be kept true.

The marker is kept and is the only thing between two entities. The reader strips comments, so
it says nothing to a listener and costs nothing; on disk it is an unambiguous boundary where a
bare `---` is not, since the source holding 69 skills holds 138 lines reading `---` and an
entity whose body carries a horizontal rule adds one that nothing tells apart from a fence. It
is also what makes coverage checkable without re-deriving the grouping, which is the guarantee
the second artifact exists to make.

Two documents ship as sources of their own beside the nine that carry entities: the
repository's `README.md`, and `export/notebooklm-AGENTS.md` as the bundle's `AGENTS.md`. The
guide is the answer to what a stripped bundle cannot say for itself — that references between
entities are by name, that an experience's `skills:` list names skills living in another source
and a claim's Evidence cell names experiences living in this one — and it carries the
mastership rule, so a reader meets a private document deliberately not linked as a decision
rather than as a gap. A guide that lives outside the bundle is a guide this reader never sees.

**Every count a document states is generated on the run that ships it.** A document holds no
marker, so the verifier has no opinion about it, and a guide saying 36 experiences beside a
bundle holding 37 is the staleness this artifact exists to catch, reached through the artifact's
own reading guide. So a document writes a token where a number goes — `{{entities}}`,
`{{sources}}`, `{{count:<source title>}}`, `{{count:<path>}}` — and the build substitutes what
it counted. A token nothing resolves is left standing and fails the build before a file is
written, because a reader served `{{count:Skils}}` is worse off than an owner served a build
that stopped.

## Not done

**A preset per notebook.** One bundle serves the whole instance in both shapes measured here,
and a brief already names the sources it wants worked from, so a mechanism that removes the
others would be a second place for the same decision.

Build it when a notebook is refused rather than when one is merely large: an instance past the
source cap, or a subject whose sources are so small a minority of the bundle that the rest
crowd it out. Neither has happened, and the numbers above say the first is a long way off.
