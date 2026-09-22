---
source: Local
owner: Controller
executed-by:
  - Controller
  - Implementer
  - Reviewer
  - Writer
  - Translator
  - Owner
supported-by:
  - Planner
gate-approvers:
  - Owner
escalation-authority: Owner
gate-to: Integrate
---

# Implement

> Make the thing, and let nothing go forward unread.

## What it takes

An approved plan, a branch, and for each task the brief that is the whole of its requirements.

## Activities

### Code

1. The Controller dispatches one brief.
2. The Implementer works it, test first where the brief says so, and reports what was built,
   what was run and what it doubts.
3. The Reviewer reads the diff against the brief and returns findings, each with a file, a line
   and a severity, strengths named first.
4. The Controller decides: fix, accept, or park for the Owner.
5. The task is committed before the next one is dispatched.
6. A finding against a task already committed comes back as its own brief; the commit
   stands and the fix is a new one.

### Prose

1. The Writer drafts the English from the brief, on the branch, and reports which claims it
   could not trace to the brief or the repository.
2. The Owner reviews on the branch, in the diff and on the rendered page.
3. The Translator makes the Swiss Standard German from the reviewed English only, one element at a time,
   with the glossary open, and hands back a back-translation beside each element.
4. An English edit re-runs the Translator on that element alone.

## What it produces

| Deliverable | Description |
| --- | --- |
| Reviewed commits | One per task, on the branch, with every finding resolved or parked |
| Reviewed English | For prose: the draft the Owner has read on the branch and on the page |
| Swiss Standard German | For prose: made from the reviewed English, with its back-translation |

## What it never does

- Never changes a test's expectation to make it pass.
- Never makes the German from English the Owner has not reviewed.
- Never dispatches the next task while the last one's findings are open.
- Never claims a check that was not run.
- Never merges.

## Gate

To leave Implement, all of these hold:

- Every task's findings are resolved, or parked for the Owner and named in the pull request.
- The repository's checks pass on the branch.
- The branch does what the specification said, and nothing else.

Where they cannot be met, the Owner decides whether the branch is reworked or abandoned.
