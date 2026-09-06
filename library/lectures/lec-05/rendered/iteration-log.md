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

---

# GATE-B fix pass — 2026-09-06

Source: `notes/lecture-5-review/pdlc/2026-09-06-gateb/presentation-critic.md`
(verdict REVISE) + `.../student-simulator.md`. 13-item fix list from
orchestrator brief. Branch unchanged throughout: `hc/pldlc-lesson5-c5cc1586`.

## P0 fixes (4/4 applied)

**1. s12 synthetic-users meme (slide-13) — Pikachu caption illegible/clipped.**
Root cause found by inspecting the raw template pixels: the stock imgflip
"Surprised Pikachu" template genuinely has a ~40%-tall BLANK WHITE band above
the face (not a stretch bug) — captions were white-fill+black-stroke text
rendered ON TOP of that white band, which is invisible, and the bottom
caption sat right at the frame edge (near-clipped). Fix in `gen_memes.py`
`s12_pikachu()`: cropped the oversized blank band down to a normal ~16%
top-caption strip, added a matching bottom white band, switched both
captions to plain BLACK text (not white+stroke) sized to actually fill each
strip. Result: `s12-pikachu.jpg` now 1893×1668 (was 1893×1892, nearly
square) — both captions fully legible, nothing touches the frame edge.

**2. s38 LLMOps (slide-44) — caption overlapped magnifier-icon row.**
Root cause: caption text_box was at y=1.70/h=0.35 (occupies 1.70-2.05) while
the icon row's icons started at y0-0.62=1.78 (occupies 1.78-2.22) — direct
overlap in the 1.78-2.05 band. Fix in `slides_band3.py` `s38()`: moved the
caption ABOVE the process-path block entirely (y=1.30) and pushed the
process path down (y0 2.40→2.55), giving the caption its own clear band with
margin on both sides.

**3. s49/slide-56 closing hero — was schematic-only (admitted gap in this
same log, Phase-6 section).** Ran 6-tier acquisition: Tier 2 (Wikimedia
Commons) search for "human-in-the-loop / mission control" imagery ->
`File:Apollo 16, Mission Control - Flickr - NASA on The Commons.jpg`,
license "No restrictions" (NASA on The Commons / Flickr Commons, public
domain). This is a *literal*, not metaphorical, match for "человек в центре
петли, суждение — дефицитный ресурс": a room of humans exercising judgment
over a live, highly-automated operation. Cropped to a 12.25×3.55in banner
(`assets/screenshots/s49-missioncontrol-crop.png`, source ratio 1.446 ->
banner ratio 3.46) = ~43.5% of the 13.333×7.5in canvas (>40% mandate).
Rebuilt `s49()` in `slides_band4.py`: photo banner hero at top, RU caption
("Центр управления NASA, Apollo 16 — люди принимают решение, пока автоматика
работает"), keystone gold_callout statement retained, 8-question checklist
compacted to a 2-row×4-col grid below (was 4×2). The old hexagon-loop hero
was DELETED from this slide (not just deprioritized) — it would have been
the 4th repetition of the same loop diagram (s03/s05/s43 already show it),
which is itself a cross-slide-redundancy violation per §5.5 checklist.
Registered in `acquire_images.py` TARGETS + `.png.url` sidecar (source URL +
license + context) per the storage convention. NO mock/stylized fallback —
this is a genuinely real, licensed photo.

**4. s01 hero (slide-1) — meme was ~16.5% of slide area (under 40% mandate).**
Root cause: split layout gave the meme only a 4.65×3.55in box among two
equal-weight panels. Rebuilt `s01()` in `slides_band1.py`: compressed the
two-fact metaphor (clock/funnel) into a narrow left column (4.35in wide,
stacked vertically) + the paradox gold_callout statement into the same
column, freeing the right side for a dominant 7.65×5.30in meme hero (=
40.5% of the 13.333×7.5in canvas, verified by direct area computation).
This-Is-Fine meme (already correct per Directive 2) is now unambiguously the
slide's hero, not a co-equal panel.

## P1 fixes (6/6 applied)

**5. AI -> ИИ cascade.** Grepped `slides/*.md` (46/56 files hit, 267 total
standalone-`AI` occurrences pre-fix across .md + 34 in the then-current
rendered .py sources) + all 4 `slides_band*.py` build scripts for standalone
`\bAI\b` tokens. Wrote a small Python cascade script
(word-boundary regex + protect-list) applied to every `slides/*.md` and
`slides_band*.py`:
  - **Protected verbatim (kept Latin):** the cover's formal lecture title
    string "AI-продукт: полный жизненный цикл — от намерения до
    эксплуатации" (matches `catalog/manifests/lectures.yaml` line 62 —
    course-convention proper title, per brief instruction); brand/product
    names `Character.AI`, `Google AI Overviews`/`AI Overviews`, source
    citations `AI Hallucination Cases Database` / `AI UI Design Tools`
    (paper titles in frontmatter `source:`, never rendered on-slide).
  - **Protected as locked mode-name-style compounds (kept Latin, judgment
    call, documented here for traceability):** `AI-first` (12+ uses
    deck-wide as this deck's own coined methodological label, "Когда здесь
    не AI-first:" — functions exactly like a keep-listed mode name, e.g.
    text-to-image) and `AI-native` (1 use, describing Spotify's own
    architecture). Flagging this explicitly in case a future pass wants to
    fully russify these too (е.g. "ИИ-first") — not done here since the
    brief's examples (s02/s06/s17/s28/s39/s46-48/closing) were all generic
    adjective/noun uses, not this specific compound.
  - **Converted to ИИ:** every other standalone `AI` — including all other
    `AI-<word>` compounds (AI-продукт->ИИ-продукт, AI-агент->ИИ-агент, etc.),
    the course subtitle "Осознанное применение AI"->"...ИИ" (not explicitly
    exempted by the brief, only the lecture title was), and the stray
    unboxed "Measure = стрелка..." floating label on s35 (slide-40), fixed
    to "Измерение = стрелка... ИИ снизил доверие" (also flagged by critic as
    a visual-inconsistency: English word with no box motif — now RU +
    consistent with the rest of the slide's language).
  - **2 baked-in-raster-image misses found AFTER the .md/.py cascade** (text
    burned into a PNG by `gen_memes.py` is invisible to a text-file grep):
    `s44_sad_pablo()` caption "от AI-пилота" -> "от ИИ-пилота"
    (slide-50 divider), `s18_pigeon()` caption "AI-генератор интерфейса" ->
    "ИИ-генератор интерфейса" (slide-21). Both regenerated + verified
    visually post-fix.
  - **Before/after (measured on git HEAD pptx vs final rebuilt pptx,
    extracted via python-pptx `shape.text_frame.text`):** standalone `\bAI\b`
    word-boundary hits 34 occurrences / 31 lines (before) -> 6 occurrences /
    6 lines (after), and all 6 remaining are exactly the protected patterns
    above (cover title ×1, AI-first ×2, Character.AI ×2, AI Overviews ×1).
    **0 unaddressed genuine anglicisms.**
  - **Deep latin-token scan** (`tools/presentation-build/deep_latin_scan.py`,
    broad regex + brand allowlist, not narrow pattern grep):
    before 206 occurrences/149 unique, after 197 occurrences/149 unique.
    Unique count unchanged because the residual 149 are ALL previously
    cross-checked-legitimate glossary-locked/brand terms documented in the
    Phase-6 section above (guardrail, eval, MVP, SLI/SLO, Stage-Gate,
    Customer Development, Gartner, Deloitte, IBM, MIT, etc.) — none are
    "AI"-family tokens; the occurrence-count drop (206->197, -9) reflects
    the `AI-` fragment count dropping from 10 to 1 (regex splits `AI-продукт`
    into token `AI-` at the Cyrillic boundary; 9 of those 10 fragments were
    genuine `AI-<ru-word>` compounds now converted, 1 remains = the
    protected cover title).

**6. "денаминатор" -> "знаменатель" typo.** Grepped all `slides/*.md` +
`rendered/*.py` for the misspelling. Found in: `slides/s47-failure-macro-
reality.md` (visible body ×1 + speaker notes ×2), `slides/s27-failure-
mcdonalds-drive-thru.md` (speaker notes ×1, both inflected forms
"денаминатора"/"денаминатором"), `rendered/slides_band4.py` (visible body
checklist item on s47 ×1). Fixed all inflections via targeted `sed`
(денаминатор/денаминатора/денаминатором -> знаменатель/знаменателя/
знаменателем). **s26 checked and found clean** (brief flagged it as a
precaution but the typo was never present in `s26-failure-google-ai-
overviews.md`). **Out of scope, NOT fixed:** `chapter-part2.md`,
`chapter-part3.md`, `chapter-part4.md` contain the same typo ~15× — these
are a separate artifact (chapter, not slides/speech) outside this GATE-B
slide-fix brief; flagged here for a future chapter-focused pass.

**7. Gold accent-line-under-heading removed from all 6 dividers.** Single
fix in `_helpers.py` `build_section_divider()`: removed the
`filled_rect(s, 0.78, 2.18, 0.70, 0.05, fill=GOLD)` line (the decorative
underline anti-pattern) between the "РАЗДЕЛ N" label and the subtitle;
subtitle y nudged from 2.55->2.62 for clean spacing without the line.
Confirmed deck has exactly 6 dividers (s07/s14/s21/s28/s36/s44 — sections
1-6; there is no separate "Раздел 0" divider, s01/s02 serve that role) —
critic's "all 7" was a miscount, all 6 real dividers share the one helper
and are fixed in a single edit. Each divider retains its gold `tag` chip
(content-count chip, e.g. "2 базы · 3 провала") as its ≥1×/slide gold
element, satisfying the palette rule without the removed anti-pattern.

**8. s43 synthesis (slide-49) hexagon — "Измерение" node clipped by gold
callout.** Computed exact geometry: old `cx,cy,r = 3.75,3.55,1.75` put node
3 ("Измерение") center at y=5.30, label extending to y=5.90 — well past the
gold_callout's top edge at y=5.10 (a ~0.8in overlap). Applied the same
fix-class already proven on s49's hexagon (per this log's Phase-6 section:
"loop moved up, cy 3.55→3.20, r 1.85→1.62"): shrunk+raised this hexagon to
`cx,cy,r = 3.65,3.00,1.45` — new node-3 label bottom lands at y=5.05,
clearing the y=5.10 callout with margin. All 6 nodes + center label fully
visible post-fix (verified visually).

**9. s03 lecture-map (slide-3) — loop read as 6 disconnected boxes.**
Replicated the connector-drawing pattern already used successfully on
s02/s49 (arcs drawn BEHIND the nodes so the ring reads as one loop), with
one addition: extended the shared `connector()` helper in `_helpers.py`
with an optional `arrow_end=True` parameter (draws a `tailEnd` triangle
arrowhead via OOXML `<a:tailEnd>`) — s02/s49 use plain lines with no
direction cue, but s03 is explicitly a `schema_cycle` (per README §4 subtype
table, "Explicit start + continue" is a hard requirement never previously
enforced on this slide). Added 6 direction-arrowed connectors behind the
existing icon-boxes, pulled in from box-edge by a fixed pad so the line
doesn't run under box interiors; the return edge (Управление(5)->
Исследование(0)) is drawn gold + thicker (2.6pt vs 2.0pt) to mark the loop
restart, matching the "Намерение" gold label already at the loop's center.

**10. s19 Character.AI (slide-22) clown meme removed; s16 gets a
replacement meme.** Removed `meme_in_box(s, "s19-clown.jpg", ...)` entirely
from `s19()` in `slides_band2.py` — replaced with a sober icon panel
(`shield-alert` icon + a plain restated-thesis text block, same footprint,
0 memes on this slide) per the explicit instruction: a case involving a
minor's death gets no meme, and NOT a replacement meme on this same slide.
Checked the Design section (s14-s20): after removing s19's meme, content-
meme count in that section was 0 (s14/s21 are dividers with their own
memes, not "Design content slides"). Added exactly 1 meme to s16 (Nielsen
heuristics = linter) — new `s16_bernie()` in `gen_memes.py`, re-purposing
the Bernie "I am once again asking" template (already downloaded, unused on
any slide — the log's Phase-6 section notes `s09-bernie.jpg` was "generated
as spare") with a NEW caption specific to s16's own claim ("эвристики —
линтер, а не тест на живом пользователе") — distinct from s09's caption, so
no joke/template duplication. First layout attempt (meme_in_box into a
5.25×1.55 landscape box) rendered the portrait-aspect (0.77) meme tiny in
the corner; fixed by building a custom narrow-image + caption-text layout
inside the box instead of relying on `meme_in_box`'s full-box aspect-fit.

## P2 fixes (3/3 attempted, 2 applied + 1 explicitly skipped)

**11. s30 experiment-traps (slide-35) — applied.** Added an explicit
grouping chip ("ДО ТЕСТА" / "ИНТЕРПРЕТАЦИЯ" / "ЭФФЕКТ") above each of the 3
cards so the sub-cluster structure reads without the lecturer, and expanded
each of the 3 glosses (SRM / peeking / Twyman) with one extra clause
explaining the mechanism in plain language (e.g. peeking gloss now explains
*why* early-checking inflates false positives, not just the ≈2× number).
Required re-flowing card height (2.55->2.85in) and pushing the gold_callout
down (4.45->4.80) to keep clearances.

**12. s40 Zillow chart (slide-46) — applied.** Root cause confirmed exactly
as flagged: both bars (356 "million-scale" and 80 "thousand-scale") were
plotted on ONE shared 0-470 axis in `gen_charts.py` `c_zillow()`, so the
$80K/home bar rendered at ~17% the length of the $304-408M bar — a
skimming reader could misread this as "$80M vs $304M" (3 orders of
magnitude off). Rewrote as two independent-scale side-by-side panels (own
xlim per panel: 0-760 / 0-170, own per-panel unit title "Общее списание, $
МЛН" / "На один дом, $ ТЫС." instead of one shared axis-footnote easy to
skim past) + an explicit "длины баров НЕ сравнивать напрямую" caption.
2 sub-iterations needed: v1 (shared-ish spacing) had panel-1's bar_label
text visually colliding with panel-2's y-tick category label; fixed via
GridSpec with explicit wide `wspace=0.85` + more xlim headroom on both
panels so labels don't hug the panel boundary.

**13. Meme swap (Change-My-Mind s33, Hide-the-Pain-Harold s39) — SKIPPED.**
This was explicitly optional/skip-if-risky in the brief. Left both memes
as-is: swapping either risks destabilizing a slide that already passes on
content/layout grounds, and the critic/student-simulator flagged these as
"weaker, not harmful" — lowest priority item in a pass that already
touched 12 other slides. No action taken.

## Re-render + verification

Rebuilt `lec-05.pptx` via `python3 build_lec05.py` (assert-56-slides check
passes) + full `bash render.sh` (all 56 pages, no partial rebuild) after
every substantive edit batch; 4 total full/partial rebuild cycles this pass
(P0 batch, s16 layout fix, s30/s40 P2 batch, final full verification pass).

Visually inspected (PNG read, not just build-success): s01, s03, s12, s16,
s17, s18(pigeon), s19, s20(divider 6, Sad-Pablo meme), s30, s35(experiment-
traps card layout), s38, s40, s43, s49, s50, s51, s56 — every fix
confirmed resolved on the actual rendered PNG, not just "the code changed".

Pre-USER-GATE mandatory grep triad (scaffold phrases / timing markers /
methodology comments) + денаминатор-check re-run on the FINAL rebuilt
pptx's extracted visible text: 0 genuine hits on all four patterns (one
"2 часа -> ~30 минут" substantive research-time-reduction claim in s10 —
same documented false-positive as the Phase-6 pass, not a section-duration
tag).

## Not fully resolved / explicitly out of scope

- **Fix #13 (meme swap):** skipped by design (optional, brief said skip if
  risky) — not a failure, a deliberate no-op.
- **денаминатор in chapter.md parts 2-4:** same typo exists ~15× in
  `chapter-part2.md`/`chapter-part3.md`/`chapter-part4.md`. Out of scope for
  this slides-only GATE-B brief; needs a separate chapter-focused fix pass.
- **`AI-first` / `AI-native` left Latin:** judgment call, documented above
  under fix #5 — treated as locked mode-name-style compounds analogous to
  keep-listed mode names, not generic adjective uses of "AI". Flagged
  explicitly in case the owner wants full russification on a future pass.
- **s43's right-hand callout box still says "Support → Product замыкает
  петлю"** (English phase names) — noticed during s43's hexagon-geometry fix
  but NOT in the original 13-item fix list and not part of the AI->ИИ
  cascade (these are different English words, not "AI"), so left untouched
  to avoid scope creep; flagged here for a future pass.
