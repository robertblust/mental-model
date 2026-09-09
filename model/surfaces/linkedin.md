---
source: Local
url: https://www.linkedin.com/in/robertblust/
---

# LinkedIn

> The professional network profile a recruiter, a client or a former colleague reaches first,
> kept by hand because the network takes no feed.

## What it shows

- **Headline** — the profile's tagline, cut to the limit below.
- **Location** — the metropolitan area the network's own list offers for the identity's
  `location`.
- **About** — the profile's `## Summary`, rewritten in the register this surface is read in.
- **Experience** — the experiences of kind `Role` and kind `Independent`, each with its period
  and a description drawn from the entry's `## Achievements`, and with its `organization` where
  the kind carries one: `Independent` carries none, because nobody commissioned the work.
- **Projects** — deliveries and open tools, each with a period and, where the entry carries a
  `url`, that address as the project's link.
- **Skills** — the names in the profile's `## Skills` table.
- **Top skills** — five names of the surface's own, each standing for a group of those skills.
- **Education** — the experiences of kind `Education`, each with its `organization` and period.
- **Volunteering** — the experiences of kind `Community` whose work was done for the host body
  rather than delivered to an audience at one of its events.
- **Languages** — the unit the network gives a language and a proficiency in it.
- **Publications** — the experiences of kind `Community` whose output is a written piece, with
  the entry's `url` as the publication's address.
- **Organizations** — the bodies those volunteering entries name in `organization`, each with
  the period of the tie.
- **Contact info** — the identity's `url` and the addresses in the profile's `## Also at`.

## Projection rules

- About is a rewrite of the profile's `## Summary` in this surface's register and never a copy
  of it: shorter sentences, and the point in the first one. The sentence naming the security
  and compliance standards is not carried there, because the LIKE MAGIC experience entry names
  those standards beside the work that met them, and the About text stands on its own, where a
  standard named without the work it belonged to is a claim the reader cannot place.
- The Projects unit is not the model's kind `Project`. It carries the deliveries the model
  holds as that kind and the open tools of the career break as well, which the model holds as
  kind `Community` because their audience is public and the audience is what that kind turns
  on. The unit and the kind are the same word for different sets, and this rule is what keeps
  them apart.
- A project entry carries one period. A delivery that ran inside another period is shown under
  that period's dates rather than its own, so that every date on the surface is still a date
  the model holds for the period the entry names.
- The Experience unit is fed from the experiences of kind `Role` and kind `Independent`, and
  from nothing else.
- The Volunteering unit is fed from the experiences of kind `Community` whose work was done for
  the host body, and from nothing else.
- An experience of kind `Community` reaches a unit by what its work was and not by its kind:
  the career break's open tools reach Projects, work done for a host body reaches Volunteering,
  a written piece reaches Publications. The kind covers several sorts of work, so it routes
  nothing on its own.
- A unit that shows a description takes it from the entry's `## Achievements`, whatever the
  experience's kind. Every experience in the model carries that section, so the Projects unit
  and the Experience unit draw from the same place and a project entry needs none of its own.
- Volunteering and Organizations are fed from the same entries and say different things about
  them: Volunteering carries what was done, Organizations carries the body and the period of
  the tie. A body that only hosted an event somebody spoke at reaches neither, because
  appearing at an event is not belonging to the body that ran it.
- Top skills is five names of the surface's own: Technology Leadership, AI Strategy &
  Governance, Context Engineering, Cloud & Platform Engineering, Business & IT Architecture.
  Each stands for a group of the model's skills rather than naming one of them, so a Top skill
  name is never added to the profile's `## Skills` table, and every skill it groups is one the
  profile claims at Proficient or above, because a Top skill is the shortest claim on the
  surface and the shortest claim is the one a reader tests first.
- The Skills unit carries no proficiency level. The surface shows a flat list of names, and a
  level beside a name the surface does not explain reads as a grade, so the level decides what
  a Top skill may group rather than appearing itself.
- The location unit takes the metropolitan area the network's list offers, not the identity's
  `location` verbatim, because the field is a list the surface chooses from and the model's
  value is a municipality the list need not carry.
- Contact info carries the model's addresses and none written for the surface. The `## Also at`
  row naming this surface is left out, because a surface that links to itself sends a reader
  back where they are, and the identity's `email` is left out, because the network carries its
  own messaging and a second address is a second inbox for the same request.
- The model's values and its vision reach no unit. The surface has no unit for a stated
  principle, and the About text is the only place one could go, where it would take the room
  that text has for the work the principle was held during.
- What decides which of the model's deliveries reach the Projects unit is open and the owner's
  to set. The unit takes a subset, nothing in this file chooses between them, and a rebuild has
  to ask.
- Whether the Projects unit widens to take an open tool from outside the career break is open
  and the owner's to decide. The model holds one — Flatland CDO Server, kind `Community`, with
  a public address — that the rule pairing the unit with kind `Project` and the career break's
  tools does not reach.
- Which of the model's skills each of the five Top skills groups is open and the owner's to
  set. The Top skills rule fixes the five names and the floor beneath them; what sits under
  each name is not fixed here.
- Which of the model's skills reach the Skills unit is open. The surface caps how many it
  takes, that cap has not been read off the editor and nothing here records it, so no floor is
  set and setting one is the owner's.
- Whether the model gains an experience for work of a sort it does not yet hold is open and the
  owner's to decide. Its experiences of kind `Role` and kind `Independent` are the professional
  record and it holds none beside them, so until it gains one a rebuild carries only what is
  there.
- Whether the model gains a volunteering period it does not yet hold is open and the owner's to
  decide. It holds none beside the `Community` entries the Volunteering rule names, so until it
  gains one a rebuild carries only what is there.
- Whether the Languages unit is filled or dropped is open and the owner's decision. The model
  types no language proficiency and the surface has the unit, so either the model gains the
  proficiencies or the surface drops the unit, and neither is decided here.
- How the surface carries a conference talk is open and the owner's to decide. The model holds
  a talk as kind `Community` with `end` equal to `start`, and neither the Volunteering unit,
  which takes work done for the host body, nor the Publications unit, which takes a written
  piece, is fed from one.
- Which unit takes an experience of kind `Community` that is neither a talk, an open tool, a
  written piece nor work done for a host body is open and the owner's to decide. Three of the
  model's entries answer to none of them: a case study a vendor published about the work rather
  than one written here, an episode published as audio on a newsletter, and a working-group
  seat held on an employer's behalf. One answers to two at once, an event co-organized and
  spoken at, and which unit takes that is open in the same way.

## Constraints

- Every unit that can travel on its own — the headline, a search result snippet, a share card —
  pairs the name with a role, a domain, a project or a location. The name is shared with a
  notable deceased academic, and a unit carrying the name and nothing else resolves to the
  wrong person.
- The headline is at most 220 characters, the network's limit, read from its editor on
  2026-09-09.
- The About section is at most 2600 characters, read from the same editor on the same day.
- Every dated entry carries as its title the H1 of the experience it was made from, and the
  dates it shows are that experience's `start` and `end`. An experience with no `end` is a
  period still running, and its entry shows the start and no end date. A project entry that
  carries a containing period, as the one-period rule directs, shows that period's title and
  dates instead.
- Every name in the Skills unit is a skill in the model, spelled as that skill's H1.
