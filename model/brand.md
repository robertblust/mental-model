---
source: Local
---

# blust.ch

> One person's work, under one address: what appears here was built before it was claimed, and what cannot be shown is not written.

## Mark

The mark is the two letters `rb`, set in Plex Mono on the ground color, and its master is `favicon.svg` in the site's repository; every other render, a tile a host is handed, the lockup on the profile photo, is made from that file and never drawn again. The mark's colors are the design tokens' ground and accent.

- A tile is a full-bleed square with no rounded corner, because the host rounds it and a transparent corner shows as a checkerboard.
- The mark fills about 60% of the tile, so it survives a circular crop.
- A change to the mark is made in the favicon first and rendered everywhere else after.
- Where a render carries values other than the tokens', the favicon included, the tokens are the master and the render follows.

## Color

| Name | Means | Never |
| --- | --- | --- |
| `--c-weak` | A candidate: considered, not accepted | Text, a border or an outline on its own, in either theme |
| `--c-mid` | Anything interactive: a link, a control, the brand accent | The resolved thing, which would then read as still open |
| `--c-firm` | The resolved thing: the thesis, the current page | A link, which would then read as settled |
| `--c-flag` | A reversal, at most once per page | Decoration |
| `--c-sum` | A conclusion, what a section's figures add up to, as the line of a conclusion and at most once per section | Text |
| `--c-path` | Where you are and how you got here: the ancestors of the focused node and the line through them | The resolved thing, which only happens to look alike |

## Typography

| Face | Job |
| --- | --- |
| Instrument Sans | Prose: the body of every page and every deck |
| Plex Mono | The ledger and the chrome: the footer, the stage, a deck's transport, and the mark |
| Bricolage Grotesque | A section's mark: the small heading that names a principle, a seat or a surface |

## Voice

| Trait | Means | Never |
| --- | --- | --- |
| Plain | I say what happened in the words the reader would use for it | An adjective that sells: nothing here is seamless, robust or elegant |
| Shown | I claim what I can show, and I say where it is shown | A number I did not count, or one that still moves, or a behavior I inferred rather than observed |
| Cause first | I say why before how, so a reader can tell whether the how still applies | A mechanism with no reason beside it |
| Forward | I say how things are, in the present, and leave how they came to be to git | A page that narrates its own history |
| Read twice | I would rather be read twice than skimmed once: one idea per sentence, the point in the first | A header that segments a text which fits on a screen |

## References

| What | URL |
| --- | --- |
| Design tokens | https://github.com/robertblust/design/blob/main/blocks/tokens.css |
| Mark | https://github.com/robertblust/robertblust.github.io/blob/main/favicon.svg |
| Rulebook of the voice | https://github.com/robertblust/conventions/blob/main/conventions/WRITING.md |
| Typefaces, as the pages set them | https://github.com/robertblust/design/blob/main/blocks/reset.css |
