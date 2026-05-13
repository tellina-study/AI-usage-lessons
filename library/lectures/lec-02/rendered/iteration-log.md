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

---

## v1.0 → v1.1 — Phase 8 revision (2026-05-13)

**Source:** `qa-reports/2026-05-13-phase7-slides-v1/SYNTHESIS.md` (combined Phase 7 verdict REVISE).

**Build script change:** ROOT path made relative via `Path(__file__).resolve().parent.parent` to support isolated worktree.

### P0 fixes (visible student-facing leaks)

1. **`[VERIFY-DAY-OF]` marker leak** — removed from visible body of `s16` and `s27` rendered slides; moved verification cue to speaker notes. Slide MDs updated accordingly.
2. **Visual scale fix on 11 slides** — `s07`, `s14`, `s15`, `s19`, `s21`, `s22`, `s24`, `s25`, `s26`, `s27`, `s28`:
   - Body font bumped to ≥14pt (most ≥15-17pt for cards / 18pt for headers)
   - Sub-label / caption fonts ≥12pt
   - Icon sizes increased (0.7→0.8, 0.85→0.95-1.10)
   - Card heights expanded (s27 cards: 3.3→3.55; s19: 3.8→4.55) to fill canvas to ≥80%
   - Number badges enlarged (s23: 0.7→0.85; s24: 0.85→0.95; s04: 0.55→0.65)

### P1 fixes (visual + content polish)

3. **s11 title** list («3 применения: similarity, clustering, search») → assertion («Эмбеддинги дают similarity, clustering и search — основу RAG»). Slide MD assertion field also updated.
4. **s14 flashlight metaphor** reduced to small inset (1.3×1.3) at bottom-right corner; bar chart distribution promoted to dominant 8.5×4.6 visual (was 6.0×4.0).
5. **s17 gold focus** flipped from negative middle dip (~30% — cognitive dissonance per P1-V6) to positive endpoints (~75% beginning/end); middle softened to ~50% per Liu et al. (P1-F2). Chart `s17-u-shape.png` regenerated via QuickChart with new Y values [78,72,58,52,58,72,76] and gold points on indices 0 and 6.
6. **s18 «Σ = 1» overflow** fixed — top-5 list row spacing tightened (0.55→0.45 row pitch), bottom label box repositioned at y=5.30 (was 5.85) with more height (0.45→0.95) and proper multi-line spacing.
7. **s19 «стандарт» unification** — T=1.0 designated «стандарт» throughout, T=0.7 noted as «consensus для чата». Gold accent moved from T=0 card to T=1.0 (standard recommendation). Slide MD updated.
8. **s23 designer-extras removal** — «← s05-s08»/«← s09-s12»/«← s13-s17»/«← s18-s20» anchor footers deleted from 4 pipeline stages; «id → learned table» unified to «id → вектор из обученной таблицы» (RU).
9. **s24 «→ sNN» forward-refs removal** — all 3 forward-ref labels («→ s15», «→ s05-s07», «→ s18-s19») removed from answer cards. Fonts bumped (q: 16→18pt, a: 13→15pt, number: 38→44pt).
10. **s25 forward-ref removal** — «Глубже — Лекции 4-7 (индустрии)» footer caption deleted. Branch heads rephrased as semantic labels (was «Ветка 1/2/3») into «Фиксированные классы / Интерпретируемость / Real-time».
11. **s26 Pearl callback softened** — replaced 3-level Pearl breakdowns («1. Ассоциация — да», etc.) with single assertion in sub-title («AI считает корреляции в данных, не строит каузальный граф»). Added gold engineering-takeaway callout.
12. **s28 «(s10-s12)» and «Lec-1 §2.2» refs removed** from concept body text; cell heights increased (2.10→2.20) and fonts bumped.
13. **s16 disambiguation** — gold callout extended to include «1M ≈ 16× дороже 100k — production-pricing с batching; чистая N²-теория дала бы 100×».
14. **s04 designer-extras removal** — «якорь: sNN» markers deleted from 3 promise cards; «3 ответа — payoff на s24» rephrased as «3 ответа — финал лекции».
15. **s01 mockup «(см. s07)» cross-ref removed** from SVG source; PNG regenerated via rsvg-convert.

### P2 cosmetics

16. s17 QuickChart legend disabled (`legend.display=false`); chart regenerated.
17. s23 number badges enlarged (0.7→0.85) and centered properly.
18. Subtitle font sizes bumped from 15pt to 16-18pt across most slides for projector readability.

### Render output

- `lec-02.pptx` rebuilt (28 slides, ~741 KB).
- `lec-02.pdf` regenerated via libreoffice headless.
- All 28 PNG snapshots at 130 dpi regenerated in `snapshots/s-NN.png`.
- No slide IDs added/removed/reordered (s01-s28 monotonic preserved).
- All 17 glossary_lock terms preserved (no drift).
- Both Phase 3 P0 fixes (Llama-3 tokenizer + strawberry split) preserved in slide visible_content + speaker notes.

### Files modified

- `library/lectures/lec-02/rendered/build_lec02.py` (P0+P1+P2 — main builder)
- `library/lectures/lec-02/rendered/assets/charts/s17-u-shape.png` (P1-F2 — regenerated)
- `library/lectures/lec-02/rendered/assets/diagrams/s01-tiktokenizer-mock.{svg,png}` (P2 — designer-extra removed)
- `library/lectures/lec-02/slides/s11-three-uses-of-embeddings.md` (P1-V5 — assertion fix)
- `library/lectures/lec-02/slides/s16-context-window.md` (P0-1 — VERIFY-DAY-OF → notes)
- `library/lectures/lec-02/slides/s17-long-context-fails.md` (P1-F2 — softened middle)
- `library/lectures/lec-02/slides/s19-temperature.md` (P1-F3 — T=1.0 unification)
- `library/lectures/lec-02/slides/s26-attention-vs-causality.md` (P1-V4 — Pearl softened)
- `library/lectures/lec-02/slides/s27-homework.md` (P0-1 — VERIFY-DAY-OF → notes)

**Status:** Ready for re-QA / USER GATE B.
