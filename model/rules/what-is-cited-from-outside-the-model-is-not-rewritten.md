---
id: 01a13c3b-e14f-7492-9f36-ffa64f8bf645
source: Local
modality: must not
---

# What is cited from outside the model is not rewritten

> Once on the default branch, an entity's id, a decision's text and a label on a page are not changed, because a link, a commit or a test outside the model may already cite them.

## Why

An outside system holds on to what it cites: a graph node to an entity's id, a commit or a later decision to a decision as it was decided, a test or a line of code to the label of a scenario, a step or an invariant. Each is the only handle that citation has, and a rewrite leaves it pointing at something that now says another thing, with nothing to tell whoever cited it. So an id stays with its entity, a decision that no longer stands is closed by its status and one dated sentence instead of being edited, and a label stays with the item it was given to and is never given to another.
