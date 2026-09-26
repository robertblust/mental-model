# Robert Blust — Mental Model

> One person, described in [CompanyGraph](https://github.com/companygraph/meta-model): the
> reference instance of the meta-model, a company of one.

This repository is roadmap item 2 of the meta-model — a real company in the core vocabulary, laid out by hand exactly as the [tooling](https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-08-25-companygraph-tooling-design.md) will lay one out, before that tooling exists. Its design and what it taught are in the meta-model's [reference instance spec](https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-08-26-reference-instance-design.md).

```
.companygraph/manifest.json    which units this vendors, and a hash per vendored file
meta/core/                     core at the release .companygraph/manifest.json names, copied whole and never edited here
model/                         the company — everything under here is an entity, nothing else is
  identity.md                  who the company is
  vision.md                    the future it works toward
  brand.md                     what it looks and sounds like, as meaning; the values live where its References point
  strategic-objectives/        what must become true for the vision to be reached
  strategies/                  how one gets reached, and what the route rules out
  kpis/                        one file per quantity the company has chosen to watch
  sources/                     where each page's facts are mastered
  proficiency-levels/          the four-rung ladder every skill claim uses
  experience-kinds/            the five kinds an experience can be
  achievement-kinds/           the kinds an achievement is filed under
  skills/                      one file per capability
  values/                      one file per value
  roles/                       one file per seat the company needs filled
  processes/                   how the company does its work, phase by phase
  surfaces/                    one file per place the model is published
  domains/                     one file per area of the company, named by its products and its concepts
  products/                    one file per thing the company puts in front of people
  features/                    one file per thing a product lets someone do
  concepts/                    one file per word the company means something exact by
  questions/                   one file per question visitors ask, and the entities its answer rests on
  profiles/robert-blust/       the person, and the experiences it owns
  profiles/ai-agent/           the agent that drafts, builds, reviews and answers; it owns no experiences yet
  profiles/*-voice/            the agents that speak the talks, one per language
AGENTS.md                      the instance's own rules; every modeling rule is in meta/core/CONVENTIONS.md
.claude/skills/companygraph-*  the tooling's skills: validate, export as a skill, produce a surface, build a profile from documents
```

The content is the whole professional portfolio, in English. Every page is mastered here — `source: Local`, corrected in this repository and nowhere else. It began as a copy of a private CV repository written to generate job applications; that repository is archived now and this one took over as the master. Nothing is invented.

## License

[CC BY 4.0](LICENSE) for everything written here — the skills, the values, the profile and its experiences, the documents under `docs/`. Use it, quote it, build on it; credit it. The prose is the artifact, which is why this is a content license rather than a code license.

`meta/core/` is not written here: it is CompanyGraph core, vendored at the release the manifest names, and stays under its own [Apache 2.0](meta/core/LICENSE).
