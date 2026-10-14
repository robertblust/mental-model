---
id: 01a13c3b-e14f-752b-b9db-56b6563a532c
source: Local
kind: preventive
mode: automated
enforces:
  - The Owner's word merges
---

# A release tag stays where the Owner put it

> Each of my repositories refuses a tag beginning with `v` that any account but the Owner's creates, moves or deletes, so a release exists only where the Owner tagged it and stays on the commit it was made on.

## How it is carried out

GitHub's ruleset `protect-release-tags` on each repository, on every push of a tag matching `v*`: it refuses its creation, its update and its deletion, and lets only the repository's admin role past, which is the Owner's account. A release is its tag and a consumer takes it by naming the tag, so a tag moved after it was taken would change what every consumer already holds; a release tagged wrongly is followed by a patch release and never moved. An agent working under the Owner's account passes it, so what holds an agent's tag to the Owner's word is An agent's permissions refuse a merge it was not given.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| GitHub's rulesets for branches and tags | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets#branch-and-tag-rulesets |
