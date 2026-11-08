---
id: 01a17189-1188-744a-8207-1f5d23f472d6
source: Local
kind: SaaS
owner: Owner
processor: Google
serves:
  - Answering
---

# Sign in with Google

> Signs a reader in with their Google account when the reader chooses it on the login of id.blust.ch, and returns to id.blust.ch the account's id, its profile and its email address with Google's own flag for whether that address is verified; it opens no account of its own. When the reader signs in with it and the Google account is not yet linked, id.blust.ch's link check links it to the account the owner made for that address, but only where Google's flag proves the address and exactly one account at id.blust.ch holds it and has it verified; once linked, later sign-ins find the link. Where the link check makes none, the reader makes the link when they accept their invitation, or the owner makes it at their request.

## References

| What | URL |
| --- | --- |
| The vendor's documentation | https://developers.google.com/identity/openid-connect/openid-connect |
| How id.blust.ch is set up for it | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/google.tf |
| How id.blust.ch links it to an account by the address | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/link-check.tf |
