---
source: Local
decided: 2026-09
kind: Portfolio
status: Standing
by: Owner
upholds:
  - Model it before you build it
---

# An agent's commit is authored by the seat it held

> A commit an agent makes in my repositories is authored by the seat it held, at the domain of the instance that governs the repository, as `Implementer <implementer@blust.ch>`, and names the process, phase and track it was made in; my own commits stay mine, and a check refuses a seat the named phase does not list.

## The question

Whether my history should say which seat did the work. My processes name the seats that execute each phase and agents do most of the Delivery work, yet every commit carried my name, so the record every change leaves could not say who did what, or in which process. It had to be decided before the hook and the report were specified, on September 28, 2026, because the tooling writes and checks whatever the call says.

## Alternatives

| Option | Why not |
| --- | --- |
| Keep my name as the author and name the seat only in a trailer | GitHub and `git shortlog` group by author, so every report by seat would need tooling to read a trailer, and my own commits could not be told from an agent's at a glance. |
| Give my own commits an `owner@` address | It would put a seat's address on work a person did, and a report tells people from agents by exactly that difference. |
| Have a Claude Code hook refuse a commit made without `--author` | It would guard one agent and be a rule no other agent sees, where the `commit-msg` hook is the one every agent meets. |

## Why

The model is where people and agents both read who does what, and a history that names only me leaves its seats unchecked in the one place every change is recorded. Authoring by seat puts the model's own vocabulary on each commit, checked against the phase that lists the seat, so a report by seat is read from git rather than reconstructed from memory.

## Consequences

Each seat that commits needs an address on each domain, a mail alias onto my mailbox verified on my GitHub account, so its commits still link to me, and until a domain receives mail the hook stays off in that organization's repositories. My own commits are authored as robert@blust.ch, the identity's address, where they were robert.blust@flatland.ch before. Commits made before the rule keep the author they have, because rewriting published history would force-push every repository. The call stays right for as long as agents do the work under seats the processes name, and the processes stay what the check reads.

## References

| What | URL |
| --- | --- |
| Specification | https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-09-28-a-commit-names-its-seat-design.md |
| Pull request of the specification | https://github.com/companygraph/meta-model/pull/179 |
