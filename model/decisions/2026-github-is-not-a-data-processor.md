---
id: 01a108dd-a3f6-7a7c-a759-4b923c201e9d
source: Local
decided: 2026-10-04
kind: Data protection
status: Standing
by: Owner
---

# GitHub is not one of our data processors

> GitHub serves blust.ch's pages and sees the request that fetches each one, and we do not write it as a data processor: no processing agreement covers our account, and what GitHub keeps of a visit it keeps for its own purposes, so it is a recipient in its own right and not a party processing data on our behalf.

## The question

Core 0.60.0 gave this model the data-processor type, in the narrow meaning of GDPR Art. 4(8) and the Swiss DSG Art. 5 lit. k: a party that processes personal data on the company's behalf. The privacy page names GitHub as the host that sees each request, and the question was whether it is a data processor in that meaning.

## Alternatives

| Option | Why not |
| --- | --- |
| Write GitHub as a data processor, citing its data protection agreement | blust.ch is served by GitHub Pages from a personal account, which GitHub's Terms of Service govern and not the GitHub Customer Agreement the data protection agreement forms part of, so the page would cite a contract that does not cover it and claim a relation that does not exist. |
| Widen the data-processor type to every recipient | The type was decided narrow on purpose, and a type that holds both processors and independent controllers stops answering the one question the law asks of it: who acts on our instructions. |

## Why

GitHub logs every Pages visitor's IP address for security purposes, whether or not the visitor is signed in. That purpose is GitHub's, not ours, so for what it keeps of a visit GitHub is a controller in its own right, which is the kind of recipient the narrow type leaves out. Without an agreement that makes it our processor, writing it as one would be the model saying more than is true.

## Consequences

The model names no host for blust.ch's pages, and the privacy page keeps saying in its own words that GitHub serves them and sees each request. The call stays right for as long as the account holds no GitHub agreement that makes GitHub its processor; if it takes one, GitHub gets a data-processor page and this call is revised.

## Bears on

| Type | Entity | Owner | How |
| --- | --- | --- | --- |
| surface | blust.ch website | | keeps naming GitHub in its own prose |

## References

| What | URL |
| --- | --- |
| GitHub Pages and the visitor data it logs | https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages |
| GitHub data protection agreement | https://github.com/customer-terms/github-data-protection-agreement |
