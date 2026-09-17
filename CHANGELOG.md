# Changelog

Meaningful changes to the public profile surface, automation, machine-readable
metadata, and repository governance are recorded here.

The format is based on **Keep a Changelog** principles without requiring
semantic versioning for ordinary profile edits.

## Unreleased

### Added

- repository governance documents;
- machine-readable profile surfaces;
- workflow documentation;
- repository hygiene configuration;
- `.github/PULL_REQUEST_TEMPLATE.md` and `.github/ISSUE_TEMPLATE/` to match
  the documented repository standard.

### Changed

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
  branch.

### Removed

- `IMPLEMENTATION.md`, a repository-audit tracking note whose listed items
  are now fully implemented.

## 2026-09-14

### Added

- refined GitHub profile README;
- generated profile metrics;
- contribution streak asset;
- Brittek Digital light and dark wordmark assets.

### Changed

- profile positioning consolidated around design engineering, digital
  infrastructure, systems, and machine-readable architecture.
