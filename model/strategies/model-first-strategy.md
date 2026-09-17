---
source: Local
adopted: 2026-09
serves:
  - Whoever decides about me decided from the model
upholds:
  - Decide well over build fast
  - Model it before you build it
---

# Model-First Strategy

> Agents draft everything, inside conventions written down first, and I spend my time on the decisions they cannot make.

## The approach

AI drafts and it checks; it never decides and it never publishes. That is the position, and
everything below exists to hold it: the constraint moved from building quickly to deciding
correctly, so the scarce thing is judgment, and judgment is protected by making every decision
leave a written artifact that a person put their name to. A fact enters the model from me or
from a document, never from a model's recall, and nothing goes out under my name that I have not
read against its sources.

A change of consequence starts as a written thing: a brief naming the audience and the facts it
may claim, a spec that keeps the finding that led to the decision, then a plan. A smaller one
still leaves a pull request, which is where its reason is written. Agents draft against those
and against the schemas; I review on the branch, in the diff and on the rendered page. The
conventions the agents work under are themselves files — how I write, how I work with git, what
each repository is — vendored into every repository at a pinned release, so a rule improves in
one place and reaches all of them. Roles are files too, in `model/roles/`: one seat held by me
and every other by an agent, each saying what it takes, what it produces and what it never does.
The Implementer commits what its brief specifies and never on its own initiative; none of the
other agent-held seats commits at all.

Checks carry the load I would otherwise carry by reading. An unresolvable reference is an error
rather than a warning, a pin that drifts fails a build, and the instance checker ends by naming
what it did not reach — because the failure mode of an agent-written repository is a green check
over an unread claim.

## What it rules out

No agent commits on its own initiative, and no agent merges at all. Work that leaves no artifact
is not done: a decision reached in conversation and never written to a spec will be re-opened,
so the conversation is not where it lives. Nothing is hand-maintained that could be derived — a
second copy of a fact is the thing this model exists to end. No tool enters the chain before the
convention it works under is written, because a tool adopted first sets the rules by what it
happens to do. And no fact reaches a published surface because a model produced it fluently: a
claim arrives from me or from a document or it does not arrive, and an agent that cannot find
its source says so instead of writing around the gap.

## What would show it is working

A change to a published surface that bypassed the path — hand-edited, no spec, no pull request —
is countable in git, and it has been zero since this strategy was adopted. A correction made
twice is countable the same way: if the same fact has to be fixed in two places, a derivation is
missing and the model has grown a second master. Both are visible the week they happen, which is
the point; a strategy about how the work is done cannot wait for the horizon to be judged.
