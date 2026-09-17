# Workflow maintenance guide

This repository uses GitHub Actions to generate the profile assets committed to
`/profile`.

## Workflow inventory

### `profile-metrics.yml`

- **Purpose:** generate `profile/metrics.svg`
- **Schedule:** `47 2 * * *`
- **Timezone reference:** Australia/Sydney
- **Manual trigger:** `workflow_dispatch`
- **Pinned dependency:** `lowlighter/metrics@366f8b9dfe3a59656c67d5dcad9950f59c9bc96d`
- **Key settings:** header, activity, community, repositories, metadata;
  repository forks excluded; most-used languages limited to 6; animations off.

### `streak-stats.yml`

- **Purpose:** generate `profile/streak.svg`
- **Schedule:** `17 2 * * *`
- **Timezone reference:** Australia/Sydney
- **Manual trigger:** `workflow_dispatch`
- **Pinned dependencies:** `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1),
  `DenverCoder1/github-readme-streak-stats@9202e37665889fdb42d9a7df8501c1800acf761d`
- **Key settings:** transparent background; animations off; Brittek accent ring
  and fire colours; bot-authored conditional commit.

Both `profile-metrics.yml` and `streak-stats.yml` run under a per-workflow
`concurrency` group with `cancel-in-progress: true`, so an overlapping
scheduled and manually dispatched run cannot push conflicting commits to the
same generated asset.

## Maintenance rules

1. Keep third-party Actions pinned to immutable commit SHAs.
2. Preserve minimum required GitHub permissions.
3. Review generated SVG changes before merging workflow edits.
4. Do not commit tokens, secrets, or private repository information.
5. Keep timezone references consistent with `Australia/Sydney`.

## Verification checklist

After changing either workflow:

1. run the workflow manually from GitHub Actions;
2. confirm the job succeeds;
3. inspect the generated SVG in `profile/`;
4. verify the README still renders correctly on GitHub;
5. confirm the resulting commit contains only expected files.
