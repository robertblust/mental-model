---
id: 01a13c3b-e14f-7bb9-851d-f1819fa21865
source: Local
kind: detective
mode: automated
enforces:
  - A state is read again before it is relied on
---

# A deployed server is asked which commit it serves

> After every deploy of mcp.blust.ch the run asks the live server which commit of the model it answers at, and fails unless it is the commit the repository pins.

## How it is carried out

The deploy job that mcp.blust.ch's workflow calls from the MCP server, on every push to main, once Terraform has applied: it calls the live server's own `list_types` tool, reads the commit every answer names under `model`, and fails unless it is the commit `source.json` pins. A deploy that applied cleanly but left an earlier revision serving, or one built from another commit, then turns the run red instead of reading as done.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| The deploy job and its check | https://github.com/companygraph/mcp-server/blob/main/.github/workflows/deploy-google.yml |
| The workflow that calls it | https://github.com/robertblust/mcp-blust-ch/blob/main/.github/workflows/deploy.yml |
