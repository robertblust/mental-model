---
source: Local
group: Modeling and process
---

# Domain-specific language design

> A language built for one domain — its metamodel, syntax and semantics — so that experts can state their intent directly and tools can act on it.

## In practice

Identify the concepts a domain's experts actually reason in and fix them as a metamodel. Give
the language a concrete syntax, textual or graphical, with the constraints that make an invalid
model unwritable. Build the editor, validation and generators around it, and evolve the
language with the domain without breaking existing models. Typical tools: EMF, Ecore, Xtext,
Sirius, MPS.
