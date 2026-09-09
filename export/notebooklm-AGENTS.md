# Robert Blust — mental model

> One person described in CompanyGraph: a profile and the {{count:model/profiles/robert-blust/experiences}} experiences it owns, the {{count:Skills}}
> skills those experiences evidence, the values the work is held to and the schema underneath
> all of it. This notebook is that model whole — {{entities}} entities across {{sources}} sources, every page
> as it is written in the repository it is mastered in.

The model answers questions about one working life. What he built and where, what a period
contained and what came out of it, which capability a piece of work shows, at what level a skill
is claimed and on what evidence, why a career break is filed as an experience rather than a gap,
and what he holds to while deciding. A question about a claim is the one this model is shaped
for: every skill claimed names the work that shows it, and every experience names the skills it
evidences, so the answer to “on what basis” is in the model rather than in a summary of it.

What is not here is not withheld and not hidden. There is no salary, no assessment written by
anyone else and no scan of a diploma or an employment reference, for the reason the last section
gives.

## The sources

Two of these sources carry documents about the model — this guide and the repository's README.
The rest carry its {{entities}} entities.

| File | Contains | Read it when you need to |
| --- | --- | --- |
| `AGENTS.md` | this guide | Read anything else here |
| `README.md` | the repository's README | See how the model is laid out and licensed |
| `profiles.md` | the profile and its {{count:model/profiles/robert-blust/experiences}} experiences, {{count:Profiles}} entities | Ask what he did, where, when and what it produced |
| `skills.md` | {{count:Skills}} skills, one per capability | Look up what a capability is and what practicing it looks like |
| `values.md` | {{count:Values}} values | Ask how he decides and what he refuses |
| `experience-kinds.md` | the {{count:Experience kinds}} kinds an experience can be | Understand why a break, a talk or a degree is filed as it is |
| `proficiency-levels.md` | the {{count:Proficiency levels}} rungs a skill is claimed on | Weigh what Expert or Competent means here |
| `sources.md` | the {{count:Sources}} source the pages are mastered in | Check where a fact would be corrected |
| `surfaces.md` | the {{count:Surfaces}} surface the model is published to by hand | Ask what reaches a published place and what is left out |
| `identity.md` | who the model is about | Find the name, the location and the public addresses |
| `vision.md` | the future the model works toward | Ask what the work is building toward |
| `meta.md` | CompanyGraph core: its conventions and its schemas, {{count:Meta}} entities | Check what a page must carry and how a reference resolves |

## How to read the model

A source is a stack of whole pages. Each one begins at a line reading
`<!-- entity: model/skills/java.md -->`, which names the file it comes from; then comes the
page, unchanged. Its frontmatter fence carries the fields a validator reads — the kind of
experience, the organization, the start and end dates, the group a skill belongs to, the skills
an experience evidences. The `#` heading under the fence is the entity's name, and that name is
the handle everything else uses.

**References between entities are by name, not by link.** An experience's `skills:` list names
skill entities that live in `skills.md`, spelled exactly as their headings spell them. The
Skills table in the profile in `profiles.md` claims each of those skills at a level and gives an
Evidence cell naming the experiences that show it, one sentence per experience, in the order
they happened. A skill page itself claims nothing about him: it defines the capability and says
what practicing it looks like, because the level and the evidence are one person's and belong in
the profile. To follow a claim, take the name and find the heading.

`meta.md` holds the rules every entity obeys — which fields a page of each type must carry, how
a date is written, and the rule that a reference naming something that does not exist is an
error rather than a note. Read it when an answer turns on whether the model is allowed to say
something, not on what it says.

## What a claim rests on

Every page here is mastered in this repository. There is no upstream system to correct first: a
fact that is wrong is corrected here and nowhere else, which is why every page carries
`source: Local`.

A fact enters from Robert Blust or from a document — a record, a deck, a published page. A
document that is public is linked, in a `url` field or a `## References` row: a talk's
recording, a published case study, a commercial register entry. **A document that is private is
deliberately not held here.** Employment references, diplomas and certifications are the source
of dates and of what a period contained, they are read when a page is written, and they stay in
his own vault and are shown on request. So an entry whose evidence is private carries the fact
and no link, and that missing link is a decision rather than a gap: read it as a claim its
author can produce a document for, not as a claim with nothing behind it.
