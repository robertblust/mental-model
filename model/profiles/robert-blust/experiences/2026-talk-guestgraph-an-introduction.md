---
source: Local
kind: Community
start: 2026-08
end: 2026-08
url: https://guestgraph.io/talks/intro/
role: Speaker
skills:
  - Public speaking
  - Storytelling
  - Data governance
---

# GuestGraph — an introduction

> A narrated talk that puts GuestGraph up for scrutiny: why a returning guest looks like five strangers, what a wrong merge costs, and how layered confidence keeps every decision explainable and reversible.

## Achievements

### Context

- Gave it as the talk on guestgraph.io, in August 2026: an idea presented for pushback rather than applause, to people who run hotels and the systems inside them, ending on four questions.

### Ways of working

- Kept the talk honest about what exists, in the speaker notes before the deck was built: the engine and one connector are there, nothing runs in production, there are no customers, and the slide says it shows a foundation and not a product.

### Sharing

- Opened on one guest: she books through a booking platform, checks in through the property system, eats in the restaurant, logs into the wifi and writes a review, five systems with five records and five keys, so the hotel has five strangers and nobody in the building notices.
- Pre-empted the obvious answer, matching on email, with where it breaks, a family sharing an address, a relay address from the booking platform, a changed provider, and named what a wrong merge is: one guest seeing another's invoices and stays, a data protection incident, which is why most do not dare try.
- Set out the design: the raw records from every system are left untouched, a correction arrives as a new record and never as an overwrite, and the golden profile is computed rather than stored, so it can be re-derived at any time; each layer decides only what it is entitled to decide, shared strong identifiers merge outright, probabilistic scoring merges only at a threshold the operator set, everything else goes to a person, and automatic probabilistic merging is off out of the box.
- Made trust the argument rather than technology: for every decision the full chain can be asked for, which matcher, how confident, on what evidence, when and by whom, and every merge can be undone with the correction sticking; an agent acting on guest data passes the same gates, thresholds, a review queue and reversibility, and the audit trail records whether a person or a named agent decided.
- Closed on the open core, Apache 2.0 for the engine and hosting, a console and MCP access as what could ever earn, with the reason stated: a black box that merges guests is not something I would deploy myself.
- Published it as a self-contained bilingual deck with a transport bar, narration recorded from the speaker notes in each language and a PDF of each.

## References

| What | URL |
| --- | --- |
| Deck as PDF, English | https://guestgraph.io/talks/intro/guestgraph-en.pdf |
| Deck as PDF, German | https://guestgraph.io/talks/intro/guestgraph-de.pdf |
