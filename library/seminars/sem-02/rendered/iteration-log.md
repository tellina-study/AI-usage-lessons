# Iteration log — Семинар 2 «Классифицируй и не ошибись»

**Продолжение в `iteration-log-round2.md`** — Round 2 (reveal-architecture
fix, 26→40 слайдов) и Round 3 (точечные фиксы) — вынесены в отдельный файл,
чтобы остаться под лимитом 600 строк на документ (CLAUDE.md Document Size
Limit). Этот файл — Round 1 (первая полная сборка деки, 26 слайдов).

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

## Автоматические проверки — финальный результат (Round 1)

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

**Заменена в Round 2 — см. `iteration-log-round2.md` для актуальной
структуры (40 слайдов). Таблица оставлена для истории.**

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

## Anti-fatigue layout variety (sem-01 known bug #5) — Round 1 baseline

- **6 инструментов раздела 2** — НЕ 6 идентичных слайдов; сгруппированы в
  3 reveal-карточки (s04/s06 горизонтальные пары) + 1 выделенный
  vertical-stack слайд для Copilot pair (s05, с gold-стрелкой-коннектором).
- **4 сценария раздела 3** — 4 РАЗНЫХ layout: `left_text_right_quad` (s08),
  `top_text_bottom_quad` (s09), `twin_column` (s10), `twin_column_gold`
  (s11, зеркальный к s10 + emphasis-панель).
- **3 раунда «найди подделку»** — question+answer объединены на одном
  слайде (не Q/A пара как в sem-01), 2 side-by-side (s14/s15) + 1 stacked
  (s16) для визуального разнообразия внутри серии. **Это решение отменено
  в Round 2** (см. `iteration-log-round2.md`) — совмещённый Q/A на одном
  статичном слайде оказался P0-багом (ответ виден до голосования).
- **4 виньетки провалов** — `wide_story_bottom_answer` (s19, s21),
  `left_answer_right_story` (s20, зеркальный layout), dashed-gold-border
  dual-answer (s22, намеренно visually distinct для пограничного случая).

## Известные баги sem-01 — статус в sem-02 (Round 1 baseline, см. Round 2/3 для обновлений)

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
   выше. **Round 1 решение (combined Q/A) создало НОВЫЙ баг (preemptive
   reveal) — см. Round 2.**
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

## Топ-2 самых удачных слайда (Round 1)

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

## Топ-2 самых слабых слайда (Round 1, с обоснованием)

1. **s08 (Сценарий 1)** — после фиксов residual minor whitespace между
   текстом сценария и Q1/Q2 блоком всё ещё присутствует (сценарий 1
   намеренно короткий текст — «разминочный», по брифу). Не блокирующий
   issue (визуальная масса приемлема), но менее плотный, чем соседние
   сценарии 2-4 с более длинными сценариями.
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
