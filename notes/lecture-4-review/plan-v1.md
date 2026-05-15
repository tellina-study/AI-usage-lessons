# Лекция 4: AI в медицине и фармацевтике
## План слайдов v1.0

**Issue:** #73 (Phase 1 of EPIC for Лекции 4)
**Branch:** `issue-73-lec-04-medicine-production`
**Длительность:** 75 минут (≈68 мин контента + 7 мин буфер ≈ 10%)
**Аудитория:** студенты-инженеры (универсальная, 3 курс, технический вуз, **не медики**)
**LO:** LO1, LO2, LO3, **LO8** (новизна vs Лекции 1)
**Формат:** публичная лекция; один слайд — одна мысль; БЕЗ студенческих упражнений (кроме **одного** микро-упражнения с AI web-chat на s19)
**Дата актуализации:** 2026-05-13
**Curriculum level:** **intermediate** (4-я лекция курса — после Лекций 1-3 introductory; студенты уже знают «model/chat/agent/app» классификацию и чек-лист «где AI работает»; теперь применяем к индустрии).
**Versus Лекции 1 v5:** добавлен LO8 (responsibility principles); industrial case (не AGI-спекуляции); mandatory real-world illustration per slide; центральный вопрос смещён на «ответственное использование» vs «где работает».
**Source-of-truth:** глава курса в `catalog/exports/docs/ai-v-raznyh-industriyah.md` (строка Лекции 4) + course-narrative + `stats-overview.md`.

---

## Центральный вопрос лекции

> **Какие AI-обещания в медицине реально сбылись к 2026 году — и кто отвечает, когда AI-диагноз оказывается ошибочным?**

**Обоснование выбора (B+C из кандидатов):**

1. **Задаётся в s05** (рамка после ice-breaker + опроса + reveal): «Drug discovery обещали 10× ускорение; AI-диагностика обещала уровень рентгенолога. Что из этого сбылось к 2026 году, а где остались только маркетинговые заявления? И когда AI ошибается — кто несёт ответственность?»
2. **Возвращается в s14 (mosmed.ai concrete case)** — здесь AI-диагностика **сбылась** (4 млрд руб/год экономии).
3. **Возвращается в s17 (DSP-1181 reality check)** — здесь обещание было **частично или не сбылось** (depending on fact-check); ценный нарратив маркетинга vs реальности.
4. **Ответ получает в s24-s25** (ответственность + регулирование).
5. **Эмоциональный payoff в s27**: «Врач ставит диагноз. AI подсказывает. Ответственность — на враче. Инженер строит AI так, чтобы эта ответственность была технически выполнима.»

**Tone:** trust-but-verify; не евангелизм AI, не диссидентство. Лекция не про «AI спасёт медицину», а про «какое именно AI работает, под чьей ответственностью, и как инженер на это влияет».

**Почему не «где работает / где не работает»** (как в Лекции 1)? — этот фрейм для introductory. Лекция 4 — intermediate; центральный вопрос углубляется до «реализация vs обещание + ответственность», что напрямую mapping на LO8 (новизна Л4 vs Л1).

---

## Арка лекции

| Этап | Слайды | Время | Функция |
|------|--------|-------|---------|
| 0. Открытие + central question | 1–5 | 9 мин | hook (mosmed.ai live demo OR AlphaFold-server query); титул; опрос; central question framing |
| 1. Карта AI в медицине | 6–8 | 7 мин | 4 типа применения (диагностика / drug discovery / personalized / admin); масштаб (FDA-authorized count); зачем медицина — instructive case |
| 2. AI-диагностика как зеркало (computer vision) | 9–13 | 14 мин | radiology CV; mosmed.ai РФ case; sensitivity vs specificity (mat-применение); AI-vs-radiologist studies; что значит «AI лучше» |
| 3. Drug discovery: обещания vs реальность | 14–18 | 14 мин | AlphaFold 3 / AlphaProteo; DSP-1181 reality check; Insilico ISM001-055; FDA AI/ML framework |
| 4. Микро-упражнение AI | 19 | 8 мин | LLM pattern (объясни как студенту) + anti-pattern (не доверяй без верификации) |
| 5. Границы + этика + ответственность | 20–25 | 14 мин | bias (Obermeyer 2019); NEDA Tessa scandal; Change Healthcare breach; ответственность; регулирование |
| 6. Заключение | 26–29 | 6 мин | 3 вывода (LO8); тизер Лекции 5; Q&A |
| Буфер | — | 7 мин | вопросы, демо, технические задержки |

**Итого:** 29 слайдов, ~68 мин контента + 7 мин буфер = 75 мин.

---

## Раздел 0. Открытие и вовлечение (9 мин)

### Слайд 1 — Ice breaker: live-демо mosmed.ai dashboard tour ИЛИ AlphaFold-server query (3 мин) (`live_demo`)

**Описание:** ноутбук + проектор; либо (A) live tour интерфейса mosmed.ai (если доступен публичный URL — `mosmed.ai`), либо (B) live AlphaFold-server query на DeepMind alphafoldserver.com — запрос структуры белка с фронта зала, появление 3D-структуры через ~30-60 сек.

**Содержание (visible):** title-screen демо + assertion внизу. Assertion: «AI ставит метку патологии на рентгене за ~3 секунды. AI разворачивает 3D-структуру белка за ~30 секунд. Обе системы — production-ready в 2026.»

**LO mapping:** **LO1** (типы AI в медицине — CV для диагностики, ML для drug discovery).

**Frame mapping:** Другой AI (не LLM) — это computer vision (mosmed) + ML+protein-folding (AlphaFold). **Демонстрирует:** medical AI ≠ ChatGPT для врачей.

**Иллюстрация (MANDATORY):**
- **Тип:** live demo + backup screenshot.
- **Источник-кандидаты:**
  - **A (preferred):** `https://mosmed.ai/` — public dashboard tour, скрин одного из CV-результатов на рентгене грудной клетки.
  - **B (fallback):** `https://alphafoldserver.com/` — input query «predict structure of hemoglobin» + 3D output.
  - **Backup PNG (если internet недоступен):** скриншот mosmed.ai dashboard в `library/lectures/lec-04/assets/backup/`.
- **Caption (5-10 слов):** «mosmed.ai — анализ КТ/МРТ в 80+ клиниках Москвы (источник: mosmed.ai, 2026)»
- **Визуальная функция:** emotional anchor («это работает прямо сейчас, на этих скриншотах»). Создаёт engagement через визуальную конкретику.

**Speaker notes hints:**
1. Backup — 2 screenshot + 30-сек видео, если internet/проектор подведут.
2. Связать с лекцией 1 («помните камера-демо? — это был YOLO для людей; сегодня тот же CV-стек на рентгене для патологий»).
3. Подчеркнуть: AI here is narrow CV, NOT LLM.
4. Заранее проверить, что demo URLs живы накануне лекции (freshness-check).
5. Не входить в техническую глубину — это hook, 3 мин total.

**Связь с другими слайдами:** setup для s09-s13 (диагностика block) + s15-s17 (drug discovery block).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` mosmed.ai active URL + клиник count + AlphaFold-server public access (был ли изменён access policy).

**Cross-frame anchor:** Другой AI (не LLM) + LO1.

---

### Слайд 2 — Титульный слайд курса (0.5 мин) (`cover`)

**Описание:** шаблонный слайд курса.

**Содержание (visible):** название курса; «Лекция 4. AI в медицине и фармацевтике»; длительность 75 мин; дата; преподаватель; вуз/факультет.

**LO mapping:** N/A (template).

**Frame mapping:** N/A.

**Иллюстрация:**
- **Тип:** decorative cover motif (large lecture-number outline 200pt + hero-motif из Ocean palette).
- **Источник:** template из `templates/lecture-title-slide.md` + лекционная цветовая палитра (Ocean Gradient).
- **Caption:** N/A.
- **Визуальная функция:** continuity курса (одинаковый cover для всех 17 лекций).

**Speaker notes hints:** шаблон, без комментариев.

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

**Frame mapping:** Человек vs AI (вопрос 3 — пинг на финальную ноту).

**Иллюстрация:**
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
- **FDA AI/ML-enabled medical devices: 1016 одобренных к августу 2024 (FDA, обновляется ~quarterly).** `[FACT-CHECK: latest count]` — на дату лекции 2026 будет ~1200-1400 (linear extrapolation, проверить FDA-list).
- График (bar chart): рост FDA-одобренных AI-devices 2015→2025 (от ~10 к 1000+, exponential curve).
- **Россия:** mosmed.ai обработал >12 млн изображений с 2020 года (источник: mosmed.ai annual report 2024-2025). `[FACT-CHECK]`.
- **Инсайт:** «AI в медицине — уже не «будущее», а production-инфраструктура. Но как мы поймём дальше, "production" ≠ "решены все проблемы".»

**LO mapping:** **LO1** (масштаб AI в медицине).

**Frame mapping:** Другой AI (не LLM) — это CV/ML-devices, не chatbot.

**Иллюстрация (MANDATORY):**
- **Тип:** data chart (self-generated via QuickChart) + 1 supporting screenshot.
- **Источник-кандидаты:**
  - **Bar chart data:** FDA AI/ML-enabled medical devices list — `https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices` (official FDA list, sortable).
  - **Alt:** Sezgin et al., NEJM AI 2024 figure про AI device approvals trend.
  - **РФ supporting:** screenshot mosmed.ai dashboard статистики (URL mosmed.ai).
- **Caption (5-10 слов):** «FDA, AI/ML medical devices list (август 2024 + проекция); mosmed.ai annual report»
- **Визуальная функция:** evidence для scale claim; устанавливает «AI в медицине — индустриальная инфраструктура».

**Speaker notes hints:**
1. Не входить в каталог device-types (next slide).
2. Подчеркнуть: FDA list — public + regularly updated, любой инженер может проверить status конкретного device.
3. Russian context — mosmed.ai первый в РФ federated AI-medical platform.
4. Avoid hype tone: «1000 devices» ≠ «1000 working in clinic» — many are research / niche.
5. Disclaimer: проекция на 2026 — линейная extrapolation, не official.

**Связь с другими слайдами:** s3 (reveal), s7 (карта типов AI), s12-13 (диагностика deep dive).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` FDA AI/ML devices count на дату лекции; `[FACT-CHECK]` mosmed.ai cumulative images processed; freshness — quarterly cadence для FDA list.

**Cross-frame anchor:** LO1 + Другой AI (не LLM).

---

### Слайд 5 — Рамка лекции + центральный вопрос (2 мин) (`assertion_visual`)

**Содержание (visible):**
- **Стейкс:** «AI в медицине — индустрия $50+ млрд в 2025 (Statista) с >$100 млрд прогнозом к 2030. В то же время — рост incident reports о AI-bias и ошибках.» `[FACT-CHECK]`
- **Рамка курса (callback к Лекции 1):** «На Лекции 1 мы спрашивали "где AI работает, где — нет". Сегодня углубляемся: даже там, где AI работает, остаются вопросы ответственности.»
- **Центральный вопрос (крупно):** «**Какие AI-обещания в медицине реально сбылись к 2026 году — и кто отвечает, когда AI-диагноз ошибочен?**»
- **Roadmap (4-point):** Карта AI в медицине → AI-диагностика → Drug discovery → Этика + ответственность.

**LO mapping:** **LO1** + framing для LO2, LO3, **LO8**.

**Frame mapping:** Человек vs AI (ответственность) + Другой AI (medical AI ≠ LLM).

**Иллюстрация (MANDATORY):**
- **Тип:** stock photo + small infographic overlay.
- **Источник-кандидаты:**
  - Unsplash `https://unsplash.com/s/photos/doctor-x-ray` (CC0, врач смотрит на рентген или КТ-скан с AI-overlay), free.
  - Pexels `https://www.pexels.com/search/medical%20ai/` (free).
  - **Wikimedia Commons CC-BY:** «AI medical imaging» categories.
- **Caption (5-10 слов):** «Врач + AI-диагностика — типичный workflow 2026 (Unsplash, CC0)»
- **Визуальная функция:** создаёт emotional anchor («медицина — это про людей, не про код»); прайминг к LO8 (responsibility).

**Speaker notes hints:**
1. Не списком — рамка, central question — крупно.
2. Callback к Лекции 1 (chek-list 4 вопросов) — поверь, что аудитория помнит. Если не помнит — кратко 10 сек напомнить.
3. Не обещать «все ответы сегодня» — мы откроем ответственность как открытый вопрос, не закроем.
4. LO8 introduction — first encounter в курсе («ответственное использование AI» — здесь explicit framing).
5. Roadmap: студент видит 4-point arc, можно референсить далее.

**Связь с другими слайдами:** возврат к central question в s14 (mosmed concrete), s17 (DSP reality), ответ в s24-25 (ответственность), payoff в s27.

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` AI medical market size (Statista); `[FACT-CHECK]` freshness; ensure stock image attribution clean.

**Cross-frame anchor:** LO1 + framing LO8 + Человек vs AI.

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
    - **Text/Molecule + Population:** Drug discovery (AlphaFold, Exscientia, Insilico) + epidemiology.
- Caption: «Один курс — не одна индустрия. Сегодня фокус: левая колонка + drug discovery (правая нижняя).»

**LO mapping:** **LO1** (классификация типов).

**Frame mapping:** Другой AI (CV, ML, signal processing, foundation models — все не-LLM по сути).

**Иллюстрация (MANDATORY):**
- **Тип:** schematic matrix (PowerPoint shapes) + 4 logo icons по углам.
- **Источник-кандидаты:**
  - **Icon set:** Lucide icons (`scan`, `heart-pulse`, `pill`, `flask-conical`) recolored to Ocean palette.
  - **Alt for real products:** small logos через LobeHub icons CDN — IBM Watson Health, mosmed.ai, DeepMind, Insilico Medicine.
- **Caption (5-10 слов):** «4 типа AI-применений; иконки Lucide + LobeHub»
- **Визуальная функция:** mental model schema (карта, к которой студент возвращается); pre-frames detailed deep-dives дальше.

**Speaker notes hints:**
1. Matrix subtype rules (Schema Readability Checklist): axis labels INSIDE quadrants; «больше →» arrows; max 2 строки текста в ячейке; font ≥14pt cells.
2. Лекция фокусируется на верхней-левой (диагностика) + нижней-правой (drug discovery) — это explicit.
3. Personalized medicine + admin AI — крайне briefly или skip; не в фокусе.
4. Назвать каждый тип СВОИМ собственным — не «AI», а «AI-диагностика», «drug discovery AI» и т.д.
5. Mental model: эта matrix должна стать «компасом» в лекции — студент возвращается визуально к ней при упоминании каждого типа.

**Связь с другими слайдами:** карта, к которой возвращаемся в s9 (диагностика deep-dive), s15 (drug discovery deep-dive).

**Risks / things to verify в Phase 0b:** Schema readability check; orchestrator pre-wireframe approval (matrix subtype).

**Cross-frame anchor:** LO1 + Другой AI.

---

### Слайд 7 — Масштаб FDA-одобренных AI-medical devices: динамика 2015→2025 (2 мин) (`assertion_visual` + schema subtype: `timeline`)

**Описание:** timeline / chart — рост FDA-authorized AI/ML medical devices.

**Содержание (visible):**
- **Assertion:** «За 10 лет — от 6 до >1000 AI-devices в FDA-list. Это не "будущее", это инфраструктура.»
- **Bar chart с timeline overlay:**
  - 2015: ~6 devices
  - 2018: ~14
  - 2020: ~64
  - 2022: ~521
  - 2024 (август): 1016 `[FACT-CHECK: latest count]`
  - 2026 проекция: ~1300-1500
- Source: FDA AI/ML-enabled Medical Devices List (FDA.gov).
- Caption: «76% — рентгенология (CV-based); 11% — кардиология (signal AI); остальное — мелкие niches.»

**LO mapping:** **LO1** (scope of AI medical adoption).

**Frame mapping:** Другой AI (не LLM) + Безопасность (FDA — regulator role).

**Иллюстрация (MANDATORY):**
- **Тип:** data chart (self-generated, QuickChart API: `https://quickchart.io/chart`).
- **Источник-кандидаты:**
  - **Data:** FDA AI/ML-Enabled Medical Devices list `https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices` (sortable by year).
  - **Supplementary visualization:** Joshi & Sezgin (2024) NEJM AI paper figure (если openable + license OK).
- **Caption (5-10 слов):** «FDA AI/ML-enabled Medical Devices list, август 2024»
- **Визуальная функция:** quantitative evidence для assertion; устанавливает «exponential growth».

**Speaker notes hints:**
1. Timeline subtype rules: events single-line; year labels не пересекают band borders; pivot point (2022 ChatGPT-effect spike) ≥2× размер.
2. Подчеркнуть: 76% — radiology (CV). LLMs в medicine FDA-approved — почти 0 на 2026 (отдельная тема).
3. Disclaimer: FDA — не EU/Russia; разные jurisdictions имеют разные approval pathways.
4. Connection: this dataset = primary source для всей лекции про «AI в медицине».
5. Не зависимости — не зачитывать все числа; ключевой message — exponential.

**Связь с другими слайдами:** s4 (reveal data), s9-13 (диагностика deep), s23 (FDA framework).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` FDA latest count + breakdown by category (radiology 76% — нужна свежая статистика); freshness — quarterly cadence.

**Cross-frame anchor:** LO1 + Безопасность.

---

### Слайд 8 — Зачем медицина — инструктивный case для инженера (2.5 мин) (`assertion_visual`)

**Описание:** мост — почему медицина значима для инженера-не-медика.

**Содержание (visible):**
- **Assertion:** «Медицина — самый яркий пример того, как технологические выборы инженера превращаются в социальные последствия.»
- **3 reasons (icon-cards):**
  1. **Высокие ставки** — ошибка модели = ошибка диагноза = вред пациенту.
  2. **Строгое регулирование** — FDA, EU AI Act (high-risk), Росздравнадзор — здесь инженер встречает реальную нормативку.
  3. **Прозрачная экономика** — mosmed.ai 4 млрд руб/год = directly measurable ROI (в отличие от «увеличение продуктивности» в офисе).
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
2. mosmed 4 млрд — explicit (callback к s4 + setup для s12).
3. EU AI Act Annex III: medical AI = high-risk category — это formal regulatory designation, не маркетинговое слово.
4. Avoid moralizing; tone = pragmatic engineer.
5. Setup для disclaimer о ответственности на s24.

**Связь с другими слайдами:** s12 (mosmed), s23 (regulation deep), s25 (responsibility).

**Risks / things to verify в Phase 0b:** EU AI Act Annex III — verify medical AI explicit listing as high-risk; check effective date (2024-2026 staggered rollout).

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
- Caption: «Это не LLM. Это CV-pipeline, ~2015-2020 архитектура с medical fine-tuning.»

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
5. Bridge to s10: «теперь видим как; на s10 — что значит «правильно»».

**Связь с другими слайдами:** Лекция 1 s07 (transformers history), s10 (sens/spec — следующий слайд), s12 (mosmed).

**Risks / things to verify в Phase 0b:** Stanford ML Group license для CheXNet figure; SOTA models 2026 freshness.

**Cross-frame anchor:** LO1 + Другой AI.

---

### Слайд 10 — Метрики: sensitivity vs specificity (3 мин) (`assertion_visual` + schema subtype: `matrix_2x2`)

**Описание:** confusion matrix как 2×2 schema + объяснение sens/spec для медицинского контекста. Студенты применяют мат-подготовку (probability + Bayes).

**Содержание (visible):**
- **Assertion:** «Для медицинского AI «accuracy» — недостаточная метрика. Нужны sensitivity (поймать всё) и specificity (не пугать здоровых).»
- **2×2 confusion matrix:**
  - Rows: **Truth: sick / healthy**
  - Cols: **AI prediction: positive / negative**
  - 4 ячейки: TP, FN, FP, TN с цветовыми маркерами (TP/TN — зелёный; FN — red bold = опасная ошибка для здравоохранения; FP — yellow).
- **Formulas (bottom):**
  - Sensitivity (recall) = TP / (TP + FN) — «доля больных, которых AI поймал»
  - Specificity = TN / (TN + FP) — «доля здоровых, которых AI не напугал»
- **Real numbers:** для mosmed.ai CV-моделей: sensitivity 0.94, specificity 0.89 (для COVID screening, 2020-2022). `[FACT-CHECK]`

**LO mapping:** **LO1** + **LO2** (применение мат-инструментов для оценки).

**Frame mapping:** Другой AI (CV evaluation) + Человек vs AI (метрики как мост между миром данных и миром врача).

**Иллюстрация (MANDATORY):**
- **Тип:** schematic 2×2 matrix (PowerPoint shapes) + small example chart.
- **Источник-кандидаты:**
  - **Self-generated** PowerPoint matrix.
  - **Sample data:** mosmed.ai annual report 2022 (sensitivity/specificity by pathology) + Sezgin 2024 NEJM AI benchmarks.
  - **Alt:** ROC curve from a published paper (Rajpurkar et al. 2017 CheXNet ROC figure).
- **Caption (5-10 слов):** «2×2 confusion matrix, mosmed.ai COVID-screening (2020-2022)»
- **Визуальная функция:** mathematical foundation; bridge between math intuition и medical decision-making.

**Speaker notes hints:**
1. Matrix subtype rules: axis labels INSIDE matrix; cells max 2 lines; font ≥14pt.
2. Trade-off explanation: «нельзя одновременно sens=1 и spec=1; это два разных threshold выбора».
3. Medical context: для screening (раннее обнаружение) — приоритет sensitivity (не пропустить рак); для confirmation (исключить) — приоритет specificity (не пугать здорового).
4. Mat-prerequisites: студент 3-курса знает Bayes; здесь applied case. Setup для s19 micro-exercise.
5. Avoid intensive proof; цель — intuition, не formal derivation.

**Связь с другими слайдами:** s11 (AI vs радиолог), s12 (mosmed numbers), s19 (мicro-упражнение — студенты просят AI объяснить sens/spec).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` mosmed.ai numbers — published в реценз. журнале (Morozov et al. возможно)? Если не публичны — заменить на CheXNet pneumonia numbers (sensitivity 0.96, specificity 0.93 — published values).

**Cross-frame anchor:** LO1 + LO2 + Другой AI + Человек vs AI.

---

### Слайд 11 — AI vs радиолог: что значит «AI лучше» (3 мин) (`comparison`)

**Описание:** 2-column comparison — AI alone vs radiologist alone vs AI+radiologist.

**Содержание (visible):**
- **Assertion:** «"AI лучше радиолога" — миф. "AI + радиолог" лучше каждого по отдельности — это уже работающая практика.»
- **3 columns / 3-row comparison:**
  - **AI alone:** sensitivity 0.94 / specificity 0.89 (mosmed COVID `[FACT-CHECK]`)
  - **Radiologist alone:** sensitivity 0.85-0.92 / specificity 0.95+ (Liu et al. 2019 Lancet Digital Health meta-analysis)
  - **AI + Radiologist:** sensitivity 0.97+ / specificity 0.94+ (Sezgin et al. 2024 + Mango Tx 2024 mammo studies)
- Caption: «Liu et al. 2019 Lancet Digital Health: первый meta-analysis 14 prospective studies AI imaging.»

**LO mapping:** **LO2** + **LO3** (оценка применимости + анализ trade-off).

**Frame mapping:** Человек vs AI (центральный frame этого слайда) + Другой AI.

**Иллюстрация (MANDATORY):**
- **Тип:** comparison_2col chart (3 stacked bar charts, side-by-side).
- **Источник-кандидаты:**
  - **Liu et al. 2019** Lancet Digital Health: «A comparison of deep learning performance against health-care professionals» `https://doi.org/10.1016/S2589-7500(19)30123-2` — figure 2.
  - **McKinney et al. 2020 Nature** «International evaluation of an AI system for breast cancer screening» — figure 3.
  - **Sezgin et al. 2024 NEJM AI** (если в open access).
  - **Self-generated chart** from numbers.
- **Caption (5-10 слов):** «Liu et al. 2019 (Lancet), McKinney 2020 (Nature)»
- **Визуальная функция:** evidence — quantitative comparison; кульминация фрейма «человек vs AI».

**Speaker notes hints:**
1. Comparison subtype rules: identical row structure; equal column widths; gold marker на «winner» row (AI+radiologist).
2. Liu et al. 2019 — landmark meta-analysis, до сих пор cited. McKinney 2020 — followed by Google's mammography work.
3. Disclaimer: numbers depend on dataset, pathology, condition. «AI alone outperforms» — narrow claims, не universal.
4. Nudge towards human-in-the-loop framing → connects to LO8.
5. Avoid «AI wins / radiologist loses» narrative; emphasize **complementarity**.

**Связь с другими слайдами:** s10 (метрики foundation), s12 (mosmed concrete), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` все 3 sets чисел; freshness — мета-анализы post-2024 могут показывать другую картину; verify license для paper figures (open access?).

**Cross-frame anchor:** LO2 + LO3 + Человек vs AI + Другой AI.

---

### Слайд 12 — Российский case: mosmed.ai (3 мин) (`assertion_visual` + schema subtype: `pipeline` for workflow)

**Описание:** concrete deep-dive — mosmed.ai в Московской ОМС-системе.

**Содержание (visible):**
- **Assertion (callback к central question):** «mosmed.ai — конкретный пример того, как AI-обещание сбылось: 4 млрд руб/год экономии для ОМС Москвы.»
- **Mini-pipeline schema:**
  - Снимок (КТ/МРТ/рентген) → mosmed.ai cloud → AI-анализ (24 модели на 2025) → результат врачу + 2nd opinion → решение
- **Numbers (info-cards):**
  - >12 млн изображений с 2020 `[FACT-CHECK]`
  - 80+ клиник Москвы подключены
  - 24 модели по разным патологиям (рак лёгкого, инсульт, COVID, остеопороз, ...)
  - **4 млрд руб/год** экономии в ОМС (Vedomosti / Kommersant 2024-2025) `[FACT-CHECK]`
- Caption: «Источник: mosmed.ai, Vedomosti, ДЗМ Москвы»

**LO mapping:** **LO2** (применимость) + **LO1** (типы AI).

**Frame mapping:** Другой AI + Безопасность (medical data, регулирование) + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** official product screenshot + small workflow diagram.
- **Источник-кандидаты:**
  - **mosmed.ai dashboard:** `https://mosmed.ai/` — screenshot of statistics page.
  - **News attribution:** Vedomosti `https://www.vedomosti.ru/` (search «mosmed.ai 4 млрд»), Kommersant `https://www.kommersant.ru/` (search same).
  - **DZM Moscow report:** if available публично.
- **Caption (5-10 слов):** «mosmed.ai dashboard статистики (2024-2025)»
- **Визуальная функция:** Russian-context anchor + concrete evidence; central case study лекции.

**Speaker notes hints:**
1. Russian context EXPLICIT — это требование курса (RU emphasis).
2. mosmed.ai — federated AI platform, не one model; разные vendor-модели (Сбер AI Lab, Care Mentor AI, Третье Мнение, ...) проходят through unified deployment + benchmark testing.
3. Bridge: «мы здесь увидели обещание AI-диагностики сбывшееся. На s17 увидим обещание drug discovery — частично сбывшееся».
4. Не уходить в политику healthcare; focus = technical + ROI evidence.
5. Cite ДЗМ + Vedomosti / Kommersant для прозрачности attribution.

**Связь с другими слайдами:** s8 (ROI framing), s11 (radiologist comparison), s14 (return to central question), s23 (Russian regulation).

**Risks / things to verify в Phase 0b:** **CRITICAL** `[FACT-CHECK]` 4 млрд руб/год figure — точная сумма, год, методология; `[FACT-CHECK]` image count + клиник count; verify mosmed.ai consent для screenshot.

**Cross-frame anchor:** LO1 + LO2 + Другой AI + Безопасность + Человек vs AI.

---

### Слайд 13 — Where AI-диагностика fails: bias studies (3 мин) (`assertion_visual`)

**Описание:** known failure modes of medical CV — bias case studies.

**Содержание (visible):**
- **Assertion:** «AI-диагностика хорошо работает в распределении обучения. Outside that — может проваливаться unfairly.»
- **3 bias case-cards:**
  1. **Dermatology skin tone bias** — most dermatology AI обучены на light-skin datasets; для dark-skin pacientов sensitivity drops 20-30%. Reference: Daneshjou et al. 2021 (Science Advances), Adamson & Smith 2018 (JAMA Dermatology).
  2. **Pulse oximeter signal AI** — racial bias в SpO2 sensors and downstream AI; FDA warning 2021.
  3. **Obermeyer et al. 2019 Science** — Optum risk-scoring AI underestimated severity для black patients (proxy: cost не severity).
- Caption: «Не bug, а consequence design choices: training data ≠ deployment population.»

**LO mapping:** **LO3** (анализ этических рисков) + **LO6** (выявление ограничений implicit).

**Frame mapping:** LLM anti-pattern adaptation (для CV: «не верь модели без проверки на твоей популяции»; см. s22 для LLM-specific) + Безопасность + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** paper figure + supporting news screenshot.
- **Источник-кандидаты:**
  - **Obermeyer et al. 2019:** Science paper figure `https://www.science.org/doi/10.1126/science.aax2342` (figure 1: gap chart).
  - **Daneshjou et al. 2021:** Science Advances `https://doi.org/10.1126/sciadv.abk1571` paper figure.
  - **News:** STAT News `https://www.statnews.com/` article на dermatology AI bias OR Wired `https://www.wired.com/story/medical-ai-racial-bias/`.
- **Caption (5-10 слов):** «Obermeyer et al. 2019, Daneshjou et al. 2021»
- **Визуальная функция:** evidence для bias claim; emotional anchor для responsibility framing.

**Speaker notes hints:**
1. Bias ≠ malice; это consequence of training data composition.
2. Engineering implication: validation set должен покрывать deployment population — это не academic point, а responsibility.
3. Russian relevance: mosmed.ai trained mostly on Russian population; what about deployments in other regions/ethnicities? Open question.
4. Bridge to s22 (NEDA Tessa) and s24 (responsibility): «эти ошибки не теоретические; они происходят systematically».
5. Avoid moralizing; engineer-tone = «вот пример, инженер должен думать об этом on day one».

**Связь с другими слайдами:** s22 (LLM anti-pattern, NEDA Tessa scandal), s24 (responsibility framework).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` все 3 papers — verify findings hold по 2026; Daneshjou paper specifics (skin tone categories used: Fitzpatrick scale).

**Cross-frame anchor:** LO3 + LO6 + Безопасность + Человек vs AI + setup для LLM anti-pattern.

---

## Раздел 3. Drug discovery: обещания vs реальность (14 мин)

### Слайд 14 — Mid-lecture callback к central question (1 мин) (`assertion_visual`)

**Описание:** explicit mid-lecture pause — return to central question.

**Содержание (visible):**
- **Assertion (callback):** «Мы прошли половину. AI-диагностика — обещание сбылось (mosmed: 4 млрд руб/год). Drug discovery — обещали 10× быстрее. Что реально?»
- **Простой layout:** central question crisp в Ocean rounded box + 2 callback-pointers (s12 mosmed cell + s17 DSP cell upcoming).

**LO mapping:** N/A (structural anchor).

**Frame mapping:** Cross-cutting — все 6 frames.

**Иллюстрация (MANDATORY):**
- **Тип:** schematic transition slide (large central question text + 2 anchor pointers).
- **Источник:** self-generated (typography + Ocean rounded box motif).
- **Caption:** N/A.
- **Визуальная функция:** structural anchor — преподаватель paused, аудитория re-orients; mid-lecture pacing.

**Speaker notes hints:**
1. Pause beat — 5-7 секунд silence allowed.
2. «Это половина. Дальше — пол лекции.» — signaling progress.
3. Если аудитория устаёт — это место для 1-вопрос Q&A или потрясения «кто помнит mosmed число?»
4. Avoid additional content; this slide is structural, not informational.
5. Setup для s15 (drug discovery foundation) + s17 (DSP reality).

**Связь с другими слайдами:** s5 (central question), s12 (mosmed payoff), s17 (DSP payoff).

**Risks:** none.

**Cross-frame anchor:** All 6 frames cross-cutting.

---

### Слайд 15 — Что такое drug discovery + AI role (2.5 мин) (`assertion_visual` + schema subtype: `pipeline`)

**Описание:** technical foundation — что такое drug discovery, где AI меняет цикл.

**Содержание (visible):**
- **Assertion:** «Drug discovery — 10-15 лет, $1-2 млрд, ~10% success rate. AI обещает сократить первые 5 лет (discovery + preclinical) до 1-2.»
- **Pipeline schema (5 stages):**
  1. **Target identification** — какой белок атаковать. AI: AlphaFold, AlphaProteo.
  2. **Hit discovery** — молекула-кандидат. AI: generative ML (Insilico, Exscientia).
  3. **Lead optimization** — улучшение свойств молекулы. AI: simulation + ML.
  4. **Preclinical** — клетки, животные. AI: predicting toxicity.
  5. **Clinical I/II/III** — люди. AI: patient stratification. (Здесь AI помогает только узко.)
- Highlight: AI accelerates stages 1-3 значительно; stages 4-5 — human trials, AI помогает marginally.
- Source: Mullard 2024 Nature Reviews Drug Discovery; DiMasi et al. 2016.

**LO mapping:** **LO1** (типы AI в drug discovery) + **LO2** (applicability).

**Frame mapping:** Другой AI (foundation models — AlphaFold; generative ML; не LLM в основе).

**Иллюстрация (MANDATORY):**
- **Тип:** pipeline diagram (PowerPoint shapes + RIGHT_ARROW) + AlphaFold 3D snapshot.
- **Источник-кандидаты:**
  - **AlphaFold visualization:** DeepMind blog `https://deepmind.google/technologies/alphafold/` — figure с протеином (например, GPCR).
  - **Paper:** Jumper et al. 2021 Nature AlphaFold2 `https://doi.org/10.1038/s41586-021-03819-2`; Abramson et al. 2024 Nature AlphaFold3 `https://doi.org/10.1038/s41586-024-07487-w`.
  - **Pipeline metrics:** DiMasi et al. 2016 JHE; Mullard 2024 Nature Reviews.
- **Caption (5-10 слов):** «AlphaFold 3 (Abramson et al., Nature 2024)»
- **Визуальная функция:** technical foundation + emotional anchor (3D-структура впечатляет, даже не-биолог понимает «это сложно»).

**Speaker notes hints:**
1. Pipeline subtype rules (5 stages OK); each stage label ≤3 слов; use RIGHT_ARROW.
2. Drug discovery total cost — $1.5-2 млрд per approved drug (DiMasi 2016, updated by Wouters et al. 2020 JAMA).
3. AlphaFold 2 (2021) — Нобель 2024 (Hassabis, Jumper) — callback к Лекции 1 s10/s25.
4. AlphaFold 3 (2024) — protein-protein, protein-DNA, protein-RNA — beyond just structure.
5. Critical: AI не делает preclinical/clinical чудом — только discovery + lead optimization; clinical trials = years and humans.

**Связь с другими слайдами:** s16 (AlphaFold deep), s17 (DSP-1181 — first AI-designed drug в trials), Лекция 1 s10/s25 (Нобель callback).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` drug discovery cost & time numbers; `[FACT-CHECK]` AlphaFold 3 capabilities + публикация date; freshness — AlphaProteo paper (DeepMind 2024).

**Cross-frame anchor:** LO1 + LO2 + Другой AI.

---

### Слайд 16 — AlphaFold + AlphaProteo: что реально достигнуто (2.5 мин) (`assertion_visual`)

**Описание:** deep-dive в AlphaFold's actual impact on drug discovery as of 2026.

**Содержание (visible):**
- **Assertion:** «AlphaFold предсказал 200M+ структур белков. Это решённая задача 50-летней давности. AlphaProteo проектирует binders.»
- **3 evidence-cards:**
  1. **200M+ structures (UniProt coverage):** AlphaFold Protein Structure Database `alphafold.ebi.ac.uk` — open, free. Used by 2M+ researchers в 190 странах (DeepMind 2024 update). `[FACT-CHECK]`
  2. **AlphaProteo (2024):** designs new protein binders с 3-300× improved affinity vs prior methods (DeepMind blog Sep 2024). `[FACT-CHECK]`
  3. **AlphaFold-Multimer + AlphaFold 3:** protein complexes, RNA-protein interactions — enables drug-target binding prediction.
- Caption: «Source: DeepMind blog 2024; Jumper et al. 2021; Abramson et al. 2024.»

**LO mapping:** **LO1** (advance state of AI in drug discovery) + **LO2** (applicability).

**Frame mapping:** Другой AI (foundation model для protein folding, не LLM).

**Иллюстрация (MANDATORY):**
- **Тип:** official product screenshot + 1 paper figure.
- **Источник-кандидаты:**
  - **AlphaFold DB screenshot:** `https://alphafold.ebi.ac.uk/` — front page or example structure.
  - **DeepMind blog AlphaProteo:** `https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/` (Sep 2024) — figure.
  - **Abramson et al. 2024 Nature AlphaFold 3:** open-access figure.
- **Caption (5-10 слов):** «AlphaFold Protein Structure DB, alphafold.ebi.ac.uk»
- **Визуальная функция:** evidence — large-scale achievement; emotional anchor (открытая база, бесплатная).

**Speaker notes hints:**
1. Не входить в transformer-architecture details (это для Лекции 2).
2. Bridge с Лекцией 1 s25: «AlphaFold = Нобель 2024; AlphaProteo — следующий шаг от prediction к generation».
3. Important: AlphaFold predicts structure, BUT drug discovery нуждается ещё в lead optimization, ADMET, ... Многое от lab work остаётся.
4. Russian context: SberMed AI и Sber AI Lab — российские игроки в drug discovery (см. s17).
5. Trust-but-verify: AlphaFold confidence scores (pLDDT) — модель сама помечает, где она уверенна, где нет.

**Связь с другими слайдами:** s15 (pipeline context), s17 (от prediction к real-world drug).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` всё — DeepMind statistics, AlphaProteo capabilities; freshness — AlphaFold 4? on 2026?; verify access to figures.

**Cross-frame anchor:** LO1 + LO2 + Другой AI.

---

### Слайд 17 — DSP-1181 reality check: обещание vs действительность (3.5 мин) (`assertion_visual`)

**Описание:** **the key narrative slide** — DSP-1181 case study (Exscientia + Sumitomo). Маркетинговое обещание «12 месяцев vs 4-5 лет» vs реальный outcome. Per user spec — fact-check может показать что drug был **discontinued** — это ценная история сама по себе.

**Содержание (visible):**
- **Assertion:** «DSP-1181 (2020): "первый AI-designed drug" — обещали 12 месяцев design vs 4-5 лет традиционно. Что случилось дальше?»
- **Timeline визуал (~5 events):**
  - **2020 (январь):** Exscientia + Sumitomo Dainippon announce DSP-1181, OCD trial.
  - **2020-2021:** Phase 1 (Japan).
  - **2022 (середина):** **Phase 1 closed/discontinued** — недостаточная эффективность. `[CRITICAL FACT-CHECK]` — Sumitomo announcement.
  - **2022-2024:** Exscientia продолжает с другими candidates (DSP-2342, EXS21546, …).
  - **2024-2026:** **Exscientia сама — turbulent** (CEO Hopkins fired 2025; merger talks с Recursion 2024). `[FACT-CHECK]`
- **Insight:** «AI ускорил design phase (это реально), но clinical efficacy — separate question. Маркетинговое обещание «AI drug = быстро + эффективно» = две разные claims, объединённые рекламой.»
- Caption: «Sources: STAT News, FierceBiotech, Endpoints News, Sumitomo 2022 PR.»

**LO mapping:** **LO2** (оценка applicability) + **LO3** (анализ рисков и обещаний) + framing для **LO8**.

**Frame mapping:** Человек vs AI (ответственность за обещания) + LLM anti-pattern adaptation (маркетинг AI ≠ working AI) + Безопасность (informed decisions in regulation).

**Иллюстрация (MANDATORY):**
- **Тип:** news screenshot + timeline schema.
- **Источник-кандидаты:**
  - **STAT News:** `https://www.statnews.com/` поиск «Exscientia DSP-1181» (2020 announcement + 2022 discontinuation).
  - **FierceBiotech:** `https://www.fiercebiotech.com/` поиск «Exscientia».
  - **Endpoints News:** `https://endpts.com/` Exscientia coverage.
  - **Original Exscientia 2020 press release:** Exscientia blog archive.
  - **Sumitomo 2022 announcement** (если public).
  - **Recent (2025):** STAT/Endpoints на Exscientia CEO firing + Recursion merger.
- **Caption (5-10 слов):** «Timeline: Exscientia DSP-1181 (STAT, FierceBiotech, Endpoints, 2020-2025)»
- **Визуальная функция:** narrative arc — обещание → реальность; **CRITICAL для central question payoff**.

**Speaker notes hints:**
1. **Per user spec:** «fact-checker подтвердит свежий статус. Если discontinued — это сама по себе ценная история: маркетинговое обещание vs реальность.»
2. Timeline subtype rules: events single-line, em-dash; max 5 events per band; pivot year (2022 discontinuation) ≥2× размер.
3. Honest, no schadenfreude tone: «Exscientia реально ускорила design. Они не виноваты, что efficacy не сложилась — это биология. Виновата маркетинговая riffраfика, которая объединила discovery time и approval probability».
4. Engineering lesson: «если ты строишь AI для drug discovery — twoclai: (1) ускоряем design; (2) ускоряем approval. Только первое — техническая мера; вторая — клинико-биологическая.»
5. Russian context: Sber AI Lab Russian drug discovery efforts (AIDD pilot 2024-2025) — параллельная история. `[FACT-CHECK]` точный статус.

**Связь с другими слайдами:** s5 (central question payoff), s14 (mid-callback), s18 (FDA framework — как regulator смотрит).

**Risks / things to verify в Phase 0b:** **CRITICAL** `[FACT-CHECK]` DSP-1181 status (Phase 1 closed? continued? other? — get authoritative source); `[FACT-CHECK]` Exscientia 2025 timeline; freshness — weekly cadence для biotech news.

**Cross-frame anchor:** LO2 + LO3 + LO8 framing + Человек vs AI + LLM anti-pattern adaptation + Безопасность.

---

### Слайд 18 — FDA AI/ML framework: как regulator оценивает (2.5 мин) (`assertion_visual` + schema subtype: `pipeline`)

**Описание:** FDA's AI/ML SaMD framework + predetermined change control plan (PCCP) — как regulator подходит к AI-medical software.

**Содержание (visible):**
- **Assertion:** «FDA не запрещает AI в медицине. FDA требует доказательство safety + effectiveness + plan для post-market updates.»
- **5-step framework simplified pipeline:**
  1. **Intended use** — что именно AI делает.
  2. **Algorithm description** — как работает (architecture, training data).
  3. **Performance evaluation** — sensitivity/specificity на test set.
  4. **Predetermined Change Control Plan (PCCP)** — какие updates разрешены post-market без re-approval. **Это innovation 2023-2024.**
  5. **Post-market monitoring** — real-world performance tracking.
- Caption: «FDA Guidance: Marketing Submission Recommendations for a Predetermined Change Control Plan for AI-Enabled Device Software Functions (final guidance Dec 2024).»

**LO mapping:** **LO3** (regulatory framework) + **LO8** (responsibility — regulatory side).

**Frame mapping:** Безопасность (regulation) + Человек vs AI (regulator role).

**Иллюстрация (MANDATORY):**
- **Тип:** schema pipeline + screenshot from FDA document.
- **Источник-кандидаты:**
  - **FDA AI/ML SaMD action plan:** `https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device`
  - **FDA PCCP guidance (Dec 2024):** `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence`
  - **Self-generated pipeline schema** + FDA logo + small document screenshot.
- **Caption (5-10 слов):** «FDA PCCP final guidance, December 2024»
- **Визуальная функция:** institutional anchor — regulation is concrete, not abstract; setup для responsibility.

**Speaker notes hints:**
1. Pipeline subtype rules: 5 stages max OK; clean separation; RIGHT_ARROW shapes.
2. PCCP — **innovation** for AI: traditional medical device = one-and-done approval; AI evolves continuously. PCCP лет vendors pre-declare what changes are OK.
3. Engineering implication: «if you design AI for medical device — design with PCCP в mind; data drift, retraining, threshold updates — all must be planned ex ante».
4. Russian parallel: Росздравнадзор (см. s23) — менее developed framework, но активно работают.
5. Mention EU AI Act briefly — медицинский AI = high-risk; conformity assessment required.

**Связь с другими слайдами:** s7 (FDA count), s17 (regulatory reality для drugs), s23 (regulation deep), s25 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` PCCP final guidance date + content (FDA публикация); `[FACT-CHECK]` actual number of devices using PCCP (recent FDA data).

**Cross-frame anchor:** LO3 + LO8 + Безопасность + Человек vs AI.

---

## Раздел 4. Микро-упражнение AI (8 мин)

### Слайд 19 — Micro-exercise: AI explains sens/spec + критическая оценка (8 мин) (`assertion_visual` + interactive)

**Описание:** **единственное студенческое упражнение лекции** (per user spec). 8 минут активной работы. Студенты используют ChatGPT/Claude web-chat — просят объяснить sensitivity/specificity для medical AI, как студенту 2 курса. Потом критически оценивают: что AI сделал хорошо? Что — поверхностно или подозрительно?

**Содержание (visible):**
- **Assertion:** «Используем AI для понимания AI. Но не доверяем без проверки.»
- **Task (2 steps):**
  1. **Step 1 (3 мин):** «Открой ChatGPT/Claude/YandexGPT. Промпт: "Объясни мне, что такое sensitivity и specificity для AI-диагностики на конкретном примере (например, mammography screening). Объясни как для студента 2 курса техн. вуза, со знанием базовой probability."»
  2. **Step 2 (3 мин):** «Прочитай ответ. Заметь: (a) есть ли error/неточность? (b) AI приводит конкретные числа — проверяемые? (c) пример adequate?»
- **Reveal (2 мин):** разбор 2-3 ответов аудитории. Лектор показывает свой "control" ответ (заранее прогнанный).
- **LLM pattern:** «Объясни как студенту X курса» — стандартный pattern для education + patient education.
- **LLM anti-pattern:** «Не доверяй медицинским советам без верификации».

**LO mapping:** **LO2** (apply AI to оценить) + **LO3** (critical evaluation).

**Frame mapping:** **LLM pattern** (объясни как студенту 2 курса) + **LLM anti-pattern** (не доверяй без верификации) — оба explicit.

**Иллюстрация (MANDATORY):**
- **Тип:** task card layout + 1 example AI response screenshot (lecturer's pre-prepared control).
- **Источник-кандидаты:**
  - **Self-generated** task layout (PowerPoint shapes + chip-pills).
  - **Control screenshot** — Claude.ai or ChatGPT response, prepared by lecturer night before, sanitized.
- **Caption (5-10 слов):** «Задача: попроси AI объяснить, потом проверь»
- **Визуальная функция:** call-to-action + control example для guided discussion.

**Speaker notes hints:**
1. **Critical pre-flight:** lecturer должен прогнать промпт сам накануне лекции (freshness — модель меняется!) и иметь скриншот baseline.
2. Russian context: добавить YandexGPT, GigaChat options.
3. If ChatGPT/Claude unavailable in classroom — pre-print 3-5 sample AI responses for paper-based exercise.
4. Discussion focus: «AI отлично объяснил для студента 2 курса» = LLM pattern сработал. «AI дал число sensitivity 0.95 без citation» = anti-pattern — не верь.
5. Bridge to s22 (NEDA Tessa scandal): «patient education через AI — реальная индустрия; и здесь — реальные риски».
6. Timing strict: 8 минут total — не давать упражнению расплыться.

**Связь с другими слайдами:** s10 (sens/spec foundation), s22 (NEDA Tessa — что бывает, когда не verified), s28 (3 главных вывода — LO8).

**Risks / things to verify в Phase 0b:** sample AI response может содержать factual errors — `[FACT-CHECK]` baseline response для control; planning for unstable wifi / no-internet fallback.

**Cross-frame anchor:** LO2 + LO3 + LLM pattern + LLM anti-pattern.

---

## Раздел 5. Границы + этика + ответственность (14 мин)

### Слайд 20 — Зачем инженеру думать про границы в медицинском AI (1 мин) (`assertion_visual`)

**Описание:** transition slide — вводная рамка для последнего content section.

**Содержание (visible):**
- **Assertion:** «В медицинском AI ставки максимальны: ошибка модели = ошибка диагноза или назначения = вред пациенту. Что инженер должен знать про границы.»
- **3 темы next 5 slides:**
  1. LLM anti-pattern в медицине (NEDA Tessa).
  2. Безопасность медицинских данных (Change Healthcare breach).
  3. Кто отвечает за AI-ошибку.

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
3. Этот блок — самая короткая arc лекции, но самая важная для LO8.
4. Pacing: одна минута strictly.
5. Avoid mentioning specific cases here (s22-23 будут).

**Связь с другими слайдами:** s22, s23, s24.

**Risks:** none beyond image attribution.

**Cross-frame anchor:** LO3 + LO8 framing.

---

### Слайд 21 — Bias в medical AI: Obermeyer 2019 deep-dive (3 мин) (`assertion_visual`)

**Описание:** одно из самых ярких bias case studies — Optum / UnitedHealth risk-scoring AI, описанный в Obermeyer et al. 2019 Science. Note: bias уже коротко затронут на s13 — здесь deep-dive с одним paper.

**Содержание (visible):**
- **Assertion:** «Obermeyer et al. 2019 (Science): commercial AI алгоритм для 200M Americans systematically underestimated severity для black patients. Proxy "стоимость лечения" вместо "тяжесть болезни".»
- **Mechanism (3 boxes):**
  1. **Goal:** identify pacients needing additional care.
  2. **Proxy used:** spending on previous care.
  3. **Bias source:** black patients spent less historically (access disparities) → AI thinks less sick → less care.
- **Result chart:** at same risk score, black patients had 26.3% more chronic illnesses than white.
- **Fix:** Optum + researchers совместно improved algorithm — reduction in bias by 84% post-fix.
- Caption: «Obermeyer, Powers, Vogeli, Mullainathan — Science 366, 447-453 (2019). DOI: 10.1126/science.aax2342»

**LO mapping:** **LO3** (анализ этических рисков) + **LO6** (выявление ограничений).

**Frame mapping:** Безопасность + Человек vs AI + LLM anti-pattern adaptation.

**Иллюстрация (MANDATORY):**
- **Тип:** paper figure + supporting news screenshot.
- **Источник-кандидаты:**
  - **Obermeyer 2019** Science figure `https://www.science.org/doi/10.1126/science.aax2342` (Figure 1: gap chart) — likely subscription, but figure should be reproduce-able under fair use as cited research.
  - **STAT News follow-up:** `https://www.statnews.com/2019/10/24/algorithm-racial-bias-care-black-patients/`.
  - **Wired follow-up:** `https://www.wired.com/story/algorithm-racial-bias-care-black-patients/`.
- **Caption (5-10 слов):** «Obermeyer et al., Science 2019. DOI: 10.1126/science.aax2342»
- **Визуальная функция:** evidence для bias claim; foundation для responsibility framing.

**Speaker notes hints:**
1. Это THE landmark paper по bias в medical AI; cited 3000+ раз; must-know для инженера.
2. Не moralize; engineer-tone: «вы будете строить metric-driven AI. Выбор proxy = design choice с consequence».
3. Optum / UnitedHealth — для российской аудитории это абстрактный «крупный insurer USA»; можно объяснить «как Сбер или ВТБ — большой scope deployment».
4. Russian parallel: bias в кредитном скоринге (Лекция 3) — тот же механизм, иная industry; cross-lecture connection.
5. Bridge to s22: «если в risk-scoring AI bias — он tabular numerical; в LLM в медицине — bias на uровне советов».

**Связь с другими слайдами:** Лекция 3 s12 (bias в финансах — параллель), s13 (bias в CV — параллель), s22 (LLM specific case), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` Obermeyer 2019 numbers verbatim — 26.3%, 84% fix; verify access to figure.

**Cross-frame anchor:** LO3 + LO6 + Безопасность + Человек vs AI.

---

### Слайд 22 — LLM anti-pattern в медицине: NEDA Tessa chatbot scandal (3 мин) (`assertion_visual`)

**Описание:** concrete LLM-specific case — NEDA chatbot «Tessa» был запущен для replace human eating-disorder helpline; снят с обращения в 2023 после providing harmful weight-loss tips. Plus ChatGPT/Bing medical misinformation incidents.

**Содержание (visible):**
- **Assertion:** «LLM в медицине ≠ медицинский AI. NEDA Tessa (2023) — chatbot, заменивший human helpline. Снят с эфира за 3 дня после providing weight-loss tips eating disorder pacientам.»
- **Mini-timeline (3 events):**
  - 2022: NEDA decides replace human helpline (cost saving) with Tessa.
  - **31 мая 2023:** Tessa launch.
  - **2 июня 2023:** Tessa suspended — Activists revealed harmful weight-loss advice provided to pacient с eating disorder.
- **2-3 supporting incident counts:**
  - **Air Canada chatbot (2024):** hallucinated refund policy — court ordered компанию pay.
  - **ChatGPT medical Q&A studies:** ~20% hallucination rate в medical literature citations (Mihalache et al. 2024 + others).
- **Why это different от s21 (Obermeyer):** s21 = tabular AI с biased proxy; s22 = generative LLM в open-ended medical advice — class apart.
- Caption: «Sources: Vice 2023, NPR 2023, Mihalache et al. 2024 JAMA Network Open.»

**LO mapping:** **LO3** (анализ риска) + **LO6** (выявление ограничений LLM конкретно) + framing для **LO8**.

**Frame mapping:** **LLM anti-pattern (CORE для этого слайда)** + Безопасность + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** news screenshot collage + 1 quoted Tessa transcript.
- **Источник-кандидаты:**
  - **Vice 2023:** `https://www.vice.com/en/article/eating-disorder-helpline-chatbot/` (full incident report).
  - **NPR 2023:** `https://www.npr.org/2023/06/08/1180553778/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea`.
  - **Mihalache et al. 2024:** JAMA Network Open `https://doi.org/10.1001/jamanetworkopen.2024.21945` (ChatGPT medical citation accuracy).
- **Caption (5-10 слов):** «NEDA Tessa суспендирована, июнь 2023 (NPR, Vice)»
- **Визуальная функция:** emotional anchor (real-world harm); evidence для LLM anti-pattern in medical context.

**Speaker notes hints:**
1. **Per user spec:** «доверие медицинским советам AI без верификации — с КОНКРЕТНЫМИ documented incidents».
2. Не sensationalize; tone = professional cautionary.
3. Engineering lesson: LLM ≠ classifier. LLM generates open-ended text — failure mode unbounded.
4. Bridge to s19 micro-exercise: «помните, мы просили AI объяснить sens/spec? Если бы мы просили medical advice — другая game.»
5. Russian context: GigaChat / YandexGPT — никаких медицинских disclosures formal? `[FACT-CHECK]` actual policies.

**Связь с другими слайдами:** s19 (micro-exercise foundation), s21 (другой bias case parallel), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` NEDA Tessa specifics + dates; `[FACT-CHECK]` Mihalache 2024 numbers; verify Vice/NPR articles still accessible.

**Cross-frame anchor:** LO3 + LO6 + LO8 framing + LLM anti-pattern + Безопасность + Человек vs AI.

---

### Слайд 23 — Безопасность медицинских данных: Change Healthcare breach (2 мин) (`assertion_visual`)

**Описание:** medical data security — Change Healthcare ransomware attack февраль 2024.

**Содержание (visible):**
- **Assertion:** «Медицинские данные — самая защищаемая категория. И самая ценная для атакующих. Change Healthcare (Feb 2024): 190 млн человек, $2-3 млрд recovery cost.»
- **Numbers (info-cards):**
  - **190 млн** affected (UnitedHealth Group estimate, Oct 2024). `[FACT-CHECK]`
  - **$2-3 млрд** recovery cost (UHG financial reports).
  - **22 дня** outage major US healthcare claims processing.
  - **ALPHV/BlackCat** — ransomware group; paid $22 млн ransom.
- **Regulations applicable:** HIPAA (US), GDPR (EU), **ФЗ-152 (РФ)** — personal data; ePHI = electronic protected health information.
- **Engineering implication:** «деперсонализация (de-identification) ≠ anonymization. Re-identification возможна через linking; medical data — особая категория».

**LO mapping:** **LO3** (risks) + **LO8** (security as responsibility).

**Frame mapping:** **Безопасность (CORE)** + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** news screenshot + small infographic.
- **Источник-кандидаты:**
  - **Reuters:** `https://www.reuters.com/` поиск «Change Healthcare 190 million».
  - **Bloomberg:** `https://www.bloomberg.com/`.
  - **The Verge:** `https://www.theverge.com/` cybersecurity section.
  - **UHG Q3 2024 financials:** UnitedHealth Group investor relations page.
- **Caption (5-10 слов):** «Change Healthcare breach Feb 2024 (Reuters, UHG IR)»
- **Визуальная функция:** evidence для scale claim; emotional anchor.

**Speaker notes hints:**
1. Russian relevance: ФЗ-152 (152-ФЗ) — особая категория «биометрические + медицинские данные»; deperonsalization обязательна.
2. Brief mention: medical AI training data — нужно деперсонализировать (есть techniques: HIPAA Safe Harbor, k-anonymity, differential privacy).
3. Bridge: «mosmed.ai обрабатывает 12M+ изображений — они hat handle this carefully; не каждый stack делает».
4. Не входить в крипто-детали ransomware (это для другой лекции).
5. Engineering lesson: проектируя medical AI, ты проектируешь target ransomware groups.

**Связь с другими слайдами:** s12 (mosmed scale = ransomware-target scope), s18 (regulation FDA), s25 (responsibility framework).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` 190M number + recovery cost + ransom amount; freshness — secondary breaches in 2025-2026 (Ascension breach?).

**Cross-frame anchor:** LO3 + LO8 + Безопасность.

---

### Слайд 24 — Кто отвечает за AI-ошибку: 4 actors (3 мин) (`assertion_visual` + schema subtype: `matrix_2x2` or `quadrant`)

**Описание:** **the responsibility slide — central для LO8.** 4-actor framework.

**Содержание (visible):**
- **Assertion (callback к central question):** «Когда AI ошибается в диагнозе — кто несёт ответственность?»
- **2×2 quadrant / 4-actor framework:**
  - **Axis X:** technical control (low ↔ high)
  - **Axis Y:** legal liability (low ↔ high)
  - 4 actors:
    - **Врач (high control + high liability):** ставит диагноз. AI — подсказка. Final decision = врача.
    - **Hospital / operator (medium ctrl + medium liability):** выбирает AI-vendor, обучает persons, monitor real-world performance.
    - **AI-vendor / разработчик (high control + medium-low liability):** разрабатывает model, ответственен за safety claims в FDA submission + post-market PCCP.
    - **Regulator / госорган (low ctrl + high oversight):** approves, audits, может revoke.
- **Centrаl line:** «Врач ставит диагноз. AI подсказывает. **Ответственность — на враче.** Vendor + regulator + hospital — обеспечивают системные условия.»
- Caption: «Source: Price 2019 Stanford TR; Gerke et al. 2020 «Ethical and legal challenges of AI-driven healthcare»; EU AI Act Annex III.»

**LO mapping:** **LO3** + **LO8** (CORE — principles of responsibility).

**Frame mapping:** **Человек vs AI (CORE — answers central question)** + Безопасность.

**Иллюстрация (MANDATORY):**
- **Тип:** schematic quadrant + 4 icons.
- **Источник-кандидаты:**
  - **Icons:** Lucide `stethoscope`, `building-2`, `code`, `gavel` (recolored Ocean).
  - **Self-generated quadrant schema.**
  - **Reference paper:** Gerke et al. 2020 в Artificial Intelligence in Healthcare (Elsevier) — chapter on legal frameworks.
- **Caption (5-10 слов):** «4-actor responsibility framework (Price 2019, Gerke 2020)»
- **Визуальная функция:** answer to central question; mental anchor for LO8 framework.

**Speaker notes hints:**
1. Quadrant subtype rules: axis labels INSIDE; max 2 lines per actor card; consistent icon size.
2. THIS is the slide where central question gets answer. Pause, eye contact, speak slowly.
3. «Final responsibility = врача» — это not punitive, it's structural: только врач имеет full context (history, exam, AI как один input).
4. Engineering lesson: «как инженер, ты в actor «AI-vendor». Твоя responsibility — design AI so врач can fulfill его responsibility (transparency, confidence scores, audit trails).»
5. Russian: Росздравнадзор + Минздрав — Russian regulators; Минцифры + Минздрав совместно на digital health.

**Связь с другими слайдами:** s5 (central question), s17 (Exscientia — обещания marketing vs reality), s25 (regulation), s27 (final payoff), s28 (3 principles LO8).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` Price 2019 / Gerke 2020 references accuracy; verify legal framework currency.

**Cross-frame anchor:** LO3 + LO8 (CORE) + Человек vs AI (CORE).

---

### Слайд 25 — Регулирование: FDA + EU AI Act + Росздравнадзор (2 мин) (`comparison`)

**Описание:** 3-column comparison — US/EU/RU approaches к medical AI regulation.

**Содержание (visible):**
- **Assertion:** «Medical AI = formally high-risk во всех 3 крупных jurisdictions. Approaches отличаются процессами, не principles.»
- **3 columns:**
  - **US (FDA):** SaMD framework, PCCP (см. s18), Post-market surveillance.
  - **EU (EU AI Act + MDR):** High-risk AI Annex III; Conformity Assessment; CE-mark; effective Aug 2026 для high-risk.
  - **РФ (Росздравнадзор + Минздрав):** Регистрация медицинских изделий, отдельный класс ПО как медицинское изделие; ГОСТ Р 59921 серия для AI в medicine (2022-2024). `[FACT-CHECK]`
- Caption: «Sources: FDA.gov, EU AI Act Reg. 2024/1689, Росздравнадзор.»

**LO mapping:** **LO3** + **LO8**.

**Frame mapping:** Безопасность + Человек vs AI.

**Иллюстрация (MANDATORY):**
- **Тип:** comparison_2col → adapted to 3-col table + 3 jurisdiction logos/flags.
- **Источник-кандидаты:**
  - **FDA:** logo + screenshot of AI/ML page.
  - **EU AI Act:** official text `https://eur-lex.europa.eu/eli/reg/2024/1689/oj` + EU flag.
  - **Росздравнадзор:** `https://roszdravnadzor.gov.ru/` + RF flag (or Минздрав logo).
- **Caption (5-10 слов):** «FDA, EU AI Act 2024/1689, Росздравнадзор»
- **Визуальная функция:** institutional anchor; concrete для Russian audience.

**Speaker notes hints:**
1. Comparison subtype rules: 3 columns equal width; identical row structure; consistent terminology.
2. RU specifics: ГОСТ Р 59921 — серия стандартов «Искусственный интеллект в здравоохранении» (введены ВНИИИМТ); добавлены 2022-2024.
3. EU AI Act timeline: prohibited practices Feb 2025; high-risk medical AI Aug 2026; полная сила Aug 2027 — relevant для аудитории.
4. Cross-frame: regulation = formal expression of responsibility framework s24.
5. Engineering lesson: deploying medical AI = projects 3 different compliance pipelines.

**Связь с другими слайдами:** s7 (FDA count), s18 (FDA framework), s24 (responsibility).

**Risks / things to verify в Phase 0b:** `[FACT-CHECK]` ГОСТ Р 59921 series — actual standards (есть series но нумерация можете отличаться); EU AI Act high-risk medical AI effective date; freshness — quarterly cadence для regulatory updates.

**Cross-frame anchor:** LO3 + LO8 + Безопасность + Человек vs AI.

---

## Раздел 6. Заключение (6 мин)

### Слайд 26 — 3 главных вывода (2 мин) (`summary`)

**Описание:** 3 takeaways — explicit mapping на LO1+LO2+LO3+LO8.

**Содержание (visible):**
- **Wider message:** «Медицинский AI к 2026 — это работающая инфраструктура, не футурология. И вместе с этим — конкретная responsibility framework.»
- **3 takeaway cards:**
  1. **AI-диагностика работает (LO1, LO2):** mosmed.ai 4 млрд руб/год, FDA 1000+ devices, AI+врач > врача alone в meta-analysis. CV-pipeline уровня 2017-2024.
  2. **Drug discovery — частично (LO2, LO3):** AlphaFold = solved structure prediction, Нобель 2024. Discovery + lead optimization ускорены 5-10×. Clinical efficacy = otherwise.
  3. **Ответственность — на враче (LO3, LO8):** AI подсказывает, врач решает. Инженер строит систему так, чтобы responsibility была технически выполнима (transparency, calibration, audit, deperonsalization, monitoring).

**LO mapping:** **LO1, LO2, LO3, LO8 — все 4.**

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
4. LO8 — explicitly framed (responsibility framework), новизна Л4.
5. Avoid extra content beyond 3 cards.

**Связь с другими слайдами:** s5 (central question), s24 (responsibility), s28 (Q&A).

**Risks:** none beyond no extra content.

**Cross-frame anchor:** All LOs + all frames.

---

### Слайд 27 — Callback to central question + emotional payoff (1 мин) (`assertion_visual`)

**Описание:** explicit callback + final emotional anchor.

**Содержание (visible):**
- **Callback to central question (большой текст):** «**Какие AI-обещания в медицине сбылись? — Диагностика да. Drug discovery — частично. Ответственность — всегда на враче.**»
- **Closing line:** «Врач ставит диагноз. AI подсказывает. Инженер делает так, чтобы врач мог по-настоящему решать.»

**LO mapping:** **LO8** (closing principle).

**Frame mapping:** Человек vs AI (CORE final note) + LO8.

**Иллюстрация (MANDATORY):**
- **Тип:** stock photo (close-up, emotional anchor).
- **Источник-кандидаты:**
  - Unsplash `https://unsplash.com/s/photos/doctor-patient` (CC0, doctor explaining to patient).
  - Pexels `https://www.pexels.com/search/medical%20consultation/`.
- **Caption (5-10 слов):** «Врач + пациент: human stays central (Unsplash CC0)»
- **Визуальная функция:** emotional payoff; reinforces center of LO8.

**Speaker notes hints:**
1. Pause, eye contact, slow speech.
2. This is the **takeaway-of-takeaways** — one sentence the student remembers.
3. Avoid further explanation; let the line stand.
4. Connect explicitly to s5 framing — это closure of arc.
5. Set up s28 (тизер Лекции 5).

**Связь с другими слайдами:** s5 (opens), s24 (frames), s28 (transitions out).

**Risks:** image attribution + no extras.

**Cross-frame anchor:** LO8 + Человек vs AI.

---

### Слайд 28 — Тизер Лекции 5 + домашнее задание (1.5 мин) (`assertion_visual`)

**Описание:** transition к следующей лекции + связь с курсом.

**Содержание (visible):**
- **Тизер:** «Лекция 5: AI в производстве и сельском хозяйстве. Российские данные: Cognitive Agro Pilot — 1500+ машин, +30-40% эффективности. Predictive maintenance, quality control, physical AI.»
- **Course map (visual):** mini-progress bar (4/14 лекций done).
- **Optional homework / call-to-action:**
  - Найти 1 case medical AI in news (Reuters / STAT News / Habr) и apply 4-actor responsibility framework (s24).
- **Closing reminder:** «Семинар sem-04: case-анализ medical AI deployment в Russian context.»

**LO mapping:** LO transition.

**Frame mapping:** All frames carried over.

**Иллюстрация (MANDATORY):**
- **Тип:** mini course-map (progress bar) + small Лекция 5 teaser graphic.
- **Источник:** self-generated layout.
- **Caption:** N/A.
- **Визуальная функция:** continuity курса; expectation-setting.

**Speaker notes hints:**
1. NOT a duplicate of s26 — focus на «что дальше», не «что было».
2. Семинар sem-04 — case study; explicit Russian context.
3. Optional homework — для motivated students; не graded.
4. Avoid extras (no «вы здесь», no «лектору»).
5. 90 sec strict; not the place для new content.

**Связь с другими слайдами:** s26 (3 takeaways), s27 (closing), s29 (Q&A).

**Risks:** none.

**Cross-frame anchor:** Course continuity.

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
| Слайдов | 29 |
| Разделов | 6 (0–5) |
| Время | 9 + 7 + 14 + 14 + 8 + 14 + 6 = 72 мин content + ≈3 мин переходы = ~68 мин + 7 мин буфер = 75 мин |
| Опросы / interactive | s3 (опрос), s4 (reveal), s14 (mid-callback), s19 (micro-exercise — единственное упражнение), s29 (Q&A) |
| Демо | s1 (mosmed.ai OR AlphaFold-server live), s19 (LLM web-chat student-driven) |
| Центральный вопрос | s5 → callbacks s12, s14, s17 → answer s24, s25 → payoff s27 |
| Главный case study | mosmed.ai (s12), DSP-1181 timeline (s17), NEDA Tessa (s22), Obermeyer Optum (s21), Change Healthcare breach (s23) |
| Студенческие упражнения | 1 micro-exercise s19 (per user spec); НЕТ полноценных упражнений |

---

## LO Coverage Matrix

| LO | Заявлен на | Реально работает | Bloom level | Статус |
|---|---|---|---|---|
| **LO1** (Классифицировать типы AI в медицине) | s01, s04, s06, s07, s09, s10, s15, s16, s26 | s06 (4-type matrix), s09 (CV pipeline), s15 (drug discovery pipeline), s26 (takeaway #1) | Understand/Remember + Apply | OK |
| **LO2** (Оценить применимость AI с клиническими данными) | s10, s11, s12, s17, s18, s26 | s10 (sens/spec), s11 (AI vs радиолог), s12 (mosmed concrete), s17 (DSP reality), s19 (apply via micro-exercise) | Apply + Evaluate | OK |
| **LO3** (Проанализировать этический риск ответственности) | s8, s13, s17, s21, s22, s23, s24, s25, s26 | s13 (CV bias), s21 (Obermeyer), s22 (NEDA Tessa), s24 (4-actor framework — CORE), s25 (regulation) | Analyze + Evaluate | OK |
| **LO8** (Сформулировать принципы ответственного использования AI) — **NEW vs L1** | s8, s18, s23, s24, s25, s26, s27 | s24 (4-actor framework), s25 (regulation), s26 (takeaway #3), s27 (closing payoff) | Evaluate + Create | OK |

---

## Frame Coverage Matrix

| Frame | Slides | Slides count |
|---|---|---|
| **LO mapping** | All slides except s2, s3, s28, s29 (template/poll/transition/Q&A) | 25 |
| **LLM pattern** («объясни как студенту») | s19 (CORE), s22 (counterpoint) | 2 (1 CORE) |
| **LLM anti-pattern** (не доверяй медицинским советам) | s13 (CV bias parallel), s19 (CORE), s22 (NEDA Tessa CORE), s24 | 4 (2 CORE) |
| **Другой AI (не LLM)** | s01, s04, s06, s07, s09, s10, s11, s12, s13, s15, s16, s17, s18 | 13 (CORE для разделов 1-3) |
| **Безопасность** | s07 (FDA), s08 (motivation), s12 (medical data), s13 (bias data), s18 (FDA framework), s21 (Obermeyer), s22 (Tessa), s23 (Change Healthcare CORE), s24 (responsibility), s25 (regulation CORE) | 10 (2 CORE) |
| **Человек vs AI** | s03, s05, s08, s10, s11 (CORE), s12, s13, s14, s17, s20, s21, s22, s24 (CORE), s25, s27 (CORE), s28 | 16 (3 CORE) |

**All 6 frames covered, with CORE concentrated в structurally most-important slides.**

---

## Glossary candidates (15-25 терминов для glossary lock после chapter approval)

Это initial список — book-editor может расширить до 25 в Phase 2; orchestrator generates `library/lectures/lec-04/glossary.yaml` после Phase 4 USER GATE.

1. **AI-диагностика (AI-diagnostics)** — применение AI (преимущественно computer vision) для анализа медицинских изображений / сигналов для постановки диагноза.
2. **Drug discovery** — процесс открытия новых лекарственных молекул; традиционно 10-15 лет + $1-2 млрд per approved drug.
3. **Sensitivity (чувствительность / recall)** — доля больных, которых AI определил как больных = TP / (TP + FN).
4. **Specificity (специфичность)** — доля здоровых, которых AI определил как здоровых = TN / (TN + FP).
5. **AlphaFold** — DeepMind модель для prediction 3D-структуры белков (v1 2018, v2 2021, v3 2024); Нобель 2024.
6. **AlphaProteo** — DeepMind модель для design новых protein binders (2024).
7. **FDA AI/ML framework (SaMD)** — Software as Medical Device — категория FDA для software-only medical AI.
8. **Predetermined Change Control Plan (PCCP)** — FDA innovation 2024: vendor pre-declares allowed updates to AI без re-submission.
9. **Computer-aided detection (CADe)** — AI как «вторая пара глаз» для радиолога; формальная FDA category.
10. **Foundation model** — крупная pre-trained модель, fine-tuned для specific задач (e.g., MedCLIP, BiomedCLIP, AlphaFold).
11. **HIPAA** — Health Insurance Portability and Accountability Act (US 1996); защищает PHI.
12. **GDPR** — General Data Protection Regulation (EU 2016/679); защищает personal data including health.
13. **ФЗ-152** — Федеральный закон РФ «О персональных данных» (2006, с поправками); особая категория медицинских данных.
14. **ePHI (electronic Protected Health Information)** — медицинская информация в электронном виде, защищаемая HIPAA.
15. **Деперсонализация (de-identification)** — удаление identifiers, чтобы data не была привязана к конкретному человеку; ≠ anonymization (full removal of re-identifiability).
16. **EU AI Act high-risk** — категория, в которой находится медицинский AI; требует conformity assessment + CE-mark.
17. **mosmed.ai** — российская federated AI-platform для медицинской визуализации, ДЗМ Москвы.
18. **DSP-1181** — первый AI-designed drug (Exscientia + Sumitomo, 2020), для OCD trial.
19. **NEDA Tessa** — chatbot, замещавший human eating-disorder helpline; снят с обращения 2023.
20. **Bias (algorithmic bias)** — systematic deviation в AI output, чаще correlated с защищёнными атрибутами (race, gender, age).
21. **Calibration** — соответствие predicted probabilities реальным частотам; критично для medical AI confidence.
22. **Confidence score** — model-internal output ([0,1]), не Bayesian posterior.
23. **Post-market surveillance** — мониторинг performance AI-медицинского устройства после deployment.
24. **Хосзу-роль (Hospital / clinic operator)** — actor в responsibility framework, ответственный за selection + training + monitoring AI-vendor.
25. **Росздравнадзор + ГОСТ Р 59921** — РФ regulator + серия стандартов «Искусственный интеллект в здравоохранении».

---

## Top 5 Uncertainty Flags (для Phase 0b critique / fact-checker)

| # | Flag | Slides affected | Why critical |
|---|---|---|---|
| 1 | **DSP-1181 текущий статус (CRITICAL)** | s17 | If discontinued → narrative shifts to «marketing promise vs reality»; if continued → different framing. Per user spec — fact-checker must verify NOW. Source: Sumitomo PR + STAT News + Endpoints. |
| 2 | **mosmed.ai 4 млрд руб/год экономии (CRITICAL)** | s5, s8, s12, s26 | Central case для лекции; if cifra wrong → лекция weakens. Source: Vedomosti / Kommersant / ДЗМ Москвы reports. |
| 3 | **FDA AI/ML medical devices count (current)** | s4, s7 | Used 2 раза as evidence для scale; freshness cadence quarterly. Source: FDA.gov AI/ML list. |
| 4 | **AlphaProteo capabilities + публикация date** | s16 | Recent DeepMind work (Sep 2024); may have been superseded by 2026; Source: DeepMind blog + Nature follow-up. |
| 5 | **Exscientia 2025 status (CEO firing, Recursion merger)** | s17 | Recent (2024-2025); status может быть turbulent — verify accurate at lecture date. Source: STAT, Endpoints. |

Дополнительные secondary flags:
- Sensitivity/specificity mosmed.ai (0.94 / 0.89) — verify published source (Morozov et al.?).
- Obermeyer 2019 numbers (26.3%, 84% fix) — verify verbatim.
- Change Healthcare 190M affected + $2-3B cost — quarterly update.
- ГОСТ Р 59921 series — verify standards numbers + dates.
- EU AI Act high-risk medical AI effective date.
- AlphaFold 2M+ users in 190 countries (DeepMind 2024 update).

---

## Notes для следующих фаз (orchestrator pre-USER-GATE walkthrough checklist для GATE 0)

Перед presenting plan-v1 пользователю на USER GATE 0:

### Phase 0a — Methodology critic + reader-text-only (parallel)

1. Methodology-critic проверяет:
   - **Curriculum Relevance Check** (intermediate level = L4): все слайды на уровне Apply/Analyze, не Evaluate/Create.
   - **LO coverage** — LO1, LO2, LO3, LO8.
   - **Sequence** — нет logical jumps.
   - **Assertion-evidence** alignment per слайд.
   - **Term canonical-validity** — нет insider phrasing.
   - **Designer-added content audit** — N/A для plan; check в Phase 5+.
2. Reader-simulator mode=text-only проверяет:
   - Self-containedness каждого слайда (assertion + evidence + visual hint).
   - Reading flow.
   - No orphan references.

### Phase 0b — Fact-checker (parallel with 0a)

1. Verify все 5 top uncertainty flags выше + 6 secondary flags.
2. Generate `freshness-report.md` со списком claims + cadence + verify-on date.
3. Особо: weekly cadence для biotech news (s17), monthly cadence для FDA/regulator updates (s7, s18, s25).

### Phase 0c — Pre-USER-GATE walkthrough (orchestrator self-review)

1. **Visual scan** — для каждого слайда, есть ли concrete illustration source + at least 2 alternatives? Все CAPTIONs present и ≤10 слов?
2. **Frame mapping audit** — все 29 слайдов имеют mapping (LO + frame); CORE concepts концентрированы в structurally-important слайдах (s5, s11, s24, s27)?
3. **Russian context check** — explicit Russian framing в s4 (mosmed), s12 (mosmed CORE), s23 (ФЗ-152, Change Healthcare context for RU), s25 (Росздравнадзор), s28 (Cognitive Agro Pilot teaser)?
4. **Schema readability pre-wireframe required** — для всех schema slides (s6 matrix, s7 timeline, s9 pipeline, s10 matrix, s11 comparison, s15 pipeline, s17 timeline, s18 pipeline, s24 quadrant, s25 comparison) — designer должен sketch ASCII/mermaid wireframe в Phase 5 ДО PowerPoint MCP render. CRITICAL для s10 (matrix), s17 (timeline), s24 (quadrant).
5. **No extras check** — нет «лектору» секций, «вы здесь», тайминг видимый студенту; subtitle только в cover s2; speaker notes derived from chapter+speech, не layout description.
6. **WPM math** — total content time = 68 min; verify per-slide duration sums to 68 (с allowance переходов).
7. **Glossary candidates** — 25 терминов sufficient для intermediate L4; book-editor may extend в chapter Phase 2.
8. **Central question** explicit на s5; returns 3 раза (s12, s14, s17); answer s24-25; payoff s27 — verify нет orphan/missing.
9. **One-slide-one-message** — каждый слайд имеет ОДНО assertion; verify.
10. **Illustrations per slide** — все 29 слайдов имеют illustration entry с at least 2 alternative URLs (per user spec MANDATORY).

### Готовность к Phase 2 (chapter draft)

После USER GATE 0 approval (plan-v1) — book-editor читает plan-v1 + все 11 встроенных «Speaker notes hints» секций + glossary candidates → пишет `chapter.md` (~10k слов). Затем cascade критиков на chapter (methodology + fact-checker + reader text-only) → Phase 4 → USER GATE A (chapter approved) → glossary lock.

---

## Артефакты, создаваемые этим планом (owner: преподаватель + producer agents)

- `library/lectures/lec-04/glossary.yaml` — 15-25 terms (generated после chapter approval Phase 4).
- `library/lectures/lec-04/assets/backup/mosmed-dashboard-screenshot.png` — backup для s01 demo.
- `library/lectures/lec-04/assets/control/s19-baseline-llm-response.png` — lecturer's control AI response для s19 micro-exercise.
- `library/lectures/lec-04/assets/charts/` — self-generated charts (s4 FDA growth, s7 trend, s10 matrix, s11 comparison, s17 timeline).
- `notes/lecture-4-review/citations-audit.md` — после fact-checker Phase 0b.
- `notes/research/lecture-4/medicine-cases.md` — research collection (mosmed, DSP-1181, NEDA Tessa, Change Healthcare, regulation).

---

## Изменения относительно (теоретического) v0

Plan-v1 — это первая версия. Будущие revisions ожидаются после Phase 0a/0b/0c critiques.

---

## Точки выбора (статус)

| Слайд | Что | Выбор | Статус |
|-------|-----|-------|--------|
| 1 | Ice breaker demo | mosmed.ai live OR AlphaFold-server | PROPOSED — needs lecturer choice + freshness verify |
| 5 | Central question | «Какие обещания сбылись + кто отвечает» (B+C blend) | SELECTED with rationale |
| 17 | DSP-1181 narrative | Зависит от fact-check; both outcomes work as narrative | NEEDS FACT-CHECK CRITICAL |
| 19 | Micro-exercise topic | Sens/spec explanation via LLM | SELECTED |
| 24 | Responsibility framework | 4-actor quadrant (Price 2019 + Gerke 2020) | SELECTED |
| 25 | Regulation 3-jurisdiction | US/EU/RU comparison | SELECTED |
| 27 | Closing line | «Врач решает. AI подсказывает. Инженер обеспечивает» | SELECTED |

---

## Следующий шаг

После approve этого plan-v1 (USER GATE 0) — Phase 2 lecture-production pipeline: `book-editor` пишет `chapter.md` (~10k слов, academic), используя plan-v1 + все 11 встроенных speaker notes hints sections + glossary candidates. Затем cascade критиков на chapter (methodology + fact-checker + reader text-only) → Phase 4 (revisions) → glossary lock → USER GATE A.

*Конец plan-v1.*
