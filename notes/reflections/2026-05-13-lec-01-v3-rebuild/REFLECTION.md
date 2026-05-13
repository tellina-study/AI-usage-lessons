# Reflection — Лекция 1 v3.x production (2026-05-13)

**Scope:** day-long production of Лекция 1 «AI вокруг нас» — chapter v3.1, slides v3.2 (33 slides), speech v3.1.
**Issues:** EPIC #64.D Phase 12 (sub-issue #70).
**Branch:** `issue-69-lec01-full-deck-from-chapter`.
**Final quality:** APPROVE-WITH-MINOR от всех 4 critic рангов на финальных артефактах. Но user **трижды** возвращался с substantial revisions после critic-approve.

---

## TL;DR (управленческое summary)

**Что прошло хорошо.** Pipeline доработан до production-grade: 33 readable slides, 16,400-word chapter, 5,100-word speech. Все 23 user замечания round 1 + 19 round 3 + 7 critic-driven фиксов закрыты. Палитра LOCKED, motif consistent, footer-tax = 0, англицизмы вычищены системно. Visual loop с min-3-iter принципом дал чистый рендер s11/s12/s13/s16/s18/s19+s19a/s21 — реально хорошие пед-визуалы. Book-first методология сработала: chapter v3 → slides + speech derive без drift крупных тезисов. 14+ designer iterations + 5 параллельных agent runs показали, что workflow выдерживает coordination нагрузку.

**Главные failure modes (5).**
1. **Critics проходят там, где user отклоняет.** Все 3 рунд'а user feedback наступали ПОСЛЕ critic APPROVE-WITH-MINOR. Critics проверяют compliance с playbook (палитра, motif, footer-tax, англицизмы, LO coverage), но **не проверяют relevance, terminology drift, schema readability, structural coherence**.
2. **Designer создаёт визуал и пропускает text-wrap в нетривиальных схемах.** Названия столбцов сломаны на s07 timeline, s12 matrix, s15 pipeline, s16 chat cycle (round 3 fix #11). Visual loop ловит overflow на простых элементах, но не на сложных композициях.
3. **Writer-driven content drift между артефактами.** «Приложение-робот» / «Приложение-автоматизация» / «Приложение (автоматизация)» — три формы для одного концепта. Chapter, slide, speaker notes, speech разъезжаются после revisions. consistency-checker должен ловить, но в первом проходе пропустил.
4. **Speaker notes как дефолт = layout description, не текст для студента.** Round 1 fix #1 — самое крупное замечание; designer думал что notes для собственной координации. Этого не было в playbook.
5. **Critics пропустили "лишние слайды" (Pearl, ARC-AGI) — их добавили critics в раунд v2/v3, удалил user.** Relevance-pre-check для лекции 1 (introductory) отсутствовал.

**Топ-5 рекомендаций для лекции 2 (P0).**
1. Перед каждым critic-approved gate — orchestrator делает **user-perspective scroll-through**: 30-минутный visual sweep по всем slides + speaker notes + read-aloud test, чтобы дублировать user feedback ДО формального gate'а.
2. Speaker notes — отдельный template + контракт в `book-editor.md` / `presentation-designer.md`: «150-300 слов читаемого текста для студента, derived from chapter §X + speech [sNN]». Layout descriptions запрещены.
3. Designer добавляет explicit **schema readability checklist** при создании любого 2D диаграмма (matrix, quadrant, timeline, layered, cycle): max 2 строки в каждой ячейке, font ≥12pt, axis labels INSIDE quadrant, единый язык подписей (RU only).
4. consistency-checker запускается **дважды**: текущий cycle (post-draft) + **terminology drift sub-check** перед каждым USER GATE с автоматическим grep по ключевым неологизмам лекции.
5. Pre-render relevance check от methodology-critic: для каждого слайда — «зачем это в лекции N (introductory/intermediate/advanced)?» — слайды без чёткого ответа = кандидаты на удаление, не на улучшение.

**Estimated effort для implementation:** 6-8 рабочих часов на agent prompts + playbooks + 1 P0 PowerPoint MCP fix (`list_shapes`/`update_shape_position` мог бы убрать половину rebuild overhead).

---

## 1. Метрики раунда

### 1.1 Time

- **Wall clock:** ~14 часов session работы с компакцией в середине (USER MSG #55 = «session continued from previous conversation»). Начало 2026-05-12, финиш 2026-05-13 ~14:46.
- **Active production phases:** Phase 12.2 chapter v3 → 12.3 deck plan → 12.4 slides v3 → 12.5 speech v3 → Phase 12.6 v3.1/v3.2 mid-stream → final cleanup.

### 1.2 Iterations + agent runs

- **User feedback rounds (substantial):** 3 (round 1 = 23 fixes, round 2 = 8 mid-stream Fix-12..19, round 3 = 19 fixes).
- **Critic-driven fixes:** ~10 (chapter v3.1 sanity, slides v3.1 sanity, speech v3.1 P0+P1).
- **Visual loop iterations on PPTX:** 14+ (iter4 → iter14 across v3, v3.1, v3.2 builds).
- **Total agent spawns (estimate from transcript):** ~15-18:
  - book-editor: 3 (chapter v3, v3.1, §5.2 sync)
  - presentation-designer: 5+ parallel batches (Fix-12, Fix-13/14, Fix-15, Fix-16, Fix-17/18, Fix-19, plus full v3.2 rebuild)
  - speech-writer: 2 (v3 draft, v3.1 P0+P1)
  - methodology-critic: 4 (chapter v3, v3.1 sanity, slides v3 in synthesis, speech v3)
  - fact-checker: 4 (chapter v3, slides v3, speech v3, also embedded in synthesis)
  - consistency-checker: 1 (speech v3)
  - presentation-critic: 3 (slides v3 initial, slides v3.2 sanity, plus embedded checks)
  - student-simulator: 2 (slides v3, slides v3 batch 2 for reliability)
  - reader-simulator: 2 (text-only pre-render, rendered post-render)

### 1.3 Final artifacts

- `chapter.md` — 16,406 words, 60 references, status=reviewed (v3.1).
- `lec-01.pptx` — 33 slides, 16:9, ~1.3 MB (v3.2).
- `speech.md` — ~5,100 spoken words, 62 active min + 13 buffer = 75 min, status=reviewed (v3.1).
- `qa-reports/2026-05-13-user-feedback-23/` — 9 docs (REQUIREMENTS, SYNTHESIS×3, methodology×2, presentation-critic, student-sim, plan).
- `iteration-log-v31.md` (38KB) + `iteration-log-v32.md` (18KB).

### 1.4 Quality scores (final)

- methodology-critic: APPROVE on chapter v3.1 (0 P0, 0 P1), APPROVE-WITH-MINOR on speech (1 P0 → fixed).
- fact-checker: 0 ошибок на 50+ verified claims.
- consistency-checker: APPROVE-WITH-MINOR (4 P1, all fixed).
- presentation-critic: APPROVE-WITH-MINOR на slides v3.2 (0 P0, 0 P1, 2 P2 cosmetic).
- student-simulator: «местами зашло, но к разделу 4 потерял ритм» (5/10 zoned out at minute 50).
- reader-rendered: 28/34 self-contained.

### 1.5 Cost (rough order)

- ~15 agent spawns × Opus 4.7 (1M context) с large input contexts (chapter 16k words + slides 33×0.5k + speech 5k = ~25k+ tokens of context per critic) = significant cost.
- Visual loop snapshots — 562 PNG @ ~100KB avg = 71MB local storage (no API cost but git-bloat).

---

## 2. Категория A — User feedback patterns

### 2.1 Round 1 (23 fixes, USER MSG #56) — после deck v2.1 показа

**Структурные** (10 issues):
| # | Тип | Caught? | Можно было предотвратить как |
|---|---|---|---|
| 1 | Speaker notes = вёрстка | ❌ critics | Template + DoD в playbook designer.md |
| 3 | s06 «Два определения» — выдуманное «инженерное» | ❌ critics | methodology-critic должен ловить выдуманные псевдо-термины |
| 4 | s08 «4 оси» с Copilot — лишняя глубина для введения | ❌ critics | Relevance-check «зачем это для introductory» в pre-flight |
| 5 | s10 «доверие падает» — фактическая инверсия | ❌ fact-checker (!) | Должна быть пометка direction-of-claim |
| 6 | s10 DeepSeek — добавить ещё прорывы, убрать «правила курса меняются» | ❌ critics | Critic не проверяет «слайд раскрывает заявленный intent» |
| 7 | Перед s11 нет divider | ⚠️ student-sim назвала «навигация хорошая», но не предложила |
| 8 | s11 title insider phrasing | ❌ presentation-critic | Title-как-assertion check был, но «соответствие auditория» не |
| 11 | s13 нет схемы вход-модель-выход | ❌ critics | Schema-presence checklist для архитектурных слайдов |
| 13 | s14 нет схемы цикла чата | ❌ critics | То же |
| 15 | s17 нет схемы агента | ❌ critics | То же |
| 17 | s18 чек-лист сложный (4 вопроса + матрица) | ❌ critics | Сложность не критикуется, оценивается «корректность» |

**Visual / typography** (5 issues):
| # | Тип | Caught? | |
|---|---|---|---|
| 21 | Footer-tax (множ. источник) | ⚠️ presentation-critic v2 caught 3 (s12/s18/s26), не все |
| 23 | s29 backup-провокации в Q&A | ❌ presentation-critic | «Полный анализ контента слайда» missing |

**Content** (8 issues):
| # | Тип | Caught? | |
|---|---|---|---|
| 2 | Англицизмы (стейкс, фоллбек etc.) | ❌ critics | Tone analysis не упоминает англицизмы как pattern |
| 12 | Ссылки на чек-лист сломаются | ❌ orchestrator | Cascade-of-changes tracking |
| 14 | s15 RTC — преждевременно | ❌ critics | Curriculum-progression check |
| 16 | s17 Copilot ambiguity | ❌ critics | Same as #4 — relevance |
| 18 | Раздел 4 7 слайдов — переоценить тайминг | ⚠️ student-sim P1 | После факта, не до |
| 19 | Перед s27 нет резюме | ❌ critics | Structural «closing arc» check |
| 20 | s27 roadmap — галлюцинация | ❌ fact-checker (!) | Не сверял с Drive doc |
| 22 | s28 takeaways = duplicate of #19 | ❌ presentation-critic | Cross-deck redundancy check |

### 2.2 Round 2 (8 mid-stream fixes USER MSG #70-#76, designer-driven) — после v3.1 show

| # | Замечание | Категория | Critics поймали? |
|---|---|---|---|
| Fix-12 | Убрать тайминг из видимого контента | Visual/UX | ❌ — никто не смотрел «зачем студенту видеть тайминги» |
| Fix-13 | s06 «нет определений, ничего не понятно» | Methodology | ⚠️ reader-text-only мог поймать, но не получил v3.1 после restructure |
| Fix-14 | s07 timeline сломан (12 событий 2 строки) | Visual readability | ❌ presentation-critic смотрел общую структуру, не word-wrap |
| Fix-15 | s11 потеряны компоненты слоёв | Pedagogical content | ❌ designer переписал layout без проверки «assertion remains supported» |
| Fix-16 | s13 поменять оси, чтобы Agent в правом-верхнем | UX/intuition | ❌ critic одобрил semantic correctness, не intuitive direction |
| Fix-17 | Nav slides все разные — нужен единый template | Consistency | ❌ presentation-critic не проверял nav-slide template uniformity |
| Fix-18 | s16 cycle не читается | Schema readability | ❌ initial design accepted by designer's own visual loop |
| Fix-19 | Убрать «вы здесь / сюда» текстовые маркеры | UX/visual minimalism | ❌ designer добавлял по своей инициативе, user не просил |

### 2.3 Round 3 (19 fixes USER MSG #86) — после v3.1 full show

| # | Замечание | Категория | Critics поймали? |
|---|---|---|---|
| 1 | Убрать «Лектору» секцию из notes | UX/separation of concerns | ❌ designer добавлял по своей инициативе |
| 2 | s02a — убрать subtitle | Visual hygiene | ❌ |
| 3 | s04 bar chart — назад на 8 типов | Consistency с s03 | ❌ |
| 4 | s04 donut «51%» потерян + не круглый | Visual chart-correctness | ❌ presentation-critic не проверял centred number visibility |
| 5 | s04 убрать takeaway band | Visual minimalism | ❌ |
| 6 | s05b funnel сломан | Visual readability | ❌ |
| 7 | s07 переносы дат + AI Effect duplicate с s06 | Cross-slide redundancy | ❌ |
| 8 | s09 убрать Llama-3 + MCP, добавить OpenClaw + Kimi K2.5 | AI tools freshness | ❌ critics не оценивают «свежесть примеров» |
| 9 | s11 квадраты не центрировать, по нижней границе | Visual aesthetic | ❌ |
| 10 | s12 добавить иконки + сломаны столбцы + заполнить | Visual readability + content density | ❌ |
| 11 | s15 сломаны стрелки + сломаны тексты | Visual readability | ❌ |
| 12 | s16 cycle — пользователь, стрелки... (полный redesign) | Schema readability (повтор Fix-18) | ❌ — designer попытался, но не дошёл до user-friendly формы |
| 13 | s17 убрать LLM bar повтор, дать дисклеймер | Cross-slide redundancy | ⚠️ reader-rendered поймал «s17 повтор s04» |
| 14 | s18 добавить пользователя | Schema completeness | ❌ |
| 15 | s19 разделить на s19+s19a | Pacing/density | ⚠️ student-sim назвал s19 «плотный», не предложил split |
| 16 | s21 ответы не соотносятся с матрицей | Visual semantics | ⚠️ presentation-critic поймал «axis outside quadrant», не «marker semantics» |
| 17 | s28 убрать «защитите перед группой» | Tone/practical | ❌ |
| 18 | s29 модули — неверная attribution Лекции 6 и 8 | Factual correction | ❌ fact-checker должен был сверить с Drive doc после module-shuffle |
| 19 | s30 callback frame лишний | Visual minimalism | ❌ |

### 2.4 Convergent observations

- **62 user-driven changes за 3 раунда.** В каждом раунде ~⅔ — это things critics НЕ caught.
- **User mental model = «прокручиваю по позиции / по экрану»**, мы — «по slide ID». User говорит «слайд 7 = таймлайн», у нас s06=определения, s07=таймлайн, и при удалении/добавлении слайдов numeration shifts. Это вызывало путаницу в FIX request mapping (см. REQUIREMENTS.md §1.#3 — пользователь сказал «слайд 7 — два определения», у нас это s06).
- **Designer-driven «свои инициативы»** (что user не просил):
  - «Лектору» секция в notes (убрана раунд 3)
  - «Вы здесь» текстовые маркеры (убраны раунд 2)
  - Тайминг в навигации (убран раунд 2)
  - subtitle в s02a (убран раунд 3)
  - Все эти добавления показались designer'у «полезной заботой», но создали шум для user.
- **Tools freshness — критическая проблема.** s09 список прорывов 2024-26 был релевантен 2 дня назад, но к моменту user review user знал свежие примеры (OpenClaw, Kimi K2.5) которых у нас не было. ARC-AGI 37.6% к 13 мая 2026 — устарело: Opus 4.6 = 68.8%, GPT-5.5 = 85% (см. SYNTHESIS-slides-v3.md fact-checker P1-8).

---

## 3. Категория B — Agent failure modes

### 3.1 presentation-designer

**Failure 1: Schema readability — initial design accepted by self-loop.**
- s16 cycle: 6 vertical step boxes + center «LOOP» badge — first design в Fix-12 (initial v3.1). User: «не читается». Fix-18 = vertical linear flow. User round 3: «снова не читается» (Fix #12). Финальная версия: 2 USER icons + диалог компактный.
- s11 layers: initial v3.1 = 4 концентрических boxes без component labels. User: «потеряны компоненты». Fix-15 переделал, потребовало 5 visual-loop итераций (iter8-iter12) чтобы text не пересекал box borders.
- s13 quadrant: initial v3 axes wrong direction. Fix-16 swap axes — потребовало 2 итераций для геометрии sub-text positioning.
- **Корень:** designer проверял PNG визуально, но критерий = «нет overflow / overlap», не «студент с 5-го ряда поймёт за 5 секунд».

**Failure 2: Designer добавлял своё, не следовал contract.**
- «Лектору» секция в notes — designer вставлял по умолчанию, не было в task brief.
- «Вы здесь» текстовые маркеры — designer добавил, чтобы навигация была явной.
- subtitle «Что мы пройдём за 75 мин» в s02a — designer думал что polishing.
- **Корень:** в `presentation-designer.md` нет явного «do nothing extra unless requested». Designer = creative role с инициативой, но без guardrails.

**Failure 3: 5 параллельных designers — coordination overhead.**
- Fix-15/16/17/18/19 запускались одновременно. PPTX file lock conflicts (Fix-15 «sequentially after libreoffice convert from another designer»; Fix-19 «первая попытка edit конфликтнула, retry прошёл»).
- Build script (build_lec01_v31.py) был monolithic — каждый designer правил один файл, неизбежные race conditions.

### 3.2 speech-writer

**Failure 1: Speech v1 вернул англицизмы обратно** после того как book-editor вычистил chapter v2.
- methodology-critic chapter v2 → 0 «стейкс / фоллбек». Speech v1 → стейкс снова. Speech v2 P0 fix.
- **Корень:** speech-writer не проверял свой output против tone-rules chapter'а.

**Failure 2: Speech v3 имел orphan reference на удалённый s26.**
- `[s26 pre-flight для ARC-AGI]` блок в «Подготовка перед лекцией» остался от v3 → v3.1 transition (ARC-AGI slide удалён в v3.1). consistency-checker поймал как P0.
- **Корень:** speech не sync с deck.yaml deletions automatically.

### 3.3 book-editor

**Failure 1: Chapter v3 «не мощно» закрыл #4 (упрощение до 2 осей).**
- Chapter §1.4 footnote «не является целью нашего курса» — too strong (противоречит Лекции 2 «Как работают современные большие модели» которая явно про architecture).
- methodology-critic v3 P1 → fixed в v3.1.
- **Корень:** book-editor применял user fix буквально, не проверял downstream consistency с программой курса.

**Failure 2: Mistral specific numbers без verifiable source.**
- chapter v3 §2.2 «20+ человек / 3 месяца» — fact-checker P1, не verifiable. Replaced softer formulation.
- **Корень:** book-editor не маркировал [FACT-CHECK] для unverified specific numbers.

### 3.4 methodology-critic

**Failure 1: Не проверяет «зачем этот контент в лекции N».**
- Pearl 3 уровня — добавлен в chapter v2 как concept depth. Critic одобрил «evaluate-level». Но user (round 1 #18 + round 3 follow-up) удалил: «слишком абстрактно для introductory».
- ARC-AGI economics — то же самое: критически важная концепция, но не для лекции 1.
- **Корень:** Critic проверяет правильность сама по себе, не curriculum-relevance.

**Failure 2: Не проверяет «term-validity».**
- Chapter v2 §1.1: «рабочее определение AI» (insider phrasing). Critic v2 одобрил. User: «что за рабочее определение ты выдумал?»
- Корень: methodology-critic не проверяет, что термин — каноничен в литературе, а не редакторский «clean phrasing».

**Failure 3: Англицизмы — pattern не учтён до Round 1.**
- Chapter v2 critic не упоминал англицизмы. Round 1 #2 — массовая чистка. Critic v3 уже учёл (после явного включения в REQUIREMENTS).
- **Корень:** Pattern не был в playbook до того, как user его явно сформулировал.

### 3.5 fact-checker

**Failure 1: Не сверял с user-provided Drive doc.**
- s27 (later s30/s29) roadmap — chapter и slides показывали «4 блока (Основы / Инструменты / Интеграция / Границы)». User: «галлюцинация, реально 3 модуля × 17 лекций» (Drive doc reference в USER MSG #58).
- Fact-checker не имел инструкции «check user-provided source documents from Drive».
- **Корень:** Fact-checker полагается на web research, но source-of-truth для course structure = Drive doc, а не web.

**Failure 2: Не оценил freshness рапорт-данных.**
- ARC-AGI 37.6% — было актуально на момент chapter draft, устарело за 2 дня к user review.
- s09 episode list (Llama-3, MCP) — устарел relative to user knowledge.
- **Корень:** AI tools/benchmarks должны иметь explicit «freshness check» (когда источник опубликован, релевантна ли цифра сейчас).

**Failure 3: Не сохранил отчёт как separate file.**
- В `qa-reports/2026-05-13-user-feedback-23/` — нет `fact-checker-chapter-v3.md`, только embedded в SYNTHESIS. Аналогично consistency-checker не сохранил.
- **Корень:** Agent инструкции не явно требуют save-as-file (или Write banned для subagent в каком-то моменте).

### 3.6 consistency-checker

**Failure 1: «Приложение-робот» drift пропущен в первом проходе.**
- Phase 12.5 sanity check (после speech v3) поймал 3 формы «Приложение-робот / Приложение-автоматизация / Приложение (автоматизация)». Но если бы он запускался ДО USER GATE 2 (после slides), мы бы поймали раньше.
- **Корень:** consistency-checker запускается только в Phase 10 (после speech). Slides+chapter drift сейчас не проверяется отдельным циклом.

**Failure 2: Speaker notes vs visual mismatch на s13.**
- presentation-critic поймал: speaker notes говорят «Модель в правом-нижнем», на слайде в левом-верхнем. consistency-checker не запускался на slides + notes alignment отдельно.

### 3.7 presentation-critic

**Failure 1: Не оценивает «нравится ли мне как студенту схема».**
- s11 layers v3 (4 concentric boxes без labels) — accepted. User: «потеряны компоненты».
- s13 quadrant v3 (axes orientation) — accepted (semantically correct). User: «оси неправильные для intuition».
- s16 cycle v3 (6 vertical steps) — accepted. User: «не читается».
- Критик проверяет «overflow / overlap / hierarchy» — но не «schema teaches the concept clearly».

**Failure 2: APPROVE-WITH-MINOR одобрял с 6+ unique P1.**
- Pattern: critic нашёл много P1, но overall verdict = APPROVE-WITH-MINOR. Verdict эмоционально читался как «можно показывать». В реальности — каждый P1 это 5-10-минутный visible issue для user.

### 3.8 student-simulator

**Failure 1: Говорил «зашло», не предлагал убрать слайды.**
- s27 (4 спикера AGI) — student: «таблица 4×4 текстом — это для самостоятельного чтения, не для зала». Но severity = P1, не «удалить».
- s28 Pearl — «слово-убийца на 65-й минуте». Severity P1.
- User в round 1 #18 еще не успел увидеть это, в round 3 решил оставить (Pearl и ARC-AGI остались на v3.2 финал). Но student-simulator должен был быть жёстче с «delete» recommendation.

**Failure 2: Не предложил конкретные удаления.**
- В отчёте student-simulator-slides-v3.md «Конкретные просьбы лектору» — есть «раздел 4 ужать на 30%», но нет explicit list slides-to-delete.

### 3.9 reader-simulator

**Failure 1: Mode=rendered «28/34 self-contained» — не оценивает «structural improvement».**
- Number сильно выросло с v2 (22/29) до v3 (28/34). Хорошо. Но reader не сказал: «эти 6 self-contained-fail слайдов = structural blockers, не просто notes-fixes».
- **Корень:** reader измеряет «понятно ли», не «что фундаментально мешает».

---

## 4. Категория C — Critic blind spots

### 4.1 Чек-лист blind spots (что critics НЕ проверяют)

| Blind spot | Result | Recommended check |
|---|---|---|
| **Schema readability for laymen** | s11/s13/s16/s18 переделывались 2-3 раза | «5-second test»: видишь схему 5 сек, понял главную мысль? |
| **Curriculum relevance** | Pearl/ARC-AGI/Copilot worked example удалены user'ом | «Зачем этот концепт в лекции N?» — answer должен быть из ≤2 фраз |
| **Visual centring of charts** | s04 donut «51%» потерян внутри ring | Visual centring rule в QuickChart presets |
| **Cross-slide redundancy** | s17 bar chart дублировал s04 | Pre-flight grep по slide content для повторов |
| **Term canonical-validity** | «рабочее определение», «приложение-робот» | Critic должен сверять с литературой / каталог терминов |
| **Tools/benchmark freshness** | ARC-AGI 37.6%, Llama-3 как «свежий пример» | Дата cutoff + warning «verify on day-of-lecture» |
| **Designer-added content** | «Лектору», «Вы здесь», тайминг в видимом | Audit: designer добавил что-то не из task brief |
| **Color-only highlights vs text** | «Вы здесь — раздел N» дублировал gold cell | Single mechanism per signal |
| **Notes-as-readable-text** | Layout descriptions в notes до round 1 | Notes word-count + content-type classifier |
| **Title-vs-body assertion alignment** | s11 title «не альтернативы» содержательно ОК, но не считывается | «Title test» — закрой body, поймёшь intent? |

### 4.2 Verdict inflation problem

Critics систематически давали APPROVE-WITH-MINOR при 4-12 unique P1 issues. Это создаёт false sense of done.
- chapter v3: 0 P0, 10 P1 = APPROVE-WITH-MINOR
- slides v3: 0 P0, 12 P1 = APPROVE-WITH-MINOR
- speech v3: 1 P0, 7 P1 = APPROVE-WITH-MINOR (после P0 fix)
- slides v3.2 sanity: 0 P0, 0 P1, 2 P2 = APPROVE (наконец clean)

**Recommend:** новая verdict scale:
- **REJECT** (any P0)
- **REVISE** (5+ P1 — must fix before show)
- **APPROVE-WITH-POLISH** (≤4 P1 — show-able с known caveats)
- **APPROVE-CLEAN** (0 P1)

Сейчас всё что не P0 = APPROVE-WITH-MINOR.

---

## 5. Категория D — Methodology gaps

### 5.1 Speaker notes format — НЕ был template'ом
- Round 1 fix #1 = «notes должны быть читаемым текстом, не описанием layout».
- В `presentation-designer.md` line 199 есть «Speaker notes — что говорит преподаватель (1-3 абзаца)» — это слишком расплывчато.
- В `book-editor.md` notes не упомянуты.
- В `tools/lecture-production/README.md` notes упомянуты как cliché.
- **Gap:** нет explicit contract: «notes = derived текст ~150-300 слов из chapter §X + speech [sNN]».

### 5.2 Terminology consistency — нет автоматического trigger
- При изменении chapter §3.6 «Приложение-робот» нужно автоматически triggerить slide rewrites + speech sync.
- Сейчас orchestrator вручную решает «грепнуть ли по проекту».
- **Gap:** консистентность check выполняется ad-hoc post-factum, не проактивно.

### 5.3 Schema readability — нет checklist
- presentation-designer.md перечисляет «иерархия / контраст / spacing» — но это generic. Specific schema-types (matrix, quadrant, timeline, layered, cycle) требуют разных checklist.
- **Gap:** §4 «slide-types library» в presentation-build/README.md имеет 8 типов, но не содержит per-type readability test.

### 5.4 User-positional vs ID-based slide referencing
- User считает «слайд 7 = третий после titlula». У нас s07 = после деления на s05a/s05b/s06.
- Round 1 #3 «слайд 7» = у нас s06.
- **Gap:** Communication protocol — orchestrator должен трансформировать user-position в slide ID при receiving feedback и обратно при response.

### 5.5 Coordination между параллельными designers
- 5 designers в Fix-15/16/17/18/19 одновременно правили `build_lec01_v31.py`. Нет file lock protocol.
- **Gap:** нет coordination strategy «какой designer владеет какой slide-builder функцией».

### 5.6 Когда удалять vs улучшать (relevance vs absolute quality)
- Pearl, ARC-AGI, Copilot worked example — все три «методически высокого качества», но user удалил/упростил.
- **Gap:** нет protocol «test for delete before improve»: «slide cuts? +30% pacing buffer? возможно лучше удалить, чем оптимизировать».

### 5.7 AI tools/data freshness
- Данные 2025-2026 устаревают за дни (ARC-AGI shifted by 30+ percentage points за 2 дня).
- **Gap:** Pre-flight checklist для лектора должен включать «check freshness 1 день до лекции» — был, но user сказал убрать (round 3 #2).

### 5.8 Pre-flight checklist actionability
- Speech v3 pre-flight включал ARC-AGI verify, который к моменту final v3.1 был moot (slide deleted). Lекторская инструкция = пыль.
- **Gap:** Pre-flight должен sync с deck deletions/additions автоматически.

### 5.9 Phase gate timing
- USER GATEs в `tools/lecture-production/README.md` определены как 3 (после chapter, slides, speech). Но user wanted 5+ gates: после draft chapter, после chapter revisions, после slides plan, после slides v1, после notes update, после speech v1, перед merge.
- **Gap:** Многие orchestrator GATEs были «de-facto skipped» (сразу проходили approve без полного review by user — например chapter v2 и speech v1 одобрены без визуального просмотра — позже именно эти артефакты получили round 1 feedback).

---

## 6. Категория E — MCP/tool issues

### 6.1 PowerPoint MCP limitations (existing in `notes/mcp-limitations.md`)
- **[#54-1]** нет `list_shapes` — заставляет держать mental model index'ов. **Не блокирует, но increases mistake rate.**
- **[#54-3]** нет `update_shape_position` — каждая итерация = full rebuild. **Реально boltleneck при 33 slides × 5 designers.**
- **[#55-1]** 4:3 default → patch для 16:9. Already documented.
- **[#55-2]** background not applying — workaround есть.

**New observations (need adding to mcp-limitations.md):**
- **[NEW] MSO_SHAPE.RIGHT_ARROW vs filled_rect+rotated_triangle** — для proper arrows используем proper shape (Fix-11 в iteration-log-v32.md). filled_rect+triangle гибрид «выглядит сломанно», не connector arrow.
- **[NEW] LibreOffice convert overhead** — каждая визуальная итерация = libreoffice headless ~3-5 сек на 30+ slides. С 14 итерациями = 1+ минута чистого latency только на convert. Mitigation: convert per-slide (если возможно), или batch convert.
- **[NEW] Build script approach (python-pptx прямо) выиграл MCP-based для full-deck rebuild.** Causes: (1) full-rebuild на каждой итерации делает MCP iterative API бесполезным, (2) python-pptx даёт прямой контроль над XML inject (для backgrounds, runs), (3) MCP serialization-deserialization overhead. **Recommend:** для full-deck builds — python-pptx скрипт + helper functions; MCP для quick spike/preview.

### 6.2 workspace-mcp
- **[#49]** OAuth disruption — re-auth был требован (USER MSG #59 «авторизовался»). Long-term fix (production status в Google Cloud Console) до сих пор не сделан. **Recommend:** сделать сейчас, до начала Лекции 2.

### 6.3 Snapshots size + git bloat
- **562 PNG snapshots** = 71 MB в repo. Это `library/lectures/lec-01/rendered/snapshots/`. Каждая итерация добавляет 30+ файлов.
- **Recommend:** `.gitignore` snapshots/ полностью — оставить только финальные `s01.png ... sNN.png`. Iter snapshots local-only.

### 6.4 Multiple build scripts (build_lec01_full.py, _v2.py, _v3.py, _v31.py, _full_v4.py, build_v36.py)
- **7 build scripts** — каждая major version. Многие не используются.
- **Recommend:** оставить только canonical `build.py` + версионирование через git history. Старые scripts удалить.

---

## 7. Категория F — Coordination issues

### 7.1 5 параллельных designers — race conditions
- iteration-log-v31.md многократно упоминает «PPTX file lock checked before each build», «Fix-15 ran sequentially after waiting for libreoffice convert from another designer».
- **Issue:** monolithic build script + parallel agents = inevitable conflicts.
- **Recommend:** design coordination strategy:
  - Each designer owns a list of slide-IDs (не функций).
  - Or use git branch per designer.
  - Or sequential designer pipeline с explicit pass-the-baton.

### 7.2 Lost reports
- **fact-checker** в Phase 12.2 (chapter v3) и **consistency-checker** в Phase 12.5 — отчёты НЕ сохранены как файлы. Содержание возвращено в чат и embedded в SYNTHESIS docs. Если orchestrator закроется без synthesis — отчёты потеряны.
- **Issue:** subagent prompt не явно требует «save report as file before completing».
- **Recommend:** в каждом critic agent prompt добавить «Output file path: ABSOLUTE_PATH. Save before finishing». Если save fails — agent retry с explicit Write tool path.

### 7.3 TaskCreate/Update проактивность пропускалась
- Orchestrator не systematically обновлял in_progress / completed для todo items. Отдельные Tasks были долгими, но без markers.
- **Issue:** transcript hard to follow, user видел только финальные деливерабли.

### 7.4 USER GATEs — иногда проходил approve без полного review
- Chapter v2 → одобрен без полного scroll-through. Slides v2.1 → одобрен после critic APPROVE. Speech v2 → одобрен после critic. **Все три** получили substantial revisions потом.
- **Issue:** «approve» = «all critics approved», not «I (user) reviewed visually».
- **Recommend:** USER GATE = orchestrator presents 30-минутный «walkthrough preview» с ключевыми визуалами + read-aloud test от orchestrator perspective + explicit «do you want to scroll through yourself?» — only after user direct approve можно gate pass.

### 7.5 Background tasks — orchestrator не consistently monitored
- 14 visual iter snapshots → designer сообщал completion в final, без incremental updates.
- **Issue:** при failure designer перезапускался с нуля без middle progress.

---

## 8. Категория G — Repository hygiene

### 8.1 Snapshots
- **562 PNG в repo** = потенциал bloat. Текущий 71MB на 1 лекцию × 17 = 1.2GB на курс. Add to .gitignore.

### 8.2 Build scripts
- 7 build scripts (`build_lec01_full.py`, `_v2.py`, `_v3.py`, `_v31.py`, `_full_v4.py`, `_full.py`, `build_v36.py`).
- **Recommend:** оставить один canonical `build.py` для каждой лекции + git history.

### 8.3 Iteration logs
- `iteration-log-v31.md` (38KB) + `iteration-log-v32.md` (18KB) + `iteration-log-v34.md` (13KB) + `iteration-log-v3.md` (10KB) + `iteration-log-v4.md` (8KB) + `iteration-log-v2.md` (6KB) + `iteration-log.md` (13KB).
- **Many iteration logs** — нумерация запутанная (`v34`?). Recommend single rolling log + git history.

### 8.4 Old slide files (s06-two-definitions, s08-classifications-4-axes etc.)
- Удалены в чистке Round 1. Git history retains. OK.

### 8.5 QA-reports organization
- `qa-reports/2026-05-12/`, `2026-05-12-chapter-v1/`, `2026-05-12-chapter-v2/`, `2026-05-12-deck-v1/`, `2026-05-12-deck-v2/`, `2026-05-12-speech-v1/`, `2026-05-12-speech-v2-sanity/`, `2026-05-12-v2/`, `2026-05-13-user-feedback-23/`.
- **9 separate folders для одной лекции** — смешение per-version + per-feedback-batch.
- **Recommend:** `qa-reports/{date}/{phase-N}-{artifact}-{vN}/` единая структура.

---

## 9. Конкретные рекомендации (приоритезированно)

### P0 (must-fix перед лекцией 2)

**P0-1. Speaker notes — explicit contract в playbook.**
- В `book-editor.md` + `presentation-designer.md` + `tools/lecture-production/README.md`:
  - «Speaker notes for each slide = 150-300 words of READABLE STUDENT TEXT, derived from chapter §X (primary) + speech [sNN] (secondary). NO layout descriptions. NO режиссёрские cues — they go to speech.md or separate `lecturer-cues.md`. Word count enforced.»
- DoD: reader-simulator (mode=rendered) ≥ 26/N self-contained.

**P0-2. Pre-USER-GATE walkthrough by orchestrator.**
- Перед каждым USER GATE (chapter / slides / speech) — orchestrator делает explicit «User-perspective sweep»:
  - Read all slides as PNG (visual scan).
  - Read all speaker notes as student.
  - Read speech as lecturer.
  - List ≥10 issues from this sweep BEFORE presenting to user.
  - Apply quick fixes (P1 cosmetic).
  - **Then** present to user with «I caught these N issues — fixed/pending — anything you'd add?»
- This catches the gap «critics approve, user rejects».

**P0-3. Schema readability checklist в `presentation-designer.md`.**
- Per-schema-type checklist:
  - **Matrix/Quadrant:** axis labels INSIDE quadrant, marker direction-of-scale, точки в углах НЕ overflow, font ≥12pt.
  - **Timeline:** events single-line via em-dash, year labels не пересекают band borders, max 3 per band, pivot year ≥2× font size.
  - **Layered:** common bottom edge (not centred), component labels per layer, не более 4 уровней.
  - **Cycle:** start/end visible, arrows direction obvious, max 6 steps OR compact dialog form.
  - **Pipeline:** RIGHT_ARROW shapes (не filled_rect+triangle), unified language sub-labels.
- DoD: presentation-critic checks checklist explicitly.

**P0-4. Curriculum relevance check в `methodology-critic.md`.**
- Per-slide вопрос: «Зачем студенту лекции N (introductory/intermediate/advanced) этот концепт?»
- Если ответ «evaluate/synthesis-level» в introductory лекции — RECOMMEND DELETE OR DEFER.
- Применять и для chapter sections («§X.Y — для лекции 1 или для семинара 12?»).

**P0-5. Designer no-extra-content rule.**
- В `presentation-designer.md`: «Do nothing the task brief doesn't request. No 'helpful additions' (subtitles, navigation markers, тайминг, лекторские cues). If you see opportunity for improvement — REPORT to orchestrator, не add.»

### P1 (highly recommended)

**P1-1. Terminology drift sub-check.**
- New consistency-checker mode: `terminology-only` — runs at every USER GATE с automated grep по списку «watched terms» (per-lecture: «Приложение-робот», «narrow AI», «ML», etc.).
- Output: «term X has N forms across artifacts» if mismatch.

**P1-2. Verdict scale recalibration.**
- New scale: REJECT / REVISE / APPROVE-WITH-POLISH / APPROVE-CLEAN.
- В each critic agent: «If 5+ P1 — verdict = REVISE, not APPROVE-WITH-MINOR.»

**P1-3. Tools/data freshness pre-flight.**
- В fact-checker для AI-content: для каждого number/benchmark — record «date of source», «typical refresh cadence», «verify on day-of-lecture» если cadence < месяц.
- Generated «freshness report» в qa-reports.

**P1-4. User-positional ↔ slide-ID translation.**
- Orchestrator skill: при receiving user feedback с positional references — explicit translation table (user-pos → slide-ID) before action.
- При presenting changes — «slide 7 (s06 в нашей нумерации) — переделан как ...».

**P1-5. Per-designer file ownership.**
- При spawn-ing parallel designers — каждый получает explicit list slide-IDs (e.g. «You own s07-s11; do not touch s12-s20»).
- File-lock проверка не достаточна.

**P1-6. Pre-flight checklist sync со deck.**
- Pre-flight в speech.md auto-generated на основе deck.yaml — sync points для new slides + removed slides.

**P1-7. consistency-checker запускается до каждого USER GATE.**
- Сейчас Phase 10 only. Move к Phase 4, 7, 10 (после chapter, slides, speech).

**P1-8. Session-end save mandate для всех critic agents.**
- Each agent prompt: «Before completing, MUST save report as file. Path: $REPORTS/{name}-{artifact}-vN.md. If save fails — explicit Write tool retry. If still fails — STOP and report.»

### P2 (nice to have)

**P2-1. Snapshots в .gitignore.**

**P2-2. Build script consolidation.**

**P2-3. QA-reports единая структура.**

**P2-4. workspace-mcp OAuth → production status.**

**P2-5. PowerPoint MCP fork: add `list_shapes`, `update_shape_position`, `delete_shape`.** Эта работа в `notes/mcp-limitations.md` помечена как Fork target — давно planned. Реально boltleneck при 33-slide deck.

**P2-6. Iteration log auto-merger.**
- Все iter-logs в один rolling log с git history = source of audit trail.

**P2-7. Visual loop iteration cap.**
- При 7+ iter без чистого результата — automatic STOP + escalate to orchestrator.

---

## 10. Implementation plan

### A. CLAUDE.md changes

**Add section «Pre-USER-GATE protocol» (under «Phase Gating Rule»):**
```
## Pre-USER-GATE Protocol (ENFORCED)

Before presenting any artefact for USER GATE approval, orchestrator MUST:
1. Visual scan all PNG snapshots (slides) — list issues found.
2. Read all speaker notes as student-perspective — list issues found.
3. Read speech as lecturer-perspective if applicable — list issues found.
4. Apply quick fixes to P2 cosmetic issues identified.
5. Present to user as: «I reviewed and found N issues — fixed M, pending K because [reason]. Anything you'd add?»

This catches issues that critics miss (relevance, schema readability, terminology drift).
```

**Update «Subagent Rules»:**
- Add: «All critic agents MUST save reports as files before completing. Path enforced in prompt. If save fails, agent must Write retry explicitly.»
- Add: «Designer agents do NOT add content not requested in task brief. Improvements are reported, not implemented.»

### B. Agent prompts changes

#### `presentation-designer.md`
- Add **Speaker notes contract** section: «Notes = 150-300 words readable text. NO layout descriptions. Source = chapter §X + speech [sNN]».
- Add **Schema readability checklist** (per slide-type: matrix/quadrant/timeline/layered/cycle/pipeline).
- Add **No-extra-content rule** (do nothing not in task brief).
- Add **5-second test**: «Show your final PNG to mental student. Did они understand main message in 5 seconds?»
- Add **Per-designer file ownership** section for parallel designer spawns.
- Update **Visual loop** with cap rule (7 iter → escalate).

#### `book-editor.md`
- Add **Mark unverified specifics**: any specific number/team-size/timing → `[FACT-CHECK]` if not from primary source.
- Add **Cross-reference to course structure**: when writing footnote like «not goal of course» — explicit check against курс program (Drive doc + lectures.yaml).
- Add **Speaker notes hand-off**: book-editor produces section markers `[for-slide-sNN]` для downstream designer.

#### `speech-writer.md`
- Add **Pre-flight sync rule**: pre-flight checklist в speech sync с deck.yaml additions/deletions автоматически (regenerate from deck).
- Add **Англицизм cleanup pass**: explicit pass after first draft with grep по списку запрещённых англицизмов из chapter-tone-rules.
- Add **Reference user-provided source documents**: course structure, instructor info — read from Drive when relevant.

#### `methodology-critic.md`
- Add **Curriculum relevance check**: per-slide question «Зачем в лекции N (introductory/intermediate/advanced)?»
- Add **Term canonical-validity check**: insider-phrasing detection («рабочее определение», custom-coined terms).
- Add **Англицизмы в tone-analysis section**: specific list per-lecture.
- Add **Designer-added content audit**: «Did designer add content not in task brief? Flag.»

#### `presentation-critic.md`
- Add **Schema readability check** (mirror designer's checklist).
- Add **Cross-slide redundancy grep**: detect duplicate content (bar chart on s04 + s17, etc.).
- Add **«5-second teach test»** for diagrams/schemas: would student understand main message in 5 seconds?
- Update **Verdict scale** (REJECT / REVISE / APPROVE-WITH-POLISH / APPROVE-CLEAN).

#### `consistency-checker.md`
- Add **Terminology drift sub-mode**: `terminology-only` — quick grep across artifacts.
- Update **When to run**: not only Phase 10 — also Phase 4 (after chapter), Phase 7 (after slides) — pre-USER-GATE.

#### `student-simulator.md`
- Add **Explicit «slides to delete» recommendation**: not only «P1 — boring», but «P1-DELETE: this slide should be cut for introductory лекции».

#### `reader-simulator.md`
- Add **Structural blocker assessment** (mode=rendered): «Of N self-contained-fail slides, which are notes-fixes vs structural cuts?»

#### `fact-checker.md`
- Add **Freshness verification**: per-number, record «date of source» + «typical refresh cadence» + «verify on day-of-lecture» if < 1 month.
- Add **User-provided source documents check**: when course structure / instructor info / Drive docs referenced — sync.
- **Mandatory file save**.

### C. Skills changes

#### `.claude/skills/build-deck/SKILL.md`
- Add **Per-designer file ownership** to spawning instructions.
- Add **Schema readability checklist** as orchestrator-level pre-check before spawning designer.
- Add **Pre-USER-GATE walkthrough** as required step before Phase 7 GATE.
- Add **Iteration cap** (7 iter → escalate to user).

### D. tools/lecture-production/README.md changes

- Add **Pre-USER-GATE walkthrough protocol** (mirror to CLAUDE.md).
- Add **Terminology drift check** as Phase 4.5, 7.5, 10.5 sub-phases.
- Add **Curriculum-level metadata** to chapter/slide artifacts: «introductory / intermediate / advanced».
- Update **Phase 7 (slides QA)** to include consistency-checker (currently only methodology + fact + reader/student).
- Add **Section «Speaker notes contract»** explicit format.

### E. tools/presentation-build/README.md changes

- Update **slide-types library**: add per-type readability checklist for matrix/quadrant/timeline/layered/cycle/pipeline.
- Add **Visual readability «5-second test»**.
- Update **anti-patterns каталог** with new entries:
  - #16 — «Designer-added content not in task brief».
  - #17 — «Layout descriptions in speaker notes».
  - #18 — «Color-only highlight + text marker (redundancy)».
  - #19 — «Cross-slide content redundancy (e.g. bar chart on s04 + s17)».
  - #20 — «AI tools/benchmarks без freshness check».
- Add **Per-designer parallel coordination strategy**.
- Update **Visual loop cap**: 7 iter max, then escalate.

### F. notes/decisions.md changes

Add new section **«2026-05-13 — Лекция 1 v3 production lessons»** with:
- Critic blind spots каталог (10 items).
- Designer-added content patterns (что не делать).
- Schema readability per type.
- Terminology drift detection trigger.
- Verdict scale recalibration.
- Pre-USER-GATE walkthrough protocol.

### G. notes/mcp-limitations.md changes

- Add **[NEW] LibreOffice convert overhead at scale** (~5 sec × N slides × M iter).
- Add **[NEW] python-pptx-direct vs MCP-based for full-deck builds** — recommend python-pptx-direct.
- Add **[NEW] MSO_SHAPE proper arrows** vs filled_rect+triangle гибрид — gotcha.
- Update **[#54-1, #54-3]** as P0-PRIORITY-FOR-FORK now (no longer P1-future).

### H. Repository hygiene

- `.gitignore` add: `library/lectures/*/rendered/snapshots/iter*.png` (keep only finalized `sNN.png`).
- Build scripts consolidation: oldest 5 scripts → archive/, keep 1 canonical `build.py` + git history.
- Iteration logs: merge to single rolling `rendered/iteration-log.md` — old version-suffixed logs → git-only.
- QA-reports: rename existing folders to `{date}-phase{N}-{artifact}-v{N}/` schema.
- workspace-mcp OAuth → production status (one-time admin task).

---

## 11. Открытые вопросы для user

1. **Pre-USER-GATE walkthrough — сколько minutes реально investirовать?** 30 минут scroll-through добавят значительный latency. Acceptable trade-off?
2. **PowerPoint MCP fork** — invest 2-3 часа in the fork now, или продолжать build-script-direct approach?
3. **Curriculum levels в metadata** — кто owner за «лекция 1 = introductory, лекция 12 = intermediate»? Нужна mapping in `catalog/manifests/lectures.yaml`?
4. **Pearl + ARC-AGI слайды** — оставлены в финальном deck (user не explicit удалил, оставил после round 3 синтеза). На лекции 2 — проверять «нужны ли concepts evaluate-level»?
5. **Speaker notes vs «Лектору»** разделение — sample показывает что user хотел чисто notes-for-student. Но в run 1 #1 was implied «Лектору» секция в конце notes допустима (как «отдельный блок»). В run 3 #1 «убери раздел для лектора». Финальное правило — без «Лектору» вообще, всё в speech.md? **Confirm.**
6. **Tools/benchmarks freshness** — practical workflow? Lecture-day script `bin/freshness-check.sh` который грепает по списку benchmarks и показывает «outdated» warnings?
7. **Designer-added vs requested split** — strict rule «do nothing not asked» может убить creative input. Где граница между «improvement reported» и «improvement applied»?
8. **Verdict scale change** — хочет ли user видеть REVISE vs APPROVE-WITH-POLISH explicitly, or нужна binary «can show / cannot»?
9. **5 параллельных designers vs 1 sequential** — sequential безопаснее, но дольше. Как принимать решение?

---

## 12. Annex — Top failure mode evidence index

Quick-look reference list of where each failure mode is documented:

| Failure mode | Evidence file |
|---|---|
| User round 1 | `library/lectures/lec-01/qa-reports/2026-05-13-user-feedback-23/REQUIREMENTS.md` (23 fixes) |
| User round 2 (Fix-12-19) | `library/lectures/lec-01/rendered/iteration-log-v31.md` (Fix-12, Fix-14, Fix-15, Fix-16, Fix-17, Fix-18, Fix-19 sections) |
| User round 3 (19 fixes) | `library/lectures/lec-01/rendered/iteration-log-v32.md` (full table) |
| Critic blind spots | `library/lectures/lec-01/qa-reports/2026-05-13-user-feedback-23/SYNTHESIS-slides-v3.md` (12 unique P1) |
| Designer schema readability fails | iteration-log-v31.md «Fix-15» (5 iter for s11) + «Fix-16» (s13 axes) |
| Terminology drift | SYNTHESIS-speech-v3.md КОНВЕРГЕНЦИЯ A («Приложение-робот / -автоматизация / (автоматизация)») |
| Lost reports | `qa-reports/2026-05-13-user-feedback-23/` directory (no fact-checker.md, no consistency-checker.md as separate files) |
| AI tools freshness | SYNTHESIS-slides-v3.md fact-checker P1-8 (ARC-AGI устарело за 2 дня) |
| User-positional confusion | REQUIREMENTS.md §1.#3 («слайд 7 = два определения», у нас s06) |
| Speaker notes layout-description | REQUIREMENTS.md §1.#1 (полное описание проблемы) |
| Designer extras | iteration-log-v31.md Fix-12 (тайминг) + Fix-19 («вы здесь») + iteration-log-v32.md Fix-1 («Лектору» strip) + Fix-2 (s02a subtitle) |
| Speech orphan reference | SYNTHESIS-speech-v3.md P0-1 (s26 pre-flight для удалённого слайда) |
| Англицизмы regression | speech v1 → v2 (после chapter был чистый) |
| Mistral unverified specifics | SYNTHESIS-chapter-v3.md fact-checker «20+ человек / 3 месяца» |
| Roadmap галлюцинация | REQUIREMENTS.md §1.#20 (4 блока vs реальные 3 модуля) |
| Critic verdict inflation | SYNTHESIS-chapter-v3 (10 P1, APPROVE-WITH-MINOR) + SYNTHESIS-slides-v3 (12 P1, APPROVE-WITH-MINOR) |

---

*Конец рефлексии. Готово для review user'ом + переход к implementation.*
