---
id: 01a06bb7-7bb0-7ab8-a36b-db23d33d4740
source: Local
kind: Project
start: 2018-11
end: 2020-10
organization: 3AP AG
role: Architect
skills:
  - Solution architecture
  - Microservices architecture
  - Cloud architecture
  - Database design
  - Container orchestration
  - Platform engineering
  - MLOps
  - Machine learning
  - Event-driven architecture
  - Event streaming
---

# Conperi

> 3AP · Architect — the platform, the labeling tool and the serving path of an applied-research proof of concept with ZHAW for reading health-insurance invoices into claims.

## Achievements

### Context

- An applied-research proof of concept for AXA Health: reading scanned invoices well enough to process a health-insurance claim without a person retyping it, built by 3AP with ZHAW as research partner.
- ZHAW made the modeling calls. The computer-vision work and the classifier that read a claim's positions were theirs; the pipeline they ran inside, the data that fed them and the path their output took to a consumer were 3AP's.

### Architecture

- Architected the processing pipeline as four stages: region detection over the scanned page, extraction of what was found, classification of the extracted positions and a quality gate before anything downstream trusted the result.
- Built it on the polyglot half of 3AP's microservice reference architecture: Java and Spring Boot for the entry point, the gateway and the dataset management, Python inside the four services that did the modeling.
- Designed the microservice cut of the pipeline, one service per pipeline stage.
- Designed the streams as one Kafka topic per pipeline stage, so each service consumed the output of the stage before it and no stage called another directly.
- Designed the MongoDB data model the pipeline held its claims and datasets in.
- Set up the training and serving split around the models — a service that trains, a registry that versions each model with the metadata to reproduce it and a separate service that serves the chosen version — so a model could be replaced without redeploying what consumed it.

### Engineering

- Built and ran the platform underneath it on Google Kubernetes Engine, from cluster creation to the Kafka backbone, the document store, distributed tracing, the OAuth gateway in front of the services and GPU nodes in the one region that had them so models could be trained where the data already was.
- Made that platform self-service for ZHAW's researchers: they deployed a new model service and trained on the GPU nodes on their own, without asking 3AP.
- Put every service on a build pipeline from the first commit.
- Stopped a service's build when nothing in its own subdirectory changed, so one edit in the eight-service monorepo rebuilt one service rather than all eight.
- Built the labeling tool that made training possible: a browser application for drawing regions over an invoice and naming what each one held. Labeled invoices were the bottleneck the whole project ran into, and none existed before this.

### Results

- Ended as a proof of concept, which is what the funding instrument is for. Nothing from it went into production at AXA.
