---
source: Local
owner: Planner
executed-by:
  - Planner
supported-by:
  - Specifier
gate-approvers:
  - Owner
escalation-authority: Owner
gate-to: Implement
---

# Plan

> Cut the approved specification into pieces that can be worked one at a time.

## What it takes

A specification or brief the Owner has approved, and the repository the work lands in with the
rules that bind it.

## Activities

### Code

1. The Planner maps the files the change creates and modifies, and what each is responsible for.
2. The Planner cuts the work into task briefs, each the whole of its own requirements.
3. The Planner names the interfaces each brief produces and consumes, so no brief depends on a
   conversation its holder did not have.
4. The Planner orders them so each can be worked, tested and committed on its own.

### Prose

1. The Planner names the elements that change, and in what order.
2. The Planner names which of them the Translator re-runs on, and which need no German.

## What it produces

| Deliverable | Description |
| --- | --- |
| Task briefs | An ordered set, each whole on its own, each with a way to tell it is done |

## What it never does

- Never re-opens a decision the specification took.
- Never writes a brief whose holder would have to guess at an interface.
- Never writes the change.
- Never plans a task whose completion cannot be checked.

## Gate

To leave Plan, all of these hold:

- The Owner has read the plan and approved it.
- Every brief states how its holder can tell the task is done.
- The order is one the briefs can actually be worked in.

Where they cannot be met, the Owner decides whether the plan is recut or the specification
reopened.
