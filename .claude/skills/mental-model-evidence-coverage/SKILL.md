---
name: mental-model-evidence-coverage
description: Check the profile's Evidence table against the Skills table and the experiences, and report the joins the schema leaves to whoever writes. Run when an Evidence row, a Skills row or an experience's skills list is written or rewritten.
---

# mental-model-evidence-coverage

This instance's own skill, not one of the portable `companygraph-*` set. The profile's evidence
is a table of its own, one row per fact, and its `Experience` column is a qualifier the checker
resolves and holds to its owner: a filled cell that names no experience, or one another profile
owns, already fails by name. What the checker does not reach are the joins the profile schema
states as writing rules and says no rule checks. This skill checks those.

## Why it is not in `companygraph-validate`

Every check in that pass and in the package's checks cites a numbered rule from
`CONVENTIONS.md`. These joins have none: each would be the first rule in the checker to name a
type, and the schema chose to leave them written rather than break that.

## Procedure

1. For every profile that owns experiences, read its `## Skills` and `## Evidence` tables, and
   for every experience it owns, its H1 and its `skills:` list. A profile with no Evidence table
   is reported and skipped.
2. **Every claim has something under it.** Each Skills row has at least one Evidence row with
   the same skill, and each Evidence row's skill has a Skills row. Report either miss.
3. **The experience lists the skill.** The experience a row names carries the row's skill in its
   `skills:` list. A miss has two repairs that claim different things, adding the skill to the
   experience or naming another one, so report it and apply neither.
4. **The year is not a copy.** A row that names an experience and ends in a year in parentheses
   keeps that year only when it marks a period shorter than the experience's own. Report a year
   that equals the experience's period, since it is a second copy nothing keeps true.
5. **The open rows.** List every row whose `Experience` is blank, with its sentence. A blank cell
   is allowed, for a claim resting on no period of its own, so these are not failures. They are
   the rows a reader weighs with nothing to follow, and the owner decides each: name one
   experience, split the sentence into a row per experience, or leave it blank on purpose.

## What this does not check

Whether a row is *true*. This checks that each fact stands on the entries the model holds, which
is a weaker thing. The other direction is not a fault either: an experience listing a skill that
no Evidence row names is a fact the table chose not to summarize.

## Not checked

Say so in the report: this reads the tables and the frontmatter, not the prose of the
experiences, so a row whose sentence claims more than its experience says passes here.
