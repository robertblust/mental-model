---
source: Local
kind: Community
start: 2026-08
url: https://blust.ch
skills:
  - Agentic AI development
  - Public speaking
  - Technical writing
  - UX design
  - CI/CD
  - Software testing
---

# blust.ch

> Ongoing. A profile page built from the model, and two talks that say what the model is for.

## Achievements

### Context

- Published the profile page, a principles page, an ideas page and two narrated talks, The Mental Model and Essential Complexity — each bilingual with a PDF, self-contained and presentable from a file with no server running.

### Architecture

- Built the model and timeline pages from the mental-model repository at a pinned commit, so the page shows what the model says and a corrected fact is one commit in one place.
- Conceived and designed the pages of all three sites and the design system they share, from layout and typography to the graph view, and had the agent seats build them to that design.
- Shared its typography, chrome and page checks with guestgraph.io and companygraph.io through one design system, released over 50 times in its first week and taken by every site by pin.

### Engineering

- Held every page to a rendered check rather than a diff: browser assertions on every page, share cards compared against the pages they were rendered from, and a pin guard that fails the build when a dependency is behind its release.
- Required one shared conventions check beside each repository's own suite on every default branch in the family, called from one reusable workflow at a pinned tag.
- Generated the narration from the speaker notes on a content hash, so editing one note regenerates one clip.

### Ways of working

- Built it through the agent seats the model defines, each under its own rulebook and none of them deciding, with the Owner reviewing and merging.
- Set the family's written voice and rules in `WRITING.md`, and briefed and reviewed every page the Writer seat drafted to those rules.
