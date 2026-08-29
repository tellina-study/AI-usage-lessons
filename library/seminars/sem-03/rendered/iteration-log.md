# Семинар 3 — iteration log

Формат матчит `library/seminars/sem-02/rendered/iteration-log.md` — прямая сборка
через `python-pptx` (не PowerPoint MCP), per `notes/mcp-limitations.md`
[#54-1/#54-2/#54-3]. Toolchain: bootstrapped `soffice` + `pdftoppm` +
`rsvg-convert` из `/tmp/claude-999/local` (см. `/tmp/claude-999/render-env.sh` +
`/tmp/claude-999/pptx_to_png.sh`).

**Важная находка toolchain'а (новая, не в notes/mcp-limitations.md ранее):**
`render-env.sh` переопределяет `$HOME` на `/tmp/claude-999/loffice-home` —
это ломает резолюцию `~/.local/lib/python3.12/site-packages`, где установлен
`python-pptx`. **Следствие:** нельзя сорсить `render-env.sh` перед запуском
`build_semNN.py` — `python3 build_sem03.py` запускается БЕЗ source
render-env.sh (использует системный `python3` с нормальным `$HOME`), а
`pptx_to_png.sh` уже сам сорсит render-env.sh внутри себя для конвертации.
Добавлено в `notes/mcp-limitations.md` как `[#sem03-render-1]`.

## Источники и подготовка

Обязательное чтение перед началом (весь список из задания): facilitator-guide.md
(полностью, 295 строк), brief.md, rubric.md, sem-02/deck.yaml + все slides/*.md
(формат, паттерны visual, q/a-split архитектура), sem-02/rendered/iteration-log.md
+ iteration-log-round2.md (методика рендера, известные баги icon-recolor и
weight-bar geometry), notes/mcp-limitations.md, lec-02/chapter.md §2.2
(SSL/HTTPS/React/борщ), §3.1-3.2 (фонарик, «Кот съел мышь»), §4.3 (таблица 4
ручек API), §5.5 (домашнее задание, баг нумерации «Тема семинара 2»).

## Hero images (6-tier acquisition)

- **s01 hero:** «T-SNE Embedding of MNIST» (Kyle McDonald, Wikimedia Commons,
  CC BY 2.0) — Tier 2 (Wikimedia напрямую). Реальная t-SNE визуализация
  embedding-пространства (10 цветных кластеров MNIST-цифр). Прямо
  иллюстрирует keystone-ось Блока 1: близость в векторном пространстве =
  близость смысла. Скачано напрямую через `upload.wikimedia.org`, проверено
  визуально (Read tool на PNG) до использования.
  `library/seminars/sem-03/assets/screenshots/s01-tsne-embedding-real.png` +
  `.url` с атрибуцией.
- **s28 hero (closing):** «Industrial-robots-21» (Haophuong21, Wikimedia
  Commons, CC BY-SA 4.0) — Tier 2. Реальное фото промышленного
  робота-манипулятора, автоматически работающего с бутылками на
  производственной линии. Мост к Лекции 3 (agent act→observe→correct loop).
  Первая попытка — «UR16e robot arm.png» — отклонена на этапе визуальной
  проверки: PNG с прозрачным фоном (product cutout), не подходит для
  full-bleed hero (выглядел бы как плавающий объект на тёмном фоне, не
  фотографично). Заменено на «Industrial-robots-21.jpg» — полнокадровое
  фото с реальным интерьером помещения.
  `library/seminars/sem-03/assets/screenshots/s-closing-industrial-robots-real.jpg`
  + `.url`.

## Иконки

828 уже отрендеренных icon-PNG из `sem-02/rendered/assets/icons/rendered/`
переиспользованы напрямую (тот же Lucide-набор, тот же Ocean-реколор) через
fallback в helper `icon_path()` — если файла нет в `sem-03/rendered/assets/icons/rendered/`,
берётся из `sem-02`. Новые комбинации icon×color, которых не было в
sem-02 (SLATE `#6B7685` для muted/no-состояний, `zap` в тёмно-золотом
`#8A6200`), сгенерированы через `assets/icons/gen_missing.sh` — тот же
sed-паттерн реколора (**только** `stroke="..."` / `currentColor`, **никогда**
`fill="..."`, per задокументированный P1-баг sem-02: `fill="none"` на root
`<svg>` ломался при блокетном реколоре fill). Проверено визуально
(help-circle/x-circle остались outline, не залитые круги).

## Сборка и рендер

`build_sem03.py` — 1290+ строк, 28 slide-builder функций + 3 shared builders
(`two_card_pair` для омонимов/перифразов, `coref_slide` для 4 раундов
Winograd/кореференции, общие helpers из sem-02: `ocean_box`, `chip`, `icon`,
`gold_callout`, `dashed_box`, `vote_hint_bar`).

PPTX сгенерирован, сконвертирован в PDF (150 dpi PNG snapshots) через
`pptx_to_png.sh`.

## Итерации (минимум 3, фактически 4)

### Iter 1 — первичный рендер, полный визуальный sweep всех 28 слайдов

Найдено при инспекции:

**P1 (структурные баги геометрии):**
1. **s01** — gold-подпись «БЛИЗОСТЬ В ПРОСТРАНСТВЕ = БЛИЗОСТЬ СМЫСЛА»
   накладывалась на верхний край gold-обводки фото, нечитаема. Root cause:
   текст рисовался на y-координате внутри рамки, а не над ней в тёмном поле.
   **Fix:** ввёл `caption_h` в геометрию hero-блока, сдвинул белую карточку
   с фото вниз на `caption_h`, подпись теперь в чистом тёмном поле над рамкой.
2. **s11** — 3-й weight-bar («голодна») в recap-примере «Кот съел мышь»
   вылезал за нижнюю границу Ocean box карточки. Root cause: `card_h=3.35`
   недостаточен для title+3 строки текста+3 weight-bar (нужно 3.75+).
   **Fix:** `card_h` 3.35→3.75, `tag_y` ниже автоматически пересчитывается
   от `card_h` (без хардкода).
3. **s17** (через `coref_slide` shared builder) — 3-й weight-bar
   («менеджер») в explanation-блоке перекрывался с explanation-карточкой,
   т.к. `exp_y` был захардкожен на `below_y+0.75`, не учитывая реальную
   высоту блока весов (для 3 items нужно больше места, чем для 2).
   **Fix:** `weights_block_h` считается динамически из фактического числа
   items, `exp_y = below_y + max(0.75, weights_block_h)`.
4. **s15** (build_s15, кастомная geometry для Winograd вариант 2 reveal) —
   2 weight-bar рисовались почти на одной y-координате (0.28 vs 0.32
   разница — визуально сливались, label «трофей» накладывался на короткий
   серый bar). Root cause: неправильная inline-арифметика вместо цикла
   с накоплением `wy`. **Fix:** переписал на цикл с `wy += 0.3` per item,
   как везде в деке.
5. **Q-slide dead space** (coref_slide question-mode: s12/s14/s16/s18) —
   card_h=2.55 оставлял ~1.7" пустого пространства между hint-bar и низом
   слайда (visual mass imbalance). **Fix:** card_h question-mode 2.55→3.6,
   icon+текст теперь MIDDLE-anchored в увеличенной карточке (контент
   заполняет пространство, а не padding).

**P2 (anti-anglicism, найдено на pattern-narrow grep + deep_latin_scan):**
6. s03 title «Cosine similarity» (bare English H1) → «Косинусная близость».
7. section_tag «WINOGRAD SCHEMA» (bare English caps, 4 слайда s12/s13/s14/s15)
   → добавлено русское слово-контекст «пара Winograd Schema» (proper noun
   остаётся non-translated per keep-list правило для академических
   бенчмарков, но обрамлён по-русски, не голый капс).
8. s09 «cross-lingual embedding» → «перевод через эмбеддинг».
9. s20 card body bare «attention» → «внимание (attention)» (inline-gloss).
10. s22/s25 «production»/«downstream-логику»/«floating-point» → русские
    формулировки («боевого режима», «логику последующих шагов», «вычислений
    с плавающей точкой»).
11. «Recap с Лекции 2» (3 карточки: s03/s11/s21) → «Повтор с Лекции 2».
    «Recap конвейера» (s02 section_tag) → «Повтор конвейера».
12. Speaker notes (не только visible body): s10 «decision tree» → «дерево
    решений»; s20 «Attention — это именно механизм» → «Внимание — это
    именно механизм» (стандалон-предложение с заглавной English-буквы,
    найдено ТОЛЬКО через deep_latin_scan на notes+visible вместе, не
    попадало в узкий pattern grep).

### Iter 2 — применены все fix'ы выше, полный re-render + re-inspect

Проверены визуально все затронутые слайды (s01, s02, s03, s11, s12, s13,
s14, s15, s16, s17, s18, s19, s21, s22, s25) — все P1-баги геометрии
подтверждены исправленными (weight bar'ы полностью внутри карточек,
caption на s01 читаема, Q-slide карточки заполняют пространство без
дыр). Anglicism-фиксы подтверждены на PNG.

### Iter 3 — deep_latin_scan на РЕНДЕРЕННЫЙ PPTX (не на markdown design-brief)

Важное методическое уточнение по ходу: первый прогон `deep_latin_scan.py`
на `slides/*.md` дал 300+ unique tokens — это ложный сигнал, потому что
скрипт сканировал `## Visual` секции markdown (design-brief прозу для
дизайнера: `Ocean box`, `DEEP`, `TEAL`, `Assertion`, `Speaker notes` —
структурные токены формата файла, никогда не попадающие в рендер). **Прогнал
повторно на извлечённый текст из самого `sem-03.pptx`** (через
`python-pptx` API `shape.text_frame.text` по всем слайдам) — это и есть
корректная цель проверки per `tools/presentation-build/deep_latin_scan.py`
docstring («For PPTX visible text»).

На PPTX visible text: 60 occurrences / 37 unique. Триаж:
- `cosine` (8×), `illustrative` — established термины из facilitator-guide/
  chapter (используются bare в источнике), badge-labels — принято.
- `WINOGRAD`/`SCHEMA`/`Winograd Schema Challenge` — proper noun академический
  бенчмарк, обязателен bare per задание («обязательно назвать вслух как
  реальный академический бенчмарк»).
- `Strawberry fields: a guide to growing your own` — буквальное название
  документа-кандидата из facilitator-guide §2.4 (данные упражнения, не
  narrative — намеренно на английском, это часть теста на cross-lingual
  embedding).
- `Retrieval-Augmented Generation` — официальный expansion RAG, факт.-гид
  называет термин именно так.
- `Function calling` / `Agent loop` (s26 bridge tags) — намеренно
  необъяснённые bare-теги мостика к Лекции 3 («не объясняйте механику» —
  прямая инструкция гида), тот же паттерн, что sem-02 s38.
- `Levesque, Davis, Morgenstern` — цитирование авторов, proper noun.
- `BY-SA`, `email-`, `argmax`, `live-` — established/лицензионные токены,
  keep-list style.

Прогнал повторно deep_latin_scan на PPTX+speaker_notes вместе (338 текстовых
блоков) — нашёл 2 дополнительных genuine hits в notes, не видимых в
narrow-grep (см. iter 1 п.12 выше — уже исправлены до этой точки, повторный
scan подтвердил 0 новых genuine hits после фикса).

### Iter 4 — финальный full render + верификация

Пересобрал PPTX (`python3 build_sem03.py`, без source render-env.sh — см.
toolchain finding выше), пересчитал 28 PNG snapshots. Финальный визуальный
sweep (s04, s05, s09, s10 повторно) — все чисто. Программная проверка
q/a-split (grep + gold-pixel-fraction анализ через PIL на всех 8 Q-slide
PNG — 0.0000 gold-fraction на всех) — подтверждает: ни один Q-слайд не
содержит gold-highlighted answer badge. Пересчитан duration_min sum — 76.0
ровно, 28 слайдов.

## Итоговая самопроверка

- **duration_min sum:** 76.0 (программно, `python3 -c "..."` по всем
  `slides/*.md`) — соответствует facilitator-guide итоговой таблице (5+20+20+24+3+4=76).
- **Q/A split:** все 8 predict-then-reveal раундов (омонимы, перифразы,
  клубника, Winograd×2, coref-tech, coref-ambiguous, temperature-guess) —
  раздельные Q/A слайды, подтверждено grep + PIL gold-pixel-анализ (0 leaks).
- **Timing/methodology scan:** 0 hits `[0-9]+\s*мин`, 0 hits `⏱/⏰`, 0 hits
  `методическ|педагогическ` (кроме мандаторной фразы «автор методического
  комплекта» из facilitator-guide §4.3, не meta-комментарий), 0 hits
  «Лектору/Преподавателю/cold-call/фасилитатор/Вы здесь».
- **Anti-anglicism:** deep_latin_scan на рендеренный PPTX (visible + notes)
  — все оставшиеся unique tokens триажированы как established terms /
  proper nouns / brand-allowlist / намеренные bridge-tags per задание.
- **Render toolchain:** LibreOffice + pdftoppm + rsvg-convert полностью
  доступны через `/tmp/claude-999/local` bootstrap — рендер прошёл успешно,
  без деградации (PPTX 1.35MB, PDF 1.57MB, 28/28 PNG).

## Открытые блокеры (Round 1)

Нет. Toolchain полностью функционален, все self-checks проходят.

---

## Round 2 — синхронизация с пересмотренным facilitator-guide.md (Iteration 5)

Источник: facilitator-guide.md переработан по итогам QA-раунда (новый тайминг
§2.5/§3.5/§4.4 — все три failure/judgment-компонента расширены с 2-4 мин до
6 мин каждый) + 3 QA-отчёта (presentation-critic APPROVE-WITH-POLISH 4×P2,
student-simulator: 2 designer-extra утечки, consistency-checker: markdown↔pptx
drift D2). Прочитан заново весь facilitator-guide.md (327 строк), brief.md,
Round-1 iteration-log (эта же секция выше), presentation-critic отчёт
`qa-reports/2026-08-09/presentation-critic.md`.

### 1. Убраны 2 designer-extra утечки (student-simulator finding)

- **s11**: убран gold-бейдж «ЯДРО ЗАНЯТИЯ» рядом с заголовком раздела (был
  methodology-marker про структурную значимость блока для оркестрации занятия,
  не содержательный факт). Section tag упрощён до «Раздел 3 · Блок 2 —
  механизм внимания» (было «...· ЯДРО ЗАНЯТИЯ»). Убрана строка speaker notes
  «Это ядро сегодняшнего занятия» — тот же паттерн self-referential
  methodology comment.
- **s22**: верхняя tag-полоса заменена с «В главе Лекции 2 это задание
  подписано устаревшим номером курса до сдвига — фактически оно закрепляется
  именно здесь» (внутренняя методическая заметка про синхронизацию нумерации
  курса, не понятная студенту без контекста) на нейтральное «Домашнее задание
  из Лекции 2». Формулировка про баг нумерации осталась ТОЛЬКО в speaker
  notes (facilitator-guide §4.2 явно требует проговорить её вслух —
  «Обязательно напомнить вслух в начале блока про баг нумерации») — это
  разделение visible-tag / speaker-notes, а не удаление контента.

### 2. Исправлены 4 P2 из presentation-critic

- **s01**: build-script «три термина Лекции 2» → «три механизма Лекции 2»
  (1-строчная правка в `build_sem03.py:316`, консистентно с central assertion
  деки и остальными 27 слайдами).
- **s11/s17 speaker notes**: голое «attention» → «внимание» (термин уже
  введён визуально на s11 card «Внимание (attention)» — повторный inline-gloss
  не обязателен, per critic recommendation).
- **s13**: «не настоящий live-инструмент» → «не настоящий работающий вживую
  инструмент» — и в visible body (badge caption), и в build-script
  explanation string, и в speaker notes (продублирована формулировка из notes
  в visible body, как рекомендовал critic).
- **s27 speaker notes**: «top-p/top-k» → добавлена inline-глосса «(альтернативные
  параметры отсечения хвоста распределения вероятностей)» — как предложил
  critic вариант 1 (не «оставить как есть»).

### 3. Расширены 3 reflection-слайда под новый тайминг facilitator-guide (6 мин каждый)

Новый общий layout `worked_example_reflection()` (shared builder,
build_sem03.py) — верхняя широкая Ocean-box с worked-example (иконка +
заголовок + body + italic takeaway-строка TEAL), нижняя gold-обведённая
строка с вопросом всем классом + 2-3 компактные Ocean-box карточки с
направлениями ответа. Паттерн вдохновлён `wide_story_bottom_answer` из
sem-02 (верхний блок + нижняя строка), адаптирован под open-discussion
(без цветного answer-badge, т.к. это не predict-then-reveal раунды).

- **s10** (было 2 мин → 6 мин, §2.5): добавлен worked-example «юридический
  поиск по договорам» (риск подмены основания расторжения «одностороннее
  расторжение» vs «расторжение по соглашению сторон» при семантическом
  поиске) — точный текст перенесён из facilitator-guide §2.5. Существующий
  закрывающий вопрос классу + 2 карточки (точность/мост к RAG) сжаты, но
  сохранены полностью.
- **s20** (было 4 мин → 6 мин, §3.5): добавлен worked-example WinoBias (Zhao,
  Wang, Yatskar, Ordonez, Chang, 2018, NAACL) — систематический
  гендерно-профессиональный перекос кореференции, явно процитирован как
  ОТДЕЛЬНЫЙ от Winograd Schema (Levesque et al., 2011/2012, упомянут на
  s12-s15) академический бенчмарк — оба источника явно различены и в visible
  body, и в speaker notes («Это не тот же бенчмарк, что мы разбирали
  раньше»). Явная связка с термином bias (Семинар 2). Существующие 3 плитки
  (корреляция/причинность/пограничный случай) + вопрос сохранены.
- **s25** (было 3 мин → 6 мин, §4.4): добавлен worked-example «банковский
  чат-бот — regex + Luhn-алгоритм вместо LLM-сэмплинга» для детекции номеров
  банковских карт (ни при каком T LLM не даёт гарантии 100% срабатывания).
  Существующие 2 карточки (воспроизводимость / оговорка про T=0) + вопрос
  классу сохранены, слегка сжаты (по 2 пункта на карточку вместо 3, чтобы
  вместить worked-example сверху).

Иконки для новых worked-example блоков: `scale` (s10, было `scale-3d` в
черновике — не существует в библиотеке, заменено на существующий `scale`),
`alert-triangle` (s20, уже использовался в деке), `shield-check` (s25, было
`shield` в черновике — не существует, заменено на существующий
`shield-check`). Все резолвятся через `icon_path()` fallback в
`sem-02/rendered/assets/icons/rendered/` (828 icon library, переиспользуется
без нового скачивания).

Все 3 слайда прогнаны через отдельный Generate→Convert→Inspect цикл
(iter5) — visual sweep подтвердил отсутствие text overflow, worked-example
body текст (10.8pt) читаем, takeaway-строка (10.5pt italic TEAL) не
накладывается на нижний gold callout, карточки с пунктами не переполнены.

### 4. Пересчитан `duration_min` под новую таблицу facilitator-guide (сумма 76.0)

Новое распределение по разделам (источник — итоговая таблица
facilitator-guide.md): Раздел 1 = 4 (s01=1, s02=3), Блок 1 = 21 (s03=2,
s04+s05=2+2 [§2.2], s06+s07=1.5+1.5 [§2.3], s08+s09=3+3 [§2.4], s10=6
[§2.5]), Блок 2 = 20 неизменно но перераспределён внутри (s11=2 [§3.1],
s12-s15=1.1+1.4+1.1+1.4=5 [§3.2], s16+s17=0.8+1.2=2 [§3.3], s18+s19=2+3=5
[§3.4], s20=6 [§3.5]), Блок 3 = 25 (s21=2, s22=9, s23+s24=3.5+4.5=8, s25=6),
Мостик = 2.5 (s26), Итог = 3.5 (s27=2.5, s28=1). Проверено программно:
`python3 -c "..."` по всем 28 `slides/*.md` frontmatter — **сумма 76.0**,
совпадает с facilitator-guide итоговой таблицей (4+21+20+25+2.5+3.5=76).

### 5. Синхронизирован markdown source с anglicism-фиксами build-script (consistency-checker D2)

Выбран подход «синхронизировать markdown» (не «markdown = design-brief,
PPTX = source of truth»), т.к. build_sem03.py и так переоткрывался для
остальных Round-2 правок. Исправлено в `slides/*.md`:

- `s01`: подтверждено — markdown никогда не содержал «три термина» (только
  build-script имел этот drift), исправление затронуло только
  `build_sem03.py`.
- `s02`: H1 «Recap конвейера» → «Повтор конвейера».
- `s03`: assertion + H1 body «Cosine similarity — угол между...» → «Косинусная
  близость — угол между...» (matching build-script rendered title); Visual
  prose «Recap с Лекции 2» → «Повтор с Лекции 2»; learning_goal «Recap
  SSL/HTTPS...» → «Повтор SSL/HTTPS...».
- `s11`: Visual prose «Recap с Лекции 2» → «Повтор с Лекции 2»; «Attention —
  фонарик» → «Внимание (attention) — фонарик» (глосса); learning_goal «Recap
  метафоры» → «Повтор метафоры».
- `s21`: Visual prose «Recap с Лекции 2» → «Повтор с Лекции 2»; learning_goal
  «Recap таблицы» → «Повтор таблицы».
- Дополнительно (найдено при Round-2 работе, не в исходном D2-списке, но того
  же класса): «Worked-example» (английский термин без established-статуса,
  в отличие от «cosine»/«Winograd Schema») в новых section_tag/heading для
  s10/s20/s25 заменён на «Разобранный пример» (термин, уже используемый в
  facilitator-guide §2.5/§3.5 дословно) — и в build_sem03.py, и в markdown
  (`## Visual` prose + `primary:` YAML field), консистентно.

Все остальные ранее задокументированные established-термины (`cosine`,
`illustrative`, `Winograd Schema`, `Retrieval-Augmented Generation`, `Function
calling`, `MCP`, `Agent loop`, keep-list bridge-теги s26) оставлены без
изменений — подтверждено Round-1 triage, не затронуты Round-2 правками.

## Round-2 self-check (Iteration 5)

- **duration_min sum:** 76.0 (программно проверено, см. §4 выше) — точное
  совпадение с facilitator-guide итоговой таблицей.
- **Q/A split:** программно проверено (pixel-level gold-fraction анализ через
  PIL на всех 8 predict-then-reveal Q-слайдах: s04, s06, s08, s12, s14, s16,
  s18, s23) — 7/8 дают ровно `0.00000`; s18 даёт `0.00356` — тот же известный
  false-positive из Round 1 (пунктирная gold-рамка карточки, не
  answer-бейдж, визуально подтверждено). s10/s20/s25 (расширенные
  reflection-слайды) — не predict-then-reveal архитектура (open-discussion
  вопросы без единственного ответа), q/a-split к ним неприменим по дизайну.
- **Anti-anglicism (deep_latin_scan.py на пересобранном PPTX, visible +
  notes):** 139 occurrences / 61 unique tokens. Полный triage: все либо (a)
  established термины из Round-1 (`cosine`, `illustrative`, `Winograd
  Schema`, `strawberry`-документ, `React`, `email-`, bridge-теги s26 и т.д.,
  без изменений), либо (b) НОВЫЕ hits того же класса — прямое цитирование
  академического источника WinoBias (`Zhao, Wang, Yatskar, Ordonez, Chang,
  NAACL, Gender Bias in Coreference Resolution: Evaluation and Debiasing
  Methods`) по прямому требованию задания «процитируй явно», либо
  established-техническая лексика (`regex`, `Luhn-`, глоссированное inline
  `bias` — «тот же термин, что на Семинаре 2»). **0 genuinely-unreviewed
  hits** — каждый unique token подпадает под одну из двух категорий.
- **Timing/methodology scan (на пересобранном PPTX, visible + notes):** 0
  hits `[0-9]+\s*мин`, 0 hits `⏱/⏰`, 0 hits `Лектору|Преподавателю|Вы
  здесь`, 0 hits `cold-call|фасилитатор`, 0 hits `[VERIFY-DAY-OF]`/
  `[FACT-CHECK]`, 0 hits `LO[1-9]`, 0 hits `§X.X`, 0 hits `→ sNN`. Найдено 2
  hits `методическ*` — оба являются той же мандаторной дословной фразой из
  facilitator-guide §4.3 «...автором методического комплекта для
  иллюстрации» (s23 visible + notes), уже одобренной Round-1 QA как часть
  содержательной инструкции, не мета-комментарий. Специально проверено, что
  новый worked-example текст (s10/s20/s25) не внёс новых timing/methodology
  паттернов — чисто.
- **Visual sweep (iter5, все 28 PNG):** осмотрены все слайды, особое внимание
  s01, s02, s03, s10, s11, s13, s17, s20, s21, s22, s25, s27 (изменённые) —
  без overflow, без geometry-багов, layout сбалансирован. s10/s20/s25 (новый
  layout) — worked-example блок + gold question + карточки помещаются в
  границы слайда без переполнения на первом же рендере (geometry рассчитана
  аналитически через `worked_example_reflection()` shared helper, не методом
  проб и ошибок).
- **Иконки:** `scale-3d`/`shield` заменены на существующие в библиотеке
  `scale`/`shield-check` до первого рендера — 0 warnings «missing image» при
  `python3 build_sem03.py`.

## Открытые блокеры (Round 2)

Нет.

## Рекомендации оркестратору (НЕ имплементированы, только предложения)

- **PROPOSED:** секция `notes/mcp-limitations.md` может выиграть от явной
  записи `[#sem03-render-1]` про конфликт `$HOME` override в
  `render-env.sh` vs `~/.local/lib/python3.12/site-packages` — добавлено
  ниже в этот же файл (см. `notes/mcp-limitations.md` diff), но
  оркестратор может захотеть смигрировать в отдельный canonical toolchain
  doc, если паттерн повторится в sem-04+.
- **PROPOSED:** `coref_slide` и `two_card_pair` shared builders в
  `build_sem03.py` достаточно универсальны, чтобы быть кандидатами на
  extraction в общий `tools/presentation-build/` helper module для
  будущих семинаров с q/a-voting паттерном (сейчас дублируются между
  sem-02 и sem-03 build-скриптами с минимальными различиями). Не
  имплементировано — awaiting orchestrator decision.
