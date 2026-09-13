# Profile automation

This repository uses GitHub Actions to generate profile telemetry committed
back into `profile/`.

## `profile-metrics.yml`

**Purpose:** generate `profile/metrics.svg`.

The output provides a compact GitHub activity snapshot without hard-coding
volatile metrics into `README.md`.

### Operating requirements

- GitHub Actions must have the minimum repository permissions required by the
  workflow.
- The external action should remain pinned to an immutable commit SHA.
- Changes to the action version should be reviewed before merging.
- Generated output is intentionally tracked in Git.

## `streak-stats.yml`

**Purpose:** generate `profile/streak.svg`.

### Operating requirements

- The workflow should write only the expected generated asset.
- Push permissions should remain limited to repository contents.
- Authentication material must remain in GitHub-provided secrets or repository
  secrets; never commit a token.
- Prefer deterministic, non-animated rendering where possible.

## Schedule

Scheduled execution exists to keep profile data fresh. Manual dispatch should
remain available for verification after workflow changes.

## Verification checklist

After modifying either workflow:

1. run it manually;
2. confirm the job completes successfully;
3. inspect the generated SVG;
4. confirm the README renders in GitHub;
5. verify no credentials or private repository names appear in generated
   output;
6. confirm the generated commit contains only expected files.

## Supply-chain policy

Third-party Actions should be pinned to commit SHA rather than floating tags
when practical. Version metadata may be documented in comments for
maintainability, but execution should use immutable references.
