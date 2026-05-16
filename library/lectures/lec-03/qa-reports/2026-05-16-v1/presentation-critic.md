VERDICT: APPROVE-WITH-POLISH

# Presentation Critic Report — Лекция 3 «Архитектуры AI-систем» — 2026-05-16

Issue #87 · branch `issue-87-lec-03-architectures` · Phase 7 (build-deck Phase 4).
Vision-enabled review: все 30 PNG-снапшотов прочитаны через Claude vision +
целевые кропы (s07/s08/s16 charts, s13/s23/s24 dense, s27 @ 50% projector test).

## Сводка

- Всего слайдов: 30
- **P0 issues (блокеры): 0**
- **P1 issues (важные): 3**
- **P2 issues (косметика): 6**
- 5-секундный тест: **30/30 PASS** (список провалов — пустой; см. ниже)
- Schema-слайды: 8/8 PASS с 1 P1-оговоркой (s24 — USER-actor gap)
- Палитра/motif: PASS — 0 off-palette, gold ≥1× на всех 30 (sampled-проверка),
  Ocean rounded box на всех content-слайдах
- Forbidden §7 на видимом слое: 0 нарушений
- Cross-slide redundancy: 0 (Air Canada s01→s13 — намеренный callback, не дубль)
- Counter-check: P1 = 3 (< 5) → APPROVE-WITH-POLISH корректно (не REVISE)

---

## 5-секундный тест — результаты

Прошёл по каждому слайду: «понятен ли main message за 5 сек с 5-го ряда?».

**Провалившие: НЕТ.** Все 30 — main message считывается. Механизм, который
это обеспечивает: на каждом content-слайде есть **gold-плашка/sub-headline,
несущая тезис** (например s06 «28 → верно», s10 gold-инвариант, s13 «вернул
что-то ≠ вернул правильное», s17 gold-вывод, s26 gold-правило, s27 gold нижняя
плашка «детерминированное → код без ИИ»). Тезис присутствует на слайде даже
там, где title bar — короткий topic-label (см. cross-deck P1-1).

s27 (7×7 матрица — watch-item): 5-сек тест **PASS условно** — главный message
несёт gold нижняя плашка (projector-legible @ 50%), а сама матрица — справочная
таблица, по которой ведёт лектор (assertion прямо говорит «матрица — структура
для аргумента, не сумма баллов»). Cell-аббревиатуры — P2 (см. ниже).

---

## Schema Readability — таблица 8 schema-слайдов

| Slide | Subtype | Verdict | Заметки (что видно на PNG) |
|---|---|---|---|
| s10 | schema_pipeline | **PASS** | 3 stage, корректные RIGHT_ARROW (не hybrid), иконки database/route/check-check, gold-инвариант снизу. Unified RU sub-labels. |
| s12 | schema_matrix¹ | **PASS** | Фактически 3 criteria-колонки (не N×M); fill 100%, gold на «скрытая бомба». Иконки per-колонка. Subtype-mismatch — см. P2-1. |
| s17 | schema_matrix | **PASS** | Настоящая таблица 4×3, fill ~100%, single-line headers, Ocean-box wrapper (добавлен iter4), gold нижняя строка + плашка. |
| s21 | schema_cycle | **PASS** | Explicit «СТАРТ» badge на Plan + explicit return-arrow «цикл ПОВТОРЯЕТСЯ → возврат к Plan». 4 элемента. Failure-mode sub-labels мелкие — P2-2. |
| s22 | schema_matrix¹ | **PASS** | Фактически 2-колонночное сравнение Workflow/Агент (не N×M); параллельная структура, gold-плашка. Subtype-mismatch — см. P2-1. |
| s24 | schema_architecture | **PASS-with-P1** | Чистая цепочка, корректные MSO-стрелки, контраст белый-на-teal отличный. **НО: нет explicit USER/human actor + нет per-node иконок** (anti-pattern #15/#24). См. **P1-2**. |
| s26 | schema_layered | **PASS** | Bottom-aligned (был P0 broken iter1 → redone iter2), 6 ступеней, trigger per-переход, gold нижняя ступень + gold rule-panel. |
| s27 | schema_matrix | **PASS-with-P2** | 7×7 full-fill, single-line headers, семантический цвет (gold=сильная/teal=слабая), gold нижняя плашка projector-legible @ 50%. Cell-аббревиатуры криптичны — **P2-3**. |

¹ s12/s22 помечены `subtype: schema_matrix` в deck.yaml, но визуально это
criteria-columns / 2-col comparison, а не 2D N×M матрица. Matrix fill-rate
checklist строго не применим; читаемость как comparison — PASS. Несоответствие
subtype — P2-1 (метаданные, не визуальный дефект).

**Projector Readability (50% zoom):** s27 — единственный watch-item. Header-row
+ row-labels + gold нижняя плашка читаемы @ 50%. Cell-аббревиатуры на грани
(P2-3). Все остальные schema — PASS @ 50%.

---

## P1 issues (важные — мешают, фиксить до показа желательно)

### P1-1 — Cross-deck: title bar = topic-label, не assertion (anti-pattern #2 / blind-spot #10)

**Severity:** P1 (один cross-deck issue, не 15 отдельных)
**Слайды:** s06, s10, s13, s15, s16, s17, s19, s20, s23, s25, s27, s28, s29, s30
(сильные assertion-заголовки только у s01, s05, s14).
**Issue:** Title bar многих content-слайдов — короткий topic-label
(«Chain-of-thought (пошаговое рассуждение)», «Провалы агентов», «Матрица
выбора», «Критерии: что куда»), а не полное предложение-тезис. Pipeline §1.4 +
anti-pattern #2: «Заголовок слайда = тезис (полное предложение)». В deck.yaml
для всех этих слайдов есть сильный `assertion`, но на видимый title bar он не
вынесен.
**Митигирующий фактор (почему P1, а не P0/множественный):** на каждом таком
слайде тезис ПРИСУТСТВУЕТ и виден как prominent gold-плашка/sub-headline
(подтверждено визуально: s06 «28→верно», s13 «вернул что-то ≠ правильное»,
s16 критерий-плашка, s17 gold-вывод, s23 «$4 200 за 63 часа», s26 gold-правило,
s27 gold-плашка). Assertion-evidence принцип удовлетворён на уровне слайда
через gold-плашку, а не через title bar. Это защитимый альтернативный паттерн
(title-bar = topic-якорь; gold-плашка = assertion), консистентный по всему deck.
**Recommendation:** Решение оркестратора/владельца — это паттерн уровня deck,
не per-slide баг. Опция A (минимально): принять паттерн как осознанный выбор
(title bar = topic-навигация, gold-плашка = тезис) — задокументировать в
decisions.md как defensible variant. Опция B (усиление): для 4-6 ключевых
слайдов (s13, s16, s23, s27 — failure/judgment-несущие) переписать title bar в
assertion-форму, оставив gold-плашку. НЕ применять без user-решения (No Extra
Content Rule / Glossary-cascade).
**Visual evidence:** title bars извлечены grep'ом; gold-плашки подтверждены на
всех 30 PNG.

### P1-2 — s24 — schema_architecture без explicit USER-actor и без per-node иконок

**Severity:** P1
**Issue:** s24 помечен `subtype: schema_architecture`. Per §4 + anti-pattern
#15/#24, architecture-схема обязана иметь **explicit USER/human actor** (студент
должен видеть «где Я в этой схеме?») и желательно per-node иконографику. На PNG:
горизонтальная цепочка «ваши данные → агент → инструмент → внешний API →
провайдер → подрядчики» — 6 одинаковых teal-боксов, **без человека/USER-иконки,
без иконок узлов**. Это designer-self-acceptance fail: геометрия чистая
(стрелки корректные MSO, контраст отличный — iteration-log заявил PASS), но
concept-anchor (актёр) отсутствует.
**Митигирующий фактор:** это data-flow карта (поток данных через границы
доверия), а не actor-interaction архитектура; «ваши данные» имплицитно якорит
пользователя; assertion — про retention-границы, не про взаимодействие актёров.
**Recommendation:** Опция A — добавить маленькую person/user-иконку у «ваши
данные» + минимальные иконки узлов (агент/инструмент/API/провайдер). Опция B —
переклассифицировать `subtype` в `schema_pipeline` (data-flow), тогда
USER-actor правило не применяется и slide проходит чисто. Опция B проще и
честнее семантически (это конвейер данных, не архитектура акторов).
**Visual evidence:** /tmp-кроп s24 chain — 6 uniform teal боксов, MSO-стрелки
OK, нет человека/иконок.

### P1-3 — s06 / s15 — assertion-несущая gold-плашка отсутствует или слабее, чем у соседних слайдов

**Severity:** P1
**Issue:** На большинстве content-слайдов gold-плашка несёт тезис и
компенсирует topic-label title (см. P1-1). На **s06** gold — только на числе
«28» (итог примера), полноценной тезис-плашки «CoT — инструмент под класс
задач, не глобальный тумблер» на видимом слое нет (есть узкая плашка «когда
CoT НЕ нужен» — но она про границу, не про сам тезис). На **s15** title
«PEFT вместо full fine-tuning» — topic; gold на «Риск catastrophic forgetting»
(причина №3), но сам тезис «PEFT почти всегда лучше: дешевле, модульнее,
↓forgetting» как единая prominent-плашка не выделен. Для этих 2 слайдов
P1-1-митигация (тезис виден через gold-плашку) работает слабее.
**Recommendation:** s06 — добавить/усилить тезис-строку или сделать title bar
assertion-формой. s15 — gold-выделить связку «3 причины → PEFT почти всегда
лучше» как единый вывод. Согласовать с решением по P1-1 (один паттерн на deck).
**Visual evidence:** s06.png — gold только на «28»; s15.png — gold на reason-3,
тезис рассыпан по 3 пунктам без сводки.

---

## P2 issues (косметика — show-able as-is, polish-кандидаты)

### P2-1 — s12 / s22 subtype-mismatch в deck.yaml
`subtype: schema_matrix` у s12 (3 criteria-колонки) и s22 (2-col comparison) —
визуально это не N×M матрица. Не влияет на читаемость (оба PASS как
comparison). Fix: поправить subtype на `comparison` в deck.yaml — метаданные,
для корректного применения checklist в будущем.

### P2-2 — s21 failure-mode sub-labels мелкие
Под каждым шагом цикла (plan/act/check/iterate) — режим отказа очень мелким
шрифтом (~10-11pt). На 50% zoom — на грани. Концепт цикла читается отлично;
sub-labels — деталь для лектора. Fix: +1-2pt или сократить формулировки.

### P2-3 — s27 cell-аббревиатуры криптичны
«детерм.», «ср-выс.», «*много», «выс.выс.», стрелочные глифы — без легенды
back-rows не расшифруют @ 50%. Главный message несёт gold нижняя плашка
(PASS). Fix: компактная легенда аббревиатур ИЛИ чуть длиннее cell-слова. Не
блокер — лектор проводит по матрице, assertion прямо снимает «не сумма баллов».

### P2-4 — Вертикальный whitespace внутри боксов (s13-right, s23-card3, s04-right)
~25-30% пустоты внутри Ocean-боксов между блоками текста (s13 «Air Canada
revisited» — большой gap между диагнозом и альтернативой; s23 card3; s04
правая rule-панель). Visual-mass дисбаланс. Не мешает чтению. Fix: подтянуть
высоты боксов или увеличить интерлиньяж/шрифт под доступное место (anti-pattern
#28 equal-height — частично).

### P2-5 — s30 Q&A-блок визуально пустой
Закрывающий «Q&A / Спасибо за внимание» — plain teal-бокс без визуальной
нагрузки. Для closing summary допустимо, но единственный слайд, близкий к
«text+box». Fix (опц.): минимальная иконка/мотив. Низкий приоритет (финальный
слайд, контент исчерпан).

### P2-6 — Cover/divider gold accent-line (s02/s09/s18) — verify-only
Под «ЛЕКЦИЯ 3»/«РАЗДЕЛ N» — короткая accent-line (teal на s02, gold на
s09/s18). Anti-pattern #1 (accent-lines под titles) — но он специфичен для
**content-слайдов**; cover/divider имеют distinct-типографику по design
(iteration-log iter4 подтвердил exempt). Это consistent divider-motif, не
content-title accent-line. **НЕ дефект**, фиксирую как verify-only: если
владелец хочет 0 accent-lines абсолютно — убрать; иначе оставить как
divider-motif. Решение — владельца, не моё.

---

## Cross-deck issues

- **Палитра:** PASS. Ocean (#21295C/#065A82/#1C7293) + Teal #028090 + Gold
  #F0AB00. 0 off-palette на 30 слайдах (визуально + sampled-проверка). Без
  красного, без generic blue, без dark backgrounds (cover/divider — light
  tinted by design).
- **Gold ≥1×/слайд:** PASS на всех 30 (sampled gold-px: min 166 на cover s02,
  min 236 на divider s09/s18 — через roadmap active-card + accent; content
  496-3095). Ни одного NO-GOLD.
- **Ocean rounded box motif:** PASS на всех content-слайдах (cover s02 +
  dividers s09/s18 exempt by design — имеют gold через roadmap-bar).
- **Шрифты:** consistent (Inter heading). Иерархия читается: assertion 28pt /
  sub 20pt / body 16pt / caption 12pt. Без mix-семейств.
- **Forbidden §7 на видимом слое:** 0 нарушений. Grep + визуально: нет
  «Лектору»/«Вы здесь»/тайминга-минут/CVE-номеров/vendor-pricing/формул
  трансформера/кода >3 строк/незапрошенных subtitle/локального ИУ6-binding.
  s23 «$4 200 за 63 часа» — это документированный failure-case anchor
  (deck.yaml s23 + decisions.md GATE 0), НЕ vendor-pricing → разрешено.
  s25/s24/s07 footers явно отсылают CVE/pricing/freshness в главу/notes —
  корректно.
- **Cross-slide redundancy:** 0. Air Canada на видимом слое только s01 (hook)
  + s13 (revisited as grounding) — намеренный narrative-callback (разные
  фрейминги: s01 = неправильный выбор архитектуры; s13 = механизм отказа
  grounding), planned в deck.yaml + GATE 0. НЕ дубль. Никаких повторяющихся
  charts/диаграмм/assertion между слайдами.
- **Designer-added extras:** не обнаружено. Нет добавленных subtitle/маркеров/
  тайминга/«Лектору»-секций сверх brief. roadmap-bar на s02 — explicitly
  allowed (§7 «кроме roadmap s02»). Слайд-count = 30 (LOCKED, совпадает с
  deck.yaml — 0 удалений/добавлений).
- **Curriculum relevance:** PASS. Каждый слайд привязан к LO7 (часть к LO7+LO4),
  chapter_ref присутствует, нет «висящих в воздухе» концептов. introductory-
  уровень: лестница/матрица/чек-лист — applied tools, не advanced theory.
  Терминология вводится постепенно, inline-define присутствует (ZDR на s24,
  CoT на s06, faithfulness на s07 — verified в md).
- **Нарратив:** PASS. Переходы читаются (s01 hook → s04 лестница-карта →
  разделы → s26 лестница payoff → s30 мост). Reveal-пары: s01↔s13 (Air Canada
  hook→revisited), s07↔s21↔s29 (callback «человек-валидатор, не self-rationale»)
  — все парные и подписаны.

---

## Вердикт по 2 PROPOSED ADDITIONS дизайнера

Примечание: предложения не задокументированы в repo (slides/iteration-log) —
оценка по визуальному состоянию слайдов и curriculum relevance.

### PA-1 — s04 / s26 «climb-scale label» (метка направления подъёма по лестнице)

**Вердикт: ПРИНЯТЬ (curriculum-relevant, не designer-extra).**
Обоснование: лестница (s04 карта, s26 payoff) — несущий концепт LO7 «когда
правильный ответ не ИИ + правило подниматься только под требование». На
текущих PNG направление читается (gold нижняя ступень + стрелка/«выше» на s04
после iter2-фикса; s26 bottom-aligned). Явная метка шкалы «сложность/риск ↑»
у оси лестницы **усиливает central assertion** и снимает риск, что студент
прочтёт лестницу как «чем выше, тем лучше» (прямо противоположно тезису). Это
не decorative extra — это disambiguation несущего концепта, привязанного к LO7
и к gold-правилу «каждый подъём — обмен, не улучшение». Рекомендую реализовать
как короткую вертикальную ось-метку (≤3 слов, Ocean, ≥12pt), без новых
сущностей. Согласуется с No Extra Content Rule (disambiguation существующего
концепта, не новый контент) — но финальное «да» за владельцем (он явно сделал
это приёмочным критерием? — нет; это designer-proposal → REPORT, орк/владелец
решает).

### PA-2 — s13 «mass-rebalance» (перебалансировка визуальной массы)

**Вердикт: ПРИНЯТЬ как P2-fix (не новый контент — чистая визуальная правка).**
Обоснование: подтверждено визуально (кроп s13-right) — ~30% вертикального
whitespace внутри «Air Canada revisited» бокса между диагнозом и
альтернативой; левые 3 кейса плотнее. Это ровно P2-4. Mass-rebalance =
подтянуть высоты/интерлиньяж, перераспределить пустоту — НЕ добавление
контента, НЕ designer-extra (No Extra Content Rule не нарушается: это visual
loop polish, прямо предусмотренный pipeline §5). Рекомендую выполнить в
fix-итерации вместе с P2-4. Низкий риск, чистое улучшение читаемости.

**Итог по PA:** обе addition'ы — НЕ designer-extras в смысле anti-pattern #19
(одна — disambiguation несущего LO7-концепта, другая — pure visual polish).
Обе рекомендованы к реализации; PA-1 требует owner-подтверждения (designer-
proposed, не в brief), PA-2 — рутинный P2 visual-loop fix.

---

## Рекомендация оркестратору

Deck **show-able** с known caveats. 0 P0, 3 P1, 6 P2 → APPROVE-WITH-POLISH.

**Минимальный fix-набор перед показом (рекомендуемый, не блокирующий):**
1. P1-2 (s24): переклассифицировать subtype → `schema_pipeline` в deck.yaml
   (опция B — простейшая, семантически честная) ИЛИ добавить user-иконку.
2. P1-1 + P1-3: owner-решение по паттерну title-bar/gold-плашка. Если
   усиливать — переписать title bars s13/s16/s23/s27 + усилить gold-тезис
   s06/s15. Если принять паттерн — задокументировать в decisions.md.
3. P2-4 + PA-2 (s13/s23/s04 whitespace): mass-rebalance в одной visual-итерации.

**Можно показывать без P2-исправлений** — все P2 косметические, не мешают
обучению. P1-1 — это методический паттерн уровня deck, требует owner-решения,
а не slide-фикса.
