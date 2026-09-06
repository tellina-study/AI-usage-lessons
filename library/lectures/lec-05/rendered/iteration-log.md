# Лекция 5 — render iteration log (Phase 6, Band 1: s01-s13a)

Issue #189 · Branch: hc/pldlc-lesson5-c5cc1586

## Scope this pass

Band 1 only (Раздел 0 Введение+keystone s01-s06 + Раздел 1 Discovery s07-s13a),
14 slides, per orchestrator instruction "validate machinery on Band 1 first".
Bands 2-4 (s14-s49, 36 slides) NOT wired yet — follow-up pass.

## Toolchain setup (one-time)

- Copied `library/lectures/lec-04/rendered/_helpers.py` as the base, stripped
  the lec-04-specific `URLS`/`SLIDE_REFS` clickable-reference registry (lec-05
  has no pre-built URL map deliverable) and replaced with a lighter
  `_frontmatter_source()` + `notes_with_sources()` pair that surfaces each
  slide's `source:` frontmatter as a plain "Источник: …" line in speaker
  notes only.
- Adapted `NAV` / `roadmap_bar` from lec-04's 8-section SDLC roadmap to
  lec-05's 7-card product-loop roadmap (0 Введение, 1 Discovery, 2 Design,
  3 Build/Launch, 4 Measure, 5 Support/Op., 6 Governance).
- Extended `build_section_divider()` with a `tag` chip (content count, e.g.
  "2 базы · 3 провала" — NEVER minutes, per No-Timing rule) and an optional
  per-divider `icon_name` (owner rule: no meme duplication across dividers).
- Built `gen_icons.py`: fetches Lucide SVGs live from unpkg.com CDN, recolors
  via `cairosvg` (needs `LD_LIBRARY_PATH` -> lo-sysroot's `libcairo.so.2` +
  `PYTHONPATH` -> harness's site-packages), rasterizes to 96px PNG per
  color variant into `assets/icons/`. 315 icon PNGs generated (45 names x 7
  color variants), idempotent (skips existing files).
- Confirmed pptx -> pdf -> png chain end-to-end via `render.sh` (portable
  soffice + pymupdf @150dpi), first attempt succeeded with no crashes.

## Iteration 1 — first full Band-1 render + visual sweep

Built `slides_band1.py` (14 slide functions) + `build_lec05.py` assembler.
`python3 build_lec05.py` succeeded first try (14/14 slides, no exceptions).
`render.sh` produced PDF + 14 PNG snapshots first try.

Visually inspected all 14 PNGs. Findings:

- **s02 (cover):** loop-node hero was 6 isolated dots with no connecting
  arcs — did not read as "one loop" at a glance. FIX: added `connector()`
  edges between adjacent nodes (drawn behind the node circles).
- **s04 (bridge):** inner "Цикл кода (Лекция 4)" gold box overlapped the
  outer loop-sequence caption text (bottom line got visually clipped behind
  the box edge). FIX: grew the outer box height (2.55->2.85in), moved the
  loop-sequence caption below the inner box's vertical extent, narrowed its
  width so it no longer runs under the inner box.
- **s08 (Customer Development):** step labels were bare English
  (Discovery/Validation/Creation/Building) with no Russian gloss, despite
  glossary.yaml explicitly cataloguing this as an inline-define term. FIX:
  added one-line RU gloss under each English step label (исследование /
  проверка / создание спроса / масштабирование).
- **s10 (AI discovery tools):** "Desk research" / "Reference dataset" block
  headers were bare English; glossary.yaml locks these as
  "reference dataset (эталонный набор)" with mandatory inline RU gloss.
  Also had "AI" used as a generic adjective (not the course's own
  AI-brand usage) and a bare "go/no-go" scaffold term. FIX: added inline RU
  glosses to both headers, changed "AI" -> "ИИ" in the generic-adjective
  callout, replaced "go/no-go" with "решение «продолжать/остановить»".
- **s11 (AI limits discovery):** "go/no-go" reused. FIX: same RU
  paraphrase as s10.
- **s12 (synthetic users failure):** "go/no-go" reused in the gold callout.
  FIX: same RU paraphrase.
- **s13a (IBM Watson failure):** gold callout used "high-stakes" /
  "evidence-based" / "guidelines" as bare English. FIX: translated to
  "домен с высокой ценой ошибки" / "доказательных клинических
  руководствах".

All fixes applied in a single batched edit pass to `slides_band1.py` (not
per-slide serial re-renders) then rebuilt + re-rendered once.

## Iteration 2 — anti-anglicism deep scan + scaffold-marker grep

Extracted all visible-shape text + speaker notes from the rebuilt
`lec-05.pptx` into a flat `.txt` via python-pptx, ran
`tools/presentation-build/deep_latin_scan.py` against it (mandatory per
CLAUDE.md Pre-USER-GATE Walkthrough Rule п.10 — pattern-narrow grep alone is
not accepted as verification).

- Deep scan surfaced 104 unique Latin tokens / 242 occurrences. Cross-checked
  every hit against `glossary.yaml`'s `canonical:` list + the shared brand
  allowlist: all were legitimate (glossary-locked terms: Customer
  Development, The Mom Test, PDCA/OODA/BML, reference dataset; roadmap
  section names matching NAV; brand/proper nouns: Deloitte, MD Anderson,
  IBM Watson, Nielsen Norman Group, Azure OpenAI, Perplexity, Dovetail, MIT).
  **0 unaddressed anglicisms** after the iteration-1 fixes above.
- Found a genuine violation NOT caught by the anglicism scan: 2 slides'
  speaker notes carried a leaked `[FACT-CHECK]` marker (from
  `_frontmatter_source()` copying the `source:` frontmatter line verbatim,
  including its internal-only bracket tag). FIX: `_frontmatter_source()` now
  strips `\[[A-Z-]+\]`-style markers before the line is used. Rebuilt +
  re-rendered; re-ran the extraction + grep — 0 hits for `FACT-CHECK` /
  `VFY-day-of` / `VERIFY-DAY-OF`.
- Ran the full Pre-USER-GATE Walkthrough Rule §5 mandatory grep triad
  (scaffold phrases / timing markers / methodology comments) against the
  same extracted text: 0 genuine hits on visible body; 2 substring
  false-positives both landed inside speaker-notes narrative prose (exempt
  zone) and were not actual timing-tag or scaffold-phrase violations
  ("это payoff всей лекции" in s01 notes narrative; "2 часа -> ~30 минут" —
  a substantive research-time-reduction claim, not a section-duration tag).

## Iteration 3 — final confirm render

Rebuilt (`python3 build_lec05.py`) and re-rendered (`render.sh`, all 14
pages) after the iteration-2 fix. Re-inspected s01, s02, s04, s08, s10, s11,
s13, s13a, s14(=s13a display position) PNGs — all clean, no overflow/overlap,
Ocean motif + gold >=1x/slide intact on every content slide, no timing/
methodology/scaffold markers visible, no photo-attribution labels (band 1
has no photo assets — all visuals are icon-compositions per each slide's own
`meme_or_visual` brief, which specified evergreen icon metaphors, not
screenshots, for this band).

## Outcome

- `lec-05.pptx`: 14 slides (s01-s13a), builds clean, `python-pptx` reports
  slide count 14.
- `lec-05.pdf` + `snapshots/slide-01.png` .. `slide-14.png`: all rendered via
  the portable-soffice + pymupdf chain, confirmed end-to-end working.
- 3 iteration rounds total (build+inspect -> fix -> rebuild+deep-scan -> fix
  -> rebuild+confirm), matching the "minimum 3 iterations" requirement.

## What remains (NOT done this pass)

- Bands 2-4 (`slides_band2.py`/`3`/`4`, s14-s49, 36 slides) — not written.
- Real-image acquisition for s49 (closing hero, ≥40% area) — Band 1 had no
  real-photo needs (all `meme_or_visual` briefs for s01-s13a specify
  evergreen icon metaphors), but s49 and several later case-study slides
  (Character.AI, Klarna, Zillow, Air Canada, McDonald's/IBM, Google AI
  Overviews) will need the 6-tier real-image acquisition pipeline + an
  `image-acquisition-log.md` / `hero-images-log.md` per the brief — not
  started.
- `gen_charts.py` (matplotlib) for later-band data slides (Zillow writedown,
  MIT funnel 60->20->5, Gartner 782/3400, Klarna 700->853, WCAG 29%) — not
  started (Band 1 had no chart-shaped data, only icon compositions).
- Full 50-slide `build_lec05.py` assembly + full deck-wide deep-scan +
  Pre-USER-GATE walkthrough (hero check, keystone-axis check, baseline/
  counterfactual coverage sample) — pending bands 2-4.

---

# Phase 6 — FULL DECK (s01-s49 + s13a + 6 ELI5 sNNb = 56 slides)

## Directive 1 — RUSSIAN headers/labels everywhere
- `_helpers.py` NAV: English section labels → RU (0 Введение · 1 Исследование ·
  2 Дизайн · 3 Сборка и запуск · 4 Измерение · 5 Поддержка · 6 Управление).
  roadmap_bar font auto-shrinks for longer RU labels (2-line wrap).
- s02 loop nodes, s03 loop+list+callout, s06 row labels (Строить/Измерять/
  Исследовать), s07 divider subtitle — all English phase labels removed.
- s05 PDCA/OODA/BML step sequences → RU verbs (планируй→делай→проверяй…), brand
  acronym chips kept (glossary-locked).
- ALL visible `->` ASCII arrows → `→` (s01/s03/s04/s05/s08/s10).
- Re-rendered + re-inspected s01-s08: all RU-clean.

## Directive 2 — REAL MEMES (15, imgflip templates + PIL RU captions)
Method: lec-02 gen_memes_v33 (base template downloaded to assets/meme_templates
with .url log; white text + black stroke OR black-on-white band). gen_memes.py.
- s01 This-Is-Fine → «код почти бесплатный / ценности — ноль» (hook paradox)
- s02 One-Does-Not-Simply → «нельзя просто превратить сборку в ценность» (cover)
- s07 divider Distracted-Boyfriend → команда смотрит на «мнение друзей» вместо
  «реальных пользователей» (офис лжёт)
- s12 Surprised-Pikachu → «синт-панель 7/7! реальные 3/7» (ложная валидация)
- s14 divider Drake → отвергает «прыгнуть к решению», выбирает «сначала проблема»
- s18 Is-This-A-Pigeon → «это доступный интерфейс?» (WCAG 29%)
- s19 Clown-Applying-Makeup → защита докручена ПОСЛЕ запуска (retrofit)
- s21 divider Expanding-Brain → писать руками→…→«сборка ≈ бесплатна»
- s26 Running-Away-Balloon → Google к «раскатке 100% сразу», от канареечной 1%
- s28 divider Woman-Yelling-Cat → «метрика выросла!» vs «а эффект реален?»
- s33 Change-My-Mind → «Facebook усилил ВСЕ 5 реакций ×5, не только гнев»
- s36 divider Disaster-Girl → «продукт в проде 24/7 / а дашборд зелёный»
- s39 Hide-the-Pain-Harold → «метрики зелёные, а доверие падает» (silent drift)
- s44 divider Sad-Pablo → «жду ROI от AI-пилота» (governance/payoff)
- (s09-bernie generated as spare; Section 1 already covered by s07+s12)
No template/joke duplication; no English captions; all resolve slide claim.

## Directive 3 — «Для чайников» ELI5 overviews (6 new slides)
s07b/s14b/s21b/s28b/s36b/s44b — created slides/sNNb-*.md + eli5_overview()
builder (hero icon + gold «простыми словами» chip + 3 cards Что это/Зачем/
Ментальная модель). Placed right after each divider, before classical base.
Cascade-safe suffix IDs; nothing renumbered.

## Directive 4 — FULL DECK build + render
- slides_band2/3/4.py written (s14-s49 + sNNb). build_lec05.py assembles in
  display order divider→ELI5→база→AI→ограничения→провал(ы). Assert n==56.
- gen_charts.py (matplotlib Ocean): WCAG 29% donut, review 200%/16%, pass@k/
  pass^k diverging, Zillow $304-408M, MIT funnel 60→20→5, Gartner 782/3400,
  Just-Walk-Out 700/1000 vs 50, Klarna 700→853. All with baseline/denominator.
- acquire_images.py (6-tier, Tier 2 Wikimedia Commons): 10/11 real images
  (Character.AI logo, Google/McDonald's/Facebook/Zillow/Klarna/IBM logos,
  Air Canada aircraft PHOTO, Amazon Go store PHOTO, MIT Great Dome PHOTO).
  iTutorGroup: no good Commons image → icon composition (documented, not mock).
  Each .png + .png.url sidecar (source URL + license). NO on-slide attribution.

## Anti-anglicism deep scan (mandatory)
deep_latin_scan.py on full extracted pptx: 242→206 occurrences, 177→149 unique
after Russification passes. Cross-checked ALL remaining vs glossary.yaml +
brand allowlist + established-acronyms-with-RU-gloss: 0 genuine unaddressed
(pull request glossed inline «запрос на слияние кода»). Fixed: Power-users→
активные пользователи, Governance drift→Дрейф правил, concept drift→дрейф
концепта, capital-committing→«совершающая сделки на деньги», Senior/Junior→
опытный/новичок, fallback→возврат к человеку, reward hacking→взлом награды,
Control/Treatment→Контроль/Воздействие, retrieval→поиск, operating model cell,
Продакшн→промышленная, augmentation→усиление людей, payoff tag→развязка,
Portfolio governance→Портфельное управление, Level 3→уровень 3.

## Visual loop fixes (min 3 iter on defects)
- s49 hero: bottom loop node hidden behind gold callout → loop moved up
  (cy 3.55→3.20, r 1.85→1.62); all 6 nodes now visible.
- s02 cover: loop repositioned upper-left to fit One-Does-Not-Simply meme.
- s04 inner box: empty area fixed (git-branch icon + repositioned sequence).
- Klarna chart y-axis FTE→чел.-эквивалент.
- Divider meme framing: build_section_divider gains meme_name (ghost digit +
  Ocean-boxed meme as right hero).

## Outcome
lec-05.pptx (56 slides) + lec-05.pdf + snapshots/slide-01..56.png all built via
portable-soffice + pymupdf chain. All 6 divider memes distinct + on-point; s01+
s49 hero present; every measurable claim has inline baseline/denominator.
