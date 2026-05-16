VERDICT: APPROVE-WITH-POLISH

# Presentation Critic Report — Лекция 3 «Архитектуры AI-систем» — 2026-05-16 (v3)

Issue #87 · branch `issue-87-lec-03-architectures` · структурная ревизия v3 (+6 слайдов).
Vision-enabled review: все 36 PNG-снапшотов прочитаны через Claude vision +
целевые кропы (s13b top/mid/bottom для §5.5). Delta-фокус v3 (6 новых/изменённых)
+ сквозная целостность 36. Source: deck.yaml + deck-part2.yaml + slides/*.md
сверены с рендером. Эталон divider/Q&A — lec-02 deck.yaml (s04a/s08a/s13a/s17a/
s22a section_divider + s29 qa_minimal).

## Сводка

- Всего слайдов: 36
- **P0 issues (блокеры): 0**
- **P1 issues (важные): 2**
- **P2 issues (косметика): 4**
- 5-секундный тест: **36/36 PASS** (провалов нет; см. ниже)
- 6 новых слайдов: **5 PASS / 1 PASS-with-P1** (s14-сосед — redundancy)
- Divider-консистентность (6 шт): **PASS** — единый визуальный язык
- s30 ретайтл (U-6): **PASS** — контентный тезис, не function-as-title
- s13b §5.5 Schema Readability (pipeline): **PASS**
- s31 Q&A: **PASS** — канон lec-02 qa_minimal воспроизведён точно
- Палитра/motif: PASS — 0 off-palette, gold ≥1× на всех content+divider,
  s31 gold=0 — **canon-consistent (не дефект)**, Ocean motif на всех content
- Forbidden §7 на видимом слое: 0 нарушений
- Resolved с v1: P1-2 (s24 USER-actor) ✅, P1-3 (s15 gold-тезис) ✅,
  P2-3 (s27 7×7→5×5) ✅
- Counter-check: P1 = 2 (< 5) → APPROVE-WITH-POLISH корректно (не REVISE)

---

## Таблица 6 новых слайдов — pass/fail

| Slide | Тип | 5-сек | §5.5 | Divider-консист. | Verdict | PNG-наблюдение |
|---|---|---|---|---|---|---|
| **s04a** | section_divider | PASS | n/a | PASS (= s09/s18) | **PASS** | РАЗДЕЛ 1 teal + gold accent-line + «Промпт и его границы» 38pt + нарративный мост italic + гигантская «1» soft-outline + roadmap gold Раздел 1. Идентичен s09/s18. |
| **s13a** | section_divider | PASS | n/a | PASS | **PASS** | РАЗДЕЛ 3 + «Fine-tune vs промпт vs RAG» + мост «Проблему знания решили через RAG. А если проблема в поведении?» + «3». Roadmap gold Раздел 3. |
| **s13b** | assertion_visual (pipeline) | PASS | **PASS** | n/a | **PASS** | Мини-схема [Предобуч.модель/общие веса] ＋ [Ваш датасет] →(дообучение)→ [Дообученные ВЕСА/модель другая, gold]. Иконки per-node (chip/db/sliders), MSO-стрелка, «+». Контраст-плашки КОНТЕКСТ vs ВЕСА + gold summary. «веса≠контекст» за 5 сек. |
| **s23a** | section_divider (sub) | PASS | n/a | PASS-distinct | **PASS** | Tag «РАЗДЕЛ 4 · БЕЗОПАСНОСТЬ» (отличается суффиксом), гигантская «4» сохранена, roadmap gold Раздел 4. Визуально отличим от секционных, но узнаваемо того же семейства. |
| **s25a** | section_divider | PASS | n/a | PASS | **PASS** | РАЗДЕЛ 5 + «Как выбрать: фреймворк решения» + мост «соберём в один инструмент выбора» + «5». Roadmap gold Раздел 5. |
| **s31** | qa_minimal | PASS | n/a | n/a (canon) | **PASS** | «Вопросы» mega bold deep + «Спасибо за внимание» mid + тихая строка Семинар 3. Белый фон, без footer/roadmap. Точная калька lec-02 s29. gold=0 — canon. |
| s30 (ретайтл) | summary | PASS | n/a | n/a | **PASS** | Title «AI-архитектура — несущая ось отраслевых лекций» (контент, не функция). Мост Модуль 1 + ДЗ Семинар 3 (gold) + gold summary. Q&A-колонка убрана — баланс восстановлен. |

**Итог:** 6/6 новых слайдов проходят 5-сек + divider/canon-консистентность.
1 P1 (s14, не сам новый слайд, а его сосед) — см. ниже.

---

## Divider-консистентность (6 divider-слайдов)

**Вердикт: PASS — единый визуальный язык.**

| Slide | Tag | Subtitle | Bridge | Big № | Roadmap-gold |
|---|---|---|---|---|---|
| s04a | РАЗДЕЛ 1 | Промпт и его границы | ✓ italic | «1» | Раздел 1 |
| s09 | РАЗДЕЛ 2 | RAG: поиск-дополненная генерация | ✓ italic | «2» | Раздел 2 |
| s13a | РАЗДЕЛ 3 | Fine-tune vs промпт vs RAG | ✓ italic | «3» | Раздел 3 |
| s18 | РАЗДЕЛ 4 | API · tools · MCP · агенты + безопасность | ✓ italic | «4» | Раздел 4 |
| s23a | РАЗДЕЛ 4 · БЕЗОПАСНОСТЬ | Кто видит данные в цепочке | ✓ italic | «4» | Раздел 4 |
| s25a | РАЗДЕЛ 5 | Как выбрать: фреймворк решения | ✓ italic | «5» | Раздел 5 |

Все 6 используют идентичный layout: teal eyebrow-tag + gold accent-line под
ним + крупный deep subtitle + italic light нарративный мост слева + гигантская
soft-outline цифра справа + 6-карточный roadmap-bar с gold-активным маркером.
Соответствует канону lec-02 (Раздел N + subtitle + frame-phrase + roadmap).

**s23a (sub-divider) — корректно отличим:** не путается с секционными
divider'ами, потому что (1) tag содержит суффикс «· БЕЗОПАСНОСТЬ»,
(2) гигантская цифра остаётся «4» (не «4a»/«5») — сигнализирует «подблок
внутри Раздела 4, не новый раздел», (3) roadmap-маркер остаётся на Раздел 4.
Это семантически честный приём: тот же визуальный язык, но явный сигнал
«sub-блок». Анти-паттерн «mini-divider между секциями когда section dividers
есть» НЕ нарушен — s23a по brief U-5a, не designer-инициатива.

Gold-присутствие на divider'ах: s04a/s09/s13a/s18/s23a/s25a ≈81–95 gold-px
(roadmap active-card + accent-line) — консистентно, ≥1× удержано.

---

## P1 issues (важные — фиксить до показа желательно)

### P1-1 — s13b ↔ s14: дублирование определения fine-tuning на back-to-back слайдах + противоречие deck.yaml

**Severity:** P1 (cross-slide redundancy, v3-introduced + spec-contradiction)
**Слайды:** s13b (новый, dedicated определение) + s14 (следующий слайд).
**Issue:** v3 добавил s13b именно как dedicated слайд-ОПРЕДЕЛЕНИЕ fine-tuning
(U-2), чтобы закрыть пререквизит-gap «на видимом слое». deck-part2.yaml s14
прямо фиксирует намерение: *«Опирается на определение s13b (inline-define
больше НЕ дублируется здесь — gap закрыт на видимом слое в s13b)»*. Но
slide-md s14 НЕ был обновлён под это решение: на видимом слое s14 по-прежнему
несёт почти идентичную inline-define.
- s13b body (видимый subtitle): *«Fine-tuning (дообучение) — продолжение
  обучения уже готовой модели на ваших данных. В Лекции 1 это был один из
  типов использования; здесь — архитектурный выбор, одна из ступеней
  лестницы.»*
- s14 body (видимый italic subtitle, СЛЕДУЮЩИЙ слайд): *«Fine-tuning
  (дообучение) — дополнительное обучение готовой модели на своих данных, при
  котором меняются её веса. В Лекции 1 — как тип использования; здесь — как
  архитектурный выбор, одна из ступеней лестницы.»*

Это парафразный повтор одного определения на двух подряд идущих слайдах
(анти-паттерн «Identical / paraphrased assertions» + cross-slide redundancy).
Усугубляется тем, что s14 frontmatter всё ещё содержит `learning_goal:
"...+ inline-define дообучения"` и `visual_brief: "Inline-define сверху"`, а
speaker notes s14 (строка «Введём термин, потому что в Лекции 1 он встречался
лишь как один из типов использования...») повторно ВВОДЯТ определение с нуля,
как будто s13b не существует. На лекции студент услышит «что такое
fine-tuning» дважды подряд за ~30 сек.
**Митигирующий фактор:** содержательно слайды разные (s13b = «что это», s14 =
«где сузился»); вред — повтор вводной фразы, не дезориентация. Поэтому P1, не
P0.
**Recommendation:** Привести slide-md s14 в соответствие с deck-part2.yaml
(книга-/спека-first): убрать дублирующую inline-define строку из видимого тела
s14, заменить короткой обратной ссылкой («fine-tuning — определили на
предыдущем слайде: меняет веса, не контекст»), и переписать первый абзац
speaker notes s14 с «введём термин» на «мы определили fine-tuning; теперь —
где он сузился». Обновить s14 frontmatter `learning_goal`/`visual_brief`
(убрать «inline-define»). НЕ трогать s13b (он корректен и является носителем
определения по дизайну v3).
**Visual evidence:** s13b.png (subtitle + мини-схема) и s14.png (italic
subtitle строка 21) — обе несут «Fine-tuning (дообучение) — ... готовой модели
на ... данных ... В Лекции 1 ... тип использования; здесь — архитектурный
выбор, одна из ступеней лестницы». Подтверждено в slides/s13b...md:22 и
slides/s14...md:21 + deck-part2.yaml s14 примечание.

### P1-2 — s04 title-bar = function-as-title («Центральный вопрос лекции»)

**Severity:** P1 (U-6 explicitly requested аудит прочих title на
function-as-title; designer заявил «function-as-title только s30» — неточно)
**Слайд:** s04.
**Issue:** U-6: «НЕ выводить ЦЕЛЬ/функцию слайда в title... Ретайтл s30 + аудит
прочих title на function-as-title». Designer сообщил, что function-as-title
был только s30 и теперь исправлен. Аудит всех 36 title-bar показал: **s04
title-bar = «Центральный вопрос лекции»** — это именно function-naming («что
это за слайд» = навигационная функция), а не контентный тезис. На PNG s04
видно: eyebrow-caps «ЦЕНТРАЛЬНЫЙ ВОПРОС ЛЕКЦИИ» сверху, под ним крупно сам
вопрос «У меня есть задача и доступ к LLM. Какую архитектуру выбрать...».
**Митигирующий фактор:** функционирует как eyebrow/kicker (аналог «ЛЕКЦИЯ 3» на
cover, «РАЗДЕЛ N» на divider — навигационные ярлыки канона), а доминирующий
видимый элемент — сам центральный вопрос (полное предложение-тезис, крупно).
Это пограничный случай: eyebrow-ярлык, не title, замещающий контент. Поэтому
P1 (точечный, не P0), а не множественный.
**Recommendation:** Owner-решение. Опция A (минимально): оставить как
осознанный eyebrow-канон (как cover/divider tag) — тогда задокументировать,
что designer-claim «только s30» уточняется: s04 eyebrow = навигационный ярлык
канона, не нарушение U-6. Опция B: убрать eyebrow «Центральный вопрос лекции»,
оставить только сам вопрос крупно (он самодостаточен как контент). НЕ
применять без user-решения (U-6 — owner-feedback пункт).
**Visual evidence:** s04.png — верхний small-caps «ЦЕНТРАЛЬНЫЙ ВОПРОС ЛЕКЦИИ»;
slides/s04...md «## Title bar → Центральный вопрос лекции».

---

## P2 issues (косметика — show-able as-is)

### P2-1 — Trailing-period в title-bar (deck-wide стилевая мелочь)
s01 «...платит компания.», s13b «Что такое fine-tuning.», s30 «...отраслевых
лекций.», s06 «...(пошаговое рассуждение).», s16 «Провал: catastrophic
forgetting.» и др. — у части title-bar точка в конце. Title-ярлыки обычно без
терминальной точки (eyebrow/topic-конвенция). Не мешает чтению; косметика
консистентности. Fix (опц.): снять терминальную точку с title-bar (оставить в
assertion-плашках, где это предложение).

### P2-2 — s14 frontmatter рассинхрон со spec (метаданные)
Связано с P1-1: даже после фикса видимого тела s14, frontmatter
`learning_goal`/`visual_brief` всё ещё описывают «inline-define сверху». Это
метаданные (не визуальный дефект), но создают drift между deck-part2.yaml
(«не дублируется») и slide-md. Fix вместе с P1-1.

### P2-3 — Вертикальный whitespace в боксах (s13-right, s23-card3, s04-right)
Перенесено из v1 P2-4 (не было fix-итерации; PA-2 в v1 рекомендовал
mass-rebalance). ~25-30% пустоты в Ocean-боксах (s13 «Air Canada revisited»
между диагнозом и альтернативой; s23 card3; s04 правая rule-панель). Не мешает
чтению. Fix: подтянуть высоты/интерлиньяж в одной visual-итерации.

### P2-4 — s13b title-period + assertion vs title-bar
s13b title-bar «Что такое fine-tuning» — topic-label (консистентно с
deck-wide паттерном title=topic / gold-плашка=assertion, документированным как
defensible variant в v1 P1-1). Сам assertion («Fine-tuning меняет САМИ ВЕСА...
отличается от промпта и RAG») виден через нижнюю контраст+gold-плашку. Не
новый дефект — тот же deck-паттерн. Фиксирую как verify-only (часть owner-
решения по deck-wide title-паттерну, см. v1 P1-1, не переоткрываю).

---

## Cross-deck issues

- **Палитра:** PASS. Ocean (#21295C/#065A82/#1C7293) + Teal #028090 + Gold
  #F0AB00. 0 off-palette на 36. Без красного/generic-blue/dark-bg
  (cover/divider — light-tinted by design).
- **Gold ≥1×:** PASS на всех content + 6 divider (≈81–95px через roadmap
  active-card + accent-line). s13b ≈81 (ВЕСА-узел + summary). s30 ≈521.
  **s31 gold=0 — canon-consistent (НЕ дефект):** точная калька lec-02 s29
  qa_minimal (белый фон, без footer/roadmap, «визуальная тишина для открытого
  Q&A»). PA-3 designer'а здесь корректен — см. вердикт ниже.
- **Ocean rounded box motif:** PASS на всех content. cover s02 + 6 divider +
  s31 Q&A — exempt by design (divider/cover/qa имеют distinct-типографику;
  divider'ы несут gold через roadmap).
- **Шрифты:** consistent (Inter heading). Иерархия: assertion/subtitle/body/
  caption. Без mix-семейств. Divider'ы единая типографика.
- **Forbidden §7 на видимом слое:** 0 нарушений. Grep + визуально: нет
  «Лектору»/«Вы здесь»/тайминга-минут/CVE-номеров на видимом слое (s25 PNG —
  «GitHub MCP heist, tool poisoning — кратко, без CVE»; CVE только в
  visual_brief/notes-ссылке «в главе/notes»)/vendor-pricing/формул/кода>3/
  локального ИУ6-binding. roadmap-bar — explicitly allowed.
- **Designer-added extras:** не обнаружено. 0 «Лектору»/«Вы здесь»/activity-
  prompts/тайминг/subtitle-без-brief. 6 новых слайдов — строго по U-1…U-7
  brief, не designer-инициатива. Слайд-count 36 = deck.yaml totals (0
  не-запрошенных add/delete). s23a sub-divider — по U-5a (не самовольный
  mini-divider).
- **Cross-slide redundancy:** 1 найдена (P1-1, s13b↔s14 определение). Air
  Canada s01→s13 — намеренный callback (deck.yaml + GATE0), НЕ дубль (разные
  фрейминги). 6 новых divider'ов НЕ плодят шум — каждый несёт уникальный
  нарративный мост, не повторяют контент. Charts: s07 bar / s08 curve / s16
  diverge / s29 donut — все разные, нет дубля.
- **Speaker notes:** PASS. 6 новых слайдов 203–263 слов связного
  студенческого текста, без layout-описаний/«Лектору». s04a — корректный
  нарративный мост. s31 — facilitation-направления вопросов (не «backup-
  провокации» в смысле lec-02 канона — это hooks для открытия диалога,
  допустимо).
- **Curriculum relevance:** PASS. Каждый слайд → LO7 (часть +LO4), chapter_ref
  присутствует, нет «висящих» концептов. introductory-уровень удержан
  (лестница/матрица/чек-лист = applied tools). 6 новых: divider'ы/определение/
  Q&A — структурные, привязаны к §-главы. s13b закрывает реальный
  пререквизит-gap (fine-tuning) — curriculum-relevant.
- **Нарратив (U-8):** PASS. Нарративные мосты на всех 6 divider'ах читаются и
  связывают разделы («Лестницу увидели — теперь снизу» s04a; «Проблему знания
  решили через RAG — а если в поведении?» s13a; «Разобрали надёжен ли агент —
  кто видит данные?» s23a; «Разобрали все архитектуры — соберём в инструмент»
  s25a). Точки возврата ЦВ: s04→разделы→s26→s30. Reveal-пары: s01↔s13 (Air
  Canada), s07↔s21↔s29 (человек-валидатор/не self-rationale) — парные,
  подписаны.
- **Resolved с v1:** P1-2 (s24 — теперь explicit USER/gold-person-иконка +
  per-node иконки в data-flow цепочке) ✅; P1-3 (s15 — теперь сильная gold-
  тезис-плашка «PEFT почти всегда лучше... full FT в 2026 почти никогда»)
  ✅; P2-3 (s27 — 7×7 → читаемая 5×5 с семантическим цветом, нет крипто-
  аббревиатур) ✅.

---

## Вердикт по 2 PROPOSED ADDITIONS дизайнера

### PA-3 — s31 без gold = canon lec-02 qa_minimal

**Вердикт: ПРИНЯТЬ (canon-consistent, НЕ дефект).**
Подтверждено: lec-02 deck.yaml s29 qa_minimal — «без footer, без roadmap-bar
— фокус на диалоге», 0 gold by design. s31 точно воспроизводит этот канон
(«Вопросы» mega deep + «Спасибо за внимание» + тихая строка, белый фон,
gold=0). Это намеренная «визуальная тишина» закрывающего Q&A, а не нарушение
правила «gold ≥1×/content» (qa_minimal — не content-тип, exempt как
cover/divider по канону). PA-3 — правильное designer-наблюдение, фиксируем как
canon-consistent. НЕ требовать gold на s31.

### PA-4 — s09/s18 bridge консистентность с новыми divider под U-8

**Вердикт: ПРИНЯТЬ (уже реализовано, консистентно).**
Проверено визуально: s09 (frame «Извлечь релевантное → положить в контекст →
ответить с опорой») и s18 (frame «От собеседника в окне чата — к компоненту
продакшен-системы») несут нарративную строку в том же стиле, что новые
s04a/s13a/s23a/s25a (italic light, нарративный мост). Все 6 divider'ов теперь
консистентны по нарративному мосту под U-8 — единый storytelling-проход. PA-4
уже выполнено; дополнительных правок не требуется. Подтверждаю консистентность.

---

## 5-секундный тест — результаты

36/36 PASS. Провалов нет. Механизм: на каждом content-слайде gold-плашка/
sub-headline несёт тезис; на divider'ах — крупный subtitle + нарративный мост;
s13b — gold «ВЕСА» + summary-плашка «Промпт/RAG = что показать; FT = изменить
модель» (за 5 сек: веса≠контекст); s31 — «Вопросы» крупно (мгновенно). s04 —
сам центральный вопрос крупно (eyebrow не мешает 5-сек). s27 5×5 — gold нижняя
плашка несёт message, projector-legible @ 50%.

**Projector Readability (50% zoom):** PASS. Divider'ы — крупная типографика,
читаемы. s13b мини-схема — node-заголовки bold ≥16pt, caption italic ~12pt
читаемы @ 50%. s27 5×5 — header/row-labels/gold-плашка читаемы (улучшено с
v1 7×7). Watch-item v1 (s27) разрешён уменьшением до 5×5.

---

## Топ-5 правок (рекомендация оркестратору)

1. **P1-1 (s13b↔s14 redundancy)** — привести slide-md s14 в соответствие с
   deck-part2.yaml: убрать дублирующую inline-define из видимого тела s14
   (заменить обратной ссылкой на s13b), переписать 1-й абзац speaker notes
   s14, обновить frontmatter (P2-2 заодно). Главное: спека прямо требует
   «не дублируется».
2. **P1-2 (s04 function-as-title)** — owner-решение: принять eyebrow
   «Центральный вопрос лекции» как навигационный канон (документировать
   уточнение designer-claim) ИЛИ убрать eyebrow. U-6 owner-пункт.
3. **P2-3 (whitespace s13/s23/s04)** — mass-rebalance в одной visual-итерации
   (перенос v1 PA-2, не выполнялось).
4. **P2-1 (trailing-period в title-bar)** — снять терминальную точку с title-
   bar deck-wide (косметика консистентности).
5. **Verify-only:** PA-3 (s31 gold=0) и PA-4 (s09/s18 bridge) подтверждены
   canon-consistent — НЕ править. Resolved v1 P1-2/P1-3/P2-3 — подтверждены
   исправленными.

**Итог:** Deck **show-able** с known caveats. 0 P0, 2 P1, 4 P2 →
APPROVE-WITH-POLISH. 6 новых слайдов методически и визуально интегрированы
корректно; divider-система консистентна; s30 ретайтл и s31 Q&A соответствуют
brief/канону. Единственный содержательный блокер качества — s13b↔s14
дублирование определения (P1-1, противоречит собственной spec v3) +
s04-eyebrow (P1-2, owner-call по U-6). Counter-check: 2 P1 (<5) →
APPROVE-WITH-POLISH, не REVISE.
