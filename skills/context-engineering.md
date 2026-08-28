---
source: Local
group: AI
---

# Context engineering

> Structuring what an AI model or agent is given to work with — the documents, definitions and rules in its context — so its output is grounded in how the organization actually works.

## In practice

Decide what an agent needs to know for a task and shape it into something a model can load:
curated documents rather than raw dumps, explicit definitions rather than implied ones, rules
written where the work happens. Keep the context where the people who own the facts can edit
it, so it stays true without becoming a maintenance project of its own. Package and distribute
it so every assistant works from the same version instead of a private copy. Test what the
model does when context is missing or stale, and constrain it so a gap surfaces as a failure
rather than as an invention.
