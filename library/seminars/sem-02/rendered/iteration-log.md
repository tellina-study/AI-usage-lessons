# Iteration log — Семинар 2 «Классифицируй и не ошибись»

Прямая сборка через python-pptx (не PowerPoint MCP), как в Семинаре 1 —
причина та же: `notes/mcp-limitations.md` [#54-1/#54-2/#54-3] (нет
`list_shapes`, баг `format_runs`, нет `update_shape_position`). Полная
пересборка presentation с нуля на каждой итерации через `build_sem02.py`.

Toolchain: `/tmp/claude-999/render-env.sh` (bootstrapped LibreOffice +
pdftoppm + rsvg-convert), `/tmp/claude-999/pptx_to_png.sh` для
convert+snapshot.

## Pre-render inventory

26 слайдов, 76 минут (сумма `duration_min` по всем `slides/*.md` == 76.0,
проверено программно). Разделы facilitator-guide.md 1–7 покрыты полностью:
recap (s01-s02), калибровка 6 инструментов (s03-s06), 4 сценария ядра
(s07-s12), «найди подделку» 3 раунда (s13-s17), 4 виньетки провалов
(s18-s23), мостик к Лекции 2 (s24), памятка на вынос (s25), hero closing
(s26).

## Iteration 1 — first full build

**Prep:** скачал 46 Lucide SVG иконок, реколорнул через `sed` (6 цветов ×
3 размера = 828 PNG), скачал 2 реальных hero-фото с Wikimedia Commons
(6-tier acquisition, Tier 2 — Wikimedia напрямую):
- s01 hero: «Intersection over Union — object detection bounding boxes»
  (Adrian Rosebrock, CC BY-SA 4.0) — реальное фото дорожного знака STOP с
  ground-truth и predicted bounding box, прямая перекличка с YOLO-демо
  Лекции 1.
- s26 hero (closing): «NVIDIA GPU» (Mickael Courtiade, CC BY 2.0) —
  реальное фото графического процессора, мостик к теме «внутри модели» на
  Лекции 2 (токены/эмбеддинги/внимание считаются именно на таком железе).

Собрал `build_sem02.py` (helpers адаптированы из sem-01: `ocean_box`,
`chip`, `icon`, `gold_callout`, `text_box`, `multipara_box`, `add_image`,
`code_card`), написал 26 slide-builder функций, сгенерировал PPTX, сконвертировал
в PDF + 26 PNG snapshots.

**Found on inspection (visual sweep всех 26 слайдов):**

### P1 — иконки `smile` и `compass` рендерились с закрашенным кругом вместо контура

**Root cause:** `sed`-паттерн для реколора SVG заменял ЛЮБОЙ `fill="..."`,
включая `fill="none"` на корневом `<svg>` элементе Lucide-иконок. Иконки со
внешним `<circle>` (smile — лицо, compass — внешний круг компаса)
получали закрашенный круг вместо outline-стиля, потому что `fill="none"`
превращался в `fill="#065A82"`.

**Fix:** переписал sed-паттерн — реколорю только `stroke="..."` и
`currentColor` токены, НЕ трогаю `fill="..."` вообще (Lucide-иконки всегда
используют `fill="none"` на root + опционально `fill="currentColor"` на
залитых деталях, которые тоже не должны трогаться). Перегенерировал все
828 PNG.

**Verification:** s02 (`compass` в чек-лист карточке), s18/s19/s20/s22/s23
(`smile` в sycophancy карточках) — все иконки теперь корректный outline.

### P1 — переполнение текста на s16 (раунд 3 «найди подделку», stacked layout)

**Root cause:** `fake_round_slide()` layout=`"stacked"` неверно считал
высоту строк (`rh = (ch * 2 + gap - 0.2) / 2` при `ch=3.35` давал слишком
высокие карточки) и `text_box` для label и body перекрывались из-за
неправильного anchor. Reveal-панель (самое длинное объяснение из 3
раундов — про спорность буквы «B» в B-дереве) переполняла границы слайда.

**Fix:** полностью переписал geometry `fake_round_slide()` — фиксированная
`rh=1.42"` на карточку варианта, `row_gap=0.16"`, единообразный расчёт
`reveal_y`/`reveal_h` через `block_bottom`, уменьшил font size в reveal-панели
(11pt→10pt для explanation, учитывая раунд 3 — самый длинный текст).

**Verification:** s16 PNG — обе карточки варианта читаемы, reveal-панель
умещается в границы слайда без overflow, label и body текст не
пересекаются.

### P2 — избыточный пустой отступ (visual mass imbalance) на нескольких слайдах

Затронуты: s08 (сценарий 1, `left_text_right_quad` layout — фиксированная
высота карточки 4.9" при коротком тексте сценария), s19/s20/s21 (виньетки
1/2/3, `wide_story_bottom_answer` и `left_answer_right_story` layouts —
story text top-anchored в слишком высокой карточке), s23 (закрывающая
рефлексия — 3 плитки занимали только верхние ~55% высоты слайда).

**Fix:** уменьшил фиксированные высоты карточек под реальный объём текста,
переключил story-текст на `MSO_ANCHOR.MIDDLE` вместо TOP, увеличил размер
плиток на s23 + добавил gold discussion-prompt панель снизу, заполняющую
оставшееся пространство содержательно (не просто padding).

**Verification:** squint-test на всех 5 затронутых слайдах — визуальная
масса теперь распределена равномерно по вертикали, нет «отрезанного»
контента наверху с пустым низом.

### P2 — англицизмы вне brand allowlist в visible body

`cold-call` (s07, шаг-плитка методики), `Human-in-the-loop review` (s12,
список действий при сбое), `rule-based` (s07/s12, callout-текст),
`Coding-agent` с латинской капитализацией (s11, title).

**Fix:** `cold-call` → «вызов» (плитка-заголовок), `Human-in-the-loop
review` → «Проверка человеком», `rule-based правила` → «готовые правила»,
`Coding-agent` → `Coding-агент` (матчит написание facilitator-guide.md
«coding-агенту» — гибридный термин с русским окончанием, не чистый
англицизм). Обновил соответствующие `.md` файлы (`## Visual` описания) и
`deck.yaml` для cross-artifact consistency.

**Residual (documented, judged acceptable):** `Coding-` внутри
«Coding-агент» — 2 occurrences — совпадает с canonical usage в
facilitator-guide.md («задачу coding-агенту»), гибридный
loanword-with-Russian-inflection, не чистый separate word. TCP/UDP/RFC/
QUIC/HTTP (раунды 2 «найди подделку» — протокольные акронимы, integral к
фактическому содержанию, не переводимы). Bayer/McCreight/Boeing/CWI/
Centrum Wiskunde Informatica/Adrian Rosebrock/Scientific Research Labs —
имена собственные. Bias/Sycophancy/Distribution shift — установленные
термины курса, glossed на первом появлении («Bias (смещение)»,
«Sycophancy (подстройка)», «Distribution shift (сдвиг распределения)»),
далее используются bare (тот же паттерн, что Лекция 1 s25).

## Iteration 2 — re-render + re-inspect

Пересобрал после icon regen + stacked layout fix + Russification round 1.
Проверил s02 (compass fix confirmed), s08 (gap fix confirmed), s16 (overlap
fix confirmed), s18/s19/s20/s21/s23 (smile icon fix confirmed, English
labels partially glossed).

**Found:** whitespace issue на s19/s20/s21 (`wide_story_bottom_answer` +
`left_answer_right_story`) всё ещё присутствовал — исходный fix зацепил
только s20 (`left_answer_right_story`), но не `wide_story_bottom_answer`
вариант (s19, s21).

## Iteration 3 — targeted layout fix

Применил тот же MIDDLE-anchor + reduced-height подход к
`wide_story_bottom_answer`. Пересобрал.

**Verification:** s19/s20/s21 — все 3 карточки теперь вертикально
центрированы, без dead space.

## Iteration 4 — anglicism cleanup + final verification sweep

Применил Russification fixes (cold-call/rule-based/Human-in-the-loop/
Coding-agent). Пересобрал. Прогнал полный набор автоматических проверок
(см. ниже). Финальный визуальный проход по s07, s11, s12 (подтверждение
fix) + projector-readability check (50% zoom simulation) на выборке
слайдов.

## Автоматические проверки — финальный результат

```
$ python3 -c "sum duration_min across slides/*.md"
76.0   # == deck.yaml duration_min, == facilitator-guide.md итоговая таблица

$ grep -nE "\[TODO|\[VERIFY|\[FACT-CHECK|LO[1-9]|§[0-9]+\.[0-9]+|→ s[0-9]+|см\. s[0-9]+|якорь:|Лектору:|Преподавателю:|Вы здесь" \
    /tmp/pptx-visible.txt /tmp/pptx-notes.txt
(no matches, exit 1)   # 0 scaffold-leaks в visible body + speaker notes

$ grep -nE "[0-9]+\s*мин(ут)?\b|Время раздел|Тайминг|Длительность|⏱|⏰" /tmp/pptx-visible.txt
(no matches, exit 1)   # 0 timing markers в visible body

$ grep -nE "малых групп|в группах|разбейтесь|команд[аы] по [0-9]" /tmp/pptx-visible.txt /tmp/pptx-notes.txt
1 match (speaker notes, s01): "Никаких малых групп, как и в прошлый раз."
# это ПОЗИТИВНОЕ подтверждение отсутствия групповой работы (соответствует
# курсовому правилу), не нарушение — false positive паттерна.

$ python3 tools/presentation-build/deep_latin_scan.py /tmp/pptx-visible.txt
54 unique tokens вне allowlist (119 occurrences)
# Все проверены вручную — proper nouns / протокольные акронимы (raunds
# "найди подделку") / established course terms glossed on first use /
# facilitator-guide-canonical hybrid loanword. См. residual-раздел выше.
# 0 переводимых bare-англицизмов после Russification round.
```

## Итоговая структура — ИСТОРИЧЕСКАЯ, Round 1 (26 слайдов)

**Заменена в Round 2 — см. «## Round 2 — reveal-architecture fix» ниже для
актуальной структуры (40 слайдов). Таблица оставлена для истории.**

| # | id | type | Раздел | duration_min |
|---|----|------|--------|---------------|
| 1 | s01 | hero_cover | 1. Открытие | 1 |
| 2 | s02 | assertion_visual | 1. Recap | 5 |
| 3 | s03 | poll_reveal | 2. Калибровка — mechanic+roster | 2 |
| 4 | s04 | poll_reveal | 2. Инструменты 1-2 | 3.5 |
| 5 | s05 | poll_reveal | 2. Copilot pair (ключевой момент) | 5.5 |
| 6 | s06 | poll_reveal | 2. Инструменты 5-6 | 3 |
| 7 | s07 | assertion_visual | 3. Intro методики | 1 |
| 8 | s08 | quadrant | 3. Сценарий 1 | 3 |
| 9 | s09 | quadrant | 3. Сценарий 2 | 5.5 |
| 10 | s10 | quadrant | 3. Сценарий 3 | 5.5 |
| 11 | s11 | quadrant | 3. Сценарий 4 | 5 |
| 12 | s12 | reflection_question | 3. Где AI не нужен | 4 |
| 13 | s13 | assertion_visual | 4. Intro + disclosure | 1 |
| 14 | s14 | comparison | 4. Раунд 1 Python | 3.5 |
| 15 | s15 | comparison | 4. Раунд 2 HTTP/2 | 3.5 |
| 16 | s16 | comparison | 4. Раунд 3 B-дерево | 3 |
| 17 | s17 | reflection_question | 4. Рефлексия | 2 |
| 18 | s18 | assertion_visual | 5. Intro 3 типа | 1.5 |
| 19 | s19 | case_study | 5. Виньетка 1 bias | 2 |
| 20 | s20 | case_study | 5. Виньетка 2 sycophancy | 2 |
| 21 | s21 | case_study | 5. Виньетка 3 shift | 2 |
| 22 | s22 | case_study | 5. Виньетка 4 ambiguous | 3 |
| 23 | s23 | reflection_question | 5. Закрывающая рефлексия | 2.5 |
| 24 | s24 | assertion_visual | 6. Мостик к Лекции 2 | 3 |
| 25 | s25 | summary | 7. Памятка на вынос | 3 |
| 26 | s26 | hero_closing | (closing) | 0 |
| | | | **ИТОГО** | **76** |

## Anti-fatigue layout variety (sem-01 known bug #5)

- **6 инструментов раздела 2** — НЕ 6 идентичных слайдов; сгруппированы в
  3 reveal-карточки (s04/s06 горизонтальные пары) + 1 выделенный
  vertical-stack слайд для Copilot pair (s05, с gold-стрелкой-коннектором).
- **4 сценария раздела 3** — 4 РАЗНЫХ layout: `left_text_right_quad` (s08),
  `top_text_bottom_quad` (s09), `twin_column` (s10), `twin_column_gold`
  (s11, зеркальный к s10 + emphasis-панель).
- **3 раунда «найди подделку»** — question+answer объединены на одном
  слайде (не Q/A пара как в sem-01), 2 side-by-side (s14/s15) + 1 stacked
  (s16) для визуального разнообразия внутри серии.
- **4 виньетки провалов** — `wide_story_bottom_answer` (s19, s21),
  `left_answer_right_story` (s20, зеркальный layout), dashed-gold-border
  dual-answer (s22, намеренно visually distinct для пограничного случая).

## Известные баги sem-01 — статус в sem-02

1. Data labels на графиках — N/A, в этой деке нет QuickChart-графиков
   (контент дискуссионный, не данные).
2. Watermark/логотип, выдающий ответ — N/A, нет внешних изображений в
   voting-разделах (только hero s01/s26, оба вне голосования).
3. Асимметричные форматы карточек в раунде — ИСПРАВЛЕНО ПРЕВЕНТИВНО: все
   3 раунда «найди подделку» используют идентичный текстовый формат для
   вариантов А/Б (`fake_round_slide()` единая функция).
4. Pill-чипы похожие на кнопки — ИСПРАВЛЕНО ПРЕВЕНТИВНО: answer badges
   везде filled_rect с текстом, не rounded pill; голосование объясняется
   через `hand`+`camera` иконки, не через кликабельный chip-стиль.
5. Структурная усталость от идентичных слайдов — см. Anti-fatigue раздел
   выше.
6. Иконка на одном пункте из шести без иконок на остальных — ИСПРАВЛЕНО
   ПРЕВЕНТИВНО: список 6 инструментов (s03) — иконка на КАЖДОЙ из 6 строк;
   4 сценария — иконка на каждом; 4 виньетки — иконка на каждой.
7. `[TODO: ...]` заглушки — 0 найдено (проверено grep).
8. Сумма duration_min == 76 — подтверждено программно.
9. Cross-artifact drift `.md` vs render — обновлены `## Visual` описания
   в s07/s11/s12 после layout/Russification фиксов.
10. Gold-текст на светлом фоне — использован `GOLD_DARK` (#8A6200,
    WCAG-safe) для всех text-color применений gold-акцента на светлом
    фоне; чистый GOLD (#F0AB00) используется только для icons/strokes/
    fills/badges и text на тёмном (DEEP) фоне (s01/s26 hero captions).
11. Англицизмы — см. deep_latin_scan раздел выше.

## Топ-2 самых удачных слайда

1. **s05 (Copilot pair, «Один инструмент — два режима»)** — ключевой
   педагогический момент раздела 2 получил визуально отличное от всех
   соседних слайдов решение: вертикальный stack с gold-стрелкой-коннектором
   между inline (TEAL «Приложение») и agent-режимом (DEEP «Агент»), плюс
   явный связующий тезис снизу тёмно-золотым текстом. Композиция сама
   передаёт «один и тот же продукт, другой путь» — 5-Second Test проходит:
   assertion читается без необходимости вчитываться в детали карточек.
2. **s01/s26 (hero cover/closing pair)** — оба используют реальные фото
   (не моки), тематически замкнуты друг на друга (bounding-box detection →
   GPU chip «внутри модели»), с честной атрибуцией источника на каждом.
   s01 прямо продолжает YOLO/детекция мотив Лекции 1, s26 явно
   форшадоуит Лекцию 2 (токены/эмбеддинги/внимание — «работает на кремнии
   вроде этого»). Emotional arc замкнут.

## Топ-2 самых слабых слайда (с обоснованием)

1. **s08 (Сценарий 1)** — после фиксов residual minor whitespace между
   текстом сценария и Q1/Q2 блоком всё ещё присутствует (сценарий 1
   намеренно короткий текст — «разминочный», по брифу). Не блокирующий
   issue (визуальная масса приемлема), но менее плотный, чем соседние
   сценарии 2-4 с более длинными сценариями. Оставлен как есть — сокращать
   карточку ещё сильнее означало бы визуально отделять «лёгкий» сценарий
   1 от более насыщенных 2-4, что противоречиво с их равным местом в
   методике раздела.
2. **s04/s06 (инструменты 1-2, 5-6)** — самые «стандартные» reveal-карточки
   в деке (horizontal pair, ocean_box + badge + text) без уникального
   визуального крючка, в отличие от s05 (Copilot pair) или сценарных
   слайдов с квадрантами. Функционально корректны, педагогически
   достаточны (это разминочные пункты по брифу), но с точки зрения чистого
   визуального интереса — наименее запоминающиеся слайды колоды.

## Ассеты — источники

- **Иконки:** Lucide static (`cdn.jsdelivr.net/npm/lucide-static@latest`),
  46 уникальных иконок × 6 цветов × 3 размера = 828 PNG в
  `rendered/assets/icons/rendered/`.
- **s01 hero:** Wikimedia Commons, «Intersection over Union - object
  detection bounding boxes.jpg», Adrian Rosebrock, CC BY-SA 4.0.
  `assets/screenshots/s01-iou-bbox-real.jpg` + `.url` provenance file.
- **s26 hero (closing):** Wikimedia Commons, «NVIDIA GPU.jpg», Mickael
  Courtiade, CC BY 2.0. `assets/screenshots/s-closing-gpu-real.jpg` + `.url`
  provenance file.
- Acquisition tier: Tier 2 (Wikimedia Commons прямой поиск) для обоих hero
  изображений — успех с первой попытки, полный 6-tier перебор не
  потребовался.

---

## Round 2 — reveal-architecture fix (2026-08-08)

### Что изменилось и почему

`presentation-critic` (REJECT) и `student-simulator` — независимо друг от
друга — нашли один и тот же архитектурный P0: 11 из 26 слайдов объединяли
вопрос и ответ на одном статичном PNG без click-to-reveal. Правильный ответ
(gold-highlighted ячейка квадранта / gold-обводка + reveal-панель / цветной
answer-badge) был виден на том же экране, что и сценарий/вопрос, который
facilitator-guide.md явно предписывает показывать студентам ДО голосования.
Root cause: python-pptx builder не поддерживает animation/click-to-reveal
(0 animation objects в PPTX подтверждено критиком), а прецедента
click-to-reveal в `notes/mcp-limitations.md` нет.

**Fix:** split на пары слайдов вопрос/ответ по образцу Семинара 1
(`sXX-q.md` → `s(X+1)-a.md`), полностью убирающий любой визуальный сигнал
ответа с Q-слайда:
- Quadrant-сценарии (было s08-s11): Q-слайд показывает квадрант БЕЗ
  gold-заливки ни одной ячейки (все 4 нейтральные `SOFT_GREY`) — выбран
  вариант «квадрант виден, но нейтрален» (не «квадрант убран совсем»),
  чтобы Q-слайд сохранял содержательность как самостоятельный визуал.
- Find-the-fake раунды (было s14-s16): оба варианта А/Б идентичны по
  формату на Q-слайде (нейтральная `LIGHT` рамка на обоих), reveal-панель
  снизу заменена на нейтральную SURFACE/TEAL полосу с подсказкой механики
  голосования; на A-слайде — gold-рамка на подделке + полная reveal-панель.
- Виньетки (было s19-s22): Q-слайд показывает только сценарий + нейтральную
  SURFACE/TEAL подсказку-полосу «Bias? Sycophancy? Distribution shift? Не
  уверен?»; A-слайд — полный цветной answer-badge/dual-answer + объяснение.
- Инструменты раздела 2 (было s04-s06): Q-слайд — 2 карточки БЕЗ badge,
  только описание контекста использования; A-слайд — полный reveal с
  badge+рассуждение. Ключевая пара Copilot inline/Agent (было s05) также
  разделена на Q (баннер + 2 режима без badge, без gold-стрелки) / A
  (то же + badge + gold-стрелка-коннектор + связующий тезис).

### Icon-leak fix (обнаружено самостоятельно при визуальной инспекции)

При построчной проверке через 5-Second Test обнаружил дополнительный канал
утечки ответа, не пойманный критиками: 2 виньетки (было s19 bias, s21
shift) использовали на Q-слайде ТОТ ЖЕ answer-hinting icon (`scale` для
bias, `trending-down` для shift), что и на A-слайде для цветного badge —
это утечка ответа через выбор иконки, тот же класс бага, что и
gold-заливка. **Исправлено превентивно** (не входило в explicit findings
критиков, но тот же принцип): s29 (виньетка 1 Q) теперь использует
нейтральную иконку `briefcase` (контекст найма) вместо `scale`; s33
(виньетка 3 Q) — нейтральную `ticket` (контекст техподдержки) вместо
`trending-down`. Виньетка 2 (было s20, sycophancy) была спроектирована
правильно с самого начала — Q-слайд уже использовал нейтральную `code`
вместо `smile`, оставлено без изменений как образец.

### Per-slide id mapping (14 исходных → 28 новых)

| Старый id (Round 1) | → | Новые id (Round 2) | duration split (было → q+a) |
|---|---|---|---|
| s04 (инструменты 1-2) | → | s04-q / s05-a | 3.5 → 1.3 + 2.2 |
| s05 (Copilot pair) | → | s06-q / s07-a | 5.5 → 2.2 + 3.3 |
| s06 (инструменты 5-6) | → | s08-q / s09-a | 3.0 → 1.2 + 1.8 |
| s08 (сценарий 1) | → | s11-q / s12-a | 3.0 → 1.2 + 1.8 |
| s09 (сценарий 2) | → | s13-q / s14-a | 5.5 → 2.0 + 3.5 |
| s10 (сценарий 3) | → | s15-q / s16-a | 5.5 → 2.0 + 3.5 |
| s11 (сценарий 4) | → | s17-q / s18-a | 5.0 → 1.8 + 3.2 |
| s14 (раунд 1 Python) | → | s21-q / s22-a | 3.5 → 1.5 + 2.0 |
| s15 (раунд 2 HTTP/2) | → | s23-q / s24-a | 3.5 → 1.5 + 2.0 |
| s16 (раунд 3 B-дерево) | → | s25-q / s26-a | 3.0 → 1.3 + 1.7 |
| s19 (виньетка 1 bias) | → | s29-q / s30-a | 2.0 → 0.8 + 1.2 |
| s20 (виньетка 2 sycophancy) | → | s31-q / s32-a | 2.0 → 0.8 + 1.2 |
| s21 (виньетка 3 shift) | → | s33-q / s34-a | 2.0 → 0.8 + 1.2 |
| s22 (виньетка 4 ambiguous) | → | s35-q / s36-a | 3.0 → 1.2 + 1.8 |

12 неизменных слайдов переномерованы вокруг сплитов: s01→s01, s02→s02,
s03→s03, s07→s10, s12→s19, s13→s20, s17→s27, s18→s28, s23→s37, s24→s38,
s25→s39, s26→s40. `deck.yaml` — единственный source of truth порядка;
sequential filenames (`s01`..`s40`) соответствуют `deck.yaml` id ровно.

Пропорция split — не 50/50: вопрос+размышление обычно короче
вопрос+обсуждение+разбор (смотрел на содержание speaker notes каждого
слайда, аналогично Sem-01 s07/s08 = 1.3+1.3 из равного 2.6, но здесь
пропорция подобрана per-slide — например s17/s18 (сценарий 4) 1.8+3.2,
потому что A-слайд несёт «второй раз за сегодня» тезис + reveal, который
требует больше времени на разбор).

### Anti-fatigue layout variety (сохранено и расширено)

Каждая половина каждой новой пары использует РАЗНЫЙ визуальный акцент от
своей второй половины (не идентичные Q/A):
- Quadrant-сценарии: Q-слайд = нейтральный квадрант (`SOFT_GREY` все 4
  ячейки) + нейтральная TEAL-подсказка вместо gold callout; A-слайд =
  оригинальная gold-reveal геометрия. Layout-variant (`left_text_right_quad`
  / `top_text_bottom_quad` / `twin_column` / `twin_column_gold`) сохранён
  ИДЕНТИЧНЫМ между Q и A одной пары (это правильно — это одна и та же
  композиция, различается только reveal-состояние), но 4 РАЗНЫХ сценария
  всё ещё используют 4 РАЗНЫХ layout между собой, как в Round 1.
- Find-the-fake раунды: Q/A пары сохраняют layout `side_by_side` (раунды
  1-2) / `stacked` (раунд 3) идентичным внутри пары — вариативность между
  3 раундами (не между Q/A) сохранена как в Round 1.
- Виньетки: та же логика — layout (`wide_story_bottom_answer` /
  `left_answer_right_story` / dashed-gold-border) идентичен внутри Q/A
  пары, вариативность между 4 виньетками сохранена.
- Инструменты раздела 2: Copilot pair (s06-q/s07-a) сохраняет
  vertical-stack-with-connector отличие от horizontal-pair (s04-q/s05-a,
  s08-q/s09-a) — тот же anti-fatigue паттерн, что в Round 1, применён
  дважды (один раз на Q, один раз на A половине).

### Visual mass balance fixes (P1, presentation-critic)

- **s04-q/s08-q (было s04, s06 — карточки инструментов):** описание теперь
  `MSO_ANCHOR.MIDDLE` в карточке фиксированной высоты 4.05" (вместо
  top-anchored в 4.7"-карточке с заголовком) — устраняет пустое
  пространство в нижней трети, которое критик отметил на s04/s06.
- **s11-q/s13-q/s15-q (было s08, s09, s10 — сценарии 1-3, Q-половины):**
  унаследовали ту же геометрию карточек, что и оригинальные A-слайды
  (нет regression — критик отмечал остаточный воздух конкретно на s08 как
  «acceptable», не блокирующий; геометрия сохранена без изменений на A-
  половине по этой же причине).
- Оба фикса верифицированы визуально через squint-test на PNG snapshots.

### Russification fixes (P1, presentation-critic)

1. **s34 (было s21, виньетка 3 ответ) — bare латиница в explanation:**
   «...классический признак shift, а не bias или sycophancy» →
   «...классический признак **сдвига распределения**, а не **смещения
   (bias)** или **подстройки (sycophancy)**» — тот же inline-gloss
   паттерн, что уже применён на s28 (было s18).
2. **s37 (было s23, закрывающая рефлексия 3 плитки) — без перевода:**
   каждая плитка теперь имеет вторую строку мельче курсивом с переводом:
   «Bias / смещение», «Sycophancy / подстройка», «Distribution shift /
   сдвиг распределения».
3. **s39 (было s25, памятка на вынос) — без перевода + terminology
   drift:** «Dist. shift» (нигде больше не встречавшееся сокращение)
   нормализовано до «Distribution shift (сдвиг распределения)», полностью
   совпадает с формулировкой s28/s37. Все три типа провала теперь имеют
   полный русский глосс на памятке (раздаточный материал без
   сопровождающего контекста — глоссинг обязателен).
4. **s28 (было s18) — H1 title целиком на латинице:** «Bias / sycophancy /
   distribution shift — та же тройка, новые примеры» → «Три типа провала:
   bias, sycophancy, distribution shift — новые примеры» (русский лид,
   термины — в подчинённой позиции, соответствует рекомендации критика).
5. **s08-q (было часть s06) — новый англицизм, добавленный при написании
   Q-слайда:** «тот же worked example, что на лекции» → «тот же
   разобранный пример, что на лекции» (в `.md` и в builder).
6. **Пред-существующие англицизмы в speaker notes, не пойманные Round 1
   grep (найдено при deep_latin_scan Round 2):** `cold-call` (2
   occurrences, s10 intro + s16-a) → «точечный вызов» / «вызовите»;
   `rule-based` (2 occurrences, s19 — было s12) → «готовые правила» /
   «правилами»; `human-in-the-loop review` (2 occurrences, s19 Visual +
   notes) → «проверка человеком перед автоматическим действием». Round 1
   log утверждал эти фиксы сделаны, но применил их только к visible body,
   не к speaker notes — Round 2 закрывает разрыв.

### Re-verification results (после всех фиксов)

Полная пересборка `build_sem02.py` → 40 слайдов → PDF → 40 PNG snapshots
@150dpi. Visual sweep: все 28 новых Q/A-слайдов прошли минимум 1
inspect-fix цикл (icon-leak fix на s29/s33 обнаружен и исправлен именно
через этот цикл); все слайды с изменённой геометрией (s04-q/s08-q visual
mass fix) прошли минимум 1 повторный inspect. 12 неизменных слайдов
(контент не трогался) визуально сверены на предмет отсутствия regression
от renumbering — все чисты.

```
$ python3 -c "sum duration_min across slides/*.md"
76.0   # == deck.yaml duration_min (76), == facilitator-guide.md
       # итоговая таблица (76). 40 файлов, все id s01..s40 без пропусков.

$ grep -nE "\[VERIFY-DAY-OF\]|\[FACT-CHECK\]|LO[1-9]|§[0-9]+\.[0-9]+|→ s[0-9]+|см\. s[0-9]+|якорь:" \
    <extracted pptx visible + notes text>
0 hits   # scaffold-leak grep — чисто

$ grep -nE "[0-9]+\s*мин(ут)?\b|Время раздел|Тайминг|Длительность|⏱|⏰" <extracted text>
0 hits   # timing-marker grep — чисто

$ grep -nE "(методическ|педагогическ)\s*\w+|Лектору|Преподавателю|Вы здесь" <extracted text>
4 hits, все false positives — «...написаны автором методического
комплекта...» (honest-labeling disclosure phrase, pre-existing с Round 1,
не meta-комментарий; критик Round 1 явно принял эту формулировку). 0
случаев реального «методически важно» / «педагогическая цель» / «Лектору:»
паттерна.

$ grep -nE "малых групп|в парах|разбейтесь|команд[аы] по [0-9]" <extracted text>
2 hits, оба — позитивные подтверждения ОТСУТСТВИЯ групповой работы (s01
speaker notes: «Никаких малых групп»; s20 speaker notes: «индивидуально и
всей аудиторией, а не в парах, как было на утренней лекции»). 0 нарушений.

$ python3 tools/presentation-build/deep_latin_scan.py <extracted pptx text>
До фиксов (первый прогон Round 2, до Russification-исправлений):
  69 unique tokens, 349 occurrences (включая artifact "NOTES" от extraction
  script и 3 новых англицизма: worked example / cold-call / rule-based).
После фиксов:
  62 unique tokens (без "NOTES:"-artifact-строки), 299 occurrences.
  Все категории — proper nouns (Bayer/McCreight/Boeing/CWI/Centrum
  Wiskunde Informatica/Adrian Rosebrock), протокольные акронимы
  (RFC/TCP/UDP/QUIC/HTTP), established course terms glossed at first use
  (Bias/Sycophancy/Distribution shift — теперь ещё и на s28/s34/s37/s39
  явно), mode names (Tab-completion/Workspace/inline), hybrid loanwords
  с русским окончанием совпадающие с facilitator-guide canonical usage
  (Agent-режим/Coding-агент/DevOps-инженеров/YOLO-детектор/PDF-отчётов).
  Рост occurrences vs Round 1 baseline (54 unique/119) объясняется
  дублированием общего словаря между Q и A половинами каждой из 14
  split-пар (протокольные акронимы/proper nouns теперь на 2 слайдах
  вместо 1) — не новой категорией проблем.
```

### Что осталось нерешённым (явно, не скрываю)

1. **s05-a/s09-a (было s04/s06, инструменты 1-2 и 5-6, A-половины)** —
   унаследовали от Round 1 minor residual whitespace в нижней части
   карточек (Round 1 log отметил их как «наименее запоминающиеся», не как
   дефект). Не тронуто в Round 2, потому что вне scope Round 2 brief
   (visual mass fix предписан явно только для s04/s06/s08/s09/s10 —
   применил MIDDLE-anchor к Q-половинам этих пар, но НЕ к A-половинам,
   чтобы не расходиться с оригинальной, уже принятой критиком геометрией
   reveal-карточек). Кандидат на P2 polish, если будет отдельный запрос.
2. **Icon-leak fix (s29/s33) не входил в explicit findings критиков** —
   обнаружен самостоятельно при повторном 5-Second Test проходе. Не
   уверен на 100%, что это исчерпывающий список — не проводил отдельный
   систематический icon-audit по всем 28 новым слайдам сверх этих двух
   находок (только целевую проверку quadrant-сценариев, где иконки
   нейтральны by design, и find-the-fake раундов, где иконок на карточках
   вариантов нет вообще).
3. **`build_sem02.py.bak`** — сохранена копия pre-Round-2 версии builder'а
   в `rendered/` для сравнения/отката; не удалена, оркестратор может
   удалить перед коммитом, если не нужна.
