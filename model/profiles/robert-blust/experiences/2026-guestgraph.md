---
source: Local
kind: Community
start: 2026-07
url: https://guestgraph.io
skills:
  - Agentic AI development
  - Software architecture
  - Requirements engineering
  - Spec-driven development
  - Data modeling
  - Database design
  - API design
  - Cloud architecture
  - Java
  - Open-source stewardship
  - Product discovery
  - Solution selling
  - Company vision and strategy
  - Public speaking
---

# GuestGraph

> Ongoing. An open-source guest identity graph for hospitality: one guest out of every system's version of them, every merge explained and reversible.

## Achievements

- Designed the engine from three written specifications — core identity resolution, probabilistic matching and the guest timeline — each reviewed before its plan and its build, and built by an AI coding agent working to them under a written agent file.
- Built it as a layered confidence model: strong identifiers merge deterministically with transitive closure, everything else is scored against a threshold the tenant chose, and what falls between goes to a human steward, whose split becomes a do-not-merge rule that new evidence cannot cross.
- Split probabilistic matching into blocking and scoring, because a database index answers only equality: phonetic keys find candidates that share no identifier, then a weighted feature vector grades them, damped when few signals were observed and penalized when birthdates conflict.
- Kept every source record immutable and every merge explainable, so a guest can be asked why two records are one person and the answer is the decision chain.
- Shipped it as a Spring Boot service on PostgreSQL with Flyway migrations and a REST API, runnable from one compose file, designed for managed platform services and agnostic of which cloud runs them — so adopting it is not also adopting a provider.
- Published it under Apache 2.0 as open core, with a billing model on one meter, arrivals, and a narrated introduction talk in German and English with a PDF in each.
- Put it in front of a professional network with a stated outcome each way, a clean no included.
