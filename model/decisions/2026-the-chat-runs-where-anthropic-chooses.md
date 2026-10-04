---
id: 01a108dd-b337-75af-a13b-6676d83aca7f
source: Local
decided: 2026-10-04
kind: Data protection
status: Standing
by: Owner
---

# The chat's requests run where Anthropic chooses

> The chat lets the Anthropic API run each request in any geography it chooses, at the standard rate, and says so: a visitor's message may be processed outside the United States, and what Anthropic keeps of it is stored there.

## The question

Anthropic runs a request in any geography it chooses unless the request names the United States, which costs 1.1 times the standard rate. Naming it would make the country a visitor's message goes to exact; the question was whether that is worth the price.

## Alternatives

| Option | Why not |
| --- | --- |
| Name the United States on every request | It makes the country exact for a tenth more on every answer, and the chat's answers are not worth more because of it. |
| Claude on Vertex AI in a European region, beside the chat in Zürich | The project holds no Vertex quota for it, so it could not be run. |

## Why

The standard rate wins, and what is given up is said rather than hidden: the privacy page and the model name the United States as where Anthropic stores what it keeps, and say that the processing itself may happen elsewhere.

## Consequences

The deployment's chat.json names no region, so the Anthropic workspace's default, any geography, applies. The privacy page and the model's Anthropic page must not say that processing happens in the United States. The call is weighed again if the price of naming a region changes, if Anthropic offers a region closer to Switzerland, or if a visitor's data ever needs more than the chat holds today.

## Bears on

| Type | Entity | Owner | How |
| --- | --- | --- | --- |
| data-processor | Anthropic | | says its processing may happen anywhere |

## References

| What | URL |
| --- | --- |
| The deployment's chat configuration | https://github.com/robertblust/mcp-blust-ch/blob/main/chat/chat.json |
| Anthropic's data residency | https://platform.claude.com/docs/en/manage-claude/data-residency |
