---
source: Local
decided: 2026-09-27
kind: Spending
status: Standing
by: Owner
serves:
  - Every service I pay for is sized to what I use
---

# Google Cloud is capped at CHF 10 a month

> Google Cloud, which runs the MCP and chat hosts, may cost at most CHF 10 in a calendar month, watched by a budget that alerts at the cap.

## The question

What the hosting may cost, when so far it has cost nothing inside the free tier and would cost something the first month the traffic or a mistake took it past. It was decided with the other caps, when what each paid service may cost was written down for the first time.

## Alternatives

| Option | Why not |
| --- | --- |
| No budget, since the free tier covers it | The first month past the free tier would be found on the invoice. |
| A cap enforced by turning billing off | Turning billing off stops every host at once, which is a larger failure than the cost it prevents. |

## Why

The free tier makes the expected cost zero, so the cap is there for the unexpected month, and CHF 10 is low enough that an alert at it means something went wrong and high enough that a busy month does not raise it.

## Consequences

A Google Cloud budget alerts at the cap and does not stop spending, so the cap can be passed and Cap Use can read over the whole without an exception behind it; that reading is a finding to act on. The budget has to exist on the billing account for this call to be kept.
