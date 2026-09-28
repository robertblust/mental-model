---
source: Local
decided: 2026-09-28
kind: Architecture
status: Standing
by: Owner
upholds:
  - Model it before you build it
---

# An agent's commit is authored by the seat it held

> A commit an agent makes in my repositories is authored by the seat it held, at the domain of the instance that governs the repository, as `Implementer <implementer@blust.ch>`, and names the process, phase and track it was made in; my own commits stay mine, and a check refuses a seat the named phase does not list.

## The question

Whose name an agent's commit carries. My processes name the seats that execute each phase and agents do most of the Delivery work, yet every commit carried my name. It had to be decided before the hook and the report were specified, on September 28, 2026, because the tooling writes and checks whatever the call says.

## Alternatives

| Option | Why not |
| --- | --- |
| My name on every commit, as before | The history could not say which seat did the work, or in which process. |
| My name as the author, and the seat only in a trailer | GitHub and `git shortlog` group by author, so every report by seat would need tooling to read a trailer, and my own commits could not be told from an agent's at a glance. |
| An email field on each seat | A second copy of what the model already derives from the role's name and the identity's `url`, free to drift from it. |
| An `owner@` address for my own commits | My name already means me, and a report tells people from agents by exactly that difference. |
| A Claude Code hook refusing a commit made without `--author` | It would guard one agent and be a rule no other agent sees, where the `commit-msg` hook is the one every agent meets. |

## Why

The model is where people and agents both read who does what, and a history that names only me leaves its seats unchecked in the one place every change is recorded. Authoring by seat puts the model's own vocabulary on each commit, checked against the phase that lists the seat, so a report by seat is read from git rather than reconstructed from memory, and with each seat's address verified on my GitHub account every commit still links to me.

## Consequences

Every seat that commits needs an address on the domain, a mail alias onto my mailbox verified on my GitHub account. The Owner, the Controller, the Reviewer, the Answerer and the Visitor get none, because they never commit: my own commits are authored as robert@blust.ch, the identity's address, where they were robert.blust@flatland.ch before, the Controller writes nothing, the Reviewer returns findings, the Answerer answers at runtime and a Visitor commits under their own name. The hook stays off in an organization until its domain receives mail. Commits made before the rule keep the author they have, because rewriting published history would force-push every repository. The call stays right for as long as agents do the work under seats the processes name, and the processes stay what the check reads.

## Bears on

| Type | Entity | Owner | How |
| --- | --- | --- | --- |
| role | Specifier | | changed it |
| role | Planner | | changed it |
| role | Implementer | | changed it |
| role | Writer | | changed it |
| role | Translator | | changed it |
| role | Narrator | | changed it |

## References

| What | URL |
| --- | --- |
| Specification | https://github.com/companygraph/meta-model/blob/main/docs/superpowers/specs/2026-09-28-a-commit-names-its-seat-design.md |
| Pull request of the specification | https://github.com/companygraph/meta-model/pull/179 |
