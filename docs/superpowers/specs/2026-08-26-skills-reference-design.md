# Skills as our own vocabulary — design

> The skills of this instance re-cut as a curated vocabulary of our own — 60 skills at the
> grain the market hires for, each defined here, person-neutral, and anchored to SFIA 9 and
> ESCO where those name the same thing.

Status: design agreed, nothing built. Instance-owned: nothing here changes `meta/` or the
meta-model. What it teaches core is in §8 and is proposed to the meta-model separately.

Supersedes an earlier draft of this spec that filed all 147 SFIA skills. That draft is in the
branch history; §2 says why it was dropped.

---

## 1. What the first cut got wrong

The first 23 skills were cut from the CV's tag cloud by feel, and every `## In practice` was
written as what one person did with the skill. Two defects, one cause:

- **A skill is shared.** Many profiles claim the same skill, each with its own level and
  evidence; the schema already puts that claim in the profile's Skills table. A skill file that
  narrates one person's history is the profile's row restated — and wrong the moment a second
  profile claims it. `## In practice` must be person-neutral.
- **The grain was arbitrary.** "Database design and operation" is two skills to anyone who has
  hired for either. With no reference vocabulary there was nothing to check a cut against.

Both are core findings (§8). The instance fixes them by adopting a vocabulary — its own.

---

## 2. The vocabulary: ours, anchored

Four public sources were compared row by row — SFIA 9, ESCO v1.2, O*NET, Lightcast Open
Skills — against 69 candidates drawn from the CV's `skills.yaml`, the 16 job postings under
`applications/`, and the first 23 skills. The comparison, with every source's name for every
row and each source's licence, is
[`docs/superpowers/research/2026-08-26-skill-sources-compared.md`](../research/2026-08-26-skill-sources-compared.md).

What it showed:

- **SFIA 9** names every leadership, architecture, governance and operations skill at the right
  grain, and nothing in the modern layer — no Kubernetes, no SRE, no RAG, no agentic
  development. Filing all 147 (the earlier draft) would also have shipped Radio frequency
  engineering and Marketing campaign management, which nobody here will claim.
- **ESCO** is free for any reuse with stable URIs and German labels, and has a concept for
  about half the rows — generic ones.
- **Lightcast** has the market grain for almost every row and a licence that is not open.
- **O*NET** is products.

So the decision: **the skill set is curated by us, at the grain the postings use.** Every
definition and every `In practice` is written here, in our words. Where SFIA or ESCO names
the same skill, the file cites it; where they do not, it says so. Lightcast and O*NET were
consulted and are not cited. Nothing is vendored, nothing is copied — the licence question
disappears with the copying.

Sixty skills (appendix). The rule for adding one: a capability a profile can claim with
evidence, at the grain a job posting would name it, distinct from its neighbours in what
someone doing it does — not in which product they use.

---

## 3. The skill file

Unchanged schema (`meta/skill-schema.md`): `source`, optional `group`, H1, `>` definition,
optional `## In practice`. Every file here has all of them. The rules this spec adds:

```markdown
---
source: Local
group: Data
---

# Database design

> How data is stored so that the systems reading and writing it stay correct and fast as they change.

## In practice

Turn a domain model into tables, keys, constraints and indexes. Decide what is normalized and
what is deliberately not. Write the migration that gets a live system from the old shape to
the new one without losing a row. Typical tools: PostgreSQL, Oracle, MSSQL, MongoDB.

Reference: SFIA 9 DBDS — Database design · ESCO design database scheme
http://data.europa.eu/esco/skill/6c08403c-a5bb-4868-b8c2-b7d039c0e511
```

- **H1 is the curated name** (appendix), ours, in house style.
- **`group`** is one of nine: Leadership and strategy, Architecture, AI, Cloud and platform,
  Data, Software development, Modeling and process, Security and compliance, Advisory. They
  are the sections of the comparison; the schema's open question about groups gets 60 data
  points on a grouping we chose.
- **`> definition`** — one line, ours, saying what the skill is. It starts with the thing
  itself, never with a wrapper — no "The practice of", "The discipline of", "The ability to".
- **`## In practice`** — two to four sentences in the **imperative, without a subject**: each
  sentence starts with the bare verb — "Assess …", "Translate …", "Engage …" — never "Someone
  doing this …" or "They …". Person-neutral: no name, employer, date or number from any
  profile. Products appear only in a closing `Typical tools:` clause, and only where a product
  is what the skill is done with. A reader who wants to know who claims the skill reads the
  profiles.
- **The reference line is fixed in form**, last in the section, one line:
  `Reference: SFIA 9 <CODE> — <SFIA name>` or `Reference: SFIA 9 none`, then
  ` · ESCO <preferred label> <URI>` or ` · ESCO none`. Only a source that names the *same*
  skill is cited — a broader parent is not a match. The form is what makes the line grep-able
  and, later, promotable to schema fields without re-reading prose.

Filename: kebab-case of the H1, as R2 and the existing files already do.

The drafted texts for all 60 — definition, In practice, reference — are the third table of
the comparison document. They were reviewed row by row before this spec was approved and are
written into the files as they stand there; the build does not redraft them.

---

## 4. What moves where — the 23 existing skills

| today | becomes |
| --- | --- |
| Scaling engineering organizations | Engineering leadership |
| Technology strategy and governance | IT strategy, IT governance |
| AI strategy and governance | AI strategy, AI governance |
| Stakeholder and vendor management | Stakeholder management, Vendor management |
| Agentic AI development | Agentic AI development |
| Cloud platform engineering | Cloud architecture, Container orchestration (Kubernetes), Platform engineering |
| Infrastructure as code and delivery automation | Infrastructure as code, CI/CD, DevOps |
| Enterprise architecture | Enterprise architecture |
| Business architecture | Business architecture |
| Domain-driven design | Domain-driven design |
| Event-driven architecture | Event-driven architecture |
| Process orchestration and automation | Process orchestration, Business process modeling (BPMN, DMN) |
| Enterprise integration | Integration architecture |
| Multi-tenant SaaS architecture | Multi-tenant SaaS architecture |
| API design | API design |
| Software modeling | Software modeling (UML, SysML, C4) |
| Model-driven engineering | Model-driven engineering, Domain-specific language design |
| Java platform engineering | Java, Software engineering |
| Web application development | Frontend development (TypeScript, React) |
| Database design and operation | Database design, Database administration |
| Information security and compliance | Information security management, Data protection (GDPR) |
| Identity and access management | Identity and access management |
| Agile delivery | Agile delivery |

The 23 files are deleted; nothing keeps the old names. A profile claim that mapped to several
skills becomes one row per skill the CV evidences — the evidence decides, not the mapping.

---

## 5. The profile, the experiences, the ladder

- **Profile Skills table**: one row per skill the CV evidences, and no other. Expect 30–40
  rows against 60 files. The `<!-- levels drafted — review -->` marker returns above the table
  because every level is re-drafted; PR review removes it, as before.
- **The level rubric is not in the profile.** It lives in §6 and the PR body; the table carries
  only the claims.
- **Experiences** re-point `skills:` at the new H1s. An entry lists a skill only where its own
  bullets evidence it — the rule from the first build, unchanged. Every entry keeps at least
  what it had, mapped.
- **The ladder** keeps its four rungs and their `## What it means`; each rung's file gains one
  sentence naming the SFIA levels of responsibility it spans, so a claim here can be read
  against a SFIA profile elsewhere: Familiar spans levels 1–2 (follow, assist), Competent 3
  (apply), Proficient 4–5 (enable, ensure and advise), Expert 6–7 (initiate and influence,
  set strategy). The sentence names the levels; it does not reproduce SFIA's level text.

---

## 6. Levels: the rubric for this profile

Written down because the first build's reviewer found two rows contradicting the rubric the
implementer had in their head.

- **Expert** — owned the skill across two or more roles or projects, and the CV shows an
  outcome others depended on (a platform in production, an organization scaled, a standard
  set).
- **Proficient** — hands-on across two or more roles or projects, or one role with an
  outcome the CV quantifies.
- **Competent** — one role or project evidences it.
- **Familiar** — named in the CV's skills list with no role evidencing it. Such a row is
  normally *omitted* rather than claimed at Familiar; the table is for claims with evidence.

The owner overrides any row in the review PR. The rubric makes the draft consistent; it does
not make it right.

---

## 7. Order of work and verification

1. `skills/README.md` becomes the index: `Skill | Group | SFIA | ESCO`, generated from the
   appendix, so the folder is self-describing and the build is checkable against it.
2. Write the 60 skill files from the comparison's third table, §3 form, no redrafting.
3. Delete the 23 old files. Rewrite the profile's Skills table (§5, §6). Re-point every
   experience's `skills:`. Add the ladder sentences.
4. Checks, throwaway, from the shell: 60 files; every H1 unique and equal to its README index
   row; every `group` one of the nine; every file has a `Reference:` line in the fixed form;
   no SFIA code cited twice; no file under `skills/` contains a profile's name, an employer, or
   a four-digit year (the person-neutral rule, mechanically); no `In practice` sentence starts
   with "Someone", "They" or "Practitioners"; no definition starts with "The practice", "The
   discipline" or "The ability"; every profile row and every experience `skills:` entry
   resolves; ESCO URIs are `http://data.europa.eu/esco/skill/<uuid>`.
5. Run `companygraph-validate`. Run `companygraph-export` and confirm counts.
6. One PR, `skills-curated`, for the owner's review — levels are theirs to dispute.

---

## 8. Findings for the meta-model

Recorded here; proposed to the meta-model as its own spec (a section per schema stating its
purpose and the rules for writing an entity of that type). Nothing in core changes from this
repository.

- **Core, `skill-schema.md`** — `## In practice` is described as "what someone using this skill
  actually does", which every first-cut file read as *what this person did*. A skill many
  profiles claim must be person-neutral, and the schema should say so and say where the
  person's evidence lives instead (the profile's Skills table). The rules that make a
  neutral text — imperative without a subject, definition starting with the thing itself,
  products in a closing clause — are writing rules, and the schema has nowhere to put them.
- **Core, every schema** — the same gap generally: a schema says the *shape* (fields,
  sections) and nothing about the *purpose* of the type or *how to write* one. The first
  instance shows that shape alone does not produce usable entities.
- **Core, `skill-schema.md`** — a skill wants a reference to an external vocabulary (a SFIA
  code, an ESCO URI). Carried as a fixed-form prose line here; the schema's `group` question
  and this one are the same question — what a skill is anchored to.
- **Core, `proficiency-level-schema.md`** — a rung wants to say which levels of an external
  ladder it spans, for the same reason.
- **Core, the type set** — products (PostgreSQL, Camunda, Claude Code) are not skills and have
  no type; they are prose in `Typical tools:` here. Whether they become a type is a pack
  question.
- **Meta-model, `example/`** — its three skills are written the first-cut way. It is the
  example adopters copy; it will need the same rewrite when core says so.
