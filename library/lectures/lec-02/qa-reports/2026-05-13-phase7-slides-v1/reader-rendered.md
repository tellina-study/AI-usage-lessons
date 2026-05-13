# Reader-Simulator (mode=rendered) Report on Slides Лекции 2 v1.0 — 2026-05-13

VERDICT: REVISE

## Critical pre-finding (BLOCKER for full mode=rendered review)

**Speaker notes файлов НЕ существует.** Orchestrator brief обещал `library/lectures/lec-02/slides/sNN-*.md` со speaker notes — но в репозитории есть только 28 PNG snapshots в `rendered/snapshots/`. Нет ни `slides/` директории, ни `chapter.md`, ни `deck.yaml`, ни `lec-02.pptx`.

Это означает: я (студент через 2 недели) **не имею текстового конспекта** к слайдам. Только картинки. Реальная reproducible self-study artefact = 0% коммуникации через notes.

Для production lecture это **P0 systemic blocker**: per orchestrator self-containedness threshold (≥85%), notes — half of the equation. Без них слайды должны быть **drastically more self-explanatory**, чем обычно. Mode=rendered review технически невозможен в полном объёме — я оценил каждый слайд **только по visual content**, что эквивалентно худшему сценарию, чем планировалось.

**Recommendation (urgent):** перед closing Phase 7 — generate speaker notes (150-300 слов на слайд) из chapter.md (когда тот появится). До этого review — preliminary, на основе visuals only.

Все оценки ниже — **визуал-only**. Где помечено «self-contained = да» — это означает слайд понятен без notes; где «нет» — без notes критическая дыра, и notes должны её закрыть.

## Self-Containedness count

**Visual-only assessment: 18/28 self-contained (64%).** Threshold ≥24/28 (≥85%) для APPROVE-CLEAN не достигается даже при щедрой оценке.

При условии что speaker notes будут written (150-300 слов на слайд), реалистичный потенциал — 24-26/28, т.е. APPROVE-WITH-POLISH. Сейчас же — REVISE.

## Per-slide self-containedness (table)

| sNN | Self-contained? (visual-only) | Reasoning |
|-----|-----|-----------|
| s01 | да | Live tokenizer 4 примера + кейс strawberry / клубника — main message «модель видит токены, не буквы» виден из самой картинки. Иконично, без слов. |
| s02 | да | Title page — Лекция 2, 4 этапа inference + бейджи Tk→Em→At→Sm + navigation bar. Понятно что это cover. |
| s03 | да | Recap из Лекции 1 §3.2 + что узнаем сегодня. Слой «Модель» подсвечен — ясно что углубляем именно его. Хороший bridge slide. |
| s04 | да | Главный вопрос лекции + 3 obecанных payoff'а с якорями s07/s15/s19. Контрактный слайд работает на 100%. |
| s05 | да | Токен = id из словаря. 3 примера, средний ratio token/char. Иконично. Минимум объяснений нужен от лектора — рисунок говорит сам. |
| s06 | да | BPE Before/After с конкретным mini-vocab. Подпись внизу «BPE-словарь строится один раз до обучения». Достаточно для cold reader. |
| s07 | **нет** | **READ FAILURE.** PNG разрешение слишком низкое — текст в правой колонке «(1) Подсчёт символов / (2) Опечатки / (3) Регистр и пробелы» едва читаем. Через 2 недели я не разберу. **Visual blocker — не notes-fix, нужен redesign (font size).** |
| s08 | да | Bar chart EN/RU/ZH/Python + правая колонка с ratio. Подпись «API-стоимость RU ≈ 2× от EN». Понимаю инженерный вывод. |
| s09 | да | Эмбеддинг = id → vector. Конкретные dim (1536, 3072, тысячи). Геометрическая близость = семантическая. Self-contained. |
| s10 | да | Cosine similarity heatmap 5×5. Подпись «Cosine = угол между векторами, [0,1], ближе к 1 — более похожи». Числа illustrative — disclaimer есть. Хорошо. |
| s11 | да | 3 применения (similarity, clustering, search) с 3 иконками и use cases. Self-contained, ссылка на Раздел 3 курса. |
| s12 | да | Full-text vs Semantic side-by-side с конкретным запросом «клубника». Очень иконично, payoff сам себя объясняет. RAG mention в footer — disclaimer есть. |
| s13 | да | Section divider «Раздел 3 — Механизм внимания». Очевидно navigation. |
| s14 | **нет** | **READ FAILURE.** Малый размер. Заголовок «Attention выдаёт распределение весов на все токены (сумма = 1)» — окей. Но метафора «фонарик в тёмной комнате» — слева quasi-illustration, справа bar chart. Через 2 нед без notes я не пойму **что именно** метафора illustrates и почему 3 bullet справа («все токены контекста / сумма = 1 / пересчитывается на каждом шаге»). **Schema-redesign кандидат.** |
| s15 | **нет** | **READ FAILURE.** «Role-токены получают повышенный вес в attention» — заголовок ОК. Но split-screen «B1. Без роли» vs «B2. С ролью» и attention map sentences — текст совсем мелкий. Без notes payoff на s24 («почему промпт с ролью работает») не реконструируется. **Notes-fix critical, плюс font enlarge.** |
| s16 | да | Контекстное окно log-scale + 3 bar (GPT-3.5 → Claude 3.5 → Claude 4.7). N² badge с подписью «1M ≈ 16× от 100k». Tag [VERIFY-DAY-OF] виден — флаг для лектора, не для студента (это нормально). Self-contained. |
| s17 | да | Lost-in-the-Middle curve + experiment description + результаты. Inженерный вывод «важное в начало или конец, не в середину» жирным внизу. Хорошо. |
| s18 | да | P(next token) bar chart + Top-5 кандидатов с конкретными числами. Контекст «Сегодня я съел…» — понятный пример. Self-contained. |
| s19 | **нет** | **READ FAILURE.** «Температура: насколько острым будет выбор» — 3 mini-charts T=0, T=0.7, T=2.0 + подписи. Текст под графиками еле читаем. Понятие «top-p (nucleus) отрезает редкие токены» в очень мелком тексте — критично для понимания. **Notes-fix + font enlarge.** |
| s20 | да | Таблица «4 ручки API под задачу». Сценарии × temperature × top_p × max_tokens × system_prompt. Очень иконично — engineering reference. Self-contained. |
| s21 | **нет** | **READ FAILURE.** «Loop: предсказали токен → добавили в context → предсказываем следующий». 5 шагов в одной строке, но текст в каждом блоке мелкий. Идея auto-regression — критическая, должна быть rock-solid. **Schema redesign / font enlarge.** |
| s22 | **нет** | **READ FAILURE.** Cross-cutting frame «Local vs Cloud». Текст внутри блоков слишком мелкий, не успеваю прочитать 4 строки модели в каждой колонке + 4 параметра ниже. **Notes-fix не поможет если visual нечитаем — font enlarge required.** |
| s23 | да | «4 этапа inference сложились в pipeline» — Tk→Em→At→Sm с описаниями и slide ranges. Хороший recap. Self-contained. |
| s24 | да | «3 промиса Лекции 1 — 3 ответа из Лекции 2». Payoff §5.3 с прямыми объяснениями: role → attention веса, strawberry → токены, sampling → variance. Контрактное замыкание работает на 100%. |
| s25 | **нет** | **READ FAILURE.** Cross-cutting frame ML vs LLM decision tree. 3 ветки с примерами (logistic, XGBoost / interpretable / time-critical). Текст в каждой ветке мелкий. Через 2 нед без notes не реконструирую границы applicability. **Notes-fix + font enlarge.** |
| s26 | **нет** | **READ FAILURE.** Cross-cutting frame Human vs AI causality. Перлы каузальности уровни 1-3 (ассоциация / вмешательство / контрфактуальность) — это **философско-методическое содержание Лекции 1 §4.8**. Без notes и без callback к §4.8 я не вспомню что означают «контрфактуальность нет». Слишком мелкий текст + heavy concept = **критический notes-fix candidate.** |
| s27 | частично | Домашка с 3 шагами. Главное считывается: 1 запрос × 3 температуры × 3 запуска × анализ. Хороший framework. НО — «Применяет LO4 + LO6 + LO7» в подзаголовке — *что это за LO?* Я как студент через 2 недели уже не помню номерацию LO. **Inline expansion needed.** Также [VERIFY-DAY-OF] о HF Playground availability — для меня (студента) нерелевантно, должно быть hidden. |
| s28 | да | Тизер Лекции 3: RAG, Tools, MCP, Agent loop. 4 квадрата с короткими определениями. Self-contained как teaser. Q&A footer — нормально. |

**Итог visual-only:** 18 self-contained, 10 not self-contained (s07, s14, s15, s19, s21, s22, s25, s26 — read failures; s27 — partial).

## Structural Blocker Assessment

Of 10 self-containment failures, classification:

### Schema redesign / font enlarge (8 slides — НЕ просто notes-fix)
- **s07** — strawberry breakdown, font в правой колонке нечитаем
- **s14** — attention метафора + bar, дуальный layout нечитаемый при rendered size
- **s15** — split-screen B1/B2 role, текст мелкий
- **s19** — 3 mini-charts температуры, подписи мелкие
- **s21** — 5-шаговый auto-regressive loop, блоки нечитаемы
- **s22** — Local vs Cloud cross-cutting frame, текст мелкий
- **s25** — ML vs LLM decision tree, ветки нечитаемы
- **s26** — Human vs AI causality cross-cutting, нечитаемо + heavy concept

**Root cause:** для significant portion слайдов содержимое перегружено относительно canvas. Шрифт 14-16pt вместо minimum 20pt для rendered presentation. Это **systemic issue**, не локальный фикс.

### Notes-fix (1 slide)
- **s27** — раскрыть LO4/LO6/LO7 inline («LO4 = подбор параметров под сценарий обоснованно, LO6 = …»), убрать [VERIFY-DAY-OF] tag из student view.

### Structural cut (0 slides)
Никаких слайдов для cut — каждый имеет место в curriculum, проблема в исполнении (font / density), не в концепции.

## Promise §5.3 cohesion (through visible content)

**Setup на s04 ("Главный вопрос лекции")** — есть 3 ясно сформулированных вопроса с явными якорями на s07/s15/s19.

**Payoff на s24** — 3 промиса × 3 ответа side-by-side, прямые объяснения по каждому. Структурно contract замкнут.

**Однако:** payoff slide s24 self-contained, но dependent на s15 и s19, которые сами **NOT self-contained** из-за font failures. Если студент не понял s15 (role-токены и attention map), то s24's claim «role-токены получают высокий вес в attention» = ungrounded.

**Verdict promise cohesion:** **structurally good, executionally compromised** через s15/s19 read-failures. Cohesion работает только если studen использует слайды для memory-jog, а не для cold reconstruction. Через 2 нед — спорно.

## Cross-cutting frames self-containedness

Все 3 cross-cutting frame'а имеют **read failures**:

1. **s22 (Local/Cloud)** — концепт ясен из заголовка («Inference loop одинаков локально и в облаке — но размер модели определяет качество»), но конкретные модели (Qwen 2.5 1.5B, Llama 3.2 1B и т.д. + GPT-5, Claude 4.7 etc.) и параметры (приватность/скорость/контекст/цена) нечитаемы без font enlarge. Frame works at high level — fails at detail.

2. **s25 (ML vs LLM)** — заголовок «LLM — не всегда правильный инструмент. Decision tree» ОК. Идея 3 веток (классификация / интерпретируемость / latency) понятна. Но конкретные criteria («классы (5-20)?» / «regulated финансы/мед/страхование» / «<100мс») мелкие, плюс это decision-critical content для production use — не fluff. **Высокая стоимость notes-fix.**

3. **s26 (Human/AI)** — это самый концептуально-нагруженный cross-cutting (Pearl уровни каузальности, callback на Лекцию 1 §4.8). Если я через 2 нед не помню Лекцию 1 §4.8, то «1. Ассоциация / 2. Вмешательство / 3. Контрфактуальность» = пустые слова. Inline disclaimer needed.

**Все три frame'а** — relied on chapter context (§4.8 Лекции 1), которого у меня нет. **Без notes — критическая дыра.**

## Domashka s27 clarity (2-week-later perspective)

**Что я понимаю через 2 нед:**
- Framework: 1 типовая задача × 3 температуры × 3 запуска × анализ = 9 generations + сравнение.
- Tool: HuggingFace Playground (есть fallback на Together.ai / Ollama локально).
- Бонус: "строгая регуляризация" × 3 модели — explain через §1.3 (токенизация).

**Что я НЕ понимаю:**
- «applies to LO4 + LO6 + LO7» — какие именно learning outcomes? Если я не делал хорошие заметки в Лекции 0 или у меня нет syllabus открытого — это just цифры. **Inline expansion критичен.**
- «оцени variance» (под Шагом 2) — что именно сравнивать? Длину ответа? Содержание? Какие метрики? Vague instruction.
- «бонус: объяснить через §1.3» — §1.3 это где? «Токенизация» из Лекции 2 я помню как Раздел 1 — но «§1.3» как обозначение? Cross-ref puzzle.

**Verdict s27:** **частично actionable, нужны 2 inline уточнения.** Framework сам — норм. Cross-refs к LO и §-нумерации — confusing without notes.

## Top-5 fixes (for Phase 8)

1. **(P0) Generate speaker notes for all 28 slides** (150-300 слов каждый) из chapter.md. Без notes mode=rendered review не работает — это **обязательное condition для production deck**.

2. **(P0) Font enlarge / layout redesign на 8 слайдах** (s07, s14, s15, s19, s21, s22, s25, s26). Это **systemic visual issue** — не локально. Минимум 20pt body text, 24pt в схемах. Сейчас многие слайды реально не читаются на rendered scale.

3. **(P1) s26 — expand inline disclaimer Pearl-уровней** («Ассоциация = X и Y часто вместе / Вмешательство = X→Y / Контрфактуальность = было бы Y, если бы не было X»). Сейчас 3 термина без определения локально. Через 2 нед без §4.8 в активной памяти — мёртвый текст.

4. **(P1) s27 — expand LO4/LO6/LO7 inline** (1 строка на каждый). Уточнить «оцени variance» — конкретная метрика (длина? lexical diversity? semantic distance?). Убрать [VERIFY-DAY-OF] tag из student-facing version.

5. **(P2) s22/s25 cross-cutting frames** — добавить one-sentence «what to take away» в подвале каждого. Сейчас frame self-claims (приватность / интерпретируемость), но «когда выбирать локальное» / «когда не LLM» — engineering decision должно быть named explicitly в нижней stripe.

## Counter-check

- **≥5 P1 issues но verdict APPROVE-WITH-POLISH?** — НЕТ. У меня 2 P0 (отсутствующие notes + font failures) + 3 P1 = верный verdict **REVISE**, не APPROVE-WITH-POLISH.
- **Self-containedness 18/28 = 64%** — это **жесткий REVISE** per threshold (20-23/28). Даже если notes починят 10 слайдов до 28/28, font issues на 8 слайдах требуют design pass — это не «polish», это substantive iteration.
- **Cross-check с methodology-critic / presentation-critic:** не сравниваю (я не видел их reports). Сужу только по ridership perspective: «через 2 нед готовлюсь к РК — могу или не могу?» — **сейчас не могу для 36% слайдов**.
- **Sequence check:** logical flow s01→s28 (icebreaker → cover → recap → contract → 4 секции → recap pipeline → payoff → cross-cuts → домашка → teaser) — clean. Pacing-wise — 28 слайдов на 75 мин = 2.7 мин/слайд = normal.
- **No structural cuts recommended** — каждый слайд on-curriculum.

---

**Итоговый recommendation для Phase 8:**
1. Write speaker notes (150-300 слов на каждый из 28 слайдов).
2. Redesign 8 read-failure слайдов: font enlarge до 20pt body, упростить layout где needed (s14, s21, s26).
3. Local fixes на s27.
4. Перезапустить mode=rendered review после исполнения 1-3.
