---
source: Local
group: Architecture
---

# Multi-tenant SaaS architecture

> Designing a software system so a single deployment serves many customers securely and efficiently while keeping their data and usage isolated.

## In practice

Decide how tenants share or are isolated from underlying compute, storage and configuration.
Design for per-tenant data isolation, customization and scaling so one tenant's usage cannot
affect another's experience. Plan onboarding, billing and upgrade paths that work across the
whole tenant base rather than one customer at a time.
