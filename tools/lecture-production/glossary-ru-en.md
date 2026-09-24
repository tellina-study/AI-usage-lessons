---
name: glossary-ru-en
issue: 172
status: locked
terms_count: 219
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
| радиус разрушения / масштаб поражения | blast radius | Locked (heavy use L14/L17). |
| канареечный деплой / канарейка | canary (release / deployment) | L14/L17. |
| откат | rollback | L17. |
| поэтапное раскатывание | staged rollout | L15/L17. |
| привязка к вендору | vendor lock-in | L17. |
| усиление (не замена) | augmentation (not replacement) | Course framing, L17. |
| парадокс автоматизации | automation paradox | L15/L17. |
| склонность доверять автомату | automation bias | L15/L17. |
| инъекция в промпт | prompt injection | L14/L17; keep EN term. |
| матрица ошибок | confusion matrix | Metrics cluster L5/L7. |
| ошибка первого / второго рода | type I / type II error | |
| точность (accuracy) | accuracy | RU «точность» is ambiguous — disambiguate by context. |
| точность (precision) vs полнота | precision vs recall | The other sense of «точность». |
| чувствительность | sensitivity | L7 (= recall in medical). |
| специфичность | specificity | L7. |
| положительная прогностическая ценность | positive predictive value (PPV) | L7. |
| распространённость | prevalence | L7. |
| скрининг | screening | L7. |
| аварийный выключатель | kill switch | L5. |
| суррогатная модель | surrogate model | L6 CAE. |
| оптимизация топологии | topology optimization | L6. |
| генеративный дизайн | generative design | L6. |
| метод конечных элементов | finite element analysis (FEA) | L6. |
| экипировка / оснастка агента | harness (agent harness) | L3 keystone; keep EN term. |
| разрыв восприятия | perception gap | L4 keystone; source introduces the EN term. |
| рубежный контроль (РК) | midterm (RK1/2/3 → Midterm 1/2/3) | Course assessment. |
| посещаемость | attendance | Course assessment. |

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
| Росздравнадзор | Roszdravnadzor | Russian medical-devices/healthcare regulator (L7) |
| Ростехнадзор | Rostekhnadzor | Russian industrial-safety regulator (L6) |
| ЕСКД | ESKD | Unified System of Design Documentation (Russian eng-drawing standard, L6) |
| АСКОН | ASCON | Russian CAD/PLM vendor (Kompas-3D), L6 |
| Третье Мнение | Third Opinion | Russian medical-imaging AI vendor (translate name; L7) |

## Part C — Seminar 4 terms (coding-agent setup: day-0 baseline vs wait for a signal)

Added for the Seminar 4 EN track (issue #204 pattern). The **axis terms** and the **case-machinery terms** below recur 20-120× each across 57 slides, so a one-off variant in any single slide reads as a different concept. Part A/B still win where they overlap (`экипировка` → *harness*, `провал` → *failure*, `слот` → *slot*), and the Lecture 3 EN deck is the upstream anchor for the harness vocabulary this seminar continues.

| RU | EN (US) | Note |
|---|---|---|
| Сборка кодинг-агента | Setting up a coding agent | Seminar 4 title. Not "assembling"/"building" — the seminar is about configuration decisions. |
| день-0 база | day-0 baseline | Keystone axis, left half. Hyphenated attributively: *a day-0 baseline practice*. |
| день-0-практика | day-0 practice | |
| жди сигнала | wait for a signal | Keystone axis, right half. Imperative, matching the RU. |
| по сигналу | on a signal | The classification label paired with "day 0". |
| сигнал | signal | Never "trigger" in this seminar: Lecture 3 EN uses *trigger* for harness complication; here the RU is consistently «сигнал» and the distinction is load-bearing. |
| на дне 0 / в первый день | on day 0 / on the first day | |
| гейт готовности | readiness gate | The `CLAUDE.md` line requiring tests + a manual check before saying "done". Deliberately **not** "definition-of-done gate" — that imports Scrum baggage the RU does not carry. |
| критерий «готово» | the "done" criterion | Keep the quotes around *done*, as the RU does around «готово». |
| файл инструкций | instruction file | Locked by the Lecture 3 EN deck. |
| вложенные файлы (инструкций) | nested (instruction) files | Case 1.3. |
| обзор репозитория / repository overview | repository overview | Source itself uses the EN term; keep it. |
| presence paradox | presence paradox | Already EN in the RU source; never translate or re-gloss. |
| недискаверабельные конвенции | non-discoverable conventions | |
| правило трёх адресов | the rule of three addresses | Case 1.3 target answer. |
| адрес (знания) | address | *knowledge has an address* — keep the metaphor. |
| журнал решений | decision log | The `DECISIONS.md` artifact. |
| структурированная вики | structured wiki | Case 2.2's actual slide wording (s38/s43); «структурированная вики-память» → *structured wiki memory*. The `deck.yaml` changelog's shorter «структура вики» → *wiki structure* is the same thing named at deck level. |
| авто-память | auto-memory | The runtime's own agent-written, machine-local layer (s32-s35, s55). Hyphenated, distinct from *memory* as a harness slot. |
| отравление памяти | memory poisoning | What s36 actually says (the SpAIware class). Distinct from `отравление контекста` → *context poisoning*, which the seminar does not use — do not substitute one for the other. |
| запись (в журнале / ADR) | record | One term for both a flat `DECISIONS.md` item and an ADR file, so the log's items and ADR's own "Record" read as the same object. Not "entry". |
| универсальная гигиена | universal hygiene | The axis label paired with *specific to the project*. |
| тезис (столбец таблицы источников) | Claim | Evidence-table header, next to *Source* / *Strength of evidence*. "Thesis" reads academic — keep *thesis* only for «тезис лекции» (a lecture's thesis). |
| гейт-фраза | the gate line | The `CLAUDE.md` line that states the readiness gate. |
| занятие | session | The seminar itself, kept distinct from «сессия агента» → *the agent's session*. |
| заявка | submission / request | The `signup-landing` domain object. |
| корзина (co-building) | basket | Matches the `cobuilding_baskets_*` pattern names. |
| плашка | plate | Matches `criterion_plate`. |
| строка-состояние | state line | |
| мостик | bridge | |
| свод-указатель | corpus pointer | See `свод`. |
| отдельные файлы (ADR) | separate files (ADRs) | Case 2.2 target answer; ADR stays an acronym per Part A. |
| оперативная память | working memory | Case 2.3 (a file per task). Not "RAM", not "operational memory". |
| практика файла-на-задачу | the file-per-task practice | |
| отравление контекста | context poisoning | |
| развилка | decision point | **Never "fork"** — in a seminar spent inside a git repository, *fork* reads as a repo fork. «Шесть развилок» → *six decision points*. |
| кейс | case | |
| сквозной кейс | running case | The `signup-landing` case carried through the whole session. |
| постановка (задачи) | setup | As in «постановка кейса» → *the case setup*. |
| задача заказчика | the client's request | |
| карточка-вариант | option card | |
| целевой ответ | target answer | The answer the case is steering toward. |
| разбор | breakdown | «Разбор карточек» → *the breakdown of the cards*. Never "analysis". |
| исследование (слайд) | the evidence | Slide type `research_evidence`: it presents published studies. «Что говорят четыре источника» → *what four sources say*. |
| честный пробел | an honest gap | Where the seminar admits no study measured this. |
| сила доказательства | strength of evidence | Evidence-table column header. |
| критерий и граница | criterion and boundary | |
| «здесь ещё рано» | "too early here" | `criterion_plate` title; keep it terse — it sits in a 10.5pt plate. |
| «пока ничего» | "nothing yet" | The recurring target answer. Keep the quotes. |
| завести (файл, практику) | to set up | «Завести CLAUDE.md» → *set up `CLAUDE.md`*. Not "to found"/"to introduce". |
| отложить | to defer | |
| зал | the room | «Карточки зала» → *the room's cards*; «при молчании зала» → *if the room stays silent*. Not "audience hall". |
| голосование | the vote | |
| цикл «создай — прожарь — улучши» | the create - roast - improve loop | *roast* is the course's own term for adversarial self-critique (see the Roast-Before-Implement rule); keep it. |
| журнал хода работы | progress log | |
| дивайдер (макро / микро) | divider (macro / micro) | Production term; appears in `deck.yaml`/frontmatter, not on slides. |
| раздел | section | |
| цена структуры | the cost of structure | Case 2.2. |
| свод (знания) | corpus | Case 1.3/2.2's second metaphor, next to *address*. Deliberately **not** "knowledge base" — that imports Confluence/product baggage the RU does not carry — and not "compendium" (too literary). `указатель-свод` → *a corpus pointer*. |
| отказ (инструмента реализовать) | refusal | s25: four tools declining to implement recursive discovery. Distinct from `режим отказа` → *failure mode* (Part A), which is the other sense the source uses. |
| п.п. (процентных пунктов) | pp (percentage points) | Abbreviated in tables as the RU abbreviates, spelled out in prose as the RU spells out. |
| цена отсутствия | the cost of not having it | |
