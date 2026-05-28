# Extracts from 16 industry chapters (Lec-01 — Lec-16)

**Цель файла:** structured input для plan-v1 Лекции 17 (capstone курса). Каждая запись извлекает: keystone-ось / cornerstone-концепты / documented failures + lessons / AI-unfit criteria / non-AI alternatives / 2D-position (AI fit × Autonomy) / current named tools.

**Контекст:** Лекция 17 — capstone, синтезирующий 16 отраслевых лекций (L1-L16) в единую инженерную модель. Несущая ось — 2D-плоскость: горизонталь = AI fit (от детерминированный non-AI до full AI); вертикаль = Лестница автономии L0→L5 (advisory → fully autonomous).

**Source status:** L1-L14 — produced/finalized в main; L15 — produced в main (PR #146); L16 — in worktree `/tmp/lec-16-wt`.

---

## L01 — Введение в AI

**Keystone-axis:** «Где AI работает, где — нет, и как это понять?» (диагностический вопрос курса; четыре способа реализации модель / чат / агент / приложение + квадрант 2×2 «задача × модальность»).

**Главные cornerstone-концепты (L17 reusable):**
- AI Effect (McCorduck) — «AI is whatever hasn't been done yet» (Tesler) — определение AI всегда сдвигается → объясняет, почему курс не строится вокруг технологии, а вокруг навыка.
- Quadrant «задача × модальность» × «модель/чат/агент/приложение» — первый из шести фреймворков курса.
- ISO/IEC 22989:2022 — оперативное определение AI-системы.
- Три уровня причинности Pearl (ассоциация → вмешательство → контрфактуальность) — ключ к «человек vs AI».
- Narrow vs General AI; AGI как market statement (Altman / Amodei / Hassabis / LeCun сводка с material interest).
- Bias / Sycophancy / Distribution shift как три проявления одной природы.
- Парадокс Моравека — то, что трудно для человека, легко для AI; то, что легко, — трудно.

**Documented failures + lessons:**
- **Samsung 2023.** Инженеры загрузили в потребительский ChatGPT проприетарный код и транскрипты совещаний. Урок: никогда не загружать конфиденциальные данные в потребительские AI-сервисы без проверки tariff policy. Альтернатива — Enterprise/API tariff с ZDR, или локальное развёртывание (LLaMA / Mistral / DeepSeek через Ollama / vLLM).
- **OpenAI GPT-4o sycophancy April 2025.** Обновление 25 апреля сделало модель «подлизой»; 28 апреля начат откат, 29 апреля postmortem. Урок: RLHF-разметка systematic biases the model toward agreement → sycophancy hard to detect because user receives compliments.
- **DeepSeek в России: 20% (ВЦИОМ) vs 43% (Microsoft telemetry).** Урок: прежде чем сравнивать AI-цифры, сравните методологии. Самоотчёт ≠ телеметрия.
- **AI Pilot Purgatory в РФ ~90%.** 30-40% пилотов закрываются без эффекта, 7-10% доходят до production (CNews/Vedomosti/Intellectual Analytics март 2026).

**AI-unfit criteria (L1):**
- Задачи на уровне 3 причинности Pearl (контрфактуальные «что было бы, если» / эпистемические вопросы) — AI structurally not capable.
- Conflict-of-interest sources (AGI predictions с material interest) — proven systematic bias.
- Любой fact requiring external verification (галлюцинации до 15% на reasoning задачах по Vectara HHEM).

**Non-AI alternatives:**
- Detection of hallucinations: Google Scholar DOI lookup (10-15 sec проверка).
- Avoiding consumer-tier leaks: ZDR enterprise contract, локальная модель.
- Pearl level 3 questions: human expert judgement.

**Position на 2D-плоскости:** L01 — не отрасль, а meta-frame. Координат не имеет; задаёт оси.

**Tools (2026):** ChatGPT 900M WAU; Claude (Anthropic); Gemini; YandexGPT, GigaChat, Шедеврум; LLaMA 4 / Mistral Large / DeepSeek-R1 локально через Ollama / LM Studio / vLLM.

---

## L02 — Как работают современные большие модели

**Keystone-axis:** 4-этапный конвейер inference LLM — токенизация → эмбеддинг → внимание → сэмплинг (с прямыми инженерными следствиями каждого этапа).

**Главные cornerstone-концепты (L17 reusable):**
- Slepota к буквам (strawberry → [st][raw][berry], 3 токена) — почему LLM не может точно сосчитать буквы или работать посимвольно.
- Эмбеддинг-пространство — базовый слой RAG; semantic-поиск.
- Self-attention + context window — почему есть «lost in the middle».
- Сэмплинг + температура — стохастичность ответа.
- Авторегрессионная природа длинного ответа.
- Scaling laws (Kaplan et al., 2020) + few-shot learning (GPT-3 175B).

**Documented failures + lessons:**
- Strawberry test (2024) — модели не умели сосчитать R-ы. Урок: ограничение токенизации, НЕ ограничение «интеллекта».
- Distribution shift на устаревшем коде 2023 → 2026: модель уверенно предлагает старую библиотеку.

**AI-unfit criteria (L2):**
- Точная посимвольная работа — не LLM, внешний инструмент.
- Long-context tasks где «lost in the middle» доминирует.

**Non-AI alternatives:**
- Регулярные выражения и парсеры для строгой структуры текста.
- Tool use: LLM делегирует посимвольную задачу внешнему calculator/regex tool.

**Position на 2D-плоскости:** L02 — fundamentals, не отрасль. Объясняет, почему AI fit падает на determinism-tasks и precision-арифметике.

**Tools (2026):** tiktoken (BPE), SentencePiece, GPT-4o (o200k_base), Llama-3, BERT.

---

## L03 — Архитектуры AI-систем: агенты, RAG, API

**Keystone-axis:** «Выбор архитектуры AI-системы — инженерное решение под конкретную задачу, а не следование моде. Часто правильный ответ — самая простая из возможных архитектур. Иногда — вообще не использовать ИИ.»

**Главные cornerstone-концепты (L17 reusable):**
- Иерархия архитектур: prompt → RAG → агент → fine-tune (4 уровня сложности).
- Golden set — эталонная разметка для оценки качества RAG.
- Reliability compounding — multi-step агент с p=0.95 на шаг → p_total=0.59 за 10 шагов.
- Plan → Act → Check → Iterate петля + 4 режима её отказа.
- $4,200-петля — провал кейс агентного бесконечного цикла без budget guard.
- Multi-agent хрупкость — Salesforce TauBench показал, что мульти-агентные системы fail in >60% случаях на complex tasks.

**Documented failures + lessons:**
- **Провал #1 ($4,200-петля).** Bare-metal API агент без budget cap → infinite recursion → $4,200 за ночь. Урок: всегда rate-limit + budget guard + max-turns.
- **Провал #3 (reliability compounding).** 10-step агент с 95% per-step → 59% end-to-end. Урок: каждый шаг multiplies error; иногда RAG лучше агента.
- **Провал #15 (мульти-агентная хрупкость).** Multi-agent чащё ломается, чем single agent с tools. Урок: «больше агентов = больше координационных провалов».

**AI-unfit criteria (L3):**
- Задачи требующие ≥10 reliable steps end-to-end без HITL.
- Задачи где golden set построить дороже самого решения.
- Real-time low-latency where агент-петля добавляет seconds.

**Non-AI alternatives:**
- Simple if-then rules + scheduled batch processing.
- Operations research (LP/ILP/TSP) для optimization tasks.
- Workflow automation (Zapier / n8n) без LLM где правила детерминистичны.

**Position на 2D-плоскости:** L03 — фундамент архитектурного выбора. AI fit ↑ на well-structured retrieval/QA; autonomy L1-L2 для RAG, L3 для агентов в narrow domain.

**Tools (2026):** OpenAI Assistants API, Claude Code, LangChain, LlamaIndex, Pinecone/Weaviate/Chroma (vector DB), Cohere Rerank, Anthropic Computer Use, Operator.

---

## L04 — AI в разработке ПО

**Keystone-axis:** «Уровни вмешательства A → B → C → D» — Autodetect (autocompletion) → Block-level (mid-task) → Coding-agent (PR-from-spec) → Engineering-agent (issue → merged PR). **Mapping a РЕЖИМ, не бренд** (Copilot=A+B+C+D, Cursor=A+B+C, Claude Code=C+D).

**Главные cornerstone-концепты (L17 reusable):**
- A/B/C/D autonomy ladder в SE — narrow domain пример лестницы автономии для capstone.
- Slopsquatting — атака через generated package names (несуществующие npm/pip packages, поскольку модели hallucинируют имена → атакующие занимают эти имена).
- Gartner-hedge: «GenAI productivity gains оверестимируются примерно в 2-3 раза» (Gartner June 2025).
- Сопровождающий = maintainer (cascade-rename: Решение #103).

**Documented failures + lessons:**
- **Curl maintainer overload by AI-bug-bounty.** Daniel Stenberg публично возмутился — AI-generated bug reports топили мейнтейнеров (~70% spam). Урок: low-cost AI generation + high-cost human review = асимметрия → backlog.
- **DevinAI overpromise 2024.** $2B оценка, demo впечатлила, реальная success rate на SWE-bench низкая. Урок: demo ≠ production.
- **Slopsquatting.** Researchers showed Claude / GPT-4 hallucinated package names; some attackers зарегистрировали эти имена → supply chain attack. Урок: AI-generated code IMPORT statements нуждаются в verification.

**AI-unfit criteria (L4):**
- Safety-critical production code без human review.
- Long-term architecture decisions с repository-wide context.
- Code refactoring where intent matters больше syntax.

**Non-AI alternatives:**
- Static analysis (SonarQube, Coverity) — детерминистичный SAST.
- Code-review by senior engineer.
- Type systems и compilers как «правда».

**Position на 2D-плоскости:** Software dev — высокий AI fit (text/code modality + ground-truth feedback от compiler), но autonomy capped at L3 (C-уровень PR-from-spec) для production code.

**Tools (2026):** GitHub Copilot (20M+ users, 46% code), Cursor (Tab/Composer/Agent), JetBrains AI, Claude Code, Devin, Aider, Tabnine, Sourcegraph Cody.

---

## L05 — AI в финансовом секторе и ритейле

**Keystone-axis:** «Какие задачи в финансах/ритейле — для AI, какие — для не-AI» через 6 разделов (forecasting / anomaly detection / scoring / customer service / recommendations / pricing-personalization).

**Главные cornerstone-концепты (L17 reusable):**
- Cost-sensitive learning ≠ precision↔recall — отдельные оси.
- iBuying как класс — пилоты с алгоритмическим ценообразованием домов.
- Trade-finance vs retail-CX вертикали с разной risk tolerance.
- PII (Personally Identifiable Information) и regulatory baseline (cbr.ru Consultation Paper 2025-11-20 «Применение ИИ на финансовом рынке»).

**Documented failures + lessons:**
- **Zillow Offers 2021.** iBuying-алгоритм неверно оценил недвижимость → $304M loss, 25% workforce laid off, exit. Урок: open-world prediction (рынок недвижимости) ≠ closed-world ML; volatility убивает.
- **Apple Card gender bias 2019.** Algorithm gave wives lower credit limits than husbands. Урок: bias из исторических данных fixes только через данные, не через модель.
- **Air Canada chatbot 2024.** Chatbot обещал refund policy, не существовавшую; суд обязал авиакомпанию выполнить обещание. Урок: chatbot — official communication channel; галлюцинация = contractual liability.
- **Klarna AI customer service 2024.** CEO сказал AI заменил 700 операторов; через год — обратный найм. Урок: AI на long-tail support ломается; high-margin cases требуют human.
- **Wendy's drive-thru AI 2023.** AI на drive-thru заказе вёл клиента в петлю «$70 за $7 еды». Урок: voice + noisy environment + complex menu = AI fails reliably.

**AI-unfit criteria (L5):**
- Open-world price prediction (Zillow iBuying).
- High-stakes credit decision без explainability (SHAP мандат).
- Adversarial environments где user actively жmет систему.

**Non-AI alternatives:**
- ARIMA / GBM (gradient boosting) для time series — часто лучше LLM.
- Rule-based fraud detection + human review for borderline cases.
- Historical pricing tables для commodity items.

**Position на 2D-плоскости:** Финансы/ритейл — high AI fit на closed-world forecasting (demand, fraud); low AI fit на open-world (iBuying, customer trust); autonomy mostly L1-L2 (advisory + alerting), L3 только в fraud auto-block.

**Tools (2026):** Stripe Radar, Visa AI, Mastercard Decision Intelligence, Sberbank GigaChat для финансов, Х5/Магнит forecasting (Yandex), CatBoost/LightGBM, Replicant voice AI, Klarna AI assistant (deprecated).

---

## L06 — AI в инженерном проектировании и CAD/CAM

**Keystone-axis:** Шесть классов AI в CAD/CAM на оси «детерминированное ↔ вероятностное», каждый с явным «подходит / не применим / классическая альтернатива»:
1. Оптимизационный ML / топологическая оптимизация
2. Эволюционные / генетические алгоритмы
3. Суррогатные модели / PINN
4. Computer Vision
5. LLM-ассистент
6. Генеративный AI для геометрии

**Главные cornerstone-концепты (L17 reusable):**
- «Garbage-in → optimal garbage» — оптимизатор честно выдаст оптимум под неверную постановку.
- POD (Probability of Detection) — нормативная метрика NDT.
- Nemenstvo: «generative design» в маркетинге ≠ generative AI (часто это deterministic topology optimization).
- ORCA benchmark CAD-LLM (45-63% accuracy на инженерных задачах).

**Documented failures + lessons:**
- **GM Seat Bracket (Autodesk 2018) — формально success.** 8 деталей → 1; -40% mass / +20% strength; 150 вариантов. Урок: это **оптимизационный ML**, не generative AI. «150 вариантов» — это 150 точек KKT, не 150 сэмплов нейросети.
- **NASA ST5 antenna (2006).** GA нашёл «органическую» антенну за 3 person-months vs 5 classical. Урок: эволюционная форма не интерпретируема → проблема для сертификации.
- **LLM hallucination on material grades / standards.** «Какая марка стали для X?» → confidently wrong. Урок: LLM не источник истины по нормативам.

**AI-unfit criteria (L6):**
- Безопасностно-критичный NDT (как единственный арбитр).
- Финальные сертификационные расчёты (всегда полный МКЭ).
- Источник истины по маркам материалов, ГОСТ-номерам, допускам.
- Точные допуски, посадки, сборочные зазоры для деталей в production.

**Non-AI alternatives:**
- Параметрический CAD + ручной выбор сечений по сортаменту + норматив.
- Нормативный расчёт без оптимизации для типовых конструкций.
- Аттестованный дефектоскопист с POD-методикой.
- Нормативная база + справочник-марочник.

**Position на 2D-плоскости:** CAD/CAM — mid AI fit (зависит от класса); autonomy mostly L1 (advisory) для finals; L3-L4 для optimization (RL/GA).

**Tools (2026):** Autodesk Fusion (generative), Ansys SimAI (2026 R1), Altair PhysicsAi / HyperWorks 2026 («до ~1000×» surrogate), Dassault Systèmes (3DEXPERIENCE), Siemens NX. РФ: топологическая оптимизация без generative-engine (честный gap).

---

## L07 — AI в медицине и фармацевтике

**Keystone-axis:** «Какие обещания AI в медицине сбылись» — карта (диагностика / drug discovery / explainability+ethics), с акцентом на **closed-loop среды** (операционная, контролируемый эксперимент) vs open-world.

**Главные cornerstone-концепты (L17 reusable):**
- HITL (Human-In-The-Loop) как стандарт медицинского AI.
- AlphaFold2 (Jumper et al., 2021) — 200M белков, Нобель 2024.
- RCT (Randomized Controlled Trial) как ground truth для drug efficacy.
- Chester AI как пример рентгенографического deep learning.
- FDA 21 CFR Part 11 — regulatory anchor.
- Доказательная медицина как фрейм оценки AI-claims.

**Documented failures + lessons:**
- **IBM Watson for Oncology 2018-2022.** Multi-$B project, рекомендовал unsafe treatments, MD Anderson отказался, IBM продала Watson Health (~$1B). Урок: training data ≠ clinical practice; AI doesn't replace physician judgment.
- **Epic Sepsis Model (Wong et al. JAMA 2021).** AUC 0.63 vs claimed 0.76; false-alert flooding. Урок: vendor benchmarks ≠ deployment performance; всегда replicate measurement.
- **Babylon Health 2023.** AI-triage app collapsed → administration, Bupa acquired remnants. Урок: regulatory + clinical complexity overwhelms AI-first product.

**AI-unfit criteria (L7):**
- Clinical decision as sole arbiter (regulatory + ethical block).
- Rare disease prediction где training data thin.
- Treatment selection без RCT validation.

**Non-AI alternatives:**
- Clinical guidelines (NICE, USPSTF, Минздрав).
- Doctor-patient consultation (Pearl level 3 questions).
- Established biomarkers (PSA, HbA1c) for monitoring.

**Position на 2D-плоскости:** Медицина — high AI fit на narrow imaging tasks (X-ray, retina); low AI fit на open-world clinical decision; autonomy L1 (assistive) is regulatory norm.

**Tools (2026):** AlphaFold3, Chester AI, Aidoc, Tempus, PathAI; OpenAI Whisper для transcription; Epic AI Sepsis Model (FAIL); IBM Watson Health (defunct).

---

## L08 — AI в креативных индустриях и медиа

**Keystone-axis:** «AI добавил → изменил → сломал» (3 времени) × 4 области (визуал / аудио / текст-журналистика / кино-VFX). Cross-product таксономия 4×3.

**Главные cornerstone-концепты (L17 reusable):**
- Diffusion models (Stable Diffusion, Midjourney, DALL-E 3) — text-to-image.
- Voice cloning + deepfake — provenance attack vectors.
- Generative pipelines — Photoshop Generative Fill, Adobe Firefly, Sora video.
- Copyright lawsuits как regulatory pressure (NYT v. OpenAI 2023, Getty v. Stability 2023).
- Coalition for Content Provenance and Authenticity (C2PA) — провенанс standard.

**Documented failures + lessons:**
- **Getty Images v. Stability AI 2023.** Watermarks Getty visible in generated images. Урок: training data contamination → IP liability.
- **NYT v. OpenAI 2023.** Verbatim regurgitation of paywalled articles. Урок: large-context retrieval может leak training data.
- **Hollywood SAG-AFTRA strike 2023.** Studios wanted to scan background actors → strike. Урок: human creative labour ≠ replaceable; consent + provenance required.
- **Deepfake fraud — CEO voice clones $25M Hong Kong 2024.** Урок: voice cloning + video conferencing = new fraud vector.

**AI-unfit criteria (L8):**
- Authentic creative authorship (vs assisted authoring).
- Investigative journalism source verification.
- Forensic photo analysis.

**Non-AI alternatives:**
- Human creative direction + photoshop manual.
- C2PA-signed provenance для journalism.
- Human voice actors with NDA + consent.

**Position на 2D-плоскости:** Креатив — high AI fit на mass-production assets (concept art, B-roll, marketing); low AI fit на signature creative work; autonomy L2-L3 (AI generates, human curates).

**Tools (2026):** Midjourney v7, DALL-E 3, Stable Diffusion XL/SD3, Adobe Firefly, ElevenLabs, Suno, Runway Gen-3, Sora, Pika, Adobe Premiere AI, DaVinci Resolve AI.

---

---

## Continuation

**L09-L16 + cross-lecture synthesis (failure patterns, cornerstone glossary, 7 criteria, open questions):** см. `extracts-part2.md`.
