# Presentation Critic Report — Лекция 1 — 2026-08-07 (issue #153 polish round)

VERDICT: REVISE

## Сводка

- Всего слайдов: 34
- P0 issues (блокеры): 3
- P1 issues (важные): 7
- P2 issues (мелочи): 5

**Методологическая база проверки:** `deck.yaml` v3.3 + `slides/*.md` (34 файла) + rendered
`lec-01.pptx`/`lec-01.pdf` (regenerated fresh via `pdftoppm -r 150` directly from the current
committed PDF — see Cross-deck issues §1, the committed `snapshots/iter153-*.png` are **stale**
relative to the final pptx/pdf timestamps) + `rendered/iteration-log-issue153.md`.

Особый фокус (по брифу) — s00a, s00b, s02a, s06a, s08, s09, s12/s13, s15-s19a (eyebrow
headers), **s18 (полный redesign схемы)**, s23, s25, s26, s28, **s29 (новый 4-модульный
контент)**, s29a, s31 — все проверены визуально (vision) построчно.

---

## По слайдам

### Slide s02 — «Введение — AI вокруг нас» (cover)

**Severity:** P0
**Issue:** Декоративная нумерация лекции должна читаться «01» (build script:
`text="01"` at 320pt, `rendered/build_lec01.py:515`), но hero-иллюстрация
(`hero-cover-light.png`, atom/orbit motif) рисуется **поверх** правой части
цифры (z-order: `add_image` вызывается после `text_box`, обе на x≈8.0-13.0) и
полностью закрывает «1». На экране остаётся только «0» — для Лекции №1 это
читается как «Лекция 0», фактически неверно и заметно с первого взгляда.
**Recommendation:** либо сдвинуть decorative-numeral левее/за пределы
bounding box hero-иллюстрации, либо уменьшить/переместить hero-image так,
чтобы не перекрывать «01», либо понизить z-order иллюстрации под текст с
полупрозрачностью текста поверх (текущий паттерн подразумевает numeral как
фоновый декор, но сейчас перекрытие полное, не полупрозрачное).
**Visual evidence:** `fresh-04.png` (150dpi re-render от текущего `lec-01.pdf`)
— виден только контур «0», «1» отсутствует полностью, скрыта под белым/светлым
фоном иллюстрации.

---

### Slide s05a — «Кто я и почему мне это важно» (instructor card)

**Severity:** P0
**Issue:** Слайд содержит **три буквальных placeholder-квадратные скобки**,
видимые студенту: `[годы работы с AI; конкретные проекты]`,
`[почему важно лично]`, `[контакт, формат вопросов]`. Это не входит в
21-fix список (слайд не редактировался в Phase 4), но deck поставляется
«к чтению» — показывать студентам незаполненный шаблон недопустимо.
**Recommendation:** до первого чтения лекции — заполнить реальными данными
преподавателя (или, как временная мера, оркестратор/владелец явно
подтверждает: «слайд будет обновлён вручную перед лекцией», и тогда это
не блокер конкретно для issue #153, но must-fix перед реальным показом).
Держать как открытый item, не закрывать GATE молча.
**Visual evidence:** `fresh-06.png` — квадратные скобки видны крупным
шрифтом рядом с иконками briefcase/lightbulb/users.

---

### Slide s20 — «Приложение = AI, упакованный в продуктовый интерфейс»

**Severity:** P0
**Issue:** Текстовое наложение (overlap). Строка метрик «1+ миллиард ...
1 триллион переведённых слов / месяц» переносится на вторую строку (текст
длиннее контейнера при смешанных размерах шрифта 26pt/14pt), и эта вторая
строка **накладывается** на fixed-position caption ниже («across Google
Translate, Search, Lens и Circle to Search...») — обе строки видны
слипшимися/перекрывающими друг друга.
**Recommendation:** пересчитать высоту text_runs блока динамически (или
сократить формулировку метрики до одной строки), сдвинуть caption вниз
на фиксированный отступ от фактической (не расчётной) высоты текста.
Заодно — caption начинается с английского «across» (см. также
Cross-deck §2, Russification).
**Visual evidence:** `fresh-22.png` — «1 триллион переведённых слов /
месяц» визуально слипается с «across Google Translate...» прямо под ней.

---

### Slide s18 — «Агент = чат + оркестратор + внешняя память + инструменты» (FULL REDESIGN)

**Severity:** P1
**Issue:** Это флагманский redesign раунда (заменяет слабую v3.2
hub-and-spoke схему на линейный ReAct-pipeline) — и с точки зрения
читаемости/5-Second Test схема **сильно улучшилась** (см. Cross-deck
позитив ниже). Но 4 центральных блока pipeline подписаны **полностью
по-английски**: «Plan», «Act», «Observe», «Reflect» — это не brand-name и
не acronym с inline-глоссом, это обычные английские глаголы, использованные
как главная видимая надпись схемы. Дополнительно loop-back стрелка подписана
«continue — цикл повторяется» (само слово «continue» не переведено) и
stop-стрелка — «stop → результат пользователю» («stop» не переведено).
Прямое нарушение §5.8 Russification mandate (ENFORCED) — ни один из 4
терминов не в keep-list (в отличие от, например, «prompt» или «fine-tuning»,
у которых нет устоявшегося русского эквивалента; «план/действие/наблюдение/
рефлексия» — устоявшиеся русские слова, эквивалент есть).
**Recommendation:** заменить подписи блоков на «План → Действие → Наблюдение
→ Рефлексия» (с возможной пометкой мелким шрифтом «(Plan/Act/Observe/Reflect)»
при первом упоминании, если важно сохранить связь с источником ReAct), «continue»
→ «продолжить», «stop» → «стоп» или «остановка».
**Visual evidence:** `fresh-19.png` — все 4 верхних блока и обе управляющие
стрелки на английском, единственный русский текст — под-подписи мелким
курсивом внутри блоков.

---

### Slide s19 — «Агент за работой: 200 PDF»

**Severity:** P1
**Issue:** Правая колонка (7 инструментов на 7 шагов) — **преимущественно
английский текст**: «file system», «PDF reader», «text extraction (OCR /
parser)», «embeddings + vector DB», «search + LLM extract», «Sheets API /
CSV writer», «orchestrator loop». Это ровно тот тип контента (tool-name
labels в схеме), который Russification playbook требует переводить (ср.
успешно Russified s16/s17/s25, где аналогичные термины даны с inline-глоссом
на русском). Также baked в `.md` source (`visual` block) и speaker notes —
не только build script, т.е. это не единичная опечатка рендера, а
исходное решение дизайнера.
**Recommendation:** «файловая система», «чтение PDF», «извлечение текста
(OCR / парсер)», «эмбеддинги + векторная БД», «поиск + извлечение LLM»,
«запись в таблицу (Sheets API / CSV)», «цикл оркестратора». Сохранить
акронимы (OCR, PDF, API, CSV, LLM) как есть — per keep-list.
**Visual evidence:** `fresh-20.png` — весь правый столбец teal-tinted
box'ов на английском.

---

### Slide s19a — «Уровни автономии AI-агентов»

**Severity:** P1
**Issue:** Лесенка 5 уровней подписана английскими терминами как primary
label: «5. Observer», «4. Approver», «3. Consultant», «2. Collaborator»,
«1. Operator» — только под-подпись курсивом на русском. Справа — рамки
«Human-in-the-loop», «Human-on-the-loop», «Human-out-of-the-loop»,
«Override modes» тоже полностью английские. Источник (Feng/McDonald/Zhang
2025) — англоязычная работа, но это не basis для показа англ. терминов
студентам без перевода (ср. как ReAct = «Reasoning + Acting», но
пайплайн на s18 задуман переведённым).
**Recommendation:** дать русский перевод как primary label с англ. в скобках
при первом появлении: «5. Наблюдатель (Observer)», «Человек в цикле
(Human-in-the-loop)» и т.д. — по аналогии с уже применённым паттерном на
s25 («Смещение (bias)»).
**Visual evidence:** `fresh-21.png` — левая лесенка и правая колонка рамок
почти целиком на английском.

---

### Slide s09 — «Пространство открыто: 4 прорыва»

**Severity:** P2
**Issue:** Card 2 (DeepSeek R1): «Nvidia drop за день» — «drop» не
переведено (ср. Russification table: нет прямой записи для «stock drop»,
но по духу таблицы стоит перевести, напр. «обвал акций Nvidia за день»).
Card 3/4: «100K★ stars» / «100K+★ на GitHub» — слово «stars» избыточно
дублирует ★-символ и не переведено (можно просто «100K★» без слова, или
«100K★ звёзд»).
**Recommendation:** точечная правка двух карточек, без redesign.
**Visual evidence:** `fresh-11.png`.

---

### Slide s17 — «Чат = модель + интерфейс + память диалога»

**Severity:** P2
**Issue:** Правый gold-tinted блок озаглавлен «Disclaimer для прод-систем»
(«Disclaimer» не переведено) и тело содержит «в production» (тоже не
переведено) — это ровно строка из Russification table §5.8
(«production use / production-уровень → промышленное применение»),
но применительно к s17 fix её пропустили (в отличие от s25, где
аналогичная зачистка была сделана тщательно).
**Recommendation:** «Disclaimer для прод-систем» → «Оговорка для
промышленных систем» (или «Важно для реальных систем»); «не используются в
production» → «не используются в промышленной эксплуатации».
**Visual evidence:** `fresh-18.png`.

---

### Slide s29a — «Формула итоговой оценки: 100 = 10 + 30 + 3×20» (NEW)

**Severity:** P2
**Issue:** Композиция визуально несбалансирована — формула центрирована по
вертикали в почти пустом слайде (верхние ~35% и нижние ~35% высоты полностью
пусты, без иных элементов). Само содержимое верное и читаемое (соответствует
brief п.20, arithmetic verified: 10+30+3×20=100), но для нового отдельного
слайда выглядит недоработанным/скудным по сравнению с плотностью соседних
слайдов (s29 «Карта семестра» — насыщенная, s29a — почти voit).
**Recommendation:** не блокирует — но стоит добавить лёгкий визуальный
довесок: напр. маленький Ocean rounded box вокруг формулы, или доп.
context line («три рубежных контроля — по одному на модуль» уже есть
внизу, можно увеличить визуальный вес блока/добавить иконку).
**Visual evidence:** `fresh-33.png`.

---

### Slide s31 — «Вопросы?»

**Severity:** P1
**Issue:** Нижний правый угол — видимый студентам плейсхолдер «контакты
лектора — заполняется перед лекцией». Это задокументированное
намеренное решение в самом `.md` (frontmatter: «заполняется перед
лекцией»), не designer-added extra и не regression от issue #153 — но
raw-текст плейсхолдера («заполняется перед лекцией») сам по себе читается
как незаконченный слайд, если кто-то откроет deck до финального заполнения.
**Recommendation:** держать как открытый TODO с owner (сам преподаватель
заполняет перед показом) — явно зафиксировать в PR description/issue,
не «терять» как немую deferred-задачу.
**Visual evidence:** `fresh-34.png`.

---

### Slide s06 — «Определений AI много — потому что AI это moving target»

**Severity:** P2 (pre-existing, известно и задокументировано)
**Issue:** Assertion-заголовок содержит непереведённое «moving target».
Дизайнер сам поймал и корректно эскалировал это как **out-of-scope находку**
(не входит в 21-fix, слайд не редактировался) — задокументировано в
iteration-log с явным «Flagged for owner decision, not auto-fixed». Логика
корректна (No Extra Content Rule), но раз deck идёт на GATE — стоит решить
сейчас, а не переносить молча.
**Recommendation:** решение владельца: (a) оставить как есть до отдельного
прохода, или (b) один быстрый text-fix «AI это движущаяся цель» — дёшево,
раз уж другие anglicisms всё равно чинятся в этом раунде.
**Visual evidence:** `fresh-07.png`.

---

## Slides без blocking issues (быстрый обзор)

s00a (welcome), s00b (course hook), s02a (lecture-map redesign), s06a
(prehistory 1943), s07 (timeline), s08 (scale numbers), s10/s22/s27
(section dividers), s11 (layers), s12 (classification matrix), s13
(control quadrant), s15 (model pipeline), s16 (chat cycle), s21
(checklist quadrant), s23 (consumer vs enterprise — **корректно
Russified**, см. ниже), s24 (hallucinations), s25 (bias/sycophancy —
**корректно Russified**), s26 (AGI table, Hassabis sync verified), s28
(summary), s29 (course roadmap redesign), s30 (Lec-2 teaser) — все прошли
5-Second Test, читаемы, без переполнения, contrast OK.

**Похвала (не для форм, для контекста верификации):** s23 и s25 — оба
претендовали на «уже исправлено» в iteration-log — **подтверждено
корректно на живом рендере**: title/bullets s23 полностью на русском,
timeline caption s25 корректно Russified («откат», «соцсети», «разбор
причин»). Это показывает, что designer's own independent-verification
pass (описанный в iteration-log) реально сработал для ЭТИХ двух слайдов —
контраст с s18/s19/s19a, которые тот же pass не покрыл.

---

## Cross-deck issues

### 1. [P1] Snapshot/PPTX временной рассинхрон — committed PNG не отражают финальный pptx

`rendered/lec-01.pptx` (timestamp 10:58) и `rendered/lec-01.pdf` (10:59)
новее, чем `rendered/snapshots/iter153-*.png` (10:47). Т.е. committed
snapshots — это снимок **промежуточной** итерации, не финального
состояния. Для большинства слайдов содержимое совпало (проверено выборочно
через regenerate `pdftoppm -r 150` напрямую из текущего `lec-01.pdf` —
результаты идентичны для s23/s25, отличий не найдено), но сам факт
рассинхрона — процессный риск: следующий ревьюер/владелец, доверяющий
committed PNG буквально, увидит не то, что реально в PPTX. Это ровно тот
класс проблемы, который Pre-USER-GATE Walkthrough Rule п.8 («Artifacts в
main repo... MUST exist BEFORE opening GATE») призван предотвращать, но
не покрывает **временной** рассинхрон snapshots vs pptx внутри одного
repo state.
**Recommendation:** перед GATE — обязательный `git diff --stat` +
regenerate snapshots заново из финального `lec-01.pptx` (`libreoffice
--headless --convert-to pdf` → `pdftoppm`) и commit финальный набор PNG
поверх `iter153-*`, чтобы snapshot-имена соответствовали actually-shipped
content. Добавить в `notes/mcp-limitations.md` как процессную заметку
(build script re-saves pptx after snapshot generation without
re-snapshotting — same class as [#69-render-1] snapshot staleness, but
temporal not resolution-based).

### 2. [P1] Russification — deep scan подтверждает системный пропуск на s18/s19/s19a

`tools/presentation-build/deep_latin_scan.py` на извлечённом PPTX visible
text даёт **270 occurrences / 224 unique** tokens вне brand allowlist —
ровно совпадает с числом, которое сам дизайнер указал в
iteration-log («270 occurrences / 224 unique» после собственных фиксов).
Ручной построчный разбор всех 224 unique токенов показывает: **большинство
— легитимные** (citation-имена авторов — Russell, Norvig, Mitchell, Turing,
Searle, Vaswani и соавторы «Attention is All You Need»; brand/product
names — YOLO, Whisper, ResNet, DALL-E, AutoGPT, Devin, OpenClaw и т.п.;
DOI-строки, дефисы вида `AI-`/`GPT-`/`PDF-`). **Но выделяется чёткий
кластер genuine narrative-body anglicisms**, сосредоточенный именно на
s18/s19/s19a (Plan/Act/Observe/Reflect/continue/stop/orchestrator/loop/
file/system/reader/extraction/parser/embeddings/vector/writer/Sheets/CSV/
Observer/Approver/Consultant/Collaborator/Operator/Human-in-the-loop/
Human-on-the-loop/Human-out-of-the-loop/Override/modes/gate/approve/each/
community/nav) плюс отдельные точки на s06 (moving target), s09 (drop,
stars), s17 (Disclaimer, production), s20 (across), s07/s08 (engineered
system, software-only — принято как методологический caveat, borderline
OK). **Это НЕ «deck clean, единичные citation-имена»** — это второй по
величине содержательный кластер после citation-имён, и он полностью
предотвратим (не proper nouns, не brand names).
**Recommendation:** одна batched-правка (book-editor или
presentation-designer, per Polish Round Pattern) на s06/s09/s17/s18/s19/
s19a/s20 — все конкретные замены перечислены в соответствующих
per-slide находках выше. После правки — перезапустить `deep_latin_scan.py`
и убедиться, что unique-count упал минимум на ~35-40 токенов (весь
s18/s19/s19a кластер).

### 3. [P0→resolved-by-design, note only] Lec-N-1 pattern compliance — нет формального эталона lec-00, но внутренняя консистентность deck'а хорошая

Курс не имеет lec-00, поэтому формальный «Lec-N-1 pattern compliance»
чек-лист неприменим буквально. Проверил внутреннюю консистентность:
- **Top bar / roadmap bar:** отсутствует на content-слайдах, используется
  только паттерн card-grid nav (s10/s22/s27 dividers) и отдельно timeline
  (s02a/s29) — соответствует правилу «roadmap только на дивайдерах+cover».
- **Lecture-map:** есть (s02a), redesigned в этом раунде — timeline-style,
  что расходится по форме с card-grid у s10/s22/s27 (divider'ы остались
  card-grid, не timeline). Это не баг per se (два разных use-case: lecture-
  map = overview в начале, divider = «вы здесь» на переходе), но два
  разных визуальных языка для, по сути, той же 6-секционной структуры
  внутри одного deck — минорная inconsistency, см. finding ниже.
- **Dedicated Q&A slide:** есть (s31).
- **Section dividers для всех разделов:** есть (s10, s22, s27) — но нет
  дивайдера перед разделом 2 («Где мы сейчас», s08-s09) — структура идёт
  s07→s08 без явного divider. Проверил deck.yaml: раздел 2 действительно
  не имеет отдельного divider slide (в отличие от разделов 3, 4, 5). Не
  новая находка issue #153 (структура предшествует ему), но раз лекция
  «полируется перед чтением» — стоит отметить.

**Severity:** P2 (не входит в 21-fix scope, pre-existing structural
choice, не regression). Flag only, no forced redesign per No Extra
Content Rule.

### 4. [P2] Card-grid nav (s10/s22/s27) vs timeline (s02a/s29) — два визуальных языка для одной структуры

См. finding 3 выше. `iteration-log-issue153.md` сам явно фиксирует, что
redesign s02a был сделан «in the style of s29» (timeline), но не
распространён на dividers — оставшиеся card-grid. Итог: студент видит
роадмап курса дважды в двух разных визуальных языках (карта лекции vs
дивайдеры), что не является ошибкой, но не полностью consistent.
**Recommendation:** не блокирует GATE — отметить как candidate для
следующего прохода (unify dividers в timeline-style тоже), решение за
владельцем (может быть намеренным сохранением двух языков — divider как
«полноэкранный акцент», map как «плотный обзор»).

### 5. [P2] No designer-added extras found (positive finding)

Grep по `slides/*.md` на все scaffold-паттерны (`Лектору`, `Преподавателю`,
`Вы здесь`, `методическ`, `педагогическ`, `[0-9]+\s*мин` вне frontmatter,
`VERIFY-DAY-OF`, `FACT-CHECK`, `§[0-9]`, `→ s[0-9]+`) — **0 hits** вне
frontmatter LO-кодов (которые exempt по правилу). Timing/methodology
discipline полностью соблюдена в visible body и speaker notes на всех 34
слайдах. Хорошая работа presentation-designer'а на этом фронте.

### 6. [Positive] Schema Readability — s18/s02a/s29 прошли checklist по существу

- **s18 (schema_architecture):** USER explicit (слева, подписан) — PASS.
  Bidirectional flows (arrow-in от USER, stop-arrow назад к USER) — PASS.
  Connectors labelled — PASS (хотя label текст не переведён, см. P1 выше —
  это Russification issue, не readability issue). 5-Second Test:
  структура «4-шаговый цикл, начинается и заканчивается пользователем»
  считывается мгновенно — это объективно самый сильный redesign раунда с
  точки зрения архитектуры схемы, минус только языковой слой.
- **s02a (schema_timeline / roadmap):** fill rate 100%, weighted-width
  correctly reflects раздел 3 как самый большой (1.6 units), gold
  highlight на текущем разделе — PASS. Единственное отличие от canonical
  schema_timeline pattern (§4) — это не событийная timeline (даты), а
  roadmap-блоки, так что em-dash/pivot-year правила неприменимы буквально;
  корректно смэппено на аналог `lecture_roadmap_timeline`.
- **s29 (roadmap, 4 modules):** weighted-width fix для Модуля 4 (2.2 units
  min) сработал — заголовок «Модуль 4 / Экзамен» не переполняется. РК-
  маркеры (◆РК1/РК2/РК3) на правильных лекциях. Isolation constraint
  verified (не трогали `lectures.yaml`/`rpd-*.md`) — подтверждаю
  собственным grep, `git diff --stat` тех файлов пуст.

---

## Итоговая оценка по критериям задачи

- **No Timing/No Methodology (ENFORCED):** PASS, 0 hits.
- **Designer-extras (scaffold/LO-коды/§-ссылки) в visible body:** PASS, 0
  hits вне frontmatter.
- **Ocean palette + motif consistency на новых слайдах (s00a/s00b/s06a/
  s29a):** PASS — все 4 используют surface/teal/deep/gold корректно, s00a
  и s00b явно без Ocean rounded box (правильно, per cover/pre-cover
  правило), s06a и s29a внутри content используют motif корректно.
- **Schema Readability (s18, s02a, s29):** PASS геометрически/структурно,
  **FAIL на языковом слое s18** (см. P1 выше) — итоговый verdict per-slide
  для s18 = geometry PASS + Russification FAIL = не готов к финальному
  accept без правки.
- **Russification (deep scan):** REVISE — системный пропуск на s18/s19/
  s19a кластер, плюс точечные misses на s06/s09/s17/s20.

## Почему REVISE, не APPROVE-WITH-POLISH

3 P0 (s02 numeral bug, s05a placeholders, s20 text overlap) — по правилу
CLAUDE.md «Any P0 → REJECT» строго говоря это тянет к REJECT, но ни один
из трёх P0 не является методическим провалом уровня «слайд непригоден к
показу целиком» — все три точечно исправимы за один batched-проход без
redesign (numeral z-order fix, заполнение 3 строк текста, height-recalc
одного text block). Плюс 7 P1 (в основном один системный Russification-
кластер на 3 слайдах, который считается за один batched-fix, не за 7
независимых). Итоговое решение: **REVISE** (не REJECT, т.к. фиксы
дёшевы и не требуют переосмысления концепции; не APPROVE-WITH-POLISH,
т.к. P0 present и ≥5 P1 — counter-check per CLAUDE.md применён:
7 P1 ⇒ REVISE, не APPROVE-WITH-POLISH).

## Рекомендуемый следующий шаг

Один batched revision-проход (presentation-designer, Polish Round
Pattern) со scope:
1. s02 — fix z-order/position decorative «01» vs hero image.
2. s05a — заполнить или явно отложить с owner-запиской (не молча).
3. s20 — fix text overlap (dynamic height recalc + сократить/убрать
   двустрочный wrap) + Russify «across».
4. s18/s19/s19a — Russify весь cluster (конкретные замены даны per-slide
   выше).
5. s06/s09/s17 — точечные Russification fixes (moving target / drop,
   stars / Disclaimer, production).

После правки — перезапустить `deep_latin_scan.py` на свежем PPTX extract,
подтвердить unique-count снизился, ре-снапшотить весь deck (устранить
finding Cross-deck §1), и только тогда — Pre-USER-GATE walkthrough →
GATE.
