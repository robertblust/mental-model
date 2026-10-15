---
id: 01a13d69-0423-7577-b12a-481bbd34838c
source: Local
kind: detective
mode: automated
enforces:
  - Nothing claims what the model does not hold
---

# A chat answer's claims are read back against the model

> Each claim of an answer the chat gives on blust.ch is read back against the tool answers it rests on, and the chat marks one they do not carry before the visitor takes it for what the model says.

## How it is carried out

The chat server behind blust.ch, on every answer once it is written: it sends each claim, with the tool answers the chat's model was given, to TypeSafe's Jev, which returns a verdict and its probability and writes no text, and the widget marks a claim whose verdict is that the evidence does not carry it, above the threshold this deployment's configuration sets. Only an answer written in English is marked; a German one is checked and its verdicts kept until German has a threshold of its own. The check changes no word of the answer, and a check that cannot run, or does not finish within its budget, marks nothing. It holds the chat's answers and nothing else: a specification or a page someone writes is held to the rule by whoever writes it.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Answer | Answering |

## References

| What | URL |
| --- | --- |
| The claim check | https://github.com/companygraph/chat-server/blob/main/lib/verdict.mjs |
| This deployment's configuration | https://github.com/robertblust/mcp-blust-ch/blob/main/chat/chat.json |
