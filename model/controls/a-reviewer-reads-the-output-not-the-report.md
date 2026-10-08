---
id: 01a0fe74-f5a5-7c70-9371-76a6ea40c295
source: Local
kind: detective
mode: manual
enforces:
  - A check counts only when its output was seen
performed-by: Reviewer
---

# A reviewer reads the output, not the report

> Each task's change is reviewed against its diff and the checks' output, and the implementer's report is read as a claim to verify.

## How it is carried out

The Reviewer, after each task in Implement and once over the whole branch before Integrate: it reads the diff and the output of the checks the task ran, verifies each claim of the report against them, and names a gap as a finding; a check whose output it cannot see does not count as passed.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| seat | Reviewer | |
| phase | Implement | Delivery |

## References

| What | URL |
| --- | --- |
| Rulebook, superpowers | https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md |
