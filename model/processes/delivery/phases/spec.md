---
source: Local
owner: Specifier
executed-by:
  - Specifier
supported-by:
  - Writer
gate-approvers:
  - Owner
escalation-authority: Owner
gate-to: Plan
---

# Spec

> Write what the change must do, completely enough that nobody downstream has to guess.

## What it takes

A classified request, the model the change must not contradict, and whatever it will touch.

## Activities

### Code

1. The Specifier reads the model and the code the change lands in, before proposing anything.
2. The Specifier names the approaches worth considering, with their trade-offs, and recommends
   one.
3. The Specifier writes the specification: the gap, the decisions and their reasons, what was
   rejected and why, and what is explicitly not being done.
4. The Specifier parks every question that is the Owner's, rather than answering it conveniently.

### Prose

1. The Specifier names the audience, the one point, and the facts the text may claim with
   where each is shown.
2. The Specifier names the file and the place it lands, and the register the place calls for.
3. The Specifier names the claims it may not make.

## What it produces

| Deliverable | Description |
| --- | --- |
| Specification | The whole of the requirements for a change to code, with what is not being done named |
| Brief | For prose: the audience, the one point, the facts it may claim and where it lands |

## What it never does

- Never writes the change it specifies.
- Never decides a question that is the Owner's; it names the options and parks it.
- Never states a fact the model does not hold.
- Never leaves a question unasked because an assumption would be convenient.

## Gate

To leave Spec, all of these hold:

- The Owner has read the specification or the brief and approved it.
- What is explicitly not being done is written down.
- Every parked question has the Owner's word on it.

Where they cannot be met, the Owner decides whether the change is reshaped, narrowed or dropped.
