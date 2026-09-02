# References on `experience` — design

> Sixteen links belong to these entries. Eight are prose inside achievement bullets, four are
> lost outright, and four have no field in the master either. `experience` has nowhere to put a
> link, so this proposes the two shapes a link actually takes.

Status: proposed, nothing built. Changes `meta/core/experience-schema.md` only, so it is made
upstream in the CompanyGraph repository and comes back through a re-vendor. Nothing in this
repository changes until it does.

Third of three, and named as the smallest remaining gap by both of the others —
[`2026-09-02-date-precision.md`](2026-09-02-date-precision.md) §9 and
[`2026-09-02-experience-kind.md`](2026-09-02-experience-kind.md) §6. Independent of both.

---

## 1. Where the links are now

Sixteen links belong to the 24 experiences. They have three different fates, and the third is
the one that should worry a reader:

**Eight are carried as prose.** Every `community` entry states its link inside an achievement
bullet — *"Recording: https://page.camunda.com/camundacon-2022-on-demand"*, the four Eclipse
wiki pages, the JUG board's jug.ch, the published Camunda case study. rob-cv holds each of
these in a `url:` field. The model receives the fact and stores it as a sentence.

**Four are gone.** rob-cv states a `url:` on four project pages — the 3ap.ch case studies for
AXA Health, Stay KooooK, Flawa iQ and Aroov — and the model carries none of them. Not in prose:
absent. `2017-axa-health-platform`, `2020-stay-koook`, `2018-flawa-iq` and
`2019-aroov-realestate` contain no link at all.

**Four have no field anywhere.** The two zefix register entries added on 2026-09-02 and
companygraph.io / guestgraph.io in `2026-career-break` are prose in the model *and* prose in the
master, because rob-cv's `url:` holds one link and means "this page's own address" — which is
not what a register record is.

The first two are the same defect as in the other two specs: a fact the master states, with
nowhere in the model to land. The third says the master has the gap too, so the model should not
copy its shape.

## 2. Two different links, and the test between them

The sixteen are not one kind of thing.

`https://wiki.eclipse.org/Eclipse_Finance_Day_2012/` **is** the entry — it is where that
conference lives on the web. `https://www.zefix.ch/en/search/entity/list/firm/1201727` is not
3AP's page; 3ap.ch is. The register entry is there to let a reader check one claim the entry
makes, namely that the company was founded in November 2014.

The test: **does the link identify the entry, or support a claim inside it?**

Core already models the first half. `identity` carries `url`, typed `string`, described as *"The
company's own address on the web"*. An experience wants exactly that field for exactly that
reason, and the description transfers with one word changed.

## 3. The change

**A field, for the entry's own address:**

```
| `url` | No | string | The entry's own address on the web |
```

**A section, for what supports it** — optional, declared `Table.` in the sections table:

```
| `## References` | No | Table. What a reader can check this entry against |
```

`` `## References` is a table with these columns: ``

```
| Column | Required | Type | Description |
| --- | --- | --- | --- |
| `What` | Yes | string | The kind of document — a register entry, a recording, a certificate, a product |
| `URL` | Yes | string | Where it is |
```

### Why a table and not a list of URLs

R8 decides it: *"A field whose value is a list of records is a table wearing YAML: put it in the
body as a Markdown table and declare its columns in the schema."* And, two paragraphs on: *"a
list of* bare names *stays in frontmatter, typed `array of ref → <type>`; a list of* records
*becomes a table in the body. […] What decides the shape is whether the edge has attributes of
its own."*

A reference is a record, and the evidence is that the label already exists. `2022-talk-camundacon`
does not write the bare URL — it writes *"Recording: …"*, because a naked
`page.camunda.com/camundacon-2022-on-demand` does not say what it is. Strip the label into an
array and that information is destroyed; keep it and the pair is a record. The profile's
`## Skills` table is the same shape for the same reason: an edge with attributes of its own.

The one entry with two links today, `2026-career-break`, also shows why a single field will not
do. Two products, two addresses, neither of them "the entry's own".

## 4. Mastership: what copies and what is added

Twelve values copy mechanically — rob-cv's `url:` becomes the model's `url`, eight of them
replacing a prose sentence and four filling a hole.

Reference rows are different and the spec should be honest about it. The `What` column is not a
value rob-cv states; it is a classification the model adds. That is acceptable only under a rule
that keeps it a fact rather than an opinion, and the schema should carry one as a writing rule:

> `What` names the kind of document, not its significance. "Commercial register entry" is a
> fact about the link; "proof that the company existed" is a reading of it.

## 5. What this does not do

- **It does not touch `organisation`.** rob-cv also carries `company_url` (3ap.ch,
  likemagic.tech), which is a link to the *organisation*, not to the entry or to a claim.
  Where that belongs depends on the question the kind spec raised — whether `organisation` stays
  one string meaning four things — and it should be answered before a link is hung off it.
- **It does not add a `url` type.** The closed vocabulary in R9 has `string` and nothing for a
  URI, so both shapes here are `string`, and a malformed link breaks no rule. `identity.url` has
  been in that position since core 0.4.1 and has cost nothing; adding a type to the vocabulary is
  a larger change than this spec should carry, and is recorded in §8 instead.
- **It does not overload `source`.** `source` says which system masters this page — rob-cv or
  Local. A reference says what an outside reader can check. Both read as "where this came from"
  in English and they are unrelated: a page mastered in rob-cv can reference a register entry,
  and a page mastered locally can reference nothing.

## 6. Filling it in this instance

`url`, copied from rob-cv, prose sentence deleted where one exists:

| Entry | Value |
| --- | --- |
| `2010-eclipse-modeling-platform` | wiki.eclipse.org/ModelingPlatform/ |
| `2011-jugs-board` | jug.ch |
| `2012-talk-eclipse-day-florence` | the YouTube recording |
| `2012-talk-eclipse-finance-day` | wiki.eclipse.org/Eclipse_Finance_Day_2012/ |
| `2013-talk-eclipse-finance-day` | wiki.eclipse.org/Eclipse_Finance_Day_2013/ |
| `2014-eclipse-finance-day-organizer` | wiki.eclipse.org/Eclipse_Finance_Day_2014/ |
| `2022-talk-camundacon` | page.camunda.com/camundacon-2022-on-demand |
| `2023-camunda-case-study` | camunda.com/case-studies/likemagic |
| `2017-axa-health-platform` | the 3ap.ch case study — **currently absent** |
| `2020-stay-koook` | the 3ap.ch case study — **currently absent** |
| `2018-flawa-iq` | the 3ap.ch case study — **currently absent** |
| `2019-aroov-realestate` | the 3ap.ch case study — **currently absent** |

`## References`, four rows across three entries:

| Entry | What | URL |
| --- | --- | --- |
| `2015-3ap` | Commercial register entry | zefix.ch/…/1201727 |
| `2022-likemagic` | Commercial register entry | zefix.ch/…/1576900 |
| `2026-career-break` | Product | companygraph.io |
| `2026-career-break` | Product | guestgraph.io |

Every one of these is `source: rob-cv` except the career break, so each is corrected in rob-cv
first and copied down — which for the two zefix rows means rob-cv needs somewhere structured to
put them too, and today it has only prose. That is a rob-cv question, not a core one, and it is
the reason those links went into a sentence this morning.

## 7. Verification, and the class of defect it cannot catch

The mechanical pass gains little: `url` is an optional string, and a `Table.` section is already
checked for its header row and its column types by R9.

What it cannot catch is exactly what happened to the four project links. **An absent optional
field is indistinguishable from a fact that does not exist.** No pass over the instance can tell
"this project has no case study" from "this project's case study was dropped in the copy". The
only thing that finds it is comparing the model against its master field by field — which is
what found it here, and which nothing in the repository does routinely.

That is worth stating plainly because it generalises: for every optional field, mastership is
enforced by nobody. A drift check between rob-cv and the model — every `source: rob-cv` page,
every field the master states — is a tooling question rather than a schema one, and it is the
obvious fourth piece of work.

## 8. Findings

- **Core, `CONVENTIONS.md`** — the closed type vocabulary has no URI type. Three fields across
  two schemas now hold links as `string`. Whether that is a gap or a deliberate refusal to
  validate the outside world should be said out loud in R9, since silence reads as an oversight.
- **Core, `experience-schema.md`** — the `organisation` question from the kind spec, unchanged
  and now with a second reason to answer it.
- **Tooling, this repository** — the drift check in §7. It is the only thing that would have
  caught four missing links, and by construction no schema rule can.
