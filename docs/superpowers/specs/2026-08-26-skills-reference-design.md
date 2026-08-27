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

---

## Appendix — the 60 curated skills

One file each, H1 = the name below; texts as in the comparison's third table.


**Leadership and strategy**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| IT strategy | none | [define technology strategy](http://data.europa.eu/esco/skill/248894d1-42dc-474f-af6e-2da52ac0c679) |
| IT governance | GOVN — Governance | none |
| AI strategy | none | none |
| AI governance | none | none |
| Engineering leadership | none | none |
| Stakeholder management | RLMT — Stakeholder relationship management | [maintain relationships with stakeholders](http://data.europa.eu/esco/skill/999286f1-22d9-4950-9422-89bd45265a5f) |
| Vendor management | SUPP — Supplier management | [maintain relationship with suppliers](http://data.europa.eu/esco/skill/3cd35f5d-ce6d-4f14-9a09-53d7a28d834c) |
| Product management | PROD — Product management | [plan product management](http://data.europa.eu/esco/skill/29fb886c-6be0-4e93-9ea1-232881f2092a) |
| Agile delivery | DEMG — Delivery management | [Agile project management](http://data.europa.eu/esco/skill/0a9acb6b-1139-4be9-b431-3a80a959f2f4) |
| Programme management | none | none |
| Change management | CIPM — Organisational change management | [apply change management](http://data.europa.eu/esco/skill/3c03ee71-4a23-448f-b79e-81fd75d27dca) |

**Architecture**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Enterprise architecture | STPL — Enterprise and business architecture | [design enterprise architecture](http://data.europa.eu/esco/skill/ee3c1d54-f46a-43c7-a0f9-0ba3648164d0) |
| Business architecture | STPL — Enterprise and business architecture | none |
| Solution architecture | ARCH — Solution architecture | none |
| Software architecture | SWDN — Software design | [create software design](http://data.europa.eu/esco/skill/3bddfd7c-ab6d-40c2-883d-5e97fb7640ba) |
| Domain-driven design | none | none |
| Event-driven architecture | none | none |
| Microservices architecture | none | none |
| API design | none | [design application interfaces](http://data.europa.eu/esco/skill/b0096dc5-2e2d-4bc1-8172-05bf486c3968) |
| Integration architecture | none | [ICT system integration](http://data.europa.eu/esco/skill/6fa1c2c0-a012-4ca0-9642-e01569ba322c) |
| Multi-tenant SaaS architecture | none | [SaaS (service-oriented modelling)](http://data.europa.eu/esco/skill/eeca3780-8049-499f-a268-95a7ad26642c) |
| Requirements engineering | REQM — Requirements definition and management | none |

**AI**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Agentic AI development | none | none |
| LLM application development | none | none |
| Retrieval-augmented generation | none | none |
| AI tool integration (MCP) | none | none |
| Machine learning | MLNG — Machine learning | [utilise machine learning](http://data.europa.eu/esco/skill/8369c2d6-c100-4cf6-bd83-9668d8678433) |
| MLOps | none | none |
| Responsible AI | AIDE — Artificial intelligence (AI) and data ethics | none |

**Cloud and platform**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Cloud architecture | none | none |
| Container orchestration (Kubernetes) | none | none |
| Infrastructure as code | none | none |
| CI/CD | DEPL — Deployment | none |
| DevOps | none | [DevOps](http://data.europa.eu/esco/skill/f0de4973-0a70-4644-8fd4-3a97080476f4) |
| Site reliability engineering | none | none |
| Observability | none | [monitor system performance](http://data.europa.eu/esco/skill/9190d87f-9792-42e0-bb7f-64294a656bcd) |
| Platform engineering | none | none |
| Incident management | USUP — Incident management | [manage major incidents](http://data.europa.eu/esco/skill/8071881c-d652-46e7-9cf4-e06a7f1e57c7) |
| FinOps | COMG — Cost management | none |

**Data**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Database design | DBDS — Database design | [design database scheme](http://data.europa.eu/esco/skill/6c08403c-a5bb-4868-b8c2-b7d039c0e511) |
| Database administration | DBAD — Database administration | [operate relational database management system](http://data.europa.eu/esco/skill/7369f779-4b71-4aab-8836-48b69c676eec) |
| Data modeling | DTAN — Data modelling and design | [create data models](http://data.europa.eu/esco/skill/fbafa41f-cd05-4109-a649-8b44d306d779) |
| Data engineering | DENG — Data engineering | [develop data processing applications](http://data.europa.eu/esco/skill/f9670490-8aa4-4540-b121-d440a8294aab) |
| Event streaming | none | none |
| Data governance | DATM — Data management | none |

**Software development**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Software engineering | PROG — Programming/software development | [ICT system programming](http://data.europa.eu/esco/skill/b105ec9b-0857-41d6-8d07-a83e58b73d90) |
| Java | none | [Java (computer programming)](http://data.europa.eu/esco/skill/19a8293b-8e95-4de3-983f-77484079c389) |
| Frontend development (TypeScript, React) | none | [TypeScript](http://data.europa.eu/esco/skill/867137fb-ff1b-4ca3-99f3-cb6969aa2c68) |
| Software testing | none | [levels of software testing](http://data.europa.eu/esco/skill/85f46538-ae70-498a-bfbc-b8ddafe96c7d) |

**Modeling and process**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Software modeling (UML, SysML, C4) | none | [unified modelling language](http://data.europa.eu/esco/skill/7193cb6d-8334-494f-86e5-21e6d03a47c3) |
| Business process modeling (BPMN, DMN) | BSMO — Business modelling | [business process modelling](http://data.europa.eu/esco/skill/98301d4a-2cc3-439d-8d7f-0b6ac76302bb) |
| Process orchestration | none | none |
| Model-driven engineering | none | none |
| Domain-specific language design | none | none |

**Security and compliance**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Information security management | SCTY — Information security | [information security strategy](http://data.europa.eu/esco/skill/11eebd42-44ab-401d-8a2c-bdb9fc9beb50) |
| Data protection (GDPR) | PEDP — Information and data compliance | [data protection](http://data.europa.eu/esco/skill/a4346013-a967-4a58-a533-6b32ad1364c5) |
| Identity and access management | IAMT — Identity and access management | [maintain ICT identity management](http://data.europa.eu/esco/skill/ab49f767-296b-47d5-af56-0b4a69515b03) |
| Application security | none | [web application security threats](http://data.europa.eu/esco/skill/902fb91c-3113-4004-9b4f-79aa86b638b7) |

**Advisory**

| Skill | SFIA 9 | ESCO |
| --- | --- | --- |
| Knowledge management | KNOW — Knowledge management | [manage business knowledge](http://data.europa.eu/esco/skill/41bf7ede-fc84-4a57-8c89-b548d11b0ba1) |
| Consulting | CNSL — Consultancy | [use consulting techniques](http://data.europa.eu/esco/skill/414332e4-8347-4771-b947-65bd3801a620) |
