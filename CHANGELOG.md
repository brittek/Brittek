# Changelog

Meaningful changes to the public profile surface, automation, machine-readable
metadata, and repository governance are recorded here.

The format is based on **Keep a Changelog** principles without requiring
semantic versioning for ordinary profile edits.

## Unreleased

### Added

- `brand/`, a reusable kit generated from the brittek-surface masters: a
  symbol sprite (`#brtk`, `#command`, `#asterisk`), standalone SVGs for the
  primary lockup, wordmark, COMMAND and ASTERISK in light and dark, the
  canonical favicon, and the five self-hosted type registers with their OFL
  licences;
- `scripts/check_brand.py`, run by the Profile quality workflow, which keeps
  the presentation's inline sprite identical to `brand/marks.svg` and rejects
  third-party font or asset origins;

- repository governance documents;
- machine-readable profile surfaces;
- workflow documentation;
- repository hygiene configuration;
- `.github/PULL_REQUEST_TEMPLATE.md` and `.github/ISSUE_TEMPLATE/` to match
  the documented repository standard;
- `presentation/index.html`, a self-contained animated presentation of
  selected Brittek work (practices, website lineage, Brittek Surface, the
  Machine Surface Inspector, identity system, studies and tools, operations).
  Content lives in one JSON block; client work is withheld until clearance.
- presentation scenes for the four identity marks (COMMAND, brtk., ASTERISK,
  Runtime), their applications (avatar, horizontal lockup, packaging lid) and
  The Lab edition 2026.14; the Lab also joins the website lineage. Marks are
  placed from the 2026.9.8 vector masters, and the opening field now draws
  blank COMMAND modules with the master ASTERISK on the signal module.

### Changed

- the presentation now places the current masters: the BRAND-01 `brtk.`
  wordmark and the APPEARANCE-04C COMMAND legend replace the retired Lab
  2026.14 drawings. The header carries `brtk.` alone; the primary lockup is
  COMMAND + `brtk.`; the favicon tile is the Signal ASTERISK; Runtime is set in
  Geist Pixel Square; the opening field marks important nodes with the
  ASTERISK and the active node in Signal;
- the presentation loads its type from `brand/fonts` and makes no third-party
  requests (Google Fonts removed). The Runtime register is now rendered;
- small Signal text on Paper uses `#CC3B02` to meet contrast;

- repository standard moved from aspirational documentation toward actual
  implementation;
- `streak-stats.yml` now pins `actions/checkout` to an immutable commit SHA,
  matching the pinned-Action policy already applied elsewhere;
- `profile-metrics.yml` and `streak-stats.yml` now run under a per-workflow
  `concurrency` group so an overlapping scheduled and manual run cannot push
  conflicting commits to the same generated asset;
- `profile-metrics.yml` and `streak-stats.yml` now restrict their `push`
  trigger to `branches: [main]`, so editing either workflow file on a
  feature branch no longer causes a bot commit to be pushed onto that
  branch;
- `lychee.toml` now excludes `codepen.io`, matching the automated-client
  blocking already worked around for LinkedIn, X, Instagram, Dribbble, and
  Behance.

### Removed

- `IMPLEMENTATION.md`, a repository-audit tracking note whose listed items
  are now fully implemented;
- the dev.to link and badge from the README "Elsewhere" section and
  `schema.org.json`'s `sameAs`; the account no longer resolves (404).

## 2026-09-14

### Added

- refined GitHub profile README;
- generated profile metrics;
- contribution streak asset;
- Brittek Digital light and dark wordmark assets.

### Changed

- profile positioning consolidated around design engineering, digital
  infrastructure, systems, and machine-readable architecture.
