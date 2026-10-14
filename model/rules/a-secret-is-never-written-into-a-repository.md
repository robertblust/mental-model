---
id: 01a13c3b-e14f-7f29-9337-6620a10a3531
source: Local
modality: must not
---

# A secret is never written into a repository

> No key, token or password is committed to any of my repositories, in a file, a commit message or a test fixture; a secret lives in the store of the workflow or the service that reads it.

## Why

Every repository I work in is public, so whatever is pushed is published the moment it reaches GitHub, and it stays in the history after a later commit removes it. A secret that reached a repository can only be rotated, never taken back, and everything it opened stays open until it is. For the same reason a secret is never printed, not even to check it: a value that reaches a transcript has to be rotated as well.

## References

| What | URL |
| --- | --- |
| Working rules | https://github.com/robertblust/conventions/blob/main/conventions/WORKING.md |
