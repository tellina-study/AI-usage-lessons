---
name: glossary-ru-en
issue: 172
status: locked
terms_count: 123
---

# RU→EN Terminology Glossary (course "AI-usage-lessons")

**Phase 1 anti-drift lock (issue #172).** This is the single source of truth for how course terminology is rendered in English **identically across all 16 lectures**. When a translator or reviewer meets a term below, use the EN column exactly. If a needed term is missing, add it here first (bump `terms_count`), then use it — never invent a one-off variant in a lecture.

This is a **lock of the load-bearing terms**, not an exhaustive thesaurus.

## Translation conventions

- **Target reader:** international practicing engineers (not academics, not the general public). Assume familiarity with software engineering, unfamiliarity with the Russian market.
- **Tone:** match the Russian — direct, teacherly, occasionally blunt. Do **not** make it more formal or more hedged than the source.
- **US-English spelling** throughout (e.g., "behavior", "labeling", "optimize", "specialized").
- **Keep established English acronyms untranslated:** LLM, RAG, MCP, GPT, API, ML, DL, NLP, CV, RLHF, SDLC, ADR, PR, ROI, ODD, SAE, HITL, TSP/VRP, C2PA — do not localize; expand on first use only where the source does.
- **Do not translate brand / product / model names:** ChatGPT, GigaChat, YandexGPT, Sora 2, Suno, Adobe Firefly, See & Spray, etc. — keep verbatim. Latin-script Russian brands (X5, Ozon) stay as-is.
- **Proper nouns (Part B):** on first use in a lecture, render with the transliteration plus the inline gloss phrase given below (e.g., "Magnit (a large Russian grocery retailer)"). Later uses: transliteration alone.
- **Numbers, dates, and facts are preserved exactly** — never round, convert currency, or "adjust" a statistic during translation. Keep the source unit (kg/acre, ₽, RUB) and add a conversion only in parentheses if the source did.
- **The failure/lesson framing is core to the course** — render "провал" as *failure* and "урок" as *lesson (learned)* consistently; do not soften to "issue" or "takeaway".

## Part A — Terms (AI / ML / course-specific)

| RU | EN (US) | Note |
|---|---|---|
| искусственный интеллект (ИИ) | artificial intelligence (AI) | Prefer the acronym AI in body text, matching source AI-first usage. |
| машинное обучение | machine learning (ML) | |
| глубокое обучение | deep learning (DL) | |
| нейросеть / нейронная сеть | neural network | |
| большая языковая модель | large language model (LLM) | |
| фундаментальная / базовая модель | foundation model | |
| модель рассуждений | reasoning model | e.g. o1/o3, DeepSeek-R1. |
| рассуждение (модели) | reasoning | Not "reflection". |
| механизм внимания / внимание | attention (mechanism) | Keystone term of Lecture 2. |
| self-attention / самовнимание | self-attention | Keep English; RU gloss optional. |
| трансформер | transformer | |
| токен | token | |
| токенизация | tokenization | |
| прогноз следующего токена | next-token prediction | |
| эмбеддинг (векторное представление) | embedding | |
| векторное пространство | vector space | |
| векторная база данных | vector database | |
| контекстное окно | context window | |
| промпт | prompt | |
| системный промпт | system prompt | |
| промптинг / инженерия промптов | prompting / prompt engineering | |
| обучение по нескольким примерам | few-shot learning | |
| законы масштабирования | scaling laws | |
| предобучение | pretraining | |
| дообучение / тонкая настройка | fine-tuning | Both RU forms → the one EN term. |
| обучение с учителем | supervised learning | |
| обучение без учителя | unsupervised learning | |
| самообучение / self-supervised | self-supervised learning | |
| обучение с подкреплением | reinforcement learning (RL) | |
| RLHF (обучение с подкреплением на основе обратной связи от человека) | RLHF (reinforcement learning from human feedback) | Keep acronym. |
| разметка (данных) | (data) labeling | US spelling, one "l". |
| размеченные данные | labeled data | |
| дистилляция | distillation | |
| квантизация | quantization | |
| градиентный бустинг | gradient boosting | XGBoost/LightGBM/CatBoost. |
| индуктивное смещение | inductive bias | |
| инференс | inference | |
| галлюцинация | hallucination | |
| галлюцинировать | to hallucinate | |
| подстраивание под данные | fitting to the data | Umbrella term in L1 §4.4 for bias/sycophancy/drift. |
| смещение / предвзятость | bias | Statistical/model bias, not "inductive bias". |
| подхалимство / угодливость модели | sycophancy | |
| дрейф распределения | distribution shift | RU gloss locked as "дрейф", not "сдвиг". |
| крайний случай | edge case | |
| открытые веса | open weights | |
| открытая модель | open(-weight) model | |
| self-hosting / развёртывание у себя | self-hosting | |
| локальная модель | local model | vs cloud model. |
| облачная модель | cloud model | |
| бенчмарк | benchmark | |
| агент | agent | |
| агентный ИИ | agentic AI | |
| уровни автономии / автономность | levels of autonomy / autonomy | |
| автономный | autonomous | |
| человек в контуре | human-in-the-loop (HITL) | Also human-on/out-of-the-loop → -on/-out-of-the-loop. |
| планирование | planning | Agent capability. |
| инструменты (агента) | tools | |
| препроцессинг / постпроцессинг | preprocessing / postprocessing | |
| задача (тип задачи) | task (task type) | Classification axis A. |
| классификация | classification | |
| распознавание | recognition | |
| поиск (retrieval) | retrieval | |
| генерация | generation | |
| генеративная модель | generative model | |
| прогноз / прогнозирование | forecasting / prediction | "regression/forecasting" per source. |
| прогнозная модель | predictive model | |
| прогноз спроса | demand forecasting | |
| модальность | modality | |
| мультимодальный | multimodal | |
| компьютерное зрение | computer vision (CV) | |
| обработка естественного языка | natural language processing (NLP) | |
| diffusion-модель | diffusion model | Keep English "diffusion". |
| латентное пространство | latent space | |
| синтез речи / нейросинтез аудио | neural audio synthesis | |
| клонирование голоса | voice cloning | |
| дипфейк | deepfake | |
| водяной знак / провенанс контента | watermark / content provenance | C2PA context. |
| провал | failure | Course-core; never "issue". |
| режим провала | failure mode | |
| выученный урок / урок | lesson (learned) | Course-core. |
| ограничение (подхода) | limitation | |
| несущая ось (лекции) | keystone axis | Course-internal production term. |
| закрытая среда / замкнутый контур | closed environment / closed-loop | L10 keystone pair. |
| открытая среда | open environment | |
| структурированность среды | environment structure | L13 keystone predictor. |
| базовая линия / точка отсчёта | baseline | For measurable-claim denominators. |
| контрфактическая оценка | counterfactual | |
| эффект (величина эффекта) | effect (effect size) | |
| пилот (AI-пилот) | pilot (AI pilot) | |
| промышленное развёртывание | production deployment | vs demo/pilot. |
| производительность | productivity | Not "performance". |
| проникновение (внедрения) | adoption / penetration | |
| жизненный цикл разработки ПО | software development lifecycle (SDLC) | |
| спецификация (спека) | specification (spec) | spec-driven → spec-driven. |
| дисциплина (инженерная) | discipline | L4 "practice, not tool" axis. |
| зима AI | AI winter | |

## Part B — Proper nouns (companies / organizations / sources)

On first use: transliteration + inline gloss. Latin-script brands kept as-is.

| RU | EN (translit) | Gloss (first-use, for international reader) |
|---|---|---|
| Сбер / Сбербанк | Sber / Sberbank | largest Russian bank, now a tech-and-AI conglomerate |
| GigaChat | GigaChat | Sber's large language model (keep as-is) |
| Яндекс | Yandex | leading Russian internet/search-and-services company |
| YandexGPT | YandexGPT | Yandex's LLM (keep as-is) |
| Шедеврум | Shedevrum | Yandex's consumer text-to-image app |
| Кандинский | Kandinsky | Sber's text-to-image model |
| Магнит | Magnit | large Russian grocery-retail chain |
| X5 | X5 | major Russian food retailer (Pyaterochka/Perekrestok); keep as-is |
| Wildberries | Wildberries | largest Russian e-commerce marketplace; keep as-is |
| Ozon | Ozon | major Russian e-commerce marketplace; keep as-is |
| Т-Банк (Тинькофф) | T-Bank (formerly Tinkoff) | large Russian digital bank |
| МТС | MTS | major Russian telecom operator |
| Ростелеком | Rostelecom | Russian state telecom incumbent |
| Мегафон | MegaFon | major Russian mobile operator |
| СИБУР / Сибур | Sibur | largest Russian petrochemicals producer |
| Норникель | Nornickel | Russian mining/metals major (nickel, palladium) |
| Росатом | Rosatom | Russian state nuclear-energy corporation |
| РЖД | RZD | Russian Railways (state rail monopoly) |
| Газпром | Gazprom | Russian state-controlled gas major |
| Роснефть | Rosneft | Russian state-controlled oil major |
| Северсталь | Severstal | large Russian steel producer |
| ММК | MMK | Magnitogorsk Iron & Steel Works |
| Самолёт | Samolet | large Russian residential developer |
| ВЦИОМ | VCIOM | Russian state pollster (public-opinion research center) |
| Минцифры | Mintsifry | Russian Ministry of Digital Development |
| Минсельхоз | Minselkhoz | Russian Ministry of Agriculture |
| Сколково | Skolkovo | Russian innovation hub / tech park near Moscow |
| Cognitive Pilot | Cognitive Pilot | Russian agri-autonomy firm (Sber/Cognitive Tech JV); keep as-is |
| CNews / Vedomosti / Intellectual Analytics | CNews / Vedomosti / Intellectual Analytics | Russian business/IT media & analytics sources; keep as-is |
