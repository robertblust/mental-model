---
id: 01a0fe74-ba7f-71c8-bb56-9f4d558f8393
source: Local
kind: preventive
mode: automated
enforces:
  - A check counts only when its output was seen
  - A state is read again before it is relied on
---

# Main takes a change only through a green, current pull request

> The default branch of each of my repositories refuses a push, and takes a change only through a pull request whose named checks pass on a branch that is up to date with it.

## How it is carried out

GitHub's ruleset on each repository's default branch, on every attempt to change it: it refuses a direct push, a force push and a deletion, allows a pull request to be merged only with a merge commit where the repository says so, requires the named checks to pass, and requires the branch to be up to date with the default branch, so a pull request whose base has moved shows as behind until main is merged into it. The ruleset lets a repository admin bypass it.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| GitHub rulesets | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets |
