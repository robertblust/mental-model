---
source: Local
production: built
built-by: https://github.com/robertblust/mcp-blust-ch
url: https://chat.blust.ch
---

# chat.blust.ch chat

> The chat a visitor opens on blust.ch to ask about the owner's work, answered from what the mcp.blust.ch MCP server says at its pinned commit, and the page a person reaches at the same address.

## What it shows

- **Endpoint** — `/chat` on this address, which a page of blust.ch posts a visitor's conversation to and which answers it as a stream of events.
- **Answer** — the text a language model writes from what the MCP server's tools returned for the visitor's question, in the language of the visitor's message, naming the entity each claim rests on.
- **From the model** — a link to each entity a tool returned on its own, opening it on the model page of blust.ch.
- **Refusals** — the sentences a visitor reads instead of an answer when the day's or the month's share is spent, when one address has sent too many messages in an hour, when the host does not answer or when the chat is switched off.
- **Page** — what a browser gets at the chat's own address: the host's name, the vision's and the identity's taglines, the paths and the events the endpoint answers, the fence that bounds what it spends, and the commit of the model it answers from.
