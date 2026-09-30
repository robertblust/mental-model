---
id: 01a0e179-0968-7ec4-8c77-b093fc507792
source: Local
owner: Owner
serves:
  - Every service I pay for is sized to what I use
unit: percent of cap per month
direction: lower
read-with:
  - Grounded Answer Rate
---

# Cap Use

> The highest share of its monthly cap that any metered cloud service spent in a calendar month.

## How it is measured

A metered service is one billed for what it used: an API billed per token, a platform billed per request, credits bought as they run out. Each has a cap, set by a decision of the Spending kind, and for each the month's spend is read from the provider's own billing page once the calendar month has closed. The service's share is that spend divided by its cap, and the value is the highest share among them, so one service over its cap shows even when the others are well under.

## What it can hide

A value over the whole means one of two things, a cap broken or a cap raised for a while by a decision, and the number cannot tell them apart; the decision that raised it can, and a reading over the whole is checked against the decisions standing that month. A cap enforced by the provider stops the service at the cap, so the value never passes the whole there, while the service itself stopped answering; reading it beside Grounded Answer Rate shows that, because a chat whose cap bit refuses questions and the rate falls. A cap only watched, by an alert that does not stop spending, can be passed, and a service running inside a free tier reads nothing until the month it leaves it. Taking the highest share hides a second service close to its cap behind the first.
