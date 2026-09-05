---
source: Local
group: Modeling and process
---

# Spec-driven development

> Writing down what a system must do, and why, before any of it is built — and building only against that text.

## In practice

Write the specification first: purpose, decisions, the alternatives rejected and why, what is
out of scope. Get it reviewed by the people who will disagree later, then derive the plan and
the tests from it rather than from the code. Keep the spec in the repository beside the code
it governs and change it before changing the behavior. Let agents and people build from the
same text. Typical tools: spec-kit.
