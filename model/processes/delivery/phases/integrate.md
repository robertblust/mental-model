---
source: Local
owner: Owner
executed-by:
  - Owner
supported-by:
  - Reviewer
gate-approvers:
  - Owner
escalation-authority: Owner
---

# Integrate

> Put the change where it binds, and move everything that names it.

## What it takes

A branch that left Implement with its checks green, and the specification it was made from.

## Activities

1. Review the whole branch against the specification, not task by task.
2. Open the pull request and stop.
3. The Owner reads the diff and the rendered page, and merges.
4. Where a release is due, tag it and publish it.
5. Move every pin that names the release, and delete the branch as its own step.

## What it produces

| Deliverable | Description |
| --- | --- |
| Merged change | On the default branch, with its checks green |
| Release | Where one is due: the tag, its notes, and every pin that names it moved |

## What it never does

- Never merges without the Owner; an agent opens and reports.
- Never chains a branch delete after a merge, because a failed merge would still run the delete
  and close the pull request.
- Never leaves a member pinned to a release that no longer exists.
- Never releases a change the model disagrees with.

## Gate

Integrate is the last phase. The work is done when all of these hold:

- The checks pass on the pull request.
- The Owner has merged it.
- Every pin that names the release has moved with it.

Where they cannot be met, the Owner decides whether the change is reverted or the release held.
