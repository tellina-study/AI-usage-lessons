# Methodology-Critic Report on Plan v1 Лекции 2 — 2026-05-13

VERDICT: REVISE

## Summary

Plan v1 — крепкий черновик: backbone (4 концепта токены/эмбеддинги/attention/температура) выстроен корректно, payoff §5.3 Lec-1 (3 «почему») явно прописан в s28, retrieval moments распределены (5 интерактивных точек на 75 мин), glossary lock включён, forbidden-additions catalog присутствует. Однако v1 **не compliant с user-locked constraints от 2026-05-13** по нескольким измерениям. Главные failure modes: (1) 3 cross-cutting frames (ML vs LLM / local vs cloud / human vs AI) **полностью отсутствуют** — это P0 gap по §1 constraints; (2) slide count 31 > target 28-30 — нужен резерв на 3 cross-cutting слайда, итого надо вырезать ~4-5 слайдов; (3) одна явная Bloom-overshoot позиция (s06 BPE worked example) и две на грани (s22 distribution + s19 multi-head); (4) минимум 2 канонически слабых термина в glossary («миопия токенизации», «магнит attention»); (5) factual freshness — 5 цифр (GPT-4 96 heads, embedding dims 12288, vocab sizes, Gemini 2M, Claude 4.7 1M) требуют hard verify-on-day, plan не маркирует ни одну `[FACT-CHECK]`. Verdict REVISE: до chapter draft нужны решения по cross-cutting placement + final slide list (28-30) + Bloom downshift s06.

---

## P0 Issues (must fix перед chapter draft)

### [P0-1] Cross-cutting frames полностью отсутствуют — нарушение constraints §1

**Issue:** `plan-v2-constraints.md` §1 явно требует 3 cross-cutting frames (по 1-2 слайда каждый): ML vs LLM decision tree, Local vs cloud trade-off, Human vs AI. В plan v1 эти три темы **не упомянуты ни в арке §2.2, ни в slide list §4-§9, ни в LO §3**. Это нарушение hard-locked scope decision.

**Evidence:** plan v1 §2.2 арка содержит только 6 этапов (0. Открытие, 1. Токенизация, 2. Эмбеддинги, 3. Внимание, 4. Сэмплинг, 5. Заключение). Slide list s01-s31 не имеет ни одного слайда «ML vs LLM», «локально vs облако», «AI vs человек».

**Recommendation:**
- **ML vs LLM decision tree → s30a (перед s30 или после s28)**, как user lean §6.10 запрашивает («когда LLM, когда классика»). 1 слайд, тип `summary`, обновляет §1.4 Lec-1 (задача × модальность) кратким callback и добавляет диагностический вопрос «нужен ли вам собственно LLM?». NB: это явный пункт «когда не LLM» — payoff §5.3 Lec-1 promise, что лекция 2 объясняет именно большие модели, не replacement для classical ML.
- **Local vs cloud → встроить как 1 слайд внутрь Раздела 4 «Сэмплинг»** между s25 и s26. Тип `assertion_visual`, assertion: «Inference loop одинаков локально и в облаке — но размер модели определяет качество». Callback к §4.2 Lec-1 (без повтора). Не более 1 минуты — иначе риск повтора §4.2.
- **Human vs AI → 1 слайд в Заключении**, между s28 и s29 (новый s28a). Assertion: «Attention статистически смотрит, не понимает причинности — см. Lec-1 §4.8». Это не повторение Pearl, а **закрытие петли**: «теперь когда знаешь механику — почему §4.8 говорит, что AI на уровне 1 Pearl». 1 минута.

**Affected slide count:** +3 слайда → план становится 31+3 = 34. Это конфликтует с P0-2 (cut to 28-30). Резюме обоих: cut 4-6 слайдов из v1 list, добавить 3 cross-cutting → final 28-30.

---

### [P0-2] Slide count overshoot vs constraint (31 > 28-30 target) + сейчас усугубляется добавлением 3 cross-cutting

**Issue:** constraints §1 явно: «target 28-30». Plan v1 = 31 (сам признает в §15 Q9). С добавлением 3 cross-cutting (P0-1) — становится 34. Нужно cut ≥4 для final 30, лучше -6 для final 28 с запасом.

**Evidence:** §2.2 итог «Итого: 31 слайд» + §15 Q9 «Перебор?»

**Recommendation:** конкретные cut кандидаты (см. секцию «Slide cut candidates» ниже). Минимум cut s09, s14, s19, s24 — это 4 слайда, plan становится 31-4+3 = 30. С дополнительным cut s11→ 29, cut s06→ 28.

---

### [P0-3] LO4 (parameter tuning) недостаточно покрыт vs его весомость в LO mix

**Issue:** constraints §3 явно требует LO4 в final mix. Plan v1 §3 формулирует LO4: «подобрать параметры запроса (`temperature`, `top_p`, `max_tokens`, `system prompt`) под конкретный сценарий». Но `max_tokens` упомянут только в glossary (§10), нигде нет slide-объяснения; `top_p` — только в s24 (которая в cut-кандидатах); `system prompt` обсуждается в s18 (роль) и в seminar (s29), но не как параметр LLM API. LO4 размазан, без явной сборки.

**Evidence:** s25 «Когда что использовать» матрица 4×3 объединяет parameters, но это **summary**, не teaching slide для самих параметров. Студент не получает clear «вот 4 ручки → вот когда какую крутить» в дидактическом режиме.

**Recommendation:** усилить s25 как teaching slide (не summary): добавить колонку «`max_tokens` typical» и явно tag «это LO4 payoff». ИЛИ — раздать LO4 на 2 слайда: s23 «температура» + новый s25 «4 ручки API: T / top_p / max_tokens / system prompt — когда что» (текущий s25 объединить с s24 в этой версии). Without LO4 explicit recap student-friendly — LO4 не достигается.

---

### [P0-4] Cumulative cognitive load в Разделе 3 (attention, 7 слайдов / 18 мин, 6 новых концептов)

**Issue:** Раздел 3 = s15 (divider) + s16 attention base + s17 worked example + s18 role-effect + s19 multi-head + s20 context window + s21 long-context fails. 6 content slides + 6 новых концептов (attention itself, attention map, role-attention, multi-head, context window, lost-in-middle) за 18 минут — 3 концепта/мин — **2-3× выше стандарта 3-5 концептов / 5 минут** (см. methodology-critic checklist). Cognitive overload для introductory.

**Evidence:** §2.2 «Раздел 3 — 18 минут / 7 слайдов». §5 forbidden additions запрещает формулы / Q-K-V, но это не решает density новых understanding concepts.

**Recommendation:**
- Merge s17 + s18 в один (constraint §6.4 user lean уже это говорит).
- Cut s19 multi-head (см. P1-1 ниже) — multi-head technically важен для архитектуры, но НЕ для introductory LO mix. Если student должен запомнить только одно про attention — это «фонарик», не «много фонариков».
- Result: 18 мин / 5 content slides (s16, s17+s18 merged, s20, s21) = 4 концепта за 18 мин. Cognitive load становится приемлемым.

---

### [P0-5] Hook s01 (live tokenizer demo) — risk единственной точки отказа на старте

**Issue:** s01 — `live_demo` на интернете. План указывает «backup: статический скриншот, если интернета нет». Но 3 минуты на live demo в первые 5 минут лекции — это **30% времени hook'а** на тех-риск. Если интернет дёргается / Tiktokenizer down (известный сторонний сервис, не Anthropic-controlled) → лекция стартует с провалом.

**Evidence:** s01 «3 мин. **Backup:** статический скриншот, если интернета нет.»

**Recommendation:**
- **Hard:** заранее сделать high-quality static screenshot 4 примеров (cat / tokenization / клубника / 🍓) → положить в `assets/`. Это primary visual; live tokenizer — optional «if works».
- **Speaker note:** «если есть интернет — можно открыть Tiktokenizer и показать live; если нет — статика этого слайда».
- Сократить s01 до 2 мин (1 мин на 4 примера + 1 мин на «and now you'll see what this means»).

---

## P1 Issues (заметно вредит обучению)

### [P1-1] s19 multi-head — Bloom overshoot для introductory + не payoff'ит ни один LO

**Issue:** Multi-head attention — Apply-Analyze concept (понять что несколько «голов» делают разное одновременно — требует абстракции «параллельной декомпозиции внимания»). Для introductory (Bloom: Remember/Understand/Apply) — overshoot. Также: ни LO1 (4-этап pipeline), ни LO4 (parameters), ни LO6 (limitations), ни LO7 (3 почему) **не зависят от multi-head**.

**Evidence:** s19 «96 голов в каждом слое. В Claude 3.5 — ~64-128.» — это цифровой факт; assertion «Несколько голов смотрят на разные аспекты» — overstatement (на самом деле head specialisation эмерджентна, не дизайн-заявлена; см. Voita et al. 2019, Clark et al. 2019 — это open research, не settled).

**Recommendation:** **CUT s19**. Если нужно упоминание — single sentence в speaker note s16: «Attention в реальной модели — не один, а ~64-128 параллельных "голов" в каждом слое; детали — Лекция 17 ⁄ дополнительное чтение». Этого достаточно для honesty.

---

### [P1-2] s06 BPE worked example — Bloom overshoot (Analyze/Understand-Apply boundary)

**Issue:** Worked example BPE с пошаговой итерацией (3 шага слияния `e+s`, `es+t`, ...) — это Analyze-level (студент следит за алгоритмом). Для introductory лекции достаточно «BPE — компромисс char vs word», без alg trace. Также: BPE — НЕ единственный токенизатор (есть WordPiece у BERT, SentencePiece у LLaMA / T5); plan v1 не упоминает alternatives, что создаёт неверное впечатление «BPE = токенизация».

**Evidence:** s06 visual «Простой worked example: 3-шаговая итерация BPE на мини-корпусе» + 3 шага слияния.

**Recommendation:**
- **Replace** worked example на **before/after**: «`low / lower / newest / widest` → словарь после BPE: `low / er / new / est / wid`». Без trace шагов merge. Тип `comparison`, не `assertion_visual+trace`.
- Add 1 строку в notes: «Современные tokenizers — варианты BPE (GPT) / WordPiece (BERT) / SentencePiece (LLaMA, T5). Различия — для глубокого dive, см. Лекция 17 / дополнительное чтение.»
- Time s06: 3 мин → 2 мин.

---

### [P1-3] Glossary §10 «миопия токенизации» — insider phrasing, не canonical

**Issue:** Plan v1 §3 LO6 формулирует ограничения как «миопия токенизации, конечное контекстное окно, стохастичность сэмплинга». Термин **«миопия токенизации»** — не canonical в литературе. Hugging Face, Karpathy («Let's build the GPT Tokenizer»), OpenAI cookbook употребляют: «character-blindness», «subword opacity», «sub-token aggregation issue». Русский canonical — «модель не видит букв», «слепота на уровне символов», «subword-агрегация».

**Evidence:** §3 LO6: «миопия токенизации». §10 glossary не определяет этот term.

**Recommendation:** заменить термин на **«слепота к буквам»** или **«subword-агрегация (модель видит подслова, не буквы)»**. Verify finally через Google Scholar / Karpathy lecture transcripts before chapter draft. Plan v2 — explicit alias list.

**Risk:** если оставить «миопия токенизации» — user или fact-checker flag «что за миопия ты выдумал».

---

### [P1-4] Glossary §10 «магнит attention» (в s18 gold callout) — metaphor risk

**Issue:** s18 visual: «Роль = "магнит" attention для следующих токенов». Metaphor «магнит» — не canonical в attention literature. Существует canonical metaphor «фонарик» (используется в s16 уже). Микс «фонарик» (s16) + «магнит» (s18) → student confusion: какая metaphor правильная?

**Evidence:** s16 «Метафора "фонарик в тёмной комнате"». s18 «Роль = "магнит" attention».

**Recommendation:** unify metaphor. Использовать **«фонарик»** всюду: в s18 — «роль-токены становятся ярче подсвеченными для следующих токенов» (одна metaphor). «Магнит» вычеркнуть.

---

### [P1-5] s11 Word2Vec king-queen — устарел и работает не как студент ожидает

**Issue:** Plan v1 §15 Q3 сам flag это. Word2Vec 2013, и сегодня:
1. Современные embeddings (text-embedding-3-small, sentence-transformers, Cohere) **не подчиняются** этому аналогийному соотношению так чисто, как Word2Vec — это специфика старой архитектуры.
2. Студенты, прочитавшие Karpathy или Bloomberg, увидят «king - man + woman ≈ queen» как cliché-пример.
3. На RU-эмбеддингах король-королева-мужчина-женщина даёт **inconsistent** результаты в зависимости от модели — student попытается воспроизвести → разочарование.

**Evidence:** §15 Q3 уже flag, constraints §6.2 lean = «mix Word2Vec + современные».

**Recommendation:** заменить на современный sentence-similarity example. Пример: 5 предложений с разной семантикой («Как настроить SSL» / «Установка HTTPS-сертификата» / «Сборка React-компонента» / «Рецепт борща» / «Деплой React») → cosine similarity matrix (heatmap или просто числа). Видно: ssl ↔ https → 0.85, React-сборка ↔ React-деплой → 0.78, что-то-vs-борщ → 0.05-0.15. Это honest и работает на любых современных embeddings.

Word2Vec king-queen — 1 строка в speaker notes как «исторический прорыв 2013, Mikolov», не central visual.

---

### [P1-6] Plan v1 §13.2 — анти-pattern phrasing «промптинг — сквозной навык»

**Issue:** §13.2 содержит фразу «**«Промптинг — сквозной навык»** — role-effect через attention». Lec-1 reflection (anti-pattern #18) явно flag фразы типа «X — сквозной навык» как marketing-tone. Plan v1 §1.5 правильно говорит «без триумфального тона», но §13.2 это нарушает.

**Evidence:** §13.2 «✅ **«Промптинг — сквозной навык»** — role-effect через attention, temperature-tuning под задачу.»

**Recommendation:** перефразировать §13.2 в neutral tone: «Промпт-параметры (роль, температура) разбираются в Лекции 2 на уровне механики; систематизация промптинга — Семинар 12 PARTS».

---

### [P1-7] s07 retrieval moment — рисково методически (студент с телефоном проверяет → может получить «AI знает 3 r», т. к. модели улучшились)

**Issue:** s07 retrieval moment: «попробуйте сейчас на телефонах ChatGPT/Claude — сколько 'r' в 'strawberry'?» — это classic 2023-2024 example. Но в 2026 многие модели обучены распознавать этот edge case (OpenAI явно публиковал fix в GPT-4o; Claude 3.5 Sonnet с reasoning может правильно ответить). Если half аудитории получает «3» — методический payoff (модель ошибается → токенизация причиной) ломается.

**Evidence:** s07 «retrieval moment».

**Recommendation:**
- **Lecturer pre-test:** за день до лекции лектор сам проверяет 3 топовых модели (ChatGPT-5, Claude 4.7, GPT-4o) на этом промпте. Если ВСЕ отвечают правильно — replace example на «сколько 'я' в "выявить"» / «сколько 'о' в "методология"» / «зашифруй ROT-13 'strawberry'» (всё ещё ломается на character-level).
- Alternative example в speech notes: ARC-AGI style char counting / reverse string («переверни 'methodology' посимвольно») — продолжает ломаться.
- Lecturer brief должна явно flag: «этот example — проверь day-of».

---

### [P1-8] s20 context window timeline — Tools/Benchmark Freshness P0

**Issue:** s20 bar chart context windows (GPT-3.5 4k, GPT-4 8k→32k, Claude 2 100k, Claude 3.5 200k, Gemini 1.5/2.5 1M-2M, Claude 4.7 1M). Это **AI-domain быстро-обновляемый факт** (refresh cadence: quarterly). Лекция 2 — date TBD (probably сентябрь-октябрь 2026). Между мая 2026 (draft date) и осенью 2026 — Anthropic / OpenAI могут анонсировать 5M+ context, или Gemini 10M. Plan v1 §14 правильно flag «Claude 4.7 1M context — already in Lec-1», но **timeline as bar chart** требует hard verify-on-day для **всех** позиций.

**Evidence:** s20 «Bar chart progression» с 6 точками + Claude 4.7 cite Lec-1 §1.3.

**Recommendation:**
- Tag s20 explicit `[VERIFY-ON-LECTURE-DAY]` в slide notes.
- Add explicit fallback: если на лекции outdated, ОК сказать «эта цифра уже устарела, актуальная X — но порядок 100k→1M остался, и квадратичная стоимость attention не зависит от точных цифр».
- Reduce timeline до 3 points (GPT-3.5 2022, Claude 3.5 2024, Claude 4.7 2026) — меньше точек = меньше risk одной обозреть.

---

### [P1-9] Curriculum cross-reference: «прогрессия промптинга» (s18 → Сем 12 PARTS) — Сем 12 ≠ Лекция 12

**Issue:** §13.1 говорит «Семинар 12 PARTS», но плановая структура курса (см. Lec-1 §5.2 chapter) употребляет «лекция 12». Семинар != Лекция в курсе. План создаёт расхождение reference.

**Evidence:** §13.1 «к **systematic frameworks** (Семинар 12 PARTS).»

**Recommendation:** verify в `catalog/manifests/lectures.yaml` или Lec-1 §5.2, какое именно (лекция 12 ИЛИ семинар 12) разбирает PARTS. Fix reference. Если не определено пока — written: «Лекция 12 / Семинар 12 — TBD».

---

### [P1-10] s28 payoff cards: assertion в card #1 («Attention распределяется на role-токены») — потенциально неверная formulation

**Issue:** Card #1 в s28 говорит: «**Почему промпт с ролью работает лучше?** → Attention распределяется на role-токены; они становятся "магнитом" для последующих». Это **simplified mechanism**, который в research literature не доказан как ТОЧНЫЙ объяснение role-effectiveness. Альтернативные / complementary объяснения: (a) role-tokens shift hidden state in retrieved direction (in-context steering), (b) role primes более consistent token distribution в training data (RLHF effect, не attention specifically), (c) role меняет priors via system-prompt-specific finetuning.

Honestly: «attention-based explanation» — popular pedagogical metaphor, но не settled science. План в s18 + s28 повторяет это как hard fact.

**Evidence:** s18 + s28 + LO7.

**Recommendation:** softer phrasing в slides и chapter: «Role задаёт контекст, на который модель опирается при выборе следующих токенов — **на уровне attention** мы видим, что role-токены имеют более высокий вес». В speaker note explicit: «Это упрощённое объяснение; альтернативно — role triggers in-context steering на уровне hidden states. Для introductory достаточно intuition.» — fact-checker / chapter author needs to be careful with «hard claim».

---

### [P1-11] Glossary §10 — отсутствует «авторегрессионный» canonical justification

**Issue:** §10 glossary включает «авторегрессионный (autoregressive в скобках 1×)». Это canonical, OK. Но «авторегрессионный» в русской AI-литературе **не повсеместен** — также используются «авторегрессивный» (без -онн-) и «авто-регрессионный» (с дефисом). Без явного выбора canonical form — будет drift между chapter / slides / speech.

**Evidence:** glossary §10 row 14.

**Recommendation:** verify через Hugging Face docs Russian / ru.wikipedia.org «авторегрессия» / Yandex AI publications. Choose ONE form, lock в glossary, alias forbidden list для остальных.

---

### [P1-12] s17 worked example — потенциальный «AI thinks like a grammar» miscue

**Issue:** s17 visual: предложение «Кот съел мышь, потому что она была голодна» — стрелки от «она» к «мышь» (толстая), «была» (средняя), «голодна» (тонкая). Plan v1 правильно flag в notes «модель не делает грамматический разбор — она статистически смотрит». Но visual со стрелками к anaphora resolution **выглядит** как grammar-parsing. Risk: student walks away thinking attention = parser.

**Evidence:** s17 + 2-3 sentences speaker note.

**Recommendation:**
- Add 2-й example в s17, где attention НЕ соответствует grammar: например, «Программа упала, потому что **она** забыла обработать null» — здесь модель смотрит на «упала» и «null» (статистически частые), не на «программа» (grammatically antecedent of «она»). Этот retrieval moment УЖЕ embedded в s17 — но his result (куда модель смотрит) **не показан**. Add 2nd visual после retrieval reveal.
- ИЛИ honest disclaimer над visual: «упрощение: реальная attention map содержит сотни связей; здесь показаны 3 самых сильных».

---

## P2 Issues (мелочи)

### [P2-1] s02 «cover» (0.5 мин) + s02a «карта» (0.5 мин) — split на 2 slides ненужен

Cover + roadmap в Лекции 1 объединены (с маркером «вы здесь»). Лекция 2 split — без явной причины. **Merge** в один s02 «Cover + roadmap» с roadmap-баром внизу слайда. Cuts 1 slide; помогает P0-2.

### [P2-2] s22 distribution example — стоит выбрать менее ambiguous

Distribution example «Кот сидит на ...» → токены `стуле`, `столе`, `подоконнике`, `диване`. **Все** четыре — реалистичные продолжения, distribution top-4 будет flat. Это ослабляет teaching point «модель ВЫБИРАЕТ из nuanced distribution». Better example: «Сегодня я съел ...» → дисбаланс яркий (food items dominate).

### [P2-3] §15 Q1 self-resolved уже в constraints §3 — vestigial

Plan v1 §15 Q1 («добавлять LO6 или нет») уже разрешён в constraints §3 (full mix LO1+LO4+LO6+LO7). При plan v2 — remove vestigial open question.

### [P2-4] §13.3 industries mention — phrasing «универсальная лекция»

§13.3: «Лекция 2 — универсальная (не привязана к индустрии). По принципу course-narrative "Каждая лекция — одна индустрия" это исключение». OK тонально, но добавить explicit: «как и Лекция 1 (диагностическая), Лекция 17 (синтез сквозных паттернов)» — student understands исключения systematically, не ad-hoc.

### [P2-5] Glossary §10 — отсутствует «in-context»

В s18 (роль), s26 (авторегрессия), s17 (worked example) — все опираются на концепт «контекст растёт по мере генерации». Glossary не lock «in-context» / «контекст» / «контекстное окно» (есть, ok) **vs** «текущий контекст в цикле inference». Будет drift между «контекстное окно» (size limit) и «контекст» (актуальное содержимое). Add row.

---

## 10 Open Questions Resolution

### Q1 (LO6 mix): **Agreed with user lean.** Full mix LO1+LO4+LO6+LO7. LO6 не требует доп. слайдов (s07, s09, s20, s21 уже покрывают limitations). Plan v2 — vestigial remove §15 Q1.

### Q2 (Hook s01 tokenizer demo vs CV callback): **Agreed with user lean — tokenizer demo.** Reasoning: новая лекция → новый hook. CV callback повторяет Lec-1 (cognitive recall) и тратит первые 3 минуты на «возврат», что снижает forward momentum Лекции 2. **Critical adjust:** P0-5 — реализовать static-screenshot-first, live-demo-optional. Не зависеть от интернета.

### Q3 (s11 Word2Vec классика vs современные embeddings): **Disagree user mix lean. Recommend ONLY sentence-similarity современные.** Reasoning P1-5: студенты в 2026 видели Word2Vec king-queen в каждом популярном объяснении эмбеддингов; это cliché, не teaching value-add. Реальный insight — semantic similarity на коротких предложениях (что они будут реально использовать в RAG / search). Word2Vec — 1 строка в speaker notes как историческая отметка.

### Q4 (s14 multimodal sustain 2 мин vs 1 мин): **Agreed with user lean — 1 мин cut.** Multimodal embeddings (CLIP, ImageBind) методически relevant, но cognitive load в Разделе 2 уже plotно. 1 minute mention достаточно. **Alternative consideration:** cut s14 entirely (не нужно для LO1/4/6/7 ни одного), упомянуть multimodal в s30 (preview Лекции 3) — это free slide. **Recommend** evaluate vs slide budget: если final list уже на 30 при добавлении 3 cross-cutting — cut s14 entirely.

### Q5 (s17 vs s18 merge): **Agreed with user lean — merge.** P0-4 + P1-12 backing. s17 worked example + s18 role-effect — две части одного teaching point (attention видна на example → role меняет attention pattern). Merge в один slide ~5 мин с структурой: «attention visual» (1 мин) → retrieval moment (30 sec) → «теперь role меняет это» (2 мин) → callback к Lec-1 §5.3 promise (30 sec).

### Q6 (s21 long-context fails): **Agreed with user lean — keep, 2 мин max.** Reasoning: Lost-in-the-middle (Liu et al. 2023) — practical inference fact, hits LO6 (limitations) и LO7 (engineering implication: place important info at edges, not middle). Это distinguishes лекцию от «attention magic». **Important:** verify (Liu 2023 paper is canonical; arXiv 2307.03172). Already cited в plan v1 §14.

### Q7 (s24 top-p/top-k merge с s23): **Agreed with user lean — merge.** Reasoning: top-p и top-k — variants одного механизма (truncate distribution tail). Standalone слайд для introductory — overshoot. Merge с s23: temperature visual + 1 строка «есть также top-p (nucleus) и top-k — альтернативные способы truncate; на практике достаточно настраивать T для start». s24 cut. Помогает P0-2.

### Q8 (Tone explanatory vs wow): **Agreed with user lean — explanatory-engineering.** Reasoning: Lec-1 был «диагностический» (where AI works / fails, что инженеру решать); Лекция 2 должна быть «explanatory» (внутренний механизм объясняет наблюдаемое). «Wow» tone конфликтует с Lec-1 «без магия LLM» (§5.3, §1.3). Также «wow» — pattern из tech-blog-ов; academic lecture для 3 курса должна быть строже.

### Q9 (slide count 31 → 28-30): **Agreed with user lean — target 28-30.** P0-2 detailed cut recommendations. После всех cuts + 3 cross-cutting add — итого 28-30.

### Q10 (ML vs LLM tree placement s30): **Agreed with user lean — placement near s30**, но **between s28 (3 почему) and s29 (homework)**. Reasoning: «когда не LLM» — payoff после deep dive (logical: «теперь когда знаешь как работает — понимаешь, что не везде это нужно»). До s29 (домашка про temperature). Это natural narrative pivot перед homework и мостом к Лекции 3.

---

## Cross-cutting frames placement (since plan v1 doesn't cover)

| Frame | Slide | Placement | Time | Type |
|---|---|---|---|---|
| ML vs LLM decision tree | **s28a** (NEW) | После s28 (3 «почему»), перед s29 (homework) | 1.5 мин | `summary` + decision tree visual |
| Local vs cloud trade-off | **s25a** (NEW) | После s25 (parameter matrix), перед s26 (autoregressive) | 1 мин | `assertion_visual` callback to Lec-1 §4.2 |
| Human vs AI («attention ≠ понимание») | **s28b** (NEW) | После s28a (ML vs LLM), перед s29 | 1 мин | `assertion_visual` callback to Lec-1 §4.8 |

**Total cross-cutting add: +3 slides / +3.5 min.**

**Narrative justification:**
- s25a (local/cloud) — natural в Разделе 4 (Сэмплинг), где обсуждается inference; «inference loop одинаков локально и в облаке — но размер модели определяет качество» → callback §4.2.
- s28a + s28b — кластер в Заключении (после 3 почему payoff): теперь когда знаем механику, можно ответить на 2 cross-cutting вопроса. ML vs LLM («когда не нужно это всё») + Human vs AI («attention ≠ понимание; см. §4.8»).

---

## Slide cut candidates (to reach 28-30 after +3 cross-cutting)

Цель: cut ≥ 4 (для 30) или ≥ 6 (для 28). Recommend cut 6 → final 28.

| Slide | Cut reasoning | Severity |
|---|---|---|
| **s02 split** (cover/roadmap = 2 slides → 1) | P2-1 — merge cover + roadmap. Saves 1 slide. | P2 |
| **s14 multimodal embeddings** | P1-3 Q4 — cut entirely; 1 строка в s30 preview Лекции 3. Saves 1 slide. | P1 |
| **s19 multi-head attention** | P1-1 Bloom overshoot + no LO support; 1 строка в s16 speaker note. Saves 1 slide. | P1 |
| **s24 top-p/top-k** | Q7 user lean merge с s23. Saves 1 slide. | P1 |
| **s17+s18 merge** | Q5 user lean. Saves 1 slide. | P1 |
| **s09 numbers/code tokenization** | Q4 vs LO trade-off — most overlap с s05 (token = subword); 1 минута в s07 «strawberry» speaker note: «то же про числа — `1234567` режется непредсказуемо, поэтому AI плохо считает; используйте Code Interpreter». Saves 1 slide. | P2 |

**Total cuts: 6.** Combined с +3 cross-cutting: 31 - 6 + 3 = **28 слайдов**. ✓ Constraint met.

---

## Counter-check

P1 count = 12 issues. Verdict = REVISE (consistent с rule «5+ P1 → REVISE»). ✓ No override needed.

Также: P0 count = 5 (cross-cutting missing, slide count overshoot, LO4 underspecified, Раздел 3 cognitive overload, hook tech-risk). Согласно verdict matrix, **any P0 + DoD metric concerns → REVISE минимум**. Подтверждено.

---

## Top-N приоритизированные правки (для plan v2)

1. **[P0-1]** Add 3 cross-cutting slides (ML/LLM s28a, local/cloud s25a, human/AI s28b) — без них plan v1 нарушает constraint §1.
2. **[P0-2]** Cut 6 slides (s02 split → 1, s14, s19, s24, s17+s18 merge, s09) → 28 final.
3. **[P0-3]** Усилить LO4 explicit teaching slide (s25 expand: 4 ручки API — T / top_p / max_tokens / system prompt).
4. **[P0-4]** Раздел 3 cognitive load: merge s17+s18, cut s19 → 5 content slides / 18 min.
5. **[P0-5]** Hook s01 — static-screenshot-first, live-demo-optional.
6. **[P1-3]** Replace «миопия токенизации» → «слепота к буквам» / «subword-агрегация» в LO6 + glossary + chapter / slides / speech.
7. **[P1-5]** Replace s11 Word2Vec king-queen → modern sentence-similarity example.
8. **[P1-8]** s20 timeline: reduce points to 3, tag `[VERIFY-ON-LECTURE-DAY]`.
9. **[P1-7]** s07 strawberry retrieval: lecturer pre-test day-of; replace example if outdated.
10. **[P1-10]** s18 + s28 role-effect mechanism: softer phrasing «на уровне attention мы видим...» вместо hard claim.
11. **[P1-4]** Unify metaphor: «фонарик» everywhere, cut «магнит».
12. **[P1-9]** Verify Семинар 12 vs Лекция 12 PARTS reference в Lec-1 §5.2 / `catalog/manifests/lectures.yaml`.
13. **[P1-6]** §13.2 marketing phrasing «промптинг — сквозной навык» — переформулировать.
14. **[P1-11]** Glossary: choose canonical form «авторегрессионный» / «авторегрессивный»; lock alias.
15. **[P1-12]** s17 worked example: add 2nd visual (counter-grammar example) ИЛИ disclaimer.
16. **[P1-2]** s06 BPE — replace 3-step trace на before/after.

---

**Конец methodology-critic report.**
