---
name: mental-model-evidence-coverage
description: Check every Skills-table evidence cell against the experiences that show the skill, and report cells claiming an engagement nothing carries. Run when a cell is written or rewritten.
---

# mental-model-evidence-coverage

This instance's own skill, not one of the portable `companygraph-*` set. It checks a thing core
does not model: the profile schema types the `Evidence` column as `string`, so R4 never reaches
inside it, and a cell can name an engagement no experience shows without any rule turning red.

The rule it enforces is the profile schema's own writing rule — **one row per skill claimed, and
a claim needs something under it**. A cell that names four engagements while two experiences
carry the skill is a claim with two thirds of nothing under it.

## Why it is not in `companygraph-validate`

Every check in that pass and in the package's `verify/check.mjs` cites a numbered rule from
`CONVENTIONS.md`. There is no rule for this, and inventing one would bind every instance to a
heuristic. The matching is heuristic: an organization name in a cell can be an engagement, a
vendor, a product or a host, and telling them apart is reading, not parsing.

## Procedure

1. For every experience, collect the names it could be cited by: its `organization` field and
   the proper nouns in its H1. Record which skills its `skills:` list declares.
2. For every row of the profile's Skills table, take the set of experiences declaring that
   skill, and the union of their names.
3. Read the Evidence cell. For each name it mentions that is not in that union, decide by
   reading which of these it is:
   - **an engagement the cell claims** — the finding. The experience is missing the skill, or
     the cell is claiming work that entry does not carry. Say which.
   - **a vendor, product, standard or host** — not a finding. Camunda in “a published Camunda
     case study” is the publisher; Camunda in “owned the Camunda orchestration” is the tool.
     Neither is an engagement.
   - **an artifact of splitting a name** — not a finding. “Analysis & Design” yields Analysis
     and Design as separate tokens and neither is an organization.
4. Report each finding as the skill, the name, and which of the two repairs applies. Do not
   apply either: which one is right is the owner's call, because adding the skill to an
   experience and narrowing the cell claim different things about what happened.

## What this does not check

The other direction — an experience declaring a skill the cell never names — is not a fault. A
cell is a summary, not an index, and Integration architecture is shown by eight experiences with
two named. Reporting it produces about thirty lines of noise and no findings; it was tried.

Nor does this reach whether an evidence cell is *true*. It checks that a claim is carried by the
entries beneath it, which is a weaker thing, and the faults it finds are usually a cell edited
without its experiences following.

## Not checked

Say so in the report: this reads names, so a cell claiming an engagement without naming it —
“across three client platforms” — passes and should not be read as verified.
