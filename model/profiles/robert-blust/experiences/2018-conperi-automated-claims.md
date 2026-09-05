---
source: Local
kind: Project
start: 2018-11
end: 2020-10
organization: 3AP AG
skills:
  - Solution architecture
  - Microservices architecture
  - Cloud architecture
  - Java
  - Database design
  - Container orchestration (Kubernetes)
  - Platform engineering
  - CI/CD
  - MLOps
  - Machine learning
  - Event-driven architecture
  - Event streaming
---

# Conperi

> 3AP · Architect — the platform, the labeling tool and the serving path of an applied-research proof of concept with ZHAW for reading health-insurance invoices into claims.

## Achievements

- An applied-research proof of concept for AXA Health: reading scanned invoices well enough to process a health-insurance claim without a person retyping it, built by 3AP with ZHAW as research partner.
- Architected the processing pipeline to 3AP's microservice reference architecture, on MongoDB and as Kafka-streamed services — Java and Spring Boot for the entry point, the gateway and the dataset management, Python inside the four services that did the modeling, which is the polyglot half of that architecture actually used — region detection over the scanned page, extraction of what was found, classification of the extracted positions and a quality gate before anything downstream trusted the result.
- Put every service on a build pipeline from the first commit, including the rule that stops a build when nothing in its own subdirectory changed — a monorepo of eight services otherwise rebuilds all of them for one edit.
- Built and ran the platform underneath it on Google Kubernetes Engine, from cluster creation to the Kafka backbone, the document store, distributed tracing, the OAuth gateway in front of the services and GPU nodes in the one region that had them so models could be trained where the data already was.
- Built the labeling tool that made training possible: a browser application for drawing regions over an invoice and naming what each one held. Labeled invoices were the bottleneck the whole project ran into, and none existed before this.
- Set up the training and serving split around the models — a service that trains, a registry that versions each model with the metadata to reproduce it and a separate service that serves the chosen version — so a model could be replaced without redeploying what consumed it.
- ZHAW made the modeling calls. The computer-vision work and the classifier that read a claim's positions were theirs; the pipeline they ran inside, the data that fed them and the path their output took to a consumer were 3AP's.
- Ended as a proof of concept, which is what the funding instrument is for. Nothing from it went into production at AXA.
