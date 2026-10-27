VERDICT: REVISE

# Presentation Critic Report — Лекция 8 «AI в креативных индустриях и медиа» — 2026-05-20

## Сводка
- Всего слайдов: 39
- P0 issues (блокеры): 0
- P1 issues (важные): 14
- P2 issues (мелочи): 6

**Counter-check (mandatory):** 14 P1 ≥ 5 → verdict = **REVISE** (не APPROVE-WITH-POLISH).

## Methodology snapshot

Структура deck'а — sound. Lec-07-pattern compliance — высокий. Open + keystone слайды (s01–s05a) методически сильные. 12 case-слайдов раздела 3 имеют consistent layout (assertion + 2-column body + Урок block). Cover, lecture-map, keystone, dedicated Q&A — все present. Section dividers (5×) с роадмар-баром только на дивайдерах + cover — правильный pattern.

Однако **главный блокер** — Phase 6 visual loop НЕ выполнен: 12+ слайдов содержат placeholder-плейсхолдеры `[ FRAME ]`, `[ news screenshot ]`, `[ frame ]`, `[ playable 3D world ]` вместо реальных скриншотов / изображений. Backup-каталог `assets/backup/` содержит только README.md, ни одного PNG. Media coverage ≥80% mandate (≥33/39) недостигнут: фактически ~20/39 ≈ 51% слайдов имеют функциональные media-elements (charts, diagrams, schema-cards, лого), 12+ — placeholder gaps. Все эти placeholder'ы visible в PPTX visible layer.

Дополнительно **3 forbidden scaffold-leaks** в visible layer PPTX (cross-verified Python+pptx grep):
- PPTX-10 (s09 voice cloning): «Voice 4 · ScarJo-like · soundalike (s9 caveat)» — slide-ref leak
- PPTX-20 (s20 4-categories): «Конкретные landmark-cases каждой категории — s21-s27.» — slide-ID range leak
- PPTX-21 (s21 NYT): timeline chip «SJ deadline · через 2 нед после лекции» — temporal scaffold leak

Орчестратор сообщил «TOTAL=0» по 10 patterns. Это **false self-report** (как Лекция 4, designer-extras silent-failure). Pattern «s21-s27» / «(s9 caveat)» / forward-reference «через 2 нед после лекции» — должны были быть detected в orchestrator-independent grep.

**Также 2 typo в PPTX visible**:
- PPTX-16 (s15 speed): «иeрация» (должно быть «итерация») + «Inженерный» (Latin I+n вместо Cyrillic «И»)
- PPTX-22 (s22 Getty): timeline chip «Suprior» (видимо «Superior» — Superior Court?)

## 10-check rollup

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | Visual design quality (palette / motif / typography) | **PASS-WITH-CAVEATS** | Ocean palette adherence high, gold #F0AB00 ≥1×/slide на всех content-слайдах. Motif consistent. Typography hierarchy clean. Минусы: overflow Урок blocks в s08/s16/s17/s35; layered text artifacts на s33 (cards перекрывают subtle case-refs ниже) |
| 2 | Media coverage ≥80% | **FAIL** | ~51% (≈20/39) против target 85%. 12 placeholder slides: s07, s10, s10a, s21–s25 (5 шт), s30 (если sentiment chart считать functional — 11 шт). `assets/backup/` пустой, Phase 6 visual loop не выполнен |
| 3 | Lec-N-1 pattern compliance | **PASS** | lecture-map (s04), keystone (s05), 5 section dividers (s06/s13/s19/s32/s36), dedicated Q&A (s38), closing (s39). Roadmap-bar только на dividers + cover. Top progress bar антипаттерн Лекции 2 избегнут |
| 4 | Speaker notes quality | **PASS** | Sample 5 slides (s07, s35, s22, s24, s25, s39): 200–350 слов connected text, derived from chapter. Никаких «Лектору» / «Вы здесь» / тайминга. Один borderline forward-reference в s07 («мы разберём подробно в третьем разделе») — acceptable в speech-derived notes |
| 5 | Forbidden content grep | **FAIL** | 3 confirmed leaks в PPTX visible layer (s09 «(s9 caveat)», s20 «s21-s27», s21 «через 2 нед после лекции»). Orchestrator self-report TOTAL=0 — silent failure. Stale PNG-snapshots показывают также [VFY-day-of] на s14/s35, но PPTX уже исправлен → snapshot regenerate needed |
| 6 | Slide-type adherence | **PASS** | Все 39 слайдов соответствуют declared type в deck.yaml. case_with_metric ≠ taxonomy_2x2 и т.д. соблюдены |
| 7 | Methodology depth (assertion + evidence) | **PASS** | Sample s07, s17, s20, s24, s25, s26, s33: clear assertion 24-28pt + evidence + (для §3) explicit «Урок для инженера» Ocean rounded box. Schema-слайды s05a/s20/s33 — typography hierarchy clear, readable |
| 8 | Keystone-axis coherence | **PASS** | s05 keystone заголовок «AI добавил → изменил → сломал» — про ось, не recap. 3 main sections явно anchored на свой axis-time (s06=ДОБАВИЛ, s13=ИЗМЕНИЛ, s19=СЛОМАЛ). Anti-pattern Лекции 4 (защитный recap) избегнут |
| 9 | «Урок для инженера» blocks на case-slides §3 | **PARTIAL** | Все 12 case-слайдов §3 имеют explicit «УРОК ДЛЯ ИНЖЕНЕРА» с Ocean rounded box + gold label. Format consistent. Минус: на s08, s16, s17, s35 content cut off / clipped at bottom of slide — rendering issue (text exists в PPTX но visual overflow) |
| 10 | Section dividers — recognizable + gold-bar emphasis | **PASS** | 5 dividers (s06/s13/s19/s32/s36) + s04 lecture-map: большая цифра, title, 1-фраза-фрейм, 6-card progress bar с gold на current section. Все instantly recognizable как divider class |

## Top 5 strongest слайды

| Slide | Why strong |
|---|---|
| **s05 keystone** | Clean axis presentation. Заголовок «AI добавил → изменил → сломал» — direct, про ось. 3 timing-blocks с inline examples (Sora 2, RIAA, Arup) — concrete anchors. Ось — не три параллельные категории, а три времени. Subtitle подтверждает это явно. Anti-pattern Лекции 4 (recap) полностью избегнут |
| **s05a three-families** | Mental model 3 архитектурных семейств (diffusion / latent video transformer / neural audio) с inline tools 2026 + inженерное следствие per family. Caption «Mental model: каждое семейство → свои inherent limits, не зависящие от качества реализации» — точная methodology framing |
| **s14 cost-collapse table** | Numeric evidence-driven таблица 4×3 (asset class × до/после/×) + gold callout «MIDDLE-TIER ≠ FREE» с $400M Adobe Firefly. Mental model «bottom vs middle vs top» visible. Источник чётко footnoted. Cost-collapse ≠ free anti-hype работает |
| **s26 Arup deepfake** | 5-step attack diagram (Email → Приглашение video → Звонок с deepfakes → 15 transactions → $25.6M gone) — visualizes mechanism конкретно. CNN headline real text. Урок block чёткий: «Видеозвонок ≠ identity proof в 2024+. Out-of-band verification обязателен». Самый strong educational case в Разделе 3 |
| **s37 5-question checklist** | Main deliverable лекции. 5 numbered questions в left column + decision tree (А: не использовать / B: митигировать / C: accept risk явно) в right. Actionable, scannable, явно designed для unloading из лекции |

## Top 5 weakest слайды

| Slide | Issue | Severity |
|---|---|---|
| **s07 text-to-video** | `[ FRAME ]` placeholder вместо Sora 2 release reel screenshot. Иронично — самый важный «AI добавил» слайд (3 модели определяющие индустрию) визуально DEAD. QR-код тоже только rectangle, не actual QR | **P1** |
| **s10a Russian context** | 2× `[ frame ]` placeholders вместо Kandinsky 5.0 Video frame + Kling 3.0 frame. Side-by-side comparison concept хорош, но без реальных кадров — методически dead. «Видимый quality gap» нечем показать | **P1** |
| **s21-s25 case-cluster** | 5 consecutive case-слайдов (NYT, Getty, Andersen, RIAA, Thomson Reuters) с **identical `[ news screenshot ]` placeholder** в левой колонке. Cumulative effect: студент видит 5 одинаковых grey rectangles → бренд-credibility слайдов рушится. Эти кейсы — landmark, должны быть с реальными news headlines / court docket screenshots | **P1** |
| **s09 voice cloning** | Visible scaffold «(s9 caveat)» в Voice 4 row — slide-ref leak в visible layer. Plus, ElevenLabs voice library mockup — 4 generic rows без real screenshot | **P1** |
| **s35 YouTube thumbnails** | Bottom Урок block overflows / cut off at slide bottom edge. Также left-column #1 stat block 47.3% — sample-render показывает разную трактовку (stale s-35 vs fresh s35-35). Render needs re-snapshot. PPTX content корректен | **P1** |

## P1 issues (детальный список — 14 штук)

### P1-1: Phase 6 visual loop НЕ выполнен — массовый media-coverage gap
**Slides:** s07, s10, s10a, s21, s22, s23, s24, s25 (8 confirmed placeholder slides)
**Issue:** PPTX visible layer содержит `[ FRAME ]`, `[ frame ]`, `[ playable 3D world ]`, `[ news screenshot ]` placeholders. `assets/backup/` каталог содержит только README.md, ни одного PNG. Phase 6 visual loop в pipeline `tools/presentation-build/README.md` явно требует генерации backup PNG'ов перед USER GATE B.
**Recommendation:** До GATE B либо (a) сгенерировать реальные screenshot'ы / sample frames для 8+ слайдов (Sora 2 reel frame, Genie 3 demo frame, Kandinsky vs Kling side-by-side, Bloomberg Law / Bird & Bird / Court docket / RIAA / Reed Smith news headlines), либо (b) явно переопределить эти placeholder'ы в content-driven 100%-text layout (без grey rectangle) — иначе студент видит «cheap deck» message.
**Visual evidence:** см. snapshot s-07 (FRAME box top-right), s-11 (s10a Russian context — 2 frame boxes), s-21 через s-25 (5 consecutive news screenshot placeholders в визуально identical layout — slide-fatigue для аудитории).

### P1-2: Forbidden scaffold leak в visible layer (s09 voice cloning)
**Slide:** s09 (PPTX-10)
**Issue:** Voice 4 row содержит text «ScarJo-like · soundalike **(s9 caveat)**». «s9» — slide-self-ID reference, scaffold-фраза, не должна быть видна студенту.
**Recommendation:** Edit text frame → remove «(s9 caveat)» полностью или заменить на нейтральное «(soundalike risk)». Cross-ref в speech.md если нужно объяснить deeply.
**Visual evidence:** s-09 PNG bottom-left ElevenLabs voice library mockup, 4-я строка.

### P1-3: Forbidden slide-ID range leak (s20 4-categories)
**Slide:** s20 (PPTX-20)
**Issue:** Footer text «Конкретные landmark-cases каждой категории — s21-s27.» — direct slide-ID range, course-scaffold, не должен быть visible.
**Recommendation:** Replace «s21-s27» на «далее в разделе» или удалить footer вообще.
**Visual evidence:** s-20 PNG, текст нижнего края.

### P1-4: Forward-reference scaffold leak (s21 NYT timeline)
**Slide:** s21 (PPTX-21)
**Issue:** Timeline chip «2 апр 2026: SJ deadline · **через 2 нед после лекции**» — meta-comment о когда event происходит относительно lecture date. Видно студенту, ломает 4th wall.
**Recommendation:** Remove «через 2 нед после лекции» — оставить только «SJ deadline».
**Visual evidence:** s-21 PNG, нижний timeline chip.

### P1-5: Typo в visible layer (s15 speed-collapse)
**Slide:** s15 (PPTX-16)
**Issue:** (a) «иeрация плотнее» в правой колонке Concept exploration row — должно быть «итерация» (пропущен символ «т»); (b) «**In**женерный урок» в Урок block — Latin «I» + «n» вместо Cyrillic «Ин». Fonts mixed.
**Recommendation:** Edit shape text — заменить «иeрация» → «итерация», «Inженерный» → «Инженерный».
**Visual evidence:** s-15 PNG.

### P1-6: Typo в visible layer (s22 Getty Stability)
**Slide:** s22 (PPTX-22)
**Issue:** Timeline chip text «Suprior» — typo, должно быть «Superior» (видимо ссылка на Superior Court — но контекст неясен из обрезанного текста).
**Recommendation:** Fix typo OR remove chip если context unclear.
**Visual evidence:** s-22 PNG, нижний chip timeline.

### P1-7: Урок block visual overflow / clipping (s08 character consistency)
**Slide:** s08 (PPTX-9)
**Issue:** Bottom «УРОК ДЛЯ ИНЖЕНЕРА» Ocean rounded box content («Anti-hype: multi-scene drift…») partially cut off at slide bottom edge. Box extends below safe area.
**Recommendation:** (a) Reduce body content height OR (b) shrink character consistency 2×2 grid выше, чтобы Урок block fit полностью. PPTX text present, render issue only.
**Visual evidence:** s-08 PNG нижний край, gold-tinted box обрезан.

### P1-8: Урок block visual overflow (s16 new professions)
**Slide:** s16 (PPTX-17)
**Issue:** Similar — Урок block content cut off at bottom edge. Текст «Между AI-tool и client deliverable. Растёт быстро, но меньше displaced класса.» — только верхняя половина видна.
**Recommendation:** Same as P1-7 — adjust layout vertically.
**Visual evidence:** s-16 PNG.

### P1-9: Урок block visual overflow (s17 displacement)
**Slide:** s17 (PPTX-18)
**Issue:** Same overflow pattern.
**Recommendation:** Same.

### P1-10: Урок block visual overflow (s35 YouTube)
**Slide:** s35 (PPTX-35)
**Issue:** Same overflow на s-35.png. Альтернативная re-render s35-35.png показывает полный Урок block — значит, layout уже исправлен в PPTX, но snapshot stale.
**Recommendation:** Re-render full snapshot set после Phase 6/7 fixes — текущий s-NN set частично stale (older than PPTX timestamp).

### P1-11: Stale snapshots vs PPTX (cross-cutting)
**Slides:** s-14, s-15, s-35 (минимум)
**Issue:** Snapshot timestamps `1779280980-1779280983` старше PPTX timestamp `1779281382`. PPTX clean (verified Python pptx grep) от `[VFY-day-of]` в s14/s15/s35, но stale PNG showing leaks. Это создаёт ложное впечатление quality issues + усложняет accurate critic-review.
**Recommendation:** Regenerate full snapshots set из current PPTX перед USER GATE B.

### P1-12: s33 cards overlap underlying case-refs (visual artifact)
**Slide:** s33 (PPTX-33) — 4 критерия
**Issue:** В render-PNG видно faded fragments текста под chips («Andersen v Stability · RIAA v Suno» etc.) — case-refs текстовые элементы перекрыты card-фоном, но проступают subtle. Render-bug, не PPTX issue.
**Recommendation:** Verify z-ordering shapes в PPTX. Либо elevate case-refs over cards (с другим стилем), либо move below cards без overlap.

### P1-13: «News headline» as substitute for screenshot (s27 Korea handling exception)
**Slide:** s27 (PPTX-27)
**Issue:** s27 (Korea schoolgirl deepfake) — единственный из case-cluster, который имеет правильное text-only handling с explicit explanation «Только text headline — без визуалов (sensitive case)». **Это образец как должны выглядеть text-only fallbacks** для всех placeholder'ов. Однако этот pattern не применен консистентно к s21-s25.
**Recommendation:** Применить s27-style text-only handling к остальным 5 case-слайдам если real screenshots недоступны: убрать grey `[ news screenshot ]` placeholder, заменить на large quote-block с headline текстом + source caption.

### P1-14: s37 checklist rendering — aspect-ratio compression
**Slide:** s37 (PPTX-37)
**Issue:** s-37.png показывает slide с unusually squashed aspect-ratio (height проявляется обрезанным по сравнению с другими slides). PPTX content OK, но visual presentation странная. Может быть rendering glitch специфический для s37 или layout-overflow.
**Recommendation:** Verify slide-level layout dimensions; possibly text shapes positioned outside safe area.

## P2 issues (cosmetic, 6 штук)

### P2-1: s30 sentiment bar chart proportions
**Slide:** s30 (PPTX-30) — Toys R Us sentiment
**Issue:** «+12.2 %» bar wraps на 2 lines внутри узкого chip (looks awkward). Bar heights не quite-proportional к values («+3.4 %» bar короче чем «13.5 %» bar, что странно).
**Recommendation:** Polish bar widths + chip layout.

### P2-2: s07 QR-код box — empty rectangle
**Slide:** s07 (PPTX-8)
**Issue:** QR-код visualized как простой white rectangle с label «QR» — не реальный QR code.
**Recommendation:** Generate реальный QR через QuickChart QR-API или python-qrcode для openai.com/index/sora-2/.

### P2-3: s10 Genie 3 — visual proportion
**Slide:** s10 (PPTX-11)
**Issue:** Left big-frame box (с `[ playable 3D world ]` placeholder + «medieval castle…») занимает ~50% слайда. Если оставить placeholder — потеря 50% canvas-real-estate бессмысленна. С реальным frame — пропорция OK.
**Recommendation:** См. P1-1; либо real frame, либо ужать box до маленького thumbnail.

### P2-4: s05 keystone subtitle font weight
**Slide:** s05 (PPTX-5)
**Issue:** Subtitle «Три времени одного процесса — каждое поколение creative-инструментов проходит их за месяцы» — italic в teal цвете, читаемо, но мог быть bolder для усиления.
**Recommendation:** Increase font-weight для subtitle (semibold), оставить italic.

### P2-5: Section dividers — numbers in light gray
**Slides:** s06, s13, s19, s32, s36
**Issue:** Большие number-decorative (1, 2, 3, 4, 5) очень faded — almost invisible. Сравнительно cover s02 имеет «08» более read.
**Recommendation:** Increase contrast на section number — current 10-15% opacity, можно поднять до 25-30% surface-tint.

### P2-6: s03 central question — split chip alignment
**Slide:** s03 (PPTX-3)
**Issue:** Bottom 2 chips «Разделы 1-3: что AI сделал» / «Разделы 4-5: где сказать "нет"» — chip-стили слегка different (gold-tint vs teal-tint), что подчёркивает split, OK. Минор — alignment chip-text within chips не quite centered.
**Recommendation:** Center-align text within chips.

## Cross-deck issues

### Cross-1: Snapshot regeneration mandate
Все s-NN.png в `rendered/snapshots/` старше lec-08.pptx — minimum 3 snapshots stale (s-14, s-15, s-35). Re-render full set перед USER GATE B обязательно. Иначе critic + user видят разную state.

### Cross-2: Backup folder population
`assets/backup/README.md` декларирует 23 PNG-файлов для tier-4 fallback (Phase 6 visual loop deliverable). Фактически 0 PNG присутствуют. До USER GATE B сгенерировать минимум 8 high-priority slides (s07 Sora reel, s10 Genie demo, s10a side-by-side, s21-s25 news headlines, s35 thumb examples).

### Cross-3: Self-report verification gap (orchestrator-level)
Orchestrator self-reported «TOTAL=0 на 10 patterns». Independent Python pptx grep нашёл **3 patterns leaked в visible layer**: (s9 caveat), s21-s27, через 2 нед после лекции. Это **silent failure** как Лекция 4. CLAUDE.md Pre-USER-GATE Walkthrough Rule пункт 5 (designer-extras grep orchestrator-INDEPENDENT) был не выполнен или выполнен с неполным pattern-set. Рекомендуется добавить patterns: `\(s[0-9]+`, `s[0-9]+-s[0-9]+`, `через [0-9N]+ (нед|дн|мес) после лекции` к standard grep.

### Cross-4: Media coverage количественная оценка
Counted functional media по 39 слайдам:
- **Functional charts / diagrams / схемы**: s01 (live demo box), s02 (decorative 08), s04 (6-card roadmap), s05 (3-stage diagram), s05a (3-card schema), s06/s13/s19/s32/s36 (5 section dividers), s14 (table+callout), s15 (timer mockup), s16 (Upwork screenshot mockup + 4 role-cards), s17 (3 stat-boxes + timeline), s20 (2×2 quadrant), s26 (5-step diagram), s27 (data chips), s28 (search-query cards), s29 (stat card), s30 (bar chart), s31 (3-stat block), s33 (4-card matrix), s34 (3-column compare), s35 (3-stat), s37 (checklist+decision tree), s38 (typography Q&A?), s39 (QR + 09 decorative)
- **Functional**: ~25 / 39 = 64% (above MVP но below ≥80% mandate)
- **Placeholder/dead**: 8 slides (s07, s09 ElevenLabs mockup, s10 Genie frame, s10a 2 frames, s21-s25 5 news screenshots) = ~21% слайдов с **explicit grey rectangle placeholder**

**Strict media ≥80% mandate FAIL** — gap ~16-20 pp до target.

## Recommendations — must-fix priority

1. **Phase 6 visual loop completion (P1-1)** — populate `assets/backup/` с 8+ real PNGs OR convert 5 news-screenshot slides к s27-style text-only-headline pattern (P1-13).
2. **3 forbidden-leak fixes (P1-2, P1-3, P1-4)** — edit PPTX text: «(s9 caveat)» → remove; «s21-s27» → «далее в разделе»; «через 2 нед после лекции» → remove chip suffix.
3. **2 typo fixes (P1-5, P1-6)** — «иeрация» → «итерация», «Inженерный» → «Инженерный», «Suprior» → «Superior» / verify intent.
4. **4 Урок block overflow fixes (P1-7..P1-10)** — adjust layout shapes на s08/s16/s17/s35 to keep Урок box inside slide bounds.
5. **Snapshot regeneration (P1-11, Cross-1)** — fresh snapshot set из current PPTX перед GATE.
6. **s33 z-order cleanup (P1-12)** — eliminate underlying case-refs faded-leak.
7. **s37 aspect-ratio (P1-14)** — verify slide layout-bounds на s37.
8. **Re-run orchestrator-independent grep (Cross-3)** — with extended pattern-set covering slide-ID-ranges + temporal scaffolds.

## Verdict justification

14 P1 issues > threshold 3 для APPROVE-WITH-POLISH → **REVISE**.

Critical structural failures:
- **Media coverage ≥80% mandate FAIL** (~64% measured, 51% strict если placeholder = gap) — это owner-mandate, не «polish».
- **Phase 6 visual loop incomplete** — backup PNGs не сгенерированы, 8 slides имеют dead placeholder content.
- **3 forbidden-leak failures + 2 typo failures** в visible PPTX layer — silent self-report failure, точно как Лекция 4.
- **4 layout overflow failures** на Урок blocks — Урок — главный pedagogical device раздела 3, нельзя clipped.

Это НЕ «cosmetic polish» — это структурные gaps между declared deliverable и actual state.

**После fixes (P1-1 через P1-14 + Cross-1/Cross-2):** likely APPROVE-CLEAN либо APPROVE-WITH-POLISH, потому что methodology base (keystone, lecture-map, dividers, slide-types, speaker notes, assertions) — solid.

---

**Critic agent:** presentation-critic
**Date:** 2026-05-20
**Phase:** 7.5 (post-Phase 7 deck designer, pre-USER-GATE B)
**Reviewed against:** Lec-07 pattern + tools/presentation-build/README.md + chapter v2 + plan v2
