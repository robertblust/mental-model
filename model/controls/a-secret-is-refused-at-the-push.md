---
id: 01a13c3b-e14f-74a9-add2-d57f91715839
source: Local
kind: preventive
mode: automated
enforces:
  - A secret is never written into a repository
---

# A secret is refused at the push

> GitHub refuses a push to any of my repositories that carries a secret it recognizes, before the secret is published, and scans what is already there for any that got in.

## How it is carried out

GitHub's secret scanning with push protection, turned on in each of my repositories one by one, since a personal account has no default that turns it on for a new one: on every push it looks for the shapes of keys and tokens its providers register, refuses the push that carries one and names the file and line, and it keeps scanning the history for any that reached a repository before. Whoever pushes may push past a refusal by giving a reason, that the secret is used in tests, is a false positive or will be fixed later, and GitHub then records an alert, writes the bypass to the audit log and emails the owners. It knows only those shapes, so a password someone made up, or a key in a form no provider registered, passes it; for those the rule rests on whoever writes the change.

## Applies to

| Type | Entity | Owner |
| --- | --- | --- |
| phase | Implement | Delivery |
| phase | Integrate | Delivery |

## References

| What | URL |
| --- | --- |
| GitHub's push protection | https://docs.github.com/en/code-security/concepts/secret-security/push-protection |
