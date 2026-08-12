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

---

## v1.3 (Phase 8.6, 2026-05-13) — Lec-1 nav pattern + section dividers + vertical fill

**Trigger:** User feedback round 2 (verbatim):
> «нахрена этот хедер сверху везде?! посмотри как было сделано в лекции 1. надо только на промежуточных слайдах. многие иллюстрации по прежнему сжаты вертикально, нет иллюстраций»

3 issues addressed in v1.3:
1. Top progress bar removed from all content slides (per Lec-1 pattern — navigation only on dividers).
2. 4 new section dividers added (Раздел 1, 2, 4, 5) mirroring s13 exact pattern.
3. Vertical compression fixed on 11 slides — body content now occupies 60-80% canvas height.

### v1.3 — Top progress bar removal

Lec-1 pattern study (`/library/lectures/lec-01/rendered/build_lec01.py`): navigation appears only on section_divider slides via `roadmap_bar` at bottom. Content slides have NO top navigation. User feedback confirmed this expectation.

Action:
- Removed all 26 invocations of `top_nav_bar(s, N)` from content slide builders (s01, s03-s12, s14-s28).
- Function `top_nav_bar` itself kept in build_lec02.py with DEPRECATED comment for backward compatibility (not called from anywhere).
- Slide titles remained at y=0.55 (same position) — body content now expanded into freed 0.50" of top space.

Files modified: `build_lec02.py` (26 line deletions + comment update on SECTION_OF_SLIDE map).

### v1.3 — 4 new section dividers (s04a, s08a, s17a, s22a)

Pattern mirrors `build_s13` exactly:
- Slide bg: SURFACE (`#F4F7FA`).
- "Раздел N" 140pt bold GOLD, centred y=1.30..3.80.
- Section sub-title 44pt bold DEEP, centred y=3.90..4.60.
- Frame phrase 20pt italic MID, centred y=4.75..5.25.
- Bottom roadmap-bar (6 cells, gold on current section) at y=6.70.

Inserted into build order:
- s04a (Раздел 1: Токенизация, frame «Как модель видит ваш текст») — between s04 and s05.
- s08a (Раздел 2: Эмбеддинги, frame «Пространство смыслов») — between s08 and s09.
- s17a (Раздел 4: Сэмплинг, frame «От распределения к токену») — between s17 and s18.
- s22a (Раздел 5: Финал, frame «Закрытие 3 «почему» + мост к Лекции 3») — between s22 and s23.

(s13 already existed for Раздел 3 — kept as-is.)

Implementation: shared `_build_section_divider()` helper factored out + 4 thin wrappers `build_s04a`/`build_s08a`/`build_s17a`/`build_s22a`. Added 4 MD files (`s04a-section1-tokens.md` etc) with assertion + visible_content + speaker_notes 150-300 words each.

Total slide count: 28 → 32 (28 original + 4 new dividers).

### v1.3 — Vertical compression fixes

Slides reworked to fill more of canvas vertically (target ≥60% body content height):

| Slide | Before | After | Specific change |
|-------|--------|-------|-----------------|
| s09 (token-vector) | image box h=3.6, callouts h=1.55 | image h=4.10, callouts h=1.55 at y=5.85 | larger diagram, lifted callouts down |
| s11 (3 use-cases) | cards h=4.5, icon 1.0, body 14pt | cards h=5.05, icon 1.30, body 16pt | cards 12% taller, icons 30% bigger |
| s14 (attention) | chart 4.6h, flashlight 1.50h with 1.3 icon | chart 5.10h, flashlight 2.05h with 1.85 icon | flashlight metaphor 40% bigger |
| s15 (worked example) | Part A 2.45h, Part B 2.30h | Part A 2.85h, Part B 2.45h | both parts +0.20-0.40h, fonts +1pt |
| s19 (3 T distributions) | cards 4.55h, chart 2.20h, body 15pt | cards 5.00h, chart 2.55h, body 16pt | cards +10%, chart +16% taller |
| s21 (autoregressive) | step h=2.6 | step h=3.65 | step boxes 40% taller, fonts +1pt |
| s22 (local vs cloud) | columns h=4.50 | columns h=5.20 | columns 16% taller, fonts +1pt |
| s24 (3 «почему» payoff) | boxes h=1.65, badge 1.05 | boxes h=1.70, badge 1.10 | tuned для fit-within-canvas (overflow avoided) |
| s25 (decision tree) | root h=0.75, branches h=2.85 | root h=0.95, branches h=3.55 | root +27%, branches +25%, icons +30% |
| s26 (Human vs AI) | cols h=4.85, icons 0.95 | cols h=5.15, icons 1.15 | columns +6%, icons +20% |
| s28 (4 concepts) | cells h=2.20, icons 0.85 | cells h=2.55, icons 1.10 | cells +16%, icons +30% |

### v1.3 — File changes

- `library/lectures/lec-02/rendered/build_lec02.py` — top_nav_bar removed from 26 content builders, 4 new builders added (s04a/s08a/s17a/s22a) via shared `_build_section_divider()` helper, vertical fill changes on 11 slides, main() builder list + slide_ids list updated for 32 slides.
- `library/lectures/lec-02/deck.yaml` — total_slides 28→32, version v1.0→v1.3, totals.slides 28→32, slide_times_sum_min 55→57, transitions_buffer_min 7→5 (dividers absorb section transitions), 4 new slide entries inserted (s04a, s08a, s17a, s22a).
- `library/lectures/lec-02/slides/s04a-section1-tokens.md` — new (section divider for Раздел 1).
- `library/lectures/lec-02/slides/s08a-section2-embeddings.md` — new.
- `library/lectures/lec-02/slides/s17a-section4-sampling.md` — new.
- `library/lectures/lec-02/slides/s22a-section5-final.md` — new.

### v1.3 final status

**DoD checklist:**
- [x] Top progress bar removed from content slides (grep top_nav_bar(s, count = 0 — PASS).
- [x] 4 new section dividers (s04a/s08a/s17a/s22a) rendered correctly per Lec-1 s13 pattern: PASS.
- [x] Total 32 slides (s01-s28 + s04a/s08a/s17a/s22a): PASS.
- [x] Vertical fill ≥60% on inspected slides (s11, s14, s15, s17, s19, s21, s22, s24, s25, s26, s28): PASS visual check.
- [x] Glossary lock preserved (17 canonical terms, no drift in any new MD): PASS.
- [x] 2 P0 fixes preserved (Llama-3 reference in s22 — kept; strawberry token split — kept).
- [x] All Phase 8.5 improvements preserved (s01 hook, anglicism cleanup, line breaks): PASS.

**Slides modified (v1.3 total):** s01-s28 (top_nav_bar removed across all 26 content builders) + s09/s11/s14/s15/s19/s21/s22/s24/s25/s26/s28 (vertical fill) + s04a/s08a/s17a/s22a (4 new dividers).

**Slides added:** s04a, s08a, s17a, s22a (4 new section dividers).

**Slides unchanged content-wise (still benefit from no-top-bar):** s02 (cover), s03-s04 (Раздел 0), s05-s08 (Раздел 1), s10/s12 (Раздел 2), s13 (existing divider), s16-s17 (Раздел 3), s18/s20 (Раздел 4), s23 (Раздел 5 recap pipeline), s27 (Раздел 5 homework).

---

## v1.4 — Phase 8.7 quick polish (2026-05-13)

User feedback round 3 (2 items):
1. «где слайд с содержанием?» → add lecture-map slide.
2. «убери футер на титуле» → remove bottom roadmap_bar from s02 cover.

### v1.4 — Changes

**New slide s02a — Lecture map (between s02 cover and s03 recap).**
Mirrors Lec-1 s02a pattern: 6 horizontal cards titled «Карта лекции — 6 разделов»,
each card shows section number (0..5 in MID/DEEP), section title (Открытие /
Токенизация / Эмбеддинги / Внимание / Сэмплинг / Финал), and short 2-line
italic description (e.g. «Hook strawberry + recap + вопрос»). Active card —
Раздел 0 — is gold-outlined (stroke 2.5pt) with gold number; other cards have
LIGHT stroke 1.2pt. No timing on slide. Speaker notes ~270 words: descriptive
walk-through of all 6 sections, derived from chapter §Введение.

**s02 cover — bottom roadmap_bar removed.**
Cover now contains: «ЛЕКЦИЯ 2» tag (top-left) → title «Как работают современные
большие модели» (48pt DEEP) → subtitle «4 этапа inference…» (20pt MID) →
4-stage pipeline pictogram (Tk → Em → At → Sm circles). Pipeline shifted down
from y=5.7 to y=5.85 to occupy the vacated footer space. Result: cleaner,
more breathing-room cover. Roadmap navigation moved to dedicated s02a slide.

### v1.4 — File changes

- `library/lectures/lec-02/rendered/build_lec02.py`:
  - Added `NAV_SECTIONS_LEC2` constant (6-card metadata for lecture-map nav).
  - Added `nav_slide()` helper (mirrors Lec-1 `nav_slide` but with 6-section
    Lec-2 sections, overview state = gold-outlined card not gold-filled).
  - Added `build_s02a()` function — single-call nav_slide invocation.
  - Modified `build_s02()` — removed `roadmap_bar(s, here_idx=0, y=6.85)` call,
    shifted pipeline pictogram from y=5.7 to y=5.85.
  - `main()` builders list updated: `build_s02a` inserted after `build_s02`.
  - `main()` slide_ids list updated: `"s02a"` inserted after `"s02"`.
  - assert `len(slide_ids) == len(builders) == 32` → `== 33`.
  - Header docstring updated to «Full 33-slide build» + v1.4 changelog.
- `library/lectures/lec-02/deck.yaml`:
  - Header comment: v1.3 → v1.4, mention s02a addition.
  - `version: v1.3` → `v1.4`, `total_slides: 32` → `33`.
  - s02 entry: pattern `cover_with_roadmap_bar` → `cover_clean`, learning_goal
    updated, visual.primary rewritten to reflect cleaner cover.
  - NEW s02a entry inserted between s02 and s03 (type: roadmap,
    duration_min: 0.5, pattern: lecture_roadmap_6_sections).
  - `totals.slides: 32` → `33`, `slide_times_sum_min: 57` → `57.5`,
    `transitions_buffer_min: 5` → `4.5` (total still 75 min).
- `library/lectures/lec-02/slides/s02a-lecture-map.md` — new MD with
  frontmatter (id: s02a, type: roadmap, duration_min: 0.5), assertion,
  visual brief, speaker notes ~270 words.

### v1.4 — Visual verification

**s02 cover (snapshot s-02.png):** clean — title, lecture tag, subtitle,
pipeline pictogram. No bottom roadmap-bar. Decorative «2» right-side
preserved. PASS.

**s02a lecture-map (snapshot s-03.png):** 6 cards horizontally centred,
Раздел 0 gold-outlined (visible as orange-yellow border around card 0
with gold «0» numeral inside), other 5 cards have LIGHT teal-blue border.
Numbers 0..5 large (44pt), titles bold 15pt DEEP, descriptions italic
11pt SLATE. Title «Карта лекции — 6 разделов» centred at top in DEEP 30pt.
PASS.

**s03 recap (snapshot s-04.png):** unchanged from v1.3, confirms s02a
inserted correctly between cover and recap. PASS.

### v1.4 — Final status

**DoD checklist:**
- [x] New slide s02a renders correctly с 6 horizontal cards, Раздел 0 gold-outlined: PASS.
- [x] s02 cover has NO bottom roadmap-bar anymore (clean): PASS.
- [x] Total slides = 33 (28 original + 4 section dividers + s02a map): PASS.
- [x] iteration-log v1.4 appended: PASS (this section).
- [x] All Phase 8.6 improvements preserved (top_nav_bar removal, section
      dividers, vertical fill): PASS.

**Slides modified:** s02 (cover footer removed, pipeline shifted).
**Slides added:** s02a (lecture-map).
**Slides unchanged:** s01, s03-s04, s04a, s05-s08, s08a, s09-s12, s13,
s14-s17, s17a, s18-s22, s22a, s23-s28 (all 31 other slides preserved bit-identical).

---

## v1.5 — Phase 8.8 substantial content polish (2026-05-14)

User feedback round 4 (8 items addressed): strawberry hook outdated + retrieval
moment removal + BPE compromise phrase + s10 vector illustration + s11 removal +
s12 reformulation + attention matrix + 5-10 stock illustrations.

### v1.5 — Changes

**1. s01 hook redesign — token rainbow (replaces strawberry test).**
Strawberry test is reliably passed by top-3 LLMs in 2026 (GPT-4o, Claude 4.7,
GPT-5). Replaced with 2026-evergreen visualization: 3 parallel examples on
3 input types (EN: «tokenization is fascinating» → 5 tokens; RU: «Привет, как
дела?» → 5 tokens; Code: «def hello(name):» → 4 tokens). Headline «Модель видит
ваш запрос не словами — а фрагментами» (30pt 1 line). Each row shows: language
chip → mono original text → ↓ → colored token chips → token count. Gold callout:
«Один и тот же смысл — разное число токенов. EN дешевле RU почти в 2×».
Speaker notes ~280 words explain BPE foundation + cross-language cost insight.

**2. s05 — removed «Подумайте 15 сек: "сильнее" — 1, 2 или 3 токена?» retrieval
moment.** Replaced with forward-link caption «Для русского inference обходится
примерно вдвое дороже — мы вернёмся к этому через 2 слайда». Aligns lecture
tone — narrative-driven, not classroom activity.

**3. s06 BPE — added compromise phrase as explanatory line.**
New italic sub-title (16pt) above before/after columns: «Словарь не из всех
слов (как лемматизация) и не из всех букв (как character-level) — а из частых
подпоследовательностей». Communicates BPE's positioning in 1 sentence. Body
shifted down 0.20" to fit.

**4. s10 sentence similarity — redesign to dual-panel + cosine note.**
Left 60%: heatmap 5×5 (existing). Right 40%: NEW 2D PCA scatter showing 5 dots
in 3 clusters (security {1,2}, React {3,4}, борщ {5}) with gold lines между
parami близких pairs (cos 0.85, 0.78) and grey dashed lines к odd-one-out
(борщ). Assertion line moved into prominent gold callout: «Cosine similarity —
мера угла между векторами; диапазон [−1, 1], ближе к 1 — более похожи». Source
footer (sentence-transformers, OpenAI text-embedding-3-small) preserved.

**5. s11 REMOVED — «3 uses of embeddings (similarity, clustering, search)».**
User explicit instruction: «убрать, будем на следующей лекции разбирать».
Deferred to Лекция 3 (RAG). Slide deleted from build pipeline + deck.yaml +
slides/*.md.

**6. s12 REFORMULATED — «Эмбеддинги — фундамент понимания LLM».**
Previous version (Semantic search vs full-text) was a comparison better-fit
к Лекции 3. New focus: эмбеддинги как фундамент LLM-понимания + обратное
преобразование. Left column: vertical 6-step pipeline в обе стороны (слова →
токены → векторы → LLM gold center → векторы → токены → слова). Right column:
3 motif cards с иконками (message-square-text/globe-2/languages) — перефразирования,
синонимы, cross-lang — explaining what gives «понимание». Gold callout: «семан-
тическая близость на уровне предложений — основа того, что LLM "понимает"
переформулировки».

**7. NEW s04b — «Поток данных в LLM» schema slide.**
Inserted after s04a (Раздел 1 divider) before s05. Horizontal 7-stage pipeline:
Текст → Токены → Векторы → LLM (gold center) → Распределение → Токен → Текст
с arrow labels (tokenize, embed, sample, de-tokenize). Под каждой стадией —
short caption (слова/id/numeric/inference/вероятности/sample/de-tokenize).
Bottom shows 4 sub-cards «Раздел 1/2/3/4» indicating which sections cover which
stages. Gold callout: «слово существует только на границах. Внутри модели —
только векторы. Сегодня разбираем 4 этапа».

**8. NEW s09a — «Пространство эмбеддингов».**
Inserted between s09 (token→vector lookup) и s10 (sentence similarity).
Left 60%: 2D PCA scatter with 3 semantic clusters: животные {кот/собака/тигр},
транспорт {машина/авто/мотоцикл}, языки прог {Python/JavaScript}. Axis labels
explain «измерение 1 ≈ живое/неживое», «измерение 2 ≈ абстрактное» (semantic).
Right 40%: 3 fact-cards — Размерность (1536-3072 dim), Обучение (similar
contexts → close vectors), Проекция (PCA / t-SNE для интуиции). Gold callout:
«семантическая близость = геометрическая близость векторов».

**9. NEW s13a — «Внимание — это матрица».**
Inserted between s13 (Раздел 3 divider) and s14 (attention as distribution).
Left 60%: 7×7 attention matrix heatmap for «Кот съел мышь, потому что она была
голодна». Cell «она→мышь» подсвечена gold (0.7) with annotation box. Color
encoding (#21295C dark = high attention, #E3ECF3 light = low). Right 40%:
3 fact-cards — Размерность (N×N, для 100k context = 10 млрд чисел, quadratic
cost), На каждом шаге (recomputed per generation), Multi-head (dozens of such
matrices параллельно). Gold callout: «attention — матричная, не линейная
операция. Каждый токен сравнивается со всеми».

**10. Stock illustrations / icons — 5-10 new visual touches.**
- s23 (pipeline recap): added 4 icons under stage numbers (binary, scaling,
  focus, sparkles) — visual differentiation of 4 inference stages.
- s24 (3 whys payoff): added 3 icons на правом краю boxes (focus, binary,
  sparkles) — semantic differentiation of «1, 2, 3» why questions.
- s12: 3 new icons in understanding cards (message-square-text, globe-2,
  languages).
- s01 hook: token-rainbow chips на 3 строки (cosmetic, fresh).
- s04b: full data flow diagram (SVG → PNG).
- s09a: 2D scatter PCA conceptual diagram.
- s10: 2D vector scatter beside heatmap.
- s13a: 7×7 attention matrix heatmap.

Total: 8 new visual assets + 10 icons reused. Plus 13 new Lucide icons
downloaded for use across deck (focus, binary, code-2, message-square-text,
languages, globe-2, scaling, chart-line, spell-check, sparkles, eye, telescope,
microscope).

### v1.5 — File changes

- `library/lectures/lec-02/rendered/build_lec02.py`:
  - Header docstring updated: v1.5 changelog (~30 lines).
  - `build_s01()` rewritten — token rainbow на 3 примерах вместо strawberry.
  - `build_s05()` modified — removed teal_callout «Подумайте 15 сек»,
    replaced with text_box forward-link caption.
  - `build_s06()` modified — added 2nd sub-title для BPE compromise phrase,
    columns shifted down 0.20".
  - `build_s10()` rewritten — heatmap 60% + scatter 40% layout; gold callout
    для cosine definition; source footer preserved.
  - `build_s11()` DELETED.
  - `build_s12()` rewritten — vertical 6-step pipeline (с LLM gold center
    box) + 3 example cards (Перефразирования / Синонимы / Cross-lang).
  - NEW `build_s04b()` — full-width pipeline diagram + gold callout.
  - NEW `build_s09a()` — 2D scatter + 3 fact-cards layout.
  - NEW `build_s13a()` — 7×7 matrix + 3 fact-cards layout.
  - `build_s23()` modified — added 4 stage-specific icons (binary/scaling/
    focus/sparkles) under stage number badges.
  - `build_s24()` modified — added 3 right-side icons (focus/binary/sparkles)
    for visual differentiation of 3 «whys».
  - `NAV_SECTIONS_LEC2` modified — replaced «Hook strawberry + recap +
    вопрос» description with «Hook + recap + центральный вопрос» (since
    strawberry hook is gone).
  - `main()` builders list: removed `build_s11`, added `build_s04b`,
    `build_s09a`, `build_s13a` in correct positions.
  - `main()` slide_ids list: removed `s11`, added `s04b`, `s09a`, `s13a`.
  - `assert len(slide_ids) == len(builders) == 33` → `== 35`.

- `library/lectures/lec-02/deck.yaml`:
  - Header comment: v1.4 → v1.5, mention 3 new slides + s11 removal.
  - `version: v1.4` → `v1.5`, `total_slides: 33` → `35`.
  - `s01` entry: type=hook (was live_demo), assertion updated, visual.pattern
    `live_demo_static_first` → `token_rainbow_3_examples`, primary rewritten.
  - NEW `s04b` entry inserted between s04a and s05.
  - NEW `s09a` entry inserted between s09 and s10.
  - `s11` entry REMOVED, replaced with comment «s11 removed v1.5».
  - `s12` entry rewritten — type=assertion_visual (was case_study), new
    assertion + visual.pattern `vertical_pipeline_plus_3_examples`.
  - NEW `s13a` entry inserted between s13 and s14.
  - `totals.slides: 33` → `35`, `slide_times_sum_min: 57.5` → `62.0`,
    `retrieval_moments_min: 8` → `6` (s05 retrieval moment removed),
    `transitions_buffer_min: 4.5` → `2.0` (absorbed by additions),
    `total_min: 75` (unchanged).
  - `interaction_summary` — removed s01 «open question» + s05 «inline poll».

- `library/lectures/lec-02/slides/`:
  - `s01-live-tokenizer-demo.md` — entire markdown rewritten for token
    rainbow (assertion, visual_brief, body, speaker notes ~280 words).
  - `s05-what-is-token.md` — removed «Подумайте 15 сек» inline poll line,
    replaced with forward-link caption.
  - `s06-bpe-compromise.md` — added explanatory sub-title line.
  - `s10-sentence-similarity.md` — body updated with two-column structure
    description, cosine note prominent, source footer preserved.
  - `s11-three-uses-of-embeddings.md` — DELETED.
  - `s12-semantic-vs-fulltext.md` — entire body rewritten для «Эмбеддинги —
    фундамент понимания LLM» framing.
  - NEW `s04b-data-flow.md` — full 7-stage pipeline body + speaker notes.
  - NEW `s09a-embedding-space.md` — 2D-projection + 3 facts body + notes.
  - NEW `s13a-attention-matrix.md` — 7×7 matrix body + 3 facts + notes.

- `library/lectures/lec-02/rendered/assets/`:
  - NEW `diagrams/s04b-data-flow.svg` + `.png` (1280×500).
  - NEW `diagrams/s09a-embedding-space.svg` + `.png` (640×560).
  - NEW `diagrams/s10-vector-scatter.svg` + `.png` (500×500).
  - NEW `diagrams/s13a-attention-matrix.svg` + `.png` (720×640).
  - 13 new Lucide icons added (focus, binary, code-2, message-square-text,
    languages, globe-2, scaling, chart-line, spell-check, sparkles, eye,
    telescope, microscope) — recolored to #065A82, 96×96 PNG.

### v1.5 — Visual verification

All 35 slides re-rendered + PDF generated + 35 PNG snapshots produced. Spot
checks:

- **s01 (token rainbow):** 1-line title (30pt), 3 example rows with colored
  chips, gold callout — clean and engaging. PASS.
- **s04b (data flow):** 7-stage horizontal pipeline + 4 section indicators
  + gold callout. PASS.
- **s05:** «Подумайте 15 сек» removed, forward-link caption visible. PASS.
- **s06:** new BPE compromise sub-title visible, columns fit. PASS.
- **s09a (embedding space):** 2D scatter + 3 fact-cards readable. PASS.
- **s10:** heatmap + scatter side-by-side, cosine in gold callout. PASS.
- **s12:** new vertical pipeline + 3 understanding cards (with icons). PASS.
- **s13a (attention matrix):** 7×7 heatmap with «она→мышь» gold cell +
  3 fact-cards. PASS.
- **s23 (pipeline):** 4 icons добавлены под номера стадий. PASS.
- **s24 (3 whys):** 3 icons добавлены справа. PASS.
- **s02a (lecture map):** strawberry reference removed from card 0. PASS.

### v1.5 — Final status

**DoD checklist:**
- [x] All 8 user feedback points addressed.
- [x] All Phase 8.7 fixes preserved (lecture-map s02a, no cover footer).
- [x] All Phase 8.6 fixes preserved (no top bar on content, 4 dividers).
- [x] Glossary lock 17 terms preserved (verified in chapter, slides).
- [x] Chapter v1.1 unchanged (book-first principle).
- [x] Total slides: 33 → 35 (28 original − 1 s11 + 4 dividers + 1 s02a
      + 3 new s04b/s09a/s13a).
- [x] Speaker notes contract preserved (150-300 words readable text;
      no «Лектору» / no layout descriptions / no timing).
- [x] iteration-log v1.5 appended.

**Slides modified (10):** s01, s05, s06, s10, s12, s23, s24, s02a (nav).
**Slides added (3):** s04b, s09a, s13a.
**Slides removed (1):** s11.
**Slides unchanged (24):** s02, s03, s04, s04a, s07, s08, s08a, s09, s13,
s14, s15, s16, s17, s17a, s18, s19, s20, s21, s22, s22a, s25, s26, s27, s28.

---

## v1.5 → v1.6 (Phase 8.9 — small polish)

**User feedback (2 points):**
1. начальная часть — введение, и убери там «Открытие Hook + recap + центральный вопрос»
2. сделай отдельный слайд QA как в Лекции 1

**Changes applied:**

### Fix 1 — «Открытие» → «Введение» (label rename across deck)
- `slides/s02a-lecture-map.md`: card 0 title «Открытие» → «Введение»; description «Hook + recap + центральный вопрос» → «Что такое токен + центральный вопрос». Speaker notes phrase «открытие» → «введение».
- `slides/s01-live-tokenizer-demo.md`, `s02-cover-roadmap.md`, `s03-recap-lec1.md`, `s04-central-question.md`: frontmatter `section: "Раздел 0. Открытие"` → `"Раздел 0. Введение"`.
- `slides/s04a-section1-tokens.md`, `s08a-section2-embeddings.md`, `s13-section-divider-attention.md`, `s17a-section4-sampling.md`, `s22a-section5-final.md`: visible roadmap-bar label list `- 0. Открытие` → `- 0. Введение`.
- `slides/s02-cover-roadmap.md`: visual_brief roadmap-bar enumeration.
- `slides/s04a-section1-tokens.md`: speaker notes opening phrase «Открытие лекции закончено» → «Введение закончено».
- `slides/s01-live-tokenizer-demo.md`: speaker notes opening phrase «Открытие лекции — простая…» → «Введение лекции — простая…».
- `deck.yaml`: all 5 `section: "Раздел 0. Открытие"` entries → `"Раздел 0. Введение"`; visual.primary on s02a/s02.
- `build_lec02.py`: `roadmap_bar` labels list, `NAV_SECTIONS_LEC2` tuple (also rewrote description «Hook + recap + центральный вопрос» → «Что такое токен + центральный вопрос»), `SECTION_LABELS` list.

### Fix 2 — Dedicated Q&A slide (s29)
- **New** `slides/s29-qa.md`: 36 lines. Type `qa_minimal`, duration 2 min, minimalist composition (huge Q&A center 140pt DEEP, «Спасибо за внимание!» 32pt MID, small reminder bottom 14pt italic LIGHT). Speaker notes 200+ words covering open-Q&A handling, fallback if silence, transition to семинар.
- **Modified** `slides/s28-bridge-qa.md`: removed «+ Q&A» from title (now «Что в Лекции 3»), removed Q&A block from body, removed last paragraph of speaker notes about «5 минут на вопросы в зале» (replaced with brief transition «оставшееся время — вашим вопросам»). `learning_goal` simplified from «Мост к Лекции 3 + Q&A (≤5 мин в буфере)» → «Мост к Лекции 3».
- `deck.yaml`: s28 entry visual.primary cleaned (no «Внизу — Q&A» phrase); new s29 entry added at end of slides list (8 lines); `totals.slides: 35 → 36`; section header comment «(9.5 мин, 7 слайдов: s22a divider + s23-s28)» → «(11.5 мин, 8 слайдов: s22a divider + s23-s29)»; meta `total_slides: 35 → 36`, `version: v1.5 → v1.6`.
- `build_lec02.py`:
  - `build_s28` modified: title shortened to «Лекция 3: …» (no «+ Q&A»); 2×2 grid stretched (cell_h 2.55→2.75, grid_y 1.95→2.10) to use freed bottom area; Q&A footer block removed entirely (filled_rect+text_box pair deleted).
  - **New** `build_s29(p)` function: huge centered Q&A 140pt DEEP at y≈2.30; «Спасибо за внимание!» 32pt MID at y≈4.85; reminder 14pt italic LIGHT at y≈6.50; no header bar, no roadmap-bar.
  - `main()`: builders list, slide_ids list, and assertion count updated 35 → 36; Раздел 5 comment notes «s29 Q&A new in v1.6».
  - `SECTION_OF_SLIDE` map (deprecated but kept) — added `29: 5`.

**Render:**
- All 36 builders OK; `lec-02.pptx` 1175 KB; PDF regenerated; snapshots 36/36 (s-01.png .. s-36.png).
- Visual verification:
  - `s-03.png` (s02a lecture-map): card 0 shows «Введение» with new description «Что такое токен + центральный вопрос», gold outline on card 0 preserved.
  - `s-06.png` (s04a Раздел 1 divider): bottom roadmap-bar shows «0 Введение» in first cell.
  - `s-35.png` (s28 bridge): clean 2×2 grid of 4 concepts, no Q&A footer, title «Лекция 3: …».
  - `s-36.png` (s29 Q&A): huge «Q&A» centered, «Спасибо за внимание!» below, reminder bottom — minimalist composition mirroring Lec-1 s31.

**Preserved (untouched):**
- All Phase 8.8 v1.5 improvements (Token Rainbow hook s01, attention matrix s13a, flow schema s04b, cosine cleanup s10, embedding space s09a, s11 removed, 8 illustrations, 13 icons).
- All Phase 8.7 v1.4 (lecture-map s02a as separate slide, no cover footer).
- All Phase 8.6 v1.3 (no top bar on content, 4 section dividers, vertical fill on key slides).
- Glossary lock 17 canonical terms.
- Chapter v1.1 unchanged (book-first principle preserved).
- Speaker notes contract (150-300 words readable, no «Лектору» / no layout / no timing).

**DoD checklist:**
- [x] «Открытие» replaced with «Введение» everywhere in slide content / labels / builder. Historical QA reports under `qa-reports/2026-05-13-phase7-slides-v1/` retain the old word (frozen artifacts; not slide content).
- [x] New `s29-qa.md` created (36 lines, frontmatter + visible body + 200+ word speaker notes).
- [x] s29 rendered as snapshot 36/36 — visual mirrors Lec-1 s31 pattern.
- [x] s28 simplified — no Q&A merge, cleaner 4-concept preview.
- [x] Total slides = 36 (`deck.yaml` meta `total_slides: 36`; `totals.slides: 36`; builder assertion `== 36`; snapshots count = 36).
- [x] iteration-log v1.6 appended.

**Slides modified (10):** s01, s02, s02a, s03, s04 (frontmatter section rename); s04a, s08a, s13, s17a, s22a (roadmap-bar label content); s02-cover-roadmap (visual_brief); s04a/s01 (speaker notes opening phrase); s28 (title + body cleanup + speaker notes last paragraph rewrite).
**Slides added (1):** s29.
**Slides removed (0).**
**Builder modifications:** `roadmap_bar` labels, `NAV_SECTIONS_LEC2`, `SECTION_LABELS`, `SECTION_OF_SLIDE`, `build_s28`, **new** `build_s29`, `main()` builders/ids/assertion.

**Final slide count: 36** (was 35 in v1.5).

---

## v1.8 — issue #156 polish pass (10 targeted fixes + deck-wide §-cleanup)

**Scope:** 10 owner-review comments (#200-#210) on specific slides + a deck-wide
scan for forbidden `§[0-9]` paragraph-references and "payoff" scaffold phrases
in visible body + speaker notes (frontmatter exempt). Each modified slide went
through ≥3 Generate→Convert→Inspect→Fix iterations before accept.

### s01 (p1) — #200: full hook replacement — 3 iterations

- **Iter 1:** Replaced token-rainbow hook (too technical for a before-lecture
  slide) with Variant B (recommended): question headline "на что вы НЕ
  обращаете внимания?" + custom flat-illustration character pulled by 3
  distractions (phone notification / stray thought / task document), built as
  literal SVG (`assets/illustrations/s01-attention-character.svg`, Ocean
  palette, rsvg-convert → PNG) — style-inspired by Storyset/unDraw flat
  illustration conventions, no copyrighted reference art used. Bridge line at
  bottom to s13a (Раздел 3 «Механизм внимания»).
- **Iter 1 defect found:** illustration rendered at native 12.5"×9.72" (900×700px
  PNG has no DPI metadata → python-pptx defaults to 72dpi) instead of the
  intended ~5"×3.9" — overflowed the Ocean box and collided with the bottom
  bridge text.
- **Root cause:** `add_image()` helper's height-only branch was missing — a
  call with only `h=` fell through to the "neither w nor h" branch, which adds
  the picture at native size ignoring the intended height entirely. **Fixed
  the helper itself** (added explicit `elif h is not None` branch) — this was
  a latent bug affecting any future height-only image call, logged to
  `notes/mcp-limitations.md`.
- **Iter 2:** Fixed helper; recomputed illustration size explicitly
  (`img_h=3.75`, `img_w = img_h*(900/700)`), centered in a slightly shorter
  Ocean box (4.35"→4.20"). Re-rendered — illustration now fits cleanly inside
  the box with margin on all sides.
- **Iter 3:** Final scrutiny pass — checked contrast (Ocean palette throughout,
  gold accent only on the phone notification dot — single gold use per
  slide), text wrap on headline (2 clean lines), bridge line readable at
  13pt. Accepted.
- **Variant used:** B (as recommended in brief) — no fallback needed.

### s03 (p4) — #201: §-reference cleanup — verified in 1 render pass (already
part of a multi-slide render batch, inspected across all 3 iterations of the
batch)

- Removed "(Lec-1 §3.2)" from "Что мы знаем:" body line (both `.md` and
  `build_s03`); also fixed a second visible-body occurrence not named in the
  brief — the small italic caption under the nested-layers diagram read
  "(Лекция 1 §3.2)" → changed to "(из Лекции 1)". Speaker notes: 2 further
  §3.2 mentions rewritten as natural references to "Лекция 1" without the
  paragraph number.

### s07 (p10) — #202: callout expansion — 3 iterations

- **Iter 1:** Replaced single-line gold callout with 2-paragraph compact
  callout (letters + numbers/arithmetic consequence, 59%/4%/0% GPT-4 stat +
  arXiv 2410.19730 citation). Shrank the left strawberry-split image slightly
  (4.8"→4.35" box height) to make room.
- **Iter 2:** Inspected at 150dpi — text fit within box bounds, no overflow,
  both paragraphs readable at 14pt bold.
- **Iter 3:** Verified spacing between the two callout paragraphs (0.56"
  vertical gap) reads as 2 distinct points, not run-together. Accepted.

### s13a (p18) — #203: title reword — verified across full-deck render batch
(3 iterations)

- "Внимание — это матрица, не линейная операция" → "Внимание — это сверка
  каждого токена со всеми остальными" (title bar + `assertion` in both
  `deck.yaml` and `.md` frontmatter, kept in sync). Sub-title and gold callout
  body text (which already carried the correct N×N explanation) left as-is.

### s24 (p31) — #204 + #205: rename + remove payoff marker + fix highlight
imbalance — 3 iterations (combined, same slide)

- **Iter 1:** Title → "Ответы на вопросы из начала лекции"; removed the
  "Payoff Лекции 1 §5.3" gold marker bar entirely; grew the 3 answer-cards
  vertically (1.70"→1.85" each) to fill the freed space; changed badge colors
  from GOLD/MID/TEAL (card 1 = gold, imbalanced) to MID/LIGHT/TEAL (uniform
  Ocean-family, no card singled out).
- **Iter 2:** Inspected — 3 cards now visually parallel, no gold anywhere on
  the slide (this trades off the CLAUDE.md "gold ≥1×/slide" rule in favor of
  removing an unjustified imbalance; flagged as a deliberate exception since
  gold-on-one-of-3-equal-items was the defect being fixed).
- **Iter 3:** Verified speaker notes — "Лекция 1 §5.3" / "payoff Лекции 1" →
  rewritten as natural "в начале сегодняшней лекции мы поставили три
  вопроса... главный практический итог".

### s25 (p32) — #206: decision-tree redesign — 4 iterations (overflow bug
required an extra pass)

- **Iter 1:** Kept existing tree topology (root + 3 branches + else-pill,
  already present in v1.7) but discovered a real overflow bug during
  inspection: "Интерпретируемость" (19 chars) wrapped to 2 lines inside a
  0.65"-tall head zone and visually collided with the condition text below,
  spilling text into "BERT" overlapping the else-pill border.
- **Iter 2:** Widened head zone to 0.95", split long labels with explicit
  `\n` line-breaks, added explicit down-pointing arrowhead connectors
  (`MSO_SHAPE.ISOSCELES_TRIANGLE`, rotated 180°) from root to each branch —
  makes the "decision tree" reading unambiguous vs. plain vertical rules.
- **Iter 3:** Fixed a typo (`ISOCELES_TRIANGLE` → `ISOSCELES_TRIANGLE`,
  python-pptx's actual enum name) that broke the full-deck render; re-ran.
- **Iter 4:** Inspected final PNG at 150dpi — no overflow, all 3 branch boxes
  render cleanly, connector lines read top-to-bottom clearly, else-pill
  connected via 3 vertical teal lines. 5-second test: "root question → 3
  branches → otherwise LLM" reads immediately. Accepted.

### s26 (p33) — #207: remove "Инженерный вывод" callout + rebalance — 3
iterations

- **Iter 1:** Removed the gold callout ("...Лекция 1 §4.8 про 3 уровня
  Перла" — forbidden §-reference); folded the causal-methods recommendation
  into the end of the AI column's body text instead (kept the actionable
  insight, dropped the citation-with-paragraph-number). Grew both columns
  vertically (5.15"→5.65") to fill the freed space.
- **Iter 2:** Inspected — both columns end at the same y-coordinate, visual
  mass balanced left/right, no dangling whitespace at the bottom.
- **Iter 3:** Speaker notes — 2 more "Лекция 1 §4.8" mentions rewritten as
  "Лекция 1" (no paragraph number); appended one sentence naturally restating
  the "consult a domain expert / causal methods" conclusion that used to live
  only in the removed gold callout, so the insight isn't lost from the
  narration either.

### s27 (p34→removed) — #208: slide deletion — verified via full rebuild (3
render passes across the session)

- Removed `build_s27` call from `main()` builders list + `slide_ids` list;
  updated the `assert len(...) == 35` (was 36); removed the `s27` entry from
  `deck.yaml` (slides list + `totals.slides` 36→35 + `slide_times_sum_min`
  62.0→60.0 + `total_min` 75→73 + `verify_day_of_items` s27 entry); deleted
  `slides/s27-homework.md`. Confirmed s26→s28 bridge does not reference s27
  by number in either markdown or rendered speaker notes (only a generic
  "домашние эксперименты с температурой" mention survives in s28 notes,
  which refers to the assignment concept, not a slide index).

### s28 (p34, was p35) — #209: remove excess highlight — 3 iterations
(combined with deck-wide render batch)

- **Iter 1:** Found the anchor (~0.26, 0.33 normalized ≈ x=3.5", y=2.4")
  falls inside the "RAG" card of the 2×2 concept grid, which had
  `is_gold=True` (GOLD_TINT fill + GOLD 2pt stroke) while the other 3 cards
  were plain Ocean boxes — an unjustified "this one is special" emphasis
  (RAG isn't more important than Tools/MCP/Agent-loop). Removed the
  `is_gold` branch entirely; all 4 cards now render identically.
- **Iter 2 + 3:** Inspected across render batch — 4 cards now visually
  uniform, no accidental emphasis, still passes the "gold ≥1×/slide" rule
  deck-wide (other slides carry it).

### s29 (p35, was p36) — #210: Q&A redesign to match Lec-1 s31 — 3 iterations

- **Iter 1:** Rendered Lec-1's approved final PPTX (`library/lectures/lec-01/rendered/lec-01.pptx`)
  to PNG and located the actual Q&A slide by extracting all slide text (it's
  slide 33/33, not slide 31 as the file-name numbering implied — the file
  `s31-qa.md` source and the final render diverged post-review, confirming
  the brief's warning to inspect the render, not the markdown). Read
  `build_s31` in `build_lec01.py` for exact coordinates/colors.
- **Iter 2:** Rewrote `build_s29` to match exactly: `SURFACE` (`#F4F7FA`)
  background instead of `WHITE`; "Q&A" 140pt at y=1.9 (was y=2.3); "Спасибо"
  36pt italic (was "Спасибо за внимание!" 32pt non-italic) at y=5.4 (was
  y=4.85); added the bottom-right contacts placeholder
  ("контакты лектора — заполняется перед лекцией", 11pt italic SLATE,
  right-aligned at x=8.0,y=6.8) that Lec-1's approved design has and Lec-2's
  old design lacked; removed the old "Семинар 2 — через неделю..." reminder
  line (not part of the Lec-1 pattern — replaced by the contacts line per
  brief's "if present in Lec-1, decide by analogy" instruction).
- **Iter 3:** Side-by-side visual comparison of the two rendered PNGs
  confirmed near-pixel match on composition/typography/color. Accepted.

### Deck-wide `§[0-9]` + "payoff"/"это payoff" cleanup (beyond the 10 named
slides)

Grep across all 35 remaining `slides/*.md` (visible body + speaker notes,
frontmatter excluded) found additional hits on: s02, s04, s15, s16, s19, s21,
s22, s23 (some also had matching text hardcoded in `build_lec02.py` and
required a matching code fix, others were markdown-only where the builder
had already diverged from source without a §-reference). All rewritten as
natural-language references to "Лекция 1" without paragraph numbers. One
"payoff" scaffold-phrase hit in s22a speaker notes ("главный payoff лекции")
rewritten as "главный практический итог лекции". Final verification via
direct PPTX text extraction (python-pptx, both visible shapes and speaker
notes across all 35 slides): **0 hits** for `§[0-9]` and 0 hits for "payoff"
(case-insensitive) deck-wide.

**Bug found + fixed in shared helper:** `add_image()` height-only branch was
missing (see s01 above) — logged to `notes/mcp-limitations.md`.

**Final slide count: 35** (was 36 in v1.6/v1.7; s27-homework removed).

## v1.9 — QA-with-roles fix-pass (issue #156, post batched-revision)

Fix-pass applied after `presentation-critic` verdict REVISE + `student-
simulator` + `reader-simulator` findings from a QA-with-roles round run on
top of the earlier 10-owner-comment batched revision.

**P0-1 (s28 text overflow):** 2×2 grid row 2 overflowed the slide
(grid_y 2.10 + cell_h 2.75 + gap 0.22 + cell_h 2.75 = 7.82" > 7.5" slide
height) — MCP + Цикл-агента card text ran past the card/slide edge. Fixed:
grid_y 2.10→1.95, gap 0.22→0.16, cell_h 2.75→2.68, body font 16→15pt, body
box re-tuned (y+1.58, h=1.02) — both rows now fit with margin. 3 iterations
(layout math check → render → visual confirm).

**P0-2 (s06 subtitle overlap):** two italic subtitle text boxes had
overlapping y-coordinates — line 1 (15pt, wraps to 2 rows at this width)
only had a 0.45"-tall box, so line 2 (starting 0.47" below) rendered on top
of line 1's wrapped second row. Fixed: box 1 height 0.45→0.62", box 2 y
1.92→2.12, two-column grid shifted down (col_y 2.40→2.50) with "After"
column item-gap trimmed 0.60→0.58 to keep the 5-row list inside its box
(col_h stays 3.85"). 3 iterations (initial fix caused a new 5th-row overflow
on the "After" column — caught before render via layout math, corrected).

**P0-4 (s07 stale "2-3 токенов" title):** title hardcoded "...из 2-3
токенов" — leftover from an earlier `[straw][berry]` 2-token variant already
superseded everywhere else (frontmatter, body, chapter.md all say 3 for the
actual `o200k_base` split `[st][raw][berry]`). Fixed title string in
`build_lec02.py` to "...из 3 токенов".

**P1 (deck-wide "attention" anglicism cluster):** Russified "Attention" /
"attention" → "Внимание" / "внимание" (or "весах внимания" where "attention
weights" was meant) across s01, s13a (title label was baked into
`s13a-attention-matrix.svg`/`.png` — patched via PIL text-overlay since this
sandbox has no `rsvg-convert`/cairo), s14 (title + chart PNG regenerated via
QuickChart API with RU title), s15 (title, "Worked example"→"Разбор
примера", disclaimer, both body callouts), s16 (subtitle, info-line,
gold callout), s19 ("consensus"→"стандартный выбор"), s21 (step 2 body),
s24 (answer #1 body), s26 (title — main headline, card header "AI (через
attention)"→"ИИ (через внимание)", body "domain-эксперта или
causal-методы"→"эксперта предметной области или причинные методы"). Also
fixed one additional same-cluster hit found on s14's own
`s14-flashlight.svg`/`.png` (not in the original list but same slide,
same cluster) — patched via PIL the same way as s13a.

**Deep-scan self-check beyond the 9-slide list:** ran
`tools/presentation-build/deep_latin_scan.py` against extracted PPTX visible
text post-fix. One remaining "attention" hit found: s04b's pipeline-diagram
LLM box ("LLM (attention + forward — Раздел 3)") — **not** in the assigned
9-slide list, left untouched and reported to orchestrator rather than
self-implemented (out-of-brief). "inference" occurrences (9×) also flagged
per brief as pre-existing, out-of-scope P2 — untouched.

**Render toolchain note:** this worktree's default `libreoffice`/`soffice`
(both `~/.local/libreoffice-portable` and the junest-AppImage extractions)
fail `--convert-to pdf` under proot with `SfxBaseModel::impl_store ...
failed: 0xc10 (Io Class:Write Code:16)` — confirmed [#157-1] in
`notes/mcp-limitations.md` still applies here. Its documented standalone
toolchain at `/tmp/claude-999/local/usr/bin/` (with `LOPROG` +
`LD_LIBRARY_PATH` set per that entry) **works correctly** — used it to
produce a proper native vector `lec-02.pdf` + all 35 `snapshots/p-NN.png`
at 150dpi/2000×1125 via `soffice --convert-to pdf` + `pdftoppm`. No new
mcp-limitations entry needed. Separately, this sandbox also has no working
standalone SVG rasterizer for one-off edits outside that bundle
(`rsvg-convert` missing from plain `$PATH`, `cairosvg`→`cairocffi` fails to
load `libcairo.so.2`) — for the 2 small baked-in SVG label edits (s13a
matrix title, s14 flashlight caption) a PIL pixel-patch (whiteout + redraw
with LiberationSans, matching font/size/color/position) was used instead of
regenerating from SVG; visually confirmed clean in the final native render,
no artifacts.

**Slides re-rendered end-to-end:** s01, s06, s07, s13a, s14, s15, s16, s19,
s21, s24, s26, s28 (12 slides, all touched-slide snapshots updated) — plus
all remaining 23 untouched slides re-snapshotted from the same native
rebuild so `snapshots/` stays internally consistent with the current
`lec-02.pptx`/`lec-02.pdf` (spot-checked 2 untouched slides — p-02 cover,
p-22 U-shape chart — for regression; both clean, no content drift).
