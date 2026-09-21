---
name: mental-model-evidence-coverage
description: Read the profile's Evidence table for what the instance checks cannot judge, a year that copies its experience's period and the rows that name no experience. Run when an Evidence row is written or rewritten.
---

# mental-model-evidence-coverage

This instance's own skill, not one of the portable `companygraph-*` set. The profile's evidence is a table of its own, one row per fact, and its `Experience` column is a qualifier the checker resolves and holds to its owner: a filled cell that names no experience, or one another profile owns, already fails by name. The two joins under that are the checker's as well: the profile schema declares that `## Evidence` stands under `## Skills` and that an experience's `skills` lists the row's skill, and the instance checks hold both (R16). What no check reaches is judgment, and this skill is what is left of it.

## Why it is not in `companygraph-validate`

Every check in that pass and in the package's checks cites a numbered rule from `CONVENTIONS.md`, and can fail. Neither step here can: whether a year is a copy depends on what the sentence means by it, and a blank cell is legal, so both end in a list for the owner and not in a finding.

## Procedure

1. Run the instance checks first. A claim with no row, a row under no claim and an experience
   that does not list the row's skill are theirs to report, and a miss of the last kind has two
   repairs that claim different things, adding the skill to the experience or naming another
   one, so report it and apply neither.
2. For every profile that owns experiences, read its `## Evidence` table, and for every
   experience it owns, its H1 and its `start` and `end`.
3. **The year is not a copy.** A row that names an experience and ends in a year in parentheses
   keeps that year only when it marks a period shorter than the experience's own. Report a year
   that equals the experience's period, since it is a second copy nothing keeps true.
4. **The open rows.** List every row whose `Experience` is blank, with its sentence. A blank cell
   is allowed, for a claim resting on no period of its own, so these are not failures. They are
   the rows a reader weighs with nothing to follow, and the owner decides each: name one
   experience, split the sentence into a row per experience, or leave it blank on purpose.

## What this does not check

Whether a row is *true*. This checks that each fact stands on the entries the model holds, which is a weaker thing. The other direction is not a fault either: an experience listing a skill that no Evidence row names is a fact the table chose not to summarize.

## Not checked

Say so in the report: this reads the tables and the frontmatter, not the prose of the experiences, so a row whose sentence claims more than its experience says passes here.
