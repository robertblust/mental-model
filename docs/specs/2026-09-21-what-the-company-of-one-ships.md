# What the company of one ships — proposal

> Core gave a company types for what it ships and for the words it means exactly, and CompanyGraph's own instance has filled them. This instance vendors the same core and writes none of the four. This proposes what a company of one puts in them, entry by entry, each with the case against it, and nothing here is decided until the owner has gone through it.

Status: proposed on 2026-09-21, for review. The entities it proposes are on the same branch, under `model/domains/`, `model/products/`, `model/features/` and `model/concepts/`, so each can be read as it would stand and the checker has already run over them. An entry the owner declines is deleted from the branch; nothing is merged ahead of that.

## The question underneath

A product is “something the company ships that somebody uses on its own”, and the schema wrote that sentence with a company of many in mind. For a company of one the question is which thing that is, and there are three honest readings. The rest of the proposal follows from which one is taken, so it is the first decision.

**Reading A: the product is the Mental Model.** What this company puts in front of people is the account of its work. The vision says so in its own words — one model, and every surface derived from it — and the strategic objective names who uses it: whoever decides about me, and the search engine or agent they ask. The glossary already fixes the name, Mental Model, as a coined name for the owner's knowledge base. Its features are what a reader can do with it: check a claim against its evidence, read the career in order, ask an agent, read it on the web, carry it into a conversation. This is the reading CompanyGraph's instance took for itself, where the product is the vocabulary the instance is written in.

**Reading B: the products are GuestGraph and CompanyGraph.** The home page says “Two ideas have come out of that, and I am building both in the open”, the career break says “two products”, and the ideas page already lays each out as numbered parts that read like features. The case against is the rule this model exists for. CompanyGraph's product and features are mastered in `companygraph/mental-model`, and a second set here would be a second master that goes stale without a sound, which is the reason that instance gives for describing no person. GuestGraph has no instance of its own yet, and when it gets one the same holds. The parts on the ideas page also carry a state, built or planned, and the product schema rules that out: nothing about a release or a roadmap. In this model the two are experiences, which is what they are from here: work I did.

**Reading C: the product is the work for hire.** Technology leadership and business architecture, sold as help. The case against is that the skills already say what I can do, with a level and evidence under each, and a product per capability would restate them with the evidence taken away. From October the work is also an employed role, and what the model does not claim it does not imply.

**Proposal: reading A, alone.** B's products are pointed at and not copied: the two experiences carry their addresses, and CompanyGraph's instance is where its product is read. What would change this: if the ideas page is one day to be drawn from a model instead of written by hand, it should read CompanyGraph's instance for CompanyGraph and an instance of GuestGraph's own for GuestGraph, and that is a decision about the site and not about this repository.

## The domain

**Portfolio.** One domain, holding the product and every concept. Its tagline covers the account of my work and the words I mean exactly when I give it, and leaves out what a model is made of — entity, type, reference, pin — which is CompanyGraph's vocabulary and sits in its Core domain, and how the work gets made, which the conventions hold.

The case against one domain: the schema asks a domain to name what it leaves “to another domain”, and the other domain here is in another instance, where no reference from this one can reach it. CompanyGraph's Core does the same when it leaves things to packs, so there is precedent, and the honest alternative, a second domain here with nothing in it, would be worse.

The case against the name: “Portfolio” is the README's word (“the whole professional portfolio”) and not one the pages use. “Career” is narrower than what the model holds, since the values and the vision are not career. “Work” is the vision's word (“The scope is the work”) and is the alternative I would take second. The owner's choice.

A second domain was considered and is not proposed: the vocabulary of how the work is made — brief, specification, plan, gate, seat, rulebook. Each of those words is already defined where it is used, in a phase's deliverables table, in a role's file or in the conventions, and a concept beside each would be the second copy the strategy rules out.

## The product

**Mental Model.** The tagline is built from the vision's own list, what I have built, the capabilities I claim with their evidence and what I hold to, and then names who opens it: whoever is deciding whether to work with me, and the search engine or the agent they ask instead. No `audience` is set, because with one product there is nothing to group.

The case against: a model that lists itself as its own product is circular, and the surfaces already say where it is published. The answer is that a surface is a place and its rules, and none of them is the thing itself; today the model can say where it is shown and cannot name what is being shown. It is also the only way a feature can exist here, since a feature must name a product.

The name is shared with the concept proposed below. The product schema expects that (“where a concept of the same name exists”), typed resolution keeps the two apart, and the parser blust.ch pins was run over the branch to confirm it: a feature's `products` reaches the product and its `concepts` reaches the concept.

## The features

The hazard with features here is that they turn into the surfaces folder told twice. The line drawn is the one CompanyGraph's instance draws: a feature says what someone can do and where that stops, and it hands the place, its rules and its build to the surface by name. Some of the features are about what the model holds, and the others about how it is reached.

**A claim is checked against its evidence.** What it says: every claimed skill carries a level and at least one row of evidence, experiences link their public documents, and it stops at what can be shown in public and gives no verdict. The case against: this is core's profile schema described again. The answer is that the schema says what a profile must carry, and the feature says what a reader gains from it and where it stops, which is the private documents; that boundary is this instance's own decision, from `AGENTS.md`, and nothing a reader of the model can find today says it to them. Proposal: keep.

**A career is read in order.** What it says: each period is an experience with dates, kind, achievements and an ending, and it stops at what happened, leaving capability to the evidence rows. The case against: it is the thinnest of them, and close to a description of the experience type. It earns its place by its boundary with the first feature, which is the rule that a period's dates and facts are not repeated as evidence. Proposal: keep, and the first one to drop if there are too many.

**An agent answers from the model.** What it says: an agent asks over MCP and every answer names its commit, read-only. It stops at this model: the server is CompanyGraph's feature, An agent reads the model, and the deployment is the mcp.blust.ch surface. The case against: once the server and the surface are taken away, little is left that is this company's. What is left is the decision to be answerable this way, which is the objective's own test, the same answer from a person, a search engine and an agent. Proposal: keep.

**The model is read on the web.** What it says: anyone reads the work in a browser in two languages, the pages are drawn from one pinned commit, the parsed model is a file anyone may fetch, and the talks and the ideas page are named as not part of it because they are written by hand. The case against: it overlaps the blust.ch website surface most of all. It follows CompanyGraph's The vocabulary on the web in form and in where it stops. Proposal: keep. One thing to confirm: that “written by hand” is how the owner wants the talks and the ideas page described in the model.

**The model is carried into a conversation.** What it says: the model is exported as a skill bundle and a notebook bundle, each held to being the model whole, handed out on request, and as old as the export. The case against: the surfaces README says handing out is not publishing, which is why neither bundle has a surface, and a feature might look like a way around that decision. It is not one: a feature is something someone can do, and someone can do this; what they cannot do is find it published, and the description says so. It names no vendor, as the schema asks. Proposal: keep.

Not proposed as features: the per-application dossiers, because the tooling is retired and a feature nothing ships is a plan; and the LinkedIn profile, because it lets a reader do nothing the features above do not already say, and it has a surface.

## The concepts

These are the words `AGENTS.md`, the vision, the objective and the glossary already use with an exact meaning, and each definition is taken from the sentence that uses it. The ontology is small on purpose. Most of the value is a definition a feature can cite and an alias a searching reader can land on, and the relations are few because few are true.

**Claim** — a skill at a level that a profile asserts, standing only with something concrete under it. Alias Anspruch, the glossary's German. One relation, to Evidence, one to many, which is the rule the instance checks already hold. The case against: core's profile schema defines a claim already. No concept file anywhere does, the vision rests on the word, and the glossary fixed its German because pages needed it.

**Evidence** — one sentence naming a thing done, concrete enough to check. Alias Beleg. No relations: the edge is written once, on Claim. Same case against, same answer.

**Document** — what a fact rests on outside the model, linked where public and kept out where private. Alias reference, as a synonym, so a reader searching that word lands here. The case against the alias: in Switzerland “reference” first means an employment reference, which is one kind of document and not all of them. Proposal: keep the concept, and the owner decides the alias.

**Own account** — what I say of my work from having done it, which enters as a fact and not as a claim awaiting a source. Alias first-hand testimony, the phrase `AGENTS.md` uses. The case against: it is one rule of one file promoted to a concept. It is also the rule an outside reader is most likely to get wrong about this model, since they will assume every fact needs a link, and the model page already says “my own account of my work” to head that off.

**Master** — the one place a fact is corrected. Aliases source of truth and mastership. The case against: core's `source` type covers the same ground, and its one entity here is Local. The type says where a page is mastered; the concept says what being the master means, which is what the vision's “derived rather than maintained” depends on. The weakest of the concepts, and the first to drop.

**Decider** — someone deciding whether to work with me, a client or an employer. The objective's word, used there without a definition. No aliases, no relations. The case against: it is an audience, and the product schema leaves open whether an audience becomes an entity. As a concept it commits to nothing about that.

**Company of one** — one person described as a company would be, the work as the whole scope and private life outside it by design. The identity's phrase and the glossary's. The site's German for it is on the model page, and is not proposed as a translation alias because the glossary has not fixed it.

**Mental Model** — the written model of a company that people and agents both read; mine describes a company of one. Aliases knowledge base, the glossary's and the talk's word, and instance, CompanyGraph's word for the same thing, whose own Instance concept lists “mental model” as a synonym in return. Relations: Company of one, one, as described company; Master, one; Claim, many. The case against: CompanyGraph's instance defines Instance, and this is a second definition of a near thing in a second instance. The two are not the same word: Instance is defined by what the repository holds, core at a release beside the company's pages, and Mental Model by what it is for. If the owner reads them as one thing, this concept goes and the product keeps the name alone.

Considered and not proposed: Level, Experience and Surface, because each is a core type with entities or a schema that already defines it; Seat, Brief, Specification, Plan and Gate, for the reason given under the second domain; and Essential complexity and the other words the talks argue for, because the values hold those positions and a concept would restate a value as a definition.

## What a merge would cost downstream

Nothing moves until a consumer re-pins. blust.ch reads the model at the commit `source.json` names, and its pinned parser was run over this branch: it reads the four types and their edges with no change, so a re-pin would draw them on the model page without a parser release. The model page's “What is in it” prose, in both languages, lists what the model holds and would then owe a sentence, which is a Writer's and a Translator's job on that repository. mcp.blust.ch serves whatever types the instance declares and would list the four after its own re-pin. The export was run over this branch and carries the four folders in both bundles; its `verify.py` could not run there, because it looks for the bundle under the clone's folder name and a worktree has another, which is a finding about the script and not about this change. The README's tree gains the four folders on this branch. `AGENTS.md` is left alone: its opening describes the instance by its profiles and what they claim, and that stays true.

## How to review this

Entry by entry, as every editorial change here is made: the reading first, because the rest depends on it; then the domain and its name; then the product; then each feature and each concept in the order above. For each, keep, reword or drop, and the branch follows. If reading A itself is declined, the entities go and this document stays as the record of what was weighed.
