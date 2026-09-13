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
- `docs/workflows.md`
- `llms.txt`
- `llm.json`
- `site-index.json`
- `schema.org.json`
- `profile/brittek-wordmark.svg`
- `profile/brittek-wordmark-dark.svg`

## Do not add to this repository by default

`sitemap.xml` and RSS belong at the canonical web origin (`brittek.net`)
unless this repository is deployed as a public website. A GitHub repository
containing a sitemap does not make that sitemap authoritative for brittek.net.

## README correction

Once these files are committed, the existing “Repository standard” section is
no longer aspirational. Keep it, but describe the listed files as the current
baseline rather than as a hypothetical standard.
