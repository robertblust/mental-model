---
source: Local
kind: Community
start: 2026-07
url: https://guestgraph.io
skills:
  - Agentic AI development
  - Software architecture
  - Spec-driven development
  - Data modeling
  - Database design
  - API design
  - Open-source stewardship
  - Product discovery
  - Company vision and strategy
  - Public speaking
  - CI/CD
  - Data governance
---

# GuestGraph

> Ongoing. An open-source guest identity graph for hospitality: one guest out of every system's version of them, every merge explained and reversible.

## Achievements

### Leadership

- Published it under Apache 2.0 as open core, with a billing model on one meter, arrivals, and a narrated introduction talk in German and English with a deck and a PDF in each.
- Put it up for validation in the open as one of two ideas: the engine, the guest graph with its API, the explain-and-undo and the connectors are the open substance, and the hosted service is the one part that could ever earn; whether it will is the experiment.

### Architecture

- Designed the identity graph's data model: guests, their source records and the merge decisions between them.
- Built it as a layered confidence model: strong identifiers merge deterministically with transitive closure, everything else is scored against a threshold the tenant chose, and what falls between goes to a human steward, whose split becomes a do-not-merge rule that new evidence cannot cross.
- Split probabilistic matching into blocking and scoring, because a database index answers only equality: phonetic keys find candidates that share no identifier, then a weighted feature vector grades them, damped when few signals were observed and penalized when birthdates conflict.
- Kept every source record immutable and every merge explainable, so a guest can be asked why two records are one person and the answer is the decision chain.
- Designed and implemented the engine's and the connector's REST APIs contract-first in OpenAPI, the engine's exposing a merge's explanation, its undoing and the review of uncertain matches as resources of their own.

### Engineering

- Shipped it as a Spring Boot service on PostgreSQL with Flyway migrations and a REST API, runnable from one compose file, designed for managed platform services and agnostic of which cloud runs them — so adopting it is not also adopting a provider.
- Held the engine and the connector to the same gates on every change: the Maven build with its tests, a check that each service carries every item of the service conventions at their pinned release and a job that regenerates the entity-relationship diagram from the Flyway migrations and fails when the committed one is stale.

### Ways of working

- Designed the engine and the connector slice by slice, each from a written specification reviewed before its plan and its build, beginning with core identity resolution, probabilistic matching and the guest timeline.
- Built it through the agent seats the model defines, each under its own rulebook and none of them deciding, with the Owner reviewing and merging.

### Results

- Put it in front of a professional network with a stated outcome each way, a clean no included.

## References

| What | URL |
| --- | --- |
| Source repository | https://github.com/guestgraph/engine |
