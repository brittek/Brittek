# Implementation notes

This bundle closes the repository-standard gap identified in the profile audit.

## Add now

- `LICENSE`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `.gitignore`
- `.github/CODEOWNERS`
- `.github/dependabot.yml`
- `docs/WORKFLOWS.md`
- `llms.txt`
- `llm.json`
- `site-index.json`
- `schema.org.json`
- `profile/brittek-wordmark.svg`
- `profile/brittek-wordmark-dark.svg`

## Do not add to this repository by default

`feed.xml` is intentionally limited to a repository-level skeleton for
GitHub-facing updates. `sitemap.xml` remains out of scope unless this
repository also becomes the canonical deployed website for `brittek.net`.

## README correction

Once these files are committed, the existing “Repository standard” section is
no longer aspirational. Keep it, but describe the listed files as the current
baseline rather than as a hypothetical standard.
