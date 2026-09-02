# Date precision in `experience` — design

> `start` and `end` are fixed at `YYYY-MM`. The instance therefore invents months it has no
> document for, and drops days it does have into prose. One rule causes both. This proposes
> `date` as a precision the source sets, not a shape the schema fixes.

Status: proposed, nothing built. This changes `meta/core/` — `CONVENTIONS.md` and
`experience-schema.md` — so it is made upstream in the CompanyGraph repository and comes back
through a re-vendor. Nothing in this repository changes until it does.

Scope is deliberately one thing. The request that prompted this also asked for an experience
*kind* (education, project, talk) with date rules per kind; §6 says why that is a separate
spec and what has to be decided first.

---

## 1. The defect

The AKAD diploma states a year. The schema types `start` as `date`, and the experience schema's
description of that field says `YYYY-MM`. So the page reads:

```yaml
start: 2002-01
end: 2006-01
```

`2002-01` is an invention. No document names a month; rob-cv, which masters the page, says
`2002`, and LinkedIn says 2002–2006. Across all 24 experiences this is the only date on which
the model and its master disagree — and it disagrees because the model *cannot say what the
master says*.

`2006-01` is a different case, and worth separating: the diploma scan is filed
`Robert_Blust_Wirtschaftsinformatiker_FH_2006_01_13.pdf`, so the diploma is dated 13 January
2006 and the January is real. One entry, two fields, two different precisions available — and
the current form can express neither. It rounds a known day up and manufactures an unknown
month.

This is not an instance defect to be corrected in the instance. On 2026-09-02 the invented
January was reviewed and deliberately kept, because every available fix was worse: a different
invented month, or a wrong year. The page is as good as the schema allows.

## 2. Why nothing caught it

`2002-01` is well formed. It matches `YYYY-MM`, so the mechanical pass passes it, and R0's
agent pass has nothing to compare it against — the file does not record what the source
document said, so no reader of the file alone can tell an observed month from a filled-in one.

The rule was found by a person opening the diploma. That is the only way it could have been
found, and it is the same failure mode R11 describes for flow sequences: *"nothing there is
malformed when it does"*. A well-formed lie passes every check that exists.

There is a second, quieter gap behind it. `CONVENTIONS.md` R9 names `date` in the closed type
vocabulary and never says what a `date` looks like. The form `YYYY-MM` is stated once, in the
Description column of one field in one schema. Two schemas could type a field `date` and mean
different things, and no rule would be broken. `date` is used in exactly two places today —
`experience.start` and `experience.end` — so this has cost nothing yet.

## 3. Precision is a property of the source, not of the type

The current rule is wrong in both directions at once, which is the clearest sign it is the
wrong rule.

**It invents precision.** One entry, above.

**It discards precision.** Seven day-level dates are recorded in this instance today, and all
seven live in prose because no field can hold them:

| Entry | In the body |
| --- | --- |
| `2012-talk-eclipse-day-florence` | 4 May 2012 |
| `2012-talk-eclipse-finance-day` | 16 October 2012 |
| `2013-talk-eclipse-finance-day` | 5 November 2013 |
| `2014-eclipse-finance-day-organizer` | 31 October 2014 |
| `2016-safe-practitioner` | 18 October 2016, 18 October 2017 |
| `2022-talk-camundacon` | 6 October 2022 |

Each of those entries also carries `start`/`end` at month grain, so the date is stated twice at
two precisions, and only the vaguer one is queryable. The reference scans hold four more:
the UBS boundaries are dated 31 March 2001, 31 July 2004, 30 September 2009 and 31 January 2015
on the Ausbildungsbestätigung, the two Zwischenzeugnisse and the final Zeugnis.

A talk does not have "a month". A diploma does not have "a month". Each has whatever its
document states, and what varies is not the *kind* of experience but the *source*.

## 4. The change

**`date` is `YYYY`, `YYYY-MM` or `YYYY-MM-DD`.**

Stated once in `CONVENTIONS.md` R9, beside the vocabulary, rather than per field — so the
lexical form of a type is core's business and not a description's:

> `date` is `YYYY`, `YYYY-MM` or `YYYY-MM-DD`. A date is written at the precision its source
> states and never at more; an author may deliberately record less. A shorter form is an
> interval, not a point: `2002` is the whole year, and comparisons take its earliest instant,
> so `2002` orders before `2002-03`.

Two things that rule is careful about:

- **Precision is a ceiling, not a floor.** "Never more than the source" makes the invented
  January illegal. It does not force a day onto every employment period whose Zeugnis names
  one — recording `2009-10` where the document says 30 September 2009 stays legal, and for
  employment it is what the CV wants to render.
- **A partial date is an interval.** Anything that sorts or compares needs to know that
  `2002` is not `2002-01-01`. Naming it in the rule keeps every implementation agreeing.

`experience-schema.md` then loses the form from its two descriptions and keeps only the
meaning:

```
| `start` | Yes | date | When the period began |
| `end`   | No  | date | Absent means the period is ongoing. |
```

Nothing else in the schema changes.

## 5. What reads dates today

- **R12, the experience filename** — "the start year, then a `-`, then a slug". Every form
  carries a year, so this is unchanged, and the folder still sorts chronologically.
- **The writing rule "a one-off sets `end` equal to `start`"** — unchanged, and it gets better:
  a talk becomes `2012-05-04 .. 2012-05-04`, which is what a one-off *is*, and its date stops
  being duplicated in prose at a precision the field could not hold.
- **The writing rule "a period still running has no `end`"** — unchanged. Absent already means
  ongoing; no sentinel value is needed and none is proposed.
- **R1–R13 otherwise** — no other rule mentions a date.

## 6. What this deliberately does not do

> **Settled since, and the reasoning here did not survive.** `kind` shipped in core 0.6.0 as a
> *type* — `experience-kind`, one file per member in the instance — not as the bare-token enum
> point 2 below argues against. That point rejects the wrong alternative: it reads "making them
> types puts them in `educations/`, `talks/` and `projects/` beside `experiences/`", which is
> four types. One type with four members is what `proficiency-level` already is, and it leaves
> the experiences folder whole. Point 3's conditional-requiredness problem never arose, because
> no date rule was made to depend on a kind — §3's finding held, and precision follows the
> source document rather than the category. Point 1 was right and is why the two are separate
> specs at all. Kept as written, with this note, because a spec that quietly acquires the
> conclusion it argued against is worth less than one that shows where it was wrong.


No `kind` field, no per-kind date rules, no conditional requiredness. Three reasons, and the
third is the one that needs a decision before that spec can be written:

1. The date problem is not a kind problem. §3 shows the precision varies with the source
   document, and a talk with a known day and a talk with only a year are the same kind.
2. R8 already rules on the shape: *"A set whose members carry a definition of their own is not
   an enum — make it a type."* If education, talk and project carry their own rules, they are
   not bare tokens. But making them types puts them in `educations/`, `talks/` and `projects/`
   beside `experiences/` under R5 and R6, and the one folder that "sorts chronologically and
   reads as a career" — the experience schema's own stated reason for its filename rule —
   fragments into five.
3. "A talk has a date, not a range" means `end` is required *if* the kind is a talk. The
   Required column is `Yes` or `No`. A schema in CompanyGraph has no way to say *conditional*,
   and giving it one is a real expansion of what a schema is — not a detail to discover while
   writing the field.

## 7. Migration in this instance, after the re-vendor

Required, because it is the invention:

- `2002-wirtschaftsinformatik-fh`: `start: 2002-01` → `2002`. `end` stays `2006-01`, or becomes
  `2006-01-13` if the diploma date is what the entry means.

Recommended, because the precision exists and is currently duplicated in prose:

- the four talks and `2016-safe-practitioner` take their day from the body (§3 table), and the
  body sentence keeps the date only where it reads as prose rather than as data.

Not recommended:

- the four UBS periods stay at month grain. The Zeugnisse name the days, but the CV renders
  months, and a start day on an employment period invites a precision no reader needs.

Each of these is a `source: rob-cv` page, so each is corrected in rob-cv first and copied down.

## 8. Verification, and the part no check reaches

The mechanical pass gains one form check and loses nothing: `^\d{4}(-\d{2}(-\d{2})?)?$` in
place of `^\d{4}-\d{2}$`.

What no check reaches is the rule that matters. Nothing in the file records what its source
document said, so "never more precision than the source" is unverifiable from the instance
alone — exactly like the invention it replaces. It is enforceable at the moment of writing, by
whoever has the document open, and not afterwards. That is a real limit and the spec does not
pretend otherwise; it is the same class as the writing rules, which is where it belongs.

The re-vendor changes the hash of `CONVENTIONS.md` and `experience-schema.md` in
`.companygraph/manifest.json`. Readers that assume `YYYY-MM` break on the new forms, so this is
a breaking change for tooling and takes a minor bump, not a patch. Core is already at 0.5.0
upstream while this instance vendors 0.4.1, so the target is **0.7.0**. It shipped there:
0.6.0 was taken by `experience-kind` while this spec sat open.

Upstream tooling is untouched. `lib/instance.mjs` parses structure — it cites R2, R3, R4, R5,
R6, R7, R9 and R13 — and validates neither a `date` form nor an `enum` value. Field-level types
are agent-enforced there as they are here, which is why the paragraph above matters more than
the regex.

## 9. Findings for the next specs

- **Core, `experience-schema.md`** — there is no field for a reference. The register entries
  behind the two founder claims (zefix) and companygraph.io / guestgraph.io in
  `2026-career-break` are all URLs inside achievement prose, because prose is the only place
  they can go. A `url` or `references` field is the smallest next spec, and it is adjacent to
  this one: a date's precision and a claim's evidence are the same question asked twice.
- **Core, the type set** — the `kind` question above, once §6.3 is decided.
- **Core, `CONVENTIONS.md`** — `date` is the only type in the closed vocabulary whose lexical
  form was never stated. Worth a pass over the others to check that no second one is being
  held up by convention alone.
