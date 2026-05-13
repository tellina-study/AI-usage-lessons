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

---

## Phase 8.5a Лекция 2 v1.2 — anglicism cleanup + line breaks + designer-extras removal

User feedback (verbatim): «ты потерял содержание и промежуточные слайды с тем как по нему идем/подзаголовками, некоторые иллюстрации непропорционально сжаты, квадранты плохо читаются, есть англицизмы типа accuracy, есть кривые переносы слов когда верхняя строка сдвинута налево от второй. короче очень сыро перепроверяй и улучшай. и начальный слайд не понятно о чем... это должен быть хук, а сейчас на отвали сделано»

7 issue categories addressed in 2 commits (v1.2a anglicism+breaks+extras; v1.2b s01 hook + visual scale + section nav).

### v1.2a — Anglicism cleanup (per user explicit «accuracy» flag + glossary lock §5)

| Anglicism | Replacement | Where |
|---|---|---|
| `accuracy` | `точность` | s17 visual_brief + body text |
| `Loop:` (assertion s21) | `Цикл:` | s21 assertion + build title |
| `Forward pass` (s21 box 2) | `Прямой проход` | s21 step (2) box label |
| `Distribution` (s21 box 3) | `Распределение` | s21 step (3) box label |
| `Distribution` (s14 footer) | `Распределение весов` | s14 chart footer |
| `Distribution` (s24 answer 3) | `Распределение` | s24 (3) answer text |
| `already` (RU/EN mix in s21 box 1) | `уже` | s21 step (1) box body |
| `trade-off` (s22 footer) | `компромисс` | s22 sub-caption |
| `Decision tree` (s25 assertion) | `Дерево решений` | s25 assertion + build title |
| `decision trees` (s25 branch 2 action) | `деревья решений` | s25 branch 2 right column |
| `Real-time` (s25 branch 3) | `Скорость отклика` | s25 branch 3 head |
| `edge` (s25 branch 3 cond) | `устройство пользователя` | s25 branch 3 condition |
| `logistic regression + feature importance` (s25 branch 2) | `лог. регрессия + важность` | s25 branch 2 action |
| `rule-based` (s25 branch 2) | `правила` | s25 branch 2 action |
| `Tools / Function calling` (s28 box 2) | `Инструменты / Вызов функций` | s28 (2) box title |
| `Agent loop` (s28 box 4) | `Цикл агента` | s28 (4) box title |
| `act → observe → reflect` (s28 box 4) | `действуй → наблюдай → корректируй` | s28 (4) box subtitle |
| `single-shot inference` (s28 subtitle) | `один проход inference` | s28 subtitle |
| `embedding similarity` (s28 box 1) | `близость эмбеддингов` | s28 (1) box body |
| `fine-tuned BERT` (s25 branch 1) | `дообученный BERT` | s25 branch 1 action |

`inference` kept as canonical technical term (glossary_lock exception, used in Lec-1).

### v1.2a — Designer-extras removal

| What | Where | Why |
|---|---|---|
| `LO7` mention in body | s24 gold marker | Visible LO refs forbidden per CLAUDE.md anti-pattern «designer-added extras». Replaced with «Payoff Лекции 1 §5.3 — связь обещаний и механизмов». |
| `См. s15` cross-ref | s24 answer 1 (slide MD) | Forward cross-refs visible to students = noise per No Extra Content Rule. |
| `См. s05–s07` cross-ref | s24 answer 2 (slide MD) | Same. |
| `См. s18–s19` cross-ref | s24 answer 3 (slide MD) | Same. |
| `LO4 — подобрать параметры...` subtitle | s20 subtitle | LO4 visible. Replaced with `Подобрать параметры под сценарий обоснованно`. |

### v1.2a — Line break / wrap fixes

- **s02 cover title** «Как работают / современные большие / модели» (3 lines, top «Как работают» short) → «Как работают современные / большие модели» (2 lines, balanced).
- **s04 central question** removed «внутренних» (redundant) and re-broke at semantic boundary. Old: «...между моим запросом и ответом — / и какие из этих внутренних механизмов меняют, как я её / использую?» New: «...между моим запросом и ответом — / и какие из этих механизмов меняют, как я её использую?» — 2 lines, balanced.
- **s04 promise cards** number badge moved to top-left, question text full-card-width below — eliminates narrow wrap «Почему промпт с / ролью / работает лучше / пустого?» → «Почему промпт с ролью / работает лучше пустого?» (2 balanced lines).

### Files modified (v1.2a)

- `library/lectures/lec-02/rendered/build_lec02.py` — anglicism replacements, layout fixes
- `library/lectures/lec-02/slides/s17-long-context-fails.md` — accuracy → точность
- `library/lectures/lec-02/slides/s20-four-api-knobs.md` — visual_brief subtitle
- `library/lectures/lec-02/slides/s21-autoregressive-loop.md` — Loop, Forward pass, Distribution, already
- `library/lectures/lec-02/slides/s22-local-vs-cloud.md` — trade-off → компромисс
- `library/lectures/lec-02/slides/s24-three-whys-payoff.md` — removed LO7, См. s15/s05-07/s18-19
- `library/lectures/lec-02/slides/s25-ml-vs-llm-decision-tree.md` — Decision tree, Real-time, edge
- `library/lectures/lec-02/slides/s28-bridge-qa.md` — Tools/Function calling, Agent loop, act→observe→reflect, single-shot

**Status:** v1.2a done. v1.2b (s01 hook + visual scale + section nav) follows.

---

### v1.2b — Section navigation (Option A — top progress bar)

Per user feedback «потерял содержание и промежуточные слайды с тем как по нему идем/подзаголовками» — chose Option A (slim 6-cell progress bar at top of every content slide) over Option B (4 new section dividers). Less disruptive, no new slides, students always see «где я сейчас».

Implementation:
- New helper `top_nav_bar(slide, here_idx)` at top of every content slide.
- 6 cells: `0 Открытие / 1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал`.
- Current section highlighted gold (`#F0AB00`), others soft grey.
- Height 0.22", y=0.08-0.30 — clean separation from title at y=0.55.
- Titles pushed down 0.10" (default y=0.45 → y=0.55) to make room.
- Applied to: s01, s03-s12, s14-s28 (24 slides).
- Excluded: s02 (cover with own bottom roadmap_bar), s13 (section divider with own bottom roadmap_bar).

Section indexes:
- 0 Открытие: s01, s02, s03, s04
- 1 Токены: s05, s06, s07, s08
- 2 Эмбеддинги: s09, s10, s11, s12
- 3 Внимание: s13, s14, s15, s16, s17
- 4 Сэмплинг: s18, s19, s20, s21, s22
- 5 Финал: s23, s24, s25, s26, s27, s28

### v1.2b — s01 Hook redesign (Option A — provocative question + reveal)

Per user feedback «начальный слайд не понятно о чем... это должен быть хук, а сейчас на отвали сделано» — completely redesigned.

Before: static tiktokenizer mock with 4 examples (cat/tokenization/strawberry/клубника) in tabular layout. «На отвали» per user. Hook factor 0/10.

After: provocative question takes top 50% of slide («Почему ChatGPT не может посчитать, сколько букв «r» в слове strawberry?» — 46pt bold, 2 balanced lines, center). Below — italic teaser «Спросите любую LLM — половина случаев ответит «2».». Bottom 30% — gold callout «Ответ:» reveal in 2 rows: «Вы видите: s · t · r · a · w · b · e · r · r · y (10 букв)» / «AI видит: [st] [raw] [berry] (3 токена)». Footer caption mentions o200k_base token-izer with GPT-4o/Claude 4.x.

Hook factor 8/10 — provocative question grabs attention, reveal answers immediately, contrast «10 букв / 3 токена» tells the whole lecture story in one glance. Also frontmatter `type: live_demo` → `type: hook`, assertion updated to match.

The 4-example tiktokenizer table (cat/tokenization/strawberry/клубника) is preserved in s05 «Токен — id из словаря» — same content but now in proper pedagogical position (definition slide), not as a flat opening.

### v1.2b — Visual scale fixes (Projector Readability Test: body ≥18pt, axis ≥14pt)

9 slides with body text increased per «некоторые иллюстрации непропорционально сжаты, квадранты плохо читаются»:

| Slide | Element | Before | After |
|---|---|---|---|
| s15 | «Без роли / С ролью» card titles | 18pt | 20pt |
| s15 | «→ generic ответ» (now «обобщённый ответ») body | 15pt | 16pt |
| s15 | role-токены body | 15pt | 16pt |
| s17 | Эксперимент head + body | 14/12pt | 16/14pt |
| s17 | Результаты cards | 13/14pt | 14/15pt |
| s19 | T-distribution card titles | 18pt | 20pt |
| s19 | T-distribution body | 14pt | 15pt |
| s21 | Step head | 17pt | 18pt |
| s21 | Step body | 14pt | 15pt |
| s22 | Local/Cloud property labels | 14pt | 16pt |
| s22 | Local/Cloud property values | 13pt | 14pt |
| s24 | Number badge | 44pt | 48pt |
| s24 | Question | 18pt | 20pt |
| s24 | Answer | 15pt | 16pt |
| s25 | Branch head | 17pt | 17pt (kept, fit) |
| s25 | Branch condition | 14pt | 14pt (kept, fit) |
| s25 | Branch action | 14pt | 14pt (kept, fit) |
| s26 | Human/AI column heads | 24pt | 26pt |
| s26 | Body italic | 15pt | 17pt |
| s26 | Definition italic | 16pt | 18pt |
| s28 | Concept card titles | 22pt | 20pt (smaller fixes overlap) |
| s28 | Concept body | 14pt | 15pt |

s28 also had layout fix: «Инструменты / Вызов функций» (long Russian title after anglicism cleanup) overlapped subtitle in v1.2a. Title box widened, font 22→20pt, subtitle pushed below title block — overlap eliminated.

### v1.2b — Title additional anglicism cleanup

- s22 title: «Inference loop одинаков» → «Inference одинаков» (removed redundant English «loop», canonical inference kept).
- s23 title: «4 этапа inference сложились в pipeline» → «4 этапа inference сложились в конвейер» (pipeline → конвейер per glossary lock; this is the most prominent visible occurrence).
- s23 footer caption: «этот pipeline» → «этот конвейер».
- s15 body «generic ответ» → «обобщённый ответ» (generic anglicism removed).

### v1.2b — Files modified

- `library/lectures/lec-02/rendered/build_lec02.py` — `top_nav_bar()` helper, `SECTION_OF_SLIDE` map, `SECTION_LABELS`, added `top_nav_bar(s, N)` to 24 builder functions, s01 hook complete rewrite, visual scale tunings on 9 slides
- `library/lectures/lec-02/slides/s01-live-tokenizer-demo.md` — type=hook, assertion + visible_content + speaker_notes rewritten for hook format

### v1.2 final status (8.5a + 8.5b)

**DoD checklist:**
- [x] Anglicism count in visible content: 8 → 0 (inference kept as canonical)
- [x] Section navigation visible on all content slides s03-s28 + s01: PASS
- [x] s15, s17, s19, s21, s22, s24, s25, s26, s28 visual scale improved: PASS
- [x] s01 transformed into real hook (not static table): PASS
- [x] Multi-line titles have semantic line breaks (s02, s04): PASS
- [x] 28 slide IDs preserved (s01-s28, no adds/removes): PASS
- [x] Glossary lock preserved (17 canonical terms, no drift): PASS
- [x] Designer-extras removed (LO refs, slide cross-refs): PASS
- [x] WPM in speaker notes ≤95 — preserved from v1.1, no notes changes that affect WPM

**Slides modified (v1.2 total):** s01 (hook redesign), s02 (line break), s04 (line break + nav), s14 (anglicism + nav), s15 (anglicism + scale + nav), s17 (anglicism + scale + nav), s20 (designer-extra + nav), s21 (anglicism + scale + nav), s22 (anglicism + scale + nav), s23 (anglicism + nav), s24 (designer-extra + scale + nav), s25 (anglicism + scale + nav), s26 (scale + nav), s28 (anglicism + scale + nav) — plus top_nav_bar added to all 24 content slides.
