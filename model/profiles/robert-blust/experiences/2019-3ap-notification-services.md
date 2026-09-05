---
source: Local
kind: Project
start: 2019-04
end: 2020-06
organization: 3AP AG
skills:
  - Platform engineering
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

> 3AP · Built the shared notification capability the company's own platform offered its projects.

## Achievements

- A notification service on 3AP's internal platform that any project could call instead of integrating messaging vendors of its own: one authenticated POST, delivered as e-mail, SMS or a Slack message, with the vendor behind each channel a detail of the platform rather than of the project.
- Separated accepting a message from delivering one — the receiving service publishes to a queue for each channel and a service per channel consumes it — so a vendor that is slow or down delays delivery instead of failing the caller.
- Traced a message across that hand-off with Spring Cloud Sleuth, so a message that never arrived can be followed past the queue rather than lost at it, and wired each service's health endpoint to its readiness and liveness probes with a request and a limit set for every container.
- Made the build the gate: every branch and every pull request analyzed on SonarCloud with test coverage attached, container images built without a Dockerfile to write, and a green build on the mainline deploying itself to the cluster.
- Kept the architecture in the repository as text — the component diagram in PlantUML beside the code, and an object model of each target platform's own concepts, written while the platform was being deployed to both.
