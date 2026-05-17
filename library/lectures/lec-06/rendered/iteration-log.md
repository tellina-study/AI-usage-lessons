# Лекция 6 — Visual Loop Iteration Log (Phase 6, Issue #101)

**Deck:** «AI в инженерном проектировании и CAD/CAM» · 32 слайда · 75.0 мин
**Builder:** `build_lec06.py` (helper layer adapted from proven lec-07 Phase 6 pipeline)
**Palette:** Ocean Gradient LOCKED v3 (#21295C / #065A82 / #1C7293 + Teal #028090
+ Gold #F0AB00 ≥1×/слайд). Motif: Ocean rounded box (radius 12, surface
#F4F7FA, stroke #1C7293 1.5pt).
**Canvas:** 13.333" × 7.5" (16:9).

## Task A — структурная правка (выполнено до рендера)

- Добавлен 6-й section-divider **s29 «Часть 6. Синтез»** (паттерн
  s04/s09/s15/s20/s25; 7-card progress bar, card 6 gold-active).
- Ренумерация: worked-decision s29→**s30**, правило+матрица s30→**s31**,
  Q&A s31→**s32**. Итого **32 слайда**.
- deck.yaml обновлён: slide list, header-комментарий (31→32, 6 divider'ов,
  Q&A s32), version/status. duration_min перераспределён по Части 6
  (divider 0.3 + s30 2.4 + s31 2.4 + s32 0.9); **сумма = 75.0** (строго).
- Frontmatter id/duration в 3 переименованных файлах + стале-ссылка
  s06 learning_goal (s30→s31, frontmatter-exempt, поправлено для точности).
- Проверено: 6 divider'ов (s04/s09/s15/s20/s25/s29), lecture-map s03,
  выделенный Q&A s32, file/id consistency, ids contiguous s01–s32.

## Visual loop — per-slide / batched (min 3, выполнено 4 итерации)

Слайды строятся через переиспользуемые блоки (`two_col_compare`,
`_matrix_da_net`, `pipeline_row`, `build_section_divider`), поэтому фиксы
батчевые — одна правка блока чинит все слайды этого типа.

### Iter 1 — baseline (110 dpi)
- (a) Inspected: все 32 PNG; фокус — cover/hook/lecture-map/divider/
  comparison/axis/matrix/timeline/pipeline/P1(s26,s31)/новый divider/Q&A.
- (b) Найдено:
  - **P0 `two_col_compare` overflow** — динамическая формула `ly` уводила
    текст НИЖЕ ocean box, наезд на gold-callout. Затронуты s05/s10/s16/
    s21/s28 (5 слайдов).
  - **s11 timeline** — labels сверху, baseline внизу, мёртвая полоса в
    середине, «плавающее» ощущение (Schema-Readability fail).
  - s02 hook: рваный baseline reveal-текста, scribble в lattice
    иллюстрации, дыра до gold-callout.
  - pipeline body center-anchored с орфанами; s23 3-я факт-строка
    выдавлена; s32 неравномерные слоты промптов.
- (c) Checklist: matrix(s07/s08) PASS; axis(s06) PASS; comparison FAIL
  (overflow); timeline FAIL (floating).

### Iter 2 — P0 + schema fixes (110 dpi)
- (a) Inspected: s05/s10/s16/s21/s28 (compare), s11 (timeline), s02, s14,
  s22, s23, s32 + P1 hi-res s26/s31 (150 dpi).
- (b) Changed:
  - `two_col_compare` переписан: фикс. равные слоты от box_h, anchor
    MIDDLE → текст НИКОГДА не выходит за box. **5 слайдов исправлены.**
  - `build_s11` timeline переписан: baseline через центр box, label
    вплотную сверху (anchor BOTTOM), sub вплотную снизу (anchor TOP),
    вывод → gold-callout внизу. Мёртвая полоса убрана.
  - `pipeline_row`: body left-tighten.
  - s02: reveal-текст перекомпонован, gold-callout к низу box (2 строки).
  - s23: Mars-блок выше, 3 факта компактнее; Gimli/Hyatt strip тоньше.
  - s32: фикс. слоты промптов (по 2 строки).
- (c) Checklist: comparison PASS (no overflow); timeline PASS (baseline
  centred, single-line, SIMP 1989 pivot gold ≥2×, arrows L→R).
  P1 s26 PASS (single-line, icon/row, fill≥75%, ≥14pt @150dpi — НЕ
  делим на s26b). P1 s31 PASS (чек-лист доминирует, матрица subdued).

### Iter 3 — polish (110 dpi) + новая иллюстрация
- (a) Inspected: s02/s14/s22/s28 (polished) + deck-wide sweep
  s08/s12/s13/s17/s19/s21/s24/s27/s30 + divider'ы.
- (b) Changed:
  - Новая bracket.svg (чистый треугольный lattice, без scribble).
  - `pipeline_row`: head-band выше (0.80") — 2-строчные заголовки не
    зажаты; body size 12.5, anchor вынесён ниже band.
  - s28: compare box выше (3.35), ТРИЗ-strip и gold-формула компактнее.
  - s02: reveal line_spacing шире, лучше заполняет box.
- (c) Найдено НА iter 3 (Anthropic principle — ищем проблему):
  **s30 worked-decision — Q3-строка левой ветки наезжает на gold
  conclusion box** (qy-инкремент мал для 3 вопросов). Реальный
  overlap-bug на ключевом LO7-слайде → требует iter 4.
- Checklist: s08/s12/s13/s17/s24 matrix PASS; s10/s16 compare PASS;
  s19/s22 pipeline PASS; s30 FAIL (overlap).

### Iter 4 — s30 overlap fix (110 + 150 dpi)
- (a) Inspected: s30 hi-res (150 dpi) + s10/s19 + перепроверка.
- (b) Changed: `build_s30` — вопросы в фикс. слотах в области НАД
  conclusion box; ch/concl_h пересчитаны под вертикальный бюджет
  (cy 2.50 + ch 3.18, gold-callout 5.85 — зазор 0.17", без наезда).
- (c) Checklist: **s30 PASS** — Q3 не наезжает; задача → 2 ветки → по 3
  вопроса-якоря → разные обоснованные выводы; LO7 worked-decision
  читается. s10/s19 PASS.

### Path-fix re-render (критично)
- Обнаружено: `ROOT` указывал на main-repo путь, где `slides/` нет
  (worktree-isolation: контент в `/tmp/lec-06-wt`). `load_notes()`
  возвращал пусто → speaker notes были пустыми в PPTX.
- Fix: `ROOT` → worktree; build script + assets перенесены в
  `/tmp/lec-06-wt/.../rendered/`; пере-рендер.
- Verify: speaker notes всех 32 слайдов = **151–268 слов** (контракт
  [150,300] — PASS); anti-leak grep visible+notes = **0 hits**.

## Schema-Readability Acceptance Gate (§5.5) — schema-слайды

| Slide | Subtype | Verdict |
|---|---|---|
| s06 | schema_axis | PASS — ось со стрелкой, gold direction-marker, 6 ярлыков single-line + микроопределение, caption «полная матрица в финале» |
| s11 | schema_timeline | PASS — em-dash-style single-line узлы, SIMP 1989 pivot gold ≥2×, baseline через центр, arrows L→R, KKT-сноска subdued footer |
| s14 | schema_pipeline | PASS — RIGHT_ARROW, 3 stage, gold на «непригодная форма», stage labels ≤3 слов, owner-смысл явный |
| s19 | schema_pipeline | PASS — 4 stage RIGHT_ARROW, gold «аттестованный решатель» финал, gold-критерий, Россия 1 строкой (cascade) |
| s22 | schema_pipeline | PASS — 4 stage, gold «верификация», unified RU sub-labels, граница форма/содержание |
| s26 | schema_matrix | PASS — 8 строк × 3 кол, fill 100%, icon/row, single-line ≥14pt @150dpi, единый RU, gold summary. **На 1 слайде, без split s26b.** |
| s29 | section_divider | PASS — Lec-7 divider pattern, 7-card bar, card 6 gold-active |
| s31 | schema_matrix | PASS — split-layout: чек-лист ДОМИНИРУЕТ (gold-tint, large), матрица 6×4 subdued (muted, small), fill≥75%, gold «кто отвечает=инженер» |

## 5-Second Test (final accept gate) — sample

- s05: «решает уравнение vs угадывает по примерам» = assertion. PASS.
- s11: «топ-оптимизация = градиентный спуск, родословная 1904→1989,
  не нейросеть» = assertion. PASS.
- s23: главный message «Mars $327M — единицы на стыке = LLM-стык» —
  Mars доминирует, gold на $327 млн. PASS.
- s26: «чем выше цена ошибки — тем меньше места ИИ; для каждого критерия
  есть правильный инструмент» = assertion. PASS.
- s31: «правило 5 вопросов (доминирует) + полная матрица (подтверждение)»
  = assertion. PASS.
- s30: «один вопрос-якорь развёл ответы» — gold-callout формулирует. PASS.

## Cascade-ограничения (Task C) — held in visuals

- s12: GM/Airbus — ровно ≤3 числа/карточка. PASS.
- s17: Ansys/Altair/NVIDIA — 3 названия, числа диапазонами «до ~10²–10³×».
  PASS.
- s19: Россия 1 строкой (Логос/CML-Bench), ≤3 числа/≤4 названия. PASS.
- s21: 2 колонки, ≤4 названия (Autodesk/Siemens/Zoo.dev/Bernini). PASS.
- s27: 4 карточки, ≤3 числа/≤4 названия, номера ФЗ subdued. PASS.
- s23: Mars ведущий ~74%, Gimli/Hyatt по 1 строке strip. PASS.
- s24: range chart БЕЗ катастроф (они на s23), ORCA ~45–63% диапазон. PASS.
- s13: APM FEM БЕЗ точного числа («существенную долю»); footer vendor-claim.
  PASS.
- 0 visible: LO/§X.X/→sNN/[FACT-CHECK]/[VERIFY-DAY-OF]/Лектору/Вы здесь/
  тайминг/second-person — grep подтверждён 0 hits в visible+notes.

## Supportive visual assets

- 1 custom SVG-иллюстрация (bracket.png — topology-optimized organic
  bracket, Ocean palette, чистый lattice).
- 56 уникальных Lucide-иконок × 4 цвет-варианта (blue/teal/gold/white),
  recolored в Ocean palette, semantic-role на каждом слайде.
- 1 stress-curve schematic (s18 — истинный пик vs PINN-сглаженная кривая,
  connector polyline, gold-маркер занижения).
- ≥10 supportive visual elements (baseline ≥5–10 satisfied).

## Итог (Phase 6 v1)

32 слайда, сумма duration_min = 75.0, 6 divider'ов, lecture-map s03,
выделенный Q&A s32. 4 visual-loop итерации (min 3 — выполнено; iter 4 по
реальному s30-overlap). Все schema-слайды проходят §5.5. 3 P1 закрыты.
Cascade удержан. Speaker notes 151–268 слов. 0 anti-leak hits.

---

# Phase 8 — Polish Round (7 P1 + P2 из qa-reports/2026-05-17-v2/SYNTHESIS)

Единый presentation-designer проход по Phase-7 синтезу. Все правки в
`build_lec06.py` (canonical render path) + deck.yaml. Slide .md не тронуты
(контент финален). БЕЗ ренумерации — 32 слайда фиксированы. split s26 = НЕТ.

## Итерации (min 3 — выполнено: 3 visual-loop iter)

- **Iter 1** — applied 7 P1 + P2; built+rendered all 32. Inspected priority
  (s02/s06/s07/s08/s18/s26/s31) + P1-1 montage + projector 50% (s26/s31).
  Found: s18 PINN label overlaps teal shoulder + marker on spike apex;
  s14 pipeline↔bottom gap loose. s26 NO-SPLIT confirmed (projector PASS).
- **Iter 2** — s18: gold-arrow clearance +0.6", labels → upper clear zone,
  marker below apex; s14: bottom blocks 5.00→4.90, taller. Re-rendered,
  full-deck montage scan (2 grids). s18 projector 50% PASS.
- **Iter 3** — s18: right PINN label → mid-height over its own teal
  shoulder (association без leader). Final render, all 32 snapshots
  sNN.png, anti-leak grep 0, notes 151–268.

## 7 P1 — закрыто

- **P1-1** вертикаль: `two_col_compare` body 14→17pt + box_h +0.5";
  `pipeline_row` body 12.5→14pt, head_h ↑; per-slide box→~85–90% canvas на
  s05/s10/s12/s13/s14/s16/s17/s21/s23/s24/s27/s28. Контент не добавлен.
- **P1-2** s26: box 5.05→5.18", cells single-line ≥14pt, формулировки
  col2/col3 компактнее (≤4 слов). Projector 50% PASS → **split НЕ нужен**.
  Schema §5.5 Matrix: fill 100% / icon/row / single-line / color-code / RU.
- **P1-3** мета снята из visible (footer/subhead, не speaker_notes —
  notes уже чисты): s11 «детали — в главе» убрано; s13 «(vendor-claim)…в
  материалах главы»→«по заявлению вендора»; s23 footer «на следующем
  слайде» убран; s24 subhead «(они на предыдущем слайде)» убран.
- **P1-4** s02: новый `bionic-bracket.svg→png` (rsvg, Ocean palette,
  лицензионно-чистая авторская вектор-иллюстрация: 2 крепёж-бобышки +
  load-eye + ветвящиеся рёбра + lattice-облегчения) вместо абстрактного
  эскиза. Узнаваемая «выращенная» форма — концепт-диссонанс работает.
- **P1-5** s31: матрица 9pt→12pt cells / 9.5→11pt headers, шире (mw
  6.35→6.85), выше строки; чек-лист gold-box 17pt circles доминирует
  (Phase-6 иерархия сохранена). Projector 50% PASS.
- **P1-6** s06: gold visible-сигнал «справочный скелет — 6 классов не
  заучивать сразу» (bookmark-иконка). s07≠s08: s07 = канонический
  грид-шаблон; s08 = ТРИ вертикальные класс-карточки с цвет-хедерами +
  3 сегмента ✓/✗/↳ (иной визуальный ритм; монотонность s06→s07→s08 снята).
- **P1-7** s18: 2 SOLID filled freeform-кривые (sharp blue spike vs broad
  teal shoulder) вместо тонких staircase-polyline; gold UP_DOWN_ARROW
  «занижение напряжения» в чистой зоне; подписи разведены. Schema §5.5
  chart: 5-sec teach PASS, projector 50% PASS.

## P2 — закрыто

s04 «шестии»→«шести» (build script уже верен — re-render фиксит);
s09 «1904–1989»→«классическая математика (Мичелл, Коши, SIMP)»;
s11 видимая аннотация «родословная (логический порядок), не хронология»;
s32 «office hours»→«консультации» + backup-3 «говорят»→«отвечают»;
s03+divider roadmap «Hook»→«Старт»; POD (s08) + LPBF (s13) + КИИ (s27)
first-use расшифрованы; deck.yaml:123 s30→s31; «топ-оптимизация»→
«топологическая оптимизация» first-use (s06/s07) + s14 title;
дубль-курсив снят: s07 субхед+футер, s14 футер, s22 футер (слит в callout).

## Schema-Readability §5.5

- **s06** schema_axis: 5-sec PASS, projector PASS, signal-banner visible.
- **s18** chart: 5-sec PASS, projector 50% PASS, solid curves ≥2pt.
- **s26** matrix 8×3: fill 100%, single-line ≥14pt, projector 50% PASS.
- **s31** matrix 6×5: ≥11pt headers/12pt cells, projector 50% PASS,
  чек-лист доминирует.

## Финал

32 слайда (без ренумерации), deck.yaml status=finalized v2. Cascade
удержан (s12/s17/s19/s21/s27 ≤3числа/≤4названия; s23 Mars ведущий; s24
без катастроф; s13 APM FEM без числа; диапазоны). Anti-leak grep: 0 hits
в visible. Speaker notes не тронуты (151–268 слов, контракт держится).
Escalations: 0 (все P1 закрыты ≤3 iter).
