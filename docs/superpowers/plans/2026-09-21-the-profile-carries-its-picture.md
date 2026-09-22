# The profile carries its picture implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** The reference instance takes core 0.38.0, and Robert Blust's profile names his picture, a file beside the profile's own.

**Architecture:** `companygraph upgrade` at meta-model v0.42.0 re-vendors `meta/core/` with fresh hashes and moves the instance's pin in all three of its places together: the vendored core, `tooling` in `.companygraph/manifest.json` and the `instance-check.yml@` line of the workflow. The picture is one file, `model/profiles/robert-blust/robert-blust.jpg`, and one frontmatter line, `image: robert-blust.jpg`. The checker holds the file from its own bytes: a JPEG that is what its name says, square, 256 to 1024 pixels on a side and at most 300 KB.

**Tech Stack:** Markdown, the `companygraph` CLI run through `npx`, the instance check in CI.

**Spec:** `docs/superpowers/specs/2026-09-21-a-profile-carries-an-image-design.md` in companygraph/meta-model.

Both tasks were run once on a scratch clone of `main` at 463ff66 with meta-model v0.42.0: the upgrade wrote five files and said `core 0.37.0 → 0.38.0`, and with the owner's photo in place the check said `✓ model/ against meta/core/ at core 0.38.0: the mechanical checks pass`.

## Global Constraints

- **The Obsidian plugin goes first.** The plugin refuses a vault whose core is newer than the checker it bundles, and the release the owner runs bundles checker 0.41.0 with core 0.37.0. The moment this merges and his vault pulls it, the plugin's checks stop with “take a plugin release that bundles 0.38.0 or newer”. So this is merged only once a plugin release that pins meta-model v0.42.0, and reads a vault's images as bytes, is installed in his vault — or on his word that he accepts the gap.
- **Nothing else that reads this model breaks.** blust.ch and mcp.blust.ch pin a commit and move when they are re-pinned; neither runs the instance checks over the model. The Python export skills read `*.md` only.
- **The photo is the owner's**, `~/Desktop/robert-blust.jpg`: 1000 by 1000, 159,462 bytes, a JPEG. It is copied as it is, never resized or re-encoded by an agent; if he names another file, that one is used and checked the same way.
- **Branch and worktree:** `the-profile-carries-its-picture`, in `~/git/robertblust/mental-model-the-profile-carries-its-picture`, which holds this plan.
- **`export PATH=/opt/homebrew/bin:$PATH`** before `node`, `npx` or `gh`. A push names the credential helper: `git -c credential.helper='!/opt/homebrew/bin/gh auth git-credential' push -u origin the-profile-carries-its-picture`.
- **Before every commit, the `companygraph-validate` skill**, as this repository's `AGENTS.md` requires, and the diff read for digits that still move.
- **Never commit on the default branch.** Merging waits for the owner's word.
- **Commit messages** follow the git register, ending with a `Verified:` line and the trailer `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.

---

### Task 1: The instance takes core 0.38.0

**Files:**

- Modify: `.companygraph/manifest.json`, `.github/workflows/companygraph.yml`, `meta/core/CONVENTIONS.md`, `meta/core/manifest.json`, `meta/core/profile-schema.md` (all written by the tooling, none by hand)

- [ ] **Step 1: Upgrade**

```bash
export PATH=/opt/homebrew/bin:$PATH
cd ~/git/robertblust/mental-model-the-profile-carries-its-picture
npx --yes 'github:companygraph/meta-model#v0.42.0' upgrade --dry-run
npx --yes 'github:companygraph/meta-model#v0.42.0' upgrade
git status --short
grep -n '"tooling"\|"version"' .companygraph/manifest.json | head -2
grep -n "instance-check.yml@" .github/workflows/companygraph.yml
```

Expected: `core 0.37.0 → 0.38.0: 5 written, 0 removed`, then `✓ … the mechanical checks pass`; exactly the five files above modified; `tooling` `0.42.0`, core `0.38.0`, and the workflow at `@v0.42.0`. All three places moved, which is the thing to read: a half-moved pin is refused by the checker only on the next run.

- [ ] **Step 2: Validate and commit**

Run the `companygraph-validate` skill. Commit the five files with a message saying the instance takes core 0.38.0, that the release adds the `image` type and the profile's optional field, and that no page of this model changes with it.

---

### Task 2: The profile names the picture

**Files:**

- Create: `model/profiles/robert-blust/robert-blust.jpg`
- Modify: `model/profiles/robert-blust/robert-blust.md` (one frontmatter line)

- [ ] **Step 1: See the check refuse the field without its file**

Add `image: robert-blust.jpg` as the last frontmatter line of `model/profiles/robert-blust/robert-blust.md`, after the `roles` list:

```yaml
roles:
  - Owner
image: robert-blust.jpg
---
```

Run: `npx --yes 'github:companygraph/meta-model#v0.42.0' check .`

Expected: one problem, `` model/profiles/robert-blust/robert-blust.md: `image` names robert-blust.jpg, and there is no model/profiles/robert-blust/robert-blust.jpg (R9) ``, and exit 1.

- [ ] **Step 2: Add the file and see it pass**

```bash
cp ~/Desktop/robert-blust.jpg model/profiles/robert-blust/robert-blust.jpg
cmp ~/Desktop/robert-blust.jpg model/profiles/robert-blust/robert-blust.jpg; echo "identical $?"
sips -g pixelWidth -g pixelHeight -g format model/profiles/robert-blust/robert-blust.jpg | tail -3
npx --yes 'github:companygraph/meta-model#v0.42.0' check .; echo "check $?"
```

Expected: `identical 0`; 1000, 1000, `jpeg`; `✓ … the mechanical checks pass` and `check 0`.

- [ ] **Step 3: The writing rule, which no script holds**

The profile schema asks that the image be the person, recognizably, and not a logo, a team or an illustration. Open the file and look. Say in the report what it shows.

- [ ] **Step 4: Validate, commit, push, open the pull request, then stop**

Run the `companygraph-validate` skill. Commit the two files; the message says why a profile carries a picture and that the checker held it from its bytes. Push, read the last two merged pull request bodies and match their shape, link companygraph/meta-model#136, and watch `gh pr checks --watch` until the instance check and `conventions / conventions` report. Then stop: merging is the owner's word, and the first constraint above says what has to be true before he gives it.

---

## What this plan does not do

Nothing draws the picture yet. blust.ch copies and shows it in `docs/superpowers/plans/2026-09-21-the-card-shows-the-person.md` there, after its content pin moves to the commit this merges as. The LinkedIn, CV and other surfaces this model describes keep their own pictures; whether a surface's rules should name this file as the one source is a question for the owner and not part of this.
