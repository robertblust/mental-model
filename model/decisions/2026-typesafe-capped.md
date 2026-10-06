---
id: 01a10f86-dcc4-7975-a987-f0b3b7488f49
source: Local
decided: 2026-10-06
kind: Spending
status: Standing
by: Owner
serves:
  - Every service I pay for is sized to what I use
---

# TypeSafe is capped at USD 5 a month

> TypeSafe, which checks the chats' answers and judges my pages against their writing rules, may cost at most USD 5 in a calendar month, paid from credits bought in advance with no automatic top-up.

## The question

What checking may cost, on a service billed per token and paid from credits bought before they are spent. Two things spend the same credits: every chat answer the check reads, and every judge run I start on the model. It had to be decided once both were in use, because the caps decided before named every metered service but this one.

## Alternatives

| Option | Why not |
| --- | --- |
| No cap, since it costs cents | A metered service with no amount decided is what the objective rules out, however small the bill. |
| Count it under the Anthropic API cap | It is another provider with its own bill, and a judge run is not the chats answering visitors. |
| Credits topped up automatically | Spending would follow the balance, and a month past the cap would show on the card before anything stopped it. |

## Why

A full judge run of this model costs a few cents and the check of a chat answer far less, so USD 5 a month holds a month of development as well as a month of visitors, and a month that reaches it means something ran that should not have. Credits with no automatic top-up stop the service when they run out, and every new purchase is one I make.

## Consequences

The cap is kept by me and read from the provider's usage export once the month closes; the credits stop spending only when the balance is gone, which can be months past a broken cap. When they run out, every chat still answers and nothing it says is checked: the widget marks no claim, and the only trace is a warning in each chat's request log. A top-up is a purchase I make, and a month that needs more than the cap is a new decision before it, not a finding after it. It stays right while a month of checking costs well under the cap; a check that reads more per answer, or a price that rises, raises it by a new decision.
