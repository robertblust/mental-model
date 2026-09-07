# Export inputs

What `companygraph-export` reads from the instance when it builds the two artifacts. The skill
holds the procedure; this folder holds what is true of this instance and not of CompanyGraph.

- `SKILL-intro.md` — the paragraph that opens the agent skill, in the instance's own voice.
- `notebooklm-sources.md` — how this instance's entities group into NotebookLM sources, and why
  each grouping is one source.
- `notebooklm-verify` — asserts a built bundle is the model, whole. Run it after every export;
  a bundle is worth nothing if it is quietly short, which is how the first one went stale.
