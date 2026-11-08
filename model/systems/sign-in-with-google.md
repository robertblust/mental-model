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

> Signs a reader in with their Google account when the reader chooses it on the login of id.blust.ch, and returns to id.blust.ch the account's id, its profile and its email address with Google's own flag for whether that address is verified; it opens no account at id.blust.ch by itself. When the reader signs in with it and the Google account is not yet linked, id.blust.ch's link check links it to the account at id.blust.ch that holds that address, but only where Google's flag proves the address and exactly one account there holds it and has it verified; once linked, later sign-ins find the link. Where the link check makes none, the login offers the reader the form that opens an account of their own, whose address counts as verified where Google's flag proves it and is otherwise verified by the code the login mails there before the account is used; a reader the owner invited may instead make the link when they accept their invitation, and the owner makes it at a reader's request.

## References

| What | URL |
| --- | --- |
| The vendor's documentation | https://developers.google.com/identity/openid-connect/openid-connect |
| How id.blust.ch is set up for it | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/google.tf |
| How id.blust.ch links it to an account by the address | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/link-check.tf |
