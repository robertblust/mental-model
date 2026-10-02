---
id: 01a0a902-0cd8-728f-87dc-03847908879e
source: Local
owner: Owner
executed-by:
  - Controller
  - Reviewer
  - Owner
gate-approvers:
  - Owner
escalation-authority: Owner
---

# Integrate

> Put the change where it binds, and move everything that names it.

## What it takes

A branch that left Implement with its checks green, and the specification it was made from.

## Activities

1. The Reviewer reviews the whole branch against the specification, not task by task.
2. The Controller opens the pull request and stops.
3. The Owner reads the diff and the rendered page and gives the word; the merge follows.
4. Where a release is due, it is tagged and published on the Owner's word.
5. The Owner moves every pin that names the release, and deletes the branch as its own step.

## What it produces

| Deliverable | Description |
| --- | --- |
| Merged change | On the default branch, with its checks green |
| Release | Where one is due: the tag, its notes, and every pin that names it moved |

## What it never does

- Never chains a branch delete after a merge, because a failed merge would still run the delete
  and close the pull request.
- Never leaves a member pinned to a release that no longer exists.

## Gate

Integrate is the last phase. The work is done when all of these hold:

- The checks pass on the pull request.
- It is merged on the Owner's word.
- Every pin that names the release has moved with it.

## If not met

| Outcome | Leads to |
| --- | --- |
| release held | Integrate |
| reverted | |
