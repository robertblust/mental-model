---
id: 01a13d69-0423-7526-81a3-ac3b6e561274
source: Local
kind: preventive
mode: automated
enforces:
  - One session holds a piece of shared work
---

# A family resync refuses to start beside another

> A resync takes a lock before it moves anything, and refuses to start while another run holds it or while a resync pull request it did not open is still open.

## How it is carried out

The family resync in robertblust/conventions, each time a session starts it: it takes a lock in the clone's own git directory, which every worktree of that clone shares, and refuses while the run that holds it is alive; it then asks GitHub for the open pull requests of every member whose branch begins with `resync-`, and refuses where one is open that no run in this checkout opened or took on that day, unless it is started with `--force`. It holds a resync and nothing else: a release, a re-pin by hand or a change across repositories is claimed by the session itself, which reads the open pull requests, branches and tags and asks the running sessions before it starts, and nothing refuses a session that skips that.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| The family resync | https://github.com/robertblust/conventions/blob/main/family/resync.mjs |
