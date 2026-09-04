# Robert Blust — mental model

> One person, described in [CompanyGraph](https://github.com/companygraph/meta-model): the
> reference instance of the meta-model, a company of one.

This repository is roadmap item 2 of the meta-model — a real company in the core vocabulary,
laid out by hand exactly as the [tooling](https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-08-25-companygraph-tooling-design.md)
will lay one out, before that tooling exists. Its design and what it taught are in the
meta-model's
[reference instance spec](https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-08-26-reference-instance-design.md).

```
.companygraph/manifest.json    which units this vendors, and a hash per vendored file
meta/core/                     core 0.11.0, copied whole and never edited here
model/                         the company — everything under here is an entity, nothing else is
  identity.md                  who the company is
  vision.md                    the future it works toward
  sources/                     where each page's facts are mastered
  proficiency-levels/          the four-rung ladder every skill claim uses
  skills/                      one file per capability
  values/                      one file per value
  profiles/robert-blust/       the profile, and the experiences it owns
AGENTS.md                      the instance's own rules; every modeling rule is in meta/core/CONVENTIONS.md
.claude/skills/companygraph-*  the portable skills: validate, add an entity, export as a skill
```

The content is the whole professional portfolio, in English. Every page is mastered here —
`source: Local`, corrected in this repository and nowhere else. It began as a copy of a private
CV repository written to generate job applications; that repository is archived now and this one
took over as the master. Nothing is invented.

## License

[CC BY 4.0](LICENSE) for everything written here — the skills, the values, the profile and its
experiences, the documents under `docs/`. Use it, quote it, build on it; credit it. The prose is
the artefact, which is why this is a content license rather than a code license.

`meta/core/` is not written here: it is CompanyGraph core, vendored at the release the manifest
names, and stays under its own [Apache 2.0](meta/core/LICENSE).
