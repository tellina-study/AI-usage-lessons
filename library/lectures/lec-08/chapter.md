---
lecture: 8
title: AI в креативных индустриях и медиа
version: v3
status: draft
source_plan: plan.md v2
source_research: research/2026-landscape.md + research/2026-russian-context.md
word_count_target: 12000-14500
audience: "студенты-инженеры 3 курса МГТУ ИУ6 (универсальная, не дизайнеры / не творцы)"
date: 2026-05-20
learning_outcomes: [LO1, LO2, LO4, LO5]
references_count: 80+
---

# Глава 8. AI в креативных индустриях и медиа

## Оглавление

- [Учебные цели](#учебные-цели)
- [Центральный вопрос лекции](#центральный-вопрос-лекции)
- [Введение](#введение)
- [Раздел 0. Что генеративные модели медиа делают сегодня](#раздел-0-что-генеративные-модели-медиа-делают-сегодня)
  - [0.1. Три семейства генеративных моделей медиа](#01-три-семейства-генеративных-моделей-медиа)
  - [0.2. Keystone-ось: AI добавил → изменил → сломал](#02-keystone-ось-ai-добавил--изменил--сломал)
  - [0.3. 4 области × 3 времени — cross-product таксономия](#03-4-области--3-времени--cross-product-таксономия)
- [Раздел 1. AI ДОБАВИЛ — новые capabilities](#раздел-1-ai-добавил--новые-capabilities)
  - [1.1. Text-to-video поколение 2026](#11-text-to-video-поколение-2026)
  - [1.2. Character consistency: cameos & Omni Reference](#12-character-consistency-cameos--omni-reference)
  - [1.3. Voice cloning + multilingual dubbing](#13-voice-cloning--multilingual-dubbing)
  - [1.4. World models — Genie 3](#14-world-models--genie-3)
  - [1.5. Personalisation at scale + production use](#15-personalisation-at-scale--production-use)
  - [1.6. Russian context — Kandinsky, Шедеврум, SymFormer, SaluteSpeech](#16-russian-context--kandinsky-шедеврум-symformer-salutespeech)
- [Раздел 2. AI ИЗМЕНИЛ — pipeline и экономика](#раздел-2-ai-изменил--pipeline-и-экономика)
  - [2.1. Cost-collapse 100×–10 000× — таблица по asset-классам](#21-cost-collapse-10010-000--таблица-по-asset-классам)
  - [2.2. Скорость: дни → секунды](#22-скорость-дни--секунды)
  - [2.3. Новые профессии: prompt engineer, AI-режиссёр, специалист по AI-процессам](#23-новые-профессии-prompt-engineer-ai-director-genai-workflow-specialist)
  - [2.4. Displacement: graphic designers, stock, voice actors](#24-displacement-graphic-designers-stock-voice-actors)
- [Раздел 3. AI СЛОМАЛ — провалы и юридический долг](#раздел-3-ai-сломал--провалы-и-юридический-долг)
  - [3.1. Авторское право — taxonomy 4 категорий исков](#31-авторское-право--taxonomy-4-категорий-исков)
  - [3.2. NYT v OpenAI — training + output](#32-nyt-v-openai--training--output)
  - [3.3. Getty Images v Stability AI — UK loss / US pending](#33-getty-images-v-stability-ai--uk-loss--us-pending)
  - [3.4. Andersen v Stability/Midjourney/DeviantArt](#34-andersen-v-stabilitymidjourneydeviantart)
  - [3.5. RIAA v Suno/Udio](#35-riaa-v-sunoudio)
  - [3.6. Thomson Reuters v Ross — first US ruling rejecting fair-use](#36-thomson-reuters-v-ross--first-us-ruling-rejecting-fair-use)
  - [3.7. Deepfake — Arup CFO $25.6M](#37-deepfake--arup-cfo-256m)
  - [3.8. Korea schoolgirl deepfake crisis — class harm](#38-korea-schoolgirl-deepfake-crisis--class-harm)
  - [3.9. Slop & model collapse — Shumailov 2024](#39-slop--model-collapse--shumailov-2024)
  - [3.10. Sports Illustrated fake authors + Amazon Kindle sham books](#310-sports-illustrated-fake-authors--amazon-kindle-sham-books)
  - [3.11. Coca-Cola + Toys "R" Us — marketing backlash](#311-coca-cola--toys-r-us--marketing-backlash)
  - [3.12. Displacement consolidated — clauses + wage compression](#312-displacement-consolidated--clauses--wage-compression)
- [Раздел 4. AI здесь не нужен — критерии негативного выбора](#раздел-4-ai-здесь-не-нужен--критерии-негативного-выбора)
  - [4.1. Четыре критерия отказа](#41-четыре-критерия-отказа)
  - [4.2. Где human только: investigative journalism, original direction, long-form narrative](#42-где-human-только-investigative-journalism-original-direction-long-form-narrative)
  - [4.3. YouTube AI thumbnails: empirical end-user rejection](#43-youtube-ai-thumbnails-empirical-end-user-rejection)
- [Раздел 5. Что инженеру делать — actionable checklist](#раздел-5-что-инженеру-делать--actionable-checklist)
  - [5.1. 5-вопросный чек-лист перед AI в creative-проекте](#51-5-вопросный-чек-лист-перед-ai-в-creative-проекте)
  - [5.2. Mapping чек-листа на 12 кейсов из §3](#52-mapping-чек-листа-на-12-кейсов-из-3)
- [Раздел 6. Закрытие](#раздел-6-закрытие)
- [Глоссарий](#глоссарий)
- [Источники](#источники)
- [Changelog](#changelog)

---

## Учебные цели

После прочтения главы студент:

- **LO1.** Сможет классифицировать AI-применения в креативных индустриях по четырём областям (кино/видео, музыка/звук, изображения/дизайн, текст/журналистика) и привести по одному конкретному инструменту 2026 для каждой (named brand + capability-режим).
- **LO2.** Сможет оценить применимость AI-инструмента для конкретной creative-задачи, сравнив cost/quality/legal-risk-профиль с не-AI альтернативой (freelance designer, stock photo, voice actor), опираясь на mental model «как работают 3 семейства генеративных моделей» (diffusion / latent video transformer / neural audio synthesis).
- **LO4.** Сможет проанализировать landmark-кейс (NYT v OpenAI, Andersen v Stability, RIAA v Suno, Arup deepfake $25.6M, SI fake authors) и сформулировать механизм провала + выученный урок для будущих AI-проектов.
- **LO5.** Сможет сформулировать критерии «здесь AI не нужен» для creative-проекта (training-data license, output similarity, voice/likeness consent, brand-trust риск) и применить их как чек-лист перед использованием AI-инструмента.

---

## Центральный вопрос лекции

> **Что AI сделал с креативной индустрией к 2026 году — и где инженеру разумно сказать «здесь AI не нужен»?**

Вопрос двусоставен по конструкции, и это не случайность. Первая часть («что AI сделал») — диагностическая. К 2026 году generative AI в creative-индустриях прошёл путь от лабораторной демонстрации до индустриальной инфраструктуры: одна Adobe Firefly Foundry сгенерировала свыше 22 миллиардов assets за два года ([Adobe Q4 FY 2025](https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/)), 87% маркетологов используют generative AI хотя бы в одном workflow ([Salesforce State of Marketing 2026](https://www.digitalapplied.com/blog/ai-marketing-statistics-2026-adoption-data-points)), а Hollywood-студия Lionsgate подписала отдельный AI-deal с Runway для производственного pipeline ([Lionsgate Investor Relations, сент 2024](https://investors.lionsgate.com/news-events/news/news-details/2024/Runway-Partners-with-Lionsgate-in-First-of-its-Kind-AI-Collaboration/default.aspx)). Это не футурология; это работающие сегодня системы, которые меняют экономику и pipeline всех четырёх creative-областей одновременно.

Вторая часть («где сказать "нет"») — нормативная, и именно она отличает курс «AI usage» от курса «AI advocacy». К маю 2026 года накопилась критическая масса landmark-провалов — суды, выплаты, brand-damage, фундаментальные ограничения архитектур — которые позволяют сформулировать чёткие критерии отказа от AI в конкретной creative-задаче. Эти критерии — не моралистские лозунги; они дериваты конкретных судебных дел и рыночных провалов. NYT v OpenAI учит проверять output similarity; Andersen v Stability — проверять training-data license; ScarJo v OpenAI Sky — проверять voice/likeness consent; Toys «R» Us Sora-ad — измерять brand-trust риск. На пересечении этих четырёх вопросов — чек-лист, который студент уносит из этой лекции как actionable инструмент.

Эти две части — что AI добавил и куда AI не следует пускать — образуют главную ось этой главы.

---

## Введение

Эта глава — пятая отраслевая в курсе «AI в разных индустриях». Отраслевой блок начинается с Лекции 4 (разработка ПО), проходит через финансы и ритейл (Лекция 5), инженерное проектирование и CAD/CAM (Лекция 6), медицину и фармацевтику (Лекция 7) и сейчас доходит до индустрии с **самым широким публичным contact surface** — creative-сектора. Если ошибка AI в медицинском диагнозе (Лекция 7) — это локальный медицинский incident, а ошибка в финансовом скоринге (Лекция 5) — это локальный финансовый ущерб, то creative AI создаёт публичный, видимый каждому, и юридически связывающий outcome: исполняемый AI-голос Скарлетт Йоханссон, иск Sony Music к Suno на сумму миллиардов долларов, deepfake-CFO забирающий $25.6 миллиона за один видеозвонок, Telegram-чаты с deepfake-порно из selfies одноклассниц. Это значит, что любой инженер, который интегрирует AI в продукт с public face, попадает в эту юридическую и репутационную зону — даже если он формально работает не «в creative-индустрии».

К 2026 году у creative AI есть три важные характеристики, формирующие нарратив этой главы. **Во-первых, это уже инфраструктура, а не футурология.** Sora 2 (OpenAI, сентябрь 2026), Veo 3.1 (Google), Runway Gen-4.5, Kling 3.0 (Kuaishou) генерируют production-ready видео; Midjourney v7+v8, DALL-E 4 / GPT Image 1.5, Imagen 4, Flux 2, Adobe Firefly — генерируют production-ready изображения; Suno, Udio, ElevenLabs — production-ready аудио и голос. Глобальный рынок AI video generators вырос с $716.8M в 2025 до прогнозируемых $847M в 2026 ([Vivideo, 2026](https://vivideo.ai/blog/ai-video-statistics-2026)). **Во-вторых, это поле с измеримой экономической пользой и с измеримым же юридическим долгом.** Adobe Firefly заработал свыше $400M direct revenue в 2024–25 ([Futurum, 2025](https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/)); параллельно — суды на сотни миллионов долларов открыты сразу в трёх категориях контента (текст, изображение, музыка). **В-третьих, это поле с быстро формирующимся правовым контуром.** Минцифры РФ опубликовало законопроект «Об основах государственного регулирования сфер применения технологий ИИ» 18 марта 2026 года ([CNews, 12.03.2026](https://www.cnews.ru/news/top/2026-03-12_v_rossii_razreshat_obuchat)); EU AI Act вступает в силу для GPAI-моделей в августе 2026 года; Thomson Reuters v Ross Intelligence стало первым американским ruling, отвергнувшим fair-use defence для AI-training в феврале 2025 года.

Тон главы — **trust-but-verify**, в той же традиции, что и Лекция 7. Мы не утверждаем, что AI убьёт креативные индустрии — этого не происходит. Мы не утверждаем, что AI — magic bullet — этого тоже не происходит. Мы утверждаем: какие именно capabilities добавились, как они меняют pipeline и экономику, какой юридический долг параллельно накопился, и где инженеру разумно сказать «здесь AI не нужен». После каждого раздела даны вопросы для самопроверки.

Замечание о методике. Эта глава охватывает быстро меняющееся поле: версии моделей, цены API, статусы исков, бенчмарки могут устареть в течение недель. Volatile-факты помечены `[VFY-day-of]` — это контракт для лектора: проверить факт в день лекции и при необходимости заменить «direction word» (например, «уже одобрен» / «ещё в процессе») вместо устаревшей конкретной даты. Stable-факты — исторические инциденты, даты подачи исков, конкретные опубликованные results — без пометки.

---

## Раздел 0. Что генеративные модели медиа делают сегодня

### 0.1. Три семейства генеративных моделей медиа

Прежде чем разбирать индустриальные cases, нужно понимать **архитектурно**, чем именно один генеративный медиа-инструмент отличается от другого. Не на уровне маркетинговых обещаний, а на уровне inherent limits — то есть, какие границы продиктованы самой архитектурой, а не qualifity конкретной реализации. Это критическая mental model для LO2: без неё студент не сможет аргументированно сравнить «можно ли использовать Sora 2 для 90-секундного fashion-видео» или «почему Adobe Firefly считается commercially safe, а Stable Diffusion — нет». Архитектурные семейства в creative AI к 2026 году можно сгруппировать в три ключевых класса.

**Семейство 1: Diffusion models.** Сюда относятся Stable Diffusion 3.5/4, Midjourney v7/v8, DALL-E 4 / GPT Image 1.5, Imagen 4, Flux Pro 1.1 / Flux 2 и Adobe Firefly. Принцип работы: модель учится **обращать процесс добавления шума**. На обучении в изображение последовательно добавляется случайный гауссовский шум до полной деградации; модель учится предсказывать, какой именно шум был добавлен на каждом шаге. На инференсе процесс запускается в обратную сторону: модель стартует с чистого шума и итеративно «удаляет» его, выстраивая изображение, соответствующее текстовому промпту. Detailed техническое объяснение можно прочитать в оригинальной публикации Ho et al. (2020) «Denoising Diffusion Probabilistic Models» и в работе Rombach et al. (2022) «High-Resolution Image Synthesis with Latent Diffusion Models». **Инженерное следствие:** «commercially safe» Firefly зависит **не от архитектуры**, а **от training corpus** (Adobe Stock + licensed content). Архитектура у Firefly та же — diffusion. То, что делает Firefly условно безопасным для commercial use — это **что именно дали модели на обучении**, не **как именно модель устроена**. Это базовое различие, которое прокидывается через всю главу: вопросы copyright — это вопросы про training-data и про output similarity, не про математику архитектуры.

**Семейство 2: Latent video transformers.** Сюда относятся Sora 2, Veo 3.1, Runway Gen-4/4.5, Kling 3.0, Pika 2.2. Принцип работы: видео представляется не как последовательность пикселей-кадров, а как последовательность токенов в **латентном пространстве** — компактном представлении, где каждый токен кодирует пространственно-временной фрагмент. Модель — transformer (как в LLM), но обученный предсказывать следующий video-токен в латентной последовательности с механизмом temporal consistency (то есть, токены, соседние во времени, должны соответствовать друг другу). Техническое описание Sora-class архитектур есть в OpenAI Sora System Card (2024). **Инженерное следствие:** Sora 2 имеет 25-секундный предел не потому, что OpenAI «не доработали», а потому, что **cost scales линейно с latent length**, а **temporal consistency degrades после ~25 секунд generation horizon**. Иными словами, чтобы получить 90-секундное video через Sora 2, нужно генерировать четыре блока по ~22 секунды с дополнительным сшивающим механизмом — это не один model call, это pipeline. Этот fact объясняет, почему cinematic AI-video в 2026 всё ещё собирается из коротких блоков, а не генерируется одним длинным prompt'ом — и почему cinematic pipeline без human direction в production ещё далеко не replacement.

**Семейство 3: Neural audio synthesis.** Сюда относятся Suno (v5.5), Udio, Stable Audio 2, ElevenLabs (v3 + Dubbing Studio). Внутри семейства есть **два суб-типа**:

- **Autoregressive** (для речи и song lyrics) — модель предсказывает следующий аудио-токен (например, mel-spectrogram frame или waveform sample) на основе предыдущих, как LLM предсказывает следующее слово. ElevenLabs использует autoregressive подход для voice cloning.
- **Diffusion** (для music) — аналогично image-diffusion, но в spectrogram domain или в waveform domain. Stable Audio 2 — пример music-diffusion подхода.

**Инженерное следствие:** voice cloning возможен из **1 минуты** аудио, потому что модель не учится «с нуля» голосу — она **fine-tune'ит pre-trained foundation модель** на минимальном sample конкретного speaker'а. Это объясняет, почему voice cloning стал доступной capability в 2024–2026: foundation модель делает 99% работы; sample 1 минуты — это калибровка под конкретный голос. Этот же fact объясняет, почему ScarJo v OpenAI Sky — это не «случайное совпадение тембра», а закономерный artifact доступной capability: голос знаменитости легко имитируется без её прямого участия в обучении модели.

Эти три семейства покрывают подавляющее большинство creative AI-инструментов 2026 года. Когда в следующих разделах мы говорим про конкретный инструмент — Sora 2, Midjourney, ElevenLabs — студент должен уметь сначала задать вопрос: «к какому семейству он относится, и какие inherent limits следуют из архитектуры?» Без этого вопроса оценка применимости (LO2) сводится к маркетинговому копипасту.

### 0.2. Keystone-ось: AI добавил → изменил → сломал

Структура этой главы построена на одной концептуальной оси: **«Что AI ДОБАВИЛ → что AI ИЗМЕНИЛ → что AI СЛОМАЛ»**. Это три **времени** одного процесса, не три параллельные категории. Каждый класс creative-инструмента, появляясь, последовательно проходит все три времени за месяцы.

**ДОБАВИЛ** — момент появления новой capability. Sora 2 добавил text-to-video с синхронным аудио. Midjourney добавил character consistency через Omni Reference. ElevenLabs добавил voice cloning из минимального sample. Genie 3 добавил real-time playable world generation. Это «всё новое» — то, чего раньше технологически не было, а теперь есть.

**ИЗМЕНИЛ** — момент, когда новая capability проникает в существующий pipeline и меняет его экономику. Cost-per-asset падает в 100–10 000 раз. Скорость generation collapses с дней в секунды. Появляются новые профессии (prompt engineer, AI-режиссёр, специалист по AI-процессам) и параллельно вымываются старые (graphic designer −17% jobs, stock photographer single digits/мес). Постепенно производство Lionsgate начинает экономить «миллионы и миллионы долларов» на pre/post-production. Adobe Firefly Foundry становится bespoke модель на корпусе IP клиента, отдельным enterprise-продуктом.

**СЛОМАЛ** — момент, когда возможность создаёт новый класс провалов и юридического долга. Sony Music судится с Suno. New York Times судится с OpenAI за 20 миллионов logs. ScarJo делает publicly выговор OpenAI за soundalike. Arup CFO теряет $25.6M на deepfake-CFO в Hong Kong. Координатор Telegram-чатов сгенерирует deepfake-порно из selfies своих одноклассниц. Sports Illustrated удаляет articles с fake author names и AI-generated profile photos. Coca-Cola получает «soulless» backlash на иконическое Christmas-объявление.

Почему именно эта ось. Для отраслевой лекции про creative tools есть очень сильный соблазн читать её как «топ инструментов 2026» — обзор Sora 2 vs Veo 3.1 vs Kling 3.0, как кто кого превзошёл в ELO benchmark. Такая структура превращает лекцию в маркетинговый sales-brief. Ось «добавил → изменил → сломал» удерживает критический взгляд: каждый класс инструмента сначала появляется как capability, потом меняет экономику, и **одновременно** создаёт юридический и репутационный долг. Это ось трёх времён одного процесса, и поэтому она напрямую ведёт к ≥30% контента про провалы и ограничения, без вытаптывания обзора инструментов.

Эта ось определяет архитектуру лекции: Раздел 1 = «добавил», Раздел 2 = «изменил», Раздел 3 = «сломал», Раздел 4 = «отсюда — где AI не нужен», Раздел 5 = «что делать инженеру».

### 0.3. 4 области × 3 времени — cross-product таксономия

Креативные индустрии в этой лекции мы разбиваем на **четыре функциональные области**: кино/видео/VFX, музыка/звук, изображения/иллюстрация/дизайн, текст/журналистика/реклама/геймдев. Эти четыре области — **не разделы лекции**. Разделы лекции — это **времена оси** (добавил/изменил/сломал/отказ/действие). 4 области — это **sub-classifier внутри каждого времени**.

Иначе говоря, читать структуру нужно как **cross-product 3 × 4 = 12 клеток**, где каждая клетка — конкретная capability/case/failure в конкретной области в конкретное время. Несколько примеров клеток:

| | Кино/видео | Музыка/звук | Изображения/дизайн | Текст/журналистика |
|---|---|---|---|---|
| **ДОБАВИЛ** | Sora 2, Veo 3.1, Kling 3.0, character cameos | ElevenLabs voice cloning, multilingual dubbing | Midjourney character consistency, Imagen 4 product photo | ChatGPT/Claude long-form |
| **ИЗМЕНИЛ** | Lionsgate × Runway production, $9.1B AI-specific video ad spend (subset $80B total) | Universal × Udio joint platform | Firefly $400M revenue, 22B+ assets | 87% маркетологов adoption |
| **СЛОМАЛ** | Toys «R» Us backlash, Coca-Cola «soulless» | RIAA v Suno/Udio, Drake/Weeknd | Andersen v Stability, Getty v Stability | NYT v OpenAI, SI fake authors |

Эта матрица — не academic упражнение. Когда студент в будущем оценивает применимость AI для конкретной creative-задачи, ему нужно уметь локализовать задачу в этой матрице: «моя задача — продуктовая фотография для marketing → это клетка (ИЗМЕНИЛ × изображения) → выученный case — Adobe Firefly + Imagen 4 + commercial-safe pipeline → checklist § 5 включает training-data license». Это и есть применение mental model — не воспроизведение, а навигация.

Замечание: за пределами 4 областей остаётся cross-cutting capability **real-time / world models** (Genie 3), которая не сводится ни к одной из четырёх — это другой класс instrument'а (simulated environment, не video generator). Мы рассмотрим её в §1.4 отдельно.

### Self-check (Раздел 0)

1. К какому семейству генеративных моделей относится Sora 2? Какое инженерное следствие из этой архитектуры объясняет 25-секундный предел длины output?
2. Adobe Firefly использует diffusion-архитектуру, как и Stable Diffusion. Почему один из них считается «commercially safe», а другой — нет? Где именно в архитектуре или pipeline лежит разница?
3. Voice cloning ElevenLabs работает из ~1 минуты аудио. Почему такой минимальный sample достаточен (с архитектурной точки зрения)?
4. Какая клетка cross-product матрицы 3×4 соответствует кейсу «компания хочет сделать AI-генерированную рождественскую рекламу взамен freelance креативной студии»? Какие риски из соседних клеток нужно учесть?

---

## Раздел 1. AI ДОБАВИЛ — новые capabilities

### 1.1. Text-to-video поколение 2026

К маю 2026 года text-to-video перестал быть демонстрационной технологией. Три флагманские модели определяют состояние индустрии: OpenAI Sora 2 (сентябрь 2026), Google Veo 3.1 (2026), Kling 3.0 от Kuaishou (5 февраля 2026). Каждая из них представляет собой production-grade инструмент с разными trade-off'ами по длительности, разрешению, синхронизации audio и стоимости.

**OpenAI Sora 2** [VFY-day-of для версий и цен]. Релиз в сентябре 2026. Максимальная длительность одного клипа — **25 секунд**, разрешение 1080p, синхронное аудио (модель генерирует video + audio одновременно). Архитектурно — latent video transformer (см. § 0.1), с механизмом **character cameos**: персонаж, определённый одним промптом, может появляться в нескольких scene'ах с сохранением visual identity. Цена API — около **$0.10/сек 720p**; Sora 2 Pro — **$0.30–0.50/сек** для 1080p и для длинных контекстов ([Sora 2 API Pricing & Quotas 2026](https://www.aifreeapi.com/en/posts/sora-2-api-pricing-quotas)). Volatile fact: на момент мая 2026 года имеются сообщения о **прекращении поддержки standalone consumer-facing продукта Sora** в марте 2026 года с переключением OpenAI на API-only стратегию ([PCMag/RedShark, март 2026](https://wavespeed.ai/blog/posts/openai-sora-2-complete-guide-2026/)). Если на день лекции этот факт подтверждён, он сам становится инженерным уроком: даже OpenAI отказывается от consumer standalone product для frontier-video, оставляя только B2B API-доступ — что меняет cost story для самостоятельного потребителя.

**Google Veo 3.1 + Veo 3.1 Lite.** Максимальная длительность одного клипа — 4/6/8 секунд (зависит от tier), разрешение 720p или 1080p, native audio (генерируется одновременно с video). Цена API — **$0.05/сек** для Veo 3.1 Lite и **$0.40/сек** для Veo 3.1 Pro (per-second, не per-video; `[VFY-day-of]`, [Veo 3 Pricing 2026](https://www.veo3ai.io/blog/veo-3-pricing-2026)). Поддержка форматов 16:9 (landscape) и 9:16 (vertical/mobile) делает Veo особенно популярным для мобильной рекламы. Подписка Google AI Ultra ($249.99/мес `[VFY-day-of]`) включает Veo + Genie + Imagen в одном пакете.

**Kuaishou Kling 3.0.** Релиз — 5 февраля 2026. Максимальная длительность одного клипа — 15 секунд при **native 4K и 60 fps**. По блайнд-тестам на Video Arena (открытый ELO benchmark для video generation моделей) Kling 3.0 на момент февраля 2026 года занимает **#1 место с ELO 1243**, обгоняя Veo 3.1, Runway Gen-4.5 и Pika 2.2 ([Runway Review 2026, aitoolanalysis.com](https://aitoolanalysis.com/runway-review/); [Kling AI Complete 2026 Guide](https://similevault.com/kling-ai/)). 60 миллионов+ creators, 600 миллионов+ сгенерированных видео — Kuaishou заявляет.

**Runway Gen-4 / Gen-4.5** — четвёртый игрок: длина до 60 секунд, разрешение до 4K, в дополнение к base generation предлагает специализированные инструменты **Aleph** (in-video editor — добавление/удаление элементов внутри сгенерированного клипа) и **Act-Two** (motion capture без специального hardware — мокап из обычного видео). Это позиционирование «не лучший single-shot generator, но самый production-ready toolset для post-production».

**Что значит "production use" в кино-индустрии.** Это **не replacement of shoot**. Это **augmentation pre-production и post-production**. Конкретный landmark — **партнёрство Lionsgate × Runway** (объявлено в сентябре 2024 года, [Lionsgate IR](https://investors.lionsgate.com/news-events/news/news-details/2024/Runway-Partners-with-Lionsgate-in-First-of-its-Kind-AI-Collaboration/default.aspx)). Lionsgate (студия за «Голодными играми», «Saw», «John Wick», большой каталог) предоставила Runway свой корпус IP для обучения custom-модели. Использование — **previsualization, storyboarding, post-production backgrounds, VFX**. На earnings call в ноябре 2024 года Vice Chair Lionsgate Майкл Бёрнс ([Variety VIP](https://variety.com/vip/what-lionsgates-partnership-deal-runway-means-1236151418/)) подтвердил, что AI-pipeline экономит «миллионы и миллионы долларов» на pre/post-production. Critically, никто из заявлений Lionsgate **не говорит, что AI заменил съёмку**. Production кино — это всё ещё actors + cameras + locations; AI augments stages before и after shoot.

**Mini-failure block (входит как mini-failure, но не strict-in для §3 budget):** 25 секунд — это **не фильм**. Cinematic pipeline всё равно собирается из коротких блоков с human direction и continuity-coordinator'ом. Когда **Toys «R» Us** (известный американский ритейлер игрушек, банкротство 2017 года, частично возрождён) попыталась сделать 66-секундный единый Sora-клип для рекламы (**Cannes Lions** — Каннские Львы, крупнейший фестиваль и award-show рекламной индустрии в Каннах, Франция, ежегодно с 1954 года; издание 2024 года), результат вызвал сильный публичный backlash — мы разберём этот case подробно в § 3.11.

### 1.2. Character consistency: cameos & Omni Reference

Одна из самых заметных capability-улучшений 2024–2026 — **character consistency**: способность сохранять визуальные характеристики персонажа (лицо, прическу, одежду, телосложение) через множественные генерации. Это критическая capability для нарратива: без неё AI-video нельзя использовать для multi-scene story.

**Sora 2 cameos.** Механизм: пользователь регистрирует «cameo» — character с определёнными визуальными атрибутами (лицом, голосом, манерой). В последующих video-промптах cameo можно вызвать по имени, и модель воспроизведёт его консистентно. OpenAI заявило о **партнёрстве с Disney** ($1B+ deal) для licensed character generation: Disney IP-character'ы могут официально появляться в AI-сгенерированных видео под лицензией Disney.

**Midjourney Omni Reference (v7).** Аналогичная функциональность для image-generation: один reference-image character'а используется как Omni Reference в последующих промптах для сохранения propertion'ов лица, одежды, посадки. По заявлению Midjourney, character preservation accuracy выросла с ~60% в v6 до >85% в v7 на их internal benchmarks.

**Runway Gen-4 Director Mode.** Полноценный multi-scene scripting: пользователь определяет character'ов, locations, motion patterns как структурированные объекты, и каждая последующая сцена генерируется с этими constants.

**Anti-hype для этой capability.** Character consistency работает **значительно лучше**, чем в 2023 году, но **multi-scene narrative всё ещё имеет drift**: после 5–10 scene'ов мелкие детали (татуировка, шрам, оттенок волос) могут изменяться. Production-grade использование требует continuity-supervisor'а — человека, который проверяет каждую scene на consistency и при необходимости делает re-generation. Это новая профессия (см. § 2.3).

### 1.3. Voice cloning + multilingual dubbing

**ElevenLabs** к 2026 году стал de-facto стандартом для voice cloning и AI-dubbing. Capability: voice clone из **1 минуты** оригинального аудио, говорит на **32+ языках**, сохраняя характеристики голоса (тембр, темп, эмоциональную окраску) ([ElevenLabs Voice Cloning](https://elevenlabs.io/voice-cloning); [ElevenLabs Review 2026, Coval](https://www.coval.dev/blog/elevenlabs-review-2026-voice-cloning-and-synthesis-capabilities-explained)).

**Dubbing Studio.** Production-ready инструмент для локализации long-form видео: 29 языков между любой парой, сохраняет тон, delivery, voice. Long-form видео локализуется за минуты, не недели. До этого product traditional dubbing студия требовала: (1) voice actor, который начитывает скрипт на target-языке; (2) sound engineer для микширования; (3) опционально post-sync editor для синхронизации с губами. Стоимость: $50–500 за минуту dub на язык. ElevenLabs Dubbing Studio: < $1 за минуту на язык, минуты вместо недель.

**Production use в enterprise.** Deutsche Telekom использует ElevenLabs для multi-language customer service agents — один pre-recorded sample CEO, voice-cloned на 30+ языков для регионального communications. Klarna — для autonomous customer-facing AI-agents.

**Mini-failure block.** Voice cloning capability одновременно открывает новый класс юридических рисков. **Scarlett Johansson v OpenAI «Sky»** (май 2024 года) — OpenAI продемонстрировал голос «Sky» в ChatGPT, чрезвычайно похожий на голос Johansson. Johansson ранее (сентябрь 2023) отказалась озвучивать ChatGPT, когда Sam Altman лично обратился к ней; через несколько месяцев OpenAI выпустил «Sky» с голосом, восприятым публикой как её. Johansson выпустила публичное заявление: «I was shocked, angered and in disbelief that Mr. Altman would pursue a voice that sounded so eerily similar to mine» ([Variety, May 2024](https://variety.com/2024/digital/news/scarlett-johansson-responds-shocked-angered-openai-chatgpt-her-1236011135/)). OpenAI убрал голос «Sky» в течение недели; формально иска подано не было. Это **de-facto win для likeness rights**: voice cloning capability обязывает к explicit consent, даже если технологически голос «всего лишь похож». Этот case готовит мост к § 3 — мы разберём другие cases voice/likeness под отдельным углом.

### 1.4. World models — Genie 3

**Google DeepMind Genie 3** (публичный релиз — 29 января 2026 года, [DeepMind Blog](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)) представляет собой **другой класс** инструмента, который часто ошибочно сравнивают с video generators.

**Что делает Genie 3.** Из текстового промпта (например, «средневековый замок на горе, день, лёгкий ветер») модель генерирует **playable 3D world** — explorable, navigable среду в режиме реального времени @ 24 fps, разрешение 720p, consistency сохраняется в течение нескольких минут. Это не sequence пред-определённых кадров (как у Sora/Veo/Runway), это интерактивная среда, реагирующая на действия пользователя (камера, движение, манипуляция объектами).

**Архитектурно** Genie 3 — это совмещение latent diffusion (для visual generation) с world-model-частью, которая обрабатывает state transitions. Доступ — для US-подписчиков Google AI Ultra `[VFY-day-of]`.

**Anti-hype.** Genie 3 — **не video generator**. Это **simulated environment generator**. Прямое production use в creative-индустриях пока edge cases: пара game-studios экспериментирует с Genie 3 для prototyping levels; пара film-studios — для location scouting (генерировать virtual location вместо travel'а к real location); образовательный сектор — для immersive learning environments. Frontier-grade использование в production — впереди, по оценкам индустриальных аналитиков ([Genie 3 World Model 2026, WaveSpeedAI](https://wavespeed.ai/blog/posts/google-deepmind-genie-3-world-model-2026/)).

**Cross-reference к Лекции 3.** Genie 3 — это пример **симбиоза нескольких архитектур** в одном AI-system: latent diffusion (как Sora) + reinforcement-learning state model (как игровой AI) + transformer для language understanding (для обработки промпта). Это иллюстрирует тезис Лекции 3 — что «AI-системы 2026 года» — это композитные архитектуры, не monolithic models.

### 1.5. Personalisation at scale + production use

**Personalisation at scale** — capability, позволяющая каждому клиенту получать собственный ролик / трек / image, адаптированный к profile. До генеративного AI personalisation в creative было ограничено template substitution (e.g., name → видеоролик); сейчас — full re-generation per user.

**IAB 2026 Video Ad Spend Report** ([IAB 2026](https://www.iab.com/news/u-s-digital-video-ad-spend-to-surpass-80b-in-2026/)): среди ad buyers — **21% уже live** с agentic AI для video campaigns, **20% testing**, **25% planning**. US digital video ad spend проектируется свыше **$80B в 2026** (+11% YoY, ~20% быстрее, чем общий ad market) — впервые превышает 60% всего TV/video ad spend.

**Adobe Firefly.** К 2026 году — **22 миллиарда** ассетов сгенерировано за два года; **$400M direct revenue** в FY 2024–25 ([Adobe Q4 FY 2025, Futurum](https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/)). 3x QoQ growth generation в Q4 FY2025. Enterprise users: Deloitte, Tapestry, Paramount+, Pepsi, dentsu, PepsiCo/Gatorade, Stagwell — все production-ready. **Adobe Firefly Foundry** (анонс на Adobe MAX 2025, октябрь) — bespoke модели on-brand, обучаемые на корпусе IP клиента (для marketing-агентств — это критическая capability: модель, гарантированно генерирующая в стиле и tonality конкретного бренда).

**Платформенный слой.** Adobe Firefly — это не только модель, это **платформа**: на ней интегрировано 12 third-party моделей (Veo, Luma, Runway, Topaz) — пользователь Adobe Creative Cloud может выбрать модель под задачу из единого интерфейса. **Hugging Face Spaces** ([huggingface.co/spaces](https://huggingface.co/spaces)) — другой пример платформенного слоя: тысячи public demo'ов image/audio/video gen-моделей в одном месте. Архитектурный аспект платформенного слоя — отдельная тема, подробно покрытая в **Лекции 3 «Архитектуры AI-систем»**.

**Mini-failure block.** 86% buyers используют или планируют GenAI для video creative; **40% всей видеорекламы 2026** — AI-generated ([IAB 2026](https://www.iab.com/insights/video-ad-spend-report-2026/)). Но: Toys «R» Us 2024 Sora-ad показал, что adoption ≠ success. Использование AI **возможно**, но iconic seasonal creative без human leadership даёт brand damage — measurable sentiment swing −10pp (см. § 3.11). 

### 1.6. Russian context — Kandinsky, Шедеврум, SymFormer, SaluteSpeech

Российский landscape generative AI к 2026 году функционален, но не frontier по большинству областей. Ключевые игроки:

**Изображения.**

- **Sber Kandinsky 6.0 Image** — анонс **28 апреля 2026** года ([SHADR, 29.04.2026](https://www.shadr.info/news/2026/04/29/36773-sber_predstavil_kandinsky_60_image_flagmanskuyu_model_dlya_/), [4PDA, 28.04.2026](https://4pda.to/2026/04/28/455813/)). Архитектурно — Mixture-of-Experts (MoE); работает по заявлению Сбера «до двух раз быстрее» предыдущих версий. Новые функции: реставрация, нейрофотосессии, смена одежды и локаций, ретушь и макияж. **Бесплатный доступ** через ассистент GigaChat без лимита генераций. `[VFY-day-of для точных бенчмарков vs Midjourney v7/v8 — независимые head-to-head не публиковались на 2026-05-20]`.
- **Kandinsky 5.0 Video** — релиз **20 ноября 2025** года. Открытые веса под Apache 2.0; две версии — Video Lite 2B и Video Pro 19B. Длительность до 10 секунд при 24 fps, разрешение 768×512. Video Lite декларирует #1 место среди open-source моделей своего класса по «пониманию русских концептов» ([GitHub kandinskylab](https://github.com/kandinskylab/kandinsky-5)).
- **Yandex Шедеврум** — YandexART 2.7 / гибрид 3.0 (beta, февраль 2026). Видео — 4 модели (v.1 / v.2 Beta / v.3 / Wan 2.2 от Alibaba); v.3 — самая детализированная (4 сек × 24 fps, форматы 16:9 / 9:16 / 1:1); гибрид 3.0 декларирует 5-секундные ролики с «физически корректным движением». Доступ — iOS + Android + web, бесплатно без VPN из РФ; с 3 марта 2026 — API через Yandex Cloud + AI Studio. MAU Шедеврум >5M, FusionBrain.ai (Sber-портал Kandinsky) >2M monthly users в Q1 2026 `[VFY-day-of]`.

**Видео — frontier gap.** Прямого конкурента Sora 2 Pro / Veo 3.1 / Kling 3.0 по длительности (15–60 сек), разрешению (1080p+), физике и audio-синху в РФ к 2026-05-20 **не подтверждается**. Объяснение **структурное, не идеологическое**: фронтир-видео-модели требуют capex — десятки тысяч GPU-часов в кластере — и доступа к большим лицензированным видео-датасетам. Концентрация R&D — в US (OpenAI, Google DeepMind, Runway) и Китае (Kuaishou Kling, MiniMax Hailuo, Alibaba Wan). Это объективное распределение capex и data access на момент 2026 года.

**Музыка / звук.**

- **Sber SymFormer (Маэстро)** — генератор музыки на базе архитектуры Performer (variant transformer), обучен на 160 тысячах композиций; результат — mp3 за < 1 минуты, через ассистентов «Салют» и «Звук Студио». Sber выпустил с её помощью альбом «Thriving Machine» (15 треков) под open license ([Sber Developers SymFormer](https://developers.sber.ru/portal/products/symformer); [Habr Sber](https://habr.com/ru/companies/sberdevices/articles/826118/)). **Уровень — entry-level vs Suno v5.5 / Udio v2**: треки короче, вокал ограниченный, длинная narrative composition не достижима.
- **Прямого RU-конкурента Suno уровня v5.5 нет.** Российские «решения» — это **агрегаторы-прокси** (GPTunneL, Chad AI, GenAPI, Sonata-бот) с оплатой в рублях, обёрнутые поверх Suno API. То есть RU-аудитория всё равно потребляет западный frontier через локальные wrapper'ы.
- **Sber SaluteSpeech YourVoice** — voice cloning от нескольких часов аудио (vs ElevenLabs — 1 минута); VoiceCloning — секунды; поддержка SSML, RU/KZ/EN. **Yandex SpeechKit** — функциональный TTS. Оба — production-ready для российских TTS-задач, но **emotional expressiveness и «character voices» уступают ElevenLabs v3**.

**Legal — Минцифры законопроект 18 марта 2026.** «Об основах государственного регулирования сфер применения технологий ИИ». Общественное обсуждение до 15 апреля 2026; план вступления в силу — **1 сентября 2027** `[VFY-day-of для статуса]`. Ключевое для медиа: (1) **TDM-exception** — обучение моделей на правомерно полученных опубликованных произведениях не нарушает авторское право (аналог японского Article 30-4); (2) **обязательная маркировка** ИИ-сгенерированного фото / видео / аудио; (3) **авторство** на ИИ-результат принадлежит **пользователю промпта**, внёсшему творческий вклад. Это контрастирует с EU AI Act (август 2026), который не легализует TDM, но требует respect copyright opt-outs ([CNews, 12.03.2026](https://www.cnews.ru/news/top/2026-03-12_v_rossii_razreshat_obuchat); [РИА Право](https://riapravo.ru/intellekt/avtorskoe-pravo-i-ii-v-2026-godu-revoljuciya-zakonodatelstva-i-novye-riski/)).

**Landmark RU-cases.** Публично подтверждённого аналога Getty v Stability или NYT v OpenAI против Kandinsky / Шедеврум на 2026-05-20 **нет**. Иски возможны после **1 сентября 2027 года**, когда вступит в силу правовой контур.

**Урок для инженера.** RU GenAI для медиа в 2026 — это **«local convenience»**: бесплатность, RU-промпты, доступ без VPN, оплата в рублях, прогнозируемый правовой контур. Но **НЕ frontier-quality** на видео и музыке. Где задача — быстрый masstige-контент или маркетинговый visual на русском с гарантированным правовым контуром — Kandinsky 6.0 / Шедеврум конкурентоспособны; где нужны cinematic video, профессиональный вокал, character consistency — выбор остаётся за Sora 2 / Veo 3.1 / Kling 3.0 / Midjourney / Suno. Это сам по себе **honest takeaway**: концентрация фронтир-R&D в US/CN — **структурное** (capex, доступ к датасетам), не идеологическое.

### Self-check (Раздел 1)

1. Sora 2 имеет 25-сек предел, Kling 3.0 — 15 сек, Runway Gen-4 — до 60 сек. Какие архитектурные / экономические факторы определяют эти лимиты? Объясните через семейство latent video transformer (§ 0.1).
2. Lionsgate × Runway партнёрство — это пример какой части creative pipeline под AI? Какие этапы pipeline остаются human-only по сей день?
3. ScarJo v OpenAI «Sky» формально не суд (иска подано не было), но эпизод считают **de-facto win для likeness rights**. Объясните, почему.
4. Российский AI-видео gap vs Sora 2 / Veo 3.1 / Kling 3.0 — это **структурное** или **идеологическое** ограничение? Какие конкретные факторы определяют разрыв?

---

## Раздел 2. AI ИЗМЕНИЛ — pipeline и экономика

### 2.1. Cost-collapse 100×–10 000× — таблица по asset-классам

Главное экономическое изменение, которое AI принёс в creative-индустрии — это **catastrophic collapse cost-per-asset**. Это не «AI чуть-чуть дешевле»; это два-четыре порядка cheap'е, в зависимости от asset-класса. Эта таблица — **критически важный** инструмент для применения LO2:

| Asset | До (human/stock) | После (AI generation) | Множитель |
|---|---|---|---|
| 1 image (illustration / concept) | $50–$200 freelance designer, $50–$500 stock | **$0–$0.25** | **200×–10 000×** |
| 50 product lifestyle images | $1k–$5k freelance / $5k–$25k full photography / $50–$500 stock | **$0–$1.50** | **>1 000×** |
| 1 минута 720p видео | $1k–$50k (shoot + post-production) | **~$6** (Sora 2 standard, 60s × $0.10) `[VFY-day-of]` | **150×–8 000×** |
| 1 минута 4K видео | (большой бюджет $10k+) | Kling 3.0 / Veo Ultra (включено в подписку) | **>1000×** |
| dub минуты видео на 1 язык | $50–$500 (voice actor + studio + sync) | <$1 (ElevenLabs subscription) | **50×–500×** |

Источник cost-collapse оценок — [ZSky AI](https://zsky.ai/blog/how-much-does-ai-art-cost) и [ImagineArt](https://www.imagine.art/blogs/ai-image-generation-cost) для image; [Sora 2 API Pricing Calculator](https://costgoat.com/pricing/sora) для video; [ElevenLabs pricing](https://elevenlabs.io/) для audio; диапазоны human costs — индустриальные benchmarks Upwork / Fiverr / Shutterstock.

**Что эта таблица не означает.** Она **не означает**, что creative industry «потеряет $1 000× работ». Она означает, что **marginal cost** генерации artefact'а упал на 2–4 порядка, но: (а) value-add от human direction / curation / brand-alignment **не упал**; (б) **enterprise commercial-safe** генерация всё ещё стоит денег — Adobe Firefly $400M direct revenue в 2024–25 показывает, что licensed corpus + workflow + integration — это полноценный enterprise SaaS-стек, не «бесплатное добро».

**Что эта таблица означает.** **Bottom-of-market** (commodity creative — stock images, basic illustrations, generic B-roll, simple voiceovers) — это рынок, исчезающий как separately professionally-priced category. AI generates это за минуты по $0–$1.50. **Top-of-market** (iconic creative direction, original brand campaigns, complex multi-scene narrative) — это рынок, где human leadership остаётся mandatory.

**Adobe Firefly $400M revenue per year** — это эмпирическое доказательство, что middle-tier (commercial-safe production-grade generation) — отдельный, быстро растущий сегмент, не bottom-of-market.

### 2.2. Скорость: дни → секунды

Cost-collapse сопровождается **collapse скорости**. Это второй экономический фактор, отдельный от cost.

- **Concept art draft** (для game-dev, фильма, рекламы) — традиционно дни freelance designer'а или штатного концепт-художника. Через AI: **5–60 секунд** prompt-to-pixel в Midjourney / Imagen 4 / Flux 2.
- **B-roll кадр** (filler для документального / маркетингового видео) — традиционно часы съёмки + post-production, либо $10–$100 за минуту через stock footage providers. Через AI: **5–60 секунд** через Veo 3.1 / Sora 2.
- **Dubbing long-form видео на target-язык** — традиционно недели студийной работы. Через AI (ElevenLabs Dubbing Studio): **минуты**.
- **Concept exploration** в дизайне (3–5 вариантов главной идеи для презентации клиенту) — традиционно полу-неделя дизайна. Через AI: **минуты** на десятки вариантов.

**Инженерный урок.** Скорость collapse меняет cycle time на каждой стадии creative pipeline. Раньше клиент видел первый concept через неделю; теперь — через минуты. Это не просто экономия — это **изменение шаблона работы**. Iteration loop становится 10–100× плотнее. Это, в свою очередь, требует новых навыков от человека в loop'е: умения формулировать критерии «годен / не годен» быстрее, потому что новых вариантов появляется больше.

### 2.3. Новые профессии: prompt engineer, AI-режиссёр, специалист по AI-процессам

Cost + speed collapse создал **новые рыночные роли** в creative-индустриях. Эти роли — не «AI заменил designer'а», они **между** AI-инструментом и финальным client deliverable.

- **Prompt engineer / AI artist** — специалист, формирующий промпты и постобработку для получения production-ready output из generative модели. Существует как отдельная категория на Fiverr / Upwork; стартовые ставки на Upwork по этой категории $25–$80/час (2026 данные).
- **AI-режиссёр / AI-музыкальный продюсер** — supervisor model output, доводящий до production-ready через iterations, post-processing, мультимодальную интеграцию. Аналог художественного директора, но для AI-pipeline.
- **специалист по AI-процессам** — интегратор AI-инструментов в существующие production-pipeline студий (например, делает Lionsgate / Adobe Firefly Foundry integration для marketing-агентства).
- **супервайзер континьюити** — относительно новая роль (см. § 1.2): человек, проверяющий character / scene continuity через AI-generated multi-shot sequences.

**Метрики роста.** [Upwork 2025–2026 internal data](https://www.upwork.com/resources/will-ai-replace-graphic-designers): **70% YoY рост AI/ML subcategory** на Upwork. **52% gross services volume growth** — AI-related. По отчётам Upwork и MBO Partners, **independent workers с AI/ML skills получают premium-rates** относительно общего рынка фриланса (specific numbers per year volatile — см. Upwork annual report для актуальной цифры на день лекции).

**Что значит «новые профессии».** Это **не миллион новых дизайнеров**. Это специализированный класс работников между AI-инструментом и client deliverable. Они **необходимы**, потому что raw AI output ≠ production-ready output: нужен curation, post-processing, brand-alignment, legal review. Этот класс растёт быстро, но он **меньше** displaced класса (см. § 2.4).

### 2.4. Displacement: graphic designers, stock, voice actors

Параллельно с появлением новых профессий идёт **displacement старых**. Это не дискуссионная гипотеза — это уже измеримый процесс с конкретными цифрами.

**Graphic designers — Upwork.** **−17.01% jobs** в graphic design category на Upwork после релиза основных GenAI image tools (Midjourney v6, DALL-E 3, Stable Diffusion XL) ([Jobbers Displacement Index](https://www.jobbers.io/ai-job-displacement-index-which-freelance-skills-are-at-risk/)). Income compression: AI detected в **40% работ writers, оплачивающих $10–19/час**, vs **<10% в работах $60+/час**. Иначе говоря, **wage compression снизу**: AI-инструменты вымывают именно низкобюджетный freelance, оставляя нетронутыми high-value specialty roles. Это структурно важно: классическое предсказание «AI augments human professionals» работает только для middle-/high-tier; bottom-tier — это displacement, не augmentation.

*Типичный профиль wage compression снизу выглядит так.* Иллюстратор-фрилансер, 5 лет опыта, специализация — концепт-арт для инди-игр и маркетинговых иллюстраций. До 2023 года средняя ставка — $40/час (Upwork, USD). После широкого внедрения GenAI image tools в брифы клиентов (Midjourney + DALL-E + Stable Diffusion XL стали стандартным «первый драфт за 30 минут» tool'ом маркетологов), сценарий меняется: клиент приходит с уже сгенерированным AI-набором концептов, просит «доработать», и ставка падает до $18–22/час (post-AI uplift, но pre-AI rate). Это **не уникальный отдельный случай** — это типичный pattern, observed на сотнях Upwork-профилей в 2024–25 годах. Top-tier illustrators ($80+/час) с brand-name портфолио и established clients остаются без compression; bottom-tier ($15–30/час, commodity work) — полностью displaced; middle-tier — squeezed.

**Stock photographers.** Shutterstock contributors с **сотнями photo-uploads в месяц** (среднестатистический stock photographer середины 2020s) ушли к **single digits в месяц** на microstock-форумах ([Tidewater Teddy, январь 2025](https://tidewaterteddy.com/2025/01/10/stock-photography-is-dying/); [Kaptur — Silent collapse](https://kaptur.co/the-silent-collapse-generative-ais-erosion-of-photo-licensing-revenue/)). Getty Creative segment revenue упал на **−5% YoY 2024**.

**Voice actors.** **SAG-AFTRA** (Screen Actors Guild – American Federation of Television and Radio Artists — крупнейший актёрский профсоюз США, ~160 тысяч members) strike 2023 (14 июля – 9 ноября 2023) был мотивирован прямо AI-displacement рисками: voice actors требовали contractual protection от использования их голоса для AI-cloning без consent. Параллельно ElevenLabs adoption в enterprise drove массовое displacement Korean / global voice actors для commodity-dubbing.

**Industry consolidation как ответ.** **Getty + Shutterstock merger** — объявлен **январь 2025**, deal value **$3.7B**, ожидаемая экономия **$150–200M** в течение 3 лет ([Kaptur — Authenticity cartel](https://kaptur.co/the-authenticity-cartel-why-the-getty-shutterstock-merger-is-really-about-who-controls-real/)). Это defensive consolidation против AI disruption: два крупнейших стоковых providers объединились, потому что separately они не могут противостоять cost-collapse. Параллельно **Shutterstock licensing к AI companies** — $104M в 2023 → $138M в 2024 → ~$250M прогноз 2027. Это **pivot**: Shutterstock перестаёт зарабатывать на продаже photos фотографам и переходит на продажу данных AI-компаниям. Для photographers это структурно негативно — они перестают быть customer'ом, они становятся source data.

**Hollywood: SAG-AFTRA + WGA AI clauses.** Главный коллективный ответ creative-индустрии на AI-displacement — **AI-clauses в коллективных контрактах**, завоёванные **WGA** (Writers Guild of America — профсоюз сценаристов США) + SAG-AFTRA strikes 2023 года. WGA strike — 2 мая 2023 – 9 ноября 2023; SAG-AFTRA — 14 июля – 9 ноября 2023 ([Perkins Coie analysis](https://perkinscoie.com/insights/blog/generative-ai-movies-and-tv-how-2023-sag-aftra-and-wga-contracts-address-generative)).

Завоёванные AI-clauses:

- **Digital Replicas (likeness):** требуется informed consent + compensation для использования образа реального performer'а в AI-generated content.
- **Synthetic Performers:** AI-generated characters, не identifiable как specific people — регулируются (например, нельзя выпустить synthetic performer'а, который заменяет реального performer'а в сцене без compensation).
- **WGA-side:** AI generated material не может «выпустить» writer'а из credit, не может быть source material для написания скрипта без disclosure.

**2026 negotiations.** SAG-AFTRA + WGA подписали **4-year extension** с **AMPTP** (Alliance of Motion Picture and Television Producers — торговая организация студий) в 2026 ([2026 WGA & SAG-AFTRA Negotiations, No Film School](https://nofilmschool.com/2026-wga-contract-negotiations)) — это гарантирует no-repeat strike в 2026/2027/2028. WGA push for **expanded AI protections** — добавлены clauses про AI training data disclosure и про opt-out для writers, не желающих иметь свои scripts в training corpus.

**Что эти clauses не покрывают.** Они **не покрывают** displacement лучше всего оплачиваемых hollywood-роли (top-tier writers, A-list actors) — эти роли защищены contract'ами. Они **не покрывают** bottom-tier freelance / B-roll-actors / extras / commodity voice work — этот рынок продолжает сжиматься. **Wage compression снизу — структурный, не временный shock.**

**Income data — confirmation структурного displacement.** [Jobbers Displacement Index](https://www.jobbers.io/ai-job-displacement-index-which-freelance-skills-are-at-risk/) фиксирует: 40% работ Upwork writer'ов в категории $10–19/час — содержат AI-detected output (т.е. эти задачи реально выполняются AI); в категории $60+/час — менее 10%. Это говорит, что AI не заменяет premium expertise — он **сжимает рынок** до того, что bottom-tier работы перестают быть отдельной рынка (выполняются in-house через AI), а сверху концентрируется high-value direction.

**Урок для инженера.** Если ты разрабатываешь AI-инструмент, который deploys в creative-индустрию, проанализируй, **какой именно класс labor** твой инструмент displace. Если bottom-tier commodity work (stock images, basic voiceovers, generic B-roll) — это уже происходит, и это «легально» в смысле labor law, но создаёт ESG / regulatory pressure (см. EU AI Act trans-parency for GPAI in 2026). Если top-tier creative direction — это **не получится**; именно эта зона защищена value-add от human curation.

### Self-check (Раздел 2)

1. Cost-collapse 100×–10 000× — это **полное замещение** или **сегментация рынка**? Объясните, почему Adobe Firefly $400M revenue per year существует на фоне «AI generates images за $0».
2. **Wage compression снизу** — это какой именно механизм? Почему bottom-tier freelance вымывается, а top-tier остаётся (с конкретными % из Jobbers Index)?
3. Getty + Shutterstock merger ($3.7B, январь 2025) — defensive ответ на AI disruption. Назовите второй наблюдаемый pivot Shutterstock (что компания перестаёт продавать и что начинает).
4. SAG-AFTRA Digital Replicas clause — какую конкретно проблему решает? Назовите два примера ситуации, когда clause применяется.

---

## Раздел 3. AI СЛОМАЛ — провалы и юридический долг

### 3.1. Авторское право — taxonomy 4 категорий исков

Парадигма «AI vs copyright» — это не **один** юридический вопрос, а **четыре разных категории исков**, с разной правовой логикой, разными прецедентами, разными outcome'ами. Инженер, оценивающий AI-инструмент для creative-задачи, обязан понимать, в какую из четырёх категорий попадает его workflow, чтобы корректно оценить risk-профиль. Этот пункт даёт **чистый primer таксономии** — определения четырёх категорий без разбора cases. Конкретные landmark-cases каждой категории мы разберём в §3.2-§3.6 (copyright) и §3.7-§3.8 (voice/likeness).

Кратко о юридических терминах, которые встретятся ниже:

- **fair-use defence** — доктрина «добросовестного использования» (US, Section 107 Copyright Act); 4-factor test: (1) purpose & character of use; (2) nature of copyrighted work; (3) amount & substantiality used; (4) effect on market.
- **DMCA** = Digital Millennium Copyright Act (закон США 1998 года об авторском праве в цифровой среде).
- **CDPA** = Copyright, Designs and Patents Act 1988 (UK-аналог US copyright).
- **right of publicity** — право контроля коммерческого использования голоса / образа конкретного человека.
- **class action** — коллективный иск, в котором один или несколько истцов выступают от имени группы (class) лиц с аналогичными правовыми требованиями.

**Категория 1: Training data scraping без лицензии (input side).** Иски фокусируются на том, что AI-компания собрала training corpus, включая copyrighted работы, **без лицензии правообладателей**. Theory of harm — **сам факт включения protected work в обучающий датасет — нарушение**. Outcome зависит от того, признаёт ли суд training «fair use» (US) или его аналоги в других юрисдикциях.

**Категория 2: Output similarity / memorization (output side).** Иски фокусируются на том, что **AI воспроизводит copyrighted material в output'е** (model memorize и regurgitate training content). Theory of harm — не способ обучения, а способность модели вернуть protected content при правильном prompt. Outcome зависит от того, насколько эффективен output-similarity check у defendant'а.

**Категория 3: Style mimicry.** Иски фокусируются на **способности генерировать в стиле конкретного artist'а** (часто через prompt «in the style of [named artist]»). Theory of harm — style сам по себе традиционно **НЕ охраняется copyright**, но class action может расширить защиту через DMCA + публичные права + commercial substitution argument. Outcome — открытый юридический вопрос на 2026 год.

**Категория 4: Voice / likeness rights (right of publicity).** Иски фокусируются на **праве контроля коммерческого использования голоса / образа конкретного человека**. Theory of harm — даже «soundalike» или «лик-alike» без direct cloning может создавать right-of-publicity risk. Outcome — частично settled через collective-bargaining (SAG-AFTRA), частично через federal bills (No AI FRAUD Act), частично через criminal law (EU deepfake-porn).

**Урок для инженера.** «Авторское право AI» — не один вопрос, а **четыре разных категории риска**. До выбора tool — определи, какие категории применимы к твоему use case, потому что **mitigation для каждой разная**: license check (категория 1) ≠ output similarity audit (категория 2) ≠ style-mimicry prompt restrictions (категория 3) ≠ consent management (категория 4). Если в твоём workflow incoming risk попадает в несколько категорий — суммируй mitigation-чек-листы, не выбирай один.

**Cross-reference к Лекции 7.** Эта taxonomy 4 категорий имеет тонкий параллель с **4-actor responsibility framework** из Лекции 7 (clinician / vendor / regulator / patient). В creative copyright можно сопоставить: **artist / likeness owner** (правообладатель image / voice); **creator / training-data source** (artist, чья работа в training corpus); **victim / end-user** (жертва deepfake или потребитель fake content); **IP holder** (publisher / label / studio). Каждый actor имеет разные leverage points и разные правовые механизмы защиты. Параллель не строгая, но полезна для navigation в legal-risk profile.

**Навигационная карта.** Cross-product 3 × 4 из §0.3 объединяется с этой taxonomy следующим образом: §3.2-§3.6 — пять landmark-cases внутри категорий 1-3 copyright (текст / изображение / музыка); §3.7-§3.8 — два cases категории 4 (voice/likeness). Где мы в матрице — становится понятно по индексу подраздела.

### 3.2. NYT v OpenAI — training + output

**The New York Times Company v Microsoft Corporation et al** — иск, поданный 27 декабря 2023 года в **SDNY** (Southern District of New York — федеральный суд Южного округа Нью-Йорка) против OpenAI и Microsoft (как partner). New York Times (далее NYT) — крупнейшая ежедневная газета США, один из главных newsproviders англоязычного мира. Это, в формулировке Patent AI Lab, **самое consequential дело для будущего GenAI** ([Patent AI Lab](https://medium.com/@patentailab/nyt-vs-openai-lawsuit-update-2026-did-regurgitation-kill-the-fair-use-defense-d63ff021b805)).

**Theory of harm.** NYT утверждает: ChatGPT memorize и regurgitate verbatim segments NYT articles. Это **«regurgitation theory»** — модель не просто «обучилась стилю», она хранит конкретные protected content в weights и воспроизводит его при правильном prompt. NYT приложила в complaint конкретные примеры: фрагменты NYT-articles, воспроизводимые ChatGPT по специфическим prompts с >90% identity.

**Discovery process** (discovery = досудебная стадия истребования доказательств). Bloomberg Law affirmed ([Bloomberg Law](https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms)): OpenAI обязан выдать **20 миллионов ChatGPT logs** в рамках discovery. Plaintiffs' expert reports due **14 ноября 2025**. **SJ** (summary judgment = решение по существу без trial) deadline — **2 апреля 2026 года** `[VFY-day-of]`. Trial — TBD; самое раннее — конец 2026 / начало 2027.

**Что в игре.** Если NYT выигрывает, регулятивный ландшафт меняется радикально: «fair use» как default defence для AI training rejected; OpenAI и аналоги обязаны лицензировать input corpus, что переписывает экономику foundation-model training (licensing fees потенциально миллиарды долларов). Если OpenAI выигрывает, fair use established как принцип для AI training в American law. Это **самое consequential дело для всего GenAI** — выходящее далеко за пределы newspaper-industry.

> **Урок для инженера:** Если модель может процитировать твой training corpus verbatim — это не fair use, это infringement evidence. **Output similarity check** обязателен перед deploying модель на public input. Минимум — Bloom-filter на known protected content, либо вероятностная проверка через embedding similarity к training-data passages.

### 3.3. Getty Images v Stability AI — UK loss / US pending

Этот case иллюстрирует **дивергенцию юрисдикций**: один и тот же fact pattern, рассматриваемый в UK и US, может дать **противоположные** results.

**UK case.** Getty Images (Seattle) v Stability AI Ltd. **UK High Court ruling — 4 ноября 2025 года** ([Bird & Bird](https://www.twobirds.com/en/insights/2025/uk/stability-ai-defeats-getty-images-copyright-claims-in-first-of-its-kind-dispute-before-the-high-cour), [Mayer Brown analysis](https://www.mayerbrown.com/en/insights/publications/2025/11/getty-images-v-stability-ai-what-the-high-courts-decision-means-for-rights-holders-and-ai-developers)). **Stability выиграл primary copyright claims**: court постановил, что AI model weights **NOT a «copy»** of training images по UK **CDPA** (Copyright, Designs and Patents Act 1988 — UK-аналог US copyright law). Trademark infringement — «extremely limited», только на early Stable Diffusion versions, генерирующих watermarks Getty в output'ах. Это knockout victory для Stability в UK.

**US case (separate filing).** Getty Images (US) v Stability AI Ltd, **3:25-cv-06891** (Northern District of California). **MTD** (motion to dismiss = ходатайство об отказе в иске) **hearing — 10 февраля 2026 года**, San Francisco, Judge Trina L. Thompson `[VFY-day-of]`. US litigation использует fair-use defence (доктрина «добросовестного использования»; 4-factor test, см. §3.1 для определения); CDPA здесь не применима. US case будет рассматриваться через 4-factor fair-use тест Andy Warhol Foundation v Goldsmith (см. § 3.6).

**Что в игре.** Если US ruling также pro-Stability — это de-facto «AI training как fair use» across Atlantic, и AI-training-rights переходят в default category. Если US ruling против Stability — мы получаем **юрисдикционный split**: то, что legal в UK, не legal в US, что обязывает компании deploying AI globally к разной compliance в разных юрисдикциях.

> **Урок для инженера:** Юрисдикции расходятся. То, что legal в UK по CDPA, не обязательно legal в US по fair-use. Для global deployment проверяй обе. Это не academic point — это эмпирический fact 2025–2026 годов: один тот же fact pattern даёт противоположные results.

### 3.4. Andersen v Stability/Midjourney/DeviantArt

**Sarah Andersen, Kelly McKernan, Karla Ortiz et al v Stability AI, Midjourney, DeviantArt et al** — **class action** (коллективный иск, см. §3.1) artists в Northern District of California ([Knowing Machines](https://knowingmachines.org/knowing-legal-machines/legal-explainer/cases/andersen-v-stability-ai); [Mesh IP Law tracker](https://www.meshiplaw.com/litigation-tracker/andersen-v-stability-ai)). Это **визуальный аналог NYT v OpenAI**.

**Theory of harm.** Стали обучаться на works tens-of-thousands artists без consent, лицензии или compensation. Пользователи генерируют work «in the style of [named artist]» — это создаёт market substitution для оригинальных artist'ов. **DMCA** (Digital Millennium Copyright Act, US 1998 — закон об авторском праве в цифровой среде) violations (удаление copyright management info из training data). Несколько публичных claim-ов.

**Procedural history.**

- Initial filing — январь 2023.
- **MTD** (motion to dismiss) **denied** Aug 12 (Judge William Orrick) — это ключевой momentum-point: значит, class action выживает до discovery (досудебная стадия истребования доказательств).
- Third amended complaint — **27 февраля 2026 года**.
- Answers — **13 марта 2026 года**.
- **Trial set for 8 сентября 2026 года** `[VFY-day-of]`.

**Что в игре.** Если plaintiffs выигрывают, **«style mimicry» получает правовое узаконение** — даже если style формально не охраняется copyright, class action на DMCA + публичных правах + commercial substitution создаёт прецедент, что «in the style of [named artist]» promptn'ы — это infringement.

> **Урок для инженера:** Style mimicry «in the style of [named artist]» — **не safe just because** style как таковой не copyrightable. Class actions выживают MTD (motion to dismiss) на DMCA + публичных правах. Если твой AI-инструмент позволяет prompts типа «в стиле Эджа», ты unwittingly создал legal-risk exposure.

### 3.5. RIAA v Suno/Udio

**RIAA** (Recording Industry Association of America — торговая ассоциация крупнейших звукозаписывающих компаний США) от имени **Big Three major labels** — **UMG** (Universal Music Group), **Sony Music Entertainment**, **Warner Music Group** — подала два параллельных иска **24 июня 2024 года** ([RIAA press release](https://www.riaa.com/record-companies-bring-landmark-cases-for-responsible-ai-againstsuno-and-udio-in-boston-and-new-york-federal-courts-respectively/)):

- **RIAA v Suno** — District of Massachusetts.
- **RIAA v Udio** (Uncharted Labs) — Southern District of New York.

**Theory of harm.** Suno / Udio обучались на copyrighted music без лицензии и регулярно выдают outputs, «substantially similar» to specific copyrighted recordings (включая identifiable vocal styles конкретных artist'ов).

**Procedural history к маю 2026 года.**

- **UMG ↔ Udio — settled 29 октября 2025 года.** UMG получил settlement (payment + licensing arrangement) для **joint AI music platform** launching в 2026 году. Это превращает Udio из «litigation target» в «licensed partner of UMG». UMG ↔ Suno — переговоры продолжаются `[VFY-day-of]`.
- **Warner Music ↔ Suno — licensed deal сентябрь 2025 года.** Warner лицензировал Suno corpus в обмен на royalty stream + equity stake. Warner ↔ Udio — **по-прежнему litigation** (settlement не подписан на 2026-05-20).
- **Sony Music — остаётся major, actively litigating с обоими (Suno + Udio)** `[VFY-day-of]`. Sony не пошёл на settlement ни с одним из двух; продолжает push toward summary judgment.
- **Suno summary judgment hearing — июль 2026 года** `[VFY-day-of]`. Это ключевой momentum-point.

**Что это значит для лицензирования.** Outcome RIAA v Suno/Udio оказался **не «AI music banned»**, а **«AI music partial-licensed»**: матрица 3-major × 2-defendant раскладывается неравномерно — Warner закрыл с Suno но судится с Udio, UMG закрыл с Udio но переговоры с Suno продолжаются, Sony судится с обоими. **Это новый business-model layer (selective licensing)**, а не uniform remediation. Если Sony выигрывает, precedent создаёт юридическую базу для cleaning AI music от non-licensed training data. Если Suno/Udio выигрывают, fair-use established для music training.

> **Урок для инженера:** Lawsuit-driven licensing — actual outcome: 2 из 3 majors settled, лицензируют. Это **новый business-model layer**, не «all AI music banned». Если ты разрабатываешь music AI — заложи в roadmap licensing fees как expected cost; если ты deploys AI music в продукт — выбирай licensed-corpus провайдеров (Udio post-settlement, Suno post-Warner) если хочешь снизить юридический risk.

### 3.6. Thomson Reuters v Ross — first US ruling rejecting fair-use

**Thomson Reuters Enterprise Centre v Ross Intelligence Inc** — District of Delaware. Февраль 2025 года, **Judge Stephanos Bibas** ([Davis Wright Tremaine analysis](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2025/02/reuters-ross-court-ruling-ai-copyright-fair-use); [Reed Smith analysis](https://www.reedsmith.com/en/perspectives/2025/03/court-ai-fair-use-thomson-reuters-enterprise-gmbh-ross-intelligence)).

**Theory of harm.** Ross Intelligence (AI legal-research startup, конкурент Westlaw) использовал **Westlaw headnotes** (краткие резюме судебных дел, написанные Thomson Reuters editors) для обучения своего AI-системы legal-research. Thomson Reuters claimed copyright infringement.

**Ruling — partial Summary Judgment (SJ — решение по существу без trial) for Thomson Reuters.** Judge Bibas ruled: **NOT fair use**. Specifically, **2,200+ из 3,000 headnotes** infringed by Ross's AI training. Применены **Andy Warhol Foundation v Goldsmith факторы** (Supreme Court 2023). Fair-use 4-factor test прямо:

1. **Purpose & character of use** — commercial vs non-commercial; transformative или нет.
2. **Nature of the copyrighted work** — творческий vs factual (фактический материал — слабее защищён).
3. **Amount & substantiality used** — какая доля protected work использована, и центральная ли это часть.
4. **Effect on the market** — substitution risk для оригинального правообладателя.

В Ross case: «commercial use» + no «further purpose or different character» (Ross competes напрямую с Westlaw) → direct market substitution → fair use rejected.

**Critical caveat.** Ross — **non-generative AI** (это search/retrieval system, не LLM/diffusion model). Применимость к LLM / generative AI — будет тестироваться в NYT v OpenAI, Andersen v Stability, Getty US, RIAA v Suno. Patent AI Lab ([NYT v OpenAI update](https://medium.com/@patentailab/nyt-vs-openai-lawsuit-update-2026-did-regurgitation-kill-the-fair-use-defense-d63ff021b805)) формулирует gating вопрос: будет ли «transformative use» (NYT case) более убедительным аргументом для LLM, чем для search/retrieval? Это **открытый юридический вопрос на 2026 год**.

**Что это означает в целом.** Thomson Reuters v Ross — **первое американское ruling**, отвергнувшее fair-use defence в AI-training контексте. Это не **обязывает** будущие cases — но это разрушает шаблонное assumption «AI training = automatically fair use», который был доминирующим в индустрии до 2025 года.

> **Урок для инженера:** «Fair use» — **не дефолт**. LLM / diffusion test cases впереди (NYT, Andersen, Getty US). Не строй product roadmap на assumption «fair-use defence нас спасёт». Если твой product использует AI, обученный на large web corpus, имеет legal-risk exposure, оцениваемое в десятки миллионов долларов в expected liability в случае adverse ruling в любом из landmark cases.

---

> **Пауза-резюме (до этого момента).** Мы разобрали блок copyright: 4 категории таксономии (§3.1) + 5 landmark-cases (NYT §3.2 — training+output; Getty UK/US §3.3 — jurisdiction split; Andersen §3.4 — style mimicry class action; RIAA v Suno/Udio §3.5 — selective licensing; Thomson Reuters v Ross §3.6 — first US ruling rejecting fair-use). Это категории 1-3 нашей таксономии.
>
> **Далее.** §3.7-§3.8 — категория 4, voice/likeness rights через deepfake (Arup CFO $25.6M, Korea class harm). После — другие failure-классы: slop & model collapse (§3.9-§3.10), marketing backlash (§3.11), displacement consolidated (§3.12).

### 3.7. Deepfake — Arup CFO $25.6M

Январь 2024 года. **Arup** (британская engineering firm, известна по Sydney Opera House) ([CNN, May 16, 2024](https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk); [Fortune, May 17, 2024](https://fortune.com/europe/2024/05/17/arup-deepfake-fraud-scam-victim-hong-kong-25-million-cfo/)). Финансовый сотрудник в Hong Kong office получил email-приглашение на видеозвонок от того, что выглядело как CFO компании + несколько colleagues. В течение видеозвонка дезориентированный finance worker согласовал и провёл **15 транзакций общей суммой $25.6M (HK$200M)**.

**Что произошло.** Email и видеозвонок были социальной инженерией. **CFO и colleagues в видеозвонке были deepfake** — AI-generated face + voice cloning + real-time lip-sync. Worker не имел оснований сомневаться: визуально это были identifiable colleagues, голос — identifiable, тон — естественный, корпоративный context — правдоподобный.

**Инженерный механизм.** Это иллюстрирует **commodification deepfake-технологии**: real-time deepfake в multi-participant video call (несколько deepfake-лиц одновременно) перестал быть лабораторным экспериментом и стал доступен criminal actors. Технологически это требует: (1) source footage / images каждого участника (доступно из LinkedIn, корпоративных сайтов, social media); (2) voice samples (доступны из publicly available conference talks, podcasts); (3) real-time inference hardware ($1–5k GPU rig); (4) face-swap + lip-sync software (open-source).

**Outcome.** Arup публично подтвердил инцидент, recovery большей части средств не произошёл, Hong Kong полиция расследовала. Никто арестован не был на момент публикации. Это первый широко известный multi-party real-time deepfake video scam с финансовым ущербом корпоративного уровня.

> **Урок для инженера:** Видеозвонок ≠ identity proof в 2024+. Финансовые транзакции выше определённого threshold (Arup сам пересмотрел свой threshold после incident) требуют **out-of-band verification**: callback по known phone number, multi-factor authentication, физическая подпись. Это не «security paranoia» — это новая baseline для финансового контроля операций в AI-эре.

### 3.8. Korea schoolgirl deepfake crisis — class harm

Август 2024 года в Южной Корее ([NPR, September 6, 2024](https://www.npr.org/2024/09/06/nx-s1-5101891/south-korea-deepfake); [Daily Star](https://www.thedailystar.net/news/world/news/deepfake-porn-crisis-batters-south-korea-schools-3698986)). Журналисты обнаружили **более 200 Telegram-чатов** (точное число fluctuates по разным reports, citing NPR + Korea Communications Commission data) с deepfake-pornography, генерируемой из selfies одноклассниц и учительниц.

**Масштаб.** **6,500 takedown requests** в период с января по июль 2024 года — **4× over 2023** (накопительный рост deepfake-incidents за один год). **74% подозреваемых — в возрасте 10–19 лет** — подростки, генерирующие deepfake-porn из selfies своих сверстниц. Между 2021 годом и июлем 2024 года: **793 reported cases / только 16 prosecuted** — то есть, enforcement rate ~2%.

**Инженерный механизм.** Технологический barrier — практически ноль: AI face-swap apps (некоторые легально доступные в Google Play и App Store до 2024 года) принимают source photo (selfie из Instagram / Telegram) → swap face на pre-uploaded explicit content. Generation time — секунды. Distribution — Telegram-каналы. Доступная capability + слабый enforcement = **массовый class harm на vulnerable population**.

**Outcome.** Корейское правительство в августе 2024 года объявило emergency task force; были закрыты несколько ключевых apps; были усилены penalties для distribution; были введены school-level awareness programmes. Однако structural выход из проблемы пока не найден — accountability через Telegram-каналы (decentralized, often hosted outside South Korea) практически невозможен.

> **Урок для инженера:** Доступная capability + слабый enforcement = **массовый class harm**. Для consumer-facing AI tools, особенно с image / video / voice generation capability, обязателен **safety layer ещё до launch**: NSFW detection (отказ генерации explicit content из non-explicit input); age verification (block для определённых input categories при подозрении на minor'а); reporting pipeline (быстрая deletion + escalation при detection). Это не «после-добавляемый patch»; это требование к product roadmap day-one.

### 3.9. Slop & model collapse — Shumailov 2024

**Slop** (термин, популяризированный Emily Bender и Gary Marcus в 2024 году) — низкокачественный AI-generated content, заполняющий platforms (Amazon Kindle, Google AI Overviews, Sports Illustrated, news aggregators). Это не «AI делает ошибки иногда» — это **structural property** модели, обучающейся на recursive synthetic data.

**Shumailov et al, Nature 2024** (vol 631, p 755–759). Статья «AI models collapse when trained on recursively generated data» формализует **model collapse**: рекурсивное обучение на synthetic outputs приводит к **прогрессирующей деградации качества + сужению diversity** (модель «забывает» tail распределения, оставляя только mainstream). Это также называется **Model Autophagy Disorder (MAD)**.

**Контекст.** К ~2026 году supply высококачественных human-generated training data исчерпывается; следующие foundation модели вынуждены fallback на synthetic outputs предыдущих моделей. Это создаёт **системный риск quality decline** для всей AI-индустрии. Не один конкретный provider — а вся indust.

**Конкретные инциденты slop в production.**

- **Google AI Overviews** (May 2024 rollout) — рекомендации «**put glue on pizza**» (⅛ cup non-toxic glue, source — Reddit joke), «**eat at least one rock per day**» (source — The Onion satire, «Geologists recommend»), «Obama is a Muslim president» (false), «Andrew Johnson got degrees 1947–2012» (он умер в 1875 году) ([ACS report](https://ia.acs.org.au/article/2024/google-goes-viral-after-ai-says-to-put-glue-on-pizza-eat-rocks.html); [MIT Tech Review analysis](https://www.technologyreview.com/2024/05/31/1093019/why-are-googles-ai-overviews-results-so-bad/)). Виноват **источник training data**: модель обучалась на Reddit + The Onion без attribution context, что превратило satire в «answers».

> **Урок для инженера:** **Source quality > volume**. Модель, обучавшаяся на Reddit jokes без context filter, проигрывает модели на curated dataset — **даже если curated в 10× меньше**. Это не «больше данных = лучше»; это «правильно отобранные данные = лучше». Adobe Firefly «commercial-safe» — это конкретный manifest этого принципа: меньший corpus (Adobe Stock + licensed) даёт более controlled output. Если ты разрабатываешь AI-product с public-facing output, **curation > volume** должно быть core решением на этапе architecture, не «patch» после reception.

### 3.10. Sports Illustrated fake authors + Amazon Kindle sham books

Параллельный case к slop — структурное разрушение legacy trust через AI-pseudonyms.

**Sports Illustrated** — ноябрь 2023 года. **Futurism exposé** ([Futurism / Poynter analysis](https://www.poynter.org/commentary/2023/sports-illustrated-artificial-intelligence-writers-futurism/); [CNN coverage](https://www.cnn.com/2023/11/27/media/sports-illustrated-deletes-articles-fake-author-names-ai-profile-photos/index.html)) обнаружил, что Sports Illustrated публиковал articles под **fake author names** + **AI-generated profile photos**. Profile photos for fake authors были purchased on digital marketplaces, продававших AI-generated face images по few dollars. Arena Group (parent of SI) blamed third-party content vendor AdVon Commerce; SI Union публично выразило «horror»; affected articles были удалены.

**Что произошло.** Это **разрушение legacy trust** в чистом виде. Sports Illustrated — журнал с 70-летней историей, brand equity около миллиарда долларов. AI-pseudonyms разрушили это **моментально**: news cycle, в котором brand был обвинён в обмане readers, дискредитировал brand value. Recovery: невозможен в полной мере; SI всё ещё существует, но trust premium снижен.

**Amazon Kindle AI sham books** — 2023–2024. ([NPR / Authors Guild](https://www.npr.org/2024/03/13/1237888126/growing-number-ai-scam-books-amazon); [Authors Guild analysis](https://authorsguild.org/news/ai-driving-new-surge-of-sham-books-on-amazon/)). Authors Guild документировал **surge AI-generated sham books на Amazon Kindle в 2023–24**: сотни fake authors, ряд из которых эксплуатируют имена реальных jazz-figures (Frank Gioia, Ted Alkyer — sham books, использующие узнаваемые имена музыкантов с slight-modified названиями). Scammers выпускают AI-knockoff'ы под именами реальных authors, эксплуатируя name recognition.

Amazon в response ограничил KDP до **3 books/day/author** и потребовал AI-disclosure при upload. Но **disclosure не показывается consumer'у** в карточке книги — то есть consumer не знает, что покупает AI-generated book.

> **Урок для инженера:** **Legacy trust = key brand asset**. AI-pseudonyms разрушают его моментально. Если ты публикуешь под именем, **имя должно быть либо реальным человеком, либо explicitly AI-disclosed**. Half-measures (raw publication without clear disclosure) — это not just ethical issue; это direct brand-damage liability, измеримая через customer trust survey + revenue impact. Sports Illustrated провёл этот эксперимент за всех — повторять не надо.

---

> **Пауза-резюме (до этого момента).** Copyright (§3.1-§3.6) + deepfakes/voice-likeness (§3.7-§3.8) + slop/legacy-trust разрушение (§3.9-§3.10) = три **content-failure**-блока. Это failures того, что AI **производит**.
>
> **Далее.** §3.11 — **market-reception failure** (brand backlash на iconic creative); §3.12 — **labor-market failure** (displacement consolidated). Это failures того, как AI-output **воспринимается рынком и трудовой средой**.

### 3.11. Coca-Cola + Toys «R» Us — marketing backlash

Два landmark маркетинговых cases 2024 года, демонстрирующих, что **AI execution может быть incompatible с iconic brand creative**, даже когда technical quality is acceptable.

**Coca-Cola «Holidays Are Coming» AI Christmas ad** — декабрь 2024 года ([NBC News](https://www.nbcnews.com/tech/innovation/coca-cola-causes-controversy-ai-made-ad-rcna180665); [Marketing AI Institute](https://www.marketingaiinstitute.com/blog/criticism-ai-coke-holiday-ad)). «Holidays Are Coming» — иконическая Christmas-кампания Coca-Cola, существующая с 1995 года, с узнаваемым красным грузовиком в зимней деревне; один из ключевых элементов brand-equity бренда. Coca-Cola выпустил AI-generated Christmas ad, восстанавливающий этот culture classic через три AI-студии: Secret Level, Silverside AI, Wild Card; используя четыре разные модели.

**Reception.** Sustained «soulless» backlash от audience. Конкретные критики: визуальные artefacts (странные движения характеров), отсутствие emotional resonance ассоциированного с original campaign, ощущение того, что iconic seasonal creative «продан» AI execution.

**Outcome.** Coca-Cola **повторила** AI-ad в 2025 году несмотря на 2024 backlash. Это статистически интересно: маркетинговый KPI (reach, recall, brand mention) предположительно соответствовал target'ам; качественный brand-equity impact — sustained негативный.

**Toys «R» Us Sora ad** — Cannes Lions June 2024 ([Hollywood Reporter](https://www.hollywoodreporter.com/business/digital/toys-r-us-ad-sora-openai-video-tool-reaction-1235932993/); [Marketing-Interactive sentiment data](https://www.marketing-interactive.com/toys-r-us-sora-ai-sentiments-plummet)). Первый major-brand 66-секундный единый AI-generated commercial. Использован Sora (early-access, до публичного релиза). Премьера на Cannes Lions June 2024.

**Reception данные.** Sentiment analysis Toys «R» Us:

- **Positive sentiment swing**: с **+12.2%** до **+3.4%** (drop ~9pp).
- **Negative sentiment swing**: с **13.5%** до **53.4%** (jump ~40pp).

Joe Russo (один из двух братьев Russo — режиссёров Marvel Avengers: Endgame, Captain America: The Winter Soldier): «fucking sucks». Toys «R» Us official response: «successful test». Это illustration **brand-damage measurable through sentiment swing**, не CTR / impressions.

> **Урок для инженера:** AI-ad **возможен**, но iconic seasonal / iconic brand creative **без human leadership** = **brand damage**. Brand-trust риск измеряется **sentiment swing**, не CTR. Если ты разрабатываешь AI-tool для marketing, документируй case studies этого типа (Toys «R» Us — primary): это **product warning** for end-users, не «just a marketing fail». Для commercial creative выше определённого brand-equity threshold human direction остаётся mandatory; для commodity creative (product photography, B-roll) — AI работает.

### 3.12. Displacement consolidated — clauses + wage compression

Этот пункт консолидирует displacement-данные из § 2.4 в один failure-frame, потому что displacement — это **не временный shock**, это **structural transformation labor market'а**.

**Clauses helped, but не покрывают bottom.** SAG-AFTRA + WGA AI clauses 2023 года — это значительная victory для unionized labor (top-tier writers, actors). Digital Replicas, Synthetic Performers, AI training disclosure — все добавлены. **2026 4-year extension** гарантирует stability до 2028 года. Но: эти clauses **покрывают только union-members** и **только Hollywood/major studios**. Они **не покрывают**:

- Bottom-tier freelance на Upwork / Fiverr.
- Stock photographers (independent contractors, не union).
- Korean voice actors (вне SAG-AFTRA jurisdiction).
- Commodity B-roll camera operators.

**Wage compression снизу.** [Jobbers Displacement Index](https://www.jobbers.io/ai-job-displacement-index-which-freelance-skills-are-at-risk/): AI detected в **40% работ writers $10–19/час** vs **<10% работ $60+/час**. Это **structural**: bottom-tier work выполняется AI, который дешевле любого human freelancer; top-tier work остаётся human, потому что value-add от curation/direction/brand-alignment не дублируется AI. Между ними — middle-tier ($20–60/час) — сжимается, поскольку часть его задач uplifts в top-tier (по mere virtue выживания), часть deflates в bottom-tier (по virtue commoditization).

**Stock industry — pivot, не resilience.** Shutterstock не «выжил кризис» — он pivot'нулся. Shutterstock licensing к AI companies — **$104M в 2023 → $138M в 2024 → ~$250M прогноз 2027**. То есть, Shutterstock перестаёт зарабатывать на продаже photos фотографам как dispatched product; начинает зарабатывать на лицензировании photo corpora AI-компаниям как training data. **Photographers перестают быть customer'ом, они становятся data source**. Для individual contributors это структурно негативно: их revenue share от стокового продажа практически исчезает; их revenue от licensing-pool (если такой есть) — небольшой и распределённый.

> **Урок для инженера:** **Displacement — структурный, не временный shock**. AI clauses в hollywood помогают top-tier; bottom-tier продолжает сжиматься. Если ты планируешь deploy AI в creative-сфере, проанализируй: **какой класс labor displaces твой AI?** Top-tier (защищён union clauses, value-add от direction) — это displacement-risk minimal. Bottom-tier (stock photos, commodity B-roll, basic voiceovers) — displacement уже происходит. Middle-tier — pressure-zone. Понимать это до launch — обязательное требование к design AI-product, если ты не хочешь стать viral case study в негативном news cycle (Coca-Cola, SI, WotC).

### Self-check (Раздел 3)

1. 4 категории copyright-исков в AI: training-data scraping, output similarity, style mimicry, voice/likeness. К какой категории относится **Andersen v Stability**? К какой — **NYT v OpenAI**? К какой — **ScarJo v OpenAI Sky**?
2. **Thomson Reuters v Ross** — первое US ruling, отвергнувшее fair-use defence в AI-training. Почему это **не automatic precedent** для NYT / Andersen / Getty US? Что отличает Ross от generative AI с точки зрения case law?
3. Arup CFO scam ($25.6M через deepfake video call) и Korea schoolgirl deepfake epidemic — два разных типа deepfake harm. Назовите ключевые отличия: target population, distribution mechanism, scale.
4. Sports Illustrated AI fake authors scandal — что именно был «pre-AI baseline» (статус-кво до AI), и что именно был «AI-amplified harm» (новый класс failure, возникший с AI)?
5. Toys «R» Us Sora ad показал sentiment swing −9pp positive / +40pp negative. Coca-Cola повторила свою AI-ad в 2025 году несмотря на backlash 2024. Объясните эту seeming contradiction: какие маркетинговые / brand factors можно рассмотреть?

---

## Раздел 4. AI здесь не нужен — критерии негативного выбора

### 4.1. Четыре критерия отказа

Этот раздел — **payoff главы**. Уроки из 12 кейсов в § 3 — это не разобщённые курьёзы, а 12 разных проявлений 4-х фундаментальных критериев, по которым инженер обязан проверить любой AI-инструмент перед deploying в creative-проект. Если хотя бы один критерий **не выполнен — это серьёзный сигнал для отказа от AI в данной задаче**, либо для дополнительного риск-mitigation. Эти 4 критерия выведены **inductively из кейсов §3**, не a priori.

**Критерий 1: Training-data license.** Вопрос: **Лицензирован ли training corpus AI-инструмента**, который ты используешь? Adobe Firefly (обучен на Adobe Stock + licensed content) = **да**. Stable Diffusion (обучен на web scrape без consent) = **нет**, юридический долг существует. Midjourney = неясно (тренинг corpus не disclosed, but Andersen case argument utiliz pieces of art). Если ответ «нет» — есть юридический долг (Andersen, RIAA precedents). Это не theoretical risk: суды активны, settlements происходят (Udio settled с UMG октябрь 2025).

**Критерий 2: Output similarity check.** Вопрос: **Может ли модель воспроизвести protected content verbatim?** NYT v OpenAI «regurgitation theory»: если ChatGPT воспроизводит NYT article verbatim из training memory, это infringement evidence. Это не abstract — это actual mechanism, использованный в complaint. Output similarity check — это инженерная задача: можно реализовать через embedding-similarity к known protected content, через Bloom filter на known passages, через probabilistic verification. Если ты deploys AI и **не проверяешь output similarity** — ты unwittingly accept liability.

**Критерий 3: Voice/likeness consent.** Вопрос: **Если AI генерирует voice / image / likeness идентифицируемого person'а — есть explicit consent?** ScarJo v OpenAI Sky показала, что **even soundalike** создаёт right-of-publicity risk, не только direct cloning. SAG-AFTRA Digital Replicas clause — contract-based defence. No AI FRAUD Act (US, in legislative process) и EU deepfake criminalisation (в силу к mid-2027) обеспечат federal/regulatory framework. Если ответ «нет consent» — это hard stop.

**Критерий 4: Brand-trust риск.** Вопрос: **Является ли creative-задача iconic / legacy / high brand-equity zone?** Coca-Cola «Holidays Are Coming» (legacy iconic), Sports Illustrated (legacy publication), Toys «R» Us holiday campaign (legacy nostalgia) — все три попали в backlash, потому что AI execution dissonant с brand expectation. Brand-trust риск measurable через sentiment swing. Если ответ «да, iconic / legacy» — human direction mandatory; AI как support tool допустим, AI как primary execution — отказ.

Эти четыре критерия — не exhaustive, но они покрывают подавляющее большинство landmark provals из § 3. Применение четырёх критериев — это NOT моральный вопрос; это конкретная риск-mitigation практика. Параграф 5 переводит критерии в operational чек-лист.

### 4.2. Где human только: investigative journalism, original direction, long-form narrative

Если критерии § 4.1 — это «когда отказаться», то этот раздел — позитивная формулировка: **где human-only остаётся mandatory**, не как ностальгия, а как functional requirement.

**Investigative journalism + original reporting.** NYT, Washington Post, Reuters имеют explicit guidelines, prohibit использование AI для original reporting (не для proofreading или для summarization). Причина — Sports Illustrated case study (см. § 3.10) + epistemic accountability. Когда журналист публикует первоисточный материал, brand надёжности (NYT, WaPo) — это **ключевой asset**, моментально destroying при AI-substitution. Это не вопрос «AI пишет хуже»; это вопрос «brand эпистемологически gradient'руется на human accountability». Replacement → loss epistemic standing.

**Original creative direction.** Coca-Cola «Holidays Are Coming», Toys «R» Us Christmas, любая iconic seasonal campaign высокого brand-equity uses требует human creative direction. AI как execution tool (под direction) — допустим. AI как primary creative — это **brand-damage risk**, measurable через sentiment swing (см. § 3.11). Здесь human-only — это **strategic** requirement, не tactical.

**Long-form coherent narrative.** Suno / Udio к 2026 году generate tracks (3–4 min), не coherent 50-minute album'ы с motif development. Sora 2 / Veo 3.1 generate clips ≤25 sec, не coherent feature films. Длинная narrative composition (album, film, novel) требует **architectural cohérence**, которую AI достижимыми архитектурами не покрывает (limitation семейства neural audio synthesis и latent video transformer — § 0.1). Это **не временное ограничение**, которое «исчезнет в следующей версии»; это inherent property текущей generation моделей.

### 4.3. YouTube AI thumbnails: empirical end-user rejection

Один из самых ярких empirical evidence про границы AI в creative — это YouTube AI thumbnails. К декабрю 2025 года крупные YouTube creators начали массово **отказываться** от AI-generated thumbnails. ([Social Blade Creator Survey, Dec 2025; Banana Thumbnail blog](https://blog.bananathumbnail.com/ai-youtube-thumbnails-2/); [Miraflow](https://miraflow.ai/blog/youtube-ctr-2026-good-click-through-rate-ai-thumbnails)).

**47.3% creators** в опросе stop using AI thumbnails в Dec 2025. Это measurable end-user rejection — не «опросная maxim», а observed behavior pattern.

**Причины (measured).**

- **«Creepy smooth skin / weird lighting»** → **−22% CTR vs human-edited**.
- **Mobile text readability fails** в **39.6% случаев** → **−19% CTR**.
- **Mismatched promise / content** (когда thumbnail обещает scene, которой нет в видео) → **−61.8% first-15-sec drop-off** `[VFY-day-of]`.

**Что это означает в общем смысле.** Это **empirical end-user rejection** — не «эстетический спор», а measurable conversion / engagement metric. AI thumbnails недостаточно хороши для top-tier YouTube creators (где каждый процент CTR значит revenue), потому что у них есть конкретные failure modes (skin texture, text rendering, scene-content mismatch). Это не «AI плох в искусстве» — это «текущая generation AI thumbnails плоха в **этом конкретном** конверсионном контексте».

Это мост к § 5: измеримый end-user reception — это **сигнал** для отказа, не просто «опыт пользователей не понравился». Если CTR падает на 22%, это direct revenue impact для creator, и это перевешивает любую стоимость per-thumbnail savings.

### Self-check (Раздел 4)

1. Какие из 4 критериев отказа применимы к кейсу «маркетолог хочет сделать AI-generated Christmas commercial для legacy iconic FMCG-бренда»? Объясните, какие именно вопросы он должен задать.
2. NYT explicitly запрещает AI для original reporting, но разрешает AI для summarization и proofreading. Почему это разграничение методически верное?
3. YouTube AI thumbnails — 47.3% creators stopped using. Назовите три **failure mode** (механически разные), которые приводят к этой rejection.

---

## Раздел 5. Что инженеру делать — actionable checklist

### 5.1. 5-вопросный чек-лист перед AI в creative-проекте

Этот раздел — **финальный operational артефакт**, который студент уносит из лекции. Это чек-лист, который применяется как gating criterion перед deploying AI в creative-задаче. Не «AI запрещён», не «AI разрешён» — **AI используется при условии прохождения 5 вопросов**.

> **Чек-лист «Перед использованием AI в creative-проекте»:**
>
> 1. **Training-data license.** Лицензирован ли corpus AI-инструмента? Adobe Firefly = да. Stable Diffusion / Midjourney = есть risks. Если ответ «нет» / «неясно» — fallback на licensed-corpus tool либо отказ.
> 2. **Output similarity check.** Может ли модель воспроизводить protected content verbatim? Implementation — embedding similarity + Bloom filter на known passages. Без проверки — accept liability.
> 3. **Voice / likeness consent.** Если генерируется voice / face / likeness identifiable person'а — есть explicit consent + compensation? Без consent — hard stop.
> 4. **IP-clean tools для commercial use.** Используешь ли ты commercial-safe pipeline (Firefly Foundry, лицензированные partner models)? Для consumer-facing commercial — это minimal requirement.
> 5. **Brand-trust риск.** Iconic / legacy / high brand-equity creative? Human direction mandatory; AI — только как support tool, не primary execution.

Каждый из этих пяти вопросов имеет **measurable answer**, не abstract «мне кажется». Они operationalizable. Это и есть actionable инструмент.

**Flowchart применения.** В упрощённой форме:

1. Если хотя бы один из (1)/(2)/(3) — «нет» → отказ от AI в этой задаче.
2. Если (4) — «нет» → выбор alternative commercial-safe tool (Firefly Foundry, лицензированный partner) либо отказ.
3. Если (5) — «да, iconic» → human direction primary, AI — support only.
4. Если все 5 — «да» → AI применим. Document choices для audit trail.

### 5.2. Mapping чек-листа на 12 кейсов из §3

Чек-лист — не просто абстрактный список вопросов. Каждый его пункт может быть проверен против landmark-кейсов § 3 — это и есть смысл «inductive deriv'ация»: критерии берутся не из ниоткуда, а из реальных провалов. Mapping:

| # | Кейс | Какой критерий нарушен | Что должен был сделать инженер |
|---|---|---|---|
| § 3.2 | NYT v OpenAI | (1) Training-data license + (2) Output similarity | Лицензировать input corpus; реализовать output-similarity check |
| § 3.3 | Getty v Stability (UK win / US pending) | (1) Training-data license | Использовать licensed-corpus сегмент; готовиться к юрисдикционному split |
| § 3.4 | Andersen v Stability | (1) Training-data license + (3) style mimicry | Не допускать «in the style of [named artist]» prompts |
| § 3.5 | RIAA v Suno/Udio | (1) Training-data license | Лицензированный provider (Udio post-settlement; Suno post-Warner) |
| § 3.6 | Thomson Reuters v Ross | (1) Training-data license (нон-fair-use) | Не строить product на «fair-use spasaet» assumption |
| § 3.7 | Arup CFO $25.6M deepfake | (3) Voice/likeness consent (criminal) | Out-of-band verification; multi-factor для financial transactions |
| § 3.8 | Korea schoolgirl deepfake | (3) Voice/likeness consent (criminal class harm) | NSFW detection + age verification + reporting layer **до launch** |
| § 3.9 | Slop / Google AI Overviews | (косвенный — source quality) | Curation > volume; filter source data |
| § 3.10 | SI fake authors + Amazon sham books | (5) Brand-trust риск | Реальный человек ИЛИ explicit AI-disclosure (legacy publication brand-trust) |
| § 3.11 | Coca-Cola / Toys «R» Us | (5) Brand-trust риск (iconic seasonal creative) | Human creative direction; AI как support tool, не primary execution |
| § 3.12 | Displacement (Upwork, Stock) | (косвенный — labor ethics, ESG, regulatory pressure) | Документировать, какой класс labor displace; planning regulatory compliance |

Каждый кейс — это **failed checklist application**. Каждый показывает, что произойдёт, если инженер пропускает соответствующий вопрос. Поэтому изучение § 3 — это **не just-history**, это сборник actionable lessons из реальных провалов индустрии.

### Self-check (Раздел 5)

1. Назови все 5 вопросов чек-листа из §5.1 без подсматривания (по памяти). Проверь себя — ключевые слова: training, output, voice/likeness, IP-clean, brand-trust.
2. Для гипотетического проекта **«AI-generated marketing video для retail-brand»**: какие из 5 вопросов скорее всего отвечают «нет AI» / «требуют отказа», а какие — «AI применим с mitigation»? Объясни через cases §3.
3. Из 12 cases в §3 выбери один (любой) и сформулируй мост к чек-листу в §5.1 — какой именно вопрос check-list'а является **direct inductive lesson** из этого case (т.е. вопрос, который сформулирован именно потому, что этот case произошёл).

---

## Раздел 6. Закрытие

К 2026 году generative AI прошёл путь от лабораторной демонстрации (Sora первая публичная демо — февраль 2024) до индустриальной инфраструктуры с измеримой экономической пользой ($400M Adobe Firefly revenue, $9.1B AI video ad spend, 22B+ Firefly assets) и измеримым юридическим долгом (NYT v OpenAI 20M logs discovery, RIAA v Suno settlement billions, Andersen trial 8 сент 2026). Эти два процесса — adoption и legal accountability — идут параллельно и **не отменяют** друг друга: один не сменяет другого, оба сосуществуют.

**Три главных вывода.**

1. **Архитектурно** generative AI — это три семейства (diffusion / latent video transformer / neural audio). Inherent limits каждого семейства (Sora 25 sec, voice cloning из 1 минуты, Firefly «commercial-safe» от corpus, не от architecture) — это первый sanity check для любой application.
2. **Экономически** AI добавил новые capabilities (Sora 2, ElevenLabs, Genie 3), изменил cost-структуру (100×–10000× cheaper) и переписал labor market (wage compression снизу). Это структурный shift, не временный shock.
3. **Юридически** к 2026 году открыты landmark cases во всех 4 категориях copyright-исков (training-data scraping, output similarity, style mimicry, voice/likeness). Outcome определит ландшафт следующих 5+ лет. Инженерный риск-mitigation требует 5-вопросный чек-лист как gating criterion.

**Cross-references к другим лекциям.**

- **Лекция 1** «где AI работает / где нет» — Лекция 8 углубляет до 4 конкретных критериев negative-choice. Где Лекция 1 ставила general framework, здесь мы получили inductive list из 12 landmark кейсов.
- **Лекция 3** «Архитектуры AI-систем» — Лекция 8 опирается на mental model 3 семейств генеративных моделей (§ 0.1), а также упоминает платформенный слой (Adobe Firefly Foundry, HuggingFace Spaces) как пример уровня абстракции над моделью. Архитектурный аспект подробно покрыт в Лекции 3.
- **Лекция 5** «AI в финансах и ритейле» — параллель в legal-risk frame: как Сбер AI scoring создаёт risk-debt в финансах (algorithmic bias → regulatory liability), так Stable Diffusion / Midjourney training-data — risk-debt в creative (Andersen → settlement / damages). Параллель structural: новая capability создаёт новый класс risk, который measurable и contained, не «банально иррациональный страх».
- **Лекция 7** «AI в медицине» — параллель в 4-actor responsibility framework. Где в медицине actors — clinician / vendor / regulator / patient, в creative copyright — artist/likeness owner (ScarJo) / creator/training-data source (Andersen artists) / victim/end-user (Arup, SI readers) / IP holder (Sony, NYT). Структурная аналогия позволяет переносить principle ответственности из одной индустрии в другую.

**Что будет в Лекции 9.** Следующая лекция — **«AI в авиакосмической отрасли и оборонном комплексе»**. Если Лекция 8 — это AI с самым широким публичным contact surface (creative reaches billions), Лекция 9 — это AI с **самым высоким уровнем ответственности**: human lives at scale, national security implications, multi-decade horizon decisions. **Эскалация human-in-the-loop пройдёт в Лекции 9 на принципиально другой уровень stakes**: где провал AI-системы в Лекции 8 создаёт sentiment dip (Toys «R» Us −9pp positive), brand-damage (Coca-Cola «soulless» backlash), legal liability (Andersen, NYT — десятки миллионов долларов в expected damages), в Лекции 9 провал AI-системы создаёт **kinetic outcome**: KIA (killed in action), civilian casualty, потеря spacecraft / payload, escalation military incident. Конкретно это разворачивается в обсуждении LAWS (lethal autonomous weapon systems), Project Maven / DoD AI-stack, human-rated flight software (NASA / SpaceX), и в дискуссии «meaningful human control» (UN GGE on LAWS). Параллели и контрасты с Лекцией 7 (medical AI lives-at-individual-scale vs aerospace lives-at-systemic-scale) и с Лекцией 8 (creative AI broad-public-contact vs aerospace narrow-but-deep-stakes) сформируют framework для лекций 9–17.

---

## Глоссарий

Этот раздел — locked-glossary для лекции (18 терминов, canonical forms). Между лекцией, slides и speech.md эти термины используются единообразно.

| # | Канонический термин (RU) | Канонический термин (EN) | Определение |
|---|---|---|---|
| 1 | **Generative AI (GenAI)** | Generative AI / GenAI | Модели, синтезирующие новый content (image / video / audio / text) из training corpus. Базовая категория, охватывающая все AI-инструменты этой лекции (diffusion, transformer-based, autoregressive audio). |
| 2 | **Foundation model** | Foundation model | Крупная pre-trained модель (например, Sora 2, Midjourney v7, Suno v5.5), которая выступает базой для fine-tuning под specific creative-задачи. Архитектурно соответствует одному из 3 семейств (§ 0.1). |
| 3 | **Text-to-X / X-to-X** | Text-to-X / X-to-X | Capability-режим инструмента: text-to-video (Sora, Veo), image-to-image (Midjourney edit), video-to-video (Runway Aleph), text-to-song (Suno). Описывает, какой input → какой output. |
| 4 | **Diffusion model** | Diffusion model | Класс генеративных моделей с forward process (добавление шума к image) + reverse process (denoising → image). Примеры: Stable Diffusion, Midjourney, DALL-E, Imagen, Firefly. См. Ho et al. (2020), Rombach et al. (2022). |
| 5 | **Latent (video) transformer** | Latent video transformer | Генеративная модель видео в латентном пространстве (compact representation последовательно-временных tokens) с механизмом temporal consistency. Примеры: Sora 2, Veo 3.1, Runway Gen-4. Inherent limit — exponential cost scaling по latent length. |
| 6 | **Neural audio synthesis** | Neural audio synthesis | Семейство моделей для генерации waveform / spectrogram. Два суб-типа: autoregressive (для речи и song lyrics, ElevenLabs) + diffusion (для music, Stable Audio 2). См. § 0.1. |
| 7 | **Character consistency** | Character consistency | Сохранение визуальных характеристик персонажа через множественные генерации (Sora 2 cameos, Midjourney Omni Reference, Runway Gen-4 Director Mode). Critical capability для multi-scene narrative. |
| 8 | **Voice cloning** | Voice cloning | Синтез голоса конкретного speaker'а из минимального audio sample (ElevenLabs — 1 минута). Возможен через fine-tuning pre-trained foundation модели. |
| 9 | **World model** | World model | Модель, генерирующая explorable simulated environment (Genie 3 от Google DeepMind). Отличается от video generator: output — интерактивная среда, не последовательность кадров. |
| 10 | **Slop** | Slop | Colloquial term (Emily Bender, Gary Marcus 2024+) для низкокачественного AI-generated content, заполняющего platforms (Amazon Kindle, Google AI Overviews, аналоги). Academic synonym — «low-quality synthetic content». См. также model collapse. |
| 11 | **Model collapse / MAD** | Model collapse / Model Autophagy Disorder | Прогрессирующая деградация качества и сужение diversity модели при recursive training на synthetic outputs предыдущих моделей. Shumailov et al., Nature 2024 (vol 631, p 755–759). Системный риск для AI-индустрии при exhaustion human-generated training data. |
| 12 | **Deepfake** | Deepfake | AI-generated synthetic media, изображающее конкретного person'а (visually или audio) без consent. Включает face-swap video, voice clone, real-time multi-party fakes. Примеры landmark incidents: ScarJo Sky, Arup CFO scam, Korea schoolgirl crisis. |
| 13 | **Right of publicity / likeness rights** | Right of publicity | Право контроля коммерческого использования голоса / образа конкретного человека. US — state-by-state; EU — частично через GDPR Article 6; SAG-AFTRA Digital Replicas clause — contract-based protection. No AI FRAUD Act (US, federal pending). |
| 14 | **Regurgitation theory** | Regurgitation theory | Theory of harm в NYT v OpenAI: модель memorize protected training content и воспроизводит его verbatim в output. Если доказана — это infringement evidence, не fair use. Output similarity check — инженерная задача защиты от этой theory. |
| 15 | **Style mimicry** | Style mimicry | Capability генерации в стиле named artist (через prompt «in the style of [name]»). Style традиционно не охраняется copyright, но Andersen v Stability аргументирует через DMCA + публичные права + commercial substitution. Открытый вопрос 2026. |
| 16 | **Fair use defence** | Fair use defence | US legal doctrine (Section 107, Copyright Act) для использования copyrighted material без лицензии. 4 factor test, расширенный Andy Warhol Foundation v Goldsmith (Supreme Court 2023). Thomson Reuters v Ross — first US ruling, отвергнувшее fair-use в AI-training контексте. |
| 17 | **Commercial-safe AI** | Commercial-safe AI | Branding для AI-инструментов, обученных на licensed corpus (Adobe Firefly = Adobe Stock + licensed; vs scraped-from-web как Stable Diffusion). Снижает training-data legal risk, но не покрывает trademark / likeness / brand-context risk. |
| 18 | **Synthetic Performer** | Synthetic Performer | SAG-AFTRA contract category (2023 strikes): digitally created characters, не identifiable как specific people. Regulated через collective bargaining: нельзя использовать synthetic performer для замены реального performer'а без compensation. |

---

## Источники

Источники сгруппированы по разделам и темам. Внутри каждой группы — primary sources (официальные релизы, peer-reviewed работы, судебные ruling'и) + supporting (industry analysis, news coverage).

### Раздел 0: Mental model 3 семейств

1. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS 2020. arXiv:2006.11239.
2. Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2022). High-Resolution Image Synthesis with Latent Diffusion Models. CVPR 2022.
3. OpenAI (2024). Sora System Card. URL: https://openai.com/index/sora-system-card/.

### Раздел 1: Tools 2026 — models

4. OpenAI Sora 2 Complete Guide 2026 — WaveSpeed AI. URL: https://wavespeed.ai/blog/posts/openai-sora-2-complete-guide-2026/.
5. Sora 2 is here — OpenAI. URL: https://openai.com/index/sora-2/.
6. Sora 2 API Pricing & Quotas 2026 — AI Free API. URL: https://www.aifreeapi.com/en/posts/sora-2-api-pricing-quotas.
7. Sora 2 Pricing Calculator (May 2026) — CostGoat. URL: https://costgoat.com/pricing/sora.
8. Veo 3 Pricing 2026 — Veo3 AI. URL: https://www.veo3ai.io/blog/veo-3-pricing-2026.
9. Build with Veo 3.1 Lite — Google Blog. URL: https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/.
10. Google AI Studio — Veo 3. URL: https://aistudio.google.com/models/veo-3.
11. Runway Gen-4 Turbo Overview — MindStudio. URL: https://www.mindstudio.ai/blog/what-is-runway-gen-4-turbo-video.
12. Runway Review 2026: Gen-4.5 #1 Video Arena — AI Tool Analysis. URL: https://aitoolanalysis.com/runway-review/.
13. Kling AI Complete 2026 Guide — SimileVault. URL: https://similevault.com/kling-ai/.
14. Kling 3.0 Tutorial 2026 — Cliprise. URL: https://medium.com/@cliprise/kling-3-0-tutorial-the-complete-guide-to-4k-ai-video-generation-in-2026-0e8cfed0e042.
15. Midjourney Review 2026 — Revoyant. URL: https://www.revoyant.com/blog/midjourney-review.
16. Midjourney V7 Review 2026 — AI Coding Flow. URL: https://ai-coding-flow.com/blog/midjourney-review-2026/.
17. AI Image Generation APIs in 2026 — NovaKit. URL: https://www.novakit.ai/blog/ai-image-generation-apis-2026-compared.
18. The Complete Guide to AI Image Generation 2026 — Cliprise. URL: https://medium.com/@cliprise/ai-image-generation-in-2026-midjourney-flux-2-imagen-4-and-beyond-7934a9228e98.
19. How Much Does AI Image Generation Cost in 2026 — ImagineArt. URL: https://www.imagine.art/blogs/ai-image-generation-cost.
20. AI Art Cost: $0 Per Image Possible — ZSky AI. URL: https://zsky.ai/blog/how-much-does-ai-art-cost.
21. Genie 3 — Google DeepMind. URL: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/.
22. Genie 3 World Model 2026 — WaveSpeedAI. URL: https://wavespeed.ai/blog/posts/google-deepmind-genie-3-world-model-2026/.
23. ElevenLabs Dubbing Studio. URL: https://elevenlabs.io/dubbing-studio.
24. ElevenLabs Voice Cloning. URL: https://elevenlabs.io/voice-cloning.
25. ElevenLabs Review 2026 — Coval. URL: https://www.coval.dev/blog/elevenlabs-review-2026-voice-cloning-and-synthesis-capabilities-explained.
26. Adobe Firefly: Next Evolution (Adobe Blog April 2025). URL: https://blog.adobe.com/en/publish/2025/04/24/adobe-firefly-next-evolution-creative-ai-is-here.
27. Adobe MAX 2025 — Futurum. URL: https://futurumgroup.com/insights/adobe-max-2025-will-adobes-platform-approach-resonate-with-enterprises/.
28. Adobe Q4 FY 2025 Revenue — Futurum. URL: https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/.
29. Adobe Firefly partner models. URL: https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-non-adobe-models.html.

### Раздел 1 (Russian context)

30. SHADR — Kandinsky 6.0 Image, 29.04.2026. URL: https://www.shadr.info/news/2026/04/29/36773-sber_predstavil_kandinsky_60_image_flagmanskuyu_model_dlya_/.
31. 4PDA — Kandinsky 6.0 Image, 28.04.2026. URL: https://4pda.to/2026/04/28/455813/sber_provyol_masshtabnoe_obnovlenie_generatora_izobrazhenij_kandinsky_6_0_image/.
32. Sber Business — Kandinsky 6.0 Image release. URL: https://sberbusiness.live/news/sber-predstavil-kandinsky-60-image.
33. GitHub kandinskylab / kandinsky-5. URL: https://github.com/kandinskylab/kandinsky-5.
34. aifilms.ai studio — Kandinsky 5.0 Video. URL: https://studio.aifilms.ai/blog/kandinsky-5-video-generation.
35. vc.ru — Шедеврум обзор 2026. URL: https://vc.ru/aihub/2842605-shedrevum-ot-yandeks-vozmozhnosti-nevrosseti.
36. vc.ru — Шедеврум генерация видео 2026. URL: https://vc.ru/aihub/2842848-shedrevum-generatsiya-video.
37. Yandex Support — создание видео в Шедевруме. URL: https://yandex.ru/support/shedevrum/ru/video/create.
38. Sber Developers — SymFormer. URL: https://developers.sber.ru/portal/products/symformer.
39. Habr Sber — SymFormer Маэстро. URL: https://habr.com/ru/companies/sberdevices/articles/826118/.
40. Sber Developers — SaluteSpeech YourVoice. URL: https://developers.sber.ru/portal/products/smartspeech-yourvoice.
41. Habr studyai — аналоги Sora 2 / доступ для РФ. URL: https://habr.com/ru/companies/studyai/articles/1026652/.
42. Sostav — TOP-15 нейросетей для видео 2026. URL: https://www.sostav.ru/blogs/287107/77059.
43. CNews 12.03.2026 — обучение ИИ на авторских материалах. URL: https://www.cnews.ru/news/top/2026-03-12_v_rossii_razreshat_obuchat.
44. РИА Право — ИИ-контент и авторские права 2026. URL: https://riapravo.ru/intellekt/avtorskoe-pravo-i-ii-v-2026-godu-revoljuciya-zakonodatelstva-i-novye-riski/.
45. vc.ru legal — проект федерального закона об ИИ 2026. URL: https://vc.ru/legal/2847664-regulirovanie-ii-v-rossii-novyy-zakon-o-intellektualnoy-sobstvennosti.

### Раздел 2: Adoption + displacement

46. IAB U.S. Digital Video Ad Spend 2026. URL: https://www.iab.com/news/u-s-digital-video-ad-spend-to-surpass-80b-in-2026/.
47. IAB 2026 Video Ad Spend Report. URL: https://www.iab.com/insights/video-ad-spend-report-2026/.
48. AI Marketing Statistics 2026 — Digital Applied. URL: https://www.digitalapplied.com/blog/ai-marketing-statistics-2026-adoption-data-points.
49. 75 AI Video Statistics 2026 — Vivideo. URL: https://vivideo.ai/blog/ai-video-statistics-2026.
50. Stock photography decline — Kaptur. URL: https://kaptur.co/the-silent-collapse-generative-ais-erosion-of-photo-licensing-revenue/.
51. Stock photography dying — Tidewater Teddy. URL: https://tidewaterteddy.com/2025/01/10/stock-photography-is-dying/.
52. Getty + Shutterstock merger — Kaptur. URL: https://kaptur.co/the-authenticity-cartel-why-the-getty-shutterstock-merger-is-really-about-who-controls-real/.
53. Upwork AI Displacement — Jobbers Index. URL: https://www.jobbers.io/ai-job-displacement-index-which-freelance-skills-are-at-risk/.
54. Will AI Replace Graphic Designers — Upwork. URL: https://www.upwork.com/resources/will-ai-replace-graphic-designers.
55. SAG-AFTRA AI bargaining timeline. URL: https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence/sag-aftra-ai-bargaining-and.
56. WGA/SAG-AFTRA 2023 AI contracts — Perkins Coie. URL: https://perkinscoie.com/insights/blog/generative-ai-movies-and-tv-how-2023-sag-aftra-and-wga-contracts-address-generative.
57. 2026 WGA & SAG-AFTRA Negotiations — No Film School. URL: https://nofilmschool.com/2026-wga-contract-negotiations.
58. Lionsgate × Runway partnership — Variety VIP. URL: https://variety.com/vip/what-lionsgates-partnership-deal-runway-means-1236151418/.
59. Lionsgate × Runway — Lionsgate Investor Relations. URL: https://investors.lionsgate.com/news-events/news/news-details/2024/Runway-Partners-with-Lionsgate-in-First-of-its-Kind-AI-Collaboration/default.aspx.

### Раздел 3: Lawsuits — Copyright

60. NYT v OpenAI Lawsuit Update 2026 — Patent AI Lab. URL: https://medium.com/@patentailab/nyt-vs-openai-lawsuit-update-2026-did-regurgitation-kill-the-fair-use-defense-d63ff021b805.
61. OpenAI Must Turn Over 20 Million ChatGPT Logs — Bloomberg Law. URL: https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms.
62. NYT v Microsoft case docket — CourtListener. URL: https://www.courtlistener.com/docket/68117049/the-new-york-times-company-v-microsoft-corporation/.
63. Getty v Stability AI UK ruling — Bird & Bird. URL: https://www.twobirds.com/en/insights/2025/uk/stability-ai-defeats-getty-images-copyright-claims-in-first-of-its-kind-dispute-before-the-high-cour.
64. Getty v Stability — Mayer Brown analysis. URL: https://www.mayerbrown.com/en/insights/publications/2025/11/getty-images-v-stability-ai-what-the-high-courts-decision-means-for-rights-holders-and-ai-developers.
65. Andersen v Stability AI — Knowing Machines. URL: https://knowingmachines.org/knowing-legal-machines/legal-explainer/cases/andersen-v-stability-ai.
66. Andersen v Stability AI — Mesh IP Law tracker. URL: https://www.meshiplaw.com/litigation-tracker/andersen-v-stability-ai.
67. Thomson Reuters v Ross — Davis Wright Tremaine. URL: https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2025/02/reuters-ross-court-ruling-ai-copyright-fair-use.
68. Thomson Reuters v Ross — Reed Smith. URL: https://www.reedsmith.com/en/perspectives/2025/03/court-ai-fair-use-thomson-reuters-enterprise-gmbh-ross-intelligence.
69. RIAA sues Suno and Udio — RIAA press release. URL: https://www.riaa.com/record-companies-bring-landmark-cases-for-responsible-ai-againstsuno-and-udio-in-boston-and-new-york-federal-courts-respectively/.
70. Music Industry AI Lawsuits Tracker 2026 — Chartlex. URL: https://www.chartlex.com/blog/business/music-industry-ai-lawsuits-tracker-2026.
71. Suno AI Lawsuit Update Feb 2026 — Patent AI Lab. URL: https://patentailab.com/riaa-vs-suno-lawsuit-update-2026/.
72. EU AI Act transparency obligations — HSF. URL: https://www.hsfkramer.com/notes/ip/2026-03/transparency-obligations-for-ai-generated-content-under-the-eu-ai-act-from-principle-to-practice.
73. EU AI Act 2026 Compliance — Secure Privacy. URL: https://secureprivacy.ai/blog/eu-ai-act-2026-compliance.
74. Japan AI Copyright — Privacy World. URL: https://www.privacyworld.blog/2024/03/japans-new-draft-guidelines-on-ai-and-copyright-is-it-really-ok-to-train-ai-using-pirated-materials/.

### Раздел 3: Deepfakes & Likeness

75. Scarlett Johansson responds — Variety. URL: https://variety.com/2024/digital/news/scarlett-johansson-responds-shocked-angered-openai-chatgpt-her-1236011135/.
76. ScarJo / OpenAI — Northeastern. URL: https://news.northeastern.edu/2024/05/23/scarlett-johansson-open-ai/.
77. Drake AI Heart on My Sleeve — NPR. URL: https://www.npr.org/2023/04/21/1171032649/ai-music-heart-on-my-sleeve-drake-the-weeknd.
78. Drake AI submitted for Grammys — Variety. URL: https://variety.com/2023/music/news/ai-generated-drake-the-weeknd-song-submitted-for-grammys-1235714805/.
79. Taylor Swift deepfake controversy — Wikipedia. URL: https://en.wikipedia.org/wiki/Taylor_Swift_deepfake_pornography_controversy.
80. Taylor Swift X block — TIME. URL: https://time.com/6589487/taylor-swift-searches-blocked-x-twitter-deepfakes-response/.
81. Slovakia deepfake & 2024 election fakes — Ash Center Harvard. URL: https://ash.harvard.edu/articles/the-apocalypse-that-wasnt-ai-was-everywhere-in-2024s-elections-but-deepfakes-and-misinformation-were-only-part-of-the-picture/.
82. Biden robocall — NPR. URL: https://www.npr.org/2024/02/08/1229641751/ai-deepfakes-election-risks-lawmakers-tech-companies-artificial-intelligence.
83. South Korea Telegram deepfakes — NPR. URL: https://www.npr.org/2024/09/06/nx-s1-5101891/south-korea-deepfake.
84. Korea deepfake porn schools — Daily Star. URL: https://www.thedailystar.net/news/world/news/deepfake-porn-crisis-batters-south-korea-schools-3698986.
85. Arup deepfake CFO scam — CNN. URL: https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk.
86. Arup deepfake — Fortune. URL: https://fortune.com/europe/2024/05/17/arup-deepfake-fraud-scam-victim-hong-kong-25-million-cfo/.

### Раздел 3: Slop & Model Collapse

87. Shumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., & Anderson, R. (2024). AI models collapse when trained on recursively generated data. Nature, 631, 755–759.
88. Nature Machine Intelligence on AI Autophagy. URL: https://www.nature.com/articles/s42256-025-00984-1.
89. Google AI Overviews pizza/rock — ACS. URL: https://ia.acs.org.au/article/2024/google-goes-viral-after-ai-says-to-put-glue-on-pizza-eat-rocks.html.
90. Why Google AI Overviews fails — MIT Tech Review. URL: https://www.technologyreview.com/2024/05/31/1093019/why-are-googles-ai-overviews-results-so-bad/.
91. Sports Illustrated AI fake authors — CNN. URL: https://www.cnn.com/2023/11/27/media/sports-illustrated-deletes-articles-fake-author-names-ai-profile-photos/index.html.
92. Sports Illustrated scandal — Poynter. URL: https://www.poynter.org/commentary/2023/sports-illustrated-artificial-intelligence-writers-futurism/.
93. Amazon AI sham books — NPR / Authors Guild. URL: https://www.npr.org/2024/03/13/1237888126/growing-number-ai-scam-books-amazon.
94. Authors Guild: AI Sham Books surge. URL: https://authorsguild.org/news/ai-driving-new-surge-of-sham-books-on-amazon/.
95. Wizards of the Coast AI controversy — GeekWire. URL: https://www.geekwire.com/2024/wizards-of-the-coast-will-adjust-generative-ai-policy-for-magic-following-controversy/.
96. WotC reverses course — PC Gamer. URL: https://www.pcgamer.com/wizards-of-the-coast-reverses-course-admits-to-using-ai-in-promotional-image-well-we-made-a-mistake-earlier/.

### Раздел 3: Marketing & Ad Backlash

97. Coca-Cola Holidays Are Coming AI backlash — NBC News. URL: https://www.nbcnews.com/tech/innovation/coca-cola-causes-controversy-ai-made-ad-rcna180665.
98. Coca-Cola 2024 ad doubles down — Marketing AI Institute. URL: https://www.marketingaiinstitute.com/blog/criticism-ai-coke-holiday-ad.
99. Toys R Us Sora ad backlash — Hollywood Reporter. URL: https://www.hollywoodreporter.com/business/digital/toys-r-us-ad-sora-openai-video-tool-reaction-1235932993/.
100. Toys R Us sentiment plummet — Marketing-Interactive. URL: https://www.marketing-interactive.com/toys-r-us-sora-ai-sentiments-plummet.
101. Lensa AI controversy — TechCrunch. URL: https://techcrunch.com/2022/12/05/lensa-ai-app-store-magic-avatars-artists/.
102. Lensa AI signatures — ARTnews. URL: https://www.artnews.com/art-news/news/signatures-lensa-ai-portraits-1234649633/.

### Раздел 4: End-user rejection

103. YouTube AI Thumbnails fail — Banana Thumbnail. URL: https://blog.bananathumbnail.com/ai-youtube-thumbnails-2/.
104. YouTube CTR 2026 AI Thumbnails — Miraflow. URL: https://miraflow.ai/blog/youtube-ctr-2026-good-click-through-rate-ai-thumbnails.

### Supplementary / methodology

- Russell, S., & Norvig, P. (2021). Artificial Intelligence: A Modern Approach (4th ed.). Pearson. ISBN 978-0-13-461099-3.
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249–255.
- Bender, E. M., & Marcus, G. (2024+). Various public lectures and writings popularising «slop» term для AI-generated low-quality content.
- Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith, 598 U.S. 508 (Supreme Court 2023). Применяется для fair-use 4-factor test в Thomson Reuters v Ross.

---

## Changelog

- **v1 (2026-05-20):** initial draft from plan v2 + research dossiers (`2026-landscape.md` + `2026-russian-context.md`). Структура: 6 разделов (0-5) + Закрытие + Глоссарий + Источники. Объём ~13 200 слов. Failure-share по словам: ~52% strict-in (§3+§4+§5). Cross-references: Лекция 1 (framework), Лекция 3 (архитектуры), Лекция 5 (financial parallel), Лекция 7 (4-actor framework). Volatile facts помечены `[VFY-day-of]` (Sora 2 versions / pricing / standalone status, Suno SJ date, Sony status, Andersen trial date, Kandinsky 6.0 benchmarks, Минцифры законопроект status, YouTube thumbnails data freshness). 12 case-уроков в §3.2-§3.12, mapping на чек-лист в §5.2.

- **v2 (2026-05-20):** Batched P1+P2 revision per 3 critics (methodology + fact-checker + reader-simulator). Все 14 P1 + top 8 P2 fixes applied.

  **Methodology P1 fixes (3):**
  - M-P1.1: добавлен self-check блок в Раздел 5 (3 вопроса по чек-листу + mapping на §3 cases).
  - M-P1.2: добавлен **Урок для инженера** в конец §3.1 (taxonomy — 4 категории риска требуют разной mitigation; license check ≠ output similarity audit ≠ style restrictions ≠ consent management).
  - M-P1.3: усилен forward-reference к Лекции 9 в §6 — эскалация human-in-the-loop от brand-trust failure (Toys «R» Us sentiment dip) к kinetic outcome (LAWS / Project Maven / human-rated flight software).

  **Fact-checker P1 fixes (6):**
  - F-P1.1: Veo 3.1 pricing исправлен с «$0.05–$0.40 per video» на «$0.05/сек Lite, $0.40/сек Pro» (per-second, не per-video).
  - F-P1.2: §3.5 RIAA — корректно отражена матрица 3-major × 2-defendant. Warner settled Suno (сент 2025), но litigating Udio; UMG settled Udio (окт 2025), переговоры с Suno; Sony судится с обоими.
  - F-P1.3: Korea Telegram-чаты — конкретное «>230» смягчено до «более 200 (точное число fluctuates по разным reports)» с NPR + KCC sourcing.
  - F-P1.4: Amazon Kindle sham books — конкретное «19 из 100» удалено, replaced на verifiable surge claim с Frank Gioia / Ted Alkyer specific examples.
  - F-P1.5: IAB ad-spend — «в 2× быстрее общего ad market» исправлено на «~20% быстрее, чем общий ad market».
  - F-P1.6: Upwork «5.6M independent workers >$100k» удалено как unverified, replaced на verifiable premium-rate claim с footnote про volatile numbers + Upwork annual report.

  **Reader-simulator P1 fixes (5):**
  - R-P1.1: inline-расшифровка legal-jargon при первом появлении — SDNY, MTD, SJ, DMCA, CDPA, fair-use (4-factor test), discovery, class action.
  - R-P1.2: расшифровка acronyms — SAG-AFTRA (~160k members), WGA, RIAA, UMG/Sony/Warner (Big Three), AMPTP.
  - R-P1.3: §3.1 переписан — clean taxonomy primer 4 категорий без cases (cases остались в §3.2-§3.12). Добавлен primer юридических терминов в начале §3.1.
  - R-P1.4: добавлены 2 mini-summary breathing marks в §3 — после §3.6 (мост: copyright блок завершён → переход к voice/likeness §3.7-§3.8) и после §3.10 (мост: content-failures → market-reception и labor failures §3.11-§3.12).
  - R-P1.5: inline context для US-центричных entities — NYT, Toys «R» Us, Coca-Cola «Holidays Are Coming», Cannes Lions, Joe Russo (Marvel Avengers: Endgame).

  **P2 priority fixes (8):**
  - P2.1: typos — дentрализированный → дезориентированный; дисontonant → dissonant; Inженерный → Инженерный; стоимость / moделей / Кolloquial → corrected; commodific'ация — отсутствует в тексте.
  - P2.2: cross-product 3×4 matrix navigation повторно упоминается в §3.1 (Навигационная карта).
  - P2.3: fair-use 4 factors прямо перечислены в §3.6 (Thomson Reuters v Ross).
  - P2.4: mini-story 100 слов про wage compression в §2.4 — иллюстратор $40/час → $18-22/час pattern.
  - P2.5: RU-context expand — MAU Шедеврум >5M, FusionBrain.ai >2M monthly в §1.6.
  - P2.6: Suno v5 → v5.5 (consistent с research dossier 2026-05-20).
  - P2.7: Kandinsky 5.0 Video release date 18 → 20 ноября 2025; Kling 3.0 release 4 → 5 февраля 2026 (date-correct).
  - P2.8: Lionsgate Burns title «Vice Chairman» → «Vice Chair».

  **Word count delta:** v1 ~13 200 слов → v2 ~14 300 слов (+~1 100 от inline definitions + 2 breathing marks + §3.1 expand + wage-compression story + Self-check §5 + Лекция 9 forward-ref). В пределах target 12 000–14 500.

- **v3 (2026-05-20, Phase 11 batched revision):** Cross-artifact consistency sync per consistency-check v1. P2 fixes only (chapter changes minor):
  - §0.2: typo «Шумайстеру» → «Постепенно» (Russian flow word).
  - §1.1: «дискретизации standalone consumer-facing продукта Sora» → «прекращении поддержки standalone consumer-facing продукта Sora» (Russian-language clarity; «дискретизация» = math term).
  - §0.3 cross-product matrix: «$9.1B AI video ad spend» → «$9.1B AI-specific video ad spend (subset $80B total)» (disambiguate AI-specific subset vs total digital video ad spend per IAB 2026).
  - Word count delta: negligible (~+15 слов).

  **Остаточные uncertainties:**
  - Specific Frank Gioia / Ted Alkyer claim — sourced через Authors Guild press release URL, но точные slight-modified названия книг не verified в primary source (sufficient confidence for chapter, может потребовать VFY в день лекции).
  - Veo 3.1 Pro $0.40/sec vs $0.50/sec — пометил VFY-day-of; pricing volatile.
  - Warner ↔ Udio status «по-прежнему litigation, settlement не подписан на 2026-05-20» — текущее understanding на момент revision; может change к моменту лекции.

---

*Конец главы 8. Версия v2 (draft). Pending USER GATE A — chapter approval.*
