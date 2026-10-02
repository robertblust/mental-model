---
id: 01a0fd58-52d1-7c40-8ffc-388462da9aaf
source: Local
modality: must
protects:
  - Decide well over build fast
---

# A state is read again before it is relied on

> A state — a branch, a pull request, a check, a release, another session's work — is read again from its source in the conversation that relies on it; an earlier reading, or a session's transcript where the session can be asked, is not the state.

## Why

Several sessions and people move the same repositories at once. On October 2, 2026, main moved three times under one pull request in a morning, and a merge on an earlier reading would have failed its release check. Fetching main before a merge is this rule.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| role | Surveyor | |
| process | Deciding | |
| phase | Integrate | Delivery |
