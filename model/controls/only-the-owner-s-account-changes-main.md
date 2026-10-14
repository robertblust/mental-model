---
id: 01a13c3b-e14f-7b2a-ac60-5ef22adf037f
source: Local
kind: preventive
mode: automated
enforces:
  - The Owner's word merges
---

# Only the Owner's account changes main

> The default branch of each of my repositories takes a push or a merge from my account alone, because no one else holds write access to them.

## How it is carried out

GitHub's permissions on a repository under a personal account, on every push and every merge into it: such a repository takes a push only from its owner and the collaborators the owner invites, and mine invite none, so anyone else can fork a repository and open a pull request but cannot merge it. A personal account cannot restrict who may push beyond that, as an organization's branch protection can, so the day a collaborator is invited this control no longer holds. An agent working under my account passes it, so what holds an agent to the Owner's word is An agent's permissions refuse a merge it was not given.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| GitHub's permission levels for a personal account's repository | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository |
