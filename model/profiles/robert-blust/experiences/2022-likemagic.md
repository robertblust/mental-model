---
source: Local
kind: Role
start: 2022-04
end: 2026-05
organization: LIKE MAGIC AG
skills:
  - Agentic AI development
  - AI tool integration (MCP)
  - Context engineering
  - Conversational AI
  - AI strategy
  - AI governance
  - API design
  - Business architecture
  - Domain-driven design
  - Multi-tenant SaaS architecture
  - Microservices architecture
  - Cloud architecture
  - Container orchestration (Kubernetes)
  - Platform engineering
  - Database design
  - Integration architecture
  - Event-driven architecture
  - Identity and access management
  - Information security management
  - Data protection (GDPR)
  - Infrastructure as code
  - CI/CD
  - DevOps
  - Java
  - Software engineering
  - Software testing
  - Process orchestration
  - Business process modeling (BPMN, DMN)
  - Engineering leadership
  - IT strategy
  - Product management
  - Frontend development (TypeScript, React)
  - Event streaming
  - Data engineering
  - Knowledge management
  - Technical writing
  - Site reliability engineering
  - Observability
  - FinOps
  - Vendor management
  - Incident management
  - Change management
  - Mentoring and coaching
  - Company vision and strategy
  - Organization design
---

# Co-Founder & Head of Technology

> Built and ran the SaaS hospitality platform behind 90+ customers and 16,000+ units across DACH.

## Achievements

- Co-founder and Head of Technology of LIKE MAGIC AG.
- Owned the technology direction and developed the technical leadership as the company grew from 5 to 25 people.
- Built and scaled a multi-tenant hospitality SaaS platform serving 90+ customers, 430+ properties and 16,000+ units across the DACH region — processing 1.5M+ reservations, 8.1M+ guest communications and 89M+ platform events annually, integrating 3 PMS (Mews, Apaleo, Oracle OHIP) and 15+ smart-lock systems into a unified guest experience.
- Developed and executed the company-wide AI strategy — governance under a Human Oversight principle, organizational knowledge management and the productive rollout of AI assistants across plan, change and run; data-privacy guardrails (no internal context used to train external LLMs), multi-provider tooling (Claude, Gemini, Copilot, n8n) and cost governance.
- Defined and executed the product and platform strategy across 12 business domains (L0 concepts, L1 capabilities) — API-first, with a managed public API and event/data hub, evolving toward an MCP-server layer so AI agents consume the platform directly.
- Cut the platform into services by business capability — booking, guest, profile, payment, door access, messaging, operation and analytics — each stateless, self-contained, horizontally scalable and contract-first, with every integrated vendor reached through its own connector carrying a fallback path behind the realtime one.
- Drove process orchestration with Camunda for the end-to-end guest journey (Booking → Check-in → Stay → Check-out), carried over from Stay KooooK and run until 2023.
- Led the reassessment when the Camunda contract came up for renewal: the platform used a fraction of what the engine offered, so the choice was to build on it properly or take it out. Recommended building on it; the decision went to removal, and the orchestration was replaced with the platform's own in April 2023.
- Featured in a Camunda reference case citing a 95% self-check-in rate, 9.0/10 guest happiness and 7,000 process instances per month.
- Owned the production cloud platform (site reliability engineering, incident management, performance), built as Infrastructure-as-Code on Google Cloud with DevOps and CI/CD standards, unit and integration tests running on every pipeline.
- Instrumented it on Cloud Monitoring and Cloud Trace with alerting driven by defined SLOs, end-to-end traceability and continuous monitoring being architecture principles the services were built to rather than instrumentation added afterward.
- Built the LIKE MAGIC Mental Model — a structured organizational knowledge base (roles, processes, features, strategies, architecture decisions) that serves as the shared context layer for AI-assisted operations.
- Kept it in step with the systems it described through MCP rather than bespoke integrations — Atlassian, Google Drive and Slack servers wired into the agent that maintained it, reading and writing Confluence pages, Jira issues, Google Docs and Sheets, each command scoped to a named allowlist of the tools it was allowed to call.
- Built an internal AI marketplace on Claude (Claude Cowork) — giving teams governed access to AI assistants and agents, grounded in the Mental Model.
- Architected the integration of AI communication vendors (d3x, ailean and onsai) into the staff solution — unified multi-channel guest messaging with AI agents answering, guest insights and staff collaboration.
- Budget holder for the cloud platform and AI tooling — forecast and governed spend across dev, test and production, with consumption KPIs defined in the Mental Model and weekly actuals generated automatically from the Google Cloud billing API, routed to owners by role when a threshold was breached.
- Held platform cost flat as volume grew to 89M+ events annually, through continuous database and code optimization.
- Built information-security management: ISO 27001 (in progress), GDPR compliance and zero-trust API boundaries.
- Published and consumed the platform's events through Spring Cloud Stream over a Pub/Sub binder, so a service declared its bindings and the transport stayed swappable underneath them.
- Built the event and data hub every service published its business events to — ingesting them into BigQuery for analytics, idempotent on the event id so a redelivery cannot double-count, and serving them back as a queryable event log with webhook subscriptions for systems that needed them pushed.
- Tech stack: Java, Spring Boot / WebFlux, Spring Cloud GCP, Spring Cloud Stream, PostgreSQL, R2DBC/jOOQ, Google Pub/Sub, BigQuery, GraphQL, React / TypeScript / MUI, Kubernetes (GKE), Camunda BPMN, GitHub Actions.

## Ending

Left in May 2026 after four years, with the platform mature at 90+ customers and 16,000+ units,
to focus on where my own work was heading: modeling and AI, built in the open.

## References

| What | URL |
| --- | --- |
| Commercial register entry | https://www.zefix.ch/en/search/entity/list/firm/1576900 |
