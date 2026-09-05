---
source: Local
kind: Project
start: 2019-04
end: 2020-06
organization: 3AP AG
skills:
  - Platform engineering
  - Cloud architecture
  - Microservices architecture
  - Event-driven architecture
  - Integration architecture
  - API design
  - Container orchestration (Kubernetes)
  - CI/CD
  - Observability
  - Software modeling (UML, SysML, C4)
  - Java
---

# 3AP Platform — Notification Services

> 3AP · Built the shared notification capability the company's own platform offered its projects, and ran it on two clouds at once to show it depended on neither.

## Achievements

- A notification service on 3AP's internal platform that any project could call instead of integrating messaging vendors of its own: one authenticated POST, delivered as e-mail, SMS or a Slack message, with the vendor behind each channel a detail of the platform rather than of the project.
- Ran the same services on two clouds at once, which was the point of building them in the open like this: pushed to Swisscom's Cloud Foundry with a manifest and a bound message broker, and deployed to Google Kubernetes Engine as containers with the broker running beside them. Only the deployment descriptor and a Spring profile differed, so what a project depended on was the service and not the cloud under it.
- Separated accepting a message from delivering one — the receiving service publishes to a queue for each channel and a service per channel consumes it — so a vendor that is slow or down delays delivery instead of failing the caller.
- Traced a message across that hand-off with Spring Cloud Sleuth, so a message that never arrived can be followed past the queue rather than lost at it, and wired each service's health endpoint to its readiness and liveness probes with a request and a limit set for every container.
- Made the build the gate: every branch and every pull request analyzed on SonarCloud with test coverage attached, container images built without a Dockerfile to write, and a green build on the mainline deploying itself to the cluster.
- Modeled both platforms' own vocabularies side by side in PlantUML beside the code — organization, space, application and a bound service on one; project, cluster, pod and an exposing service on the other — so that what the two call the same thing, and where they genuinely differ, could be read rather than argued about.
- Retired the Cloud Foundry half in November 2019 once 3AP settled on its own Google Cloud platform, having established what it was built to establish.
