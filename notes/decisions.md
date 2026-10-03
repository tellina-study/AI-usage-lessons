# Decisions Log

Журнал перерос лимит в 600 строк, поэтому старые периоды вынесены в отдельные файлы. Новые записи добавляются **сюда**, в конец.

## Части журнала

- [Март — 17 мая 2026](decisions-2026-03-05-lectures-1-6.md) — становление конвейера, лекции 1–6, правило ≥30% про провалы, пайплайн презентаций.
- [21 мая 2026](decisions-2026-05-lectures-8-11.md) — рефлексии лекций 8–11, три ENFORCED-правила, глубина главы.

## 2026-08-08 — Module boundary shift (Модуль 1: 1–8→1–6, Модуль 2: 9–12→7–12)

Owner подтвердил сдвиг границ модулей курса (виден на ручной правке финального слайда s03 `library/seminars/sem-01/`). Обновлены `course-plan.md`, `course-plan-seminars.md`, `catalog/manifests/lectures.yaml` (issue tracking TBD).

- **Новые названия модулей:** Модуль 1 — «Теоретико-методологические основы систем искусственного интеллекта и их применение в цифровых и инженерных отраслях» (лекции 1–6). Модуль 2 — «Искусственный интеллект в специализированных отраслях с высокой ценой ошибки: от медицины и креативных индустрий до высокотехнологичного производства и систем двойного назначения» (лекции 7–12). Модуль 3 не менялся.

- **Renumbering границы модуля обнажил скрытый content gap, не создал его.** Задача владельца формально требовала ДВЕ вещи, которые для слота «Семинар 6» конфликтуют: (а) «семинары зеркалят лекции 1:1» (Л6 остаётся в модуле 1, значит С6 = его практика) И (б) «Рубежный контроль 1 переезжает на Семинар 6» (слот С6 теперь = контроль). Агент (course-curator) НЕ разрешил конфликт молча — применил буквальное прочтение (б) для слота С6, сохранил старый контент С6 текстом в `[NEEDS-OWNER-CONFIRMATION]` блоке в том же каноническом файле, и явно пометил, что слот «Семинар 8» (ранее занятый текстом RK1, теперь освобождённый) логически должен зеркалить Лекцию 8 (креативные индустрии), но контента для него в источнике никогда не было — это дыра в исходном документе, не решение агента.

- **Pattern: canonical doc в статусе `status: canon` — если правка создаёт неоднозначность, не разрешаемую формальной инструкцией однозначно, встраивать `[NEEDS-OWNER-CONFIRMATION]` блок прямо в canon-файл, а не только в отчёт агента.** Отчёт агента теряется в истории чата; блок в файле переживёт следующего читателя документа (следующий agent или сам owner), пока owner явно не решит и не уберёт маркер. Применимо к любому canon/РПД-подобному документу при структурных изменениях.

- **Известный follow-up вне этой сессии:** `library/normative/rpd-otraslevoe-primenenie-ai.md` содержит ещё более старые границы модулей (Модуль 1 там — всего 5 лекций-плейсхолдеров), рассинхронизирован с `course-plan.md` уже до этого изменения. Не трогался (вероятно issue #51 или его продолжение) — нужен отдельный проход.
---

## 2026-08-11 — Лекция 2 polish pass (issue #156) findings

- **`§[0-9]` scaffold-reference cleanup is a deck-wide, not per-slide, defect.** 10 named review comments pointed at specific slides (s03/s24/s26/s27), but a full-deck grep found the same pattern on 8 additional untouched slides (s02, s04, s15, s16, s19, s21, s22, s23) — some already absent from the actual PPTX render (build script had drifted from markdown source without the §-ref), others genuinely leaking into visible body/notes. **Lesson: always run the deck-wide grep even when the brief names specific slides** — targeted fixes alone under-clean by ~2×.
- **Markdown source and build-script visible text can silently diverge.** Several slides (s04, s21, s22, s23, s26) had stale `§X.Y` text in the `.md` source's Body/Speaker-notes sections that was **already absent** from the corresponding `build_sNN()` function — meaning a prior editing pass fixed the render but not the source, or vice-versa. Cross-check both, not just one, when auditing for forbidden patterns; grep against the rendered PPTX text is the ground truth, grep against `.md` catches source-drift that would resurface on next full rebuild-from-source.
- **`deck.yaml` `visual.primary` free-text fields can contain unescaped inner double-quotes that break strict YAML parsing.** Found 2 instances (`«1-е из 3 "почему"...»`, `«3-е из 3 "почему"...»`) where a Russian curly-quote sentence embedded a literal `"почему"` inside an already-double-quoted YAML scalar — `yaml.safe_load()` fails with a parser error at that line. **The file was already broken before this session** (verified via `git show HEAD:...`), so no tooling that actually parses `deck.yaml` as YAML had been run against it recently, or the break would have been caught. Fixed both instances by rewording to avoid nested quotes (same §-cleanup pass already needed there). **Recommend a `python3 -c "import yaml; yaml.safe_load(open('deck.yaml'))"` sanity check added to the pre-render checklist** — cheap, would have caught this immediately.
- **Shared per-lecture `add_image()` helper had a live silent-failure bug** (height-only calls fell through to "native size" branch, ignoring `h`) — found via visual-loop inspection on a *new* illustration (s01), not by testing the helper directly. Audit showed 13/14 other lecture `build_lecNN.py` copies share the same bug (only lec-02 fixed in this session). See `notes/mcp-limitations.md` [#156-1]. **Lesson: per-lecture copy-pasted build-script helpers accumulate divergent bugfixes — a shared module would propagate fixes automatically.**
- **Decision-tree schema slides benefit from explicit arrowhead connectors, not just thin rectangles.** s25's v1.7 tree used plain `filled_rect` lines root→branches with no visual arrowhead — technically a tree, but read ambiguously at a glance. Adding `MSO_SHAPE.ISOSCELES_TRIANGLE` (rotated 180°) arrowheads at the branch end of each connector made the "flow direction" immediately legible — cheap fix, meaningfully improves the 5-second test pass rate for `schema_pipeline`/`schema_cycle`-adjacent tree diagrams not explicitly covered by the existing subtype table.
- **Inspecting a "final approved" reference slide (Lec-1 s31 Q&A) required rendering, not reading markdown** — confirmed by this session: `s31-qa.md` source and slide-33-of-33 in the actual `lec-01.pptx` diverged (file numbering ≠ final PPTX position after review revisions moved/renamed slides). Brief's explicit instruction to inspect the rendered PPTX (not source `.md`) for reference-pattern-matching tasks was necessary, not just cautious — text-extraction-by-position (`python-pptx` shape dump per slide) was the fastest way to locate the actual target slide among 33.

## 2026-09-06 — Лекция 5 Phase 6 render, Band 1 (issue #189)

- **cairosvg works via the portable LibreOffice sysroot's `libcairo.so.2`** — no separate cairo install needed. Requires BOTH `LD_LIBRARY_PATH=/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu` AND `PYTHONPATH` pointing at the harness's `.local/lib/python3.12/site-packages` (where `cairosvg`/`cairocffi` are actually installed) — either alone fails (`ModuleNotFoundError` or `OSError: no library called "cairo-2"`). Fetching Lucide SVGs live from `https://unpkg.com/lucide-static@latest/icons/{name}.svg` with `-sL`-equivalent (follow redirect) works fine over the sandboxed network; cached to a local `assets/icons/src/` so re-runs of `gen_icons.py` are idempotent and offline-safe.
- **A lecture without a pre-built clickable-URL registry (no `notes/research/lecture-N/references-*.md` deliverable) should NOT port lec-04's full `URLS`/`SLIDE_REFS` machinery wholesale.** Lec-05 had per-slide `source:` frontmatter strings but no canonical URL map. Built a much lighter `_frontmatter_source()` + `notes_with_sources()` pair instead (plain "Источник: …" line appended to speaker notes) — correct-sized solution, avoids inventing fake URLs to satisfy a heavier API surface the lecture's own source material doesn't support yet.
- **`source:` frontmatter can carry internal-only tags like `[FACT-CHECK]` that MUST be stripped before landing in speaker notes** — a naive regex pull of the `source:` line verbatim leaked `[FACT-CHECK]` into 2 slides' visible speaker-notes text, caught only by the mandatory deep-scan/grep pass (`tools/presentation-build/deep_latin_scan.py` on pptx-extracted text), not by eyeballing PNG snapshots (notes aren't in the PNG). **Lesson: any helper that copies raw frontmatter text into notes/body needs an explicit marker-strip step (`\[[A-Z-]+\]`) — don't assume frontmatter is pre-cleaned.**
- **`deep_latin_scan.py` takes markdown/text files, not `.pptx` directly** — extract visible text + speaker notes via a tiny python-pptx script into a `.txt` first (`shape.text_frame.text` + `notes_slide.notes_text_frame.text` per slide), then scan that. Confirmed useful: caught the `[FACT-CHECK]` leak above; also surfaced that section-loop node names (Discovery/Design/Build/Measure/Support/Governance) recur ~50× as "unique Latin tokens" — all legitimate against this lecture's own `deck.yaml`/`glossary.yaml` (roadmap NAV labels + PDCA/OODA/BML formal names + Customer Development/reference dataset canonical glossary-locked terms) — reviewer should cross-check hits against the lecture's own `glossary.yaml` `canonical:` list before flagging, not just the shared brand allowlist.
- **A decorative circular "loop" of icon nodes reads as scattered dots without explicit connector arcs between them** — s02's cover hero (6 nodes on a circle) only became legible as "one loop" after adding `connector()` lines between adjacent nodes in the same draw pass (drawn before the nodes so they sit behind). Any circular-arrangement hero visual needs the connecting edges as a first-class element, not just positioned nodes.

## 2026-09-30 — Семинар 5, пересборка рендерера деки (issue #211)

Сессия вёрстки, четыре круга правок в общих файлах при трёх параллельных сессиях-авторах.
Ниже — то, что переносится на любую деку курса, а не только на эту.

- **Два ложных дефекта за сессию имели ОДНО происхождение: предпросмотр восстанавливал намерение по
  косвенному признаку.** Первый раз — «раз первый прогон абзаца моноширинный, значит абзац не
  переносится»: ячейка таблицы разъезжалась на строку-на-прогон. Второй — «раз прогон моноширинный,
  значит это вывод команды»: моноширинная команда рисовалась одной строкой и на картинке налезала
  на соседнюю колонку, хотя в самом `.pptx` переносилась на три строки и высота под них была
  отведена. Обе догадки разумны, обе неверны. **Цена второй: ложный дефект прошёл прожарку
  студентом, был передан владельцу как «проверенное глазами» и вызвал две правки в чужих слайдах,
  которые пришлось отменять.** Починка в обоих случаях одна и не в читателе: записать свойство в
  сам файл (`text_frame.word_wrap = False`) и читать его, а не выводить. Пока намерение живёт
  только в догадке читателя, следующий читатель угадает иначе. Это же — тема кейса 2 самого
  Семинара 5 (хук «работал, потом молча перестал»): та же порода дефекта, молчит одинаково.
- **«Влезло» и «читается» — разные вопросы, и проверка легко отвечает только на первый.**
  Предупреждение о подгонке кегля сообщает, что пришлось УСТУПИТЬ, и молчит, когда уступать не
  пришлось: таблица, которой хватило 9 pt с первого захода, не даёт ни одного сообщения — она ведь
  влезла. На этой деке так вышло два слайда, набранных на 86% и 98% кеглем мельче 10 pt, при
  четырнадцати сообщениях о подгонке, ни одно из которых про них не сказало. **Проверяя вёрстку,
  спрашивать оба вопроса по отдельности.**
- **Порог в проверке должен быть фактом об инструменте, а не мнением о типографике.** Первая
  редакция той же проверки ставила абсолютные 10 pt и давала 19 сообщений — то есть вёрстка
  выносила приговор, на который не уполномочена, и утопила бы настоящие случаи в спорных.
  Выброшена и заменена на «блок набран на ДНЕ лестницы кеглей своего приёма» (9 pt у таблицы, 7,5 у
  терминальной карточки): проверяемо, однозначно, означает ровно «уступать больше нечего».
  Читается ли это с задних рядов — решает человек, глядя на картинку.
- **Проверку надо доказывать сквозным опытом, иначе она мёртвая.** Правило «блок либо нарисован,
  либо назван в предупреждении» и обе новые проверки по горизонтали (слово шире рамки; наложение
  нарисованного текста на нарисованный) проверялись так: воспроизвести дефект на старом коде,
  убедиться, что проверка его ловит и называет величину, вернуть починку, убедиться в нуле. Без
  этого шага в этой же сессии уже было две проверки, показывавших ноль просто потому, что они
  ничего не умели найти.
- **Сравнивать РАМКИ на пересечение бесполезно — сравнивать надо плотные прямоугольники
  нарисованного текста.** В деке с текстом поверх коробок рамки налезают друг на друга штатно
  сплошь и рядом; список по рамкам утопил бы настоящее столкновение.
- **Правило, записанное как намерение, а не как наблюдение, ломается на первом же исключении.**
  В рендерере стояло «голый абзац в `## Visual` — спецификация для дизайнера, на слайд не
  выводится». Во всех 50 слайдах прежней деки не было НИ ОДНОГО такого абзаца, то есть правило
  никогда не проверялось практикой; первый же новый раздел потерял на нём 18 абзацев на 8 слайдах,
  молча. **Перед тем как закрепить правило, посчитать, на скольких живых случаях оно уже
  подтвердилось.**
- **Разметку нельзя молча срезать, но и молча печатать нельзя.** Обратная кавычка внутри блока
  кода — разметка показываемого файла или настоящий знак содержимого (подстановка команды в
  оболочке)? Вёрстка это не знает и не должна угадывать: решает автор, помечая ограждение языком
  (` ```markdown ` — разметка, всё прочее — дословно). Там, где выбора нет (курсив внутри строки),
  сборка говорит вслух, что не умеет, вместо того чтобы съесть или напечатать.

## 2026-09-30 — Семинар 5: чему научили четыре параллельные сессии над одной декой (issue #211)

Три автора (рамка, хуки, скиллы) плюс сессия рендерера правили один дек в своих worktree. Уроки переносимые, не про Семинар 5.

**1. Проверка, показывающая ноль, — не то же самое, что чистый результат.** За сутки трижды: проверка курсива стояла у одного входа из шести форм; предпросмотр угадывал перенос по шрифту («моноширинный ⇒ вывод команды») и рисовал мнимое наложение; скан текста схем выдирал строковые литералы регуляркой и отчитался «0 попаданий» при двух датах на схеме. Правило: **проверку доказывают сквозным опытом** — сломать нарочно, убедиться, что поймала, вернуть, убедиться, что молчит.

**2. Молчащая проверка молчит в типичном случае, а не на краю.** Уточнение от сессии скиллов, и оно меняет способ отладки: объяснение «проверка работает, просто не поймала редкий случай» почти всегда неверно. Мнимое наложение возникло на *первой же* моноширинной ячейке таблицы; даты не находились в строках, ничем не отличавшихся от найденных. Проверять надо типичный случай, не экзотику.

**3. Диф ветки против головы — не способ забрать чужую работу.** У N веток, отросших в разное время, `git diff HEAD <ветка>` показывает чужие правки как откат. Забирать надо **поимённым списком файлов по владельцу**. Дважды поймано на грани: один диф воскресил бы удалённый слайд, другой — откатил бы круг правок соседнего блока. Отдельно: `git diff --name-status` выдаёт переименования строками `R` с двумя путями — фильтр по `$2` берёт старое имя и молча теряет файл; нужен `--no-renames`.

**4. Разрешение конфликтов — решение по каждому файлу, не оптом.** «Взять свою сторону списком» затянуло откат чужой правки в файле, который автору не принадлежал. Цена: потерянное обобщение, которого требовал владелец.

**5. Забирать каталог целиком (`git checkout <ref> -- dir/`) опаснее, чем кажется:** воскрешает не только удалённые файлы, но и **старые версии живых**. Худший случай прошёл молча — схема собралась правильно, просто уже отведённого места; сказал о ней только класс предупреждения «схема зажата», а не проверки на ошибки.

**6. Записанное намерение против догадки по косвенному признаку.** Оба ложных дефекта предпросмотра родились из разумной догадки о намерении автора. Починка одна: записать свойство в файл (`word_wrap = False` на рамке), а не выводить его из шрифта. Тот же класс — реестр схем: «намерение» в реестре расходится с каталогом в момент правки, когда на слайд никто не смотрит; нужны предупреждения в обе стороны (файла нет / слайда нет).

**7. Границы, заданные числами, ломаются на первой вставке.** Границы разделов деки трижды переписывались вручную, и каждый раз надзаголовок на хвосте врал молча. Выводить их надо из самой деки по опорным приёмам. Но и это держится на допущении о составе — допущение обязано **говорить о себе вслух**, когда перестаёт выполняться.

**8. «Влезло» и «читается» — разные вопросы.** Проверка на переполнение молчит о таблице, которой хватило 9 pt с первого захода. Нужен отдельный класс «на дне кегля» с порогом **по дну лестницы самого приёма**, а не по абсолютному кеглю: первый — факт о вёрстке, второй — мнение о типографике.

**9. Схема платит первой, и это не выглядит дефектом.** Из 12 схем деки 8 были у́же отведённого (61–85%): не «схема обрезана», а «слайд полупустой по бокам». Механика: **укоротить схему на перегруженном слайде не значит дать ей ширину** — освободившаяся высота уходит в бюджет сжатых соседей. Помогает уменьшение содержания или смена раскладки на более широкую.

**10. На плотном слайде схема стоит дороже, чем кажется по списку предупреждений.** Трижды за круг выбор был «иллюстрация или содержание», и все три раза выиграло содержание; в одном случае схема оказалась чистым дублем таблицы под ней, только читалась миниатюрой.

**11. Заметки — половина деки, и ни одна проверка в них не смотрела.** Разметка в заметках не обрабатывалась вовсе, и `*курсив*` доезжал в PowerPoint звёздочками — дефект жил неизвестно сколько, потому что все проверки были про слайд.

**12. Правка ради долей дюйма дважды вернула уже закрытые дефекты.** Закрытый дефект считается закрытым только после повторного замера.

**13. Когда правка затрагивает работу другого автора — спросить дешевле, чем выполнить и откатить**, даже если указание выглядит однозначным: фронт мог сдвинуться, и автор указания об этом не знает. Сессия рендерера так спасла три заголовка, сделанных лучше, чем предписывало моё указание.

## 2026-10-01 — `tools:` во фронтматтере субагента: «All tools» даёт НОЛЬ инструментов (issue #212)

- **`tools: All tools` в `.claude/agents/*.md` — не «все инструменты», а пустой список.** Значение парсится как список из двух элементов (`All`, `tools`), оба не распознаются как имена инструментов, и спавн падает: «Agent 'literary-editor' would be spawned with zero tools — refusing. Its tools list resolved to nothing: unrecognized [All, tools]». Поймано на трёх одновременных спавнах `literary-editor` — все три упали до единой строки работы.
- **Правильный способ дать агенту все инструменты — вообще не писать `tools:`.** Проверено по репозиторию: `literary-editor` был единственным агентом из девяти с этой строкой, у всех работающих (`book-editor`, `methodology-critic`, `fact-checker`, `consistency-checker`, …) поля `tools:` нет вовсе. Строка удалена.
- **Почему дефект дожил до первого запуска:** агент заведён коммитами `fcc11d34`/`ed17dd12` вместе с методикой, но ни разу не вызывался — описание в каталоге агентов рендерится из `description:` и выглядит исправным независимо от того, резолвится ли `tools:`. **Ошибка такого рода не видна ни при чтении файла, ни в списке доступных агентов — только при спавне.** Заводя нового субагента, сделай один пробный спавн сразу, а не в тот момент, когда он понадобился в работе.
- **Правка файла агента НЕ помогает текущей сессии: каталог агентов кэшируется на старте.** После удаления строки и коммита три повторных спавна упали с тем же самым сообщением, дословно. Значит `.claude/agents/*.md` читается один раз при запуске сессии, и починка в середине работы действует только на следующие сессии. **Обход, не требующий перезапуска:** спавнить штатного агента (`general-purpose`), а роль выдавать заданием — «прочитай `.claude/agents/literary-editor.md` и работай по нему». Системная подсказка роли лежит в том же файле, который и так был бы системной подсказкой, так что поведение то же, а сломанное поле `tools:` просто не участвует.
- **Follow-up (не сделано здесь):** сам `notes/decisions.md` на 671 строке при лимите репозитория 600 (CLAUDE.md § Document Size Limit) — нарушение возникло до этой сессии. Разбиение на части — отдельная задача, бандлить её с правкой агента не стал.
