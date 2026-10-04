---
id: 01a108dd-c2b7-7d88-b4b4-352c9a1e84b4
source: Local
decided: 2026-10-04
kind: Data protection
status: Standing
by: Owner
---

# blust.ch's privacy page is built from the model

> The privacy page on blust.ch is built from this model's data processors, processing activities and stored items, at the pinned commit the site draws, so what the page names is what the model holds and a correction is made once, in the model.

## The question

Core 0.60.0 gave the model types for what a privacy page discloses, and the page had drifted from what the site and the chat do: it named neither Google Cloud, which runs the chat and keeps its questions, nor the chat-facts key, and still said that everything stored was listed. Either the page is corrected by hand and kept in step by hand, or it is built from the model.

## Alternatives

| Option | Why not |
| --- | --- |
| Correct the page by hand now and keep it in step by hand | That is how it drifted: the facts were written in the page and in the code, and nothing compared them. The model would be a third copy to keep in step. |
| Leave the page as it is and keep the model as the record | A visitor reads the page and not the model, so the page would go on telling them less than the company knows. |

## Why

The model is the master: a page built from it cannot name less than the model holds, and a fact corrected in the model reaches the page on the next build. The site already builds its model pages from a pinned commit of this model, so the privacy page joins a build that exists rather than starting one.

## Consequences

The site gains a build for the privacy page from the processors, activities and stored items at its pinned commit; the prose around them stays written by hand. Until that build exists the page stays out of step with the model, without Google Cloud and the chat-facts key. The call stays right for as long as every key a surface sets and every party that receives a visitor's data has a page in the model.

## Bears on

| Type | Entity | Owner | How |
| --- | --- | --- | --- |
| surface | blust.ch website | | its Privacy page is built from the model |

## References

| What | URL |
| --- | --- |
| The privacy page | https://blust.ch/privacy/ |
| The rule that the model is the master, R17 | https://github.com/companygraph/meta-model/blob/main/core/CONVENTIONS.md |
