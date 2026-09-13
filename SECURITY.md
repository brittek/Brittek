# Security Policy

## Reporting a vulnerability

Do **not** open a public GitHub issue for a suspected security vulnerability.

Report security concerns privately to:

**hello@brittek.net**

Include, where possible:

- affected workflow, file, or dependency;
- reproduction steps;
- expected and observed behaviour;
- potential impact;
- suggested remediation, if known.

## Scope

Security reports are relevant to this repository when they concern:

- GitHub Actions configuration;
- workflow permissions;
- token or secret handling;
- third-party Actions or generated assets;
- unsafe external content rendering;
- supply-chain integrity;
- accidental disclosure of private information.

## Secrets

No credentials, personal access tokens, API keys, or private environment
values should be committed to this repository.

GitHub Actions should use the minimum permissions required for each job.

## Dependency policy

External Actions should be pinned to immutable commit SHAs where practical.
Version changes should be reviewed before adoption.

## Disclosure

Please allow reasonable time for investigation and remediation before public
disclosure.
