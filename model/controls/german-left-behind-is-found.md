---
id: 01a0fe74-e6af-76a7-a319-db623e7edf44
source: Local
kind: detective
mode: automated
enforces:
  - German follows reviewed English
---

# German left behind is found

> A site's pull request fails where an English edit left its German unchanged, unless a commit says the German is right on purpose.

## How it is carried out

The site's CI, on every pull request: `design german stale` compares the change with its base and fails for each element whose English moved while its German did not; a commit that names the element in a `German-unchanged:` trailer releases it.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| blust.ch's CI | https://github.com/robertblust/robertblust.github.io/blob/main/.github/workflows/ci.yml |
| The German stale check | https://github.com/robertblust/design#readme |
