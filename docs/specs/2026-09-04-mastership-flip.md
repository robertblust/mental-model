# The model masters itself — design

> The profile and 23 of the 24 experiences read `source: rob-cv` and were mastered in a private
> CV repository. That repository is archived. This records why the arrow was reversed, what the
> reversal decided beyond the field value, and the one rule it broke on the way.

> **Shipped, in `dc05391` and `0554be3`.** Every page reads `source: Local`, no page carries a
> `source-id`, and `model/sources/` holds one source. The correction in `0554be3` is the part
> worth reading: the flip rewrote a house rule into something narrower than the rule it
> replaced, and the narrowing was invisible until a claim it wrongly refused came along.

## Why the arrow was pointing the other way

rob-cv was written to generate tailored application dossiers, bilingual, from one set of facts.
The model was built from it, so the CV was the master and every page here was a copy — which is
why `AGENTS.md` said to correct a fact there first and copy it down, and why 23 experiences
carried a `source-id` pointing into its folders.

The role that repository was written to find starts on 1 October 2026. What it did — one source
of facts, many rendered forms — is work this model can carry itself, and rebuilding that on top
of the graph is a separate project that is deliberately not part of the model. So the CV is
archived, and an archived master is not a master.

## What the flip decided beyond the field value

**`source-id` goes, rather than staying as a trace.** The source schema says the field is the
page's identifier inside its source and is absent where the source issues none, “as a repository
does not”. Sixteen of the 23 differed from their filename — they were rob-cv's own ids, undated
because it filed projects and community entries in separate folders — so they pointed into a
tree that stops resolving. A field that claims a live pointer and has none is worse than no
field.

**Nothing about the content changed.** The prose here was already the copy. Only the direction
of the arrow was upstream, which is the whole reason this is written down: a reader finding
`source: Local` on every page has no way to see that it once did not, and every convention
around it was drafted while it pointed the other way.

**The `docs/specs/` entries that describe the old arrangement stay as they are.** Four of them
name rob-cv as the master. They are dated records of decisions made while that held, and
rewriting them would falsify the history rather than update it.

## The rule that narrowed by accident

`AGENTS.md`'s house style said “claim only what the CV states”. With the CV archived that
sentence had no referent, and the flip rewrote it as “claim only what something outside this
repository can confirm — a document, a record, a published page”.

That is not what the old rule meant. The CV was Robert Blust's own account of himself, so his
word was always the primary source and a document was the corroboration. The rewrite inverted that
without anyone noticing, because it reads like a tightening and tightening a rule about
invention feels safe.

It surfaced when a skill claim rested on Robert Blust describing his own practice, which the new
wording refused and the old wording had always allowed. The rule now reads “claim only what
Robert Blust states or a document shows”, and names what the guard is actually against:
invention by whoever is
editing, not first-hand testimony.

The finding is more general than the sentence. A rule whose referent is removed cannot simply be
reworded around the gap — what it meant has to be recovered first, and the recovery is not
obvious from the words that are left.

## When a document and the person disagree about the person

The mastership rule says a fact enters from Robert Blust or from a document. It does not say
what happens when the two conflict, and they did.

The January 2015 Zeugnis lists among his responsibilities “Erstellung einer Anwendungsarchitektur
zur Reduktion der Komplexität von Mengen von Punkt-zu-Punkt-Verbindungen mit Hilfe eines
Integrationsbusses”. A bullet was written from it. He removed it: he did not create that
architecture, he built the tooling that measured conformance to it, which the entry already
claims through the coupling metric and the source-code analysis.

His word governs, and the reason is not seniority. A Zeugnis is written by an employer
summarizing a role, often generously and at one remove from who did what; the person is the
only source that can distinguish the architecture from the tooling that checked it. So on a
claim about what he personally did, the document is evidence and he is the authority.

This is recorded because the document still says it. Anyone re-deriving the entry from the
Zeugnis will find that line, see no matching bullet, and take the model for incomplete. It is
not: the omission is a correction.
