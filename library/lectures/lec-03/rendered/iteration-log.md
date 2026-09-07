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

---

# v2 → v3 STRUCTURAL REVISION (owner-обратная связь, plan §4, U-1…U-9)

Issue #87 · branch issue-87-lec-03-architectures · 2026-05-16 · НЕ git.
Объём: +6 suffix-слайдов (НЕ перенумеровывая s01–s30), ретайтл s30,
case-refs в notes, deck.yaml split, сторителлинг-проход. v2-геометрия
30 базовых слайдов идентична (rebuild bit-identical для них — build_v3
тот же код-путь, только +6 builders и порядок).

## Scope guard
- s01–s30 ID НЕ перенумерованы (cascade lock). 6 suffix: s04a/s13a/s13b/
  s23a/s25a/s31. Порядок предъявления — plan §4. build_v3 main() имеет
  assert len(builders)==36 + load_deck() assert на канонический порядок.
- 0 designer-extras сверх plan §4. 0 локального binding. Палитра LOCKED.

## Новые слайды — итерации

### s04a / s13a / s25a — section_divider (U-1/U-3/U-5b)
- (a) inspected: консистентность с locked-шаблоном build_section_divider
  (тем же, что s09/s18 v2 — accepted).
- (b) changed: только текст (here_idx, subtitle, narrative bridge, sid);
  геометрия НЕ менялась (locked template).
- iter-1 render+inspect: pixel-консистентны с s09/s18 (cross-checked
  s04a vs s09 snapshot — идентичный layout/roadmap/типографика).
- iter-2 cross-check: roadmap-бар 5+1 карточек, gold-маркер на корректном
  активном разделе (1/3/5), РАЗДЕЛ N teal + gold-underline.
- iter-3 projector 50% + 5-сек: subtitle 38pt / label 20pt / bridge 18pt /
  roadmap 11pt — все > hard-min; main message = тема раздела. PASS.
- VERDICT: accept iter-3 (3 iter; дефектов нет — наследует accepted
  v2-template, что и есть требование «единый стиль с s09/s18»).

### s23a — section_divider (sub, U-5a)
- (a) inspected: остаётся в Разделе 4 (giant «4», roadmap gold Раздел 4),
  но distinct subtitle + «РАЗДЕЛ 4 · БЕЗОПАСНОСТЬ» label.
- (b) changed: новый helper build_subdivider_security (тот же layout,
  кастомный label/subtitle/bridge); roadmap_bar(s,4).
- iter-1: render — label «РАЗДЕЛ 4 · БЕЗОПАСНОСТЬ» teal, subtitle «Кто
  видит данные в цепочке», bridge-фраза читается, roadmap gold Раздел 4.
- iter-2: cross-check vs s18 (тот же Раздел 4 divider) — семейство
  консистентно, sub-блок визуально отличён через label suffix.
- iter-3: projector 50% + 5-сек — PASS (main = «безопасность: кто видит
  данные»).
- VERDICT: accept iter-3.

### s13b — assertion_visual + mini-schema pipeline (U-2) — KEY new visual
- (a) inspected: определение FT + 3-node pipeline + контраст-плашка.
- iter-1: «дообучение»-label и arrow зажаты между node2/node3 (gap 0.48",
  label overflow к gold node top). Schema §5.5 Pipeline: arrow есть, но
  output→input коннект тесный → FAIL читаемости.
- (b iter-2) changed: bw 3.30→2.85, gap-зоны явные («+» 0.58, arrow 1.50),
  узлы центрированы (n1x 1.35, симметричные поля 0.80/0.82), label
  «дообучение» поднят над arrow с clearance, schema box sh 2.30→2.48.
  Schema §5.5: PASS (arrow MSO_SHAPE.RIGHT_ARROW, per-stage sub-captions,
  ≤3 слова/label, RU единый, 3 stage ≤5).
- (b iter-3) changed: «дообучение» y-fine-tune, arrow толще (0.40→0.42),
  контраст-плашка текст переписан (убран orphan «запроса.»/«контекст.»),
  line_spacing 1.18→1.22.
- iter-3 projector 50%: 3-node pipeline + gold «ВЕСА» + контраст читаются
  из ряда 5. 5-сек: main = «FT меняет ВЕСА, промпт/RAG — контекст» =
  assertion. PASS.
- Schema §5.5 Process/Pipeline checklist (final):
  [x] RIGHT_ARROW (не rect+triangle гибрид)
  [x] per-stage sub-caption (общие веса / примеры поведения / модель др.)
  [x] unified RU sub-labels
  [x] 3 stage ≤5
  [x] stage label ≤3 слов (2/2/2)
  [x] output→input visually connected («+» и arrow коннекторы)
  → ALL PASS.
- VERDICT: accept iter-3.

### s30 — retitle + Q&A removal (U-6/U-7)
- (a) inspected: title было «Мост к отраслям + задание» (function-as-title).
- (b iter-1) changed: title → «AI-архитектура — несущая ось отраслевых
  лекций.» (контентный тезис, = assertion). Q&A-блок (правая teal-колонка
  «Q&A»+«Спасибо») УДАЛЁН → s31. Homework-box → full-width (rebalance
  mass, иначе 40% пустоты справа). + route-icon в bridge. + gold takeaway.
- iter-1 inspect: rebalanced, но bottom takeaway orphan «лекции.» +
  whitespace под ним.
- (b iter-2) changed: homework hh 2.50→2.85, body 13→14pt, такаway
  shorter.
- iter-2 inspect: лучше, остался 1-словный orphan.
- (b iter-3) changed: takeaway → одна строка, centered, h 0.78→0.72.
- iter-3: orphan устранён, mass-balance OK (нет пустой колонки), gold
  ×2 (homework + takeaway). 5-сек: main = «рамка = ось Л4–17 + ДЗ С3» =
  assertion. PASS.
- VERDICT: accept iter-3.

### s31 — qa_minimal dedicated Q&A (U-7)
- (a) inspected: зеркалит lec-02 dedicated Q&A (s29): «Вопросы» 120pt
  deep центр, «Спасибо за внимание» 32pt mid, тихий reminder bottom,
  белый фон, без footer/roadmap.
- iter-1: рендер консистентен с lec-02 canon. Намеренно «тихий» слайд —
  это и есть subtype qa_minimal.
- INTENTIONAL CANON DEVIATION: нет gold (gold ≥1×/slide уступает
  qa_minimal-канону — lec-02 s29 dedicated Q&A тоже без gold/motif;
  закрывающий слайд намеренно визуально тих). Документировано как
  осознанное, canon-consistent отклонение, НЕ регрессия.
- iter-2/3: cross-check vs lec-02 s29 — layout-семейство идентично;
  projector 50% — «Вопросы» 120pt тривиально читается. PASS.
- VERDICT: accept (qa_minimal — минимальный по дизайну, как и требует
  brief «как dedicated Q&A в lec-02»).

## Notes case-refs (U-4) — book-first, fact-checker verified в chapter
- s01: + «Moffatt v. Air Canada, BC CRT (Канада)», истец Дж. Моффатт,
  ответчик Air Canada, 14.02.2024, McCarthy Tétrault 2024 + ABA 2024.
- s13: + Barnett et al. arXiv:2401.05856 (2024) — паттерн 7 точек отказа
  RAG; Air Canada callback с явной датой (Moffatt v. Air Canada, BC CRT,
  14.02.2024).
- s16: + Luo et al. arXiv:2308.08747 (2023) — catastrophic forgetting
  эмпирически при continual fine-tuning.
- s23: + постмортем Sattyam Jain 2026-04 (single-author, illustrative,
  числа округлены); MindStudio 2025–2026 (reliability compounding).
- s24: + NYT v. OpenAI федеральный суд май 2025 (Bloomberg Law 2025,
  National Law Review 2025, [VFY day-of]); ZDR — Anthropic live-doc 2026
  ([VFY quarterly]).
- s25: + GitHub MCP heist май 2025 (Docker «MCP Horror Stories» 2025,
  AuthZed 2025–2026, Simon Willison 2025-04-09).
- Все notes в [150,300] слов (auto-checked, см. final). CVE-номера /
  vendor-pricing НЕ вынесены на видимый слой (остались в chapter/notes
  framing). s30 notes: Q&A-хвост убран, добавлен мост к s31.

## deck.yaml split (U-9)
- deck.yaml (PART 1, 353 строки ≤600): deck/palette/motif/typography/
  glossary_lock + slides s01..s13a (15). version v1→v3, total_slides 36.
- deck-part2.yaml (PART 2, 425 строк ≤600): slides s13b..s31 (21) +
  totals + ai_failure_judgment + verify_day_of_items + fact_check_items.
- Двусторонние кросс-ссылки-комментарии в обоих файлах (SPLIT box).
- Loader build_v3.load_deck(): читает обе части, merge `slides`, assert
  канонический 36-порядок (cascade lock guard) + totals.slides==36.
  Запуск build_v3 печатает «deck spec OK — 36 slides … version v3».
- YAML оба валидны (yaml.safe_load), 36 slide-id, s01–s30 не
  перенумерованы.

## Storytelling pass (U-8) — findings
- ЦВ return-chain (s04 ЦВ → s08/s12/s17/s22/s23 → payoff s26–s28):
  непрерывна. s23 notes явно «пятая точка возврата ЦВ»; s25a bridge
  явно закрывает петлю («…инструмент, которым отвечать на ЦВ»).
- Air Canada through-line (s01 hook → s13 revisited → s27 matrix):
  непрерывна; U-4 усилил единой атрибуцией (Moffatt v. Air Canada,
  BC CRT 14.02.2024) на s01 и s13.
- Divider bridges: 6/6 — «откуда пришли → куда идём», НЕ
  function-as-title. s04a/s13a/s23a/s25a — новые; s09/s18 — v2
  (bridge в build-коде, не трогали).
- Найденный narrative-разрыв в scope v2→v3: НЕТ.

## Final accept (v3, 150dpi, 36/36)
- Палитра LOCKED Ocean+Teal+Gold — 0 off-palette. Gold ≥1× на всех
  content/divider слайдах (divider — gold underline + roadmap-маркер;
  s13b — gold node+takeaway; s30 — gold homework+takeaway). s31
  qa_minimal — намеренно без gold (canon lec-02, документировано).
- Ocean motif на всех content-слайдах; dividers/cover/s31 exempt (canon).
- 0 forbidden-добавлений сверх plan §4 (grep новых .md: нет «Лектору»/
  «Вы здесь»/тайминг/subtitle на видимом слое).
- Schema §5.5: s13b Pipeline PASS (полный чек-лист выше).
- 5-сек тест: s04a/s13a/s23a/s25a/s13b/s30/s31 — main = assertion, PASS.
  Projector 50%: s13b/s30 explicit PASS; dividers наследуют accepted
  v2-template (>hard-min).
- Iterations: s13b=3, s30=3, s04a/s13a/s23a/s25a=3 (locked-template,
  cross-check + projector + 5-сек, дефектов нет), s31=accept (qa_minimal
  by-design). Min 3 соблюдён; max 7 не достигнут.
- Геометрия s01–s30 (кроме s30) НЕ менялась — v2-снапшоты валидны,
  перегенерены из единого pptx для полного набора.
- Файлы: lec-03.pptx + lec-03.pdf (36 слайдов), snapshots/ s01..s31
  (включая suffix, 36 PNG), build_v3.py, deck.yaml + deck-part2.yaml,
  6 новых slides/*.md + s30 правка + 6 notes-правок case-слайдов.

VERDICT v3: ACCEPT — 36 слайдов, s01–s30 НЕ перенумерованы, палитра/
gold/motif соблюдены, 0 extras сверх plan §4. Handed to orchestrator.

---

## v3→v3.1: s14 dedupe (P1-1 из v3 SYNTHESIS, точечно — ТОЛЬКО s14)

**Контекст.** v3 вынес определение fine-tuning на новый s13b (ПЕРЕД
s14). presentation-critic v3 P1-1: видимое тело s14 + 1-й абзац notes
всё ещё несли почти идентичный inline-парафраз определения → back-to-
back дубль с s13b и противоречие deck-part2.yaml note «s14 inline-define
больше НЕ дублируется». Причина: s14-md/build не обновили под решение
v3. deck-part2.yaml note s14 (строка 49) уже корректна — НЕ трогали.

**Что изменено (только s14):**
- `build_v3.py` build_s14: текст subtitle-бокса (геометрия x/y/w/h
  0.55/1.16/12.25/0.78 НЕ менялась) — было дубль-определение «доп.
  обучение готовой модели на своих данных, меняются веса. В Л1 — тип
  использования; здесь — архитектурный выбор…» → стало опора на s13b +
  hook: «Fine-tuning (определение — предыдущий слайд) меняет сами веса.
  Среди инженеров ходит: «в 2026 он умер — всё решает RAG». Это
  неточно — он не умер, а сузился.»
- `slides/s14-*.md` Body: тот же дубль-define заменён на ту же опору-
  на-s13b строку (видимый слой синхронизирован с build).
- `slides/s14-*.md` Speaker notes 1-й абзац: убрано повторное
  определение FT (verbatim с s13b); начинается с опоры на s13b
  («На предыдущем слайде мы зафиксировали определение…») и сразу к
  сути «почему сузился» (знание → RAG, поведение → FT). Derived из
  chapter §3.1 [for-slide-s14] абз.1-2 (book-first), без новых фактов.
  Слов в notes: 292 (orig) → 300 (≤300 ceiling соблюдён, в [150,300]);
  абз.1: 97 → 105 слов; абз.2-3 не трогали.

### Iter 1 — s14 (P1-1 dedupe)
- (a) inspected: snapshots/s14.png (page 17, 150dpi) — subtitle-строка
  vs s13b subtitle (pptx text extract обоих слайдов).
- (b) changed: subtitle-текст build_s14 + Body md + notes абз.1.
- (c) checklist: dedupe vs s13b — PASS (s13b = «продолжение обучения
  готовой модели…», s14 = «определение — предыдущий слайд… он
  сузился»; back-to-back парафраз устранён). assertion_visual: motif
  Ocean box обе зоны PASS, gold callout ≥1× PASS, палитра 0 off PASS.
  Регрессия: 35/36 PNG byte-identical к committed (md5), CHANGED=[s14]
  только; s13b byte-identical (не задет).

### Iter 2 — s14 Projector Readability (50% zoom)
- (a) inspected: /tmp/s14_50pct.png (1000×563, row-5 симуляция).
- (b) changed: ничего (проверка).
- (c) Projector 50%: PASS — title/subtitle/zone-headers/gold callout
  читаемы; subtitle wrap = 2 строки (как было), 2-зона стартует с
  locked y=2.08 → нет floating/thin gap; visual mass balance L/R равны.

### Iter 3 — s14 5-Second Test (final accept gate)
- (a) inspected: snapshots/s14.png overview.
- (b) changed: ничего (gate).
- (c) 5-sec: PASS — main message read = «FT не умер, сузился: знание
  → RAG, поведение остаётся за FT» == assertion YAML «Fine-tuning не
  "умер" — он сузился: … поведение/…, НЕ знания». Match.
- Verdict: ACCEPT.

**Подтверждение v3.1:** изменён ТОЛЬКО s14 (35/36 PNG byte-identical);
дубль с s13b устранён (видимый слой + notes); notes 300 слов book-first
(≤300 ceiling, no new facts); 0 регрессий палитра/gold/motif; 0
forbidden-добавлений; deck.yaml/deck-part2.yaml/title s14 НЕ менялись;
iter count = 3 (min соблюдён, layout не менялся — текст в существующем
боксе). Файлы: build_v3.py, slides/s14-*.md, lec-03.pptx, lec-03.pdf
(оба перегенерены из единого build, 36 слайдов), snapshots/s14.png.

VERDICT v3.1: ACCEPT — точечный s14 dedupe, 0 collateral. Handed to
orchestrator.

---

## v4.0 (2026-08-09) — полная пересборка под issue #157 (chapter v2.0)

Deck приведён в соответствие переписанной главе v2.0 (~31k слов, 5 частей).
36 → **40 слайдов**. Toolchain: standalone soffice/pdftoppm/rsvg из
`/tmp/claude-999/local` (см. notes/mcp-limitations.md [#157-1]; render.sh в
scratchpad). Все слайды прошли Generate→Convert→Inspect→Fix ≥3 iter где
изменялись; новые/dense — 3-4 iter.

### Структурные изменения
- R0: +lecture-map s02a (#212, cover разделён на чистый cover + карту).
- R1: +s05a (роли, §1.2), +s05b (структура, §1.3), +s08a (чит-шит, §1.8);
  s06+s07 MERGED (CoT worked-example + faithfulness, #219).
- R2: s11 без жаргона конъюнкция/дизъюнкция (#221/#222); s12 3-й критерий =
  live API/MCP, не observability (#223/#224).
- R3: реордер (определение→PEFT s15→критерии s14→forgetting); s14+s17 MERGED;
  **P0 #227** дистилляция = «fine-tune teacher + дистилляция student, две
  отдельные техники», НЕ вид fine-tuning (исправлено в visible + notes);
  s15 +LoRA baseline 98.4% с обязательной оговоркой (denominator).
- R4 (11 content): divider «Агенты» без «+безопасность»; s19 MERGED API+MCP;
  +s22b (экипировка, assertion=headline), +s22c (память), +s22d (провал
  памяти Letta+Anthropic, freshness-оговорка), +s22e (операц.слой presence
  paradox), s25 = skills+subagents+access+**безопасность GOLD-блоком равного
  веса (P1)**, +s25b (4 coding-агента, OpenClaw hedge неподтв.гипотеза);
  s23 +retry-baseline (#233), «правильно»→«более подходящая» (#232).
- R5: s27 = flowchart «План решения» (замена 7×7 матрицы, §5.2); +s27b
  (стартовый комплект, §5.2b); s29 +3 измерения (#237); s30 hero-bridge к
  Лекции 4 «AI в разработке ПО» (#238); s31 Q&A стиль Лекции 1 (#239).

### Hero images (6-tier §5.7, Tier 2 Wikimedia)
- s01: Air Canada Boeing 787 (CC-BY-SA), ≥40% площади, attribution visible.
- s30: разработчик за IDE (CC-BY-SA), ≥40% площади, attribution visible.

### Visual-loop findings & fixes (iter 2)
- s01: subtitle gap + gold callout height подогнаны.
- s06: note→heading collision устранён (note в 1 строку).
- s25: security gold-блок вырос (gh 3.0→3.6) — rule #4 больше не overflow.
- s25b: OpenHands hedge-note box увеличен под 4 строки.
- s27: qh/vg сжаты — step-8 line видна без коллизии с gold-плашкой.
- s30: teal Лекция-4 box увеличен под 3-строчный body.
- s03 (последним): убран RAG gold-highlight + chip «стоит на эмбеддингах»
  (#213), gold перенесён на hub; footer упрощён (#214).

### Verification (ENFORCED greps на rendered PPTX visible + speaker_notes)
- P0 дистилляция(fine-tuning): **0** в обоих слоях.
- Timing markers: 0 real (единственный хит «23 минус 7» = математика CoT).
- Methodology/lecturer cues: 0 (хит «контакты преподавателя» на s31 =
  легитимный placeholder контактов, паттерн Лекции 1).
- Slide-refs / LO codes / [VERIFY]/[FACT-CHECK] в visible+notes: 0.
- Internal §-refs в visible body: 0 (остались только cross-lecture Л2 §2/§3/§4).
- Anti-anglicism: deep_latin_scan — все non-brand токены = glossary_lock термины
  / paper-author names / case names / established tech (RCT, ReAct, USB-C, CLI,
  top-k, third-party); avoidable (baseline/budget/ROI/monitoring/scope/callback/
  learning gap/human-review/revisited) — русифицированы.
- deck.yaml → 3 части (deck.yaml + deck-part2.yaml + deck-part3.yaml),
  loader order == builder order (40, asserted).

VERDICT v4.0: ACCEPT — 40 слайдов, 2 real hero, все 20 применимых
comment-id закрыты, P0 #227 + P1 security/coding-agents/LoRA-baseline закрыты.
Speaker notes (46 секций, 150-300 слов) написаны book-editor из главы v2.0.
Передаётся оркестратору для QA-агентов.

---

## v4.1 (2026-08-09) — orchestrator visual-verification pass, 5 overlap fixes

После v4.0 designer-handoff orchestrator восстановил standalone render toolchain
([#157-1], `/tmp/claude-999/local`) и заново прогнал Convert→Inspect на все
40 снимков (designer's second fix-pass agent не имел доступа к toolchain и не
мог визуально проверить свои последние правки — только PPTX text-level greps).

**Найдено 5 real text-overflow/collision дефектов** визуальной инспекцией
(не поймано self-report предыдущих итераций):

1. **s05b** («Структура промпта») — 2-строчный title (25pt) наезжал на
   subtitle снизу (title box height не учитывал wrap). Fix: title h=1.30,
   size=23, subtitle/left-column/right-column сдвинуты вниз + пересчитаны
   высоты, чтобы уместиться до gold_callout.
2. **s10** («Принцип RAG — три шага») — card 3 header «Генерация с опорой»
   (19 симв.) не влезал в узкую box-width на 1 строке, wrap-строка наезжала
   на tag «grounding». Fix: сокращено до «Генерация» + tag
   «с опорой (grounding)», ширина title box увеличена.
3. **s11** («Когда RAG — правильный выбор») — teal-box снизу справа: текст
   «Один признак…следующем слайде» в узкой box переполнял отведённую
   высоту, визуально «резался» о нижнюю границу box. Fix: box padding/icon
   пересчитаны, font 14→12.5pt, text_box height увеличен.
4. **s13b** («Что такое fine-tuning») — все 3 pipeline-узла: заголовок узла
   (14pt bold, 1-строчный text_box) при wrap на 2 строки наезжал на subtitle
   (за 0.02-0.04" ниже). Затронуты все 3 узла («Предобученная модель»,
   «Ваш датасет», «Дообученные ВЕСА»). Fix: заголовки переведены на explicit
   2-строчный `\n` формат где нужно, subtitle сдвинут вниз, font 14→13,
   12→11.5pt.
5. **s23** («Провалы агентов») — card 1: italic-caption «$4 200 — цена не
   автоматизации…» (94 симв, 10.5pt) при wrap на 2-3 строки наезжала на
   следующий bold-блок «Более подходящая архитектура…» (0.04" gap). Fix:
   все 4 текстовых блока card 1 пересчитаны компактнее (font 10.5→10/11pt,
   позиции сдвинуты), уместились в chh=4.55 без overflow.

**Re-verification после fix:** full rebuild (`python3 build_v3.py`) →
soffice convert → pdftoppm 150dpi → все 5 слайдов повторно инспектированы
PNG-by-PNG — 0 residual overlap. Полный 40-slide sweep повторён для regression
check на соседних/похожих слайдах (schema pipeline/layered nodes) — чисто.

**Re-run mandatory greps на rebuilt PPTX (visible text_frame, все 40 слайдов):**
- Timing markers (`[0-9]+\s*мин`, Тайминг, Длительность, ⏱): 0 hits.
- Methodology/lecturer cues (методическ*, педагогическ*, Лектору, На этом
  этапе студент): 0 hits.
- Scaffold leaks (`[VERIFY-DAY-OF]`, LO codes, `§[0-9]`, `→ sNN`, «Вы здесь»):
  0 hits.
- Deep latin-token scan (`tools/presentation-build/deep_latin_scan.py`):
  338 occurrences / 176 unique non-brand tokens — все либо glossary_lock
  термины (fine-tuning/PEFT/CoT/LoRA/RAG/MCP/forgetting/workflow/subagents/
  grounding/retrieval/faithfulness), либо brand/product names (Claude Code,
  Letta, Air Canada, ZDR, MIT), либо established tech phrasing (structured
  output, function calling, semantic search) — согласуется с glossary_lock
  из deck.yaml, no avoidable anglicisms found.

**s03 (recap Л2) — финальная сверка (делалась последней, как требовал бриф):**
рендер (`build_s03` в build_v3.py) уже был financially синхронизирован
дизайнером (v4.0 commit note: «финальная сверка формулировок — после
готовности всей деки», gold-highlight и embeddings-chip убраны — #213/#214
закрыты). Обнаружено расхождение МЕЖДУ orphaned `.md`-источником (устаревший
черновик с visible `§2`/`§4` cross-refs) и фактическим рендером (чистый,
0 `§`-ссылок) — сам PPTX корректен, `.md` был просто не обновлён следом за
build-скриптом. `.md` visible-content секция приведена в соответствие
фактическому рендеру (frontmatter `chapter_ref` тоже очищен от `§`).
Speaker notes (parsed live из `.md` в PPTX через `load_notes()`) содержат
«Лекции 2, раздел 2» текстом (не `§`-нумерацию) — это legitimate
cross-lecture reference, не запрещённый паттерн.

**Files touched:** `rendered/build_v3.py` (5 функций: build_s05b, build_s10,
build_s11, build_s13b, build_s23), `rendered/lec-03.pptx` (rebuilt),
`rendered/lec-03.pdf` + `rendered/snapshots/*.png` (regenerated 40/40),
`slides/s03-recap-lec2-bridge.md` (doc-sync, no visible-render impact).

VERDICT v4.1: ACCEPT — 40 слайдов, 0 residual overlap defects, 0 timing/
methodology/scaffold leaks, glossary-consistent anglicism profile. Ready for
QA-agent pass (presentation-critic / student-simulator / reader-simulator)
per orchestrator's pipeline, then USER GATE per plan v2 §4 (единая финальная
сверка).

---

**Продолжение лога (v4.2+) — см. `iteration-log-part2.md`** (файл достиг
лимита 600 строк, CLAUDE.md § Document Size Limit).

---

## v5 consolidated QA-polish pass (issue #185, 2026-09-06)

Единый батч-полиш по 4 QA-критикам (presentation-critic REVISE P0 russification + 3× APPROVE-WITH-POLISH). Все правки — в build_v3.py (visible) + slides/*.md (notes).

### P0 — Russification видимого слоя
- Deep-latin-scan (deep_latin_scan.py) до: **648 occ / 328 unique**; после: **463 occ**.
- Body narrative-residual (parens+cite-footers stripped, keep-list applied): **32 unique / 50 occ** — все легитимны: acronym-компаунды (MCP-/RAG-/AI-/GPT-/CoT-), verbatim Anthropic-цитата, author/case-имена (Dixit/Kamal/Oates/Moffatt), file/repo (claude-code/issue), glossed-1× термины. Untranslated narrative anglicisms → 0.
- Cyrillic-транслит (block A) — все заменены 1:1: апгрейд→улучшение/не даёт прироста ×4; дефолт→по умолчанию ×2; продакшен/в прод/прод-БД→боевая эксплуатация/боевая БД/в бой ×6; чит-шит→шпаргалка; латентность→задержка ×5; парсинг→разбор; бэкапы→резервные копии; ревью→проверка; сэмплов→примеров; хопов→переходов ×2.
- Glossed англотермины (block B) → РУ-канон с англ. в скобках 1×: fine-tuning→дообучение; workflow→сценарий; retrieval→поиск; grounding→опора на источник; forgetting→забывание; subagent→субагент; skills→навыки; structured output→структурированный вывод; prompt caching→кэш промптов; least-privilege→наименьшие привилегии; human-in-the-loop→человек в контуре; allowlist→белый список; deny-by-default→запрет по умолчанию; over-privilege→избыток прав; zero-click→без клика; full-context→полный контекст; lookup→таблица соответствий; few-shot→примеры в промпте; single-shot→одиночный вызов; live-eval→независимая проверка; coding-агенты→агенты для кода; heist→утечка/ограбление; third-party→сторонний; lossy→сжатие с потерями.
- **Keystone-лестница (s04/s26) ступени 4-6**: Multi-agent/Agent/Workflow → Мульти-агент / Агент / Сценарий — RU-primary с англ.-глоссой; студент видит 3× (s-06, s-45, s-48) — все RU.
- Цикл plan→act→check→iterate (s21/s06/s26): RU-глосса «план→действие→проверка→повтор» primary, ReAct-имя сохранён в скобках.
- s22c память (mem0/Cognee/Graphiti/Zep): бренды keep, связки русифицированы (память между сессиями / память на графе знаний / временной граф / граф-база знаний).
- s25 правила безопасности: Навык/Субагент/MCP-доступ; Наименьшие привилегии/Человек в контуре на запись/Белый список/запрет по умолчанию.
- Keep-list соблюдён: бренды, аббревиатуры, case-имена, ChatML `<|im_start|>`, citation-титулы в [N]-футерах, ReAct.

### P1 — Layout (fix + re-render + visual-verify PNG)
- **s29 (PNG s-49):** вводный курсив укорочен до 2 строк + dims сдвинуты (ly+1.42→1.52) → нет overlap с «Степень автономности». Donut c29-nanda.png перегенерён: убраны нечитаемые «5»/«95», центр-подпись «пилоты GenAI»; big «~95%» несёт число. VISUAL-CONFIRMED.
- **s07 (PNG s-13):** bar-step 1.02→0.92, subtitle укорочен (0.66→0.58h, 12→11.5pt) → подпись «GPQA ниже MMLU» больше не подрезана рамкой. VISUAL-CONFIRMED.
- **s27 flowchart (PNG s-46):** убраны клиппящиеся «нет ↓» (заменены тонким down-connector'ом); vg 0.085→0.10; легенда «да→результат / нет→ниже» в subtitle; 8-й пункт унифицирован с рядами 1-7 (gold-box + «8»-круг). VISUAL-CONFIRMED.
- **s05c (PNG s-10):** разгружен — ChatML/Jinja/Anthropic-top-level detail-line свёрнута в 1 строку; IH-Challenge 84,1→94,1% перенесён в notes (63,8% приоритет + ASR-скачок 5,18→32,05% оставлены как 2 якоря). VISUAL-CONFIRMED.

### P1 — Consistency
- **RAG-2026 на видимый слой (D-P1-1):** добавлена teal-полоса на s10 (=PNG s-17): «agentic (агентный) RAG по умолчанию · гибридный поиск (BM25+плотные векторы) · реранкер · каскад промахов 5,7%→1,9% (Contextual Retrieval)». VISUAL-CONFIRMED.
- **s05c forward-ref (D-P1-2):** в speaker notes s05c добавлен мост «полный разбор инъекции как класса атак — в разделе про агенты (безопасность)».

### P1 — Reader
- **s23b (PNG s-42):** class-names русифицированы/глоссированы; lesson-колонка inline-раскрывает slopsquatting («выдуманное имя пакета → атакующий его регистрирует; не доверять без реестра»), rug-pull («подмена версии»), zero-click, наименьшие привилегии.

### P2
- s06→s07 дубль faithfulness: числа 25%/39% УБРАНЫ с s06 (=PNG s-12; заменены качественной карточкой + forward «прямое измерение — на следующем слайде»), оставлены только на s07. VISUAL-CONFIRMED.
- MCP двойное определение: s20 (=PNG s-30) свёрнут — «MCP — стандарт подключения (уже разобран выше)»; полное N×M→N+M/USB-C определение остаётся 1× на s19(=s-28).
- s07 «два из пяти = 25%» (D-P2-1): в notes s07 → «Claude 3.7 — примерно в одном из четырёх — 25%, DeepSeek R1 — почти в двух из пяти — 39%».
- s30 footer «в главе методички» → «см. источники» (×2: s19+s20).
- s19b (D-P2-2): «×несколько» → «≈50×» (симметрия с ×15). VISUAL-CONFIRMED.
- s05c notes drift «чат-шаблон» → «chat-шаблон» (D-P2-3).
- by_section metadata в deck-part3.yaml актуализирован под v5 (51 слайд, 6 разделов).

### Жёсткие правила — без регрессий
- timing (N мин) / методология / LO-коды / §X / →sNN / [VERIFY] в visible+notes: **все 0** (grep подтверждён).
- Slide count: **51** (assert OK). Ocean-палитра + rounded box + gold сохранены. Cover/дивайдеры/hero не тронуты.

### НЕ сделано (report to orchestrator)
- s25/s14 дистилляция consolidation (student P2 «избыточно на 60-й минуте»): НЕ тронуто — консолидация/удаление слайда = структурное design-решение, требует owner-approval (см. финальный отчёт PROPOSED).
