# Лекция 3 — Visual-loop iteration log (часть 2)

Продолжение `iteration-log.md` (часть 1 достигла лимита 600 строк).

---

## v4.2 — точечный полировочный патч (issue #157 review, post-QA)

**Контекст:** дека уже прошла полный QA-цикл (presentation-critic +
student-simulator + reader-simulator + consistency-checker), все 4 отчёта —
APPROVE-WITH-POLISH / чисто, 0 P0. Ниже — единый проход по 8 точечным
находкам (не 5 отдельных visual-loop проходов на слайд — это разумные
точечные фиксы, не редизайн).

**Rendering environment note:** в этой сессии LibreOffice/`soffice`
недоступен в sandbox (не установлен, нет root/sudo для установки) → PNG
snapshot regen через `libreoffice --headless --convert-to pdf` +
`pdftoppm` физически невозможен. Верификация сделана через:
1. `python3 build_v3.py` — полная пересборка pptx (успех, 40/40 слайдов,
   без исключений).
2. Программная geometry-проверка через python-pptx: bounding-box каждого
   шейпа на каждом из 40 слайдов — 0 шейпов за границами canvas
   (13.333×7.5"), ручная сверка координат на предмет overlap для всех
   4 изменённых слайдов (s11/s12/s19/s25b) — coordinates пересчитаны
   вручную, 0 коллизий найдено (см. детали по каждому слайду ниже).
3. Deep latin-token scan (`tools/presentation-build/deep_latin_scan.py`)
   на extracted PPTX visible text — 334 occurrences / 176 unique
   (было 338/176 в v4.1) — профиль не изменился, новых англицизмов нет.
4. Scaffold/timing/methodology grep sweep на visible layer — 0 hits
   (включая проверку, что `[требует подтверждения]` действительно исчез
   с видимого слоя).

Визуальный PNG-инспекшн (обязательный шаг §5 pipeline) **не выполнен** в
этой сессии из-за окружения — это ограничение отмечено явно, не скрыто.
Рекомендация: при следующей сессии с доступным LibreOffice — прогнать
полный snapshot regen + визуальную проверку s11/s12/s19/s25b (минимум)
как inspection follow-up, до финального USER GATE sign-off.

### Применённые фиксы

**1. s19 (`build_s19`, build_v3.py) — P1 presentation-critic.**
Trust-warning блок (MCP-доверие, teal box справа): 3 буллета → 2. Оставлены
самые нагруженные по смыслу: (а) код в окружении / доступ к данным —
корневая причина риска, (б) описание попадает в контекст — носитель prompt
injection — конкретный вектор атаки. Убран третий («ещё одна граница
доверия и retention-политика») — он дублируется на s25 (ZDR-блок), поэтому
без потери контента. Bullet spacing увеличен 0.44"→0.52" на освободившееся
место. Хронология брендов (Anthropic 11/2024 / OpenAI 03/2025 / Google
04/2025): font дат 10pt italic → 11.5pt bold italic (тот же размер, что имя
бренда) для проекторной читаемости на заднем ряду.

**2. s19 footer — P2 student-simulator.**
«Числа экономии prompt caching и масштаб экосистемы MCP — в главе;
перепроверить ко дню лекции.» → «Актуальные цифры экономии и масштаб
экосистемы MCP — в главе методички.» Убран императив «перепроверить» (читался
как незакрытый TODO лектора) — теперь звучит как обычная справочная сноска
для читателя.

**3. s11/s12 (`build_s11`/`build_s12`) — P1 presentation-critic.**
Оба слайда использовали идентичный skeleton «N карточек + итоговая
плашка» подряд → визуально сливались. Content/текст не тронут. Визуальная
дифференциация s12 (не s11, чтобы не трогать уже устоявшийся s11):
- Базовая палитра карточек: `LIGHT`/`SURFACE` (primary blue, как у s11) →
  `TEAL_TINT`/`TEAL` (teal accent) — регистр «исключающие критерии /
  осторожность» вместо s11's «primary blue = признаки за RAG».
- Добавлен нумерованный gold/teal badge-кружок в левом верхнем углу каждой
  карточки (паттерн из s22b slot-badge) — силуэт, которого нет у карточек
  s11 (там карточки без номеров).
- Убран текстовый префикс «1./2./3.» из заголовка карточки (дублировался
  бы с новым badge) — сам номер теперь несёт badge, не текст.
- Card 3 (критерий «данные доступны live через API/MCP») остался
  gold-выделенным (как в v4.1) — это не тронуто, сохраняет «сильнейший
  критерий» семантику.
Geometry пересчитана и проверена: badge `x+0.20..0.52`, icon
`x+cw-0.76..cw-0.24`, title text box `x+0.66` шириной `cw-1.55=2.45"` —
между badge и icon, 0 overlap. Макс. 2 строки заголовка при 15pt bold в
2.45" (проверено оценкой char-width), помещается в 0.78"-box.

**4. s25b (`build_s25b`) — P1/P2 student-simulator + reader-simulator.**
OpenHands card note: `[требует подтверждения] вероятный кандидат на
«OpenClaw» из issue #157 — рабочая гипотеза по совпадению профиля, не
установленный факт` (134 симв, читался как незакрытый TODO/draft-синтаксис)
→ `рабочая гипотеза по совпадению профиля — вероятный кандидат на
«OpenClaw», не подтверждённый факт` (97 симв, органичная проза-hedge, тот
же italic 9.5pt что и раньше). Короче на 37 симв → без риска overflow в
существующем `nb_h=1.30` note-боксе (проверено).

**5. Определение agent-harness-registry — P1 reader-simulator.**
Термин используется как источник авторитетности данных на s22b/s22c/s22d/
s25b, нигде не объяснён. Добавлена inline-define строка в speaker notes
s22b (первое использование термина в разделе): «agent-harness-registry —
это независимый публичный реестр, который тестирует экипировку агентов
(память, skills, subagents, MCP) через live-eval бенчмарки на реальных
задачах, а не через вендорские самоотчёты о возможностях.» Не дублируется
на s22c/s22d/s25b — там термин уже используется коротко, читатель отсылается
к первому определению по порядку чтения. Notes word count после правки: 248
слов (в допустимом диапазоне 150-300).

**6. s22d (Tier легенда) — P1 reader-simulator.**
Speaker notes s22d дополнены: «На слайде системы помечены буквой Tier — это
рейтинговая категория реестра от A (лучшие результаты) до D (худшие) по
сумме бенчмарков live-eval; чем ближе к A, тем стабильнее система
показывала себя на полном наборе тестов.» Вставлено перед первым упоминанием
«Letta, Tier D» в тексте notes. Notes word count: 298 слов (на границе
допустимого диапазона 150-300, но в пределах).

**7. s25 (ZDR gloss) — P2 reader-simulator.**
Speaker notes s25 дополнены inline-define при первом развёрнутом упоминании
ZDR: «ZDR, Zero Data Retention, — это политика вендора не сохранять
содержимое запросов после обработки». Вставлено перед существующим
предложением про судебный приказ NYT v. OpenAI. Notes word count: 290 слов
(в допустимом диапазоне).

**8. Frontmatter-фиксы (housekeeping, не влияют на рендер).**
- `slides/s21-agent-loop.md`: `callback s07` → `callback s06` (2 места:
  `learning_goal` frontmatter + inline visible-body caption). Проверено:
  s07 не существует как файл/слайд; контент про faithfulness/human-validator
  живёт на s06 («chain-of-thought… человек проверяет результат, а не
  самообъяснение») — callback теперь указывает на реальный слайд.
- `slides/s29-human-validator-nanda.md`: `callback s07` → `callback s06`
  (2 места: `learning_goal` + `visual_brief` frontmatter). Тот же callback
  target fix.
- `slides/s30-bridge-homework-qa.md`: `(s28)` → `(s27)` (visible body,
  «Mini-apply задача B»). Проверено: «Разминка (задача B)» контент
  фактически построен в `build_s27` (grep по build_v3.py), не s28 — s28
  вообще не существует в деке. s30's md-файл — единственное место, где
  фигурировал `(s28)`; в build_v3.py эта ссылка не хардкожена, так что
  правка изолирована к markdown.
- `slides/s16-catastrophic-forgetting.md`: `chapter_ref: "§3.3` →
  `chapter_ref: "§3.4` (frontmatter). Проверено по chapter-part2.md TOC:
  «3.4. Провал: catastrophic forgetting» — точное совпадение с содержанием
  s16 («Провал: catastrophic forgetting»); §3.3 — это «Когда fine-tuning
  оправдан», другой раздел. Старая ссылка была стале.
Ни один из этих 4 паттернов (`callback s07`, `(s28)`, `§3.3` для s16) не
встречается в `build_v3.py` — все 4 фикса изолированы к markdown-источникам,
без изменения рендера.

### Пересборка + верификация

```
python3 build_v3.py
# → saved lec-03.pptx — 40 slides (успех, без исключений)
```

Post-build checks (все — программные, см. rendering environment note выше):
- python-pptx geometry sweep: 0 shapes out-of-bounds (40/40 слайдов).
- Manual coordinate re-derivation для s11/s12/s19/s25b: 0 overlaps.
- Deep latin scan: 334/176 (было 338/176) — не регрессировал.
- Scaffold/timing/methodology/bracket-leak grep: 0 hits на visible layer.

### Files touched

`rendered/build_v3.py` (4 функции: `build_s12`, `build_s19`, `build_s25b` —
+ docstring комментарий в `build_s11` region не менялся, только `build_s12`),
`rendered/lec-03.pptx` (rebuilt), `slides/s19-api-layer.md` (не трогался —
footer/bullets только в build-скрипте, markdown source этого слайда носит
характер spec, не 1:1 rendered text), `slides/s22b-agent-equipment.md`,
`slides/s22d-memory-failure.md`, `slides/s25-tool-attacks.md` (speaker notes
дополнены), `slides/s21-agent-loop.md`, `slides/s29-human-validator-nanda.md`,
`slides/s30-bridge-homework-qa.md`, `slides/s16-catastrophic-forgetting.md`
(frontmatter housekeeping).

**Не тронуто:** `rendered/lec-03.pdf` и `rendered/snapshots/*.png` — не
regenerated в этой сессии (LibreOffice недоступен, см. environment note).
Требуется regen перед финальным USER GATE, если snapshots используются
как evidence.

VERDICT v4.2: 8/8 запрошенных фиксов применены точечно, pptx пересобран
успешно, geometry programmatically verified 0 overlaps/out-of-bounds,
anglicism profile не регрессировал. **Открытый пункт:** визуальный
PNG-инспекшн (Anthropic vision-loop principle) не выполнен из-за
недоступности LibreOffice в этой sandbox-сессии — рекомендуется как
follow-up перед финальным sign-off. Не закоммичено (по инструкции).

---

## v5 (issue #185) — 40→51 расширение под 100 мин (2026-09-06)

**База:** deck v4 (40 слайдов) + chapter v3.0 (5 частей) + образец Лекции 2 v2.
**Spec:** `notes/lecture-3-rework/deck-v5-inventory-draft.md` (§3 ordered-list).

### Счёт слайдов — важное расхождение
Spec §9 указывал «54» — это **арифметическая ошибка** (дважды посчитаны
дивайдеры). Финализированный ordered-list §3 содержит ровно **51 слайд**
(46 content + 5 внутрираздельных дивайдеров, cover+map вводят Р0). Реализован
51 слайд; `build_v3.py main()` — `assert len == 51`. Задачный бриф просил
«assert 54» на основе §9; следую authoritative-таблице §3 = 51.

### NEW-слайды (14 builder'ов)
s01 (переделан в мем-хук «магическая пилюля»), s01b (Air Canada вынесен
отдельно), s05c (протокольные роли + STI), s07 (CoT faithfulness — split из
s06), s17 (FT-критерии — split из s14), s19b (экономика агента), s20 (MCP),
s22a_multi (мульти-агент p^n), s23b (каталог 10 классов провалов таблицей),
s23c (deep-dive 4 класса), s24 (data-security/ZDR), s28 (итоги-таблица),
s14 (переделан → дистилляция как отдельная техника), s30 (мост SDLC×AI).

### Divider-образы (6-tier acquisition, все Tier 1 Wikimedia)
- s04a нож (Chef's_knife) · s09 библиотека (George_Peabody_Library) ·
  s13a пульт (DiGiCo_S21_Mixing_Console) · s18 робот-рука
  (Factory_Automation_Robotics) · s25a кокпит (Cockpit_Convair_Coronado).
- `build_section_divider` расширен параметром `image_src`/`image_caption`/`tag`
  (giant white номер поверх фото + tag-чип «X разборов · Y провалов» БЕЗ минут).
- Attribution: `rendered/assets/web/attribution.md` (honest per-image log).

### Визуальный цикл (min 3 итерации на NEW/changed/divider)
- **Iter 1:** первичный рендер 51 слайда. Найдено: s01 timing «за 100 минут» в
  gold-callout (P0 — timing в visible); s01b callout overlap с ref-строкой;
  s14 pipeline 3-й бокс overflow за грань ocean-box; s22a_multi gold-подпись
  клипается gold-callout'ом; s24 bullets overlap summary-строкой.
- **Iter 2:** timing удалён; s14 геометрия (bw 3.30→3.05, gap 1.35→1.05,
  arrow 1.23→0.90) — 3 бокса вписались; s22a_multi (box lh 3.10→3.28, bar
  spacing 0.96→0.86, callout 5.02→5.22) — подпись не клипается; s24 (bullet
  spacing 0.66→0.56) — no overlap; s01b callout 6.06→5.98/h1.00→0.90.
- **Iter 3:** russification-pass + re-inspect — все NEW-слайды pass 5-Second
  Test (главный message = assertion), mass balance OK, gold ≥1×, «Что делать»
  callout на всех содержательных.

### Russification
- deep_latin_scan на visible: 342 unique — из них brand (Air Canada, MCP, RAG,
  PEFT, LoRA, QLoRA, MIT, Letta, Cognition, ZDR, CoT, AI) + glossed
  (fine-tuning, workflow, faithfulness, grounding, retrieval — glossary-locked)
  + английские source/case-имена (Anthropic verbatim quote на s22a_multi —
  намеренно EN) + pre-existing v4 термины.
- Русифицированы MY new-slide анлицизмы: self-rationale→самообъяснение,
  command injection→внедрение команд, path traversal→обход пути, hard cap→
  жёсткий потолок, kill-switch→аварийный стоп, hard boundary→жёсткая граница,
  supply chain→цепочка поставок, owns вывод→вывод принадлежит компании,
  Downstream→следующий агент, «system prompts are not security controls»→
  «системный промпт — не средство контроля безопасности».

### Compliance greps (visible layer)
- Timing grep (`N мин|Тайминг|⏱`): **0 hits**.
- Methodology/scaffold grep (`методическ|Лектору|LO[1-9]|§[0-9]|[for-slide|
  [VFY|→ sNN`): **0 hits** в visible body.
- `[VFY-day-of]` в speaker notes — только на source-citation строках (baked
  patch_notes.py, v4-конвенция) + s31 контакты (spec-requested); НЕ в narrative.

### Финал
- `rendered/lec-03.pptx` — 51 слайд, `assert len==51` pass, all ref anchors OK.
- Speaker notes 150-300 слов на всех NEW-слайдах (trim-pass для >300).

---

## v6 — issue #185 R-round (10 owner-комментариев #311-319 + правило)

Дек 56→55. Все правки к текущему деку (owner видел /51, применены к /56→/55).

### Правило #1 — БЕЗ превосходных форм (везде)
- Visible layer: 5 истинных суперлативов нейтрализованы в `build_v3.py`
  («ГЛАВНЫЙ МИФ»→«МИФ»; «тот самый поиск»→«тот же»; «не засорять главный»→
  «основной»; «не бери самый оснащённый»→«максимально оснащённый»; «Лучший
  RAG-2026»→«Сильный»). Плюс 14 сравнительных «лучше»/«улучшение» переведены
  нейтрально (предпочтительнее / вернее / выигрыш / докрутить), т.к. owner-grep
  `лучш` их ловит. **Independent PPTX-check: visible superlative (broad incl
  улучш) = 0.**
- Speaker notes: 2 fork-прохода → 0 суперлативов (broad+exact) в rendered notes.
  **Independent PPTX notes-check = 0.**

### #311 s01 — минимум текста + мем
- Убран верхний «ГЛАВНЫЙ»; текст сокращён; мем усилен: целая пилюля «ЧЕГО ЖДЁМ»
  vs разбитая «ЧТО ПРОИСХОДИТ» (+трещина, осколки) + «Точность не меняется.
  Меняется только тон ответа». Прямо показывает «это не так».

### #312 s01b — снесён
- Удалён из `builders`/`sids`/deck.yaml/deck-part3.yaml; `assert 56→55`; убран
  s01b-спецкейс в ref-loop. Air Canada остаётся кейсом §2 (s13, стр.21). Дек 55.
  `refs_lec03.py` s01b-записи — dead code (не в loop, harmless).

### #313 cover s02 — атрибуция курса снята + мем
- Убрано «3 курс ИУ6 · Модуль 1…». Добавлен flat-мем `_cover_pill_meme`:
  перечёркнутая пилюля + «"магической пилюли" не существует».

### #2/#317 атрибуции фото — сняты со всех
- Дивайдеры s04a/s09/s13a/s18/s25a: `image_caption=None` (само изображение
  оставлено). Hero s30: убран DEEP-бар + «Фото:…Wikimedia·CC-BY-SA».
  `assets/web/attribution.md` СОХРАНЁН (legal). **Independent PPTX-check:
  «Фото:|Wikimedia|CC-BY» в visible = 0.**

### #314/#315 s02a lecture-map
- Раздел 4 «Агенты» больше НЕ подсвечен (GOLD→MID, все карточки равнозначны).
  Gold-акцент перенесён на несущую линию (маркер перед подзаголовком).
- Раздел 0 нейтрализован: «Air Canada: неправильная архитектура…» → «постановка
  задачи: откуда берётся надёжность».

### #316 s03 — облегчён
- Тяжёлая схема «4 обвязки + hub» снята. Теперь лёгкое напоминание 2 понятий
  Лекции 2: одиночный вызов (single-shot) + семантический поиск на эмбеддингах.
  Два recap-бокса + gold-callout. Обвязки раскрываются по разделам.

### #318 s05 — мем вместо правых блоков
- Убраны «Добавляешь RAG →…» / «Добавляешь инструменты →…». Левая часть (один
  вызов + что знает модель) сохранена. Справа flat-мем `_s05_overengineering_meme`:
  «ДОСТАТОЧНО» (спокойное лицо + один вызов) vs «НА ВСЯКИЙ СЛУЧАЙ» (кривая башня
  наверченных коробок + gold «!»). Anchor [1] на нижнем gold-callout сохранён.

### #319 s06 — мем вместо текст-комментария
- Убран текст-блок «CoT-текст — это сгенерированная аргументация…». Мем
  `_s06_faithfulness_meme`: «говорит:» (аккуратная цепочка) ≠ «почему на деле:»
  (чёрный ящик «?», «скрыто — не аудировать»). Intro-anchor [2] и top-band [1]
  сохранены; правый gold-callout сохранён.

### Мемы (созданы)
- Все 4 (cover, s01-усиление, s05, s06) — чистые flat Ocean-иллюстрации через
  python-pptx shapes (стиль существующего s01-мема). Реальные мемы (imgflip
  доступен) НЕ использованы: атрибуции запрещены (#317), а flat-стиль держит
  бренд-консистентность и самодостаточность. Несут тезис слайда, не украшение.

### Russification (не регрессировать)
- Pre-existing транслит в notes (латентность/дефолт/апгрейд/продакшен) вычищен
  fork-проходом: латентность→задержка, дефолт→выбор по умолчанию, апгрейд→
  выигрыш, продакшен→промышленная эксплуатация. **Rendered notes translit = 0;
  visible translit = 0.** (Остатки в `## Body`/frontmatter source-md — не
  рендерятся, exempt.)

### Compliance (independent PPTX-grep, rendered layer)
- Superlative (broad): visible 0 / notes 0.
- Photo-attr / course-attr: visible 0.
- Timing / methodology / LO / §-ref / forward-ref / day-of markers: visible 0.
- Translit (продакшен/апгрейд/дефолт/латентност): visible 0 / notes 0.
- Gold ≥1×: все content-слайды (s31 Q&A — намеренно минимальный, как было).

### Build / render
- `/usr/bin/python3 build_v3.py` → «all ref anchors matched OK», 55 slides.
- Render 55 pages / 55 PNGs; визуальный цикл (≥3 прохода) на s01/cover/s02a/s03/
  s05/s06 + дивайдеры s04a/s09/s18 + hero s30 — overflow/читаемость OK.

---

## WAVE 2 (issue #196) — §2 RAG deepening: +6 слайдов (59 → 65)

Вставка ПОСЛЕ s10 (принцип RAG), ПЕРЕД s11 (когда RAG правильный). Новый порядок §2:
s09(div) → s-classic-rag → s10 → **s-rag-hybrid → s-rag-stack → s-rag-elastic →
s-rag-chunk1 → s-rag-chunk2 → s-rag-design** → s11 → s12 → s13.
Источник — глава §2.6–§2.11 (chapter-part7.md), каждое число С БАЗОЙ.

### Media plan (kind per slide)
- s-rag-hybrid (#23): schema-pipeline (BM25 + плотные векторы → RRF → cross-encoder), не мем.
- s-rag-stack (#24): comparison-matrix 5 движков + обвязки, не мем.
- s-rag-elastic (#25): meme-forward (Woman Yelling at Cat — судьба «нужна ли вектор-БД») + 3-ярусная граница.
- s-rag-chunk1 (#26): schema-matrix 6 стратегий + Contextual-полоса, не мем.
- s-rag-chunk2 (#27): meme-forward (Disaster Girl — anti-cargo-cult) + конфликтующие замеры + тихий провал таблиц.
- s-rag-design (#28): checklist/schema (пайплайн ingest→index + 4 карточки + каунтерфактуал), не мем.

### Новые мем-шаблоны (fresh, не переиспользованы)
- Woman Yelling at a Cat — imgflip id 188390779 → `s-rag-elastic-cat-ru.png`.
- Disaster Girl — imgflip id 97984 → `s-rag-chunk2-disaster-ru.png`.
Blank в `assets/web/memes-src/` (+ .url), русские подписи через PIL, attribution.md обновлён.

### Visual loop (≥3 итерации на каждый новый слайд)
- Iter 1: rendered w2-23..28. Inspected fill-rate/overflow/mass-balance/contrast.
  - (a) все 6 читаются, схемы/таблицы/мемы на месте, refs [N] сматчены.
  - (b) найдено: s26 «(следующий слайд про eval)» = soft forward-ref; s28 title «POC» =
    непереведённый акроним; `ops` ×3 (stack/elastic/design) = переводимый англицизм;
    s23 reranker-box текст касался нижней грани.
- Iter 2: (a) fix forward-ref → «метрики качества retrieval»; POC → «Прототип → продакшн»;
  ops → «эксплуатация» (×3); anchor s-rag-stack[2] обновлён под новый текст.
  (b) re-render 24/25/26/28 — чисто; anchors matched.
- Iter 3: (a) s23 reranker body укорочен («пару вместе», line_spacing 1.10→1.08, +«кандидатам»)
  → появился нижний зазор бокса. (b) re-render 23 — clean.

### 5-Second Test (после iter ≥3)
- s23: read = «гибрид = 2 ретривера → RRF → реранкер, приросты с базой» = assertion PASS.
- s24: read = «движок под масштаб; pgvector ~50M, Milvus 100M+» = assertion PASS.
- s25: read = «3 яруса: BM25 / встроенный гибрид / выделенная БД» = assertion PASS.
- s26: read = «стратегии чанкирования, дефолта нет» = assertion PASS.
- s27: read = «не карго-культи semantic; таблицы — тихий провал» = assertion PASS.
- s28: read = «прод — другая архитектура; <200k → RAG не нужен» = assertion PASS.

### Checklists
- Matrix/Grid (s24, s26): fill ≥75%, icons per row/tile, single-line headers, color-coding, ≥12pt — PASS.
- Process/Pipeline (s23, s28): RIGHT_ARROW-шейпы, ≤5 stages, owner-подписи (ingest gold=горло) — PASS.
- Meme-forward (s25, s27): мем несёт тезис суждения, ≈43-45% ширины, mass-balance — PASS.

### Anti-leak / russification
- Leak grep (visible body 6 слайдов): 0 timing/методология/LO/§X.X/→sNN/[VERIFY] после iter 2.
- Deep latin scan: остаток — brand/product names (Qdrant/Weaviate/Milvus/FAISS/pgvector/
  Postgres/LlamaIndex/RAGAS/ELSER…), established RAG-glossary (BM25/retrieval/embedding/
  dense/sparse/cross-encoder) + English source-titles в bottom refs (exempt). Narrative
  англ-лексика вроде «ops»/«POC» русифицирована.

### Counts / build
- 59 → 65. assert 65 (builders+sids). deck.yaml total_slides 65; deck-part2.yaml +6 spec;
  deck-part3 totals.slides 65 + by_section RAG list + ai_failure 18/65.
- Build: «deck spec OK — 65 slides» + «all ref anchors matched OK» + «saved … 65 slides».
- refs_lec03.py: +9 URLs, +6 SLIDE_REFS, +6 ANCHORS (все 12 новых [N] matched).

---

## WAVE 3 (#196) — §3/§4 deepening (65 → 67 FINAL)

### Scope
- §3 (+2): s-ft-cost (§3.6, comparison-table, no meme) после s13b; s-ft-eval
  (§3.7, meme-forward + границы) в конце §3.
- §4 (net 0): CUT s22c (память=RAG-scale) + s22e (presence-paradox musing);
  TRIM s19 (убран L2-recap structured output/function calling/prompt caching —
  оставлен L3: модель-как-компонент + tool use + MCP N×M→N+M + поворот доверия);
  REFRAME s22 → «Когда workflow: пять паттернов» (chaining/routing/parallel/
  orchestrator-workers/evaluator-optimizer, diagram, no meme); ADD
  s-agent-frameworks (§4.3c, comparison-table, no meme) + s-agent-when
  (meme-forward judgment) после s22a_multi по брифу.
- §5: s28 итог-таблица 9 → 12 строк (+гибрид+reranking, векторная БД, чанкинг,
  измерение обучения, агент-vs-workflow); font 11→9.5pt, читается без overflow.

### Мемы (2 fresh, ни один из 23 занятых)
- s-ft-eval: Left Exit 12 Off Ramp (imgflip 124822590) — «строгая оценка vs
  красивое число на бенчмарке».
- s-agent-when: Clown Applying Makeup (imgflip 141136560) — эскалация агентов
  без триггера → 0,95²⁰ ≈ 36% надёжности (p^n).
- attribution.md: WAVE 3 блок добавлен.

### Visual loop (мин 3 итерации на changed-слайдах)
- iter1: build+render+inspect 7 PNG (s-ft-cost/eval/s19/s22/frameworks/when/s28)
  — все чистые с первого прохода (table fill, gold-highlight, meme-thesis,
  refs [N]).
- iter2: s22 card-body/«когда»-strip tight overlap (card 3 Parallelization) →
  body 10→9.5pt, height 1.12→1.08, title y-nudge; re-render — зазор чистый.
- iter3: latin-scan → russify «риск adoption» → «риск при внедрении»;
  «Human eval» → «Оценка людьми (human)»; «rubric» → «разметка». Consistency:
  workflow/faithfulness/eval/harness/reranking уже в approved Wave1/2 деке —
  конвенция сохранена, не введена новая.

### Counts / build
- 65 → 67 (assert 67). deck.yaml version v6.1 + total_slides 67;
  deck-part2 (+s-ft-cost, +s-ft-eval); deck-part3 (+s-agent-frameworks,
  +s-agent-when; CUT s22c/s22e; totals.slides 67; by_section §3=9/§4=18;
  ai_failure_judgment 22/67 ≈ 32,8% strict-in — порог ≥30% превышен без waiver).
- Build: «deck spec OK — 67 slides» + «all ref anchors matched OK» +
  «saved … 67 slides».
- refs_lec03.py: +6 URLs (thinkingmachines_lora, gsm1k, benchmark_contamination,
  langgraph, tau_bench, anthropic_multiagent), +4 SLIDE_REFS новых, ANCHORS+
  NOTES_ANCHORS для 4 новых + переписаны для trimmed s19 / reframed s22;
  patch_notes.py: все markers matched (2/2 × 4 new, 1/1 × s19/s22).
- Cuts verified: build_s22c/s22e не в main() builders/sids; s22c/s22e не
  рендерятся (67 страниц, не 69). Dead builder-функции оставлены (harmless).
- Anti-leak grep 7 changed-слайдов: 0 timing(«мин.»=«минимум» false-pos)/
  методология/LO/§X.X/→sNN/[VERIFY].

---

## v6.4 owner-review — 4-slide revision (2026-09-16)

Branch: issue-lec03-v4-deepen. Builder: build_v3.py. 4 slides touched: 37 (s-ft-cost),
50 (s22), 52 (s-agent-when), 55 (s22d). Slide count unchanged at 67. Build: all ref
anchors matched OK; both asserts (67 builders / 67 sids) pass.

### Slide 37 (s-ft-cost) — REVERT to axes×methods with relative params
- FIX: replaced the D2 by-model-size table (7B/13B/70B/405B columns) with the old
  6-rows-×-5-methods form, RELATIVE values (Full-FT = базлайн ×1). Recovered structural
  scaffold from `git show 1d98414:...build_v3.py` lines 2003–2062, then swapped row set +
  values to relative ones per owner brief.
- Iter 1: inspected PNG — table fits ocean box, no overflow, LoRA gold column clear,
  gold_callout carries [1]+[2] markers. Multi-line cells wrap with slight continuation
  indent (cosmetic, in-bounds).
- Iter 2/3: re-inspected after rebuilds — stable, no overflow. 5-sec test PASS
  (main message = "training cost is order-of-magnitude; LoRA is cheap default" = assertion).
- Anchors: [1] "7B-LoRA <$10 — дешевле фронтир-претрейна ($61–92M) на ~7 порядков" and
  [2] "65B влезает в одну 48-ГБ карту" both re-included verbatim in gold_callout; matched OK.
- Notes rewritten (362w) to relative-params framing; dropped "функция размера модели"
  / 7B/13B/70B/405B narrative. Источники [1][2] intact.

### Slide 50 (s22) — evaluator-optimizer self-explanatory
- FIX: 5th card body → generator↔critic loop wording; when → translation example.
- Iter 1: PNG showed card-5 body (8.6pt) + "когда:" box overflowing (last lines clipped,
  collided with card bottom).
- Iter 2: dropped gold-card body to 8.4pt, trimmed body wording, enlarged gold-card
  "когда:" box (kbh 0.98 vs 0.66) + 8.4pt. Re-inspected: all card-5 text in-bounds, box
  contains full 4-line "когда:" text. Other 4 cards unchanged/clean.
- Iter 3: final squint check PASS, no overflow.
- Notes deepened 247w → 418w; all 5 patterns walked with WHAT+WHEN+concrete example;
  evaluator-optimizer explained from scratch (generator↔critic, draft-translation loop).
  Источник [1] intact.

### Slide 52 (s-agent-when) — named 3 multi-agent conditions + examples
- FIX: rung-3 label → "Мульти-агент — под конкретный кейс"; right side repurposed to a
  gold box listing the 3 named conditions each with a concrete example; Cognition/Anthropic
  box kept smaller; pointer strip states "вне этих кейсов … неверный инструмент (×15 токенов),
  числа на следующем слайде".
- Iter 1: PNG — 3 conditions visible, but Cognition box text overflowed (tail
  "быстрее коллапс" clipped, overlapping gold callout).
- Iter 2: recomputed right column to fit 1.74→6.06: conditions box 2.98 tall (spacing 0.80,
  10.5/9.5pt), Cognition box ly+3.06 h1.24 at 9pt, text trimmed. Re-inspected: Cognition tail
  fully in box, [2] marker inside; [1] marker on "ЧТЕНИЯ" visible; no overflow.
- Iter 3: final check PASS.
- Anchors [1] "параллельте независимые ЧТЕНИЯ" / [2] "быстрее коллапс" kept verbatim; matched.
- Notes updated (412w) naming the 3 conditions + examples; anchors "магии координации",
  "быстрее коллапс, а конкретные множители" intact; Источники [1][2] intact.

### Slide 55 (s22d) — scope = specially-organized persistent memory
- FIX: title → "Специально организованная память агента — не всегда во благо." (24pt);
  subtitle → distinguishes in-session context ("помнит всегда") from added persistent
  cross-session layer (mem0/Cognee/Letta/Memory Tool). Left/right case boxes nudged
  (ly 1.86→1.92, lh 4.05→3.99) to clear 3-line subtitle. All failure data unchanged.
- Iter 1: PNG — title one line, 3-line subtitle clears boxes, [1] marker after "нет",
  both boxes clean, no overflow. (No further fix needed.)
- Iter 2/3: re-inspected after neighbour rebuilds — stable. PASS.
- Anchor [1] "Независимая проверка показывает: иногда — драматически нет" kept verbatim in
  subtitle; matched. Notes (352w) got 3 scope-clarifying sentences up front;
  "независимого реестра" anchor + Источник [1] intact.
