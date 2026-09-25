---
source: Local
owner: Owner
measures: Delivery
unit: percent of deployments
direction: lower
read-with:
  - Deployment Frequency
---

# Deployment Rework Rate

> The share of deployments that were not planned and happened because of an incident in production.

## How it is measured

A deployment is a merge to `main` in a repository whose workflows publish one of this model's surfaces: the blust.ch website, which GitHub Pages publishes, and the mcp.blust.ch MCP server and the chat.blust.ch chat, which that repository's deploy and chat workflows publish. A merge counts once, however many of its workflows publish. The MCP Registry listing, republished when a release is tagged, and the LinkedIn profile, kept by hand, are not deployments.

The deployments of a calendar month made because something in production was wrong, a revert, a hotfix or an emergency re-pin, divided by all deployments of that month. Whether a deployment is rework is read from why it was made, which its pull request says, not from its size.

## What it can hide

It falls when fixes are held back and shipped inside planned work, so the incident lasts longer and the rate looks better. Deployment Frequency, read beside it, shows whether planned deployments are still going out.

## References

| What | URL |
| --- | --- |
| DORA's definition | https://dora.dev/guides/dora-metrics/ |
