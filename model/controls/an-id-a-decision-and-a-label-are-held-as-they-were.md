---
id: 01a13c3b-e14f-78de-8e41-201b8987c4d4
source: Local
kind: preventive
mode: automated
enforces:
  - What is cited from outside the model is not rewritten
---

# An id, a decision and a label are held as they were

> A pull request to the model fails where it changes an id already on the default branch, rewrites a decision beyond closing it, or moves, swaps or reuses a label.

## How it is carried out

The instance check, required on the default branch, on every pull request: its step `companygraph ids --range` compares each page of the branch with its base after both are put in the one form, and refuses a changed id, a decision whose text changed beyond its status and one dated closing sentence, and a label of a scenario, a step or an invariant that moved to another item, swapped with one or came back after it was removed. A reference name may follow the rename of what it names, and a URL under `## References` may change on its own. Where a release of core changed the schema that governs a type, the decision and label checks stand aside for that type and say so in a note.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| The instance check | https://github.com/companygraph/meta-model/blob/main/.github/workflows/instance-check.yml |
| The change checks | https://github.com/companygraph/meta-model/blob/main/lib/checks.mjs |
