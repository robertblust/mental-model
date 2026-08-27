---
source: Local
group: Architecture
---

# Microservices architecture

> Designing a system as a set of independently deployable services organized around business capabilities.

## In practice

Decompose a system into services with clear boundaries and define how those services
communicate and share data. Design for independent deployment, resilience to partial failure
and observability across service boundaries. Weigh the added operational complexity against the
flexibility gained from decoupling services. Typical tools: Kubernetes, Docker, Istio.
