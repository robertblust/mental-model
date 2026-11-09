---
id: 01a1bfd6-9eaa-77d8-b4e8-3d0a588f049d
source: Local
kind: SaaS
owner: Owner
processor: GitHub
serves:
  - Answering
---

# Sign in with GitHub

> Signs a reader in with their GitHub account when the reader chooses it on the login of id.blust.ch, and returns to id.blust.ch the account's id, its login, its name and one email address of the account, the public one on its profile or else its primary verified one; it opens no account at id.blust.ch by itself. id.blust.ch signs the reader in where that GitHub account is linked to an account there. Because id.blust.ch's identity service counts every address GitHub returns as verified without GitHub saying so, id.blust.ch's link check makes that link by the address only where the account's own list of addresses at GitHub holds it as verified, and exactly one account at id.blust.ch holds that address and has it verified. Where the link check makes none, the login offers the reader the form that opens an account of their own, whose address counts as verified where GitHub proved it and is otherwise verified by the code the login mails there before the account is used; while the link check cannot answer, a new account's address counts as verified as the identity service took it, and nothing is linked.

## References

| What | URL |
| --- | --- |
| The vendor's documentation | https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps |
| How id.blust.ch is set up for it | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/github.tf |
| How id.blust.ch links it to an account by the address | https://github.com/robertblust/id-blust-ch/blob/main/zitadel/link-check.tf |
