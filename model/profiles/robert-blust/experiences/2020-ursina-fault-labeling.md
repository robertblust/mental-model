---
source: Local
kind: Project
start: 2020-04
end: 2020-07
organization: 3AP AG
role: Architect
skills:
  - Solution architecture
  - Integration architecture
  - Identity and access management
  - Java
  - Software architecture
  - Microservices architecture
  - Database design
  - Software engineering
---

# Ursina

> 3AP · Architect — the software architecture, the path into a broadband operator's network and the authentication boundary of a tool that turns network faults into a labeled training set.

## Achievements

### Context

- A tool for a cable-broadband operator that turns network faults into a training set: an operator assigns a cause to a device over a time window, a scheduled job proposes assignments from event mappings and every assignment carries a verification status, so what reaches the training database has been accepted by a person rather than inferred.

### Architecture

- Designed the software architecture, the microservice cut and the database design, on 3AP's reference architecture.
- Designed the path from a public cloud application to the operator's own data platform — device telemetry read from an HBase cluster on their network and the labeled set held in their PostgreSQL — over tunnels that kept both databases unexposed.

### Engineering

- Wrote the API gateway in Java and Spring Cloud Gateway, with Keycloak as the identity provider and OAuth2 in front of every route.
- Implemented the gateway's token relay as a filter of its own, because the framework's relay handed on an access token without refreshing it and a session outlived its token. It follows Spring's own authorized-client exchange filter and cites the upstream issue it stands in for, so it can be deleted when that closes.
- Put the monorepo on a build pipeline that tested each package and pushed images to a registry before deploying, with static analysis reporting on every build.
