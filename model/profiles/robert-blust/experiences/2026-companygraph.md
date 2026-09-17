---
source: Local
kind: Community
start: 2026-08
url: https://companygraph.io
skills:
  - Agentic AI development
  - Context engineering
  - Knowledge management
  - Model-driven engineering
  - Data modeling
  - Spec-driven development
  - Technical writing
  - Open-source stewardship
  - Product discovery
  - Company vision and strategy
  - Public speaking
  - AI tool integration (MCP)
  - Infrastructure as code
  - CI/CD
---

# CompanyGraph

> Ongoing. A meta-model for describing a company as a graph of Markdown files, so people and AI agents can both rely on it.

## Achievements

- Extracted the meta-model from two instances that never knew about each other, a company of 25 people and a company of one, which had arrived at the same shape: one Markdown file per entity, YAML frontmatter and a body, in a folder named for its type, with a folder of schemas beside it.
- Published the core as one shipped unit — a schema per type and numbered conventions that make the graph checkable — with a worked example company and an instance parser, released by tag with a manifest per release.
- Wrote the conventions for the agents that would work in an instance, encoding the failure modes seen before: an unresolvable reference is an error rather than a warning, and every validation pass names what it did not check.
- Built the reference instance from it: this profile, its experiences, its skills on a proficiency ladder and its values, every claim traced to an experience that shows it.
- Wrote an MCP server that serves any instance to an agent through read-only tools, every answer naming the model commit it was read from, and deployed it for the reference instance at mcp.blust.ch, listed in the MCP Registry.
- Defined that deployment on Google Cloud in Terraform, planned on every pull request and applied by GitHub Actions on merge, with only a one-time bootstrap applied by hand.
- Gated the instance on the checks the meta-model ships as a reusable workflow, so a change that breaks a rule cannot merge.
- Made the deployment prove itself by calling a tool over the live endpoint, since the platform answers a health path on its own.
- Added a test that fails the build when the lockfile resolves an older release than the pin names, after a stale one had built green.
- Wrote a reviewed specification before every plan and every build, for the meta-model, its tooling and this instance, so what was asked for was settled before an agent built it.
- Built it through the agent seats the model defines, specifier, planner, controller, implementer, reviewer, writer and translator, each under its own rulebook and none deciding, with the Owner reviewing and merging.
- Came to it the second time. The Flatland CDO Server carried a model of a company from 2014, served over an API and true for as long as the server ran; this one is Markdown a person reads and edits, in a repository with a history, true for as long as the files exist.
- Published it under Apache 2.0 as open core with a billing model and a narrated introduction talk in German and English, and put it in front of a professional network with a stated outcome each way.

## References

| What | URL |
| --- | --- |
| MCP server repository | https://github.com/companygraph/mcp-server |
| Source repository | https://github.com/companygraph/meta-model |
