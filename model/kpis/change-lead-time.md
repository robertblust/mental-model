---
source: Local
owner: Owner
measures: Delivery
unit: hours
direction: lower
read-with:
  - Change Fail Rate
---

# Change Lead Time

> The time a change takes from being committed to version control to running in production.

## How it is measured

A deployment is a merge to `main` in a repository whose workflows publish one of this model's surfaces: the blust.ch website, which GitHub Pages publishes, and the mcp.blust.ch MCP server and the chat.blust.ch chat, which that repository's deploy and chat workflows publish. A merge counts once, however many of its workflows publish. The MCP Registry listing, republished when a release is tagged, and the LinkedIn profile, kept by hand, are not deployments.

For each deployment, the time from the earliest commit it carries that no earlier deployment carried to the moment it is live; a change to the model counts from its commit in robertblust/mental-model to the deployment of the re-pin that carries it. The value is the median over the deployments of a calendar month in UTC, read from the merges to `main` and their times in the GitHub history of robertblust/robertblust.github.io and robertblust/mcp-blust-ch, and from their publishing runs on `main` — GitHub Pages' own `pages-build-deployment` for the site, and mcp-blust-ch's `deploy` and `chat` workflow runs.

## What it can hide

It shortens when changes get smaller and when review gets thinner, and only the first is progress. Thinner review shows as a higher Change Fail Rate, which is why the two are read together. A median also hides the change that waited a week behind a re-pin.

## References

| What | URL |
| --- | --- |
| DORA's definition | https://dora.dev/guides/dora-metrics/ |
