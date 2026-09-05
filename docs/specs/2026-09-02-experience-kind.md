# `kind` on `experience` — design

> The master files these 24 entries in four folders; the model flattens them into one and the
> distinction is lost. This proposes `kind` as a required reference to a new type,
> `experience-kind` — one file per kind, the way `proficiency-level` already works — so the set
> can grow without a schema change.

Status: proposed, nothing built. Changes `meta/core/experience-schema.md` and adds
`meta/core/experience-kind-schema.md`, so both are made upstream in the CompanyGraph repository
and come back through a re-vendor. Nothing in this repository changes until they do.

Second of three. [`2026-09-02-date-precision.md`](2026-09-02-date-precision.md) is the first and
is independent of this one: it deferred `kind` on the grounds that dates and kinds are separate
questions, and this spec agrees — the case below never mentions a date except to say `kind` does
not govern one.

---

## 1. The fact the model cannot hold

rob-cv, which masters every page here except one, files these entries in four folders:

| rob-cv folder | Entries | Examples |
| --- | --- | --- |
| `content/experience/` | 6 | the four UBS periods, 3AP, LIKE MAGIC |
| `content/community/` | 8 | the four talks, the JUG board, the Modeling Platform, the case study |
| `content/projects/` | 7 | AXA Health, Aroov, Stay KooooK, the CS MDR |
| `content/education/` | 2 | the AKAD degree, the SAFe certification |

The model puts all 24 in `profiles/robert-blust/experiences/` and records nothing about which
folder they came from. The category is a fact the master states, and the model has nowhere to
put it — the same shape of defect as the AKAD year in the first spec, and the same remedy:
give it a field.

What is lost is not cosmetic. "Which of these are jobs?" is unanswerable from the model today
without reading 24 bodies and judging. A reader cannot separate a talk from an employment
period, an employer from a client, or a degree from a role, and the graph is built to be read
by things that do not judge.

## 2. `kind`, as a reference to a type

```
| `kind` | Yes | ref → experience-kind | What sort of period this is — the H1 of a file in `experience-kinds/` |
```

A new type, `experience-kind`, with one file per member in `model/experience-kinds/`:

- **Role** — a position held in an organization. The employment history.
- **Project** — a delivery inside a role, worth naming on its own. Client and internal alike.
- **Community** — work in public: a talk, a board seat, a working group, a published case.
- **Education** — a degree, a certification, a course.

`Role` rather than `Experience`, because a member named for its own type says nothing.

### An earlier draft of this spec proposed a bare-token enum. It was wrong, three times over

Worth recording, because the enum is the obvious answer and each objection to it only becomes
visible after you write it down.

**It rejected the wrong alternative.** That draft argued: *"Under R5 and R6, four types means
`roles/`, `projects/`, `community/` and `educations/` beside each other in the profile's folder,
and the experience schema's own reason for its filename rule — 'the folder then sorts
chronologically and reads as a career' — is spent."* That is true, and it is not what this
proposes. `proficiency-level` is **one** type with four entities, not four types; the analogue
here is one type, `experience-kind`, with four entities. Experiences stay in a single folder,
still named by start year, still sorting as one career. Nothing about R5 or R6 is engaged,
because an experience-kind is not owned by a profile — it sits at the container root beside
`skills/` and `proficiency-levels/`, and an experience points at it.

**R8's own test points the other way.** The rule reads: *"A set whose members carry a definition
of their own is not an enum — make it a type."* The draft answered *"a kind carries one line of
gloss and nothing that needs a file"* — and then wrote a definition for each of the four, and
closed by observing that `organisation` means something different for each of them: an employer
for a role, a client for a project, a host for a community entry, an awarding body for
education. That is definitional content belonging to the member, and a file per kind is exactly
where it goes. The four definitions above are the first paragraph of four files that do not
exist yet.

**It failed the variability test on its own first example.** §4 of that draft needed a fifth
token, `independent`, for the one entry that fits none of the four — and called that *"a token
added for one entry, which is how a set of four becomes a set of nine"*. That cost is real and
it is what a set living in a schema costs:

| | adding a member as an enum token | adding a member as a type |
| --- | --- | --- |
| edit | `meta/core/experience-schema.md`, upstream | one file in `model/experience-kinds/` |
| release | a core release and tag | none |
| re-vendor | copy `meta/core/`, update the sha256 map in `.companygraph/manifest.json` | none |
| blast radius | every instance on that core version | this instance |

The sibling type already says this out loud. `proficiency-level`'s `rank` is documented as
*"spaced in tens so a rung can be added without renumbering the others"* — that type was
designed for members arriving later. Kinds are the same shape of set, and a career acquires
categories: `independent`, `advisory`, `board` are all plausible next members, and none of them
should require a release of the metamodel.

## 3. What `kind` does not do

**It does not govern dates.** A one-off writes `end` equal to `start`, as it does today and as
the experience schema's writing rule already says. All six one-offs in this instance comply.
With the precision change in the first spec a talk becomes `2012-05-04 .. 2012-05-04`, which is
exactly a point; nothing about that depends on the kind.

The rejected alternative is worth recording because it is the obvious one: let an absent `end`
mean "one-off" when the kind is community, and "ongoing" when it is a role. That makes an
absence mean two things and resolves it by a label, so every reader of a date must first read
the kind. It also collides with the live case — `2026-career-break` is ongoing and has no
`end` — so the two meanings are not hypothetical. Date semantics stay independent of `kind`.

**It does not split the experiences folder**, change a filename, or add a section. R12 is
untouched: the filename is still the start year and a chosen slug.

**It does not order the kinds.** `proficiency-level` carries `rank` because a ladder has rungs;
kinds are a set, not a ladder. If a page ever needs them in a fixed order, that is a rendering
question first and a `rank` field only if rendering cannot answer it.

## 4. What it adds

**A schema, upstream.** `meta/core/experience-kind-schema.md`, modeled on
`proficiency-level-schema.md` and shorter, since it carries no `rank`:

| Field | Required | Type | Description |
| --- | --- | --- | --- |
| `source` | Yes | ref → source | Where this page's facts are mastered |
| `source-id` | No | string | The identifier this page has in its source |

`# [Name]` for the H1, a `>` tagline saying what the kind is in one line, and a `## What it
means` section — the same three-part shape every other singular-value type here uses.

**A folder, here.** `model/experience-kinds/` with `role.md`, `project.md`, `community.md`,
`education.md`. R7 singularizes the folder to `experience-kind`; R12 gives each file the slug of
its H1.

**One field on `experience`**, `kind`, required, `ref → experience-kind`.

### Why `experience-kind` and not `kind`

The folder would be `model/kinds/`, sitting at the container root beside `skills/` and
`sources/`. `kind` is a word this graph will want again — a source has kinds, an entity has a
type — and a bare `kinds/` claims it for one use. The house style is already the specific
compound: the ladder type is `proficiency-level`, not `level`. `experience-kind` follows it.

The cost is a longer `ref → experience-kind` in one schema row, which nobody reads twice.

## 5. Filling it in this instance

The value is derived, not decided: an entry takes the kind matching the rob-cv folder that
masters it. That makes 23 of 24 mechanical —

- **Role** — `1999-ubs-trainee`, `2001-ubs-engineer`, `2004-ubs-solution-manager`,
  `2009-ubs-architect`, `2015-3ap`, `2022-likemagic`
- **Project** — `2015-swisscard-data-integration`, `2015-swisscom-agile-cockpit`,
  `2016-credit-suisse-mdr`, `2017-axa-health-platform`, `2018-flawa-iq`,
  `2019-aroov-realestate`, `2020-stay-koook`
- **Community** — `2010-eclipse-modeling-platform`, `2011-jugs-board`,
  `2012-talk-eclipse-day-florence`, `2012-talk-eclipse-finance-day`,
  `2013-talk-eclipse-finance-day`, `2014-eclipse-finance-day-organizer`,
  `2022-talk-camundacon`, `2023-camunda-case-study`
- **Education** — `2002-wirtschaftsinformatik-fh`, `2016-safe-practitioner`

— and leaves one open.

### The one that does not fit

`2026-career-break` is `source: Local` and has no rob-cv folder to inherit from. Its H1 is
*"Career break — ideation and product building"*: a self-directed period, ongoing, whose
achievements are two published open-core products. Three readings:

1. **Project** — what it produced. Understates it: the period is not a delivery inside a role,
   and there is no role.
2. **Role** — a period held, self-employed. Overstates it: there is no organization, and
   `organisation` is where a reader would look for one.
3. **A fifth kind, `Independent`** — a self-directed period with no employer. Honest, and a
   category many careers now have.

**Recommended: (3), and the recommendation changed with the modeling.** As an enum token this
was the expensive option and the draft hedged it against "if a second such period is
foreseeable". As a type it is one file in this repository — no core edit, no release, no
re-vendor — so the question collapses back to the only one that should have mattered: is it
true? It is. The period is not a project and not a role, and saying so costs a file.

## 6. Verification

`kind` becomes a reference, so it is covered by the rule that already covers every reference in
this instance rather than needing one of its own. The agent pass gains:

- every experience has `kind`, and its value is the H1 of a file in `experience-kinds/`;
- every file in `experience-kinds/` clears its schema — R9's floor, `source` resolving, the H1
  and tagline present;
- nothing else, because `kind` implies nothing else.

**What the parser does and does not do, stated precisely, because the draft overclaimed the
enum's story here.** `lib/instance.mjs` in companygraph/meta-model reads a scalar frontmatter
value as a reference only when it happens to resolve to a canonical name: it becomes an edge
when it resolves and stays a plain fact when it does not. So a misspelled `kind` is not a parse
error, exactly as a misspelled enum token would not have been. The parser catches neither.

Two things do change, and both are real:

- **The value becomes checkable by an existing rule.** `verify/check.mjs` mechanically checks
  part of R4 against declared `ref → <type>` fields. An enum would have needed R8's check, which
  has had no subject since core 0.4.1 and which no script implements.
- **The kind becomes a node.** As a token it is a string on 24 entities; as an entity it is one
  node with 24 edges pointing at it. "Which of these are roles?" stops being a string match over
  frontmatter and becomes an edge traversal — and the kinds appear on the model page, drawn,
  the way proficiency levels already are.

That second point is the one worth weighing: it is also the argument for *not* doing this, if
five more nodes on the stage is a cost. It is a small graph and four nodes with a clear job in
it are not clutter, but the drawing is a consequence and should be looked at rather than
discovered.

## 7. Findings for the third spec

- **Core, `experience-schema.md`** — still no field for a reference. Unchanged from the first
  spec's §9 and still the smallest remaining gap: zefix and companygraph.io are URLs inside
  achievement prose because prose is the only place they can go.
- **Core, `experience-schema.md`** — `organisation` is optional and means a different thing for
  each kind: an employer for a role, a client for a project, a host for a community entry, an
  awarding body for education. The schema's writing rules already say the last one. With `kind`
  as a type there is now a place to say the other three — each kind's own `## What it means`
  section — which turns the question from "one field with four meanings, or a modeling smell?"
  into something answerable in prose the model actually holds. Whether that is enough, or
  whether `organisation` should split, is still the question to ask before anything is built on
  it.
