# Lecture 5 — EN render iteration log

Issue #189 (bilingual production, RU source approved) · Branch:
hc/pldlc-lesson5-c5cc1586

Cross-ref: `iteration-log.md` (RU build log, this file's counterpart).

## Scope

Full EN re-render of the approved RU 56-slide deck, mirroring
`build_lec05.py` display order exactly. EN content sourced from
`deck.en.yaml` + `deck-part2.en.yaml` + `slides-en/*.md` (56 files,
already produced/approved before this session).

## Files produced

- `_helpers_en.py` — copy of `_helpers.py` with: `CHARTS`/`SLIDES_DIR`
  pointed at `-en` asset dirs; `NAV` translated to EN section names
  (Intro/Discovery/Design/Build & Launch/Measure/Support/Governance);
  `"РАЗДЕЛ {N}"` → `"SECTION {N}"` on dividers; `"Источники:"` marker →
  `"Sources:"`; ELI5 gold chip `"простыми словами"` → `"in plain terms"`;
  `SLIDE_REFS` dict (all ~50 entries) translated to English glosses (URLs
  and `URLS` registry unchanged — language-agnostic).
- `gen_charts_en.py` — EN twin of `gen_charts.py`: same 8 charts, same
  data/layout, English axis/bar/legend labels. Output → `assets/charts-en/`.
- `gen_memes_en.py` — EN twin of `gen_memes.py`: same 15 evergreen meme
  templates (Spider-Man/One-Does-Not-Simply/Distracted-Boyfriend/Drake/
  Anakin-Padme/Woman-Yelling-Cat/Disaster-Girl/Sad-Pablo/Bernie/Trade-Offer/
  Is-This-A-Pigeon/Clown/Balloon/They're-Same-Picture/Gru's-Plan), no new
  template picks, English captions resolving to each slide's claim. Mirrors
  the RU set exactly including the RU quirk of `s09_bernie()` being defined
  but unused (s09 itself has no meme in either language). Output →
  `assets/memes-en/`.
- `slides_band1_en.py`..`slides_band4_en.py` — EN twins of `slides_band1.py`
  ..`slides_band4.py`: identical layout/geometry/palette per slide, all
  visible strings + speaker-note calls translated using the approved
  `slides-en/sNN*.md` phrasing as the source of truth (not a fresh
  translation — reused the already-produced EN copy verbatim where slide
  layout allowed).
- `build_lec05_en.py` — EN twin of `build_lec05.py`, same 56-builder display
  order, same `assert n == 56`.
- `render_en.sh` — EN twin of `render.sh`: renders `lec-05-en.pptx` →
  `lec-05-en.pdf` → `snapshots/en-slide-NN.png`.

## Bug found + fixed during visual QA

`_helpers_en.py` was copied from `_helpers.py` with `MEMES = ASSETS /
"memes"` left unchanged (only `CHARTS`/`SLIDES_DIR` had been repointed).
First render of s01 showed the RU Spider-Man meme (Cyrillic captions
"сборка почти бесплатна" / "ценность — ноль у 95%") despite the EN build
otherwise being correct. Fixed: `MEMES = ASSETS / "memes-en"`. Rebuilt +
re-rendered full deck; s01 and all other meme slides now show EN captions.

## Verification

- `build_lec05_en.py`: `assert n == 56` passes, both before and after the
  meme-path fix.
- Deep scan for Cyrillic: `pymupdf` text extraction over all 56 PDF pages
  → **0 Cyrillic characters** in the visible layer. `python-pptx` scan of
  all 56 slides' speaker notes → **0 Cyrillic characters**. (Brand/quoted
  RU source titles is the only allowed exception per the task brief; none
  were present in the scanned content, so this is a clean 0, not a
  filtered 0.)
- Visual inspection (vision, on actual rendered PNGs, not build-success
  alone) of 8 slides across the deck: s01 (hook, real index 1), s02 (cover,
  2), s07 (Discovery divider, 7), s13/s12-index (synthetic-users failure
  w/ trade-offer meme, 13), s18-index (WCAG chart + pigeon meme, 21),
  s28b-index (Measure ELI5, 33), s38-index (LLMOps tracing, 44), s49 (closing
  hero, real index 56). All render cleanly: no text overflow/clipping, no
  overlapping elements, EN memes show EN captions, EN charts show EN
  axis/bar labels, roadmap bar + section dividers show EN section names,
  no timing markers, no methodology commentary on visible body.
- Additionally spot-checked s27-index (McDonald's, real photo), s47-index
  (MIT funnel chart + real MIT photo, index 54), s41-index (Air Canada, real
  photo) — all clean.
- One pre-existing minor cosmetic quirk mirrored faithfully from RU (not a
  regression introduced by the EN pass): on the cover slide the
  "Support"/"Измерение"-equivalent hexagon-node label sits close to the
  meme-box top edge; identical framing present in the RU `slide-02.png`.
  Also the s47-index reference line at the bottom occasionally wraps to a
  second line for long 5-entry reference lists — confirmed identical
  wrap behavior in the RU original.

## Outcome

`lec-05-en.pptx` (56 slides) + `lec-05-en.pdf` + 56
`snapshots/en-slide-NN.png` all produced and verified. Nothing left
unresolved for this pass.
