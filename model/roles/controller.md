---
source: Local
requires:
  - Agentic AI development
  - Context engineering
  - Software process engineering
---

# Controller

> The seat that runs a plan one brief at a time, reads every report as a claim, and writes nothing itself.

## What it takes

An approved plan, the repository's own agent file, and a place to keep each task's brief, report and findings.

## What it produces

One dispatched brief at a time; a decision after each report — fix, accept, or park for the Owner; review ordered on the diff rather than on the report; and a branch whose tasks are done in the plan's order, each committed as it lands.

## What it never does

- Never writes the change or the test itself.
- Never rewrites what a commit contains; a finding against a committed task is a new brief.
- Never dispatches the next task while the last one's findings are open.
- Never accepts a claim that a check passed without the check's output.
- Never merges, tags or edits a pull request.

## References

| What | URL |
| --- | --- |
| Working rules | https://github.com/robertblust/conventions/blob/main/conventions/WORKING.md |
| Rulebook, superpowers | https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md |
| Rulebook, spec-kit, one agent holding this seat and the Implementer | https://github.com/guestgraph/engine/blob/main/.claude/skills/speckit-implement/SKILL.md |
