---
source: Local
owner: Owner
measures: Answering
serves:
  - Whoever decides about me decided from the model
unit: percent of questions per week
direction: higher
---

# Grounded Answer Rate

> The share of a week's questions to the chat whose answer rested on what the model's tools returned.

## How it is measured

Every message the chat accepted from a page of blust.ch leaves one line in the chat's log: the question, its language, the entities the answer cited, how many tool calls the answer made, how many of them found nothing, and whether the fence refused it. The answer itself is not kept. A question counts as answered when the fence did not refuse it and the model had material from the tools: an entity it cited, or more calls than found nothing, since a list answer names rows without citing one entity. A call found nothing when the host refused it, when it failed, or when it returned a list with no rows.

The weekly report reads the lines of the ISO week that ended, Monday midnight UTC to the next, and applies that rule; the value is the questions it counts as answered divided by all questions of the week, refused ones included. The rule lives in the report and not in the server that writes the line, so it can change while the lines stand.

## What it can hide

An answer that cites the right entity and says something wrong about it counts as answered: the rate measures whether the answer rested on the model, not whether it was true, and nothing kept can tell the two apart, because the answer is not kept. It rises when the model reads the identity entity for every question, since one cite is enough, so a week where every answer cites the same entity reads as well as one where each cites the entity the question was about; the report's table of most cited entities shows the difference. It falls when the fence refuses, for a spent share or a host that is down, which is the fence working and not the answer failing; the report's table of unanswered questions separates a refusal from an answer without material. A question that was not about the model, which the Answerer meets with one sentence and no tool, counts as not answered though it got the right reply.

## References

| What | URL |
| --- | --- |
| The kept line's fields and the rule for an answered question | https://github.com/companygraph/chat-server/blob/main/docs/INTERFACE.md |
| The weekly report that computes the value | https://github.com/robertblust/mcp-blust-ch/blob/main/.github/workflows/report.yml |
