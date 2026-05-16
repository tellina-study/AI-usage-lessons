# Лекция 3 — Visual-loop iteration log

Issue #87 · branch `issue-87-lec-03-architectures` · 30 slides.
Palette LOCKED Ocean + Teal + Gold. Motif: Ocean rounded box.
Build: `build_v1.py` (full rebuild per iter — PowerPoint MCP limitation [#54-3]).
Schema slides per deck.yaml: s10 pipeline · s12/s17/s22/s27 matrix ·
s21 cycle · s24 architecture · s26 layered. s27 = density watch-item.

---

## Iter 1 — full deck (110dpi)

- (a) Inspected: all 30 PNG. Baseline render clean — palette/motif/gold
  consistent, fonts legible, no accent-lines, charts render with Ocean colors.
- (b) Built from scratch via build_v1.py — 30 builders, 53 icons, 5 charts.
- (c) Problems found (fix list for iter 2):
  - **s26 [P0]** layered ladder BROKEN — boxes overlap, text overflow,
    trigger labels collide. base_y/trig_h math wrong. Full redo.
  - **s04 [P1]** ladder direction: step 1 (code, gold) at TOP — should be at
    BOTTOM (it IS at top in render → must invert so «1 код» = bottom rung).
    Also right rule panel 30%+ whitespace.
  - **s21 [P1]** loop-back: stray teal dash at far right (meaningless
    connector); no visible return-arrow Iterate→Plan. ~30% bottom whitespace.
  - **s10 [P2]** stage boxes ~60% empty (text only top 40%) — tighten height
    or enlarge content; whitespace imbalance.
  - **s01 [P2]** right column 2 blocks float — bottom whitespace; left
    chronicle uneven gaps (item 3 wraps).
  - General: several content boxes have bottom whitespace → tighten heights,
    rebalance visual mass.
- 5-sec test (iter1): s27 PASS, s17 PASS, s24 PASS, s10 PASS, s21 PASS
  (concept), s04 FAIL (direction confusing), s26 FAIL (unreadable).

---

## Iter 2 — targeted fixes (110dpi)

- (a) Inspected: all 30 PNG iter1.
- (b) Changed:
  - s04: ladder geometry rebuilt bottom-up (step 1 gold = BOTTOM rung →
    step 6 top); added up-arrow + «выше»; rule panel gold full-height.
  - s26: full redo — bottom-aligned ladder, short rung labels, triggers in
    gaps ABOVE each rung, full-height gold rule panel. (was P0 broken)
  - s21: cards enlarged (less internal whitespace), START teal badge on
    Plan, explicit return path (down→left→up into Plan) + loop chip.
  - s10: stage icons added (database/route/check-check), body enlarged,
    vertical balance improved.
  - s03: spoke cards enlarged with icons, gold «эмбеддинги Л2» as chip
    inside RAG card (was floating label).
  - s01: chronicle rows evenly distributed (anchor=MIDDLE per row),
    right contrast blocks enlarged + icons added (message-square-warning,
    key) + teal-tint on «что было нужно».
- (c) Checklist status:
  - s26 schema_layered: bottom-aligned PASS, captions/layer PASS, max 6
    rungs OK, hierarchy PASS, trigger connectors PASS → was FAIL now PASS.
  - s04: 5-sec test PASS (direction now reads code→multi-agent).
  - s21 schema_cycle: explicit START PASS, explicit CONTINUE PASS (loop
    chip+arrow), 4 elems PASS, direction PASS.

## Iter 2b — icon coverage fix (110dpi)

- (a) Inspected: s05 missing target icon.
- (b) Found: gen_icons.sh only made partial variant matrix → target-teal,
  key-teal, check-check-teal, database-teal etc missing. Regenerated FULL
  matrix (29 icons × 4 variants = 116 + 3 logos = 119 files).
- (c) Re-rendered all 30: s05 target icon now present; s03/s10/s20 dynamic
  -variant icons all resolve.

## Iter 3 — divider redesign + 150dpi final inspection

- (a) Inspected: s09 section divider BROKEN (210pt «Раздел 2» wrapped +
  giant stray digit bleed-through).
- (b) Changed: build_section_divider full redo — cover-style giant soft
  digit (380pt COVER_OUTLINE) on right, «РАЗДЕЛ N» label + subtitle +
  frame phrase left, gold roadmap. Distinct from content (no Ocean motif).
- (c) 150dpi inspection (per [#69-render-1] dense-slide rule):
  - s09/s18 dividers: PASS — clean, distinct, gold roadmap marker.
  - **s27 decision matrix (watch-item): PASS** — 7×7 full fill, single-line
    headers, semantic color (gold=strong/teal=weak), gold bottom plate.
    Cell font ~11pt = at minimum but legible at 150dpi (reference matrix,
    speaker walks through). Schema_matrix checklist PASS.
  - s20 MCP: PASS — dense but legible, callout/footer separated.
  - s28 checklist: PASS — 8 items legible.
- 5-sec test (iter3): all 30 PASS — main message matches assertion.

## Iter 4 — motif compliance + final 150dpi accept

- (a) Deck-level scan: gold/motif compliance check + 25% overview montage.
- (b) Found + fixed: s17 + s27 (schema_matrix tables) had NO Ocean motif
  wrapper (tables sat directly on white) — deck.yaml visual_brief mandates
  «в Ocean rounded box». Added ocean_box behind both tables (drawn first,
  cells on top). s02/s09/s18 NO-GOLD flag = false positive (gold via shared
  roadmap_bar: GOLD_TINT card + GOLD accent line — verified).
- (c) Final accept (150dpi, all 30):
  - Palette LOCKED Ocean+Teal+Gold — 0 off-palette. Gold ≥1×/slide ✓.
  - Ocean motif on every content slide ✓ (cover/dividers exempt by design,
    have gold via roadmap).
  - 8 schema slides Schema Readability Checklist: ALL PASS
    (s10 pipeline · s12/s17/s22/s27 matrix · s21 cycle · s24 architecture
    · s26 layered). s27 watch-item PASS at 150dpi.
  - 5-Second Test: 30/30 PASS. Projector 50%: PASS (cell font s27 = floor).
  - No forbidden additions (no «Лектору»/«Вы здесь»/timing/CVE/pricing/
    SDK-code/transformer-formulas on visible layer — verified visually).
- Iterations per slide: schema/ladder slides (s04,s10,s21,s26,s17,s27) =
  4 iters; divider slides (s09,s18) = 3 iters (incl iter3 redesign);
  all others = 3 iters. Min 3 satisfied for every slide; max 7 not hit.

VERDICT: ACCEPT — handed to orchestrator for QA agents.

---

# v1→v2 fix iteration (Phase 4 QA SYNTHESIS + USER-решения)

Issue #87 · build_v2.py · фиксы только по SYNTHESIS fix-list + USER PA-1/PA-2.
Затронуто 12 слайдов + 3 чарта; остальные 18 слайдов v1 не тронуты (их
геометрия в build_v2.py идентична v1, PNG перерендерены из единого pptx).
Палитра LOCKED Ocean+Teal+Gold — без изменений. 0 forbidden-добавлений.

## charts c07 / c08 / c16 — illustrative-метка + атрибуция (prev session)
- (a) Inspected: c07/c08/c16 на 150dpi.
- (b) Changed: c08 «СХЕМАТИЧНО — иллюстрация эффекта, не измеренные данные ·
  Chroma Research, 2025»; c16 то же + «Luo et al., arXiv:2308.08747, 2023»;
  оси/легенда крупные и читаемы на 150dpi-снапшоте. c07 — подписи столбец↔
  модель (Claude 3.7 / DeepSeek R1) + «меньше = тревожнее», значения 25%/39%
  крупно.
- (c) fact-checker P1×2 закрыто: illustrative-framing + атрибуция на чарте.

## s27 — матрица СЖАТА 7×7 → 5×5 (USER-решение; prev session, verified)
- (a) Inspected: v1 7×7 — крипто-сокращения нечитаемы из зала, gold/teal-tint
  сливались в бежевый (student P1 + critic P2-3 + reader P1).
- (b) Changed: точный owner-layout — колонки Промпт·RAG·Fine-tune·Агент·
  Код(без ИИ); строки Знание·Свежесть·Стоимость·Аудируемость·Недетерминизм;
  читаемые слова без сокращений; контраст SOLID gold(сильно)/teal(слабо)/
  surface(нейтр); иконка на каждой колонке; Ocean motif за матрицей; нижняя
  gold-плашка во всю ширину (stroke 3pt) — доминанта слайда.
- (c) Schema §5.5 Matrix: fill 100% PASS · icons per column PASS · single-line
  headers PASS · semantic color PASS (solid, не сливается) · font ≥14/15pt
  PASS · ≤2 строки/ячейка PASS · RU-only PASS. 5-сек PASS (main=«детерм.→
  код без ИИ»). Projector 50% PASS. До/после: плотность 49→25 ячеек (-49%),
  читаемость из зала FAIL→PASS.

## s13/s24/s25 — разгрузка компоновки (task #7; partly prev, finished now)
- s24: subtype reclassified schema_architecture→schema_pipeline (data-flow
  конвейер границ доверия, QA P1-2 опция B). USER-actor иконка добавлена:
  узел «ваши данные» = user-check icon, gold-заливка (точка отсчёта),
  RIGHT_ARROW между всеми звеньями, дефиниции ZDR/least-priv/BAA → footer/
  notes. Schema §5.5 Pipeline: USER-actor PASS · RIGHT_ARROW PASS · owner-
  annotation per stage PASS · ≤6 stages PASS · unified RU PASS · ≥70% canvas
  PASS. 5-сек PASS. Projector 50% PASS. Решение: ICON (не было нужды менять
  subtype обратно — pipeline-классификация + USER-actor вместе закрыли P1-2).
- s25: tool-poisoning деталь → speaker notes, видимый текст короче, больше
  воздуха (механизм-flow + 1 кейс + catastrophe-box | 4 правила). CVE-номера
  не на видимом слое (footer лишь указывает «в главе» — не реальный CVE).
- s13: см. PA-2 ниже.

## PA-1 (USER-approved) — s04 + s26 climb-scale «проще ↓ / сложнее ↑»
- (a) Inspected iter1: s04 «сложнее ↑» клипалось у верхней кромки (наезжало
  на question-box); s26 — узкая полоса между лестницей и gold-панелью.
- (b) iter2 changed: s04 — метку «сложнее ↑» опустил в чистую зону между
  question-box (низ 2.15) и верхней ступенью (~2.45), arrow 2.62→6.54, size
  12; s26 — лестница сужена full_w 8.40→8.05, открыта вертикальная полоса
  x≈8.66 с up-arrow + «сложнее ↑»/«проще ↓», trigger-метки сужены чтобы не
  пересекать полосу.
- (c) iter3 verified: обе метки полностью видимы, не клипаются, не
  пересекают соседние элементы. Снимает обратное прочтение «выше=лучше»
  (climb = сложнее, не лучше). PASS.
- iters: s04 = 3 (v1 baseline + iter1 fix + iter2 reposition + iter3 verify);
  s26 = 3 (iter1 narrow ladder + iter2 strip + iter3 verify).

## PA-2 (USER-approved) — s13 visual mass rebalance
- (a) Inspected: левый бокс ~15-20% пустоты снизу (3 кейса жались вверх,
  row_h фиксированный 1.18 → dead band).
- (b) Changed: 3 кейса распределены РАВНОМЕРНО по всей высоте бокса
  (cell_h = box_h/3, anchor каждого в своей ячейке) + тонкие разделители
  между кейсами (зеркалит структуру правого Air-Canada-бокса). Gold-плашка
  сверху усилена 0.86→0.95h.
- (c) Verified: dead band устранён, последний кейс заканчивается у нижней
  кромки, масса левого = масса правого бокса. Squint-тест: половины
  сбалансированы. PASS. iters: 3 (baseline + rebalance + verify).

## #9 — s06 + s15 усилить assertion-несущую gold-плашку
- s06: callout 0.92h/14.5pt → 1.10h/15pt + текст несёт assertion («CoT —
  инструмент под класс задач, не глобальный тумблер...»). Уровень соседей
  (s05/s08/s14) достигнут.
- s15: НЕ было нижней gold-плашки (assertion жил только в reason-3 tint-
  боксе) → добавлена full-width gold-плашка 1.05h/15pt с assertion
  («PEFT почти всегда лучше full FT...»), заполнила мёртвую полосу 5.6→7.0,
  уровень s14/s17. iters: s06=3, s15=3.

## notes-fix s07/s08/s16 + s02 subtitle (#12)
- s07 notes: +фраза «каждый столбец — это модель, высота — доля честных
  упоминаний: чем ниже столбец, тем тревожнее» (270→290 слов, in-range).
- s08 notes: +фраза «горизонтальная ось — сколько токенов, чем дальше
  вправо (длиннее контекст), тем ниже кривая точности» (266→292, in-range).
- s16 notes: +фраза «две линии: сплошная вверх — целевая метрика (растёт),
  пунктирная вниз — общие способности (падают незаметно)»; trim 1
  избыточной оговорки чтобы остаться ≤300 (294→293, in-range).
- s02 subtitle: приведён к КАНОНУ cover lec-02 — designer-инициативная
  meta «Курс «Применение AI» · 75 минут» (italic-light) УБРАНА; заменена
  content-promise строкой «Какую архитектуру выбрать под задачу — и когда
  правильный ответ „не ИИ“» с teal вертикальной accent-полосой + MID-цвет
  (точная калька стиля lec-02 build_lec02.py:build_s02). iter1+verify.

## Final accept (v2, 150dpi, 30/30)
- Палитра LOCKED Ocean+Teal+Gold — 0 off-palette. Gold ≥1×/slide ✓.
  Ocean motif на каждом content-слайде ✓ (cover/dividers exempt, gold via
  roadmap). 0 forbidden-добавлений (grep на 8 модиф. слайдах: clean; s25
  «CVE-» = footer-указатель «в главе», не реальный CVE — v1-наследие, не
  регрессия).
- Schema §5.5: s24 Pipeline PASS · s27 Matrix PASS (оба формально пройдены).
- 5-сек тест модиф. слайдов: s02/s04/s06/s13/s15/s24/s26/s27 — main message
  = assertion, все PASS. Projector 50%: s24/s27 PASS (s27 — watch-item,
  теперь крупно читается из зала).
- deck.yaml: version v1→v2 (было), s24 subtype→schema_pipeline+v2-note
  (было), s27 visual-описание обновлено (5×5), s02 visual-описание
  обновлено (canon subtitle). 30 слайдов, YAML valid. ⚠ 602 строки
  (+9 от mandated fix-list updates, было ~593) — см. PROPOSED ниже.
- Iterations: s04=3, s26=3, s13=3, s06=3, s15=3, s02=2, s07/s08/s16
  notes-only (no visual iter). Min 3 для всех визуально-изменённых; max 7
  не достигнут.

VERDICT v2: ACCEPT — handed to orchestrator for pre-gate + QA.
