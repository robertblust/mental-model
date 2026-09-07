# Export inputs

What `companygraph-export` reads from the instance when it builds the two artifacts. The skill
holds the procedure; this folder holds what is true of this instance and not of CompanyGraph.

- `SKILL-intro.md` — the paragraph that opens the agent skill, in the instance's own voice.
- `notebooklm-AGENTS.md` — the reading guide the NotebookLM bundle ships as its `AGENTS.md`:
  what the notebook is, what each source holds, that references between entities are by name,
  and what a claim in the model rests on. A reader who opens a notebook cold has no other way
  to learn any of it. Every count it states is a `{{...}}` token the build substitutes with what
  it counted, so the guide cannot tell a reader 36 experiences beside a bundle holding 37.
- `notebooklm-verify` — asserts a built bundle is the model, whole. Run it after every export;
  a bundle is worth nothing if it is quietly short, which is how the first one went stale.

A `notebooklm-sources.md` beside these would group the entities into sources of the instance's
own naming, one `##` heading per source. This instance writes none, so the export cuts the
model by its own root types: a grouping keyed to anything the model has not declared for every
entity is a cut made by whatever a pattern happens to match.
