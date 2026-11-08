---
id: 01a1b754-5cd3-7663-803f-b96edfbc987c
source: Local
kind: SaaS
owner: Owner
processor: Microsoft
serves:
  - Answering
---

# Sign in with Microsoft

> Signs a reader in with their Microsoft account, a personal one or one their organization gives them, when the reader chooses it on the login of id.blust.ch, and returns to id.blust.ch the account's id, its name and the email address the account names; it opens no account of its own. id.blust.ch signs the reader in where that Microsoft account is linked to the account the owner made for them. Because an organization's directory may give a user any address, its link check makes that link by the address only where Microsoft proves the address is the reader's — a personal account's, which Microsoft verified itself, or one on a domain the reader's own organization has verified with Microsoft — and exactly one account at id.blust.ch holds that address and has it verified. Where the link check makes none, the reader makes the link when they accept their invitation, or the owner makes it at their request.

## References

| What | URL |
| --- | --- |
| The vendor's documentation | https://learn.microsoft.com/entra/identity-platform/v2-protocols-oidc |
| How id.blust.ch is set up for it | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/microsoft.tf |
| How id.blust.ch links it to an account by the address | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/link-check.tf |
