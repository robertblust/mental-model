---
name: companygraph-add-entity
description: Add one entity to this CompanyGraph instance from a prompt — the shell from its schema, the body from the prompt, then validate.
---

# companygraph-add-entity

`companygraph add` — the CLI — does not exist in this instance, so its half is done by hand:
read the schema by the R9 fixed shape, write the shell, then fill it.

## Procedure

1. Take the type and the name from the prompt. Read `meta/<type>-schema.md` — its tables only.
2. Resolve the path from `## File Location`. An owned type (`**Owner:**` line) needs its owner
   named in the prompt and lands inside the owner's folder; refuse an owner that resolves to
   no entity of the owning type. A type that owns collections becomes a folder holding its own
   file and one empty folder per owned type.
3. Write the shell: frontmatter with every field the table declares — required ones present,
   optional ones as `# field:` YAML comments; H1 exactly as given; every required section as a
   heading; a `Table.` section gets its header row from the column table.
4. Fill the body from the prompt. Every reference is the H1 of an existing entity — never
   invent one; if the prompt names an entity that does not exist, stop and offer to add it
   first, in a separate run.
5. Remove the optional-field comments that stayed empty. Run `companygraph-validate`.
