---
id: 01a1713f-93a4-77e2-ae7c-46e9dfe5e912
source: Local
kind: Deployment
owner: Owner
processor: Google Cloud
serves:
  - Answering
---

# id.blust.ch

> Signs readers in to the chat on blust.ch, and to the chats on companygraph.io and guestgraph.io, with ZITADEL, the identity service the company runs at https://id.blust.ch in its Google Cloud project blust-ch-mcp in the Zurich region, where accounts are by invitation only, and issues the token from which each chat reads the models a reader may choose. Beside ZITADEL, in the same project and region, the company runs the link check, a small service of its own that ZITADEL calls after every sign-in with Google or Microsoft: it links that account to an existing one by its address only where the provider proved the address and exactly one account holds it with its address verified, and it keeps nothing and logs no address and no token.

## Connects to

| System | As | Service | Carries | Via |
| --- | --- | --- | --- | --- |
| Sign in with Google | OpenID Connect | | | HTTPS |
| Sign in with Microsoft | OpenID Connect | | | HTTPS |

## References

| What | URL |
| --- | --- |
| The service's source, infrastructure and the owner's steps | https://github.com/robertblust/id-blust-ch |
