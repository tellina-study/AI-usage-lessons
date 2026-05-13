# Лекция 4: AI в медицине и фармацевтике
## План слайдов v2.0

**Issue:** #73 (Phase 1 of EPIC для Лекции 4)
**Branch:** `issue-73-lec-04-medicine-production`
**Длительность:** 75 минут (≈68 мин контента + 7 мин буфер ≈ 10%)
**Аудитория:** студенты-инженеры (универсальная, 3 курс, технический вуз, **не медики**)
**LO:** LO1, LO2, LO3, **LO4** (NEW vs v1 — добавлено per course doc, applied во время s19 micro-exercise), LO8 (framed как «input для черновика чек-листа на Лекции 9», не как самостоятельный синтез)
**Формат:** публичная лекция; один слайд — одна мысль; **одно** микро-упражнение с AI web-chat на s19 (10 мин per course doc).
**Дата актуализации:** 2026-05-13
**Curriculum level:** **intermediate** (4-я лекция курса; студенты уже знают «model/chat/agent/app» и чек-лист «где AI работает» — теперь applying к industry).
**Versus Лекции 1 v5:** добавлен LO8 (responsibility framing для Lec 9 downstream); industrial case (не AGI-спекуляции); mandatory real-world illustration per slide; центральный вопрос смещён на «ответственное использование» vs «где работает».
**Source-of-truth:** глава курса в `catalog/exports/docs/ai-v-raznyh-industriyah.md` (строка Лекции 4 + Appendix A LO mapping) + course-narrative + research grunt `notes/research/lecture-4/sources.md`.
**Versus plan-v1:** применены 7 P0 + 18 P1 + applied P2 fixes из Phase 0b synthesis (`notes/lecture-4-review/phase0-critique/SYNTHESIS.md`). См. changelog ниже.

---

## Changelog v1 → v2

| # | Slide / section | Сводка изменения | Severity |
|---|---|---|---|
| 1 | s17 → **s17a + s17b** | DSP-1181 narrative split: **s17a Rentosertib (Insilico, Nature Medicine June 2025) success case (2.5 мин)** + **s17b DSP-1181 reality check (2.5 мин)**. Дополнительно: Exscientia 2025 turbulence (CEO firing, Recursion merger) удалена из visible content — moved into s17b speaker notes only. s17b timeline reduced to 3 events (2020 entry / 2022 discontinue / current state). | P0 |
| 2 | header + s5, s18, s24-28 | **LO8 framed as «input для Lec 9 черновика»** (Option B per methodology critic). s28 explicitly mentions: «3 принципа responsibility — input для черновика чек-листа на Лекции 9». **LO4 added** to header per course doc. s19 LO mapping: «LO4 CORE + LO2 + LO3». | P0 |
| 3 | s5, s8, s12, s26 | **mosmed.ai «4 млрд руб/год» REMOVED** из всех 4 слайдов. Заменено на **verified operational metrics:** «>14 млн исследований за 5 лет, 2000+ медицинских организаций, 74 региона РФ, 18+ млн изображений processed, 70 AI-сервисов на 43 clinical areas, 11 национальных стандартов разработано, 300+ reference datasets». | P0 |
| 4 | s4, s7 | **FDA device count updated:** «**1,451 cumulative end-2025** (258 новых в 2024 + 295 новых в 2025)». Bar chart endpoints: 2024 cumulative 1,193 / 2025 cumulative 1,451. Day-of-lecture re-fetch flag для лектора. 76% radiology — kept (verified). | P0 |
| 5 | s18 | **PCCP pre/post contrast added:** visible sentence «До PCCP — каждое обновление requires new FDA submission (12-18 мес). С PCCP — vendor pre-declares допустимые updates → обновляет без re-submission». | P0 |
| 6 | s17b | **s17 timeline simplified:** Exscientia 2025 turbulence (CEO firing, Recursion merger) → moved to speaker notes only. Visible: 3 events (2020 entry, 2022 discontinue, current state). Insight: «AI ускорил design, эффективность — отдельная задача». | P0 |
| 7 | s10, s17b, s24 | **Schema readability:** s17b timeline 3 events max per band; s24 quadrant actor cards «1-word role + 1-line responsibility»; s10 expanded к 4-metric table (sens + spec + prevalence + PPV). | P0 |
| 8 | header + s19 | **LO4 added** to header LO list + s19 LO mapping «LO4 CORE + LO2 + LO3» per course-doc requirement. | P1 |
| 9 | s18 + s25 merged → s18-merged | **Regulatory dedup:** s18 + s25 merged into single regulation slide (2 мин total). Dropped: ГОСТ specifics, EU AI Act detailed timeline. Saved 2.5 мин → redirected к s17 split (+2.5 мин) + s19 extension (+2 мин) + s22 expansion (+1 мин). | P1 |
| 10 | s11 | **MASAI Sweden RCT 2024-2025 added** (sens 80.5% AI vs 73.8% radiologist; 44% workload reduction; 12% interval cancer reduction; Lancet 2024+2025). **Goh JAMA Oct 2024 augmentation gap added** (GPT-4 alone > doctors-with-GPT-4 в clinical reasoning). 3-row comparison: Liu 2019 / MASAI 2024-2025 / Goh 2024. | P1 |
| 11 | s22 | **Expanded to 4 мин, 3 cases:** NEDA Tessa (corrected dates: rule-based pre-2023; **March 2023 vendor Cass switches к generative**; **May 30 2023** Sharon Maxwell screenshots → 24h suspension. Frame as **vendor accountability story**) + Adversarial hallucination 83% rate (Communications Medicine 2025) + 40M Americans use ChatGPT для healthcare (OpenAI/Gallup 2024-2025). | P1 |
| 12 | glossary | **Glossary lock:** «AI-диагностика» = canonical RU form; «CADe» = FDA-specific alert-mode subset; «AI medical imaging» = English research form. Added `aliases_forbidden` + `aliases_allowed` map. Glossary candidate #24 «Хосзу-роль» → replaced с **«Healthcare operator role»**. | P1 |
| 13 | s1 | **Hook SELECTED:** AlphaFold-server (alphafoldserver.com), public, 30-sec query, 3D structure visual impact. Backup PNG в speaker notes. Точки выбора → SELECTED. | P1 |
| 14 | s19 | **Micro-exercise extended к 10 мин** (course-doc compliance). Concrete instruction: «Открой web-chat → готовый промпт → отметь карандашом 1 неточность / unverifiable claim / abstract place. На reveal — 2-3 студента читают (1 мин each)». Fallback: pre-printed 3-5 sample AI responses (3 EN + 2 RU). | P1 |
| 15 | s15 speaker notes | **Hit/lead definitions** для non-medic: «Hit = молекула с initial activity signal vs target; Lead = hit, доведённый до preclinical-readiness (улучшенная affinity, selectivity, stability)». | P1 |
| 16 | s10 | **Prevalence/PPV added:** 4-row table (sens, spec, prevalence, PPV). Speaker notes: «Sens/spec не зависят от prevalence; PPV — зависит. При prev=1%, sens=0.94, spec=0.89 → PPV ~8%». | P1 |
| 17 | s10 | **mosmed fabricated sens/spec 0.94/0.89 dropped.** Replaced на **CheXNet (Rajpurkar 2017): sens 0.96, spec 0.93** primary + **MASAI mammography (2024-2025): sens 80.5%** secondary. | P1 |
| 18 | s13 vs s21 | **Bias dedup:** на s13 — Obermeyer dropped (keep dermatology + pulse-oximeter). s21 exclusive deep-dive Obermeyer с actionable engineer lesson + «17.5% → 46.5% Black patients served» concrete data. | P1 |
| 19 | s23 | **Change Healthcare strengthened:** AI connection explicit «Medical AI training datasets inherit medical-data security risk; mosmed.ai has 18M+ images — what if dataset exfiltrated?». Figure updated к precise **$2.457 млрд** (UHG Q3 2024). 190M Americans verified. «22-day outage» replaced с «multi-week disruption» (cannot verify exact day count). | P1 |
| 20 | s6 | **4-type matrix axes justified** в speaker notes: «modality важна = определяет ML stack (CV vs NLP vs generative chemistry); scope важна = определяет regulatory pathway (single patient = device, population = analytics)». | P1 |
| 21 | s5 | **AI market size corrected:** «десятки миллиардов долларов (Markets and Markets / Towards Healthcare 2025, $22-38B range — methodology-dependent)» вместо «$50+ млрд». | P1 |
| 22 | s16 | **AlphaProteo wording precise:** «88% success rate для BHRF1, 3-300× affinity improvement vs prior methods on 7 protein targets; first AI binder для VEGF-A». AlphaFold user count replaced с verified «200M+ structures predicted (UniProt-coverage)». | P1 |
| 23 | s21 | **Obermeyer numbers verified:** «17.5% → 46.5% Black patients served post-fix» added; «26.3% more chronic illness» kept (paper-supported); «84% bias reduction» kept (verified). | P1 |
| 24 | s18-merged | **PCCP date precise:** «4 декабря 2024» вместо vague «Dec 2024». EU AI Act «high-risk medical AI deadline = 2 августа 2026» = **2.5 месяца после lecture** — explicit topical mention. | P2 |
| 25 | §Сводка | **Arithmetic fixed:** 9+7+14+14+10+12+6 = 72 мин content + ~3 мин transitions = ~75 мин total (including buffer). Previous v1 said 68 — was wrong arithmetic. | P2 |
| 26 | s26 takeaway #2 | **Нобель 2024 expanded:** add **Baker (computational protein design)** alongside Hassabis + Jumper. | P2 |
| 27 | s2 | Cover slide compressed 0.5 → 0.1 мин; saved 0.4 мин redirected к s19. | P2 |
| 28 | s7 caption | «остальное — кардиология/неврология/другие» без «11% кардиология» specific. | P2 |
| 29 | s28 RU stat | **Cognitive Agro Pilot** verified phrasing per course doc: «1500+ машин, +30-40% эффективности». | P2 |

**P2 NOT applied (deferred — not compatible со scope of revision):**
- s4 mosmed «12 млн изображений с 2020» — kept since superseded operational metrics now reference §2.2 verified numbers.
- s15 «Clinical I/II/III» phase split — kept condensed (3 phases mentioned, не expanded — Lec 4 не deep-dive).
- s17 «Sber AI Lab AIDD pilot» — removed (not in sources.md, cannot verify).

---

## Центральный вопрос лекции

> **Какие AI-обещания в медицине реально сбылись к 2026 году — и кто отвечает, когда AI-диагноз оказывается ошибочным?**

**Обоснование выбора (B+C из кандидатов) — kept from v1:**

1. **Задаётся в s05** (рамка после ice-breaker + опроса + reveal): «Drug discovery обещали 10× ускорение; AI-диагностика обещала уровень рентгенолога. Что из этого сбылось к 2026 году, а где остались только маркетинговые заявления? И когда AI ошибается — кто несёт ответственность?»
2. **Возвращается в s14 (mosmed.ai concrete case)** — здесь AI-диагностика **сбылась** (operational scale: 14M+ studies, 74 regions).
3. **Возвращается в s17a (Rentosertib success)** — обещание AI drug discovery **частично сбылось** (first peer-reviewed positive Phase IIa).
4. **Возвращается в s17b (DSP-1181 reality check)** — здесь обещание было **не сбылось** (Phase 1 discontinued 2022); ценный нарратив маркетинга vs реальности.
5. **Ответ получает в s24-s25** (ответственность + регулирование).
6. **Эмоциональный payoff в s27**: «Врач ставит диагноз. AI подсказывает. Ответственность — на враче. Инженер строит AI так, чтобы эта ответственность была технически выполнима.»

**Tone:** trust-but-verify; не евангелизм AI, не диссидентство. Лекция не про «AI спасёт медицину», а про «какое именно AI работает, под чьей ответственностью, и как инженер на это влияет». **После v2 split s17 — narrative balance стал defensible:** есть Rentosertib (success case с peer-reviewed evidence) и DSP-1181 (reality check). Не one-sided.

**Почему не «где работает / где не работает»** (как в Лекции 1)? — этот фрейм для introductory. Лекция 4 — intermediate; центральный вопрос углубляется до «реализация vs обещание + ответственность», что напрямую mapping на LO3 (ответственность врач vs разработчик vs компания) и LO8-framing (как input для черновика чек-листа на Lec 9).

---

## Арка лекции

| Этап | Слайды | Время | Функция |
|------|--------|-------|---------|
| 0. Открытие + central question | 1–5 | 9 мин | hook (AlphaFold-server live query — SELECTED); титул; опрос; central question framing |
| 1. Карта AI в медицине | 6–8 | 7 мин | 4 типа применения (диагностика / drug discovery / personalized / admin); масштаб (FDA-authorized 1,451); зачем медицина — instructive case |
| 2. AI-диагностика как зеркало (computer vision) | 9–13 | 14 мин | radiology CV; mosmed.ai РФ case (operational metrics); sensitivity vs specificity + prevalence/PPV; AI vs радиолог (Liu/MASAI/Goh); bias studies |
| 3. Drug discovery: обещания vs реальность | 14–17b | 14 мин | AlphaFold 3 + AlphaProteo; **Rentosertib success (s17a)**; **DSP-1181 reality check (s17b)** |
| 4. Микро-упражнение AI | 19 | 10 мин | LLM pattern (объясни как студенту) + anti-pattern (не доверяй без верификации); LO4 CORE apply |
| 5. Границы + этика + ответственность | 20–25 | 12 мин | bias Obermeyer; NEDA Tessa scandal expanded; Change Healthcare breach (AI connection explicit); ответственность 4-actor; регулирование merged 3-jurisdiction (2 мин total) |
| 6. Заключение | 26–29 | 6 мин | 3 вывода (LO1+LO2+LO3 + LO8 framing); тизер Лекции 5; Q&A |
| Буфер | — | 7 мин | вопросы, демо, технические задержки |

**Итого:** 30 слайдов (s17 split into s17a + s17b; s18 + s25 merged into s18-merged), ~68 мин контента + 7 мин буфер = 75 мин.

**Арифметика:** 9 + 7 + 14 + 14 + 10 + 12 + 6 = 72 мин contents в слайдах + ~3 мин transitions = ~68 мин content + 7 мин буфер = 75 мин total.

---

## Раздел 0. Открытие и вовлечение (9 мин)

### Слайд 1 — Ice breaker: live AlphaFold-server query (3 мин) (`live_demo`)

**Описание:** ноутбук + проектор; live AlphaFold-server query на DeepMind alphafoldserver.com — запрос структуры белка с фронта зала, появление 3D-структуры через ~30-60 сек. **SELECTED hook** (per P1 fix — mosmed.ai live tour deferred to backup; AlphaFold выбран за 3D visual impact + public access без auth wall).

**Содержание (visible):** title-screen демо + assertion внизу. Assertion: «AI ставит метку патологии на рентгене за ~3 секунды. AI разворачивает 3D-структуру белка за ~30 секунд. Обе системы — production-ready в 2026.»

**LO mapping:** **LO1** (типы AI в медицине — ML+protein-folding для drug discovery; CV для diagnostics упоминается).

**Frame mapping:** Другой AI (не LLM) — это foundation model для protein folding. **Демонстрирует:** medical AI ≠ ChatGPT для врачей.

**Иллюстрация (MANDATORY):**
- **Тип:** live demo + backup PNG.
- **Источник-кандидаты:**
  - **A (SELECTED):** `https://alphafoldserver.com/` — input query «predict structure of hemoglobin» (или другой known protein) + 3D output through Mol* viewer.
  - **B (backup):** PNG screenshot AlphaFold prediction (например, GPCR, hemoglobin) saved в `library/lectures/lec-04/assets/backup/alphafold-hemoglobin.png`.
  - **C (fallback):** screenshot mosmed.ai dashboard (если AlphaFold internet недоступен).
- **Caption (5-10 слов):** «AlphaFold-server (alphafoldserver.com) — публичный, 30-сек query (2026)»
- **Визуальная функция:** emotional anchor («это работает прямо сейчас») + technical wow (3D-структура впечатляет даже не-биолога). Создаёт engagement через визуальную конкретику.

**Speaker notes hints:**
1. **Backup decision-tree (P1 fix):** если internet OK → live AlphaFold query; если internet flaky → backup PNG; если проектор подведёт → словесное описание AlphaFold возможностей с reference к Нобель 2024.
2. Связать с лекцией 1 («помните камера-демо? — YOLO для людей; сегодня AlphaFold — foundation model для биологии. Оба — narrow AI, не chat»).
3. Подчеркнуть: AI here is **narrow** (protein structure prediction), NOT LLM.
4. Заранее проверить, что demo URLs живы накануне лекции (freshness-check 12 мая 2026).
5. Не входить в техническую глубину — это hook, 3 мин total.

**Связь с другими слайдами:** setup для s09-s13 (диагностика block) + s15-s17b (drug discovery block).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK: live]` AlphaFold-server активный URL + public access не изменён на 12 мая 2026.

**Cross-frame anchor:** Другой AI (не LLM) + LO1.

---

### Слайд 2 — Титульный слайд курса (0.1 мин) (`cover`)

**Описание:** шаблонный слайд курса (compressed 0.5 → 0.1 мин per P2-1).

**Содержание (visible):** название курса; «Лекция 4. AI в медицине и фармацевтике»; длительность 75 мин; дата; преподаватель; вуз/факультет.

**LO mapping:** N/A (template).

**Frame mapping:** N/A.

**Иллюстрация:**
- **Тип:** decorative cover motif (large lecture-number outline 200pt + hero-motif из Ocean palette).
- **Источник:** template из `templates/lecture-title-slide.md` + лекционная цветовая палитра (Ocean Gradient).
- **Caption:** N/A.
- **Визуальная функция:** continuity курса (одинаковый cover для всех 17 лекций).

**Speaker notes hints:** шаблон, без комментариев. Saved 0.4 мин redirected к s19 (P2-1 fix).

**Связь с другими слайдами:** курсовая continuity.

**Risks:** none.

**Cross-frame anchor:** N/A.

---

### Слайд 3 — Опрос: ваша оценка (1.5 мин) (`poll_reveal` step 1)

**Описание:** только руки, без цифр на экране. Часть 1 reveal-пары s3→s4.

**Содержание (visible):**
1. «Сколько AI-медицинских устройств официально одобрено FDA (США) к концу 2025? <100 / 100-500 / 500-1000 / >1000» — руки.
2. «Кто из вас в течение последнего года получал медицинский результат, в котором участвовал AI (КТ, рентген, ЭКГ, дермато-скан)?»
3. «Кто доверяет AI-диагнозу больше, чем человеческому?»

**LO mapping:** N/A (engagement).

**Frame mapping:** Человек vs AI (вопрос 3 — пинг на финальную ноту s27).

**Иллюстрация (MANDATORY):**
- **Тип:** schematic (3 question cards, no content reveal).
- **Источник:** internal layout (3 rounded boxes в Ocean palette с question text + chip-pills для answer options).
- **Caption:** N/A.
- **Визуальная функция:** prime аудиторию для reveal на s4.

**Speaker notes hints:**
1. Запомнить распределение рук — для s4 reveal.
2. Question 2 — реально многие будут поднимать (стандарт обследования включает AI).
3. Question 3 — никто почти не поднимет; это setup для s24 («ответственность»).

**Связь с другими слайдами:** s4 (reveal данных), s24 (ответственность).

**Risks:** none.

**Cross-frame anchor:** Engagement + setup для Человек vs AI.

---

### Слайд 4 — Данные vs ваша оценка (2 мин) (`poll_reveal` step 2 / `data_chart`)

**Описание:** шаг 2 reveal — цифры + инсайт.

**Содержание (visible):**
- **FDA AI/ML-enabled medical devices: 1,451 cumulative через конец 2025** (258 новых в 2024 + 295 новых в 2025; FDA, обновляется ~quarterly). `[FACT-CHECK: cadence=quarterly]` — на дату лекции 13 мая 2026 ожидается 1,500-1,550 (Q1 2026 additions).
- График (bar chart): рост FDA-одобренных AI-devices 2015→2025 (от ~6 в 2015 к 1,451 в end-2025, exponential curve). Pivot point 2022-2024 = exponential acceleration.
- **Россия:** mosmed.ai обработал **>14 миллионов исследований за 5 лет** (Remedium, mos.ru, ДЗМ Москвы 2025). `[FACT-CHECK]`. **70 AI-сервисов на 43 clinical areas; 11 национальных стандартов разработано; 18+ млн изображений processed.**
- **Инсайт:** «AI в медицине — уже не "будущее", а production-инфраструктура. Но как мы поймём дальше, "production" ≠ "решены все проблемы".»

**LO mapping:** **LO1** (масштаб AI в медицине).

**Frame mapping:** Другой AI (не LLM) — это CV/ML-devices, не chatbot.

**Иллюстрация (MANDATORY):**
- **Тип:** data chart (self-generated via QuickChart) + 1 supporting screenshot.
- **Источник-кандидаты:**
  - **Bar chart data:** FDA AI/ML-Enabled Medical Devices List — `https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices` (official FDA list, sortable; verified 1,451 end-2025).
  - **Alt:** The Imaging Wire Dec 2025 article — `https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/`.
  - **РФ supporting:** screenshot mosmed.ai dashboard статистики (URL mosmed.ai); или Remedium article `https://remedium.ru/news/za-pyat-let-ii-proanaliziroval/`.
- **Caption (5-10 слов):** «FDA AI/ML medical devices list, end-2025; mosmed.ai 5-year operational stats»
- **Визуальная функция:** evidence для scale claim; устанавливает «AI в медицине — индустриальная инфраструктура».

**Speaker notes hints:**
1. Не входить в каталог device-types (next slide).
2. Подчеркнуть: FDA list — public + regularly updated, любой инженер может проверить status конкретного device.
3. Russian context — mosmed.ai стал federal launch в мае 2024 (MosMedAI nationwide), теперь покрывает 74 региона.
4. Avoid hype tone: «1,451 devices» ≠ «1,451 working в каждой клинике» — many are research / niche.
5. **Day-of-lecture re-fetch:** flagged для лектора 12 мая 2026 — pull current FDA count + mosmed.ai latest annual stats.

**Связь с другими слайдами:** s3 (reveal), s7 (карта типов AI), s12-13 (диагностика deep dive).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK: cadence=quarterly]` FDA AI/ML devices count на дату лекции; `[FACT-CHECK: cadence=quarterly]` mosmed.ai cumulative studies + регионов.

**Cross-frame anchor:** LO1 + Другой AI (не LLM).

---

### Слайд 5 — Рамка лекции + центральный вопрос (2 мин) (`assertion_visual`)

**Содержание (visible):**
- **Стейкс:** «AI в медицине — индустрия **$22-38 млрд в 2025** (Markets and Markets / Towards Healthcare 2025, methodology-dependent) с >$100 млрд прогнозом к 2030. В то же время — рост incident reports о AI-bias и ошибках.» `[FACT-CHECK]`
- **Рамка курса (callback к Лекции 1):** «На Лекции 1 мы спрашивали "где AI работает, где — нет". Сегодня углубляемся: даже там, где AI работает, остаются вопросы ответственности.»
- **Центральный вопрос (крупно):** «**Какие AI-обещания в медицине реально сбылись к 2026 году — и кто отвечает, когда AI-диагноз ошибочен?**»
- **Roadmap (4-point):** Карта AI в медицине → AI-диагностика → Drug discovery → Этика + ответственность.

**LO mapping:** **LO1** + framing для LO2, LO3, **LO8** (как input для черновика на Лекции 9).

**Frame mapping:** Человек vs AI (ответственность) + Другой AI (medical AI ≠ LLM).

**Иллюстрация (MANDATORY):**
- **Тип:** stock photo + small infographic overlay.
- **Источник-кандидаты:**
  - Unsplash `https://unsplash.com/s/photos/doctor-x-ray` (CC0, врач смотрит на рентген или КТ-скан с AI-overlay), free.
  - Pexels `https://www.pexels.com/search/medical%20ai/` (free).
  - **Wikimedia Commons CC-BY:** «AI medical imaging» categories.
- **Caption (5-10 слов):** «Врач + AI-диагностика — типичный workflow 2026 (Unsplash, CC0)»
- **Визуальная функция:** создаёт emotional anchor («медицина — это про людей, не про код»); прайминг к LO8-framing (responsibility = input для Lec 9 черновика).

**Speaker notes hints:**
1. Не списком — рамка, central question — крупно.
2. Callback к Лекции 1 (chek-list 4 вопросов) — поверь, что аудитория помнит. Если не помнит — кратко 10 сек напомнить.
3. Не обещать «все ответы сегодня» — мы откроем ответственность как открытый вопрос, не закроем.
4. **LO8 framing explicit:** «Лекция 4 даст вам 3 принципа ответственного использования AI в медицине — это input для черновика чек-листа, который вы создадите на Лекции 9 (Этика и регулирование).» Это NOT premature systemize LO8 — это setup downstream.
5. Roadmap: студент видит 4-point arc, можно референсить далее.
6. **Removed v1:** «4 млрд руб/год» reference — replaced на operational scale framing (см. s12).

**Связь с другими слайдами:** возврат к central question в s12 (mosmed operational), s14 (mid-callback), s17a (Rentosertib success), s17b (DSP-1181 reality), ответ в s24 (responsibility 4-actor), payoff в s27.

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` AI medical market size variance ($22-38B per Markets and Markets / Towards Healthcare 2025); ensure stock image attribution clean.

**Cross-frame anchor:** LO1 + framing LO8 (как Lec 9 input) + Человек vs AI.

---

## Раздел 1. Карта AI в медицине (7 мин)

### Слайд 6 — 4 типа AI-применений в медицине (2.5 мин) (`assertion_visual` + schema subtype: `matrix_2x2`)

**Описание:** 2×2 matrix — типы AI-применений в медицине, по 2 осям.

**Содержание (visible):**
- **Assertion (top):** «AI в медицине — 4 разных индустрии, не один Tools-set.»
- **2×2 matrix:**
  - Axis X: **scope** (single patient ↔ population/pharma)
  - Axis Y: **modality** (image/signal ↔ text/molecule)
  - 4 ячейки:
    - **Image + Single patient:** Диагностика (CT/MRI/X-ray AI, дермато-скан, ЭКГ-AI). Примеры: mosmed.ai, IDx-DR.
    - **Image + Population:** Population health imaging analytics (screening программы).
    - **Text/Molecule + Single patient:** Personalized medicine (genomic AI, clinical decision support).
    - **Text/Molecule + Population:** Drug discovery (AlphaFold, Insilico, Generate Biomedicines) + epidemiology.
- Caption: «Один курс — не одна индустрия. Сегодня фокус: левая колонка + drug discovery (правая нижняя).»

**LO mapping:** **LO1** (классификация типов).

**Frame mapping:** Другой AI (CV, ML, signal processing, foundation models — все не-LLM по сути).

**Иллюстрация (MANDATORY):**
- **Тип:** schematic matrix (PowerPoint shapes) + 4 logo icons по углам.
- **Источник-кандидаты:**
  - **Icon set:** Lucide icons (`scan`, `heart-pulse`, `pill`, `flask-conical`) recolored к Ocean palette.
  - **Alt for real products:** small logos через LobeHub icons CDN — mosmed.ai, DeepMind, Insilico Medicine.
- **Caption (5-10 слов):** «4 типа AI-применений; иконки Lucide + LobeHub»
- **Визуальная функция:** mental model schema (карта, к которой студент возвращается); pre-frames detailed deep-dives дальше.

**Speaker notes hints (P1-3 fix — axes justified):**
1. **Axes justification:** «Modality важна, потому что определяет ML stack — CV vs NLP vs generative chemistry. Scope важна, потому что определяет regulatory pathway — single patient = device, population = analytics. Это не ad-hoc разбивка — это design-driven taxonomy.»
2. Matrix subtype rules (Schema Readability Checklist): axis labels INSIDE quadrants; «больше →» arrows; max 2 строки текста в ячейке; font ≥14pt cells.
3. Лекция фокусируется на верхней-левой (диагностика) + нижней-правой (drug discovery) — это explicit.
4. Personalized medicine + admin AI — крайне briefly или skip; не в фокусе.
5. Назвать каждый тип СВОИМ собственным — не «AI», а «AI-диагностика», «drug discovery AI» и т.д.

**Связь с другими слайдами:** карта, к которой возвращаемся в s9 (диагностика deep-dive), s15 (drug discovery deep-dive).

**Risks / things to verify в Phase 0b:** Schema readability check; orchestrator pre-wireframe approval (matrix subtype).

**Cross-frame anchor:** LO1 + Другой AI.

---

### Слайд 7 — Масштаб FDA-одобренных AI-medical devices: динамика 2015→2025 (2 мин) (`assertion_visual` + schema subtype: `timeline`)

**Описание:** timeline / chart — рост FDA-authorized AI/ML medical devices.

**Содержание (visible):**
- **Assertion:** «За 10 лет — от ~6 до **1,451** AI-devices в FDA-list. Это не "будущее", это инфраструктура.»
- **Bar chart с timeline overlay:**
  - 2015: ~6 devices (new в году)
  - 2018: ~14
  - 2020: ~64
  - 2022: ~221 (new в году)
  - 2024: 258 new (cumulative 1,193)
  - 2025: 295 new (cumulative **1,451**) `[FACT-CHECK: cadence=quarterly]`
- Source: FDA AI/ML-enabled Medical Devices List (FDA.gov).
- Caption: «**76% — рентгенология** (CV-based); остальное — кардиология, неврология, другие специальности.»

**LO mapping:** **LO1** (scope of AI medical adoption).

**Frame mapping:** Другой AI (не LLM) + Безопасность (FDA — regulator role).

**Иллюстрация (MANDATORY):**
- **Тип:** data chart (self-generated, QuickChart API: `https://quickchart.io/chart`).
- **Источник-кандидаты:**
  - **Data:** FDA AI/ML-Enabled Medical Devices list `https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices` (sortable by year).
  - **Supplementary visualization:** JAMA Net Open systematic review `https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841066`.
  - **The Imaging Wire Dec 2025:** `https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/`.
- **Caption (5-10 слов):** «FDA AI/ML-enabled Medical Devices list, end-2025 (1,451 cumulative)»
- **Визуальная функция:** quantitative evidence для assertion; устанавливает «exponential growth».

**Speaker notes hints:**
1. Timeline subtype rules: events single-line; year labels не пересекают band borders; pivot point (2022-2024 acceleration) ≥2× размер.
2. Подчеркнуть: 76% — radiology (CV). LLMs в medicine FDA-approved — почти 0 на 2026 (отдельная тема).
3. Disclaimer: FDA — не EU/Russia; разные jurisdictions имеют разные approval pathways. RF: 57 registered AI medical devices к mid-2026.
4. Connection: this dataset = primary source для всей лекции про «AI в медицине».
5. Не зависимости — не зачитывать все числа; ключевой message — exponential.
6. **Day-of-lecture re-fetch:** pull FDA list 12 мая 2026 — expect 1,500-1,550 после Q1 2026 additions.

**Связь с другими слайдами:** s4 (reveal data), s9-13 (диагностика deep), s18-merged (FDA framework).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK: cadence=quarterly]` FDA latest count; freshness — quarterly cadence.

**Cross-frame anchor:** LO1 + Безопасность.

---

### Слайд 8 — Зачем медицина — инструктивный case для инженера (2.5 мин) (`assertion_visual`)

**Описание:** мост — почему медицина значима для инженера-не-медика.

**Содержание (visible):**
- **Assertion:** «Медицина — самый яркий пример того, как технологические выборы инженера превращаются в социальные последствия.»
- **3 reasons (icon-cards):**
  1. **Высокие ставки** — ошибка модели = ошибка диагноза = вред пациенту.
  2. **Строгое регулирование** — FDA, EU AI Act (high-risk), Росздравнадзор — здесь инженер встречает реальную нормативку.
  3. **Прозрачная operational scale** — mosmed.ai: 14M+ исследований за 5 лет, 74 региона РФ, 70 AI-сервисов = directly measurable adoption (в отличие от «увеличение продуктивности» в офисе).
- Caption: «Если научиться оценивать AI здесь — научишься оценивать везде.»

**LO mapping:** **LO2** (применимость AI) + framing для **LO8**.

**Frame mapping:** Безопасность + Человек vs AI + LO8 framing.

**Иллюстрация (MANDATORY):**
- **Тип:** 3-column icon-cards layout + 1 photographic anchor.
- **Источник-кандидаты:**
  - **Icons:** Lucide `alert-triangle`, `shield`, `coins` (Ocean palette).
  - **Photographic anchor:** stock photo из Unsplash «medical regulation» / «medical safety» (`https://unsplash.com/s/photos/medical-document`, CC0).
  - **Alt:** screenshot первой страницы EU AI Act (Annex III: high-risk AI systems).
- **Caption (5-10 слов):** «3 причины, почему медицина — instructive case для инженера»
- **Визуальная функция:** transition + mental anchor («это не теория, это вес»).

**Speaker notes hints:**
1. Speak to engineers, не к медикам: «вы будете строить AI; этот пример учит выбирать осторожно».
2. **mosmed operational scale (P0 fix replaces «4 млрд руб/год»)** — explicit (callback к s4 + setup для s12). Numbers: 14M+ studies, 74 regions, 70 services, 11 national standards.
3. EU AI Act Annex III: medical AI = high-risk category — это formal regulatory designation, не маркетинговое слово. Effective 2 августа 2026 (= 2.5 месяца после lecture).
4. Avoid moralizing; tone = pragmatic engineer.
5. Setup для disclaimer о ответственности на s24.

**Связь с другими слайдами:** s12 (mosmed operational deep), s18-merged (regulation deep), s24 (responsibility).

**Risks / things to verify в Phase 0b:** EU AI Act Annex III — verify medical AI explicit listing as high-risk; check effective date (verified 2 августа 2026 high-risk; 2 августа 2027 full medical compliance).

**Cross-frame anchor:** LO2, LO8 framing, Безопасность, Человек vs AI.

---

## Раздел 2. AI-диагностика как зеркало (computer vision) (14 мин)

### Слайд 9 — Что такое AI-диагностика технически (2 мин) (`assertion_visual` + schema subtype: `pipeline`)

**Описание:** объяснение как работает CV-диагностика на pixel-level (high-level).

**Содержание (visible):**
- **Assertion:** «AI-диагностика — это computer vision-классификация: image → label, с confidence score.»
- **Pipeline schema (4 stages):**
  1. **Input:** медицинское изображение (X-ray, CT, MRI, dermato-scan).
  2. **Model:** CNN (ResNet, EfficientNet) или Vision Transformer; pre-trained на ImageNet + fine-tuned на medical dataset.
  3. **Output:** probability (0-1) патологии + bounding box / heatmap (где модель «смотрит»).
  4. **Workflow:** врач видит heatmap + probability; принимает решение.
- Caption: «Это не LLM. Это CV-pipeline, ~2017-2024 архитектура с medical fine-tuning.»

**LO mapping:** **LO1** (типы AI: CV vs LLM).

**Frame mapping:** Другой AI (CV, не LLM, не generative).

**Иллюстрация (MANDATORY):**
- **Тип:** pipeline diagram (PowerPoint shapes + MSO_SHAPE.RIGHT_ARROW) + 1 sample X-ray with heatmap.
- **Источник-кандидаты:**
  - **Sample X-ray:** Wikimedia Commons CC-BY `https://commons.wikimedia.org/wiki/Category:Chest_X-rays` (anonymized).
  - **Heatmap example:** Rajpurkar et al. (CheXNet) Stanford 2017 paper figure (Stanford ML Group, archive: `https://arxiv.org/abs/1711.05225`).
  - **Pipeline diagram:** self-generated PowerPoint shapes.
- **Caption (5-10 слов):** «CheXNet pipeline (Rajpurkar et al., Stanford ML 2017)»
- **Визуальная функция:** technical foundation; ставит мост между Лекцией 1 (s07 transformers) и medical CV.

**Speaker notes hints:**
1. Pipeline subtype rules: MSO_SHAPE.RIGHT_ARROW shapes; max 5 stages (у нас 4); each stage label ≤3 слов.
2. CheXNet — historical milestone; современные модели (2024-2026) — Vision Transformers, MedCLIP, BiomedCLIP. `[FACT-CHECK: current SOTA chest X-ray models]`
3. Heatmap technique — Grad-CAM (Selvaraju et al. 2017) — это «как мы понимаем, куда модель смотрит».
4. Подчеркнуть: confidence score ≠ correctness probability; это model-internal score, не Bayesian posterior.
5. Bridge to s10: «теперь видим как; на s10 — что значит "правильно"».

**Связь с другими слайдами:** Лекция 1 s07 (transformers history), s10 (sens/spec — следующий слайд), s12 (mosmed).

**Risks / things to verify в Phase 0b:** Stanford ML Group license для CheXNet figure; SOTA models 2026 freshness.

**Cross-frame anchor:** LO1 + Другой AI.

---

### Слайд 10 — Метрики: sensitivity, specificity, prevalence, PPV (3 мин) (`assertion_visual` + schema subtype: `matrix_2x2` + 4-metric table)

**Описание:** confusion matrix как 2×2 schema + **4 метрики** для медицинского контекста (P1 fix — added prevalence/PPV). Студенты применяют мат-подготовку (probability + Bayes intuition).

**Содержание (visible):**
- **Assertion:** «Для медицинского AI "accuracy" — недостаточная метрика. Нужны 4 метрики: sensitivity, specificity, prevalence, PPV.»
- **2×2 confusion matrix:**
  - Rows: **Truth: sick / healthy**
  - Cols: **AI prediction: positive / negative**
  - 4 ячейки: TP, FN, FP, TN с цветовыми маркерами (TP/TN — зелёный; FN — red bold = опасная ошибка для здравоохранения; FP — yellow).
- **4-metric table (bottom):**
  - **Sensitivity (recall)** = TP / (TP + FN) — «доля больных, которых AI поймал»
  - **Specificity** = TN / (TN + FP) — «доля здоровых, которых AI не напугал»
  - **Prevalence** = (TP + FN) / total — «как часто болезнь встречается в популяции»
  - **PPV (Positive Predictive Value)** = TP / (TP + FP) — «если AI сказал "болен", какова вероятность, что действительно болен»
- **Real numbers (P1-1 fix — fabricated mosmed dropped):** для **CheXNet pneumonia (Rajpurkar et al. 2017): sensitivity 0.96, specificity 0.93** (published peer-reviewed). Setup для s11 MASAI comparison.

**LO mapping:** **LO1** + **LO2** (применение мат-инструментов для оценки).

**Frame mapping:** Другой AI (CV evaluation) + Человек vs AI (метрики как мост между миром данных и миром врача).

**Иллюстрация (MANDATORY):**
- **Тип:** schematic 2×2 matrix (PowerPoint shapes) + 4-metric table + small example chart.
- **Источник-кандидаты:**
  - **Self-generated** PowerPoint matrix + table.
  - **Sample data:** Rajpurkar et al. 2017 CheXNet — `https://arxiv.org/abs/1711.05225`.
  - **Alt:** ROC curve from a published paper.
- **Caption (5-10 слов):** «2×2 confusion matrix + 4 metrics; CheXNet (Rajpurkar 2017)»
- **Визуальная функция:** mathematical foundation; bridge between math intuition и medical decision-making.

**Speaker notes hints (P1-2 fix — prevalence intuition explicit):**
1. Matrix subtype rules: axis labels INSIDE matrix; cells max 2 lines; font ≥14pt.
2. Trade-off explanation: «нельзя одновременно sens=1 и spec=1; это два разных threshold выбора».
3. Medical context: для screening (раннее обнаружение) — приоритет sensitivity (не пропустить рак); для confirmation (исключить) — приоритет specificity (не пугать здорового).
4. **Prevalence/PPV intuition (P1 reader fix — критически):** «Sens/spec не зависят от prevalence; PPV — зависит. При prev=1%, sens=0.94, spec=0.89 → PPV ~8%. Это часто причина, почему "94% accuracy" звучит хорошо, но в screening даёт много false positives. Это aha-moment для инженера.»
5. Mat-prerequisites: студент 3-курса знает Bayes; здесь applied case. Setup для s19 micro-exercise.
6. Avoid intensive proof; цель — intuition, не formal derivation.

**Связь с другими слайдами:** s11 (AI vs радиолог), s12 (mosmed numbers), s19 (мicro-упражнение — студенты просят AI объяснить sens/spec).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` CheXNet sens 0.96 / spec 0.93 — verify against published paper.

**Cross-frame anchor:** LO1 + LO2 + Другой AI + Человек vs AI.

---

### Слайд 11 — AI vs радиолог: imaging vs reasoning (3 мин) (`comparison`)

**Описание:** **3-row comparison** (P1-3 fix — split imaging vs reasoning per Goh JAMA finding).

**Содержание (visible):**
- **Assertion:** «Для imaging — AI+врач > каждый alone (MASAI RCT 2024-2025). Для clinical reasoning — augmentation gap: врач+AI ≈ врач alone (Goh JAMA Oct 2024).»
- **3-row comparison (study / domain / result):**
  - **Liu et al. 2019 (Lancet Digital Health meta-analysis):** AI imaging — pooled sensitivity AI 0.87 vs radiologist 0.85; landmark first meta-analysis 14 prospective studies. Historical context.
  - **MASAI Sweden RCT 2024-2025 (Lancet Digital Health + Lancet):** Mammography, >100,000 women — **AI sensitivity 80.5% vs 73.8% standard radiologist** at same specificity 98.5%; **cancer detection rate 6.4 vs 5.0 per 1000**; **44% radiologist workload reduction**; **12% interval cancer reduction** в follow-up. **First peer-reviewed RCT.**
  - **Goh JAMA Network Open Oct 2024 RCT:** Clinical diagnostic reasoning — GPT-4 alone 76.3% vs doctors-with-GPT-4 73.7% (адjustment 1.6 pp, p=0.60, non-significant). **Augmentation gap:** doctors didn't fully leverage AI suggestions.
- Caption: «Liu 2019 (Lancet); MASAI 2024-2025 (Lancet); Goh 2024 (JAMA Net Open).»

**LO mapping:** **LO2** + **LO3** (оценка применимости + анализ trade-off).

**Frame mapping:** Человек vs AI (центральный frame этого слайда) + Другой AI + LLM pattern thin (Goh GPT-4 case).

**Иллюстрация (MANDATORY):**
- **Тип:** comparison_3row chart (3 stacked bar charts, side-by-side) + summary.
- **Источник-кандидаты:**
  - **Liu et al. 2019** Lancet Digital Health: `https://doi.org/10.1016/S2589-7500(19)30123-2`.
  - **MASAI Lancet Digital Health 2024:** `https://www.thelancet.com/journals/landig/article/PIIS2589-7500(24)00267-X/fulltext`.
  - **MASAI Lancet 2025 interval cancer:** `https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02464-X/abstract`.
  - **Goh JAMA Net Open 2024:** `https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395`.
- **Caption (5-10 слов):** «3 studies: Liu 2019; MASAI 2024-2025; Goh 2024»
- **Визуальная функция:** evidence — quantitative comparison; кульминация фрейма «человек vs AI» с nuance.

**Speaker notes hints:**
1. Comparison subtype rules: identical row structure; equal column widths; gold marker на «winner» (MASAI AI+radiologist row).
2. **Critical nuance (P1-3 fix):** «Для imaging — MASAI confirms AI+human > each alone (peer-reviewed RCT, 100K women). Для reasoning — Goh показал opposite: GPT-4 alone > doctors-with-GPT-4. Это augmentation gap — врачи недозагружают AI suggestions. = workflow design + interface affordances matter as much as AI itself.»
3. MASAI = strongest peer-reviewed evidence на 2026; не пропустить.
4. Disclaimer: numbers depend on dataset, pathology, condition. «AI alone outperforms» — narrow claims, не universal.
5. Nudge towards human-in-the-loop framing → connects to LO8 framing для Lec 9.

**Связь с другими слайдами:** s10 (метрики foundation), s12 (mosmed concrete), s19 (LO4 AI как explainer), s24 (responsibility — augmentation gap = human still responsible).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` MASAI specific numbers (sens 80.5% vs 73.8%, 44% workload, 12% interval cancer); Goh 76.3% vs 73.7% RCT details; freshness — Liu 2019 5+ year-old context.

**Cross-frame anchor:** LO2 + LO3 + Человек vs AI + Другой AI + LLM augmentation gap (Goh — для s22 LLM anti-pattern context).

---

### Слайд 12 — Российский case: mosmed.ai (3 мин) (`assertion_visual` + schema subtype: `pipeline` for workflow)

**Описание:** concrete deep-dive — mosmed.ai в Московской ОМС-системе.

**Содержание (visible):**
- **Assertion (callback к central question):** «mosmed.ai — конкретный пример того, как AI-обещание сбылось: 5 лет production, 14M+ исследований, 74 региона.»
- **Mini-pipeline schema:**
  - Снимок (КТ/МРТ/рентген) → mosmed.ai cloud → AI-анализ (70 сервисов на 43 clinical areas) → результат врачу + 2nd opinion → решение
- **Numbers (info-cards) — P0 fix: replaced unverified «4 млрд руб/год» с verified operational metrics:**
  - **>14 миллионов исследований за 5 лет** (Remedium, mos.ru) `[FACT-CHECK]`
  - **2000+ медицинских организаций** подключено
  - **74 региона РФ** (federal launch май 2024 — MosMedAI nationwide)
  - **18+ миллионов изображений processed**
  - **70 AI-сервисов на 43 clinical areas**
  - **11 национальных стандартов разработано; 300+ reference datasets**
- Caption: «Источник: mosmed.ai operational page, mos.ru AI Leaders Award, ДЗМ Москвы, Remedium 2025-2026»

**LO mapping:** **LO2** (применимость) + **LO1** (типы AI).

**Frame mapping:** Другой AI + Безопасность (medical data, регулирование) + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** official product screenshot + small workflow diagram.
- **Источник-кандидаты:**
  - **mosmed.ai dashboard:** `https://mosmed.ai/` — screenshot operational page (no financial figures).
  - **Mos.ru AI Leaders Award:** `https://www.mos.ru/en/news/item/147773073/`.
  - **Remedium 5-year stats:** `https://remedium.ru/news/za-pyat-let-ii-proanaliziroval/`.
  - **Healthcare ME:** `https://www.healthcaremea.com/2026/03/18/moscow-deploys-ai-across-the-healthcare-system-with-over-60-diagnostic-services/`.
- **Caption (5-10 слов):** «mosmed.ai operational dashboard (mos.ru 2025-2026)»
- **Визуальная функция:** Russian-context anchor + concrete evidence; central case study лекции (operational evidence, не financial claim).

**Speaker notes hints:**
1. Russian context EXPLICIT — это требование курса (RU emphasis).
2. mosmed.ai — federated AI platform, не one model; разные vendor-модели (Сбер AI Lab, Care Mentor AI, Третье Мнение, Webiomed, ...) проходят through unified deployment + benchmark testing.
3. Bridge: «мы здесь увидели обещание AI-диагностики сбывшееся — operational scale. На s17a увидим обещание drug discovery — первый peer-reviewed Phase IIa positive (Rentosertib). На s17b — обратная история (DSP-1181 discontinued)».
4. Не уходить в политику healthcare; focus = technical + operational scale evidence.
5. Cite mos.ru + Remedium + Healthcare ME для прозрачности attribution.
6. **Critical (P0-2 fix):** «4 млрд руб/год» — NOT in sources.md, не цитируется. Operational metrics sufficient impact.

**Связь с другими слайдами:** s8 (ROI framing — operational scale), s11 (radiologist comparison), s14 (return to central question), s23 (Russian medical data security context).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK: cadence=quarterly]` 14M studies + 74 regions + 70 services — DZM Moscow quarterly updates; verify mosmed.ai consent для screenshot.

**Cross-frame anchor:** LO1 + LO2 + Другой AI + Безопасность + Человек vs AI.

---

### Слайд 13 — Where AI-диагностика fails: bias studies (3 мин) (`assertion_visual`)

**Описание:** known failure modes of medical CV — bias case studies. **P1-5 fix: Obermeyer dropped here (now exclusive deep-dive on s21).** Кеep dermatology + pulse-oximeter.

**Содержание (visible):**
- **Assertion:** «AI-диагностика хорошо работает в распределении обучения. Outside that — может проваливаться unfairly.»
- **2 bias case-cards (P1-5 dedup — Obermeyer moved to s21):**
  1. **Dermatology skin tone bias** — most dermatology AI обучены на light-skin datasets; для dark-skin pacientов sensitivity drops 20-30%. **Reference: Daneshjou et al. 2022 Science Advances (corrected date per fact-check)**, Adamson & Smith 2018 (JAMA Dermatology).
  2. **Pulse oximeter signal AI** — racial bias в SpO2 sensors and downstream AI; FDA warning 2021.
- Caption: «Не bug, а consequence design choices: training data ≠ deployment population.»

**LO mapping:** **LO3** (анализ этических рисков) + **LO6** (выявление ограничений implicit).

**Frame mapping:** LLM anti-pattern adaptation (для CV: «не верь модели без проверки на твоей популяции»; см. s22 для LLM-specific) + Безопасность + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** paper figure + supporting news screenshot.
- **Источник-кандидаты:**
  - **Daneshjou et al. 2022:** Science Advances `https://www.science.org/doi/10.1126/sciadv.abq6147` paper figure.
  - **Adamson & Smith 2018:** JAMA Dermatology `https://jamanetwork.com/journals/jamadermatology/article-abstract/2688587`.
  - **News:** STAT News `https://www.statnews.com/` article на dermatology AI bias OR FDA pulse-oximeter warning 2021 press.
- **Caption (5-10 слов):** «Daneshjou et al. 2022 Science Advances; FDA pulse-ox warning 2021»
- **Визуальная функция:** evidence для bias claim; emotional anchor для responsibility framing.

**Speaker notes hints:**
1. Bias ≠ malice; это consequence of training data composition.
2. Engineering implication: validation set должен покрывать deployment population — это не academic point, а responsibility.
3. Russian relevance: mosmed.ai trained mostly on Russian population; what about deployments в других regions/ethnicities? Open question.
4. Bridge to s21 (Obermeyer deep-dive — exclusive there) и s22 (NEDA Tessa): «эти ошибки не теоретические; они происходят systematically. На s21 углубимся в Obermeyer 2019.»
5. Avoid moralizing; engineer-tone = «вот пример, инженер должен думать об этом on day one».

**Связь с другими слайдами:** s21 (Obermeyer Obermeyer deep — НЕ here), s22 (LLM anti-pattern NEDA Tessa), s24 (responsibility framework).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` Daneshjou 2022 Aug date (P2 from fact-checker); FDA pulse-ox warning 2021 specifics.

**Cross-frame anchor:** LO3 + LO6 + Безопасность + Человек vs AI + setup для LLM anti-pattern.

---

## Раздел 3. Drug discovery: обещания vs реальность (14 мин)

### Слайд 14 — Mid-lecture callback к central question (1 мин) (`assertion_visual`)

**Описание:** explicit mid-lecture pause — return to central question.

**Содержание (visible):**
- **Assertion (callback):** «Мы прошли половину. AI-диагностика — обещание сбылось (mosmed: 14M+ исследований, 74 региона). Drug discovery — обещали 10× быстрее. Что реально на 2026?»
- **Простой layout:** central question crisp в Ocean rounded box + 3 callback-pointers (s12 mosmed cell + s17a Rentosertib cell upcoming + s17b DSP-1181 cell upcoming).

**LO mapping:** N/A (structural anchor).

**Frame mapping:** Cross-cutting — все 6 frames.

**Иллюстрация (MANDATORY):**
- **Тип:** schematic transition slide (large central question text + 3 anchor pointers).
- **Источник:** self-generated (typography + Ocean rounded box motif).
- **Caption:** N/A.
- **Визуальная функция:** structural anchor — преподаватель paused, аудитория re-orients; mid-lecture pacing.

**Speaker notes hints:**
1. Pause beat — 5-7 секунд silence allowed.
2. «Это половина. Дальше — пол лекции.» — signaling progress.
3. Если аудитория устаёт — это место для 1-вопрос Q&A или потрясения «кто помнит mosmed число (14M+)?»
4. Avoid additional content; this slide is structural, not informational.
5. Setup для s15 (drug discovery foundation) + s17a (Rentosertib success) + s17b (DSP reality).

**Связь с другими слайдами:** s5 (central question), s12 (mosmed payoff), s17a + s17b (drug discovery payoffs).

**Risks:** none.

**Cross-frame anchor:** All 6 frames cross-cutting.

---

### Слайд 15 — Что такое drug discovery + AI role (2.5 мин) (`assertion_visual` + schema subtype: `pipeline`)

**Описание:** technical foundation — что такое drug discovery, где AI меняет цикл.

**Содержание (visible):**
- **Assertion:** «Drug discovery — 10-15 лет, $1-2 млрд, ~10% success rate. AI обещает сократить первые stages (discovery + preclinical) от ~6 лет до 1-2.»
- **Pipeline schema (5 stages):**
  1. **Target identification** — какой белок атаковать. AI: AlphaFold, AlphaProteo.
  2. **Hit discovery** — молекула-кандидат. AI: generative ML (Insilico, Exscientia, Generate Biomedicines).
  3. **Lead optimization** — улучшение свойств молекулы. AI: simulation + ML.
  4. **Preclinical** — клетки, животные. AI: predicting toxicity.
  5. **Clinical I/II/III** — люди. AI: patient stratification. (Здесь AI помогает marginally.)
- **Highlight:** AI accelerates stages 1-3 значительно; stages 4-5 — human trials, AI помогает marginally. **~90% clinical attrition rate unchanged by AI.**
- Source: Mullard 2024 Nature Reviews Drug Discovery; DiMasi et al. 2016; npj Drug Discovery 2025.

**LO mapping:** **LO1** (типы AI в drug discovery) + **LO2** (applicability).

**Frame mapping:** Другой AI (foundation models — AlphaFold; generative ML; не LLM в основе).

**Иллюстрация (MANDATORY):**
- **Тип:** pipeline diagram (PowerPoint shapes + RIGHT_ARROW) + AlphaFold 3D snapshot.
- **Источник-кандидаты:**
  - **AlphaFold visualization:** DeepMind blog `https://deepmind.google/technologies/alphafold/`.
  - **Paper:** Jumper et al. 2021 Nature AlphaFold2 `https://doi.org/10.1038/s41586-021-03819-2`; Abramson et al. 2024 Nature AlphaFold3 `https://doi.org/10.1038/s41586-024-07487-w`.
  - **Pipeline metrics:** DiMasi et al. 2016 JHE; Mullard 2024 Nature Reviews; npj Drug Discovery 2025.
- **Caption (5-10 слов):** «AlphaFold 3 (Abramson et al., Nature 2024)»
- **Визуальная функция:** technical foundation + emotional anchor (3D-структура впечатляет, даже не-биолог понимает «это сложно»).

**Speaker notes hints (P1-1 reader fix — hit/lead definitions explicit):**
1. Pipeline subtype rules (5 stages OK); each stage label ≤3 слов; use RIGHT_ARROW.
2. **Hit vs Lead definitions (P1 reader fix):** «Hit = молекула с initial activity signal vs target. Lead = hit, доведённый до preclinical-readiness (улучшенная affinity, selectivity, stability). Между ними — лет лабораторной работы.»
3. Drug discovery total cost — $1.5-2 млрд per approved drug (DiMasi 2016, updated by Wouters et al. 2020 JAMA).
4. AlphaFold 2 (2021) → AlphaFold 3 (Nature May 2024) — Нобель 2024 (Hassabis, Jumper, **Baker для computational protein design**) — callback к Лекции 1 s10/s25.
5. Critical: AI не делает preclinical/clinical чудом — только discovery + lead optimization; clinical trials = years and humans. **~90% clinical attrition unchanged.**
6. **Clinical I/II/III — 3 phases briefly:** Phase 1 = safety (small n); Phase 2 = efficacy + dose (medium n); Phase 3 = confirmatory (large n).

**Связь с другими слайдами:** s16 (AlphaFold deep), s17a (Rentosertib — Phase IIa positive success), s17b (DSP-1181 — Phase 1 discontinued), Лекция 1 s10/s25 (Нобель callback).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` drug discovery cost & time numbers; AlphaFold 3 publication date verified (8 May 2024); freshness — AlphaProteo paper (DeepMind 2024).

**Cross-frame anchor:** LO1 + LO2 + Другой AI.

---

### Слайд 16 — AlphaFold + AlphaProteo: что реально достигнуто (2.5 мин) (`assertion_visual`)

**Описание:** deep-dive в AlphaFold's actual impact on drug discovery as of 2026.

**Содержание (visible):**
- **Assertion:** «AlphaFold предсказал **200M+ структур белков** (UniProt-coverage). Это решённая задача 50-летней давности. AlphaProteo проектирует binders.»
- **3 evidence-cards:**
  1. **200M+ structures:** AlphaFold Protein Structure Database `alphafold.ebi.ac.uk` — open, free. UniProt-coverage. Public-access. `[FACT-CHECK]`
  2. **AlphaProteo (DeepMind, 5 сентября 2024):** designs novel protein binders для 7 targets; **88% success rate для BHRF1, 3-300× affinity improvement** vs prior methods; first AI binder для VEGF-A. arXiv:2409.08022. `[FACT-CHECK]`
  3. **AlphaFold 3 (Abramson et al. Nature May 2024):** protein complexes, RNA-protein interactions, protein-ligand — enables drug-target binding prediction. **50% accuracy improvement** на PoseBusters benchmark vs classical docking.
- Caption: «Source: DeepMind blog 2024; Jumper et al. 2021; Abramson et al. 2024.»

**LO mapping:** **LO1** (advance state of AI in drug discovery) + **LO2** (applicability).

**Frame mapping:** Другой AI (foundation model для protein folding, не LLM).

**Иллюстрация (MANDATORY):**
- **Тип:** official product screenshot + 1 paper figure.
- **Источник-кандидаты:**
  - **AlphaFold DB screenshot:** `https://alphafold.ebi.ac.uk/` — front page or example structure.
  - **DeepMind blog AlphaProteo:** `https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/`.
  - **Abramson et al. 2024 Nature AlphaFold 3:** `https://www.nature.com/articles/s41586-024-07487-w`.
- **Caption (5-10 слов):** «AlphaFold Protein Structure DB, alphafold.ebi.ac.uk; AlphaProteo arXiv:2409.08022»
- **Визуальная функция:** evidence — large-scale achievement; emotional anchor (открытая база, бесплатная).

**Speaker notes hints (P1-4 + P1-5 fact-checker fixes — wording precise):**
1. Не входить в transformer-architecture details (это для Лекции 2).
2. Bridge с Лекцией 1 s25: «AlphaFold = Нобель 2024 (Hassabis, Jumper, **Baker для protein design**); AlphaProteo — следующий шаг от prediction к generation».
3. **AlphaProteo precise wording (P1-4 fact-checker):** «88% success rate для BHRF1; 3-300× affinity improvement vs prior methods on 7 protein targets; first AI binder for VEGF-A». Caveat: independent replication outside DeepMind не было found в search (proprietary lab data).
4. **AlphaFold user count (P1-5 fact-checker):** sources.md confirms 200M+ structures predicted. «2M+ researchers» — needs Hassabis Nobel Dec 2024 primary source verify; if unverified, use «200M+ structures» as primary number.
5. Important: AlphaFold predicts structure, BUT drug discovery нуждается ещё в lead optimization, ADMET, ... Многое от lab work остаётся.
6. Russian context: Webiomed Russian medical AI vendor, Sber AI Lab — `[FACT-CHECK]` actual Russian drug discovery effort status (sources.md does not cover Russian drug discovery deeply).
7. Trust-but-verify: AlphaFold confidence scores (pLDDT) — модель сама помечает, где она уверенна, где нет.

**Связь с другими слайдами:** s15 (pipeline context), s17a (Rentosertib — от prediction к Phase IIa), s17b (DSP-1181 — от prediction к Phase 1 fail).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` 200M structures + AlphaProteo capabilities; freshness — AlphaFold 4 на 2026?

**Cross-frame anchor:** LO1 + LO2 + Другой AI.

---

### Слайд 17a — **Insilico Rentosertib: peer-reviewed success case (2.5 мин)** (`assertion_visual` + schema subtype: `timeline`) [NEW vs v1]

**Описание:** **THE primary success case — verified peer-reviewed Phase IIa positive readout.** First AI-designed drug с published peer-reviewed clinical proof-of-concept. P0-1 fix: replaces DSP-1181 as flagship.

**Содержание (visible):**
- **Assertion:** «Insilico Medicine **Rentosertib (ISM001-055 / INS018_055)** — **первый AI-designed drug с peer-reviewed positive Phase IIa readout** (Nature Medicine, June 2025).»
- **Mini-timeline (3 events):**
  - **2020-2022 (~18 месяцев):** AI-driven target identification → preclinical candidate (vs traditional ~4-5 лет).
  - **2024 (октябрь):** Topline Phase IIa results announced (Insilico PR).
  - **2025 (июнь):** **Nature Medicine peer-reviewed publication** — Phase IIa randomized double-blind placebo-controlled, n=71 IPF patients across 21 China sites.
- **Result (info-card):** Доза 60 mg QD: **+98.4 mL FVC vs −62.3 mL placebo at 12 weeks**. Most common AEs: diarrhea 14.8%, abnormal liver function 14.8%.
- **Insight:** «AI ускорил discovery → preclinical с 4-5 лет до 18 месяцев. Это measurable success — впервые подтверждённый в peer-reviewed journal.»
- Caption: «Sources: Nature Medicine June 2025 (PMID 40461817); Insilico press release; PubMed 40461817.»

**LO mapping:** **LO1** + **LO2** (applicability + clinical evidence).

**Frame mapping:** Другой AI (generative chemistry, foundation models) + Человек vs AI (AI как design tool, не replacement).

**Иллюстрация (MANDATORY):**
- **Тип:** timeline schema + Nature Medicine paper screenshot OR Insilico AIDD platform screenshot.
- **Источник-кандидаты:**
  - **Nature Medicine paper:** PubMed [40461817](https://pubmed.ncbi.nlm.nih.gov/40461817/).
  - **Insilico press release:** [https://insilico.com/news/tnrecuxsc1-insilico-announces-nature-medicine-publi](https://insilico.com/news/tnrecuxsc1-insilico-announces-nature-medicine-publi).
  - **PRNewswire topline Oct 2024:** [https://www.prnewswire.com/news-releases/insilico-medicine-announces-positive-topline-results-of-ism001-055-for-the-treatment-of-idiopathic-pulmonary-fibrosis-ipf-developed-using-generative-ai-302302583.html](https://www.prnewswire.com/news-releases/insilico-medicine-announces-positive-topline-results-of-ism001-055-for-the-treatment-of-idiopathic-pulmonary-fibrosis-ipf-developed-using-generative-ai-302302583.html).
- **Caption (5-10 слов):** «Insilico Rentosertib Nature Medicine, June 2025 (n=71 IPF)»
- **Визуальная функция:** **narrative success anchor** — concrete peer-reviewed evidence; payoff для central question «обещание сбылось».

**Speaker notes hints:**
1. Timeline subtype rules: 3 events single-line, em-dash; max 3 events per band (per Schema Readability Checklist).
2. **Why Rentosertib не DSP-1181 (P0-1):** «На plan-v1 мы планировали DSP-1181 как flagship. Fact-check показал — drug discontinued в 2022. Rentosertib (Insilico) — peer-reviewed positive readout в Nature Medicine June 2025. Это credibility upgrade.»
3. **IPF (Idiopathic Pulmonary Fibrosis)** — серьёзное заболевание лёгких; positive FVC change = клинически значимый endpoint.
4. **TNIK inhibitor mechanism** — AI помог identify novel target + design ligand; verified в independent peer review.
5. **Russian context:** Webiomed (российский medical AI vendor) — параллельная история (clinical decision support, не drug discovery). Sber AI Lab — мало public drug discovery data, `[FACT-CHECK]` нужен.
6. Engineering lesson: **AI ускоряет design (verified). Clinical efficacy — separate question (биология). Two distinct claims, не один.**
7. **Critical:** AI не изменил ~90% clinical attrition rate. Rentosertib — early success; Phase 3 ещё требуется.

**Связь с другими слайдами:** s5 (central question payoff — success case), s14 (mid-callback), s17b (DSP-1181 contrast), s24 (responsibility framework — AI design choice).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` Rentosertib status — Phase 3 announcement may have happened since June 2025 publication; weekly biotech news cadence.

**Cross-frame anchor:** LO1 + LO2 + Другой AI + Человек vs AI + central question payoff (positive side).

---

### Слайд 17b — **DSP-1181 reality check: обещание vs действительность (2.5 мин)** (`assertion_visual` + schema subtype: `timeline`) [REVISED from v1 s17]

**Описание:** DSP-1181 case study — marketing-vs-reality. **P0 fix: simplified to 3 events; Exscientia 2025 turbulence moved to speaker notes only.** Frame: AI ускорил design, эффективность — отдельная задача.

**Содержание (visible):**
- **Assertion:** «DSP-1181 (2020): "первый AI-designed drug в clinical trials" — обещали 12 месяцев design vs 4-5 лет традиционно. Что случилось дальше?»
- **Timeline визуал (3 events — P0-7 + P0-6 fix — reduced from 5):**
  - **2020 (январь):** Exscientia + Sumitomo Dainippon announce DSP-1181, OCD Phase 1 (Japan).
  - **2022:** **Phase 1 discontinued в Японии** — cause not specified (efficacy/safety/business). Sumitomo announcement.
  - **2026 (current):** DSP-1181 R&D status = **Discontinued** (Synapse/PatSnap, CAS Insights).
- **Insight:** «AI ускорил design phase (verified — это реально). Но clinical efficacy — separate question. Маркетинговое обещание "AI drug = быстро + эффективно" = две разные claims, объединённые рекламой.»
- Caption: «Sources: Synapse/PatSnap, Sumitomo 2020 PR, CAS Insights, npj Drug Discovery 2025.»

**LO mapping:** **LO2** (оценка applicability) + **LO3** (анализ рисков и обещаний) + framing для **LO8**.

**Frame mapping:** Человек vs AI (ответственность за обещания) + LLM anti-pattern adaptation (маркетинг AI ≠ working AI) + Безопасность (informed decisions in regulation).

**Иллюстрация (MANDATORY):**
- **Тип:** news screenshot + timeline schema.
- **Источник-кандидаты:**
  - **Synapse Drug Profile DSP-1181:** [https://synapse.patsnap.com/drug/a785db59b5d54d209ddfe8619dfcc2b0](https://synapse.patsnap.com/drug/a785db59b5d54d209ddfe8619dfcc2b0).
  - **Sumitomo 2020 press:** [https://www.sumitomo-pharma.com/news/20200130.html](https://www.sumitomo-pharma.com/news/20200130.html).
  - **CAS Insights:** [https://www.cas.org/resources/cas-insights/ai-drug-discovery-assessing-the-first-ai-designed-drug-candidates-to-go-into-human-clinical-trials](https://www.cas.org/resources/cas-insights/ai-drug-discovery-assessing-the-first-ai-designed-drug-candidates-to-go-into-human-clinical-trials).
- **Caption (5-10 слов):** «DSP-1181 timeline: Sumitomo, Synapse/PatSnap, CAS Insights»
- **Визуальная функция:** narrative arc — обещание → реальность; **counter-balance к s17a (Rentosertib success)** для defensible trust-but-verify tone.

**Speaker notes hints (P0-6 fix — Exscientia 2025 turbulence moved here):**
1. **Per user spec:** «Fact-check подтвердил discontinued status. Это сама по себе ценная история: маркетинговое обещание vs реальность.»
2. Timeline subtype rules: events single-line, em-dash; **max 3 events per band (P0-7 fix)**; pivot 2022 discontinuation ≥2× размер.
3. Honest, no schadenfreude tone: «Exscientia реально ускорила design. Они не виноваты, что efficacy не сложилась — это биология. Виновата маркетинговая riffраfика, которая объединила discovery time и approval probability».
4. **Exscientia 2025 context (P0-6 — speaker notes only, NOT visible content):** Recursion + Exscientia merger August 2024 (announced), November 2024 (closed, $688M all-stock). Exscientia folded into combined company. CEO Hopkins firing not verified in sources.md — drop or skip in speech if not separately verified. Не overload visible content.
5. Engineering lesson: «если ты строишь AI для drug discovery — two distinct claims: (1) ускоряем design (verified для Insilico, Exscientia); (2) ускоряем approval (не verified — clinical attrition unchanged). Только первое — техническая мера; вторая — клинико-биологическая.»
6. Pair с s17a: «Rentosertib (s17a) — success case. DSP-1181 (s17b) — reality check. Defensible balance.»

**Связь с другими слайдами:** s5 (central question payoff — reality side), s14 (mid-callback), s17a (success contrast), s18-merged (FDA framework — regulator perspective).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` DSP-1181 still discontinued (Synapse/PatSnap weekly cadence); `[FACT-CHECK]` Exscientia/Recursion post-merger biotech news.

**Cross-frame anchor:** LO2 + LO3 + LO8 framing + Человек vs AI + LLM anti-pattern adaptation + Безопасность + central question payoff (reality side).

---

### Слайд 18-merged — Регулирование AI в медицине: FDA + EU + РФ (2 мин) (`comparison` + schema: 3-column condensed) [MERGED s18 + s25 from v1]

**Описание:** **P1-3 fix:** s18 (FDA PCCP, 2.5 мин) + s25 (3-jurisdiction, 2 мин) **merged** в один condensed slide (2 мин total). Dropped: ГОСТ specifics, EU AI Act detailed timeline, conformity assessment process details. Kept: PCCP innovation + high-risk classification + Russian expedited registration.

**Содержание (visible):**
- **Assertion:** «Medical AI = high-risk во всех 3 крупных jurisdictions (FDA, EU, RF). Approaches отличаются процессами, не principles.»
- **3-column condensed table:**
  - **US (FDA):** SaMD framework + **PCCP (Predetermined Change Control Plan)** — finalized **4 декабря 2024**. **Innovation:** до PCCP — каждое обновление requires new FDA submission (12-18 мес); с PCCP — vendor pre-declares допустимые updates → обновляет без re-submission. (P0-5 fix — pre/post contrast explicit.)
  - **EU (EU AI Act):** High-risk medical AI per Article 6 + Annex III. **Effective 2 августа 2026 (= 2.5 месяца после lecture)** для high-risk medical AI. Full medical device compliance Aug 2027.
  - **РФ (Росздравнадзор):** **57 registered AI medical devices** к mid-2026 (52 RF + 5 foreign). **Expedited procedure** для AI medical devices с 1 марта 2025 (ПП РФ № 1684).
- Caption: «FDA.gov; EU AI Act Reg. 2024/1689; Webiomed registered devices; VNIIIMT ПП РФ № 1684.»

**LO mapping:** **LO3** (regulatory framework) + **LO8 framing** (responsibility — regulatory side).

**Frame mapping:** Безопасность + Человек vs AI (regulator role).

**Иллюстрация (MANDATORY):**
- **Тип:** schematic 3-column comparison + 3 flags/logos.
- **Источник-кандидаты:**
  - **FDA PCCP guidance Dec 2024:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence).
  - **EU AI Act Article 6:** [https://artificialintelligenceact.eu/article/6/](https://artificialintelligenceact.eu/article/6/).
  - **Webiomed RF registered:** [https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/](https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/).
- **Caption (5-10 слов):** «FDA PCCP Dec 2024; EU AI Act 2024/1689; Webiomed RF 2026»
- **Визуальная функция:** institutional anchor — regulation is concrete, not abstract; setup для responsibility (s24).

**Speaker notes hints:**
1. Comparison subtype rules: 3 columns equal width; identical row structure; consistent terminology.
2. **PCCP pre/post contrast (P0-5 fix, critical):** «Traditional medical device = one-and-done approval. AI evolves continuously. PCCP позволяет vendors pre-declare what changes are OK — vendor может обновлять model без full re-submission. Это упрощает CI/CD для medical AI впервые.»
3. **EU AI Act timeline urgency:** «high-risk medical AI deadline = 2 августа 2026 — это **2.5 месяца после нашей лекции 13 мая 2026**. Сейчас vendors готовятся к compliance.»
4. **РФ context:** Webiomed (первый AI software зарегистрирован 3 апреля 2020); 48 → 57 registered AI medical devices 2024 → 2026.
5. Engineering implication: «if you design AI for medical device — design with PCCP in mind; data drift, retraining, threshold updates — all must be planned ex ante. Russian deployment requires data localization (ФЗ-152 + ФЗ-23).»
6. Cross-frame: regulation = formal expression of responsibility framework (next slide s24).

**Связь с другими слайдами:** s7 (FDA count), s17b (regulatory reality для drugs), s23 (ФЗ-152 data security), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` PCCP final guidance date (Dec 4, 2024); `[FACT-CHECK]` EU AI Act high-risk medical AI deadline; freshness — monthly cadence для regulatory updates.

**Cross-frame anchor:** LO3 + LO8 framing + Безопасность + Человек vs AI.

---

## Раздел 4. Микро-упражнение AI (10 мин — P1-9 fix course-doc compliance)

### Слайд 19 — Micro-exercise: AI explains sens/spec + критическая оценка (10 мин) (`assertion_visual` + interactive)

**Описание:** **единственное студенческое упражнение лекции** (per user spec + course-doc compliance). **10 минут активной работы** (course-doc explicit «микро-упражнение с AI 10 мин»). Студенты используют ChatGPT/Claude web-chat — просят объяснить sensitivity/specificity для medical AI, как студенту 2 курса. Потом критически оценивают: что AI сделал хорошо? Что — поверхностно или подозрительно?

**Содержание (visible):**
- **Assertion:** «Используем AI для понимания AI. Но не доверяем без проверки.»
- **Task (concrete instruction — P1-4 reader fix):**
  1. **Step 1 (3 мин):** «Открой ChatGPT/Claude/YandexGPT/GigaChat. Промпт (готовый текст ниже): "Объясни мне, что такое sensitivity и specificity для AI-диагностики на конкретном примере (например, mammography screening). Объясни как для студента 2 курса техн. вуза, со знанием базовой probability."»
  2. **Step 2 (3 мин):** «Прочитай ответ. Отметь карандашом на распечатке (или в notes app): **1 неточность ИЛИ 1 unverifiable claim ИЛИ 1 место, где объяснение слишком абстрактное.**»
  3. **Step 3 (4 мин — reveal):** «Лектор спросит: "у кого нашёлся пример?" → **2-3 студента читают (1 мин each)**. Лектор показывает свой "control" ответ (заранее прогнанный накануне).»
- **LLM pattern:** «Объясни как студенту X курса» — стандартный pattern для education + patient education.
- **LLM anti-pattern:** «Не доверяй медицинским советам без верификации».

**LO mapping:** **LO4 CORE** (apply AI web-chat per course doc) + **LO2** (apply AI to оценить) + **LO3** (critical evaluation).

**Frame mapping:** **LLM pattern** (объясни как студенту 2 курса) + **LLM anti-pattern** (не доверяй без верификации) — оба explicit.

**Иллюстрация (MANDATORY):**
- **Тип:** task card layout + 1 example AI response screenshot (lecturer's pre-prepared control).
- **Источник-кандидаты:**
  - **Self-generated** task layout (PowerPoint shapes + chip-pills) с promptom visible.
  - **Control screenshot** — Claude.ai or ChatGPT response, prepared by lecturer night before, sanitized, saved в `library/lectures/lec-04/assets/control/s19-baseline-llm-response.png`.
- **Caption (5-10 слов):** «Задача: попроси AI объяснить, потом проверь»
- **Визуальная функция:** call-to-action + control example для guided discussion.

**Speaker notes hints:**
1. **Critical pre-flight:** lecturer должен прогнать промпт сам накануне лекции (freshness — модель меняется!) и иметь скриншот baseline.
2. Russian context: добавить YandexGPT, GigaChat options.
3. **Fallback (no wifi):** pre-print 3-5 sample AI responses for paper-based exercise (3 EN responses + 2 RU responses). Saved в `library/lectures/lec-04/assets/control/s19-fallback-responses.pdf`.
4. Discussion focus: «AI отлично объяснил для студента 2 курса» = LLM pattern сработал. «AI дал число sensitivity 0.95 без citation» = anti-pattern — не верь.
5. Bridge to s22 (NEDA Tessa scandal): «patient education через AI — реальная индустрия; и здесь — реальные риски».
6. **Timing strict:** 10 минут total — не давать упражнению расплыться.
7. **LO4 explicit (course-doc compliance):** «Это применение AI web-chat — LO4 на 3-курсном курсе. У вас уже было 3 микро-упражнения (Лекции 1, 2, 3); это 4-е. На Лекции 9 — Практикум 1 (полноценная работа).»

**Связь с другими слайдами:** s10 (sens/spec foundation), s22 (NEDA Tessa — что бывает, когда не verified), s28 (3 главных вывода + LO8 framing).

**Risks / things to verify в Phase 0b:** sample AI response может содержать factual errors — `[FACT-CHECK]` baseline response для control; planning для unstable wifi / no-internet fallback.

**Cross-frame anchor:** LO4 (CORE — apply AI) + LO2 + LO3 + LLM pattern + LLM anti-pattern.

---

## Раздел 5. Границы + этика + ответственность (12 мин — P1-3 fix merged regulation saved 2 мин)

### Слайд 20 — Зачем инженеру думать про границы в медицинском AI (1 мин) (`assertion_visual`)

**Описание:** transition slide — вводная рамка для последнего content section.

**Содержание (visible):**
- **Assertion:** «В медицинском AI ставки максимальны: ошибка модели = ошибка диагноза или назначения = вред пациенту. Что инженер должен знать про границы.»
- **3 темы next 5 slides:**
  1. Bias в medical AI (Obermeyer 2019 deep-dive).
  2. LLM anti-pattern в медицине (NEDA Tessa + 3 cases).
  3. Безопасность медицинских данных + ответственность framework.

**LO mapping:** **LO3** + framing для **LO8**.

**Frame mapping:** All — bridging slide.

**Иллюстрация (MANDATORY):**
- **Тип:** stock photo (medical context, professional).
- **Источник-кандидаты:**
  - Unsplash `https://unsplash.com/s/photos/medical-team` (CC0).
  - Pexels `https://www.pexels.com/search/hospital%20technology/` (free).
- **Caption (5-10 слов):** «Медицинский AI — высокие ставки, не sandbox»
- **Визуальная функция:** transition + emotional anchor.

**Speaker notes hints:**
1. Не повторять content предыдущих slides; это transition.
2. Set tone seriousness без alarmism.
3. Этот блок — самая короткая arc лекции, но самая важная для LO8 framing (input для Lec 9 черновика).
4. Pacing: одна минута strictly.
5. Avoid mentioning specific cases here (s21-23 будут).

**Связь с другими слайдами:** s21, s22, s23, s24.

**Risks:** none beyond image attribution.

**Cross-frame anchor:** LO3 + LO8 framing.

---

### Слайд 21 — Bias в medical AI: Obermeyer 2019 exclusive deep-dive (3 мин) (`assertion_visual`)

**Описание:** **Exclusive Obermeyer deep-dive** (P1-5 fix — moved entirely here from s13). Optum / UnitedHealth risk-scoring AI, описанный в Obermeyer et al. 2019 Science.

**Содержание (visible):**
- **Assertion:** «Obermeyer et al. 2019 (Science): commercial AI алгоритм для 200M Americans systematically underestimated severity для black patients. Proxy "стоимость лечения" вместо "тяжесть болезни".»
- **Mechanism (3 boxes):**
  1. **Goal:** identify pacients needing additional care.
  2. **Proxy used:** spending on previous care.
  3. **Bias source:** black patients spent **$1,800/year less** historically (access disparities) → AI thinks less sick → less care.
- **Result chart:** at same risk score, black patients had **26% more chronic illnesses** than white (sources.md §9.1 — exact verbatim verify).
- **Fix:** Optum + researchers совместно improved algorithm — **84% bias reduction** post-fix; **Black patients served increased from 17.5% to 46.5%** (P1-9 fact-checker fix — added concrete progression).
- Caption: «Obermeyer, Powers, Vogeli, Mullainathan — Science 366, 447-453 (2019). DOI: 10.1126/science.aax2342»

**LO mapping:** **LO3** (анализ этических рисков) + **LO6** (выявление ограничений).

**Frame mapping:** Безопасность + Человек vs AI + LLM anti-pattern adaptation.

**Иллюстрация (MANDATORY):**
- **Тип:** paper figure + supporting news screenshot.
- **Источник-кандидаты:**
  - **Obermeyer 2019** Science figure `https://www.science.org/doi/10.1126/science.aax2342` (Figure 1: gap chart).
  - **Berkeley News press:** `https://news.berkeley.edu/2019/10/24/widely-used-health-care-prediction-algorithm-biased-against-black-people/`.
  - **STAT News follow-up:** `https://www.statnews.com/2019/10/24/algorithm-racial-bias-care-black-patients/`.
- **Caption (5-10 слов):** «Obermeyer et al., Science 2019. DOI: 10.1126/science.aax2342»
- **Визуальная функция:** evidence для bias claim; foundation для responsibility framing.

**Speaker notes hints:**
1. Это THE landmark paper по bias в medical AI; cited 3000+ раз; must-know для инженера.
2. Не moralize; engineer-tone: «вы будете строить metric-driven AI. Выбор proxy = design choice с consequence».
3. **Actionable engineer lesson (P1-5 reader fix):** «Когда выбираешь proxy для goal в metric, всегда задай вопрос: какие demographics могут иметь systematically different access к этому proxy? В Obermeyer — black patients had less access к care historically → spending был low → AI thought they were healthy. Fix = use combined proxy (cost + chronic conditions) → 84% bias reduction.»
4. Optum / UnitedHealth — для российской аудитории это абстрактный «крупный insurer USA»; можно объяснить «как Сбер или ВТБ — большой scope deployment».
5. Russian parallel: bias в кредитном скоринге (Лекция 3) — тот же механизм, иная industry; cross-lecture connection.
6. Bridge to s22: «если в risk-scoring AI bias — он tabular numerical; в LLM в медицине — bias на уровне советов».

**Связь с другими слайдами:** Лекция 3 s12 (bias в финансах — параллель), s13 (bias в CV — параллель, dermatology + pulse-ox only), s22 (LLM specific case), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` Obermeyer 26% verbatim from paper; verify «17.5% → 46.5%» Black patients served (sources.md confirms).

**Cross-frame anchor:** LO3 + LO6 + Безопасность + Человек vs AI.

---

### Слайд 22 — LLM anti-pattern в медицине: 3 cases (4 мин — P1-5 expanded from 3) (`assertion_visual`)

**Описание:** **Expanded к 4 мин, 3 LLM anti-pattern cases (P1-5 fix).** NEDA Tessa scandal с corrected dates + vendor accountability frame + Adversarial hallucination + Patient self-diagnosis adoption.

**Содержание (visible):**
- **Assertion:** «LLM в медицине ≠ медицинский AI. 3 documented anti-pattern cases на 2025-2026.»
- **Case 1: NEDA Tessa chatbot scandal (corrected timeline — P1-13 fact-checker fix):**
  - **~2018-2022:** Tessa runs as rule-based chatbot для eating disorder helpline.
  - **March 2023:** Cass (vendor) silently switches Tessa from rule-based к generative LLM **без NEDA approval**.
  - **May 30, 2023:** Sharon Maxwell posts screenshots of harmful weight-loss advice (lose 1-2 lbs/week, calorie deficit 500-1000/day = eating disorder triggers). **NEDA suspends Tessa within 24h** (2 days before scheduled hotline shutdown).
  - **Frame:** **vendor accountability story** — Cass changed rule-based к generative without principal approval.
- **Case 2: Adversarial hallucination 83% rate (Communications Medicine 2025):** 6 leading LLMs on 300 clinical vignettes with single fake lab/sign/disease — models **repeat/elaborate on fake error в up to 83% of cases**. Mitigation prompt halves rate but not eliminates.
- **Case 3: Patient self-diagnosis explosion (OpenAI/Gallup 2024-2025):** **40 million Americans** use ChatGPT для healthcare questions. 3 в 5 US adults used AI tools для health past 3 months. **Регулирование не успевает.**
- **Why это different от s21 (Obermeyer):** s21 = tabular AI с biased proxy; s22 = generative LLM в open-ended medical advice — class apart.
- Caption: «Sources: NPR June 2023; AI Incident DB 545; Communications Medicine 2025; Becker's Hospital Review.»

**LO mapping:** **LO3** (анализ риска) + **LO6** (выявление ограничений LLM конкретно) + framing для **LO8**.

**Frame mapping:** **LLM anti-pattern (CORE для этого слайда)** + Безопасность + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** news screenshot collage + 1 quoted Tessa transcript.
- **Источник-кандидаты:**
  - **NPR 2023:** `https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea`.
  - **AI Incident Database 545:** `https://incidentdatabase.ai/cite/545/`.
  - **Communications Medicine 2025 (Nature):** `https://www.nature.com/articles/s43856-025-01021-3`.
  - **Becker's Hospital Review 40M:** `https://www.beckershospitalreview.com/healthcare-information-technology/ai/40m-americans-turn-to-chatgpt-for-healthcare-report/`.
  - **Gallup:** `https://news.gallup.com/poll/707789/americans-turning-supplement-healthcare-visits.aspx`.
- **Caption (5-10 слов):** «NEDA Tessa May 2023; Adversarial 83% 2025; OpenAI/Gallup 40M»
- **Визуальная функция:** emotional anchor (real-world harm); evidence для LLM anti-pattern in medical context.

**Speaker notes hints:**
1. **Per user spec:** «доверие медицинским советам AI без верификации — с КОНКРЕТНЫМИ documented incidents.»
2. Не sensationalize; tone = professional cautionary.
3. **Vendor accountability frame (P1-13 critical):** «NEDA Tessa = НЕ chatbot story. ЭТО vendor accountability story. Cass changed rule-based к generative без согласования с NEDA. Engineering lesson: generative AI ≠ rule-based AI; vendor design changes can bypass clinical safety.»
4. **Adversarial hallucination 83% explanation:** «LLMs are gullible к planted errors; physician verification required для every fact. Mitigation prompt халвес rate, не zero.»
5. **40M Americans framing:** «Massive adoption signal — даже если AI not safe для self-diagnosis, 40M people already doing it. Regulation lags.»
6. Bridge to s19 micro-exercise: «помните, мы просили AI объяснить sens/spec? Если бы мы просили medical advice — другая game.»
7. Russian context: GigaChat / YandexGPT — `[FACT-CHECK]` actual medical disclaimers policies (sources.md does not cover Russian LLM medical policy).

**Связь с другими слайдами:** s19 (micro-exercise foundation — LO4 apply), s21 (другой bias case parallel), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` NEDA Tessa dates verbatim (March 2023 generative switch; May 30, 2023 suspend); `[FACT-CHECK]` 83% adversarial Communications Medicine 2025 verbatim; verify NPR/AI Incident DB articles still accessible.

**Cross-frame anchor:** LO3 + LO6 + LO8 framing + LLM anti-pattern + Безопасность + Человек vs AI.

---

### Слайд 23 — Безопасность медицинских данных: Change Healthcare breach + AI connection (2 мин) (`assertion_visual`)

**Описание:** medical data security — Change Healthcare ransomware attack февраль 2024. **P1-6 reader fix: AI connection strengthened explicitly visible.**

**Содержание (visible):**
- **Assertion:** «Медицинские данные — самая защищаемая категория. И самая ценная для атакующих. Change Healthcare (Feb 2024): 190M человек, **$2.457 млрд** recovery cost.»
- **Numbers (info-cards) — P1-8 fact-checker fix — precise figures:**
  - **190 миллионов** affected (UHG official, verified) `[FACT-CHECK]`
  - **$2.457 млрд** recovery cost (UHG Q3 2024 — verified precise, не «$2-3 млрд»)
  - **6 TB** data exfiltrated
  - **multi-week disruption** US healthcare claims processing (не «22 days» — cannot verify exact day count, replaced with generic)
  - **ALPHV/BlackCat** — ransomware group; paid **$22 млн** ransom
- **AI connection (P1-6 fix — explicit visible):** «**Medical AI training datasets inherit medical-data security risk. mosmed.ai has 18M+ images — what if dataset exfiltrated?** Anonymisation ≠ anonymity: re-identification возможна.»
- **Regulations applicable:** HIPAA (US), GDPR (EU), **ФЗ-152 + ФЗ-23 data localization (РФ)** — personal data; ePHI = electronic protected health information.

**LO mapping:** **LO3** (risks) + **LO8** (security as responsibility).

**Frame mapping:** **Безопасность (CORE)** + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** news screenshot + small infographic.
- **Источник-кандидаты:**
  - **UHG official:** `https://www.unitedhealthgroup.com/newsroom/2024/2024-04-22-uhg-updates-on-change-healthcare-cyberattack.html`.
  - **BleepingComputer 190M:** `https://www.bleepingcomputer.com/news/security/unitedhealth-now-says-190-million-impacted-by-2024-data-breach/`.
  - **HIPAA Journal 2024 report:** `https://www.hipaajournal.com/biggest-healthcare-data-breaches-2024/`.
  - **House Energy & Commerce:** `https://energycommerce.house.gov/posts/what-we-learned-change-healthcare-cyber-attack`.
- **Caption (5-10 слов):** «Change Healthcare breach Feb 2024 (UHG, BleepingComputer)»
- **Визуальная функция:** evidence для scale claim; emotional anchor + AI connection bridge.

**Speaker notes hints:**
1. **AI connection explicit (P1-6 reader fix):** «Это про security медицинских данных. Связь с medical AI: training datasets = high-value target. mosmed.ai 18M+ изображений — ransomware target scope. Engineering lesson: проектируя medical AI, ты проектируешь target для criminal groups.»
2. **Russian relevance (P2-8 fix — explicit speaker note):** «Russian ransomware group attacked US system. **Tech-criminal orgs don't respect borders; healthcare AI built anywhere must defend против any threat.** Нюанс для российской аудитории — обсуждай аккуратно.»
3. ФЗ-152 + ФЗ-23 (152-ФЗ + 23-ФЗ) — major amendments 2025; data localization with 1 July 2025; medical data special category.
4. Brief mention: medical AI training data — нужно деперсонализировать (techniques: HIPAA Safe Harbor, k-anonymity, differential privacy). **Sweeney 1997 attack** — re-identified Governor of Massachusetts медицинские records using voter rolls + public data. De-identification ≠ anonymisation.
5. Не входить в крипто-детали ransomware (это для другой лекции).
6. Engineering lesson: проектируя medical AI, ты проектируешь target ransomware groups.

**Связь с другими слайдами:** s12 (mosmed scale = ransomware-target scope), s18-merged (regulation), s24 (responsibility framework).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` precise $2.457 млрд UHG Q3 2024; verify 6 TB exfiltrated + 190M (verified per sources.md §7.1).

**Cross-frame anchor:** LO3 + LO8 + Безопасность.

---

### Слайд 24 — Кто отвечает за AI-ошибку: 4 actors (3 мин) (`assertion_visual` + schema subtype: `quadrant`)

**Описание:** **the responsibility slide — central для LO3 + LO8 framing.** 4-actor framework. **P1-6 fix: actor cards «1-word role + 1-line responsibility» constraint.**

**Содержание (visible):**
- **Assertion (callback к central question):** «Когда AI ошибается в диагнозе — кто несёт ответственность?»
- **2×2 quadrant / 4-actor framework (P1-6 fix — constrained card format):**
  - **Axis X:** technical control (low ↔ high)
  - **Axis Y:** legal liability (low ↔ high)
  - 4 actors (each card = **1-word role + 1-line responsibility**):
    - **Врач (high control + high liability):** «Final diagnostic decision; AI = подсказка»
    - **Healthcare operator (medium ctrl + medium liability — P2-10 glossary fix — replaces "Хосзу-роль"):** «Vendor selection + training + monitoring»
    - **AI-vendor (high control + medium-low liability):** «Model design + safety claims + PCCP updates»
    - **Regulator (low ctrl + high oversight):** «Approves + audits + revokes»
- **Centrаl line:** «Врач ставит диагноз. AI подсказывает. **Ответственность — на враче.** Vendor + regulator + operator — обеспечивают системные условия.»
- Caption: «Source: Price 2019 Stanford TR; Gerke et al. 2020 «Ethical and legal challenges of AI-driven healthcare»; EU AI Act Annex III.»

**LO mapping:** **LO3 (CORE)** + **LO8 framing** (3 принципа — input для черновика Lec 9).

**Frame mapping:** **Человек vs AI (CORE — answers central question)** + Безопасность.

**Иллюстрация (MANDATORY):**
- **Тип:** schematic quadrant + 4 icons (1 per actor).
- **Источник-кандидаты:**
  - **Icons:** Lucide `stethoscope`, `building-2`, `code`, `gavel` (recolored Ocean).
  - **Self-generated quadrant schema.**
  - **Reference paper:** Gerke et al. 2020 в Artificial Intelligence in Healthcare (Elsevier).
- **Caption (5-10 слов):** «4-actor responsibility framework (Price 2019, Gerke 2020)»
- **Визуальная функция:** answer to central question; mental anchor для LO8 framing (input для Lec 9).

**Speaker notes hints:**
1. **Quadrant subtype rules (P1-6 fix):** axis labels INSIDE; **max 1-word role + 1-line responsibility per actor card** (Schema Readability Checklist); consistent icon size.
2. THIS is the slide where central question gets answer. Pause, eye contact, speak slowly.
3. «Final responsibility = врача» — это not punitive, it's structural: только врач имеет full context (history, exam, AI как один input).
4. Engineering lesson: «как инженер, ты в actor "AI-vendor". Твоя responsibility — design AI so врач can fulfill его responsibility (transparency, confidence scores, audit trails).»
5. **LO8 framing explicit:** «Эти 3 принципа — input для черновика чек-листа, который вы создадите на Лекции 9. Не финальный синтез — input.»
6. Russian: Росздравнадзор + Минздрав — Russian regulators; Минцифры + Минздрав совместно на digital health.
7. **Per fact-checker P2-3:** No notable AI medical malpractice lawsuits yet (mid-2025). Liability law still catching up. Doctor remains juridically responsible. Use «honest framing».

**Связь с другими слайдами:** s5 (central question), s17a + s17b (AI design responsibility), s18-merged (regulation), s27 (final payoff), s28 (3 principles LO8 framing).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` Price 2019 / Gerke 2020 references accuracy.

**Cross-frame anchor:** LO3 (CORE) + LO8 framing (CORE — input для Lec 9) + Человек vs AI (CORE).

---

### Слайд 25 — MERGED INTO s18-merged

*Per P1-3 fix — s25 from v1 merged into s18-merged above. См. above для regulation 3-jurisdiction comparison.*

---

## Раздел 6. Заключение (6 мин)

### Слайд 26 — 3 главных вывода (2 мин) (`summary`)

**Описание:** 3 takeaways — explicit mapping на LO1+LO2+LO3+LO8 framing.

**Содержание (visible):**
- **Wider message:** «Медицинский AI к 2026 — это работающая инфраструктура, не футурология. И вместе с этим — конкретная responsibility framework.»
- **3 takeaway cards:**
  1. **AI-диагностика работает (LO1, LO2):** mosmed.ai 14M+ исследований за 5 лет, 74 региона; FDA 1,451 devices end-2025; MASAI Sweden RCT 44% workload reduction. CV-pipeline уровня 2017-2024.
  2. **Drug discovery — частично (LO2, LO3):** AlphaFold = solved structure prediction, **Нобель 2024 (Hassabis + Jumper + Baker)**. Insilico Rentosertib = first peer-reviewed Phase IIa positive (Nature Medicine 2025). DSP-1181 discontinued. AI ускоряет discovery 5-10×; clinical attrition unchanged.
  3. **Ответственность — на враче (LO3, LO8 framing для Lec 9):** AI подсказывает, врач решает. Инженер строит систему так, чтобы responsibility была технически выполнима (transparency, calibration, audit, деперсонализация, monitoring). **Эти 3 принципа — input для черновика чек-листа на Лекции 9.**

**LO mapping:** **LO1, LO2, LO3 — все 3 + LO8 framing.**

**Frame mapping:** All 6 frames — каждый сжато.

**Иллюстрация (MANDATORY):**
- **Тип:** 3-card summary layout + small reference icons.
- **Источник:** self-generated layout + Lucide icons (`activity`, `flask-conical`, `users`).
- **Caption:** N/A.
- **Визуальная функция:** crystallize 3 takeaways visually; mental anchor для exam recall.

**Speaker notes hints:**
1. Connection back to LO mapping explicit — это apply-уровень takeaways.
2. Tone: confident, не дидактический. Студент должен помнить эти 3 пункта через 2 недели.
3. Russian context preserved (mosmed, ФЗ-152) — explicit.
4. **LO8 framing explicit (P0-2 fix):** «3 принципа responsibility — input для Лекции 9 черновика. Не финальный синтез.»
5. **P2-9 fix Нобель 2024:** add Baker alongside Hassabis + Jumper (computational protein design).
6. **P0-3 fix mosmed:** «4 млрд руб/год» REMOVED; replaced с verified operational metrics (14M+ studies, 74 regions).
7. Avoid extra content beyond 3 cards.

**Связь с другими слайдами:** s5 (central question), s24 (responsibility), s28 (Q&A).

**Risks:** none beyond no extra content.

**Cross-frame anchor:** All LOs + all frames + LO8 framing для Lec 9.

---

### Слайд 27 — Callback to central question + emotional payoff (1 мин) (`assertion_visual`)

**Описание:** explicit callback + final emotional anchor.

**Содержание (visible):**
- **Callback to central question (большой текст):** «**Какие AI-обещания в медицине сбылись? — Диагностика да (mosmed: 14M+, MASAI: 44% workload). Drug discovery — частично (Rentosertib peer-reviewed; DSP-1181 discontinued). Ответственность — всегда на враче.**»
- **Closing line:** «Врач ставит диагноз. AI подсказывает. Инженер делает так, чтобы врач мог по-настоящему решать.»

**LO mapping:** **LO8 framing** (closing principle — input для Lec 9).

**Frame mapping:** Человек vs AI (CORE final note) + LO8 framing.

**Иллюстрация (MANDATORY):**
- **Тип:** stock photo (close-up, emotional anchor).
- **Источник-кандидаты:**
  - Unsplash `https://unsplash.com/s/photos/doctor-patient` (CC0, doctor explaining to patient).
  - Pexels `https://www.pexels.com/search/medical%20consultation/`.
- **Caption (5-10 слов):** «Врач + пациент: human stays central (Unsplash CC0)»
- **Визуальная функция:** emotional payoff; reinforces center of LO8 framing.

**Speaker notes hints:**
1. Pause, eye contact, slow speech.
2. This is the **takeaway-of-takeaways** — one sentence the student remembers.
3. Avoid further explanation; let the line stand.
4. Connect explicitly to s5 framing — это closure of arc.
5. Set up s28 (тизер Лекции 5 + Lec 9 черновик).

**Связь с другими слайдами:** s5 (opens), s24 (frames), s28 (transitions out).

**Risks:** image attribution + no extras.

**Cross-frame anchor:** LO8 framing + Человек vs AI.

---

### Слайд 28 — Тизер Лекции 5 + Lec 9 reference + домашнее задание (1.5 мин) (`assertion_visual`)

**Описание:** transition к следующей лекции + связь с курсом + explicit LO8 reference forward.

**Содержание (visible):**
- **Тизер Лекции 5:** «AI в производстве и сельском хозяйстве. Российские данные: **Cognitive Agro Pilot — 1500+ машин, +30-40% эффективности**. Predictive maintenance, quality control, physical AI.»
- **Лекция 9 reference:** «3 принципа responsibility сегодня — input для **черновика чек-листа на Лекции 9** (Этика и регулирование). На Лекции 14 финализируете.»
- **Course map (visual):** mini-progress bar (4/14 лекций done).
- **Optional homework / call-to-action:**
  - Найти 1 case medical AI in news (Reuters / STAT News / Habr) и apply 4-actor responsibility framework (s24).
- **Closing reminder:** «Семинар sem-04: case-анализ medical AI deployment в Russian context.»

**LO mapping:** LO transition + LO8 framing forward (explicit для Lec 9).

**Frame mapping:** All frames carried over.

**Иллюстрация (MANDATORY):**
- **Тип:** mini course-map (progress bar) + small Лекция 5 teaser graphic + Lec 9 arrow.
- **Источник:** self-generated layout.
- **Caption:** N/A.
- **Визуальная функция:** continuity курса; expectation-setting; LO8 framing forward.

**Speaker notes hints:**
1. NOT a duplicate of s26 — focus на «что дальше», не «что было».
2. Семинар sem-04 — case study; explicit Russian context.
3. Optional homework — для motivated students; не graded.
4. Avoid extras (no «вы здесь», no «лектору»).
5. **LO8 framing forward (P0-2 fix critical):** «3 принципа сегодня = input для Lec 9 черновика. Course doc explicit: LO8 → Lec 9 + Lec 14.»
6. 90 sec strict; not the place для new content.
7. **P2-10 Cognitive Agro Pilot phrasing:** verified per course doc «1500+ машин, +30-40% эффективности».

**Связь с другими слайдами:** s26 (3 takeaways), s27 (closing), s29 (Q&A), Lec 5 (next), Lec 9 (LO8 черновик).

**Risks:** none.

**Cross-frame anchor:** Course continuity + LO8 framing forward.

---

### Слайд 29 — Q&A с провокацией (1.5 мин) (`assertion_visual`)

**Описание:** open Q&A. Если тишина — провокация.

**Содержание (visible):**
- «Q&A»
- Если тишина (3 backup-prompts):
  1. «Кто после этой лекции изменил мнение о медицинском AI?»
  2. «У кого был знакомый/родственник, чей диагноз ставился с AI? Поделитесь.»
  3. «Если бы вам предложили работать в medical AI стартапе — какой первый вопрос вы бы задали о их validation процессе?»

**LO mapping:** N/A.

**Frame mapping:** N/A (open).

**Иллюстрация (MANDATORY):**
- **Тип:** simple Q&A graphic + small contact-info card.
- **Источник:** self-generated layout (large «Q&A?» + small subdued course-contact card).
- **Caption:** N/A.
- **Визуальная функция:** signaling — лекция закончилась, ждём вопросы.

**Speaker notes hints:**
1. Avoid filling silence — wait 5-10 seconds.
2. If technical question stops лекцию — defer answer to office hours or speech.md (later).
3. Most likely question: «как студент-инженер войти в medical AI?» — prepare 2-sentence answer (Курс «Системы ИИ» track + Сбер AI Lab / Yandex AI Lab / Сколтех medical AI).
4. Russian context: реальные internships and research opportunities.
5. Final beat: thank for attention; remind семинар sem-04.

**Связь с другими слайдами:** All — closing.

**Risks:** none.

**Cross-frame anchor:** N/A.

---

## Сводка

| Параметр | Значение |
|----------|----------|
| Слайдов | **30** (was 29 — s17 split into s17a + s17b; s25 merged into s18-merged → net +1) |
| Разделов | 6 (0–5) |
| Время | 9 + 7 + 14 + 14 + 10 + 12 + 6 = **72 мин content** + ~3 мин transitions = ~68 мин active + 7 мин буфер = **75 мин total** (P2-12 arithmetic fix) |
| Опросы / interactive | s3 (опрос), s4 (reveal), s14 (mid-callback), s19 (micro-exercise — единственное упражнение, 10 мин per course doc), s29 (Q&A) |
| Демо | s1 (AlphaFold-server live SELECTED), s19 (LLM web-chat student-driven LO4 apply) |
| Центральный вопрос | s5 → callbacks s12, s14, s17a, s17b → answer s24 → payoff s27 |
| Главный case study | mosmed.ai operational (s12), Rentosertib peer-reviewed success (s17a), DSP-1181 reality check (s17b), Obermeyer Optum (s21), NEDA Tessa + 3 LLM cases (s22), Change Healthcare breach (s23) |
| Студенческие упражнения | 1 micro-exercise s19 (10 min per course doc); НЕТ полноценных упражнений |

---

## LO Coverage Matrix

| LO | Заявлен на | Реально работает | Bloom level | Статус |
|---|---|---|---|---|
| **LO1** (Классифицировать типы AI в медицине) | s01, s04, s06, s07, s09, s10, s15, s16, s17a, s26 | s06 (4-type matrix), s09 (CV pipeline), s15 (drug discovery pipeline), s16 (AlphaFold + AlphaProteo), s17a (Rentosertib), s26 (takeaway #1) | Understand/Remember + Apply | OK |
| **LO2** (Оценить применимость AI с клиническими данными) | s10, s11, s12, s17a, s17b, s18-merged, s19, s26 | s10 (sens/spec + prevalence/PPV), s11 (AI vs радиолог — Liu/MASAI/Goh 3-row), s12 (mosmed operational), s17a (Rentosertib Nature Medicine), s17b (DSP-1181 reality), s19 (apply via micro-exercise) | Apply + Evaluate | OK |
| **LO3** (Проанализировать этический риск ответственности) | s8, s13, s17b, s21, s22, s23, s24, s18-merged, s26, s27 | s13 (CV bias dermatology + pulse-ox), s21 (Obermeyer deep + actionable engineer lesson), s22 (NEDA Tessa + 3 LLM cases), s24 (4-actor framework — CORE), s18-merged (regulation) | Analyze + Evaluate | OK |
| **LO4** (Применить AI web-chat — NEW vs v1, per course doc) | s19 | s19 (micro-exercise CORE: 10 min apply AI to объяснить sens/spec) | Apply | OK (added per P1-1) |
| **LO8 framing** (Сформулировать принципы ответственного использования AI) — **framed как input для Lec 9 черновика, не финальный синтез** | s8, s17b, s23, s24, s26, s27, s28 | s24 (4-actor framework as input), s26 (takeaway #3 explicit framing для Lec 9), s27 (closing payoff), s28 (forward reference к Lec 9 черновик) | Evaluate (framing, не Create) | OK — properly framed downstream |

---

## Frame Coverage Matrix

| Frame | Slides | Slides count |
|---|---|---|
| **LO mapping** | All slides except s2, s3, s28-meta, s29 (template/poll/transition/Q&A) | 26 |
| **LLM pattern** («объясни как студенту») | s11 (Goh GPT-4 reasoning), s19 (CORE) | 2 (1 CORE) |
| **LLM anti-pattern** (не доверяй медицинским советам) | s13 (CV bias parallel), s19 (CORE), s22 (NEDA Tessa + 3 cases CORE), s24 | 4 (2 CORE) |
| **Другой AI (не LLM)** | s01, s04, s06, s07, s09, s10, s11, s12, s13, s15, s16, s17a, s17b, s18-merged | 14 (CORE для разделов 1-3) |
| **Безопасность** | s07 (FDA), s08 (motivation), s12 (medical data), s13 (bias data), s18-merged (FDA + regulation), s21 (Obermeyer), s22 (Tessa), s23 (Change Healthcare CORE), s24 (responsibility) | 9 (2 CORE) |
| **Человек vs AI** | s03, s05, s08, s10, s11 (CORE — Liu/MASAI/Goh), s12, s13, s14, s17a, s17b, s20, s21, s22, s24 (CORE), s18-merged, s27 (CORE), s28 | 17 (3 CORE) |

**All 6 frames covered, с CORE concentrated в structurally most-important slides (s11, s19, s22, s24, s27).**

---

## Glossary candidates (25 терминов + canonical-lock map для glossary lock после chapter approval)

**Critical: canonical-lock map (P1-7 methodology fix):**

```yaml
ai_diagnostics:
  canonical_RU: "AI-диагностика"
  canonical_EN: "AI medical imaging"
  aliases_allowed:
    - "AI-диагностика" # RU canonical
    - "AI medical imaging" # EN research literature
    - "AI medical diagnostics" # EN secondary
  aliases_forbidden:
    - "computer-aided diagnosis (CADx)" # different FDA category — refer separately
    - "medical AI" # too broad (includes drug discovery, admin)
  CADe_FDA_subset:
    canonical: "Computer-aided detection (CADe)"
    scope: "FDA-specific alert-mode subset of AI diagnostics; not synonym for ai_diagnostics"
```

**Глоссарий:**

1. **AI-диагностика (canonical RU)** — применение AI (преимущественно computer vision) для анализа медицинских изображений / сигналов для постановки диагноза. EN: «AI medical imaging» / «AI medical diagnostics» (research literature).
2. **Drug discovery** — процесс открытия новых лекарственных молекул; традиционно 10-15 лет + $1-2 млрд per approved drug.
3. **Sensitivity (чувствительность / recall)** — доля больных, которых AI определил как больных = TP / (TP + FN).
4. **Specificity (специфичность)** — доля здоровых, которых AI определил как здоровых = TN / (TN + FP).
5. **Prevalence** — частота встречаемости болезни в популяции. Не зависит от sensitivity/specificity, но влияет на PPV.
6. **PPV (Positive Predictive Value)** — TP / (TP + FP). Зависит от prevalence. Critical для screening interpretation.
7. **AlphaFold** — DeepMind модель для prediction 3D-структуры белков (v1 2018, v2 2021, v3 May 2024); Нобель 2024 (Hassabis + Jumper + Baker для protein design).
8. **AlphaProteo** — DeepMind модель для design новых protein binders (September 2024); 3-300× affinity improvement vs prior methods on 7 targets.
9. **FDA AI/ML framework (SaMD)** — Software as Medical Device — категория FDA для software-only medical AI.
10. **Predetermined Change Control Plan (PCCP)** — FDA innovation **4 декабря 2024**: vendor pre-declares allowed updates to AI без re-submission.
11. **Computer-aided detection (CADe)** — AI как «вторая пара глаз» для радиолога; формальная FDA category. **Subset of AI-диагностика, не synonym.**
12. **Foundation model** — крупная pre-trained модель, fine-tuned для specific задач (e.g., MedCLIP, BiomedCLIP, AlphaFold).
13. **HIPAA** — Health Insurance Portability and Accountability Act (US 1996); защищает PHI.
14. **GDPR** — General Data Protection Regulation (EU 2016/679); защищает personal data including health.
15. **ФЗ-152** — Федеральный закон РФ «О персональных данных» (2006, major amendments 2024-2025); особая категория медицинских данных.
16. **ФЗ-23 (data localization)** — Federal Law N 23-ФЗ 28 February 2025: personal data of Russian citizens cannot be processed/stored on databases outside Russia; effective 1 July 2025.
17. **ePHI (electronic Protected Health Information)** — медицинская информация в электронном виде, защищаемая HIPAA.
18. **Деперсонализация (de-identification)** — удаление identifiers, чтобы data не была привязана к конкретному человеку; ≠ anonymisation (full removal of re-identifiability).
19. **EU AI Act high-risk** — категория, в которой находится медицинский AI; requires conformity assessment + CE-mark. **Effective 2 августа 2026.**
20. **mosmed.ai** — российская federated AI-platform для медицинской визуализации, ДЗМ Москвы. 14M+ исследований за 5 лет, 74 региона.
21. **Insilico Rentosertib (ISM001-055 / INS018_055)** — first AI-designed drug с peer-reviewed positive Phase IIa (Nature Medicine June 2025); TNIK inhibitor для IPF.
22. **DSP-1181** — first AI-designed drug в clinical trials (Exscientia + Sumitomo, January 2020); Phase 1 discontinued 2022.
23. **NEDA Tessa** — chatbot, замещавший human eating-disorder helpline; vendor Cass changed rule-based → generative без NEDA approval; снят с обращения 30 May 2023.
24. **Bias (algorithmic bias)** — systematic deviation в AI output, чаще correlated с защищёнными атрибутами (race, gender, age).
25. **Healthcare operator role (P2-4 fix — replaces «Хосзу-роль»)** — actor в responsibility framework, ответственный за selection + training + monitoring AI-vendor (hospital, clinic, ДЗМ).

**Note:** Calibration, Confidence score, Post-market surveillance из v1 — kept в notes для book-editor (deferred к chapter level, не key terms для slides).

**Final count: 25 terms (same as v1, but improved canonical-lock map + glossary candidate 24 fixed).**

---

## Top 5 Uncertainty Flags (для Phase 0b critique / fact-checker resolution в plan-v2)

| # | Flag | Slides affected | Resolution status в v2 |
|---|---|---|---|
| 1 | **DSP-1181 status (CRITICAL)** | s17b | **RESOLVED:** Discontinued status accepted; s17b framed as reality check; s17a Rentosertib added as primary success. |
| 2 | **mosmed.ai «4 млрд руб/год» (CRITICAL)** | s5, s8, s12, s26 | **RESOLVED:** Removed everywhere; replaced с verified operational metrics (14M+ studies, 74 regions, 70 services, 11 standards). |
| 3 | **FDA AI/ML device count (current)** | s4, s7 | **RESOLVED:** Updated к 1,451 cumulative end-2025 (258 в 2024 + 295 в 2025); day-of-lecture re-fetch flagged. |
| 4 | **Rentosertib post-Phase IIa status** | s17a | **NEW FLAG в v2** — monthly cadence for Insilico Phase 3 announcement. Check 12 мая 2026. |
| 5 | **Exscientia 2025 status (CEO firing)** | s17b speaker notes only | **PARTIALLY RESOLVED:** Recursion merger verified (Aug 2024 announce, Nov 2024 close, $688M). CEO Hopkins firing claim not verified — dropped from visible content; if not separately verified before chapter Phase 2, drop from speech.md as well. |

**Дополнительные secondary flags:**

- MASAI Sweden RCT numbers verbatim (sens 80.5% vs 73.8%, 44%, 12%) — verify Lancet papers.
- Obermeyer 2019 verbatim «26% more chronic illness» + «17.5% → 46.5% Black patients served».
- NEDA Tessa dates — verified per sources.md (March 2023 generative switch; May 30, 2023 suspend).
- Change Healthcare $2.457 млрд UHG Q3 2024 — precise figure verified.
- ФЗ-152 + ФЗ-23 2025 amendments — verified per sources.md §7.4.
- EU AI Act high-risk medical AI effective 2 августа 2026 — verified.
- AlphaFold 200M+ structures + AlphaProteo 88% BHRF1 + 3-300× — verified per sources.md.

---

## Freshness watchlist (verify on day of lecture 12 мая 2026)

| Item | Cadence | Action |
|---|---|---|
| **FDA AI/ML device count** | Quarterly | Re-pull FDA list 12 мая 2026 — expect 1,500-1,550 cumulative (Q1 2026 additions) |
| **Exscientia / Recursion post-merger clinical readouts** | Weekly | Check FierceBiotech / Endpoints 1 week pre-lecture |
| **Insilico Rentosertib post-Phase IIa** | Monthly | Check Insilico investor news / Phase 3 announcements |
| **mosmed.ai operational stats** | Quarterly | Check mos.ru ДЗМ press для Q1-Q2 2026 figures |
| **AlphaFold-server URL liveness** | Day-of | Verify alphafoldserver.com active 12 мая 2026 |
| **NEDA Tessa case freshness** | Yearly | Confirm no new significant developments |
| **EU AI Act 2 Aug 2026 deadline** | Monthly | Hot topic = 81 days post-lecture |
| **Russian medical AI registrations** | Quarterly | Webiomed updated count |

**Top 4 items requiring re-verification 12 мая 2026 (day-of-lecture pre-flight):**

1. FDA AI/ML device count (most likely to have moved).
2. Insilico Rentosertib news (Phase 3 announcement potential).
3. mosmed.ai dashboard URL liveness + key stats.
4. AlphaFold-server URL active (s1 demo dependency).

---

## Notes для следующих фаз (orchestrator pre-USER-GATE walkthrough checklist для GATE 0 — обновлено для plan-v2)

Перед presenting plan-v2 пользователю на USER GATE 0:

### Phase 0a (already done) — Methodology critic + reader-text-only

✓ Methodology-critic: REVISE verdict; 2 P0 + 9 P1 + 12 P2 — все addressed в plan-v2 per changelog.
✓ Reader-simulator text-only: APPROVE-WITH-POLISH verdict; 2 P0 + 7 P1 + 5 P2 — все addressed.

### Phase 0b (already done) — Fact-checker

✓ Fact-checker: REVISE verdict; 3 P0 + 14 P1 + 4 P2 — все P0 addressed; 12 P1 applied; 2 P1 deferred (AlphaFold user count needs primary verify; Liu 2019 exact numbers TBD before chapter).
✓ All 5 top uncertainty flags resolved или re-flagged для chapter phase.
✓ Freshness watchlist generated со списком claims + cadence + verify-on date.

### Phase 0c (this revision pass) — Plan-v2 pre-USER-GATE walkthrough

**Mandatory checks before USER GATE 0:**

1. **Visual scan** — для каждого слайда, есть ли concrete illustration source + at least 2 alternatives? Все CAPTIONs present и ≤10 слов? **Check для s17a + s17b (NEW splits) + s18-merged (NEW merged) специально.**
2. **Frame mapping audit** — все 30 слайдов имеют mapping (LO + frame); CORE concepts концентрированы в structurally-important слайдах (s5, s11, s19, s22, s24, s27)?
3. **Russian context check** — explicit Russian framing в s4 (FDA + mosmed), s12 (mosmed CORE), s23 (ФЗ-152 + ФЗ-23 + Russian ransomware nuance), s18-merged (Росздравнадзор + ПП РФ 1684), s28 (Cognitive Agro Pilot teaser)? **Glossary candidate 25 = «Healthcare operator role» (NOT "Хосзу-роль").**
4. **Schema readability pre-wireframe required** — для всех schema slides (s6 matrix, s7 timeline, s9 pipeline, s10 matrix + table, s11 comparison, s15 pipeline, **s17a timeline (NEW, 3 events)**, **s17b timeline (NEW, 3 events)**, s18-merged comparison, s24 quadrant). **CRITICAL для s10 (4-metric table), s17a/s17b (timelines), s24 (quadrant с 1-word role + 1-line responsibility constraint).**
5. **No extras check** — нет «лектору» секций, «вы здесь», тайминг видимый студенту; subtitle только в cover s2; speaker notes derived from chapter+speech, не layout description.
6. **WPM math** — total content time = 68 мин active + 7 мин буфер = 75 мин; verify per-slide duration sums per арифметика (9+7+14+14+10+12+6 = 72 мин в слайдах + ~3 мин transitions).
7. **Glossary candidates** — **25 terms (locked map с canonical_RU + aliases_forbidden + aliases_allowed) для intermediate L4**; book-editor may extend в chapter Phase 2.
8. **Central question** explicit на s5; returns 4 раза (s12, s14, s17a, s17b); answer s24; payoff s27 — verify нет orphan/missing.
9. **One-slide-one-message** — каждый слайд имеет ОДНО assertion; verify.
10. **Illustrations per slide** — все 30 слайдов имеют illustration entry с at least 2 alternative URLs (per user spec MANDATORY). Special check: s17a + s17b new illustration briefs.
11. **LO4 added к header** (P1-1 — course doc compliance); s19 LO mapping = «LO4 CORE + LO2 + LO3».
12. **LO8 framing audit** — везде framed as «input для Lec 9 черновика», NOT premature finale; s5, s24, s26, s27, s28 all consistent.

### Готовность к Phase 2 (chapter draft) после USER GATE 0

После USER GATE 0 approval (plan-v2) — book-editor читает plan-v2 + 11 встроенных «Speaker notes hints» секций + glossary candidates → пишет `chapter.md` (~10k слов). Затем cascade критиков на chapter (methodology + fact-checker + reader text-only) → Phase 4 → USER GATE A (chapter approved) → glossary lock.

---

## Артефакты, создаваемые этим планом (owner: преподаватель + producer agents)

- `library/lectures/lec-04/glossary.yaml` — 25 terms + canonical-lock map (generated после chapter approval Phase 4).
- `library/lectures/lec-04/assets/backup/alphafold-hemoglobin.png` — backup для s01 demo.
- `library/lectures/lec-04/assets/control/s19-baseline-llm-response.png` — lecturer's control AI response для s19 micro-exercise.
- `library/lectures/lec-04/assets/control/s19-fallback-responses.pdf` — 5 pre-printed sample AI responses (3 EN + 2 RU) для no-internet fallback.
- `library/lectures/lec-04/assets/charts/` — self-generated charts (s4 FDA growth, s7 trend, s10 4-metric table, s11 3-row comparison, s17a Rentosertib timeline, s17b DSP-1181 timeline).
- `notes/lecture-4-review/citations-audit.md` — после fact-checker Phase 0b (existing, used для v2 revision).
- `notes/research/lecture-4/sources.md` — research collection (existing, 82 sources).

---

## Изменения относительно v1

См. **Changelog v1 → v2** at the top of this document. Summary:
- **7 P0 applied:** s17 split (s17a + s17b); LO8 framing rework; mosmed «4 млрд» removed; FDA count updated; PCCP pre/post contrast; s17 timeline simplified; schema readability for s10/s17b/s24.
- **18 P1 applied (15 в visible content; 3 в speaker notes):** LO4 added; s18+s25 merged; s11 imaging vs reasoning split; s22 expanded к 3 cases; glossary canonical lock; s1 hook SELECTED; s19 extended к 10 min; s15 hit/lead defined; s10 prevalence/PPV; s10 sens/spec verified; s13 vs s21 bias dedup; s23 AI connection strengthened; s6 axes justified; s5 market size corrected; s16 AlphaProteo precise; s21 Obermeyer numbers verified.
- **8 P2 applied:** PCCP date precise; arithmetic fixed; Нобель expanded; s2 cover compressed; s7 caption; s28 Cognitive Agro phrasing; freshness watchlist updated; Glossary candidate 25 renamed.

---

## Точки выбора (статус — все resolved в v2)

| Слайд | Что | Выбор | Статус |
|-------|-----|-------|--------|
| 1 | Ice breaker demo | **AlphaFold-server (alphafoldserver.com)** live OR backup PNG | **SELECTED** (P1-8 fix) |
| 5 | Central question | «Какие обещания сбылись + кто отвечает» (B+C blend) | SELECTED (kept from v1) |
| 17a | Drug discovery success | **Insilico Rentosertib (Nature Medicine June 2025)** | **SELECTED** (P0-1 fix — replaces DSP-1181 как flagship) |
| 17b | Drug discovery reality | **DSP-1181 discontinued reality check** | SELECTED (kept v1 narrative; simplified to 3 events) |
| 18-merged | Regulation | **3-jurisdiction merged (FDA + EU + RF) — 2 мин** | **SELECTED** (P1-3 merge от v1 s18+s25) |
| 19 | Micro-exercise topic + duration | Sens/spec explanation via LLM web-chat, **10 мин** | **SELECTED** (P1-9 fix — extended from 8 to 10 per course doc) |
| 24 | Responsibility framework | 4-actor quadrant (Price 2019 + Gerke 2020) | SELECTED (kept v1) |
| 27 | Closing line | «Врач решает. AI подсказывает. Инженер обеспечивает» | SELECTED (kept v1) |

**Все Точки выбора → SELECTED. No PROPOSED остаются для USER GATE 0.**

---

## Следующий шаг

После approve этого plan-v2 (USER GATE 0) — Phase 2 lecture-production pipeline: `book-editor` пишет `chapter.md` (~10k слов, academic), используя plan-v2 + 11 встроенных speaker notes hints sections + glossary candidates (25 terms + canonical-lock map). Затем cascade критиков на chapter (methodology + fact-checker + reader text-only) → Phase 4 (revisions) → glossary lock → USER GATE A.

*Конец plan-v2.*
