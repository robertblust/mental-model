# Curated Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the instance's 23 first-cut skills with the 60 curated skills, texts exactly as reviewed, and re-point the profile and the experiences at them.

**Architecture:** Markdown only. The 60 skill files are generated from two committed sources — the reviewed texts in the comparison document's third table and the group per skill in the spec's appendix — by a throwaway script run from the shell and never committed. The profile's Skills table is re-cut by hand against the CV; the experiences' `skills:` lists are re-pointed by the spec's §4 mapping and each entry's own bullets. Validation is the agent pass.

**Tech Stack:** Markdown, YAML frontmatter, git, `gh`; Python 3 from the shell for the throwaway generator and checks. No code in the repository.

**Spec:** `docs/superpowers/specs/2026-08-26-skills-reference-design.md` — read it first; §3 is the file form, §4 the mapping, §5–§6 the profile rules. Texts: `docs/superpowers/research/2026-08-26-skill-sources-compared.md`, section "Curated skills — drafted definition and In practice".

## Global Constraints

- Work on branch `skills-curated`, created from `skills-reference-spec` (the branch of PR #2, which carries the spec and this plan). Push the branch; open one PR at the end; merge nothing.
- `git config user.email` must print `robert.blust@flatland.ch`. Every commit message ends with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
- `meta/` is vendored and never touched. No file under `.companygraph/` changes.
- Skill file form (spec §3): `source: Local`; `group:` one of exactly nine strings — `Leadership and strategy`, `Architecture`, `AI`, `Cloud and platform`, `Data`, `Software development`, `Modeling and process`, `Security and compliance`, `Advisory`; H1 = the curated name; `> ` definition; `## In practice`. No `Reference:` line; no SFIA or ESCO mention anywhere under `skills/`.
- Texts are written **exactly as they stand in the comparison's third table** — no redrafting, no "improvements". A text that seems wrong is reported, not changed.
- Person-neutral: no file under `skills/` contains `Robert`, `LIKE MAGIC`, `3AP`, `UBS`, or a four-digit year. No `In practice` sentence starts with `Someone`, `They` or `Practitioners`. No definition starts with `The practice`, `The discipline` or `The ability`.
- Every reference resolves: every `Skill` cell in the profile table and every entry in an experience's `skills:` equals the H1 of a file in `skills/` character for character (R3, R4 in `meta/CONVENTIONS.md`).
- House style for prose written new in this plan (profile evidence cells): American English, no Oxford comma, past tense for what ended.
- Throwaway scripts and checks run from the shell are never committed. `dist/` is gitignored.

---

## File map

- Create: 60 files `skills/<kebab>.md`; rewrite `skills/README.md` (index `Skill | Group`)
- Delete: the 23 existing `skills/*.md` (everything except README.md)
- Modify: `profiles/robert-blust/robert-blust.md` (Skills table), `profiles/robert-blust/experiences/*.md` (`skills:` lines), `AGENTS.md` (one new section)

---

### Task 1: Generate the 60 skill files, replace the 23, index them

**Files:**
- Create: `skills/*.md` (60), `skills/README.md` (rewritten)
- Delete: `skills/*.md` (23 old)
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: the third table of `docs/superpowers/research/2026-08-26-skill-sources-compared.md` (rows `| **Name** | definition | in practice |`) and the appendix of the spec (group headers `**Group**` followed by `| Name |` rows).
- Produces: 60 H1s, listed in `skills/README.md`, that Tasks 2 and 3 reference verbatim.

- [ ] **Step 1: Branch**

```bash
cd ~/git/robertblust/mental-model && git fetch -q && git checkout skills-reference-spec && git pull -q && git checkout -b skills-curated
git config user.email    # robert.blust@flatland.ch
ls skills/*.md | grep -vc README   # 23
```

- [ ] **Step 2: Delete the 23 old files**

```bash
git rm -q $(ls skills/*.md | grep -v README.md)
ls skills   # README.md only
```

- [ ] **Step 3: Generate the 60 files and the index (throwaway script; do not commit it)**

```bash
python3 - <<'EOF'
import re,pathlib
spec=open('docs/superpowers/specs/2026-08-26-skills-reference-design.md').read()
cmp=open('docs/superpowers/research/2026-08-26-skill-sources-compared.md').read()
GROUPS=["Leadership and strategy","Architecture","AI","Cloud and platform","Data","Software development","Modeling and process","Security and compliance","Advisory"]
# groups from the appendix
app=spec.split("## Appendix")[1]; group={}; cur=None
for l in app.split("\n"):
    m=re.fullmatch(r"\*\*(.+)\*\*",l.strip())
    if m: cur=m.group(1); assert cur in GROUPS, cur; continue
    m=re.fullmatch(r"\| (.+?) \|",l.strip())
    if m and m.group(1) not in ("Skill","---"): group[m.group(1)]=cur
assert len(group)==60, len(group)
# texts from the third table
third=cmp.split("## Curated skills")[1]; texts={}
for l in third.split("\n"):
    if not l.startswith("| **"): continue
    c=[x.strip() for x in l.strip().strip("|").split("|")]
    name=c[0].strip("*"); texts[name]=(c[1],c[2])
assert set(texts)==set(group), set(texts)^set(group)
def kebab(h): return re.sub(r"[^a-z0-9]+","-",h.lower()).strip("-")
for name,(d,ip) in texts.items():
    # wrap In practice at ~95 columns without touching words
    words=ip.split(" "); lines=[]; cur=""
    for w in words:
        if len(cur)+len(w)+1>95: lines.append(cur); cur=w
        else: cur=(cur+" "+w).strip()
    lines.append(cur)
    body=f"---\nsource: Local\ngroup: {group[name]}\n---\n\n# {name}\n\n> {d}\n\n## In practice\n\n"+"\n".join(lines)+"\n"
    pathlib.Path(f"skills/{kebab(name)}.md").write_text(body)
idx=["# Skills","","One file per skill, written against `meta/skill-schema.md` and the rules in","`docs/superpowers/specs/2026-08-26-skills-reference-design.md` §3. Sixty skills, ours; nine groups.","","| Skill | Group |","| --- | --- |"]
for g in GROUPS:
    for name in [n for n in texts if group[n]==g]: idx.append(f"| {name} | {g} |")
pathlib.Path("skills/README.md").write_text("\n".join(idx)+"\n")
print(len(texts),"files written")
EOF
```

Expected: `60 files written`.

- [ ] **Step 4: Throwaway checks (do not commit)**

```bash
python3 - <<'EOF'
import re,glob
files=[f for f in glob.glob("skills/*.md") if not f.endswith("README.md")]
assert len(files)==60, len(files)
GROUPS={"Leadership and strategy","Architecture","AI","Cloud and platform","Data","Software development","Modeling and process","Security and compliance","Advisory"}
idx=open("skills/README.md").read(); h1s=set(); bad=[]
for f in files:
    s=open(f).read()
    m=re.search(r"^# (.+)$",s,re.M); h=m.group(1); h1s.add(h)
    fm=s.split("---")[1]
    if "source: Local" not in fm: bad.append((f,"source"))
    g=re.search(r"^group: (.+)$",fm,re.M); 
    if not g or g.group(1) not in GROUPS: bad.append((f,"group"))
    if not re.search(r"^> \S",s,re.M): bad.append((f,"definition"))
    if "## In practice" not in s: bad.append((f,"in practice"))
    if re.search(r"Reference:|SFIA|ESCO",s): bad.append((f,"reference"))
    if re.search(r"Robert|LIKE MAGIC|3AP|UBS|\b(19|20)\d\d\b",s): bad.append((f,"not neutral"))
    ip=s.split("## In practice")[1]
    if re.search(r"(^|\. )(Someone|They|Practitioners)\b",ip): bad.append((f,"subject"))
    d=re.search(r"^> (.+)$",s,re.M).group(1)
    if re.match(r"The (practice|discipline|ability)",d): bad.append((f,"wrapper"))
    k=re.sub(r"[^a-z0-9]+","-",h.lower()).strip("-")
    if f!=f"skills/{k}.md": bad.append((f,"filename"))
    if f"| {h} |" not in idx: bad.append((f,"not in index"))
assert len(h1s)==60, "duplicate H1"
print("problems:",bad or "none")
EOF
```

Expected: `problems: none`.

- [ ] **Step 5: AGENTS.md — the skill writing rules as instance rules**

Append to `AGENTS.md`, before the `## Sync slot` section:

```markdown
## Writing a skill

The rules are in `docs/superpowers/specs/2026-08-26-skills-reference-design.md` §3. In short:
the definition starts with the thing itself, never "The practice of"; `## In practice` is in
the imperative without a subject and names no person, employer, date or number; products
appear only in a closing `Typical tools:` clause. A skill is claimed in a profile's Skills
table — that is where one person's level and evidence live, never in the skill file.
```

- [ ] **Step 6: Commit**

```bash
git add -A skills AGENTS.md
git commit -m "$(cat <<'EOF'
Replace the 23 first-cut skills with the 60 curated ones

Texts exactly as reviewed in the comparison; nine groups; person-neutral,
imperative, no external vocabulary cited. The index in skills/README.md
lists them.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
EOF
)"
git push -u origin skills-curated
```

---

### Task 2: Re-cut the profile's Skills table

**Files:**
- Modify: `profiles/robert-blust/robert-blust.md` — the `## Skills` table only

**Interfaces:**
- Consumes: the 60 H1s (`grep -h '^# ' skills/*.md`), the four level H1s (`Familiar`, `Competent`, `Proficient`, `Expert`), the CV at `~/git/robertblust/rob-cv/content/` (profile.yaml, experience/, projects/, education/, community/).
- Produces: the set of claimed skills, which Task 3 must keep consistent with the experiences.

- [ ] **Step 1: Build the claim list from the spec's mapping, then from the CV**

Read spec §4 (the 23 → 60 mapping) and the current table (23 rows, each with evidence). For each old row, the new row(s) are the mapped skills whose half of the evidence the CV actually supports — e.g. "Cloud platform engineering" (evidence: owned the production platform on Google Cloud, IaC, CI/CD) yields `Cloud architecture` and `Platform engineering`, and `Container orchestration (Kubernetes)` only if the CV names GKE/Kubernetes for it (it does: `2022-likemagic.md`). Then read every CV file once more for skills in the 60 that no old row covered — `Site reliability engineering`, `Observability`, `Incident management` (the LIKE MAGIC role names SRE, incident management), `Event streaming` (Pub/Sub, Kafka), `Requirements engineering`, `Consulting` (3AP), `Knowledge management` (the LIKE MAGIC Mental Model). Add a row only where one CV fact evidences it.

- [ ] **Step 2: Write the table**

Replace the `## Skills` section's table (keep the `<!-- levels drafted — review -->` line above it):

```markdown
| Skill | Level | Evidence |
| --- | --- | --- |
| Engineering leadership | Expert | Grew LIKE MAGIC engineering from 5 to 25 and 3AP to about 70 people. |
| IT strategy | Expert | Defined and executed LIKE MAGIC's product and platform strategy across 12 business domains. |
| … one row per claimed skill, 30–40 rows … |
```

Levels by the spec's §6 rubric, verbatim: Expert — two or more roles/projects and an outcome others depended on; Proficient — two or more roles/projects hands-on, or one role with a quantified outcome; Competent — one role or project; Familiar — omitted. Evidence: one concrete CV fact — a number, a system, a named outcome — American English, no Oxford comma, past tense.

- [ ] **Step 3: Throwaway check**

```bash
p=profiles/robert-blust/robert-blust.md
python3 - <<'EOF'
import re,glob
h1={re.search(r"^# (.+)$",open(f).read(),re.M).group(1) for f in glob.glob("skills/*.md") if "README" not in f}
lv={re.search(r"^# (.+)$",open(f).read(),re.M).group(1) for f in glob.glob("proficiency-levels/*.md") if "README" not in f}
s=open("profiles/robert-blust/robert-blust.md").read()
tab=s.split("## Skills")[1].split("## Summary")[0]
rows=[l for l in tab.split("\n") if l.startswith("| ") and not l.startswith("| Skill") and not l.startswith("| ---")]
bad=[]
for r in rows:
    c=[x.strip() for x in r.strip().strip("|").split("|")]
    if len(c)!=3: bad.append(("cells",r)); continue
    if c[0] not in h1: bad.append(("skill",c[0]))
    if c[1] not in lv: bad.append(("level",c[1]))
    if not c[2] or c[2].endswith(", and") or re.search(r", and ",c[2]): bad.append(("evidence",c[0]))
    if c[1]=="Familiar": bad.append(("familiar row",c[0]))
print(len(rows),"rows; problems:",bad or "none"); assert "<!-- levels drafted — review -->" in s
EOF
```

Expected: between 30 and 40 rows; `problems: none`.

- [ ] **Step 4: Commit**

```bash
git add profiles/robert-blust/robert-blust.md
git commit -m "$(cat <<'EOF'
Re-cut the profile's claims onto the curated skills

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Re-point the experiences

**Files:**
- Modify: `profiles/robert-blust/experiences/*.md` — the `skills:` line of each (20 files)

**Interfaces:**
- Consumes: the 60 H1s, spec §4 mapping, the profile's claimed set (Task 2).
- Produces: every claimed skill evidenced by at least one experience.

- [ ] **Step 1: Re-point by mapping, then by bullets**

For each experience file: replace every old name in `skills:` by its §4 successor(s), then read the file's own `## Achievements` and keep only the successors its bullets evidence; add any of the 60 its bullets evidence that the mapping did not produce (the same SRE / Observability / Incident management / Event streaming / Consulting / Knowledge management candidates as Task 2). Keep the flow-list form `skills: [A, B, C]`. A file with no `skills:` line (three of them) gets one only if its bullets evidence a skill.

- [ ] **Step 2: Throwaway checks**

```bash
python3 - <<'EOF'
import re,glob
h1={re.search(r"^# (.+)$",open(f).read(),re.M).group(1) for f in glob.glob("skills/*.md") if "README" not in f}
s=open("profiles/robert-blust/robert-blust.md").read().split("## Skills")[1].split("## Summary")[0]
claimed={l.strip().strip("|").split("|")[0].strip() for l in s.split("\n") if l.startswith("| ") and not l.startswith("| Skill") and not l.startswith("| ---")}
used=set(); bad=[]
for f in sorted(glob.glob("profiles/robert-blust/experiences/*.md")):
    t=open(f).read(); m=re.search(r"^skills: \[(.*)\]$",t,re.M)
    if not m: continue
    for e in [x.strip() for x in m.group(1).split(",") if x.strip()]:
        if e not in h1: bad.append((f,e))
        used.add(e)
print("unresolved:",bad or "none")
print("claimed but evidenced by no experience:",sorted(claimed-used) or "none")
print("evidenced but not claimed:",sorted(used-claimed) or "none")
EOF
```

Expected: `unresolved: none`; `claimed but evidenced by no experience: none`. "Evidenced but not claimed" may list skills — for each, either add a profile row (Task 2's rules) or drop it from the experience; report which.

- [ ] **Step 3: Commit**

```bash
git add profiles/robert-blust/experiences
git commit -m "$(cat <<'EOF'
Re-point every experience at the curated skills it evidences

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
EOF
)"
git push
```

---

### Task 4: Validate, export, and the review PR

**Files:**
- Modify: whatever validate reports (content only, never `meta/`)

**Interfaces:**
- Consumes: everything above.

- [ ] **Step 1: Run the validate skill**

Read `.claude/skills/companygraph-validate/SKILL.md` and carry out its procedure literally over the whole instance. Fix every `✗` in content, one commit per fix (`Fix: <rule> — <what>`), until the report has no `✗`. Record the full report and the **Not checked** block.

- [ ] **Step 2: Run the export skill and check counts**

Read `.claude/skills/companygraph-export/SKILL.md`, carry it out, then:

```bash
unzip -l dist/mental-model-skill.zip | tail -3
for d in sources proficiency-levels skills values; do echo "$d $(ls $d/*.md | grep -vc README)"; done
echo "experiences $(ls profiles/robert-blust/experiences/*.md | wc -l)"
unzip -p dist/mental-model-skill.zip mental-model/SKILL.md | grep -E '^\|'
```

Expected: the SKILL.md table shows skills 60, experiences 20, and the same numbers as the loop for the rest. Commit nothing from `dist/`.

- [ ] **Step 3: Open the PR**

```bash
gh pr create --base main --title "Skills: the 60 curated skills, profile and experiences re-cut" --body "$(cat <<'EOF'
Implements docs/superpowers/specs/2026-08-26-skills-reference-design.md (PR #2).

- 23 first-cut skills replaced by 60 curated ones, texts exactly as reviewed in the comparison's third table; nine groups; `skills/README.md` indexes them
- Profile Skills table re-cut: <N> rows, levels drafted by the spec's §6 rubric — the `<!-- levels drafted — review -->` marker stays until you have read them
- Every experience re-pointed at the skills its own bullets evidence
- validate: R1–R10 ✓; export counts match disk

Merging accepts the levels. Edit a row on this branch first if one is wrong.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

Replace `<N>` with the actual row count. The PR's base is `main`; it includes the spec and plan commits from `skills-reference-spec`, so PR #2 can be closed as superseded or merged first — the owner's call, say so in the report.

- [ ] **Step 4: Report**

State: the PR URL; the validate report's per-rule lines and its **Not checked** block verbatim; the export counts; the row count of the profile table; any skill from the 60 that no experience evidences and no profile row claims (expected: most of the 60 — that is by design, the vocabulary is larger than one person's claims).
