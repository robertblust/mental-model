---
source: Local
owner: Owner
measures: Delivery
unit: hours
direction: lower
read-with:
  - Change Fail Rate
---

# Failed Deployment Recovery Time

> The time it takes to recover from a deployment that fails and needs immediate intervention.

## How it is measured

A deployment is a merge to `main` in a repository whose workflows publish one of this model's surfaces: the blust.ch website, which GitHub Pages publishes, and the mcp.blust.ch MCP server and the chat.blust.ch chat, which that repository's deploy and chat workflows publish. A merge counts once, however many of its workflows publish. The MCP Registry listing, republished when a release is tagged, and the LinkedIn profile, kept by hand, are not deployments.

For each failed deployment, as Change Fail Rate counts them, the time from that deployment going live to the deployment that restores the surface going live, whether a revert, a fix or a re-pin to an earlier release. The value is the median over a calendar quarter. A failure no deployment caused, a provider's outage, is not counted.

## What it can hide

It shortens when every failure is reverted rather than fixed, which restores the surface and leaves the change undone, so the change comes back as rework. Failures are rare here, so a quarter's median can rest on one or two events, and one slow recovery moves it a long way.

## References

| What | URL |
| --- | --- |
| DORA's definition | https://dora.dev/guides/dora-metrics/ |
