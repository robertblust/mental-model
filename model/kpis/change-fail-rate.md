---
source: Local
owner: Owner
measures: Delivery
unit: percent of deployments
direction: lower
read-with:
  - Deployment Frequency
---

# Change Fail Rate

> The share of deployments that need immediate intervention once they are in production.

## How it is measured

A deployment is a merge to `main` in a repository whose workflows publish one of this model's surfaces: the blust.ch website, which GitHub Pages publishes, and the mcp.blust.ch MCP server and the chat.blust.ch chat, which that repository's deploy and chat workflows publish. A merge counts once, however many of its workflows publish. The MCP Registry listing, republished when a release is tagged, and the LinkedIn profile, kept by hand, are not deployments.

The deployments of a calendar month in UTC that were followed, before the next planned change to the same surface, by a revert, a fix or a re-pin made because of them, divided by all deployments of that month. Deployments and their times are read from the merges to `main` in the GitHub history of robertblust/robertblust.github.io and robertblust/mcp-blust-ch; their publishing runs are GitHub Pages' own `pages-build-deployment` runs for the site and mcp-blust-ch's `deploy` and `chat` workflow runs on `main`. A failure is what a visitor, an agent or a check against the live surface met, not a workflow run that failed before publishing anything.

## What it can hide

It falls when fewer changes ship, and when a failure is folded into the next planned change instead of being named as one. Deployment Frequency, read beside it, shows the first; the second shows only if failures are named when they happen.

## References

| What | URL |
| --- | --- |
| DORA's definition | https://dora.dev/guides/dora-metrics/ |
