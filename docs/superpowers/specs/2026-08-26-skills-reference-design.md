# Skills on a reference vocabulary — design

> The skills of this instance re-cut against SFIA 9, every skill written so that many profiles
> can claim it, with the SFIA and ESCO references carried as prose until core learns a field
> for them.

Status: design agreed, nothing built. Instance-owned: nothing here changes `meta/` or the
meta-model. The core findings this produces are listed in §8 and go to the meta-model's
reference-instance spec §7 as one later PR.

---

## 1. What the first cut got wrong

The first 23 skills were cut from the CV's tag cloud by feel, and every `## In practice` was
written as what one person did with the skill. Two defects, one cause:

- **A skill is shared.** Many profiles claim the same skill, each with its own level and
  evidence; the schema already puts that claim in the profile's Skills table. A skill file that
  narrates one person's history is the profile's row restated — and wrong the moment a second
  profile claims it. `## In practice` must be person-neutral.
- **The grain was arbitrary.** "Database design and operation" is two skills to anyone who has
  hired for either; "Cloud platform engineering" is design and operation folded together. With
  no reference vocabulary there was nothing to check a cut against.

Both are core findings (§8). The instance fixes them by adopting a vocabulary.

---

## 2. The vocabulary: SFIA 9, all of it

[SFIA 9](https://sfia-online.org/en/sfia-9/sfia-9) — 147 skills in 6 categories and 19
subcategories, each defined at some of 7 levels of responsibility. Chosen over ESCO, O*NET and
Lightcast because it is the one built for exactly this grain: professional capability in
technology work, split where practitioners split it (`DBDS` design / `DBAD` administration),
and its own skill-versus-level split is the distinction this model already draws between
`skill` and `proficiency-level`.

**All 147, not the ones one person claims.** A reference vocabulary that is only the subset one
CV happened to touch is not a reference; the next profile would start cutting again. An
unclaimed skill file is a definition waiting for a claimant, and costs nothing.

**In our own words.** SFIA's names and codes are facts and are cited; its descriptions and
level texts are copyright of the SFIA Foundation and are never reproduced. Every definition
and every `## In practice` here is written for this repository. The owner registers the free
SFIA user licence on sfia-online.org so that citing the framework in a public repository is
inside its terms on their side too.

**ESCO as the second anchor.** Where [ESCO v1.2](https://esco.ec.europa.eu/en/classification/skill_main)
has a concept that means the same thing, its URI is cited beside the SFIA code — free for any
reuse, stable URIs, and a German label for later. ESCO's grain is generic ("design database
scheme", "operate relational database management system") and it has nothing for
domain-driven design or model-driven engineering; it anchors, it does not decide.

---

## 3. The skill file

Unchanged schema (`meta/skill-schema.md`): `source`, optional `group`, H1, `>` definition,
optional `## In practice`. Every file here has all of them. The rules this spec adds:

```markdown
---
source: Local
group: Development and implementation · Data and analytics
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

- **H1 is the SFIA skill name**, spelled as SFIA spells it, British spelling included
  (`Data modelling and design`) — it is a proper name, and R2 makes the H1 the thing every
  claim references. House style applies to everything else in the file.
- **`group` is `<Category> · <Subcategory>`** from the SFIA framework view, verbatim. Ten CV
  groups become nineteen SFIA subcategories; the schema's open question about groups gets
  147 data points on a published taxonomy.
- **`> definition`** — one line, ours, saying what the skill is. It starts with the thing
  itself, never with a wrapper — no "The practice of", "The discipline of", "The ability to".
  Not SFIA's overall description paraphrased; written from what the skill means to someone
  who has done it.
- **`## In practice`** — two to four sentences in the **imperative, without a subject**: each
  sentence starts with the bare verb — "Assess …", "Translate …", "Engage …" — never "Someone
  doing this …" or "They …". Person-neutral: no name, employer, date or number from any
  profile. Products appear only in a closing `Typical tools:` clause, and only where a product
  is what the skill is done with. A reader who wants to know who claims the skill reads the
  profiles.
- **The reference line is fixed in form**, last in the section, one line:
  `Reference: SFIA 9 <CODE> — <SFIA name>` then ` · ESCO <preferred label> <URI>` when ESCO has
  a match, else ` · ESCO none`. The form is what makes the line grep-able and, later,
  promotable to schema fields without re-reading prose. The CODE in the line must equal the
  code the H1 was taken from.

Filename: kebab-case of the H1, as R2 and the existing files already do
(`database-design.md`, `artificial-intelligence-ai-and-data-ethics.md`).

---

## 4. Instance skills that SFIA does not cover

Some of what the CV evidences has no SFIA skill: it is a method or an architecture style,
below SFIA's grain. Those stay as instance-defined skills, same file shape, with the reference
line reading `Reference: SFIA 9 none` and ESCO where it has one, and `group` set to the SFIA
subcategory they would sit under, so they sort with their neighbours:

| instance skill | group | why not a SFIA skill |
| --- | --- | --- |
| Domain-driven design | Development and implementation · Systems development | a design method inside `SWDN` |
| Event-driven architecture | Development and implementation · Systems development | an architecture style inside `ARCH`/`DESN` |
| Model-driven engineering | Development and implementation · Systems development | a method spanning `SWDN`, `PROG`, `METL` |
| Process orchestration | Development and implementation · Systems development | executable BPMN/DMN — narrower than `BPRE` |
| API design | Development and implementation · Systems development | the contract half of `SWDN`/`SINT` |
| Multi-tenant SaaS architecture | Development and implementation · Systems development | a concern inside `ARCH` |
| Agentic AI development | Development and implementation · Systems development | building with and for agents; SFIA 9 has `MLNG` and `AIDE`, neither is this |

The rule for adding one: a capability the profile claims with evidence, that no SFIA skill
names, and that a second profile could plausibly claim. Seven now; the list is reviewed
whenever SFIA releases.

---

## 5. What moves where — the 23 existing skills

| today | becomes |
| --- | --- |
| Scaling engineering organizations | `OCDV` Organisational capability development, `WFPL` Workforce planning |
| Technology strategy and governance | `ITSP` Strategic planning, `GOVN` Governance |
| AI strategy and governance | `ITSP` Strategic planning (claim), `AIDE` Artificial intelligence (AI) and data ethics |
| Stakeholder and vendor management | `RLMT` Stakeholder relationship management, `SUPP` Supplier management |
| Agentic AI development | instance skill, unchanged name |
| Cloud platform engineering | `IFDN` Infrastructure design, `ITOP` Infrastructure operations |
| Infrastructure as code and delivery automation | `DEPL` Deployment, `RELM` Release management, `CFMG` Configuration management |
| Enterprise architecture | `STPL` Enterprise and business architecture |
| Business architecture | `STPL` (same skill; the claim's evidence names the L0/L1 work), `BSMO` Business modelling |
| Domain-driven design | instance skill |
| Event-driven architecture | instance skill |
| Process orchestration and automation | instance skill `Process orchestration`, plus `BPRE` where the evidence is process improvement |
| Enterprise integration | `SINT` Systems integration and build |
| Multi-tenant SaaS architecture | instance skill |
| API design | instance skill |
| Software modeling | `DTAN` Data modelling and design, `BSMO` Business modelling, `DESN` Systems design |
| Model-driven engineering | instance skill |
| Java platform engineering | `PROG` Programming/software development |
| Web application development | `PROG` (the claim's evidence names the frontend work) |
| Database design and operation | `DBDS` Database design, `DBAD` Database administration |
| Information security and compliance | `SCTY` Information security, `PEDP` Information and data compliance |
| Identity and access management | `IAMT` Identity and access management |
| Agile delivery | `DEMG` Delivery management, `METL` Methods and tools |

The 23 files are deleted; nothing keeps the old names. A profile claim that mapped to two
SFIA skills becomes two rows, each with the evidence that fits it, or one row if the CV
evidences only one half — the evidence decides, not the mapping.

---

## 6. The profile, the experiences, the ladder

- **Profile Skills table**: one row per skill the CV evidences, and no other. Expect 25–35
  rows against 154 files. The `<!-- levels drafted — review -->` marker returns above the
  table because every level is re-drafted; PR review removes it, as before.
- **The level rubric is not in the profile.** It lives in this spec (§7) and the PR body; the
  table carries only the claims.
- **Experiences** re-point `skills:` at the new H1s. An entry lists a skill only where its own
  bullets evidence it — the rule from the first build, unchanged. Every entry keeps at least
  what it had, mapped.
- **The ladder** keeps its four rungs and their `## What it means`; each rung's file gains one
  sentence naming the SFIA levels of responsibility it spans, so a claim here can be read
  against a SFIA profile elsewhere: Familiar spans levels 1–2 (follow, assist), Competent 3
  (apply), Proficient 4–5 (enable, ensure and advise), Expert 6–7 (initiate and influence,
  set strategy). The sentence names the levels; it does not reproduce SFIA's level text.

---

## 7. Levels: the rubric for this profile

Written down because the first build's reviewer found two rows contradicting the rubric the
implementer had in their head.

- **Expert** — owned the skill across two or more roles or projects, and the CV shows an
  outcome others depended on (a platform in production, an organisation scaled, a standard
  set).
- **Proficient** — hands-on across two or more roles or projects, or one role with an
  outcome the CV quantifies.
- **Competent** — one role or project evidences it.
- **Familiar** — named in the CV's skills list with no role evidencing it. Such a row is
  normally *omitted* rather than claimed at Familiar; the table is for claims with evidence.

The owner overrides any row in the review PR. The rubric makes the draft consistent; it does
not make it right.

---

## 8. Findings for the meta-model (deferred, recorded here)

To be carried into the meta-model's reference-instance spec §7 later, in one PR:

- **Core, `skill-schema.md`** — `## In practice` is described as "what someone using this skill
  actually does", which every first-cut file read as *what this person did*. A skill many
  profiles claim must be person-neutral; the schema should say so, and say where the person's
  evidence lives instead (the profile's Skills table).
- **Core, `skill-schema.md`** — a skill wants a reference to an external vocabulary (a SFIA
  code, an ESCO URI). Carried as a fixed-form prose line here; the schema's `group` question
  and this one are the same question — what a skill is anchored to — and should be answered
  together.
- **Core, `proficiency-level-schema.md`** — a rung wants to say which levels of an external
  ladder it spans, for the same reason.
- **Core, the type set** — products (PostgreSQL, Camunda, Claude Code) are not skills and have
  no type; they are prose in `Typical tools:` here. Whether they become a type is a pack
  question.
- **Meta-model, `example/`** — its three skills are written the first-cut way (Java
  Programming's In practice names "the person who reads the stack trace"). It is the example
  adopters copy; it will need the same rewrite when core says so.

---

## 9. Order of work and verification

1. Owner registers the free SFIA user licence (outside this repository).
2. The appendix below is the list. It is written into `skills/README.md` as an index table —
   `Code | Skill | Group` — so the folder is self-describing and the build
   is checkable against it.
3. Write the 147 SFIA skill files and the 7 instance skill files, §3 form. ESCO matched per
   skill through the ESCO search API at build time; `none` where nothing means the same thing.
4. Delete the 23 old files. Rewrite the profile's Skills table (§6, §7). Re-point every
   experience's `skills:`. Add the ladder sentences.
5. Checks, throwaway, from the shell: 154 files; every H1 unique and equal to its README index
   row; every `group` one of the 19 `Category · Subcategory` strings; every file has a
   `Reference:` line in the fixed form whose CODE matches the index (or `none` for the seven);
   no reference line's CODE appears twice; no file under `skills/` contains a profile's name,
   an employer, or a four-digit year (the person-neutral rule, mechanically); every profile
   row and every experience `skills:` entry resolves; ESCO URIs are `http://data.europa.eu/esco/skill/<uuid>`.
6. Run `companygraph-validate`. Run `companygraph-export` and confirm counts.
7. One PR, `skills-on-sfia`, for the owner's review — levels and definitions are theirs to
   dispute.

---

## Appendix — the 147 SFIA 9 skills, as they will be filed

One file each, H1 = the name below, `group` = `<Category> · <Subcategory>`. Source: the SFIA 9
A–Z and the full framework view, cross-checked code for code. The seven instance skills of §4
are not in this table.


**Strategy and architecture · Strategy and planning**

| Code | Skill |
| --- | --- |
| `ITSP` | Strategic planning |
| `ISCO` | Information systems coordination |
| `IRMG` | Information management |
| `STPL` | Enterprise and business architecture |
| `ARCH` | Solution architecture |
| `INOV` | Innovation management |
| `EMRG` | Emerging technology monitoring |
| `RSCH` | Formal research |
| `SUST` | Sustainability |

**Strategy and architecture · Financial and value management**

| Code | Skill |
| --- | --- |
| `FMIT` | Financial management |
| `INVA` | Investment appraisal |
| `BENM` | Benefits management |
| `BUDF` | Budgeting and forecasting |
| `FIAN` | Financial analysis |
| `COMG` | Cost management |
| `DEMM` | Demand management |
| `MEAS` | Measurement |

**Strategy and architecture · Security and privacy**

| Code | Skill |
| --- | --- |
| `SCTY` | Information security |
| `INAS` | Information assurance |
| `PEDP` | Information and data compliance |
| `VURE` | Vulnerability research |
| `THIN` | Threat intelligence |

**Strategy and architecture · Governance, risk and compliance**

| Code | Skill |
| --- | --- |
| `GOVN` | Governance |
| `BURM` | Risk management |
| `AIDE` | Artificial intelligence (AI) and data ethics |
| `AUDT` | Audit |
| `QUMG` | Quality management |
| `QUAS` | Quality assurance |

**Strategy and architecture · Advice and guidance**

| Code | Skill |
| --- | --- |
| `CNSL` | Consultancy |
| `TECH` | Specialist advice |
| `METL` | Methods and tools |

**Change and transformation · Change implementation**

| Code | Skill |
| --- | --- |
| `POMG` | Portfolio management |
| `PGMG` | Programme management |
| `PRMG` | Project management |
| `PROF` | Portfolio, programme and project support |
| `DEMG` | Delivery management |

**Change and transformation · Change analysis**

| Code | Skill |
| --- | --- |
| `BUSA` | Business situation analysis |
| `FEAS` | Feasibility assessment |
| `REQM` | Requirements definition and management |
| `BSMO` | Business modelling |
| `BPTS` | User acceptance testing |

**Change and transformation · Change planning**

| Code | Skill |
| --- | --- |
| `BPRE` | Business process improvement |
| `OCDV` | Organisational capability development |
| `ORDI` | Organisation design and implementation |
| `CIPM` | Organisational change management |
| `JADN` | Job analysis and design |
| `OCEN` | Organisational change enablement |

**Development and implementation · Systems development**

| Code | Skill |
| --- | --- |
| `PROD` | Product management |
| `DLMG` | Systems development management |
| `SLEN` | Systems and software lifecycle engineering |
| `DESN` | Systems design |
| `SWDN` | Software design |
| `NTDS` | Network design |
| `IFDN` | Infrastructure design |
| `HWDE` | Hardware design |
| `PROG` | Programming/software development |
| `SINT` | Systems integration and build |
| `TEST` | Functional testing |
| `NFTS` | Non-functional testing |
| `PRTS` | Process testing |
| `PORT` | Software configuration |
| `RESD` | Real-time/embedded systems development |
| `SFEN` | Safety engineering |
| `SFAS` | Safety assessment |
| `RFEN` | Radio frequency engineering |
| `ADEV` | Animation development |

**Development and implementation · Data and analytics**

| Code | Skill |
| --- | --- |
| `DATM` | Data management |
| `DTAN` | Data modelling and design |
| `DBDS` | Database design |
| `DAAN` | Data analytics |
| `DATS` | Data science |
| `MLNG` | Machine learning |
| `BINT` | Business intelligence |
| `DENG` | Data engineering |
| `VISL` | Data visualisation |

**Development and implementation · User centred design**

| Code | Skill |
| --- | --- |
| `URCH` | User research |
| `CEXP` | Customer experience |
| `ACIN` | Accessibility and inclusion |
| `UNAN` | User experience analysis |
| `HCEV` | User experience design |
| `USEV` | User experience evaluation |

**Development and implementation · Content management**

| Code | Skill |
| --- | --- |
| `INCA` | Content design and authoring |
| `ICPM` | Content publishing |
| `KNOW` | Knowledge management |
| `GRDN` | Graphic design |

**Development and implementation · Computational science**

| Code | Skill |
| --- | --- |
| `SCMO` | Scientific modelling |
| `NUAN` | Numerical analysis |
| `HPCC` | High-performance computing |

**Delivery and operation · Technology management**

| Code | Skill |
| --- | --- |
| `ITMG` | Technology service management |
| `ASUP` | Application support |
| `ITOP` | Infrastructure operations |
| `SYSP` | System software administration |
| `NTAS` | Network support |
| `HSIN` | Systems installation and removal |
| `CFMG` | Configuration management |
| `RELM` | Release management |
| `DEPL` | Deployment |
| `STMG` | Storage management |
| `DCMA` | Facilities management |

**Delivery and operation · Service management**

| Code | Skill |
| --- | --- |
| `SLMO` | Service level management |
| `SCMG` | Service catalogue management |
| `AVMT` | Availability management |
| `COPL` | Continuity management |
| `CPMG` | Capacity management |
| `USUP` | Incident management |
| `PBMG` | Problem management |
| `CHMG` | Change control |
| `ASMG` | Asset management |
| `SEAC` | Service acceptance |

**Delivery and operation · Security services**

| Code | Skill |
| --- | --- |
| `IAMT` | Identity and access management |
| `SCAD` | Security operations |
| `VUAS` | Vulnerability assessment |
| `DGFS` | Digital forensics |
| `CRIM` | Cybercrime investigation |
| `OCOP` | Offensive cyber operations |
| `PENT` | Penetration testing |

**Delivery and operation · Data and records operations**

| Code | Skill |
| --- | --- |
| `RMGT` | Records management |
| `ANCC` | Analytical classification and coding |
| `DBAD` | Database administration |

**People and skills · People management**

| Code | Skill |
| --- | --- |
| `PEMT` | Performance management |
| `EEXP` | Employee experience |
| `OFCL` | Organisational facilitation |
| `PDSV` | Professional development |
| `WFPL` | Workforce planning |
| `RESC` | Resourcing |

**People and skills · Skills management**

| Code | Skill |
| --- | --- |
| `ETMG` | Learning and development management |
| `TMCR` | Learning design and development |
| `ETDL` | Learning delivery |
| `LEDA` | Competency assessment |
| `CSOP` | Certification scheme operation |
| `TEAC` | Teaching |
| `SUBF` | Subject formation |

**Relationships and engagement · Stakeholder management**

| Code | Skill |
| --- | --- |
| `SORC` | Sourcing |
| `SUPP` | Supplier management |
| `ITCM` | Contract management |
| `RLMT` | Stakeholder relationship management |
| `CSMG` | Customer service support |
| `ADMN` | Business administration |

**Relationships and engagement · Sales and bid management**

| Code | Skill |
| --- | --- |
| `BIDM` | Bid/proposal management |
| `SALE` | Selling |
| `SSUP` | Sales support |

**Relationships and engagement · Marketing**

| Code | Skill |
| --- | --- |
| `MKTG` | Marketing management |
| `MRCH` | Market research |
| `BRMG` | Brand management |
| `CELO` | Customer engagement and loyalty |
| `MKCM` | Marketing campaign management |
| `DIGM` | Digital marketing |
