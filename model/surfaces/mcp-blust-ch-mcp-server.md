---
source: Local
production: built
built-by: https://github.com/robertblust/mcp-blust-ch
url: https://mcp.blust.ch
---

# mcp.blust.ch MCP server

> The server an agent connects to for answers about the owner's work, and the page a person
> reaches at the same address, reading a pinned commit of the model and adding nothing to it.

## What it shows

- **Endpoint** — `/mcp` on this address, the only path that speaks the protocol and the one a
  client is given. The registry listing's remote is this.
- **Title** — the identity's name.
- **Instructions** — the vision's tagline and the identity's tagline, then one sentence saying
  that every answer names the commit it was read from, and no commit of their own.
- **Tools** — listing the types, describing a schema, what the types declare about each other,
  the rules the model is held to, listing and returning entities, finding evidence, searching
  and fetching, over every entity in the model.
- **Page** — what a browser gets at the server's own address, for a reader who arrived at a
  protocol endpoint without a client: the identity's name, the vision's and the identity's
  taglines, the address to give a client, every tool with what it returns, and the commit the
  answers are read from.
- **Structured data** — the person and the endpoint that the page describes to a crawler, with
  the person's addresses from the profile's `## Also at`.
