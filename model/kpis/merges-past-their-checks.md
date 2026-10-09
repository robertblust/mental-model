---
id: 01a101e9-6374-7d23-8ab4-d3605dda358b
source: Local
owner: Owner
assesses:
  - Main takes a change only through a green, current pull request
unit: merges per week
direction: lower
read-with:
  - Change Fail Rate
---

# Merges Past Their Checks

> The merges that reached the default branch of a family repository in one week while a required check had not passed.

## How it is measured

GitHub records a rule suite with the result `bypass` each time a change reaches a default branch although a rule of its ruleset did not pass, which only an admin can do. Every Monday, the `kpi` workflow of robertblust/mcp-blust-ch reads the ISO week that ended, Monday 00:00 to Monday 00:00 UTC, across the family's repositories in robertblust with my GitHub App, which is installed on those alone, and classifies each bypass from its pull request. A merge counts here when a required check had not completed with success by the merge — still queued, running or failed — or when the change had no pull request, broke a rule other than the required checks, or could not be read. A merge whose branch was only behind main, with every required check passed, does not count. The week's object, `ruleset-bypasses/<year>-W<week>.json` in the bucket `kpi-reports-blust-ch-mcp`, holds this count as `past_checks`, beside `behind_main` and the total.

## What it can hide

A family repository the App is not installed on is never read, so a new one counts only once it is added to the installation. A repository with no ruleset is never evaluated, and a check that is not required does not count. A merge behind main is not counted although its checks ran against an older main. A required check that a path filter skipped counts as not passed although nothing was skipped on purpose. Where the App cannot read a ruleset's history, the required checks are counted from the rule suite at the merge, and a check required today but not then can, if it ran green, stand in for one that never started. Change Fail Rate, read beside it, shows whether these merges failed more often than the rest.

## References

| What | URL |
| --- | --- |
| The weekly workflow | https://github.com/robertblust/mcp-blust-ch/blob/main/.github/workflows/kpi.yml |
| Where the values are kept | https://console.cloud.google.com/storage/browser/kpi-reports-blust-ch-mcp/ruleset-bypasses |
| GitHub's rule suites | https://docs.github.com/en/rest/repos/rule-suites |
