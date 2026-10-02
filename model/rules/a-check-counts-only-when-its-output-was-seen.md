---
id: 01a0fd4b-1c5b-7cbb-9e11-5816805eb457
source: Local
modality: must
protects:
  - Decide well over build fast
serves:
  - Whoever decides about me decided from the model
---

# A check counts only when its output was seen

> A check counts as passed only when its output, from a run over the change as it now stands, has been read; a report that it passed is not its output, and a check that finds nothing counts only once it has been shown to find something.

## Why

A report is a claim, and the person or agent writing it is the one least placed to see what it missed. A check run over an earlier state says nothing about the change as it stands, and a search that returns nothing may never have been asking the right question; on October 2, 2026, a form check that every task's tests passed failed on every family repository the first time it ran over one. Only an output, read, of a check that can find something tells me the change holds.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| role | Controller | |
| role | Implementer | |
| role | Reviewer | |
| process | Delivery | |
