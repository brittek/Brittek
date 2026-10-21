# Brand kit

The Brittek identity masters, packaged for reuse outside the production
application. Every file here is generated from the canonical sources in
`brittek/brittek-surface`; nothing is redrawn or traced.

| Source in brittek-surface | Ruling | Provides |
| :--- | :--- | :--- |
| `lib/design/brtk-mark.ts` | BRAND-01, 2026-10-19 | `brtk.` wordmark: letters and full stop |
| `components/system/CommandMark.tsx` | APPEARANCE-04C, 2026-10-19 | COMMAND faces and legend, `ASTERISK_PATH` |
| `public/brand/source/favicon-v4/asterisk-signal.svg` | Identity doctrine 2026-09-27 | Favicon master |
| `app/fonts/*.woff2`, `public/licenses/*` | Font lock 2026-09-21 | Five type registers (OFL) |

Generated from `brittek-surface@45ca03e`. When a master changes there, regenerate
here; do not edit the geometry by hand.

## Contents

```text
brand/
├── marks.svg                 sprite: #brtk, #command, #asterisk, #asterisk-path
├── svg/
│   ├── lockup-ink.svg        primary lockup, COMMAND + brtk., for light grounds
│   ├── lockup-paper.svg      primary lockup for dark grounds
│   ├── brtk-ink.svg          wordmark, Ink letters, Signal stop
│   ├── brtk-paper.svg        wordmark, Paper letters, Signal stop
│   ├── command-ink.svg       COMMAND, Ink line on Paper faces
│   ├── command-paper.svg     COMMAND, Paper line on Ink faces
│   ├── asterisk-signal.svg   ASTERISK in Signal, transparent ground
│   └── favicon-asterisk-signal.svg   canonical favicon, copied byte for byte
└── fonts/                    Inter Tight, Inter, Geist, Geist Mono, Geist Pixel Square
```

## Using the sprite

Inline the `<defs>` of `marks.svg` once per page, or reference it on the same
origin. A `<use>` of a `<symbol>` draws from the outer SVG's origin, so the outer
`viewBox` starts at `0 0` and carries the symbol's size:

```html
<svg viewBox="0 0 3669 1510" style="height:20px; color:#111111"><use href="#brtk"/></svg>
<svg viewBox="0 0 262.49 220" style="fill:#F4F3EF; stroke:#111111; stroke-width:2.2"><use href="#command"/></svg>
<svg viewBox="0 0 120 32" style="color:#FE4A02"><use href="#asterisk"/></svg>
```

| Symbol | Colour hooks |
| :--- | :--- |
| `#brtk` | letters take `currentColor`; the stop takes `--brtk-stop` (default Signal) |
| `#command` | faces inherit `fill` and `stroke`; the legend takes `--command-legend` (default `currentColor`) |
| `#asterisk` | `currentColor` |
| `#asterisk-path` | raw path for canvas `Path2D` and custom placements |

## Usage rules

From the identity doctrine in `brittek-surface` (`docs/platform/identity-typography-doctrine-2026-09-27.md`)
and later owner rulings:

- **COMMAND + `brtk.`** is the primary lockup, for full identity compositions.
- **`brtk.`** is the only mark in the compact header (HEADER-SINGLE-MARK, #320).
- **ASTERISK** is the favicon and compact app identity. Below about 32px,
  COMMAND loses its construction; use the ASTERISK instead.
- **Pixel `brtk.`** is a runtime word-sign: Geist Pixel Square with the Signal
  stop, paired with a Mono state label, only while the system is working.
- **One Signal event per plate.** In the lockup the stop carries Signal, so the
  COMMAND legend stays Ink.
- In Registered Execution fields: ordinary module blank, important node
  ASTERISK, active node Signal ASTERISK.
- Never set `brtk.` in a font, approximate COMMAND with CSS polygons or rebuild
  a mark from a screenshot.

The lockup's spacing (COMMAND on the wordmark's ascender-to-baseline band, gap
0.42 of that band) is a proposal, not an owner ruling.

## Colour

| Token | Value | Notes |
| :--- | :--- | :--- |
| Paper | `#F4F3EF` | Primary surface |
| Bone | `#ECEAE3` | Secondary surface |
| Ink | `#111111` | Text and dark surface |
| Signal | `#FE4A02` | The only accent. Large text, marks and rules only on Paper |
| Signal text | `#CC3B02` | Small text in the interaction colour on Paper (4.51:1) |

## Fonts

Latin-subset WOFF2 files, copied from `brittek-surface/app/fonts`, with their
OFL licences. Declare them with `@font-face` and `font-display: swap`; see
`presentation/index.html` for a working block. No page should load fonts from
Google Fonts or another third-party origin.

## Verification

`python3 scripts/check_brand.py` confirms the sprite's symbols, that the
presentation's inline sprite matches this file, that every declared font
exists, and that the presentation requests nothing from a third-party origin.
It runs in the Profile quality workflow.
