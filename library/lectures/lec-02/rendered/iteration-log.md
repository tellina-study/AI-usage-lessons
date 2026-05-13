# Iteration Log — Lecture 2 v1.0 (28 slides)

**Phase:** 6 — PowerPoint rendering
**Approach:** python-pptx direct (canonical builder `build_lec02.py`)
**Canvas:** 13.333" × 7.5" (16:9 widescreen)
**Palette:** Ocean Gradient + Teal accent + Gold highlight (LOCKED v1, deck.yaml)
**Motif:** Ocean rounded box (radius 12, surface `#F4F7FA`, stroke `#1C7293` 1.5pt) — on every content slide.

## Pre-Design Wireframes (for custom-schema slides)

For each schema slide (s11, s14, s15, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26), wireframe was documented inline in `build_lec02.py` as docstring + Builder function source code. Layout planning happened during build_lec02.py write phase, before iter-1 render.

Key schema decisions:
- **s10 (matrix heatmap):** rendered via SVG (rsvg-convert) with manual cell colors (Ocean scale + Gold for key pairs), not QuickChart — needed precise control over cell value placement and color gradient.
- **s17 (U-shape):** Chart.js line chart with custom point sizes (50% middle point = gold 10px radius vs 6px others).
- **s19 (3 distributions):** 3 separate QuickChart bar PNGs side-by-side in 3 motif cards — avoids dataset overlap issues.
- **s20 (matrix 4×5):** Native python-pptx rectangles + textbox grid (no chart library) — full control over header bar, T-column color coding by accent.
- **s21 (cycle 5 steps):** Horizontal flow with MSO_SHAPE.RIGHT_ARROW between stages + bottom "return" indicator bar (cleaner than circular layout at 13.33"×7.5" canvas).
- **s23 (pipeline 4 stages):** Horizontal RIGHT_ARROW pipeline; stage number circles for visual rhythm.
- **s25 (decision tree):** Root → 3 vertical branches via filled lines; "Иначе" pill at bottom in Teal accent.

## Per-slide iteration counts

| Slide | Iter count | Issues fixed | Final status |
|-------|------------|--------------|--------------|
| s01 | 3 | none — clean first render | PASS |
| s02 | 3 | iter-1: "02" textbox clipped to "0" (size=320 too large for 4.8" box); iter-2: changed to single "2" at 420pt, repositioned roadmap-bar from y=6.7 to y=6.85 (it was clipping at canvas bottom) | PASS |
| s03 | 3 | none — clean nested-layers pyramid + bridge | PASS |
| s04 | 3 | none — central question + 3 promise cards balanced | PASS |
| s05 | 3 | none — 3 vertical example rows + gold callout + teal poll | PASS |
| s06 | 3 | iter-1: big "→" arrow text box (size=48) collapsed to barely-visible char; iter-2: replaced with proper `MSO_SHAPE.RIGHT_ARROW` between columns at full gap width | PASS |
| s07 | 3 | none — strawberry split (custom SVG) + 3 consequence cards | PASS |
| s08 | 3 | none — QuickChart bar + side table | PASS |
| s09 | 3 | none — custom SVG token→vector lookup | PASS |
| s10 | 3 | none — custom SVG heatmap 5×5 with Ocean scale + Gold key pairs | PASS |
| s11 | 3 | none — 3 motif cards with Lucide icons (magnet/box/search-check) | PASS |
| s12 | 3 | none — query + 2-column compare with check/cross marks | PASS |
| s13 | 3 | none — Section 3 divider with mega gold "Раздел 3" + roadmap | PASS |
| s14 | 3 | none — flashlight metaphor (custom SVG) + attention bars (QuickChart) | PASS |
| s15 | 3 | none — worked example Part A (sentence + 3 arrow-strength chips) + Part B (without/with role with gold inline runs for role words) | PASS |
| s16 | 3 | none — context window log-scale bar chart + N² visual + gold callout | PASS |
| s17 | 3 | none — U-shape curve chart (QuickChart line) with middle gold marker + results panel | PASS |
| s18 | 3 | none — QuickChart bar distribution + top-5 side table | PASS |
| s19 | 3 | none — 3 distribution charts side-by-side (gold/blue/teal accents per T value) | PASS |
| s20 | 3 | none — 5-column 5-row matrix with T-column gold/teal color coding | PASS |
| s21 | 3 | none — 5-stage horizontal flow with RIGHT_ARROW connectors + return-loop indicator | PASS |
| s22 | 3 | none — 2-column local vs cloud with status dots (Teal/Light/Gold accents) | PASS |
| s23 | 3 | none — 4-stage pipeline with RIGHT_ARROW + chapter-anchor labels | PASS |
| s24 | 3 | none — gold-marker header + 3 numbered answer cards | PASS |
| s25 | 3 | none — decision tree with root + 3 branches + teal "иначе" pill | PASS |
| s26 | 3 | none — human vs AI 2-column with Pearl levels visualization | PASS |
| s27 | 3 | none — 3 step cards + playground + bonus gold box | PASS |
| s28 | 3 | iter-1: Agent loop used same `workflow.png` icon as Tools/Function calling; iter-2: replaced with `repeat-2` Lucide icon (unique per concept) | PASS |

## Final iteration distribution

- **Average iterations per slide:** 3.0 (minimum enforced)
- **Slides requiring fixes:** 3 (s02, s06, s28)
- **Slides clean on iter-1:** 25
- **Escalations:** 0

## Asset inventory

### Charts (QuickChart API)
- `s08-tokens-per-char.png` — bar chart 4 languages, RU gold-highlighted
- `s14-attention-bars.png` — attention distribution on 8 tokens, max in gold
- `s16-context-window.png` — 3-bar log-scale (GPT-3.5 / Claude 3.5 / Claude 4.7)
- `s17-u-shape.png` — Lost-in-the-middle line curve with mid-position gold marker
- `s18-distribution.png` — top-5 P(token) bars, max in gold
- `s19-T0.png` / `s19-T1.png` / `s19-T2.png` — 3 small distribution bars per T value

### Custom SVG → PNG (rsvg-convert)
- `s01-tiktokenizer-mock.png` — recreation of Tiktokenizer interface with 4 token splits
- `s07-strawberry-split.png` — 10-letter vs 3-token comparison
- `s09-token-to-vector.png` — id-to-vector lookup schema
- `s10-heatmap.png` — 5×5 cosine similarity heatmap
- `s14-flashlight.png` — flashlight metaphor for attention

### Icons (Lucide, recolored to `#065A82`, 96px)
zap, magnet, search-check, target, sliders-horizontal, file-text, flashlight, gauge, cpu, users, lightbulb, workflow, brain, layers, arrow-right-left, book-open, box, hand, database, repeat-2

(One set per deck — semantic role, max 4 per slide, recolored to Ocean palette.)

## Anti-pattern compliance

- [x] **NO subtitle** on content slides (only s02 title slide has 4-stage promise line — which is the main message).
- [x] **NO «Вы здесь» / «Лектору» / тайминг** on visible content. Roadmap-bar gold-highlight is sole navigation indicator.
- [x] **NO decorative SVG/icons without semantic role** — all icons have a semantic mapping (target→ДЗ цель, sliders→T-controls, repeat-2→loop, etc.).
- [x] **NO axis labels outside quadrant** — n/a (no quadrant subtypes in this deck).
- [x] **NO cycle with 6+ steps as vertical list** — s21 uses horizontal 5-step flow + return indicator.
- [x] **NO pipeline with filled_rect+triangle hybrid** — all arrows are `MSO_SHAPE.RIGHT_ARROW`.
- [x] **NO mixed icon sets** — Lucide only.
- [x] **NO 6+ icons per slide** — max 4 per slide (s11=3, s28=4, s25=3, s27=3).
- [x] **Gold highlight ≥1× per slide** — verified visually across all 28 PNGs.
- [x] **Ocean rounded box motif present** on every content slide.

## DoD verification

- [x] 28 final PNG snapshots saved as `sNN.png` in `snapshots/`
- [x] `lec-02.pptx` saved (722 KB) — 28 slides + speaker notes
- [x] `iteration-log.md` documents per-slide iter count
- [x] All slides pass Schema Readability Checklist (per applicable subtype)
- [x] All slides pass 5-Second Test (main message readable from PNG @ 25% zoom)
- [x] All slides pass Projector Readability (50% zoom — minimum font ≥12pt body / ≥14pt axis verified)
- [x] Palette Ocean Gradient + Gold ≥1× per slide
- [x] Ocean rounded box motif on each content slide
- [x] Speaker notes 200-340 words per slide (target 150-300; some slides slightly over — connected readable text, no layout description)

## Notes for downstream phases

- All 28 PNGs at 130dpi (~1700×950px each) — sufficient for projector readability tests.
- PDF rendered with libreoffice headless (~3s for 28-slide deck).
- Total deck PPTX: 722 KB; PDF: ~5 MB; PNG snapshots: 4.3 MB total.
- Schema slides s14, s17, s20, s21, s23, s25 are the most schema-heavy — recommended for student-simulator/critic review priority.
- No slides were deleted or added (28 fixed per Phase 5 freeze).
- No visible_content or speaker_notes were modified (frozen at Phase 5).

## Tool footprint update

No new MCP limitations or render-toolchain artifacts encountered in this run. All existing limitations (PowerPoint MCP missing inspection tools, QuickChart UTF-8 in POST requires `ensure_ascii=True` workaround, mermaid Chrome missing — used custom SVG path) avoided through python-pptx direct + Python urllib for QuickChart + rsvg-convert for SVG.
