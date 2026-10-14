---
id: 01a13c3b-e14f-722f-a2e8-240dc563ab97
source: Local
modality: must not
---

# A worktree is removed only once its plan is done

> A worktree that holds a plan's ledger is not removed before every task of that plan is done, even when its pull request has merged.

## Why

A plan's ledger, its briefs and its task reports live in the worktree under `.superpowers/`, which git ignores, and `git worktree remove` deletes ignored files without asking, with or without `--force`, so nothing brings them back. A merged pull request does not finish a plan: a plan can carry tasks in other repositories that are still owed. Three ledgers were lost this way in September 2026, twice in one day.
