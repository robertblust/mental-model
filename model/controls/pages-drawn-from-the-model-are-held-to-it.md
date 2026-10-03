---
id: 01a0fe74-d886-7d67-9f52-b610af38f5e3
source: Local
kind: detective
mode: automated
enforces:
  - The model is corrected first
---

# Pages drawn from the model are held to it

> A site's pull request fails where a page drawn from the model differs from what the model, at the commit the site pins, would draw.

## How it is carried out

The site's CI, on every pull request: `model:check`, `pages:check` and `build:check` run each writer that draws from the pinned model and fail where the committed output differs, so a page edited by hand, or one the model no longer produces, cannot merge until the model is corrected and the page drawn again.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| blust.ch's CI | https://github.com/robertblust/robertblust.github.io/blob/main/.github/workflows/ci.yml |
