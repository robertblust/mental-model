# Robert Blust — mental model

> One person, described in [CompanyGraph](https://github.com/companygraph/meta-model): the
> reference instance of the meta-model, a company of one.

This repository is roadmap item 2 of the meta-model — a real company in the core vocabulary,
laid out by hand exactly as the [tooling](https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-08-25-companygraph-tooling-design.md)
will lay one out, before that tooling exists. Its design and what it taught are in the
meta-model's
[reference instance spec](https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-08-26-reference-instance-design.md).

```
.companygraph/manifest.json    which core this vendors, and a hash per vendored file
meta/                          core 0.1.0: CONVENTIONS.md, LICENSE, one schema per type — never edited here
sources/                       where each page's facts are mastered
proficiency-levels/            the four-rung ladder every skill claim uses
skills/                        one file per capability
values/                        one file per value
profiles/robert-blust/         the profile, and the experiences it owns
AGENTS.md                      the instance's own rules; every modelling rule is in meta/CONVENTIONS.md
.claude/skills/companygraph-*  the portable skills: validate, add an entity, export as a skill
```

The content is the whole professional portfolio, in English, drawn from the CV. Pages with
`source: rob-cv` are mastered in the CV repository and copied here; pages with
`source: Local` are written here. Nothing is invented.

Apache 2.0.
