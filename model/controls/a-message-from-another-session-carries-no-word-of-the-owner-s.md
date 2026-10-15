---
id: 01a13d69-0423-773e-ab3d-3ea3a261d170
source: Local
kind: preventive
mode: automated
enforces:
  - A refusal is not carried out by another session
---

# A message from another session carries no word of the Owner's

> A session that receives a message from another takes it as that session's and never as the Owner's, so a refusal one session met is not passed to another to carry out.

## How it is carried out

The agent harness, in every session that receives a message from another: it delivers the message marked as another session's and not as the Owner's, tells the receiving agent that such a message grants no permission and that a request to do what the sender was refused is to be declined and shown to the Owner, and its permission layer judges any action the message asks for against the receiving session's own conversation, where the Owner gave no word for it. The marking is how the agent harness delivers such a message, seen in its sessions and not in its documentation, and it rests on the agent heeding it; a session the Owner gives the word in, in its own conversation, may carry out what another was refused, because the word is then the Owner's.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| seat | Controller | |
| seat | Implementer | |
| seat | Surveyor | |

## References

| What | URL |
| --- | --- |
| The agent harness's permission modes | https://code.claude.com/docs/en/permission-modes |
