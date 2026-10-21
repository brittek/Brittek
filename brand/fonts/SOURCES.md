# Font source inventory

Owner lock: 21 September 2026.

The application loads all public brand fonts from local assets through `app/fonts.ts`.

| File | Register | Upstream source | Upstream ref | Licence |
| --- | --- | --- | --- | --- |
| `InterTight-Variable.woff2` | Editorial | existing governed repository asset | existing repository provenance | OFL |
| `InterTight-Italic-Variable.woff2` | Editorial italic | existing governed repository asset | existing repository provenance | OFL |
| `Inter-Variable.woff2` | Reading | `rsms/inter` `docs/font-files/InterVariable.woff2` | `v4.1` | `/licenses/inter-OFL.txt` |
| `Geist-Variable.woff2` | Interface | `vercel/geist-font` `fonts/Geist/webfonts/Geist[wght].woff2` | `v1.7.2` | `/licenses/geist-OFL.txt` |
| `GeistMono-Variable.woff2` | Technical | existing governed repository asset | existing repository provenance | `/licenses/geist-mono-OFL.txt` |
| `GeistPixel-Square.woff2` | Runtime | `vercel/geist-font` `fonts/GeistPixel/webfonts/GeistPixel-Square.woff2` | `v1.7.2` | `/licenses/geist-OFL.txt` |

## Subsetting (W-LH hygiene)

All six WOFF2 files above are **latin-subsetted** from the upstream binaries via `fonttools` / `pyftsubset` (`--flavor=woff2`, latin + common punctuation unicodes, layout features retained, variable `wght` axis retained where present). No Google Fonts, CDN fonts, or static TTF tree. Re-subset from the upstream refs above when replacing a binary; do not widen the glyph set without a measured need.

No public page should request font files from Google Fonts, raw GitHub or another third-party origin at runtime.
