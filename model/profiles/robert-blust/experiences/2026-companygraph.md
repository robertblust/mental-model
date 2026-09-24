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

### Context

- Extracted the meta-model from two instances that never knew about each other, a company of 25 people and a company of one, which had arrived at the same shape: one Markdown file per entity, YAML frontmatter and a body, in a folder named for its type, with a folder of schemas beside it.
- Came to it the second time. The Flatland CDO Server carried a model of a company from 2014, served over an API and true for as long as the server ran; this one is Markdown a person reads and edits, in a repository with a history, true for as long as the files exist.

### Leadership

- Published it under Apache 2.0 as open core with a billing model and a narrated introduction talk in German and English with a deck and a PDF in each, and put it in front of a professional network with a stated outcome each way.
- Put it up for validation in the open as one of two ideas: the meta-model, the graph of Markdown, the tooling with the server and the talks with the example are the open substance, and consulting is the one part that could ever earn; whether it will is the experiment.

### Engineering

- Published the core as one shipped unit — a schema per type and numbered conventions that make the graph checkable — with a worked example company and an instance parser, released by tag with a manifest per release.
- Built the reference instance from it: this profile, its experiences, its skills on a proficiency ladder and its values, every claim traced to an experience that shows it.
- Wrote an MCP server that serves any instance to an agent through read-only tools, every answer naming the model commit it was read from, and deployed it for the reference instance at mcp.blust.ch, listed in the MCP Registry, its name, description and instructions written from the model rather than by hand.
- Defined that deployment on Google Cloud in Terraform, planned on every pull request and applied by GitHub Actions on merge, with only a one-time bootstrap applied by hand.
- Gated the instance on the checks the meta-model ships as a reusable workflow, so a change that breaks a rule cannot merge.
- Made the deployment prove itself by calling a tool over the live endpoint, since the platform answers a health path on its own.
- Added a test that fails the build when the lockfile resolves an older release than the pin names, after a stale one had built green.
- Shipped the tooling inside the meta-model as one command that, run bare, opens a menu: it makes an instance that passes the checks on its first day, checks it, moves its vendored core to a newer release and installs the Obsidian plugin.
- Wrote the Obsidian plugin, which bundles the meta-model's own checker, so a page shows what breaks while it is edited and a new rule in core reaches the editor without code of its own.
- Described CompanyGraph in its own vocabulary as a second instance, the first with no person in it, drawn on companygraph.io and served at mcp.companygraph.io.
- Wrote a chat over any instance's MCP host that answers a visitor from what the tools return, naming and linking the entity each claim rests on, and put it on every prose page of blust.ch, companygraph.io and guestgraph.io.

### Ways of working

- Wrote the conventions for the agents that would work in an instance, encoding the failure modes seen before: an unresolvable reference is an error rather than a warning, and every validation pass names what it did not check.
- Wrote a reviewed specification before every plan and every build, for the meta-model, its tooling and this instance, so what was asked for was settled before an agent built it.
- Built it through the agent seats the model defines, each under its own rulebook and none of them deciding, with the Owner reviewing and merging.

## References

| What | URL |
| --- | --- |
| Chat server repository | https://github.com/companygraph/chat-server |
| MCP server repository | https://github.com/companygraph/mcp-server |
| Model repository | https://github.com/companygraph/mental-model |
| Obsidian plugin repository | https://github.com/companygraph/obsidian-plugin |
| Source repository | https://github.com/companygraph/meta-model |
