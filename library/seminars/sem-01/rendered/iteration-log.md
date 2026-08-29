# Iteration log — Семинар 1 «Знакомство: курс, группа и мой опыт с AI»

**Continued in `iteration-log-round3.md`** — round-3 point-fix round
(2 independent P0 TODO-leak findings + 2 P1 + 1 optional bonus fix,
2026-08-07 QA pass) — split here to stay under the 600-line doc limit.

Build script: `library/seminars/sem-01/rendered/build_sem01.py` (python-pptx direct,
adapted from `library/lectures/lec-01/rendered/build_lec01.py` design patterns).
Render toolchain: `/tmp/claude-999/pptx_to_png.sh` (bootstrapped LibreOffice + pdftoppm).

11 slides total. Deck built and inspected as a whole per iteration (single build script,
single render pass) rather than slide-by-slide MCP rebuilds — python-pptx allows targeted
edits to individual `build_sNN()` functions without touching unaffected slides, so the
"iteration" unit below is a full deck rebuild + full visual re-inspection, with fixes
scoped to the specific slides that showed problems.

---

## Iteration 1 (initial build)

- Generated icon assets: 9 industry icons (white, 72px, for hero tiles) + 9 industry icons
  (LIGHT teal, 72px, for s02 mini-row) + ~20 content icons (MID blue 96px / TEAL 72px /
  DEEP 64px) via Lucide CDN → sed recolor → rsvg-convert. All from
  `library/seminars/sem-01/rendered/assets/icons/src/*.svg` (downloaded once, recolored
  per-use via `assets/icons/recolor.sh`).
- Generated 2 QuickChart PNGs for s04 (Stack Overflow grouped bar, ВЦИОМ grouped bar),
  `version=4` explicit per known QuickChart gotcha ([#55-render-2] in mcp-limitations.md).
- Built all 11 slides in one pass, rendered to PDF/PNG @150dpi.
- **Inspected all 11 PNGs visually.** Found:
  - s01, s02, s03, s06, s08, s09, s10, s11 — clean on first pass (Ocean palette
    consistent, motif present, gold ≥1×, hierarchy clear, no accent lines, no
    centered body text, hero ≥40% on s01/s11).
  - **s04 BUG:** right panel (ВЦИОМ) — gold callout box overlapped the "Источник:"
    citation line below it (chart too tall, callout too close to panel bottom).
  - **s05 BUG:** gold callout (Deloitte methodology note) overlapped the panel's
    bottom border — visible cut-off / ghost text underneath.
  - **s07 ISSUE:** large empty whitespace at bottom of each text card (card height
    5.05" too tall for the 2-3 sentence texts) — Visual Mass Balance violation
    (30%+ empty vertical space reads as "missing content").
- **Verdict:** continue — 3 concrete fixes queued (s04, s05, s07).

## Iteration 2 (fix s04/s05/s07 geometry)

- **s04 fix:** reduced ВЦИОМ chart height ratio (0.62→0.46 of panel width), tightened
  gap before gold callout, reduced callout font 11.5→11pt to guarantee clearance
  above the source citation line. Verified via computed geometry (Python arithmetic)
  before re-render: gap changed from -0.14" (overlap) to +0.58" (clear).
- **s05 fix (attempt 1):** enlarged top panel (top_h 3.05→3.25), moved callout down.
  Re-rendered — **new bug surfaced:** stat labels (previously using literal `\n` inside
  a single `text_box` run) did not wrap to 2 lines as intended — `\n` inside a
  python-pptx run does not render as a line break, so labels rendered as single-line
  and got clipped by the gold callout box moving up into them. **New MCP-limitation-adjacent
  finding logged separately below.**
- **s07 fix:** reduced card height 5.05"→4.35", enlarged text font 13→15pt, shortened
  quotes slightly, tightened vote-chip position — still overflowed on iter2 (text1 card's
  last line touched the AI/человек chip row).
- Re-rendered. **Inspected s04 (fixed clean), s05 (new bug: single-line labels clipped
  by callout), s07 (still overflowing, less severe).**
- **Verdict:** continue — s05 needs the `\n`-in-textbox root cause fixed, not just
  repositioned; s07 needs another height/font pass.

## Iteration 3 (root-cause fix s05, finalize s07)

- **s05 fix (root cause):** replaced literal `\n` in stat label strings with plain
  single-line text (removed the manual line-break attempt entirely — labels are short
  enough to read as one line at 11.5pt in a 3.4"-wide column). Enlarged top panel once
  more (top_h 3.25→3.65) and recomputed all vertical offsets via Python arithmetic
  before rendering — confirmed +0.11" clearance between label bottom and callout top,
  and re-verified bottom 3-column framework row still fits within the 7.5" canvas
  (bot_h 1.85" — enough for icon + title + 2-line description at 11.5pt).
- **s07 fix (final):** card height 4.35"→4.75", text box height ratio adjusted
  (`ch - 1.95`), grid_y raised slightly (1.75) to keep total composition centered.
  Verified via arithmetic that footer icon block (foot_y = grid_y+ch+0.2 = 6.7) still
  clears the 7.5" bottom margin.
- Re-rendered all 11 slides. **Inspected s04, s05, s07 — all three bugs resolved,
  no new overlaps.** Re-inspected s01, s02, s08, s09, s11 as regression check — unaffected,
  still clean.
- **50% zoom projector-readability pass** on all 11 slides (PIL downscale to 1000×563,
  simulating back-row viewing distance): all text, chip labels, axis-equivalent labels,
  icon labels remained legible. No slide failed.
- **Verdict: ACCEPT for all 11 slides.** 3 iterations minimum met; s04/s05/s07 got
  a 3rd targeted fix pass; s01/s02/s03/s06/s08/s09/s10/s11 clean since iteration 1
  and re-verified unaffected across iterations 2-3 (regression-checked, not just
  assumed stable).

---

## Per-slide summary

| Slide | Iterations | Final verdict |
|---|---|---|
| s01 hero_cover | 3 (clean since iter1, re-verified iter2/3 regression-free) | ACCEPT |
| s02 assertion_visual | 3 (clean since iter1) | ACCEPT |
| s03 poll_reveal | 3 (clean since iter1) | ACCEPT |
| s04 assertion_visual (dual stat) | 3 (bug iter1 → fixed iter2) | ACCEPT |
| s05 assertion_visual (stat+framework) | 3 (bug iter1 → partial fix iter2 → root-cause fix iter3) | ACCEPT |
| s06 assertion_visual (failure grid) | 3 (clean since iter1) | ACCEPT |
| s07 comparison (3-text voting) | 3 (whitespace iter1 → improved iter2 → finalized iter3) | ACCEPT |
| s08 assertion_visual (quiz list) | 3 (clean since iter1) | ACCEPT |
| s09 summary (5-point memo) | 3 (clean since iter1) | ACCEPT |
| s10 reflection_question (profile card) | 3 (clean since iter1) | ACCEPT |
| s11 hero_closing | 3 (clean since iter1) | ACCEPT |

---

## Schema Readability Checklist — applicable slides

s05's bottom 3-column framework (кто отвечал / как спрашивали / кто выигрывает) is the
closest thing to a `schema_matrix`-adjacent pattern in this deck (3 parallel category
columns). Checked against README §5.5 subset relevant to simple parallel-column layouts:

- Fill rate: 3/3 columns filled with icon + title + description — 100%.
- Icons per column: yes (users / message-circle-question / scale), one per column,
  same Lucide family, TEAL recolor, consistent 72px size.
- Single-line headers: yes ("Кто отвечал?" etc., ≤4 words each).
- Font ≥12pt axis-equivalent (titles 14.5pt), ≥11.5pt body — meets minimum.
- Max 2 lines per cell description — yes.
- Single language (RU only) — yes.

s08's quiz list and s09's memo list are simple numbered-row patterns, not one of the
7 named schema subtypes (matrix/quadrant/layered/cycle/pipeline/timeline/architecture) —
Schema Readability Checklist not mandatory for these, but informally verified: number
badges consistent size, single-line-per-row where possible, ≥14pt body throughout.

## 5-Second Test (per slide, applied at iteration 3 final accept)

- s01: "Курс о AI по многим отраслям, семинар знакомства" — PASS (hero collage +
  title communicate this instantly).
2. s02: "17+17 занятий, от основ к отраслям, 3 контроля" — PASS.
3. s03: "Опрос про AI-опыт, живое голосование" — PASS.
4. s04: "Используют больше AI, но доверяют меньше" — PASS (bar charts + assertion align).
5. s05: "Проверяй источник статистики" — PASS (3-column framework reinforces headline).
6. s06: "Расскажи свою историю AI" — PASS (hand icon + grid instantly readable).
7. s07: "Угадай кто автор" — PASS (3 text cards + AI/человек chips self-explanatory).
8. s08: "Проверь себя на мифах об AI" — PASS (verно/неверно chips × 6 rows).
9. s09: "5 уроков на будущее" — PASS (numbered list, #1 gold-highlighted).
10. s10: "Заполни профиль, сравним позже" — PASS (3 fields + bridge callout).
11. s11: "Спасибо, дальше — Лекция 1" — PASS (hero + Лекция 1 chip).

All 11 slides PASS 5-Second Test at final accept (iteration 3).

---

## New finding for `notes/mcp-limitations.md` (candidate, not yet logged there)

**python-pptx `text_box` helper + literal `\n` inside a single run does not create a
visual line break reliably in LibreOffice rendering** — when composing a multi-line
label by putting `\n` inside a single `r.text = "line1\nline2"` run (as opposed to
`text.add_paragraph()` per line), LibreOffice's PDF export did not consistently honor
the line break, causing text to overflow its box or overlap adjacent elements when the
box height was sized assuming 2 lines. **Workaround used:** either (a) use separate
paragraphs (`tf.add_paragraph()`) for each line, or (b) as done here, avoid manual line
breaks and size the box for single-line auto-wrap instead. This is now added to
`notes/mcp-limitations.md` as a render-toolchain finding (see separate edit).

---

# v2 rebuild — major redesign (2026-08-07)

Full deck rebuild per owner brief: 11 slides → 20 slides, new YOLO hand-raise poll
mechanic (replaces old 6-card multi-select), 5-category calibration game (5 → 10
slides), real Wikimedia Commons hero photos replacing icon-mock hero, roadmap +
checkpoint-mechanics slides added, profile-card slide (s10 old) deleted per owner
("если студент должен заполнить — выпиливаем"). New numbering s01-s20. Old
`slides/s02..s11-*.md` deleted and replaced; `s01`/`s11`(→`s20`) kept their file
identity but content substantially rewritten.

Builder `build_sem01.py` extended in place (not rewritten from scratch) — all
existing helpers (`ocean_box`, `chip`, `icon`, `gold_callout`, `text_box`,
`text_runs`, `add_image`) reused as-is. New helpers added: `multipara_box` (proper
paragraph-per-line, avoiding the `\n`-in-single-run bug documented above),
`dashed_box` (for the "live audience data" slot on s05), `vote_badge` (small
hand+camera badge repeated on every poll slide), `industry_photo_grid` (replaces
old `industry_tile_grid` — real JPGs instead of icon tiles), `code_card` (dark
monospace code block inside an Ocean rounded box, used in s12/s13).

## 6-tier image acquisition — s01/s20 hero (industry photo collage)

Wikimedia Commons (Tier 2) delivered **7/8 industries** as real CC/public-domain
photos on the first attempt — no need to fall through to tiers 3-6 for those 7:

| Industry | File | Source | License |
|---|---|---|---|
| Медицина | `s01-medicine-davinci.jpg` | `File:New Da Vinci Xi.jpg` (da Vinci Xi surgical robot) | CC BY-SA 4.0 |
| Финансы | `s01-finance-nyse.jpg` | `File:Trading floor of the New York Stock Exchange...LCCN2011632435.tif` | Public domain |
| Транспорт | `s01-transport-yandex.jpg` | `File:Moscow, Yandex self-driving Hyundai Sonata, Aug 2025...jpg` | CC0 |
| Производство | `s01-manufacturing-kuka.jpg` | `File:KUKA Industrial Robot KR10 SCARA.jpg` | Public domain (small, 250×350 — max resolution available, used as-is for small collage tile) |
| Разработка / IT | `s01-datacenter.jpg` | `File:BalticServers data center.jpg` | CC BY-SA 3.0 |
| Логистика | `s01-logistics-ocado.jpg` | `File:Ocado warehouse bots.jpg` | CC BY-SA 4.0 |
| Наука | `s01-science-microscope.jpg` | `File:Researcher looks through microscope (1).jpg` | Public domain |

**Кибербезопасность — best-effort, no real photo found.** Attempted 2 Commons
searches (`security operations center cyber analyst screens`, `network operations
center monitoring screens`) — both returned only PDF documents (government reports,
academic papers), zero usable photos. Attempted 2 more targeted searches (`hacker
laptop hoodie code screen`, `computer security padlock code screen photo`) — zero
results at all. **4 search attempts total, documented honestly** — fell back to a
single icon tile (`shield-check`, MID fill) for this 1/8 industries, per brief's
explicit allowance ("если реально не нашёл фото... оставь 1 icon-плитку с пометкой
best effort"). All images resized to max 1000px via PIL before embedding (original
Commons downloads ranged 785×1000 to 1280×1631) — kept render fast, no visible
quality loss at slide scale.

Same 7 photos + same 1 icon tile reused on s20 (hero_closing) per brief's explicit
"тот же реальный-фото мотив" instruction — `Разработка/IT` (datacenter) tile
gold-framed as the bridge highlight to Lecture 1.

## Calibration game sources (5 categories, s08-s17)

| # | Category | Real sample | Source | AI sample |
|---|---|---|---|---|
| 1 | Художественный текст | Viktor Pelevin, *Generation П* (1999), verbatim quote per brief | Provided in brief, not independently re-verified (well-known novel excerpt) | Designer-written, philosophical/reflective register on sleep/reality theme, explicitly logged as AI-generated-for-the-exercise (not a real AI tool call — Claude-authored text standing in for "AI output" per brief's own instruction) |
| 2 | Технический текст | Python official docs, `for` statement paragraph | docs.python.org/3/tutorial/controlflow.html — verified verbatim via WebFetch, exact match confirmed | Designer-written `while`-statement explanation in matching documentation register |
| 3 | Код | `requests` library `prepare_method()` | github.com/psf/requests (MIT) — verified via WebFetch against `src/requests/models.py`; **note: current HEAD has since added type hints** (`method: str \| None`, `-> None`) not present in the brief's quoted version — used the brief's exact quoted text (predates type-hint addition) | Designer-written `normalize_header_name()`, matching scale/style |
| 4 | Картина | Ivan Shishkin + Konstantin Savitsky, «Утро в сосновом лесу» (1886) | Wikimedia Commons, already downloaded pre-session to `assets/screenshots/s07-shishkin-real.jpg` (5668×3840); resized to 1600×1084 (`s07-shishkin-real-web.jpg`) for faster embed | **No real AI-generated image produced** — honestly represented as a text description of the hypothetical prompt/output per brief's explicit instruction not to fake a file that doesn't exist |
| 5 | Визуализация данных | Our World in Data, "Share of the population using the Internet" (Russia vs World line chart, 1990-2025) | Fetched directly from OWID Grapher PNG API (`ourworldindata.org/grapher/share-of-individuals-using-the-internet.png?tab=chart&country=OWID_WRL~RUS`) — real chart, real ITU/World Bank data, CC-BY | QuickChart-generated line chart on invented-but-plausible "AI assistant adoption" data, explicitly labeled on-slide as "вымышленные данные" |

## Bug fixes found during visual-loop (iterations 4-6 of the overall deck, first 3
iterations of this v2 rebuild)

### Iteration 4 (first full v2 render + inspection)
Inspected all 20 PNGs. Found:
- **s02 BUG:** "Сегодня" flag marker positioned with negative x-offset (`today_x -
  0.55`, `today_x - 1.1` off a `today_x` of ~0.5) — rendered flag icon clipped at
  the left slide edge, "Сегодня" label text missing entirely (off-canvas).
- **s09 (fiction calibration answer) ISSUE:** Visual Mass Balance violation — card
  height 4.4" sized for the longest possible text but actual quotes only filled
  ~35% of each card, leaving ~65% empty vertical space below the text.
- **s11 (technical calibration answer) ISSUE:** same class of issue, less severe —
  tradeoff block auto-sized to fill remaining canvas height (2.45") for 2 lines of
  text.
- **s15 BUG:** attribution caption ("общественное достояние · Wikimedia Commons")
  rendered as an overlay directly on top of the dark/shadowed area of the Shishkin
  painting — WCAG contrast failure, text barely legible against the image.
- Also confirmed **no other slides** had comparable issues on first pass — s01,
  s03-s08, s10, s12-s14, s16-s20 clean.

### Iteration 5 (fix s02/s09/s15; partial fix s11)
- **s02 fix:** replaced the broken icon+text combo with a single `chip()` pill
  ("Сегодня", GOLD fill) positioned at `tl_x` (in-bounds) + a small flag icon beside
  it. Also tightened the cross-cutting-themes box height (was auto-sized to fill
  remaining canvas = excess bottom whitespace; fixed to `themes_h = 2.35`).
- **s09 fix:** reduced card height 4.4"→3.15", added a counter-weight visual (2
  large `quote` icons framing the gold conclusion callout) plus a new 2-column
  "grounding row" (long-form vs short-fragment imitation difficulty) below it —
  fills the freed vertical space with substantive content instead of just shrinking
  the card.
- **s11 fix (partial):** reduced card height 3.55"→2.75" — improved but tradeoff
  block still had visible empty space below the 2-line text (not caught as
  fully-resolved until iteration 6).
- **s15 fix (root cause):** moved the attribution caption from an overlay-on-image
  position to a dedicated line below the image on the card's light surface —
  correct WCAG contrast. Also replaced the `\n`-in-single-run caption title (which
  happened to render correctly here, but is the exact known bug class from
  `notes/mcp-limitations.md` [#sem01-render-1]) with `multipara_box` as a
  preventive fix, not because it had visibly failed this time.
- Re-rendered, re-inspected s02/s09/s11/s15 — s02/s09/s15 fully resolved; s11 still
  showed a Visual Mass Balance gap in the tradeoff block.

### Iteration 6 (finish s11 fix; full regression check)
- **s11 fix (root cause):** replaced the auto-sized (`7.2 - tw_y`) tradeoff block
  with a fixed compact height (1.35"), added small icons beside each column
  (`file-code` MID / `sparkles` GOLD) for visual anchoring, and added a new gold
  "lesson" callout row below it ("Урок: скорость генерации — не то же самое, что
  надёжность источника") — same counter-weight pattern as s09, closes the
  remaining whitespace with substantive content rather than arbitrary padding.
  Audited s13/s17 (same tradeoff-block code pattern) — their auto-sized heights
  (1.95"/1.98") were reasonable for their taller code/chart cards above, no fix
  needed there.
- Re-rendered all 20 slides. **Inspected s02, s09, s11, s15 — all four bugs fully
  resolved, no new regressions.** Re-inspected s01, s03-s08, s10, s12-s14, s16-s20
  as regression check — unaffected.
- Ran automated checks: deep latin-token scan (88 unique tokens, all either code/
  quoted-English-source content legitimately part of the calibration game, or
  brand/UI-convention markers — 0 genuine anglicism hits in narrative prose), no-
  timing/no-methodology grep (0 hits in visible body), anti-groupwork grep (1 false
  positive: "исследовательская команда" refers to Our World in Data's research
  team, not student groupwork), scaffold-leak grep (0 hits), `duration_min` sum
  (exactly 75.0).
- **Verdict: ACCEPT for all 20 slides.** Minimum 3 iterations met for every touched
  slide (most got exactly 3: iter4 finds it, iter5 fixes root or partial, iter6
  finishes/regression-checks); s01/s03-s08/s10/s12-s14/s16-s20 clean since iter4 and
  re-verified regression-free across iter5-6.

## Per-slide summary (v2, 20 slides)

| Slide | Iterations | Final verdict |
|---|---|---|
| s01 hero_cover (real photos) | 3 (clean since iter4) | ACCEPT |
| s02 assertion_visual (roadmap) | 3 (bug iter4 → fixed iter5) | ACCEPT |
| s03 process (checkpoint mechanics) | 3 (clean since iter4) | ACCEPT |
| s04 poll_reveal (YOLO hand-raise) | 3 (clean since iter4) | ACCEPT |
| s05 assertion_visual (dual stat + live slot) | 3 (clean since iter4) | ACCEPT |
| s06 assertion_visual (critical reading framework) | 3 (clean since iter4) | ACCEPT |
| s07 assertion_visual (experience sharing) | 3 (clean since iter4) | ACCEPT |
| s08 comparison (calibration 1 Q) | 3 (clean since iter4) | ACCEPT |
| s09 assertion_visual (calibration 1 A) | 3 (issue iter4 → fixed iter5) | ACCEPT |
| s10 comparison (calibration 2 Q) | 3 (clean since iter4) | ACCEPT |
| s11 assertion_visual (calibration 2 A) | 3 (issue iter4 → partial iter5 → fixed iter6) | ACCEPT |
| s12 comparison (calibration 3 Q, code) | 3 (clean since iter4) | ACCEPT |
| s13 assertion_visual (calibration 3 A, code) | 3 (clean since iter4) | ACCEPT |
| s14 comparison (calibration 4 Q, image) | 3 (clean since iter4) | ACCEPT |
| s15 assertion_visual (calibration 4 A, image) | 3 (bug iter4 → fixed iter5) | ACCEPT |
| s16 comparison (calibration 5 Q, dataviz) | 3 (clean since iter4) | ACCEPT |
| s17 assertion_visual (calibration 5 A, dataviz) | 3 (clean since iter4) | ACCEPT |
| s18 assertion_visual (quiz, 7 statements) | 3 (clean since iter4) | ACCEPT |
| s19 summary (memo, 5 points) | 3 (clean since iter4) | ACCEPT |
| s20 hero_closing (real photos + TODO) | 3 (clean since iter4) | ACCEPT |

## Automated checks (final, post-iter6)

- `duration_min` sum across all `slides/*.md`: **75.0** (exact).
- Deep latin-token scan (`tools/presentation-build/deep_latin_scan.py` on extracted
  PPTX visible text): 218 occurrences / 88 unique tokens — reviewed manually, all
  are either (a) verbatim quoted English source material intentionally part of the
  calibration game content itself (Python docs quote, `requests` code, OWID chart
  labels), or (b) brand/UI markers (`TODO`, `LIVE`, `AI`). **0 genuine narrative
  anglicisms.**
- No-timing/no-methodology grep on visible body: **0 hits** (patterns: `\d+\s*мин`,
  «Время раздел», «Тайминг», «методическ», «педагогическ», «На этом этапе
  студент», «Лектору», «Преподавателю», «Вы здесь»).
- Anti-groupwork grep: 1 false positive («исследовательская команда» = Our World in
  Data's research team, not student groupwork); 0 genuine hits.
- Scaffold-leak grep (`[VERIFY-DAY-OF]`, `[FACT-CHECK]`, `LO[1-9]`, `§X.X`, `→ sNN`,
  `(sNN)`): **0 hits.**
- Speaker notes word count: 12/20 slides in the 100-300 word range; 8/20 (all
  calibration-game slides, s08-s17) fall below 150 words individually — but this is
  a structural consequence of splitting each of the 5 categories into a Q-slide +
  A-slide pair (~1.3 min each); **combined per-category-pair word counts land in
  186-224 words**, matching the intended "one unit of content" scope of the 150-300
  target. Reported to orchestrator as a known/accepted design tradeoff, not
  silently normalized.

## New finding for `notes/mcp-limitations.md`

No new limitation found in this session — reused the already-documented
[#sem01-render-1] finding preventively (via `multipara_box`) rather than
re-discovering it.

---

# Round 2 revisions (owner feedback, post-Iteration-6 baseline)

Baseline: `snapshots/iter6-*.png`, 20 slides, ACCEPT verdict (see Iteration 6 above).
This round applies a large owner-feedback brief: s06 (Deloitte) deleted entirely →
19 slides, full renumber s07→s06...s20→s19, 5 calibration reveal-slides rewritten
to a positive/task-dependent AI framing, A/B allocation shuffled on 3/5 categories,
real Velasco painting replacing Shishkin/Savitsky, real RU Python docs text
replacing English docs.python.org excerpt, quiz trimmed 7→6 statements with 2
spoiler-glosses removed + 1 new determinism statement, memo trimmed to match,
AI/human pill-chip buttons removed from all 10 calibration slides, vote badge
removed from all poll/calibration slides, s05 rebuilt from 3-panel/2-live-slot to
2-panel+4-live-card layout, s01 title de-duplicated, s02 theme order changed, s06
(experience-sharing) top invite region removed + 2 categories renamed.

## Iteration 7 (structural rebuild + first pass content rewrite)

- **Structural:** deleted `slides/s06-critical-reading-framework.md`; renamed
  `s07-*.md`→`s06-*.md` through `s20-*.md`→`s19-*.md` (ascending order, safe
  because target `s06` was freed by the deletion before the rename chain reached
  it); updated `id:` frontmatter in each renamed file to match new filename;
  verified `id` == filename-prefix for all 19 files programmatically (0
  mismatches). Rebuilt `build_sem01.py` from the captured pre-edit content
  (reconstructed via Write after an in-place `sed` line-count error corrupted the
  file mid-edit — recovered from the two full `Read` calls made at session start,
  verified `python3 -m py_compile` clean immediately after).
- Removed `build_s06()` (Deloitte slide) entirely; renamed `build_s07()..build_s20()`
  → `build_s06()..build_s19()`; updated every internal `load_notes("sNN")` call to
  match the new id (grep-verified: each `build_sNN` calls `load_notes("sNN")` with
  matching NN); updated `BUILDERS` list to 19 entries.
- `duration_min` redistribution: deleted s06 carried 8 min. Applied +3 to s05
  (8→11, new 4-slot live panel needs more airtime) and +5 to experience-sharing
  (17→22, becomes s06, already the longest block and benefits from more live
  discussion time) per brief's suggested split. Verified sum == 75.0 exactly via
  `awk` over all `slides/*.md` `duration_min:` fields.
- Rewrote `deck.yaml` from scratch — 19 slides, ids/files/patterns/assertions all
  matching the new build script and slide content.
- Downloaded Velasco painting (see dedicated acquisition note below).
- Generated 5 missing recolored icons (`sparkles-1C7293-72`, `clock-1C7293-72`,
  `layers-028090-72`, `target-028090-72`, `database-028090-64`) via
  `assets/icons/recolor.sh` — `layers.svg` didn't exist in `assets/icons/src/`,
  fetched fresh from Lucide CDN (`jsdelivr.net/npm/lucide-static@latest`).
- First full rebuild + render (`snapshots/iter7-*.png`, 19 slides). Inspected s01,
  s02, s05, s06 first (highest-risk per brief). **Found:** s05 4-slot live panel
  (2×2 grid inside one dashed box) had ~0.3" of dead vertical whitespace per row
  (row height 0.93" for single-line text) — Visual Mass Balance issue, read as
  "half-empty box."
- **Verdict:** continue — s05 layout needs rework (individual cards, not bare grid).

## Iteration 8 (s05 rework + full chip/badge removal pass)

- **s05 fix:** replaced the 2×2 grid-inside-one-dashed-box with 4 independent
  mini-cards (own `dashed_box` outline each, side-by-side). Gives each of the 4
  poll questions its own visual weight instead of floating in a single tall
  container. Re-rendered — clean, no dead whitespace, Visual Mass Balance restored.
- Removed all `chip(s, ..., "AI", ...)` / `chip(s, ..., "человек", ...)` pill-button
  pairs from the 5 question-slides (s07, s09, s11, s13, s15 in new numbering) —
  grep-verified `chip(s.*"AI"` count 0 in `build_sem01.py` after this pass. Each
  card's text/image now uses the freed vertical space (extended height or centered
  anchor) instead of leaving a gap where the chips used to be.
- Fixed a latent bug introduced during the Write-reconstruction of `build_s14`
  (Velasco reveal slide): a stray `cx + pad if False else cx + 0.22` conditional
  leftover from drafting — caught by re-reading the diff before first render,
  fixed to plain `cx + 0.22` before any snapshot was taken (never visible in a
  rendered artifact).
- Re-rendered all 19 slides (`snapshots/iter8-*.png`). Inspected s01, s02, s05,
  s06, s07, s09, s11, s13, s15 (question slides), s08/s10/s12/s14/s16 (reveal
  slides), s17 (quiz), s18 (memo). All clean at this pass — no chips, no badge, no
  LIVE tag, no inline instruction text, positive-framing tradeoff blocks read
  correctly, Velasco image renders with correct attribution.
- **Verdict:** continue — need a 3rd critical pass (deep grep + 50%-zoom + slides/*.md
  content sync, which was still stale relative to the rendered deck at this point).

## Iteration 9 (deep grep + slides/*.md content sync)

- Ran deep-latin-token scan on extracted PPTX visible text: 132 occurrences / 44
  unique tokens, all either (a) verbatim Python code / quoted English-language
  content that is the calibration-game's own subject matter (the `requests`
  function, `while`/`for` keywords inline in the AI-generated Russian explanation
  text), or (b) brand/source markers (`Stack Overflow`, `ВЦИОМ`-adjacent `Our World
  in Data`, `digitology.tech`, `MIT license`, `TODO`) — 0 genuine narrative
  anglicisms, consistent with round-1's accepted 88-unique-token baseline.
- Ran no-timing/no-methodology/scaffold-leak greps directly on extracted PPTX
  visible text (not just source `.md`) — 0 hits on all 3 categories.
- **Found:** `slides/*.md` frontmatter/Visual/Speaker-notes sections were still
  describing the OLD (round-1) design for every touched slide — deck.yaml also
  still had the deleted s06 and old 20-slide numbering. This is a real content gap
  (brief explicitly requires updating `## Visual` + frontmatter + `deck.yaml` to
  match the rendered design, not just the Python code).
- Rewrote `slides/s01-hero-cover.md` (eyebrow dedup note), `s02-course-roadmap.md`
  (theme order in Visual + Speaker notes), `s04-poll-questions.md` (stale
  `s09–s18` badge cross-ref fixed to describe the badge's removal), `s05-*.md`
  (full Visual + Speaker notes rewrite for 4-card layout), `s06-experience-sharing.md`
  (removed invite-region description, renamed 2 categories, added round-2 changelog
  note), `s07`/`s09`/`s11`/`s13`/`s15` (question slides: badge/chip removal notes),
  `s08` (unaffected, no A/B change, no visual claim needed updating),
  `s10`/`s12`/`s14`/`s16` (reveal slides: full positive-framing tradeoff rewrite +
  A/B-flip documentation + Velasco/RU-docs source swap documentation), `s17`
  (quiz: 7→6 statements, spoiler-gloss removal, new determinism statement, full
  speaker-notes rewrite with the owner-provided explanation text), `s18` (memo:
  removed gold-highlight + footer caption descriptions, added new determinism
  item). Rewrote `deck.yaml` in full (19 slides).
- Re-ran all grep checks post-.md-edit — 0 genuine hits on scaffold-leak, LIVE,
  "впишите", "Утечка данных", "docs.python.org" (only in explanatory "was removed"
  prose now), "Шишкин/Савицкий" (only in explanatory prose, deck.yaml assertion
  for s15 still needs updating — caught and fixed in iteration 10, see below),
  "самая частая ошибка"/"унесите с собой" (only in explanatory prose).
- **Verdict:** continue — found deck.yaml still had a stale s15 assertion
  referencing Shishkin (leftover from copy-paste before the full rewrite);
  needed one more full-file rewrite pass.

## Iteration 10 (final deck.yaml rewrite + regression sweep)

- Rewrote `deck.yaml` completely (not patched) to guarantee no stale
  cross-references survived — verified via grep afterward: 0 hits for "Шишкин",
  "Савицкий", "shishkin" anywhere in `deck.yaml`.
- Re-verified: 19 slides in `deck.yaml` == 19 files in `slides/` == 19 `id:`
  frontmatter values, all matching filename prefixes (programmatic check, 0
  mismatches). `duration_min` sum == 75.0 exactly.
- Rebuilt (`python3 build_sem01.py`, 0 warnings — all icon assets present) and
  re-rendered full deck (`snapshots/iter10-*.png`, 19 slides).
- **Full regression sweep** — re-inspected every slide changed across iter7-9
  (s01, s02, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18,
  s19) plus s03/s04 (untouched, checked for accidental collateral damage from the
  renumbering — none found). All stable, no new issues.
- 50%-zoom projector-readability check on s05 (highest layout-complexity slide
  this round): all text, chart labels, and the 4 live-card labels/underscores
  remained legible at 1000×562 downscale. Pass.
- Final deep-latin-token scan + no-timing/no-methodology/scaffold-leak greps
  re-run on the final PPTX extract — same clean results as iteration 9 (0 genuine
  hits on all forbidden categories).
- **Verdict: ACCEPT for all 19 slides.** Minimum 3 iterations met for every
  touched slide (iter7 finds/fixes structural issues, iter8 fixes s05 layout +
  removes chips/badges, iter9 syncs slides/*.md content + fixes a latent code bug,
  iter10 does final deck.yaml rewrite + full regression sweep). s03/s04 untouched
  by content brief but re-verified regression-free after the renumbering
  mechanical changes.

## Velasco painting acquisition (Tier 2 success, first attempt)

Brief requested honest 6-tier acquisition documentation. Actual result: **Tier 2
(Wikimedia Commons API) succeeded on the first real attempt** — no fallback
needed.

1. Queried Wikimedia Commons API directly for the target file
   (`José María Velasco - The Valley of Mexico from the Santa Isabel Mountain
   Range - Google Art Project.jpg`) via
   `action=query&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json` with
   `-A "Mozilla/5.0 ..."` user-agent. API responded immediately with a valid
   `thumburl` (1280×879px JPEG thumb).
2. Downloaded the thumb URL directly — 233KB JPEG, verified via `file` command
   (`JPEG image data, baseline, precision 8, 1280x879`) and visually confirmed via
   `Read` tool: panoramic valley/lake/mountain landscape with small human figures
   in foreground, no prominent buildings — matches the brief's description
   exactly (Popocatépetl-adjacent snow-capped peaks visible on the horizon).
3. Saved to `assets/screenshots/s13-velasco-real.jpg` (using the new post-renumber
   slide id, per brief instruction to name the file after the final slide id, not
   the original s14/s07 numbering) + `s13-velasco-real.url` with the Commons page
   URL for traceability.
4. No retry needed — the fallback candidates (Metlac Ravine, other Barbizon-school
   painters) documented in the brief were **not** needed.

## Grep verification results (final, iteration 10)

```
рука + камера / рука+камера  → 0 active uses (helper fn unused in BUILDERS;
                                 remaining hits are explanatory "was removed" prose)
LIVE                          → 0 active uses (remaining hits are code comments /
                                 explanatory prose documenting the removal)
впишите / впишите сюда        → 0 active uses (1 hit is explanatory prose)
Утечка данных                 → 0 hits anywhere
docs.python.org                → 0 active uses (2 hits are explanatory prose
                                 documenting the swap to the RU translation)
Шишкин / Савицкий / shishkin  → 0 hits in build_sem01.py or deck.yaml;
                                 remaining hits are explanatory prose in
                                 s13-*.md/s14-*.md documenting the swap to Velasco
самая частая ошибка / унесите с собой → 0 active uses (explanatory prose only)
chip(s.*"AI"                  → 0 (regex count)
```

All 8 mandatory grep checks pass with 0 genuine hits (all surviving matches are
either code comments or `.md` prose explicitly documenting what was removed —
legitimate historical/explanatory text, not active leaks).

## Round-3 point fix — s18 memo item 4 orphan reference (iteration 11)

**Bug:** memo (s18) item 4 — "В длинном диалоге AI может терять детали из
начала — напоминайте условия явно" — referenced the old quiz context-window
statement that round-2 had already replaced with a new statement 5
(determinism/training data, see s17). Quiz statements after round-2: 1) tokens,
2) knowledge cutoff, 3) hallucination, 4) privacy, 5) determinism/training
data, 6) models differ. Memo covered 2/3/5/6 — item 4 was an orphan, and quiz
statements 1 (tokens) and 4 (privacy) were both uncovered by the memo.

**Fix:** replaced item 4 with a new item mirroring quiz statement 1 (tokens,
not letters) — chosen over statement 4 (privacy) as the more practical
"gotcha fact" fitting the memo's tone (all other items are misconception-facts,
not behavioral advice). New item 4 text: "AI видит текст не буквами, а
токенами — поэтому иногда путается в побуквенных задачах вроде подсчёта букв
в слове." Updated both `slides/s18-reality-check-memo.md` (`## Visual` +
`## Speaker notes`) and the hardcoded `items` list in `build_sem01.py`
(`build_s18`, matching string). `duration_min` unchanged (3).

**Verification:**
- Rebuilt `sem-01.pptx` (19 slides) via `python3 build_sem01.py` — succeeded,
  no PYTHONPATH issues once run outside `.render-env.sh` (that script resets
  `HOME`, which drops the user site-packages dir where `python-pptx` lives;
  `soffice`/`pdftoppm` still need `.render-env.sh` sourced for the convert
  step).
- Converted to PDF, extracted page 18 only → `snapshots/iter11-s18-fix.png`.
- Visual inspection: item 4 renders cleanly, wraps to 2 lines (consistent with
  items 1/2/3/5 styling — badge, fill, stroke, spacing all unchanged), no
  overflow/clipping, no reference to context-window/dialogue-memory concept
  remains anywhere in the slide.
- Confirmed memo's 5 items now map onto a subset of the quiz's current 6
  statements with no orphans: 1→(general, not quiz-specific), 2→quiz#2,
  3→quiz#5, 4→quiz#1, 5→quiz#6. (Quiz#3 hallucination and #4 privacy remain
  uncovered by the memo by design — memo is 5 of 6, not exhaustive.)
- Title "Памятка «AI reality-check»" left unchanged — `reality-check` is used
  as a fixed phrase across `brief.md`, `facilitator-guide.md`, `rubric.md`,
  `deck.yaml`, and today's `qa-reports/2026-08-07/presentation-critic.md`
  (which explicitly classified it as a legitimate non-anglicism / brand-like
  term, "0 critical anglicism hits" in the deep-scan). Renaming only on s18
  would create fresh cross-artifact drift; out of scope for a point fix.
  Flagged in final report per task instructions (optional, not blocking).
