---
id: 01a0fe74-c963-7a42-b821-190fc35cdfae
source: Local
kind: preventive
mode: automated
enforces:
  - The Owner's word merges
---

# An agent's permissions refuse a merge it was not given

> The permission layer an agent runs under refuses a merge the agent attempts without the Owner's word for it in that conversation.

## How it is carried out

Claude Code's permission layer, before the agent's command runs: it judges the action against the conversation, and a merge without a review it can see is refused, so the agent stops and the merge waits for the Owner. On October 2, 2026 it refused the merge of meta-model #223, which the Owner then gave in another session.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| seat | Controller | |
| seat | Implementer | |
| seat | Surveyor | |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| Claude Code permissions and auto mode | https://code.claude.com/docs/en/permissions |
