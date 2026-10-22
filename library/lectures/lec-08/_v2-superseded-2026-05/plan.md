# Лекция 8 «AI в креативных индустриях и медиа» — Plan v2

**Дата:** 2026-05-20
**Issue:** #119
**Аудитория:** студенты-инженеры 3 курса МГТУ ИУ6 (универсальная, не дизайнеры / не творцы)
**Длительность:** 75 мин
**Source-of-truth (research):** `library/lectures/lec-08/research/2026-landscape.md` + `library/lectures/lec-08/research/2026-russian-context.md`
**Lec-N-1 pattern reference:** `library/lectures/lec-07/` (34 слайдов, 5 разделов + Q&A, keystone в Разделе 0)
**Plan version:** v2 (post USER GATE 0, applies P1/P2 + owner decisions)

---

## 1. Цели и учебные результаты (LO)

Манифест курса (`catalog/manifests/lectures.yaml`): **lec-08 → learning_outcomes: [LO1, LO2, LO4, LO5]**. Семантика LO в курсе сложилась по чтениям предыдущих глав (Лекции 1, 5, 7); унифицированная формулировка для Лекции 8:

- **LO1.** Студент **сможет классифицировать** AI-применения в креативных индустриях по 4 областям (кино/видео, музыка/звук, изображения/дизайн, текст/журналистика) и привести по одному **конкретному инструменту 2026** для каждой (named brand + капабилити-режим). Покрытие: Разделы 0, 1.
- **LO2.** Студент **сможет оценить применимость** AI-инструмента для конкретной creative-задачи, сравнив cost/quality/legal-risk-профиль с не-AI альтернативой (freelance designer, stock photo, voice actor), **опираясь на mental model «как работают 3 семейства генеративных моделей»** (diffusion / latent video transformer / neural audio synthesis). Покрытие: Разделы 0, 1, 2.
- **LO4.** Студент **сможет проанализировать landmark-кейс** (NYT v OpenAI, Andersen v Stability, RIAA v Suno, Arup deepfake $25.6M, SI fake authors) и сформулировать механизм провала + выученный урок для будущих AI-проектов. Покрытие: Раздел 3.
- **LO5.** Студент **сможет сформулировать критерии «здесь AI не нужен»** для creative-проекта (training-data license, output similarity, voice/likeness consent, brand-trust риск) и применить их как чек-лист перед использованием AI-инструмента. Покрытие: Разделы 3, 4, 5.

---

## 2. Keystone axis (ENFORCED)

**«Что AI ДОБАВИЛ → что AI ИЗМЕНИЛ → что AI СЛОМАЛ» — три времени единой оси.**

**Почему именно эта ось.** Для отраслевой лекции про creative tools соблазн читать как «топ инструментов» (Sora 2, Midjourney v7, Suno…) — это превращает лекцию в маркетинговый обзор. Ось «добавил → изменил → сломал» удерживает критический взгляд: каждый класс инструмента сначала появляется как новая capability (добавил), потом меняет экономику и pipeline (изменил), и одновременно создаёт новый класс провалов и юридического долга (сломал). Это ось трёх **времён** одного процесса, а не три параллельные категории — и поэтому она прямо ведёт к ≥30% failure-content без вытаптывания tools-обзора.

**Keystone-слайд:** s05 (после s01 ice-breaker / s02 cover / s03 central question / s04 lecture-map) в Разделе 0.
- Заголовок: **«AI добавил → изменил → сломал»** (про саму ось, не про устройство курса).
- Первая строка: «Три времени одного процесса — каждое поколение creative-инструментов проходит их за месяцы».
- Каждый последующий раздел = мотивированный спуск по оси: Раздел 1 = «добавил», Раздел 2 = «изменил», Раздел 3 = «сломал», Раздел 4 = «отсюда — критерий: где AI не нужен».

**Связь оси с 4 областями (отвечает на P1.3 — explicit relationship).** Эти 4 области (кино/видео, музыка/звук, изображения/дизайн, текст/журналистика) — **НЕ разделы лекции**. Разделы лекции = **времена оси** (добавил / изменил / сломал / отказ / действие). 4 области = **sub-classifier внутри каждого времени**: читать как cross-product **3 × 4 = 12 cells**, где каждая клетка — конкретная capability/case/failure в конкретной области в конкретное время. Например: cell «ДОБАВИЛ × видео» = Sora 2 / Veo 3.1 / Kling 3.0 character cameos (s07); cell «СЛОМАЛ × музыка» = RIAA v Suno (s24); cell «ИЗМЕНИЛ × изображения» = Firefly $400M revenue + Getty/Shutterstock merger (s14/s17). Это **ортогональные таксономии**, не дублирующие друг друга, и student должен видеть их именно так.

**Что НЕ keystone (anti-pattern, ловушка Лекции 4):** s05 НЕ должен быть recap «что было в Лекции 7» или защитой подхода («мы не вводим нового»). Он подаёт ось и ничего больше.

---

## 3. Central question (для s04 lecture-map + s05 keystone)

> **Что AI сделал с creative-индустрией к 2026 году — и где инженеру разумно сказать «здесь AI не нужен»?**

Вопрос двусоставен по проекту. Первая часть («что сделал») разворачивается через keystone-ось ДОБАВИЛ/ИЗМЕНИЛ/СЛОМАЛ. Вторая часть («где сказать нет») — это LO5: чек-лист критериев негативного выбора, который студент уносит из лекции.

**Разграничение функций s04 vs s05 (отвечает на P2.4):**
- **s04 lecture-map** = «вот **6 разделов**» — **горизонталь roadmap** (6 карточек: 0/1/2/3/4/5 + Q&A).
- **s05 keystone** = «вот **ось трёх времён**, по которой эти разделы выстроены» — **вертикаль метафоры** (ДОБАВИЛ → ИЗМЕНИЛ → СЛОМАЛ → отказ → действие).
- Это два разных уровня: s04 — структурный (что-куда-когда), s05 — концептуальный (почему эта последовательность).

---

## 4. Учебная таксономия — 4 области (industry lecture L4+, tools-per-taxonomy ENFORCED)

На каждой ветке таксономии — **named current tools 2026 (вендор-режим, mode ≠ brand)**. Volatile числа/версии → `[VFY-day-of]` на видимом слое, только направления словами.

### 4.1 Кино / видео / VFX
- **Mode:** text-to-video, image-to-video, video-to-video editing, lip-sync, motion mocap
- **Brands 2026:** Sora 2 (OpenAI), Veo 3.1 / Lite (Google), Runway Gen-4.5 + Aleph + Act-Two, Kling 3.0 (Kuaishou), Pika 2.2, Luma `[VFY-day-of для версий]`
- **Adoption-направление:** **production use** (Lionsgate × Runway — pre-viz, storyboards, VFX backgrounds, earnings-call confirmation ноябрь 2024); **hype demo** (большинство social-shorts)
- **Anti-hype:** ELO benchmarks — Kling 3.0 #1, но это качество-в-целом, не «лучший для cinematic-pipeline»; production usage всё ещё ограничен previz и post (не replacement of shoot)

### 4.2 Музыка / звук
- **Mode:** text-to-song (vocals+instrumental+lyrics), voice cloning, multilingual dubbing
- **Brands 2026:** Suno (v5), Udio (Uncharted Labs), Stable Audio 2 (Stability), ElevenLabs v3 + Dubbing Studio `[VFY-day-of]`
- **Adoption-направление:** **production use** для dubbing/localization (ElevenLabs — Deutsche Telekom, Klarna enterprise агенты); **disputed** для consumer music (RIAA litigation 2024–2026)
- **Anti-hype:** «trackable song» ≠ «coherent album»; coherent long-form classical/narrative music — пока человек

### 4.3 Изображения / иллюстрация / дизайн
- **Mode:** text-to-image, image-to-image edit, character consistency, product photography
- **Brands 2026:** Midjourney v7/v8, DALL-E 4 / GPT Image 1.5, Imagen 4 (Google), Flux Pro 1.1 / Flux 2, Adobe Firefly (commercially safe), Stable Diffusion 3.5/4 `[VFY-day-of]`
- **Adoption-направление:** **production use** для product photography (Imagen 4 — пакшоты стекло/металл/жидкости), marketing creative (Adobe Firefly — 22B+ ассетов <2 лет, Deloitte/Tapestry/Paramount+/Pepsi); **под давлением исков** Stable Diffusion (Andersen, Getty)
- **Anti-hype:** «commercially safe» (Firefly) ≠ «legally safe everywhere» — даже Firefly не покрывает trademark/likeness; «character consistency» работает лучше, но multi-scene narrative всё ещё имеет drift

### 4.4 Текст / журналистика / геймдев / реклама
- **Mode:** long-form writing assist, marketing copy, NPC dialogue, ad creative
- **Brands 2026:** ChatGPT, Claude, Gemini (general-purpose); Adobe Firefly + Runway (ad creative) `[VFY-day-of]`
- **Adoption-направление:** **production use** в marketing (87% маркетологов, Salesforce 2026); **rejected** в investigative journalism (NYT/WaPo guidelines — никакого AI для original reporting); **disputed** в game art (Wizards of the Coast vendor policy)
- **Anti-hype:** «AI как стартовая копия» работает для marketing; «AI как replacement автора» — даёт SI fake authors / Amazon sham books scandal

### 4.5 Cross-cutting capability — Real-time / world models
- Genie 3 (DeepMind, 29 янв 2026) — text → playable 3D world, real-time @24 fps, 720p, consistency несколько минут `[VFY-day-of]`
- Это **другой класс**: simulated environment, не video generator. Не для прямого creative output — для интерактивных experiences.

### 4.6 Russian context (L4+ industry — отдельный слайд, см. s10a)
- **Изображения:** Sber Kandinsky 6.0 (28.04.2026 анонс, MoE, бесплатно в GigaChat) + Yandex Шедеврум (YandexART 2.7 / гибрид 3.0) `[VFY-day-of]`
- **Видео:** Kandinsky 5.0 Video (open-source Apache 2.0, 10 сек 768×512); прямого Sora 2 Pro / Veo 3 competitor по длительности/качеству нет
- **Музыка/голос:** Sber SymFormer (entry-level vs Suno v5), SaluteSpeech VoiceCloning, Yandex SpeechKit — функциональны, но ElevenLabs v3 впереди по emotional expressiveness
- **Legal:** Минцифры законопроект 18.03.2026 (TDM-exception для training, обязательная маркировка AI-контента, авторство у промпт-пользователя, в силу с 1 сент 2027) `[VFY-day-of]`
- **Урок:** «local convenience» (бесплатно, RU-промпты, без VPN, рубли, ожидаемый правовой контур), но **НЕ frontier-quality**. Концентрация R&D в US/CN — структурное (capex, доступ к датасетам), не идеологическое.

### 4.7 Платформенный слой (justified rejection of separate slide)

Платформенный слой (Adobe Firefly Foundry — bespoke on-brand модели, Adobe partner-model ecosystem из 12 third-party, Hugging Face Spaces — open demos) **концептуально отделён** от «инструмент для генерации», но **не получает отдельного слайда**: Лекция 8 = L4 industry lecture про **tools/capabilities**, не infrastructure lecture (последнее покрывает **Лекция 3 «Архитектуры AI-систем»**). Платформы упоминаются inline на **s11** (Adobe enterprise logos collage) и устным якорем в speech bridge (Phase-5 anchor flag: «Adobe Firefly Foundry + Hugging Face Spaces — это платформенный слой; архитектурный аспект подробнее в Лекции 3»).

---

## 5. Структура (75 мин = 6 разделов + Q&A)

Lec-07-pattern: 34 слайда (8 в Разделе 0, ~5-7 на каждый из 4 контент-разделов, divider per section, Q&A). Лекция 8 целевая — **39 слайдов** (1 кейс = 1 слайд для navigability — owner decision; компенсация slot'ами s05a fundamentals + s10a Russian, минус s12 + s18 summary).

**Prescription для presentation-designer:** top progress bar — **только на dividers + cover** (Lec-2 anti-pattern: bar на каждом content slide); content slides не получают progress bar.

### Раздел 0. Открытие + keystone (9.5 мин)

- **s01 (3 мин) — ice-breaker live demo.**
  - **Primary (audio-version, owner decision):** Live: открыть https://suno.com/create в браузере, попросить аудиторию накидать 1 промпт (тема + жанр + язык) → сгенерировать трек на месте → проиграть 30 сек. **Hook narrative:** «Вы только что сгенерировали **30-секундный музыкальный трек**. 3 года назад это был студийный композитор + неделя + $500-2000. Сегодня — 30 секунд, 0 музыкального образования, $0 за trial».
  - **Fallback (image-version, если sound в аудитории не работает):** https://firefly.adobe.com — текст-промпт → image за 5 сек. **Hook narrative:** «Вы только что сгенерировали **photoreal изображение**. 3 года назад это freelance designer $50-200 + 1-3 дня; stock photo $25-100 + ограничения license. Сегодня — 5 секунд, 0 designer-навыков, $0 за trial».
  - **assertion:** «AI генерирует production-уровень artefact за секунды без специальных навыков — это новая базовая capability creative-индустрии».
  - **LO:** LO1.
  - **media:** live https://suno.com/create OR https://firefly.adobe.com; fallback PNG в `assets/backup/`.
- **s02 (0.1 мин) — cover.** Title + meta. No media. Background image: Sora 2 sample frame (+media для ≥80% ковеража).
- **s03 (2 мин) — central question.** «Что AI сделал с creative-индустрией к 2026 — и где инженеру разумно сказать "нет"?» Crисp 1 фраза в Ocean rounded box.
- **s04 (1.5 мин) — lecture-map (горизонталь).** 6-card horizontal: Раздел 1 «ДОБАВИЛ» → Раздел 2 «ИЗМЕНИЛ» → Раздел 3 «СЛОМАЛ» → Раздел 4 «Где AI не нужен» → Раздел 5 «Что инженеру делать» → Q&A. Roadmap. Top progress bar на этом слайде (cover-class).
- **s05 (1.4 мин) — KEYSTONE: «AI добавил → изменил → сломал» (вертикаль метафоры).** Большой заголовок про ось. Под ним — 3 timing-полоски: Раздел 1 (новые capabilities) | Раздел 2 (новая экономика) | Раздел 3 (новые провалы и иски). **Это ось, а не recap.** Media: иконография трёх временных столбцов в Ocean palette + 3-icon strip.
- **s05a (1.5 мин) — NEW: «Как работают 3 семейства генеративных моделей медиа».** P1.1 fix. **Это не deep dive, это mental model.**
  - **Diffusion** (Stable Diffusion, Midjourney, Flux, DALL-E, Imagen, Firefly) — **noise → reverse → image**. Объясняет почему «commercially safe» Firefly зависит от **training corpus** (Adobe Stock + licensed), а не от архитектуры.
  - **Latent video transformer** (Sora 2, Veo, Runway) — **latent space + temporal consistency**. Объясняет почему Sora 2 имеет **25-сек предел**: cost scales линейно с latent length, а consistency degrades после ~25 сек generation horizon.
  - **Neural audio synthesis** (Suno, Udio, ElevenLabs) — **autoregressive (для речи/song) vs diffusion (для music)**. Объясняет почему voice cloning возможен из **1 минуты** аудио (fine-tuning, не from-scratch training).
  - **Format на слайде:** 3-card horizontal в Ocean rounded box, по 1 строке-эссенции на семейство + 1 строка «explains-X consequence». Media: 3 schematic diagrams (diffusion forward/reverse arrow, latent space cube, autoregressive waveform).
  - **LO:** foundation для LO2 — без mental model студент не сможет оценить inherent limits.

### Раздел 1. AI ДОБАВИЛ — новые capabilities (12 мин) — LO1, LO2

5-7 слайдов, каждый — конкретная новая capability с named brand + live media. Лёгкие mini-failure-блоки («но это сразу разрушает Y») для распределения failure-share.

- **s06 — divider «AI ДОБАВИЛ» (0.5 мин).** Большое «1» + 6-card progress bar.
- **s07 (2 мин) — Text-to-video поколение 2026.** Sora 2 (25 сек, 1080p, синх. аудио, $0.10/сек 720p `[VFY-day-of]`), Veo 3.1, Kling 3.0 (#1 ELO 1243, 4K, 60 fps `[VFY-day-of]`). Media: embed Sora 2 release reel (https://openai.com/index/sora-2/) + Kling 3.0 sample. Mini-failure: «но 25 сек — это не фильм; cinematic pipeline всё равно собирается из коротких блоков».
- **s08 (2 мин) — Character consistency: cameos & Omni Reference.** Sora 2 character cameos, Midjourney Omni Reference, Runway Director Mode. Media: side-by-side screenshots character-consistency examples из Midjourney showcase.
- **s09 (2 мин) — Voice cloning + multilingual dubbing.** ElevenLabs: voice из 1 мин аудио → 32+ языков; Dubbing Studio 29 языков, сохраняет тон. Media: live https://elevenlabs.io/voice-library — играть 2 sample voices. Mini-failure: «Scarlett Johansson v OpenAI Sky — soundalike тоже создаёт legal risk, не только consent-based cloning» (вход к Разделу 3).
- **s10 (1.5 мин) — Real-time / world models.** Genie 3 — text → playable 3D world @ 24 fps. Media: embed Genie 3 demo (https://deepmind.google/blog/genie-3...). Anti-hype: «это не video generator — это simulated environment; production use пока edge cases».
- **s10a (2 мин) — NEW: Russian context — local convenience vs frontier.** P1 owner decision.
  - **Изображения:** Sber Kandinsky 6.0 (28.04.2026 анонс, MoE, бесплатно в GigaChat без лимита) + Yandex Шедеврум (YandexART 2.7 / Hybrid 3.0 beta февраль 2026, бесплатно из РФ без VPN) `[VFY-day-of]`.
  - **Видео:** Kandinsky 5.0 Video (open-source Apache 2.0, релиз 18.11.2025, до 10 сек 768×512, Video Lite 2B / Video Pro 19B) — нет прямого Sora 2 Pro / Veo 3 / Kling 3.0 competitor по длительности и качеству на 2026-05-20.
  - **Музыка/голос:** Sber SymFormer (Performer-архитектура, 160k треков training, entry-level vs Suno v5) + SaluteSpeech VoiceCloning + Yandex SpeechKit — функциональны для RU TTS, но ElevenLabs v3 впереди по emotional expressiveness.
  - **Legal:** Минцифры законопроект 18.03.2026 (TDM-exception для training, обязательная маркировка AI-контента, авторство у промпт-пользователя при творческом вкладе, в силу с 1 сент 2027) `[VFY-day-of]`.
  - **Урок для инженера:** «local convenience» (бесплатно, RU-промпты, без VPN, рубли, ожидаемый правовой контур) — НО **НЕ frontier-quality** на видео и музыке. Концентрация фронтир-R&D в US/CN — **структурное** (capex десятки тыс. GPU-часов, доступ к большим видео-датасетам), **не идеологическое**.
  - **Media:** side-by-side comparison — Kandinsky 5.0 Video sample frame vs Kling 3.0 sample frame (визуально показывает quality gap по детализации/физике).
- **s11 (2 мин) — Personalisation at scale + workflow примеры.** IAB: 21% live + 20% testing + 25% planning agentic AI video campaigns. Lionsgate × Runway production use (pre-viz, storyboards, VFX). Media: Lionsgate earnings-call quote screenshot + Adobe Firefly enterprise logos collage (mentions: Adobe Firefly Foundry + Hugging Face Spaces — платформенный слой, inline только). Mini-failure: «86% buyers используют, но 40% всех video ads 2026 — AI-generated, и Toys R Us показал что reception ≠ success».
- ~~**s12 — DELETED**~~ (cross-cutting capability summary timeline — methodologically слабее cases, plain summary; deleted per P1 pacing balance).

### Раздел 2. AI ИЗМЕНИЛ — pipeline, экономика, профессии (11.5 мин) — LO2, LO4

5 слайдов. Cost-collapse как главная история; новые профессии vs displaced.

- **s13 — divider «AI ИЗМЕНИЛ» (0.5 мин).**
- **s14 (3 мин) — Cost-collapse по asset-классам.** Таблица из research C.1: 1 image ($50-200 → $0-0.25), 50 product images ($1k-25k → $0-1.5), минута 720p video (~$1k-50k → $6 при Sora 2 standard `[VFY-day-of]`), dub-минута на язык ($50-500 → <$1). Median: **100×–10,000× дешевле**. Media: comparison-bar chart (QuickChart). Failure-mini-block: «дешевле ≠ бесплатно — Adobe Firefly $400M direct revenue 2024-25 показывает, что enterprise commercial-safe всё ещё стоит денег».
- **s15 (2.5 мин) — Скорость: дни → секунды.** Concept art (дни → сек), B-roll (часы → 60 сек), dubbing (недели → минуты ElevenLabs). Media: side-by-side timer-mockup.
- **s16 (2.5 мин) — Новые профессии: prompt engineer / AI director / GenAI workflow specialist.** Upwork 70% YoY рост AI/ML; 52% gross services volume — AI-related; 5.6M independent workers US >$100k/yr в 2025 (vs 3M 2020). Media: Upwork screenshot + категории.
- **s17 (2 мин) — Под удар: graphic designers −17% jobs, stock photographers single digits/мес.** Getty + Shutterstock merger $3.7B январь 2025 — defensive против AI. Shutterstock licensing $104M→$138M→$250M прогноз. Media: bar chart Upwork displacement + Shutterstock pivot. Mini-failure-block для Раздела 3: «consolidation как ответ — но это удар именно по нижнему звену авторов, не по компании-собственнику IP».
- ~~**s18 — DELETED**~~ (adoption metrics summary 4-card strip — methodologically слабее cases; metrics распределяем inline в s11/s14/s16; deleted per P1 pacing balance).

### Раздел 3. AI СЛОМАЛ — основной failure budget (24 мин) — LO4, LO5

**12 кейс-слайдов** (s20-s31 + s19 divider = 13 слайдов). Это **главный носитель failure-content**. Каждый кейс = **конкретный механизм + evidence + implication + "Урок для инженера: 1 фраза" в Ocean rounded box** (P2.1 fix — explicit для каждого s20-s31).

- **s19 — divider «AI СЛОМАЛ» (0.5 мин).**
- **s20 (1.5 мин) — Авторское право: 4 категории исков.** Taxonomy: (1) training data scraping (input), (2) output similarity / memorization, (3) style mimicry, (4) voice/likeness rights. Media: 2×2 матрица в Ocean palette. **Урок для инженера:** «"Авторское право AI" — не один вопрос, а 4 разных категории риска; смотри какая из 4 применима к твоему workflow».
- **s21 (2 мин) — NYT v OpenAI (training+output).** Filed Dec 2023; **20M ChatGPT logs** OpenAI обязан выдать (Bloomberg Law); SJ deadline **2 апр 2026** `[VFY-day-of]`. "Regurgitation" theory. Media: Bloomberg Law headline screenshot. **Урок для инженера:** «Если модель может процитировать твой training corpus verbatim — это не fair use, это infringement evidence; output similarity check обязателен».
- **s22 (2 мин) — Getty v Stability AI (UK loss / US pending).** UK High Court 4 нояб 2025 — Stability **выиграл** primary copyright claims (weights ≠ copy по CDPA); US case MTD 10 фев 2026 `[VFY-day-of]`. Media: Bird & Bird ruling article screenshot. **Урок для инженера:** «Юрисдикции расходятся — то, что legal в UK по CDPA, не legal в US по fair-use; для global deployment проверяй обе».
- **s23 (2 мин) — Andersen v Stability/Midjourney/DeviantArt.** Class action artists; MTD denied Aug 12 (Judge Orrick) → discovery; третий amended 27 фев 2026; **trial 8 сент 2026** `[VFY-day-of]`. Media: docket screenshot. **Урок для инженера:** «Style mimicry "in the style of [named artist]" — не safe just because style не copyrightable; класс actions выживают MTD на DMCA + публичные права».
- **s24 (2 мин) — RIAA v Suno/Udio.** Filed 24 июня 2024. UMG settled Udio 29 окт 2025 (joint platform 2026); Warner license late 2025; **Sony — последний major litigating**; Suno SJ hearing июль 2026 `[VFY-day-of]`. Media: RIAA press release + settlement timeline. **Урок для инженера:** «Lawsuit-driven licensing — actual outcome: 2 из 3 majors settled, лицензируют. Это новый business-model layer, не "all AI music banned"».
- **s25 (2 мин) — Thomson Reuters v Ross — first US ruling REJECTING fair-use.** Feb 2025 Judge Bibas, 2200+ из 3000 headnotes infringed, Warhol v Goldsmith факторы. **⚠ caveat:** Ross — non-generative AI. Applicability to LLM/diffusion — test cases pending. Media: Reed Smith analysis screenshot. **Урок для инженера:** «"Fair use" — не дефолт; LLM/diffusion test cases впереди (NYT, Andersen, Getty US). Не строй product roadmap на assumption fair-use defence».
- **s26 (2.5 мин) — Deepfakes: Arup CFO scam $25.6M.** Hong Kong, январь 2024; deepfake-CFO + colleagues на видеозвонке → 15 транзакций. Engineering firm Sydney Opera House. Media: CNN article screenshot + diagram атаки. **Урок для инженера:** «Видеозвонок ≠ identity proof в 2024+; финансовые транзакции требуют out-of-band verification (callback по known number, multi-factor)».
- **s27 (2 мин) — Korea schoolgirl deepfake crisis (owner decision — include).** >230 Telegram-чатов deepfake-porn из selfies; 6,500 takedowns Jan-Jul 2024 (4× over 2023); 74% подозреваемых 10-19 лет; 793 reported / **only 16 prosecuted** 2021-jul 2024. Media: **NPR headline screenshot** (sensitive — БЕЗ любых deepfake-визуалов, только текст headline + numbers). **Урок для инженера:** «Доступная capability + слабый enforcement = массовый class harm; для consumer-facing AI tools обязателен safety layer (NSFW detection + age verification + reporting pipeline) ещё до launch».
- **s28 (2 мин) — Slop & model collapse.** Shumailov Nature 2024 (vol 631, p 755-759): recursive training на синтетике → деградация + сужение diversity ("MAD"). Конкретный slop: Google AI Overviews — "**put glue on pizza**" (⅛ cup non-toxic glue, Reddit joke source), "**eat at least one rock per day**" (Onion satire). Media: screenshot Google AI Overview результата + Nature paper header. **Урок для инженера:** «Source quality > volume; модель, обучавшаяся на Reddit jokes без filter, проигрывает модели на curated dataset — даже если curated в 10× меньше».
- **s29 (2 мин) — Sports Illustrated fake authors + Amazon Kindle sham books.** SI ноябрь 2023 (Futurism exposé): articles от fake author names + AI-generated profile photos. Amazon 2023-24: **19 из 100 top-bestseller** — actual human writers; остальные — AI-knockoffs (Frank Gioia, Ted Alkyer — fakes реальных jazz figures). Media: Futurism article screenshot + Authors Guild data. **Урок для инженера:** «Legacy trust = key brand asset; AI-pseudonyms разрушают его моментально — если ты публикуешь под именем, имя должно быть реальным человеком или явно AI-disclosed».
- **s30 (1.5 мин) — Coca-Cola + Toys "R" Us — marketing backlash.** Toys R Us sentiment swing **+12.2%→+3.4% positive; 13.5%→53.4% negative**; Joe Russo: "fucking sucks". Coca-Cola повторила AI-ad 2025 несмотря на 2024 backlash. Media: 2 sentiment-bar charts side-by-side. **Урок для инженера:** «AI-ad возможен, но iconic seasonal creative без human leadership = brand damage; brand-trust риск измеряется sentiment swing, не CTR».
- **s31 (1.5 мин) — Displacement consolidated.** Upwork −17% graphic design; income compression (AI detected в 40% работ $10-19/час vs <10% $60+/час); SAG-AFTRA + WGA 2023 — Digital Replicas clause; 2026 4-year extension. Media: 3-stat block. **Урок для инженера:** «Displacement — структурный, не temp shock; clauses помогают, но wage-compression снизу остаётся. Понимай, какой класс labor твой AI-deploy сместит, до launch».

### Раздел 4. «AI здесь не нужен» — критерии негативного выбора (8 мин) — LO5

3-4 слайда. **In-bucket для failure/judgment — это уроки из Раздела 3, переведённые в чек-лист.**

- **s32 — divider «AI здесь не нужен» (0.3 мин).**
- **s33 (2.5 мин) — 4 критерия отказа от AI.** (1) Training data license — нет у tool → юридический долг (Andersen, RIAA precedents); (2) Output similarity check — если outputs могут воспроизвести protected content → liability (NYT regurgitation); (3) Voice/likeness consent — нет → ScarJo-class risk; (4) Brand-trust риск — legacy/iconic creative → backlash (Coca-Cola, Toys R Us, SI). Media: 4-card decision matrix.
- **s34 (2 мин) — Где human только: investigative journalism, original creative direction, long-form coherent narrative.** NYT/WaPo/Reuters guidelines прохибит AI для original reporting. Coherent 50-min album — пока человек. Media: 3-column comparison.
- **s35 (2.7 мин) — YouTube AI thumbnails: 47.3% creators dropped.** Social Blade Creator Survey, Dec 2025. Причины: −22% CTR (creepy smooth skin), −19% CTR (mobile text fail), **−61.8% first-15-sec drop-off** (mismatched promise/content) `[VFY-day-of]`. Media: 3-stat block с numbers. Это empirical end-user rejection — мост к Разделу 5.

### Раздел 5. Что инженеру делать (4 мин) — LO5

2 слайда. Actionable checklist.

- **s36 — divider/takeaway «Чек-лист перед использованием AI в creative-проекте» (0.5 мин).**
- **s37 (3.5 мин) — 5-вопросный чек-лист.** (1) Training-data licensing tool? (Adobe Firefly = да; Stable Diffusion / Midjourney = есть риски); (2) Output similarity check для protected content? (3) Voice/likeness consent если применимо? (4) IP-clean tools для commercial use? (5) Brand-trust риск — legacy/iconic creative? Media: checklist в Ocean rounded box + flowchart decision tree.

### Раздел 6. Q&A + Closing (3 мин)

- **s38 (2.5 мин) — Q&A слайд.** Central question recap + 3 anticipated questions. Media: Ocean rounded box с вопросом + хэштеги тем для дискуссии.
- **s39 (0.5 мин) — Closing/sources.** «В Лекции 9 — AI в авиакосмической отрасли и оборонном комплексе» + источники QR.

**Итого: 39 слайдов, 70 мин на контент + 5 мин buffer = 75 мин (buffer 7% ✓).**

**Slide-count math:**
- Base (plan v1): 39 слайдов
- DELETED: s12, s18 (−2)
- NEW: s05a fundamentals (+1), s10a Russian (+1)
- **Final: 39 слайдов**, нумерация сохранена с letter-suffix для новых (s05a, s10a), gaps для deleted (s12, s18 → не существуют в plan v2).

**Pacing math (sum):**
- Раздел 0 (открытие + keystone + fundamentals): 9.5 мин = s01 (3) + s02 (0.1) + s03 (2) + s04 (1.5) + s05 (1.4) + s05a (1.5) = **9.5 мин** ✓
- Раздел 1 (ДОБАВИЛ): 12 мин = s06 (0.5) + s07 (2) + s08 (2) + s09 (2) + s10 (1.5) + s10a (2) + s11 (2) = **12.0 мин** ✓
- Раздел 2 (ИЗМЕНИЛ): 11.5 мин = s13 (0.5) + s14 (3) + s15 (2.5) + s16 (2.5) + s17 (2) = **10.5 мин** (gap 1 мин для устной связки между cost-collapse и displacement; либо растянуть s17 до 3 мин)
- Раздел 3 (СЛОМАЛ): 24 мин = s19 (0.5) + s20 (1.5) + s21 (2) + s22 (2) + s23 (2) + s24 (2) + s25 (2) + s26 (2.5) + s27 (2) + s28 (2) + s29 (2) + s30 (1.5) + s31 (1.5) = **23.5 мин** ✓
- Раздел 4 (не нужен): 7.5 мин = s32 (0.3) + s33 (2.5) + s34 (2) + s35 (2.7) = **7.5 мин** ✓
- Раздел 5 (что делать): 4 мин = s36 (0.5) + s37 (3.5) = **4.0 мин** ✓
- Q&A: 3 мин = s38 (2.5) + s39 (0.5) = **3.0 мин** ✓

**Sum: 9.5 + 12.0 + 10.5 + 23.5 + 7.5 + 4.0 + 3.0 = 70.0 мин** + 5 мин buffer (Q&A overrun + transitions) = **75 мин ✓ (buffer 7%)**.

---

## 6. Failure-share breakdown (≥30% strict-in, ENFORCED)

**Time-based:**
- Раздел 3 «AI СЛОМАЛ» = **23.5 мин из 75 = 31.3%** — strict-in (каждый слайд — провал + явный «Урок для инженера»).
- Раздел 4 «AI не нужен» = **7.5 мин из 75 = 10%** — strict-in (критерии негативного выбора).
- Раздел 5 чек-лист = **4 мин из 75 = 5.3%** — strict-in (актionable «когда отказаться»).
- Mini-blocks в Разделах 1-2 («но это разрушает Y»): s07/s09/s11/s14/s17 — ~4-5 мин дополнительно, но они **смешанные** (не strict-in по правилу — считаем как out при подсчёте %).

**Strict-in time: 35 мин из 75 = 46.7% ✓**

**Slide-based:**
- Раздел 3: s20-s31 = **12 слайдов** strict-in (divider не считаем).
- Раздел 4: s33-s35 = **3 слайда** strict-in.
- Раздел 5: s37 = **1 слайд** strict-in (s36 — divider).
- **Strict-in slides: 16 из 39 = 41% ✓**

**Word-based (целевой chapter ~10500 слов):**
- §3 «AI сломал» = ~3800 слов (cases + cited механизмы + «Урок» на каждый из 12).
- §4 «Не нужен» = ~1200 слов.
- §5 чек-лист = ~600 слов.
- **Strict-in chapter: ~5600 из ~10500 = 53% ✓**

**Распределение по артефактам (видимо в КАЖДОМ):**
- **Chapter:** §3+§4+§5 = ~5600 слов из ~10500 (≈53%) ✓
- **Slides:** 16 strict-in из 39 (≈41%) ✓
- **Speech:** ~35 мин из 75 strict-in (≈47%) ✓

**Не сконцентрировано в одном артефакте: ✓** (все три ≥31%, разброс 41-53%).

---

## 7. Media plan (≥80% slides с embed, owner-требование ENFORCED)

**Total slides: 39. Target ≥80% = 32+ слайдов с embedded media.**

| Bucket | Слайды | Media-тип | Источник из research |
|---|---|---|---|
| Live demos | s01 | live URL Suno (primary) / Firefly (fallback) | research G.4 |
| Video embed | s07, s08, s10 | Sora 2 reel, Midjourney character showcase, Genie 3 demo | research G.1 |
| Audio embed | s09 | ElevenLabs voice library (https://elevenlabs.io/voice-library) | research G.3 |
| Mental-model schematics | s05a | 3 schematic diagrams (diffusion arrow, latent cube, autoregressive waveform) | derived |
| Russian comparison | s10a | side-by-side Kandinsky 5.0 Video frame + Kling 3.0 frame | RU research |
| Image embed | s11, s14, s15, s16, s17 | Lionsgate quote + Adobe enterprise logos, comparison-bar charts, Upwork screenshots | research G.2 |
| Lawsuit screenshots | s20-s25 | Bloomberg Law, Bird & Bird, Andersen docket, RIAA press, Reed Smith | research C/D |
| Failure-case media | s26 (Arup CNN), s27 (Korea NPR — headline only, sensitive), s28 (Google AI Overview screenshot + Nature header), s29 (Futurism SI + Authors Guild), s30 (Toys R Us sentiment chart) | screenshots + 1-2 generated bar charts | research D.2-D.4 |
| Marketing-backlash | s30 | sentiment chart QuickChart | research C.6 |
| Charts (generated via QuickChart) | s04, s14, s17, s31, s33 | comparison/timeline/displacement | derived |
| **Без media** (dividers + Q&A) | s06/s13/s19/s32/s36 dividers (5), s38 Q&A, s39 closing | text-only Ocean palette | – |
| **Без media count: 7 / 39 = 18%** | | | |
| **С media: 32 / 39 = 82% ✓** | (с background image на s02 cover + s05 keystone 3-icon strip — 33/39 = 85%) | | |

**Fallback strategy для каждого embed:** online URL → clickable hyperlink → QR-код → static PNG в `assets/backup/`. Backup screenshots обязательны для всех live demos.

**Volatile media:** ВСЕ embed media с timestamps / версиями → `[VFY-day-of]` контроль за день до лекции (Sora 2 sample URL может deprecate, Suno UI меняется, Kling release reel может быть обновлён).

---

## 8. Терминология (glossary lock — финализируется после chapter draft)

Ключевые термины (10-15) для lock после Phase 3:

1. **Generative AI (GenAI)** — модели, синтезирующие новый content (image/video/audio/text) из training data.
2. **Foundation model** — общий-purpose модель, fine-tuned под specific задачи.
3. **Text-to-X / X-to-X** — capability-режим (text-to-video, image-to-image edit, video-to-video).
4. **Diffusion model** — класс генеративных моделей: forward process (add noise) + reverse process (denoise → image). Stable Diffusion, Midjourney, DALL-E, Imagen, Firefly.
5. **Latent (video) transformer** — генеративная модель видео в латентном пространстве с temporal-consistency-механизмом. Sora 2, Veo, Runway.
6. **Neural audio synthesis** — autoregressive (для речи/song lyrics) или diffusion (для music) генерация waveform/spectrogram. Suno, Udio, ElevenLabs.
7. **Character consistency** — сохранение визуальных характеристик персонажа через генерации (Sora cameos, Midjourney Omni Reference).
8. **Voice cloning** — синтез голоса конкретного speaker'а из minimal sample (ElevenLabs — 1 мин).
9. **World model** — модель, генерирующая explorable simulated environment (Genie 3), отличие от video gen.
10. **Slop** — низкокачественный AI-generated content, заполняющий platforms (Amazon Kindle, AI Overviews). **Colloquial term** (Bender, Marcus 2024+); academic synonym = «low-quality synthetic content».
11. **Model collapse / MAD (Model Autophagy Disorder)** — деградация качества при recursive training на синтетике (Shumailov Nature 2024).
12. **Deepfake** — AI-generated synthetic media, изображающий конкретного person без consent.
13. **Right of publicity / likeness rights** — право контроля коммерческого использования голоса/образа (ScarJo, SAG-AFTRA Digital Replicas).
14. **Regurgitation** (theory) — memorization модели + воспроизведение training content (NYT v OpenAI центр-аргумент).
15. **Style mimicry** — генерация в стиле named artist (Andersen case центр-аргумент).
16. **Fair use defence** — US legal doctrine для использования copyrighted material; Thomson Reuters v Ross — first US ruling rejecting её в AI-training.
17. **Commercial-safe AI** (Adobe Firefly framing) — обучен на licensed data; vs «scraped-from-web» (Stable Diffusion class).
18. **Synthetic Performers** (SAG-AFTRA clause) — digitally created characters, не identifiable как specific people; regulated.

---

## 9. Cross-references (для post-chapter lock)

- **Lec-1 framing** «где AI работает / где нет» — Лекция 8 углубляет до 4 конкретных критериев negative-choice. (Устный bridge — owner-anchor flag, без слайда.)
- **Lec-3 архитектуры** (агент, RAG, API, платформенный слой) — Лекция 8 на видимый слой не вытаскивает архитектуру; в speech упомянуть Sora 2 / Veo 3.1 как API endpoints + Adobe Firefly Foundry / HuggingFace Spaces как платформенный слой (Phase-5 owner-anchor flag: устный якорь без слайда — justified, см. §4.7).
- **Lec-5 финансы/ритейл AI-failure кейсы (Сбер AI scoring + Klarna ROI provisions)** — Лекция 8 параллелит legal-risk frame: как Сбер AI scoring создаёт risk-debt в финансах, так Stable Diffusion / Midjourney training-data — risk-debt в creative. Параллель в speech bridge при s20 (4-категории исков). P2.7 fix.
- **Lec-7 medical AI 4-actor responsibility framework** — Лекция 8 имеет аналог: ScarJo v OpenAI = artist/likeness owner; Andersen = creator/training-data source; Arup = victim/end-user; Sony v Suno = IP holder. Параллель тонкая — упомянуть в speech, не делать explicit framework на слайде.

---

## 10. Volatile facts to verify day-of (P2.6 fix — был §10 Open questions)

**Все factual claims с timestamps / версиями / numbers требуют day-of verification:**

1. **Sora 2 standalone discontinuation** — research содержит «standalone discontinued март 2026 (PCMag/RedShark)». Если confirmed на дату лекции — упомянуть как урок в s07 / speech bridge («даже OpenAI отказался от consumer-facing standalone product, оставив API → cost story меняется»). Fact-check trigger, не owner-decision.
2. **Suno SJ hearing date** (s24) — заявлено «июль 2026»; verify exact date через RIAA / Patent AI Lab tracker.
3. **Sony litigation status** (s24) — заявлено «last major actively litigating»; verify per latest Music Industry Tracker.
4. **Andersen trial date** (s23) — заявлено «8 сентября 2026»; verify через docket.
5. **Sora 2 / Veo 3.1 / Kling 3.0 / Imagen 4 / Midjourney v7+v8 versions + benchmark numbers** — все volatile, могут update между планом и лекцией.
6. **Kandinsky 6.0 Image announcement date** (s10a) — заявлено «28.04.2026»; verify актуальные бенчмарки vs Midjourney v7/v8 при доступности.
7. **Минцифры законопроект even-of-law date** (s10a) — заявлено «в силу с 1 сент 2027»; verify статус общественного обсуждения / правок.
8. **YouTube AI thumbnails 47.3% drop** (s35) — Social Blade Creator Survey Dec 2025; verify не было ли обновления.
9. **Adobe Firefly $400M revenue + 22B+ assets** — verify последний earnings report (Q4 FY 2025 / новый).
10. **Sora 2 API pricing $0.10/sec** — verify не было ли price drop / hike.

**Owner action (Phase 5 deck-build):** runtime check всех `[VFY-day-of]` в день лекции; substitute «direction words» если specific numbers устарели.

---

## Changelog v1 → v2

**Applied per critic-feedback + USER GATE 0 owner-decisions:**

### P1 fixes (mandatory)
- **P1.1 — Fundamentals slide added.** NEW **s05a** «Как работают 3 семейства генеративных моделей медиа» (1.5 мин), между s05 keystone и s06 Раздел 1 divider. Объясняет diffusion / latent video transformer / neural audio synthesis на mental-model уровне для inженер-аудитории. Без этого LO2 «оценить применимость» недостижим (студент не понимает архитектурную причину границ Sora-25-сек / Firefly commercial-safety).
- **P1.3 — Explicit «3 времени × 4 области» relationship.** §2 (Keystone axis) — добавлен мини-параграф: 4 области = sub-classifier внутри каждого времени; читать как cross-product 3×4 = 12 cells. Примеры cells: ДОБАВИЛ × видео = Sora 2; СЛОМАЛ × музыка = RIAA v Suno; ИЗМЕНИЛ × изображения = Firefly $400M + Getty merger.
- **P1.4 — Justified rejection of infrastructure slide.** §4.7 — explicit обоснование: L4 industry lecture про tools/capabilities, не infrastructure (последнее — Лекция 3). Платформенный слой (Firefly Foundry, HuggingFace Spaces) упоминается inline на s11 + устным якорем в speech bridge.
- **NEW: Russian context slide.** **s10a** в Разделе 1 (после s10 Genie 3) — 2 мин, на основе `2026-russian-context.md`. 4 области (изображения / видео / музыка-голос / legal) + Минцифры законопроект 18.03.2026. Урок «local convenience vs frontier — структурное, не идеологическое». Media: side-by-side Kandinsky 5.0 Video vs Kling 3.0 frame.

### Pacing re-balance
- **s12 DELETED** (cross-cutting capability summary timeline — methodologically слабее cases).
- **s18 DELETED** (adoption metrics 4-card summary — metrics распределяются inline в s11/s14/s16).
- **Net slide count: 39 → 39** (unchanged): −2 (s12, s18) + 2 (s05a, s10a). Total 70 мин content + 5 мин buffer (7% — ≥ recommended 7-10%).
- Numbering: original numbers preserved для diff-readability; new slides с letter-suffix (s05a, s10a); deleted numbers (s12, s18) = gaps в нумерации.

### P2 polish (applied all)
- **P2.1 — Explicit «Урок для инженера» на каждом из 12 case-слайдов s20-s31** (concentrated phrase в Ocean rounded box). Format: assertion + evidence + implication → строка «Урок для инженера: ...».
- **P2.2 — Fallback hook narrative для image-version s01** прописан explicit (audio-version vs image-version, две полные narrative версии).
- **P2.3 — «Slop» colloquial flag в glossary §8** entry #10 (colloquial Bender/Marcus 2024+, academic synonym = «low-quality synthetic content»).
- **P2.4 — s04 lecture-map + s05 keystone разграничены** в §3: s04 = горизонталь roadmap (6 cards); s05 = вертикаль метафоры (ось 3 времён).
- **P2.5 — Top progress bar prescription** в §5: «только на dividers + cover, НЕ на content slides» (Lec-2 anti-pattern).
- **P2.6 — Open Q #5 (Sora 2 standalone) → fact-check trigger.** §10 переписан полностью: «Open questions» → «Volatile facts to verify day-of» (10 items). Sora 2 standalone — fact-check, не owner-decision.
- **P2.7 — Lec-5 financial-failure parallel** добавлен в §9 cross-references (Sber AI scoring → legal-risk frame parallel for s20).
- **P2.8 — Open questions §10 удалены** (все 5 решены через owner-decisions GATE 0): #1 (Suno+Firefly), #2 (Korea включить), #3 (Russian context отдельный слайд s10a), #4 (39 слайдов оставлено), #5 (Sora 2 → fact-check). §10 переименован в «Volatile facts to verify day-of».

### Owner decisions из USER GATE 0
1. **Slide count = 39 detailed** (1 кейс = 1 слайд для navigability) — НЕ consolidate s23+s24, s28+s29; вместо этого удалены s12+s18 summary.
2. **Ice-breaker s01:** Suno primary + Firefly fallback — обе narrative версии прописаны в s01 spec.
3. **Russian context:** мини-блок в Разделе 1, **отдельный слайд s10a** (не footnote).
4. **Korea schoolgirl s27:** включить как слайд с NPR headline screenshot, БЕЗ deepfake-визуалов.

---

**End of plan v2.**
**Next step:** Phase 2 chapter draft (book-editor) → ~10500 слов academic prose с теми же 6 разделами + glossary + 12 case-lessons.
