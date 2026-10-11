---
name: glossary-ru-en
issue: 172, 204, 211
status: locked
terms_count: 429---

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

## Part D — Seminar 5 terms (hooks and skills: when a request is not enough)

Added for the Seminar 5 EN track (issue #211), same pattern as Part C. Parts A/B/C still win
where they overlap — in particular `развилка` → *decision point*, `разбор` → *breakdown*,
`кейс` → *case*, `целевой ответ` → *target answer*, `карточка-вариант` → *option card*,
`честный пробел` → *an honest gap*, `зал` → *the room*, `занятие` → *session*,
`файл инструкций` → *instruction file* are already locked there and are **not** re-decided here.

**Vendor terms are not free translation.** `hook`, `matcher`, `hook event`, `hook input`,
`exit code`, `frontmatter`, `progressive disclosure`, `SKILL.md`, `name`, `description` are the
provider's own English names for these objects. Verified 2026-10-03 against
`code.claude.com/docs/en/hooks` ("The `matcher` field filters when hooks fire"; *hook event*;
*hook input* arriving as JSON on stdin; *exit code* / *JSON output*) and
`platform.claude.com/docs/en/agents-and-tools/agent-skills/overview` (YAML *frontmatter*;
*progressive disclosure*; Level 1 *Metadata* `name`+`description` ≈100 tokens, Level 2
*Instructions* = the SKILL.md body under 5k tokens, Level 3 *Resources and code* = **bundled
files**). Do not substitute a synonym that reads better — a reader who goes to the vendor docs
must find the same word.

### Three term pairs that must not be collapsed

These are the drift traps specific to this seminar. Each pair is one Russian word with two
different English answers, or two Russian words competing for one English word.

| Trap | Rule |
|---|---|
| `завязка` vs `хук` | **`завязка` is never *the hook*.** In narrative English a story's opening is "the hook", but *hook* is this seminar's central product term — using it for both would make the opening slide read as a slide about hooks. `завязка` → *the opening*. |
| `перечень` — two senses | In the **hook / settings** sense it is an **allowlist** (`перечень закрыт` → *the allowlist is closed*; `широкий / расширенный перечень` → *the broad allowlist*). In the **skill** sense it is **the listing** — the preloaded `name` + `description` lines. Never one word for both. |
| `вложения` vs `вложенность` | `вложения` (of a skill) → **bundled files** (the vendor's Level 3). `вложенность` (of instruction files) → **nesting** / *nesting depth*. Part C's `вложенные файлы` → *nested (instruction) files* governs the second. |

### Axis and frame

| RU | EN (US) | Note |
|---|---|---|
| Когда просьбы недостаточно: барьер и загрузка по требованию | When a request is not enough: a barrier and on-demand loading | Seminar 5 title. |
| просьба | a request | The axis noun: the instruction file *is a request*. Part C's `заявка` (the `signup-landing` domain object) renders as *submission* in this seminar so the two never collide. |
| усиление | reinforcement | «Пять усилений» → *five reinforcements*. What you put next to the instruction file. Not "enhancement" (product-marketing register the RU does not carry). |
| барьер | barrier | «Исполняемый барьер» → *an executable barrier* (the hook's one-line gloss). |
| загрузка по требованию | on-demand loading | The skill's one-line gloss. |
| механизм | mechanism | The generic word for all five. |
| ступень | stage | The five mechanisms as stages of the course: «три ступени из пяти» → *three of the five stages*. (The `ступень 1/2` in the builder's `ПОДГОНКА` lines is a shrink **tier** — diagnostics only, never drawn, never translated.) |
| кто приводит механизм в действие | what sets the mechanism going | The axis question. Keep it a question about an agent-of-action, not about "triggering" — Part C reserves *trigger*. |
| среда | the environment | What sets a hook going. |
| порядок работы | the way the work is ordered | What `процесс` amounts to. |
| Открытие | Opening | Section name; drawn as a roadmap pill. |
| Сборка (раздел) | Wrap-up | Section name, the closing section. Distinct from Part C's «Сборка кодинг-агента» → *Setting up a coding agent*, which is a seminar title, not a section. |
| Доступ наружу | Outbound access | Section name for the MCP stage. Moved to Session 6 in full, but still named on n03/n05/n65. |
| СЕМИНАР 5 | SEMINAR 5 | Cover eyebrow line. Caps as in the source. |
| завязка | the opening | See the trap table above. Never *the hook*. |
| сцена | the scene | The slide that puts the room inside a concrete situation. |
| база (такт) | the base | Left track of the `base_and_edge` slides: the plain fundamentals of a mechanism. Drawn as the pill **Base**. |
| кромка | the edge | Right track of `base_and_edge`: the non-obvious corner a strong engineer would still get wrong. Drawn as the pill **Edge**. Not "margin", not "rim" — *edge* carries the "sharp part" sense the RU intends. |
| такт Б | beat B | Production term (`base_and_edge` pattern). Appears in briefs and docstrings, never on a slide. |
| предел применимости | the limit of applicability | The end-of-case slide stating where the mechanism stops working. In running prose «докуда её хватает» → *how far it gets you*. |
| свидетельства | the evidence | Slide type `evidence_table_with_gap`, consistent with Part C's `исследование (слайд)` → *the evidence*. |
| оговорка | caveat | The dashed plate. `CAVEAT_OPEN` in the builder matches «Оговорка про…» → *Caveat on…*. |
| что оказалось | what it turned out to be | Recurring slide title. |
| что появилось в репозитории | what appeared in the repository | n66 title. |
| что стало проверяемым | what became checkable | n68 title. Not "verifiable" — the seminar means "you can now run a check", not formal verification. |

### Hooks (vendor terminology)

| RU | EN (US) | Note |
|---|---|---|
| хук | hook | Vendor term. Lowercase in body text, as the vendor docs do. |
| матчер | matcher | Vendor term — the `matcher` field. **Not** "pattern", "filter" or "selector". |
| событие (хука) | hook event | Vendor term. The named trigger point (`PreToolUse`, `Stop`, …). Event names are identifiers: never translate, never re-case. |
| условие | condition | The third of the three decisions a hook is made of (matcher, event, logic). |
| логика (хука) | logic | «Матчер, событие, логика» → *matcher, event, logic*. |
| вход хука | hook input | Vendor term. The JSON the hook receives on stdin. Field names (`tool_input`, `cwd`, `permission_mode`) are identifiers — verbatim. |
| код возврата | exit code | Vendor term. |
| настройки | settings | «Одна строка в настройках» → *one line in the settings*. `settings.json` verbatim. |
| перечень (в настройках) | allowlist | See the trap table. |
| оболочка | the shell | «На каждом вызове оболочки» → *on every shell call*. |
| область видимости | scope | «Три области видимости» → *three scopes*. |
| таймаут | timeout | Already an English term in the RU; keep it. |
| срок (отведённый хуку) | the time budget | Where the RU means the allowance rather than the setting. |
| исполняемый | executable | Attributive: *an executable barrier*. |
| срабатывает сам | fires on its own | The hook's defining property. *Fires* is the vendor's own verb ("filters when hooks fire"). |
| обход | bypass | «Пять форм обхода» → *five forms of bypass*. |
| слой провала | failure layer | «Два слоя провала» → *two failure layers*. Part A's `провал` → *failure* governs the noun. |
| причина молчания | reason for silence | «Шесть причин молчания» → *six reasons for silence* (a hook that fired and said nothing). |

### Skills (vendor terminology)

| RU | EN (US) | Note |
|---|---|---|
| скилл | skill | Vendor term. Lowercase for the object; capitalize only when naming the product **Agent Skills**. |
| SKILL.md | SKILL.md | Verbatim, always. |
| фронтматтер | frontmatter | Vendor term — YAML frontmatter. One word, no hyphen. |
| имя (поле) | `name` | A field. Keep the backticks the RU keeps. |
| описание (поле) | `description` | A field. «Описание ~100 токенов» → *the `description`, ≈100 tokens*. |
| тело (скилла) | the body | The SKILL.md body — the vendor's Level 2 *Instructions*. |
| вложения | bundled files | Vendor Level 3. See the trap table. |
| перечень (скиллов) | the listing | The preloaded `name` + `description` lines. See the trap table. |
| три уровня загрузки | three loading levels | The vendor's own framing; the mechanism itself is **progressive disclosure** — use that name where the RU names the mechanism rather than counting the levels. |
| загружается по требованию | loads on demand | |
| вызов (скилла) | invocation | «Два способа вызова» → *two ways of invoking it*. |
| ручной вызов | manual invocation | |
| отбор | selection | «Скиллы, которые кто-то прочитал и отобрал» → *skills someone read and selected*. |
| чужой каталог | a third-party catalog | |
| свой или готовый | your own or off-the-shelf | Slide axis. |
| годный (фронтматтер, текст) | sound | «Фронтматтер годный» → *the frontmatter is sound* — it parses and is non-empty, which is not the same as useful. Not "valid" (that claims schema conformance) and not "good". |

### The other three mechanisms

| RU | EN (US) | Note |
|---|---|---|
| субагент | subagent | One word, lowercase. |
| процесс | process | As a mechanism, not as an OS process. Where the seminar means the latter it says so explicitly. |
| MCP | MCP (Model Context Protocol) | Part A keeps the acronym; expand on first use, as the RU does on n03. |
| урезанные права | reduced permissions | The subagent's defining property. |
| переносится ли | does it transfer | Third column of n03. «Переносимость» → *transferability*. |
| приём | the practice | «Приём — у всех; запись — у каждого своя» → *the practice is universal; the way it is written down is not*. Deliberately **not** "technique" (too crafty) and never *pattern*. Distinct from the production sense below. |
| приём (вёрстки) | layout device | Production term (`visual.pattern`); never on a slide. Kept separate from `приём` above on purpose — they are different words in English. |
| запись (механизма) | the way it is written down | The per-vendor config format. Part C's `запись (в журнале / ADR)` → *record* is a different sense and keeps its own entry. |
| открытый формат / протокол | open format / open protocol | |

### Demo repository and co-building

| RU | EN (US) | Note |
|---|---|---|
| signup-landing-demo | signup-landing-demo | Never translate. Same rule as Part C's `signup-landing`. |
| демо-репозиторий | the demo repository | |
| наряд | work order | The `WORK-ORDER-demo-repo.md` artifact. |
| совместное формирование артефакта | co-building the artifact | Matches the `cobuilding_*` pattern names and Part C's `корзина (co-building)` → *basket*. |
| собранный фронтматтер | the assembled frontmatter | `cobuilding_description_assembly`. |
| что разложено | what has been laid out | n62/n65 figure. |
| три корзины | three baskets | |

## Part E — Seminar 6 terms (access to the outside / trimmed permissions)

Added for the Seminar 6 EN track (issue #225), following the Part C/D pattern. Seminar 6 is
where the course's own runtime vocabulary becomes load-bearing: `субагент` (862×), `сессия`
(808×), `сервер` (785×), `ключ` (719×), `контекст` (508×) across slides and chapter. Parts
A-C still win where they overlap (`экипировка` → *harness*, `провал` → *failure*, `развилка`
→ *decision point* and **never** *fork* — this seminar is spent inside a git repository,
`файл инструкций` → *instruction file*). Lecture 3's EN deck is the upstream anchor for the
harness vocabulary (*subagent*, *harness*, *access to the outside*, *trust boundary*), and
Seminar 4's EN deck for the case machinery.

**Second pass, after the deck was actually translated (49 rows added).** E.2 below was written
*before* the 64 slides were rendered into English; the two translation halves then reported back
what it did not cover. Three kinds of gap came back, and all three are closed here:

1. **Seven load-bearing terms** that the lock simply did not have, each recurring 5-225× and each
   carrying a case: `кусок`, `раскладка` / `разложить`, `справочник`, `обвязка`,
   `прогон перед выкладкой`, `промежуток`, `проверка, которая гоняется сама`. These are the rows a
   one-off variant would have been most visible in.
2. **The production and layout vocabulary**, which was missing *in full* — see E.3 and the reason
   it matters stated there.
3. **Two rows where the two halves of one deck actually diverged and had to be reconciled by
   hand** — `предотвращаем / решаем` and `ограничение`. They are marked in E.2 and are the proof
   that an unlocked row does not stay consistent by luck: both halves carry the same axis table,
   the recap depends on the two copies being identical, and they came back different.

Plus one **exception** (E.4): the single legitimate *fork* in the seminar, stated as an exception
so that a translator neither breaks Part C's ban nor translates a product's mode name away.


### E.0 — one row Part D (Seminar 5) and this part decide differently

Seminar 5's EN track locked `занятие` → *session* and built its deck on it. Seminar 6 defines
**`сессия`** as a term of its own — a separate run of an agent that a human can talk to by hand,
set against a subagent — so bare *session* has to mean the agent-run, and the class is
*the seminar* / *today's class*. The rule is: the load-bearing term takes the bare word, the
framing word gets the explicit one.

**This is a real contradiction, not a numbering one, and it is recorded rather than resolved
here.** From Seminar 6 on, the rows below apply. Seminar 5's own EN deck already shipped with
the earlier reading; whether to re-render it is an owner decision, filed as issue #230 together
with the course's other cross-seminar term drifts. A lock that quietly held two readings of one
word would be worse than one that says which seminar changed it and when.

### E.1 — `session`: the collision, resolved course-wide

**The problem.** Part C renders `занятие` (the class itself) as *session*, with a warning not
to confuse it with `сессия агента`. After the Seminar 6 terminology pass, Russian `сессия` is
itself a **defined term of the seminar** — one run of the agent that a person can talk to by
hand — introduced on a definition slide and set directly against `субагент`. Two different
things would now both be *session* in English.

**The decision.** The taught concept takes the bare term; the frame word takes an explicit
one.

- **`сессия` → *session***, bare, no qualifier. On its **first use in a seminar**, gloss it
  once — *an agent session: one run of the agent that you talk to by hand* — then bare
  everywhere after.
- **`занятие` → *the seminar*** (the event: «вопрос занятия» → *the seminar's question*) or
  ***today's class*** / ***the class*** in direct address («чем занятие кончается» → *how the
  class ends*). **Never bare *session*** for this sense, from Seminar 5 onward.

**Why this way round, and why it generalizes.** (1) `сессия` is the one of the two that the
course *defines and draws* — it sits in a box on a three-box diagram opposite `субагент`, and
the whole third case turns on two of them in one folder; `занятие` is never defined, it is
only the frame. (2) The technical sense has an external referent the reader already carries:
the product's own UI and docs say *session*, and an engineer reading an
agent-configuration seminar will read *session* that way whatever a glossary says. (3) The
frame sense has good English substitutes (*seminar*, *class*); the agent sense does not
(*run*, *conversation* both lose the product term). (4) The rule is decidable without
judgement and holds for every seminar from 4 onward, all of which live inside a coding-agent
harness.

**Three live readings from Seminar 6.**

| RU (source) | EN | What the rule prevents |
|---|---|---|
| «если **в сессии** подключены трекер задач и сервер документации из прошлого **раздела занятия**, субагент получает их описания бесплатно» | "if the issue tracker and the documentation server from the previous **section of the seminar** are connected **in the session**, the subagent gets their definitions for free" | Both senses in one sentence. Under Part C's rule this reads "from the previous section of the session … connected in the session" — two referents, one word, four words apart. |
| «**сессия** обрастает серверами по ходу работы… Механика хуков и скиллов здесь своя, и **занятие** её не разбирает» | "a **session** accumulates servers as the work goes on… The mechanics of hooks and skills are their own thing here, and the **seminar** does not break them down" | The subject changes between the two sentences — from the agent's run to the class. With one word for both, the paragraph reads as if the run stopped covering something. |
| «вытеснило то, ради чего **сессию** открывали… На этой противоположности стоит порядок всего **занятия**» | "it crowded out the very thing the **session** was opened for… The order of the whole **class** rests on that opposition" | *The session was opened for* and *the order of the whole session* in adjacent clauses would make the seminar sound like something you open and crowd out. |

**Consequence to carry.** Seminars 1-4 EN already use bare *session* for both senses (sem-04:
"the first open question of the session" = the class; "a new agent session from scratch" = the
run). Harmonizing those is a separate one-pass sweep, not part of this lock.

### E.2 — Terms

| RU | EN (US) | Note |
|---|---|---|
| занятие | the seminar / today's class | **Supersedes the Part C row** `занятие → session`. See E.1. Never bare *session* for this sense. |
| сессия | session | The seminar's own defined term: one run of the agent you talk to by hand. Gloss once on first use (E.1), bare thereafter. |
| вызвавшая сессия | the calling session | **Not *the parent session***. The RU deliberately dropped «родитель» in revision 5; the only place *parent session* may appear is inside the verbatim harness-documentation quote, which stays verbatim. |
| вторая сессия | a second session | The thing set against *a subagent*: same clean context, but the answer stays there and you carry it back by hand. |
| дочерняя сессия | child session | A full session an orchestrator starts; you can walk into it by hand. |
| сессия-оркестратор / оркестратор | orchestrator session / the orchestrator | |
| субагент | subagent | One word, never *sub-agent*. **Never *role***: the RU term was «роль» until the post-delivery pass and the English must not resurrect it. Animate in RU; in EN prefer *who* over *which* for it, matching the source. |
| ступень | rung | The course's own ladder metaphor, already *rungs* in the Seminar 4 EN deck. |
| блок (занятия) / раздел | section | The RU source uses **both words for the same object** («предыдущий блок занятия» and «прошлого раздела занятия»); English keeps one term, matching Part C's `раздел → section`. |
| промах | a miss | «Два промаха, причины противоположные» → *Two misses, opposite causes*. Not *mistake*, not *failure* — `провал` is *failure* (Part A). |
| край контекста | the edge of the context | «работа вышла за край его контекста» → *the work ran past the edge of its context*. |
| доступ наружу | access to the outside | Seminar 4 EN anchor; one half of the Seminar 6 title. |
| урезанные права | trimmed permissions | The other half of the title. **Not *least privilege*** (a principle name the seminar never invokes), **not *restricted/limited*** (reads as imposed from outside). The trimming is voluntary and done by the person setting the subagent up, in the `tools:` line — keep the active voice: *you trim the list yourself*, not *permissions are restricted*. |
| урезать (права) | to trim (permissions) down | |
| контекст | context | Bare. **Not *context window* in prose**: the word «окно» was removed from this seminar deliberately. *Context window* survives only inside the verbatim harness-documentation quote. |
| состав контекста | the composition of the context | **Never *size*, *usage*, *budget* or *window***. The first case turns on *what* is loaded and where it came from (four sources), which is a different question from how much room is left. |
| что лежит в контексте | what is sitting in the context | The prose form the slides actually use; prefer it over the abstract noun. |
| размер контекста | the size of the context | The other question. Keep the two visibly apart. |
| постоянная плата | the standing cost | Paid for a server being connected at all, whether or not the agent ever calls it. Not *overhead*. |
| цена вызова | the cost of a call | Paired with *the standing cost*; the seminar's numbers only read correctly if the pair stays a pair. |
| сервер / MCP-сервер | server / MCP server | |
| подключение (сервера) | the connection | «подключить сервер» → *to connect a server*. |
| «подключено» (зелёная отметка) | the green "connected" marker | Keep the quotes, as the RU does. It is a fact about the process, not about whether the agent went there. |
| доказательный вызов | the proof call | The named move: name the server in the request, then look for a call in the output signed with the server's name. |
| подписан именем сервера | signed with the server's name | The one checkable sign. |
| имя инструмента | tool name | Loaded at session start. |
| описание инструмента | tool definition | Matches the harness documentation's own *tool definition*. |
| полная схема инструмента | the tool's full schema | Pulled in on demand. **These three are distinct and must not merge** — the whole first case's number depends on names-at-start vs schema-on-demand. |
| отложенная загрузка | deferred loading | Not *lazy loading*: the RU uses the plain form, not the jargon, and the register is part of the point. |
| по требованию | on demand | |
| отсрочка | the deferral | «отсрочку отменяют две вещи» → *two things cancel the deferral*. |
| область видимости (конфигурации) | scope | The three scope names stay verbatim in code font: `local`, `project`, `user`. Never translate them. |
| набор инструментов | toolset | As in `--toolsets repos,issues`. |
| операция | operation | The list drawn up first, from which permissions are then derived. |
| права / список прав | permissions / the permissions list | The `tools:` field of a subagent file. |
| ключ | key | |
| широкий (персональный) токен | a broad (personal access) token | |
| узкий ключ | a narrow key | |
| хранилище секретов | a secrets store | A key's home between runs. Not *secrets manager* (a product category the RU does not name). |
| утечка / канал утечки | a leak / a leak channel | |
| галочки (проставить все) | checkboxes (to tick every box) | Deliberately colloquial — «галочки прощёлкивают» → *the boxes get clicked straight through*. Do not raise it to *over-provisioning*. |
| сторож поставщика | the provider's watchdog | **Never *secret scanning*** or any vendor product name: the slide carries this explicitly as a past cohort's story, not as a verified property of a named service, and its own `[FACT-CHECK]` marker says so. Naming the product would upgrade the claim in translation. |
| смертельное трио | lethal trifecta | Willison's coinage, already *lethal trifecta* in the Lecture 4 EN deck. The three parts: *access to private data* + *exposure to untrusted content* + *a channel to the outside*. |
| канал наружу | a channel to the outside | Use *exfiltration channel* only where the source itself says «эксфильтрация». |
| эксфильтрация | exfiltration | |
| чужая инструкция | someone else's instruction | The seminar's plain-words title for the mechanism. The mechanism's name is *prompt injection* (Part A) — keep both, do not substitute one for the other. |
| стоп-критерий | a stop criterion | |
| трекер задач | the issue tracker | Not *task tracker*; the objects are issues. |
| снимок | a snapshot | Both senses the seminar uses: a hand-copied snapshot of a tracker item, and the repository state a subagent gets at its own start. |
| фон, не очередь | background, not a queue | |
| предел (на одновременность) | the cap (on concurrency) | Twenty subagents **running at once**, not twenty per session. The *at once* is the whole point and must survive. |
| изоляция / изолированный субагент | isolation / an isolated subagent | |
| команда агентов / напарник | agent team / teammate | From the verbatim documentation line: "Agent teams don't isolate teammates in worktrees". |
| рабочая копия | working copy | The taught term. On first use, gloss it as the source does — *a separate working copy; in git this is a `worktree`* — then stay with *working copy* in prose. **Not *clone*** (the history is shared), **not *checkout***. See the report note on the mixed-script RU spelling. |
| основная копия | the main working copy | |
| ветка / ветвь | branch | The RU uses both; English keeps one. |
| базовая инструкция проекта | the project's root instruction file | Short form *the root file*, matching the Seminar 4 EN deck. |
| столкновение | a collision | Two sessions or two subagents writing over each other in one folder. |
| признаки успеха сошлись | every sign of success lined up | The failure case's headline line; keep it as one phrase, it recurs. |
| зона / раскладка зон | zone / the zone layout | «развести зоны» → *to divide the zones up*. The defense that works where a separate copy does not exist. |
| цена в железе | the cost in hardware | RAM per session, measured on the author's own machine. |
| ход (Ход 1 / Ход 2) | move (Move 1 / Move 2) | Numbered moves of a co-building sequence, and the rows of the five-move comparison table. |
| приём | technique | Distinct from `ход`: a technique is reusable and off-the-shelf, a move is a step in one sequence. Both words are live in this seminar. |
| нивелировать | to mitigate | Not *to eliminate*: each of the five techniques names what it does **not** close. |
| сцена | the scene | The observed-problem opener of each case. |
| свидетельства | the evidence | Same slide type Part C locks as *the evidence*; Seminar 6 renamed the RU label from «исследование», the EN term does not change. |
| со-сборка | co-building | The Part C `корзина → basket` family. |
| граница (в обе стороны) | a boundary (stated both ways) | Each piece records what is inside it and what stays outside; the point is that both sides state it. |
| кусок (задачи) | piece | The unit a task is taken apart into (225× in the Seminar 6 EN deck — the whole second subagent case). Not *chunk* (a technical flavor the RU does not have), not *part* (collides with a part of a chapter). «Независимых кусков три» → *three of the pieces are independent*. |
| раскладка (задачи) / разложить | the layout / to lay out | Taken under the existing `раскладка зон` → *the zone layout*, so one English word covers both uses. **Not *decomposition***: Part C already spends *breakdown* on `разбор`, and a third near-synonym would read as a third concept. The one place *decompose* is allowed is the verbatim owner quote that itself uses the loanword. |
| справочник (на настраиваемой платформе) | lookup list | The object of the second subagent case (28×). Not *catalog* (pulls ERP-localization baggage), not *directory* (collides with a filesystem directory, which is *directory* in the same half). |
| обвязка | scaffolding | The wiring a subagent needs around it. *harness* is taken (`экипировка`), and *wiring*/*plumbing* read as hardware infrastructure. |
| прогон перед выкладкой | the pre-release run | One of the pieces the practice slide lays the task out into. |
| промежуток (между зонами) | the gap | The place nothing covers. The collision with `честный пробел` → *an honest gap* is harmless — both mean an uncovered place, and the two slides sit far apart. |
| проверка, которая гоняется сама | a check that runs itself | Deliberately plain words, as in the RU. **Never *CI***: the seminar does not name the tool, and naming it in translation would name an instrument the source refuses to name. |
| сжатие (разговора) / сжимать / уплотняться | compaction / to compact / to get condensed | The product's own word for the runtime shortening a long conversation, and the observed symptom the second MCP case is built on. Never *to shrink* / *to squeeze* — the reader has to recognize the term from the product's own UI. |
| статья (расхода) | line item | The MCP block's whole bill stands on «три статьи». Not *item* / *entry* / *category*, which drift from slide to slide. |
| заказчик | the client | Bare, next to Part C's `задача заказчика` → *the client's request*. |
| задача (в трекере) | issue | One Russian word, two English ones. The RU source itself writes `читать открытые issue` in code font, which settles it. |
| задача (дня, занятия) | task | The work in front of you — the thing that gets laid out into pieces. |
| предотвращаем / решаем | prevent / settle | Column header of the axis table, shown twice (first statement and recap) and required to match character for character, because the return of the axis in the closing block rests on the two tables being identical. **Locked to *settle*, not *fix***: the two halves of the Seminar 6 deck translated it independently and disagreed, and the disagreement had to be undone by hand. «Решаем — правило уже нарушено» → *Settle — the rule has already been broken*. |
| ограничение (шапка «что не делает») | the limit | Same story, same column pair, locked the same way: *the limit*, not *the limitation*, in all eight axis and comparison tables of a seminar. |
| описание-триггер (скилла) | the trigger description | From the Seminar 5 vocabulary. Part C's ban on *trigger* covers `сигнал` → *signal*; here the Russian itself says «триггер», so the ban does not reach this row. |
| перенос руками | the transfer by hand | The name of the defect the first MCP case is built around. |
| живой источник / живость источника | a live source / the liveness of the source | Defined on the slide: a source is live if its answer depends on the time of the request. |
| автовыбор / маршрутизация | auto-selection / routing | The second of the two ways to call a subagent. |
| поставщик | provider | Models provider, harness provider, and `сторож поставщика` → *the provider's watchdog*. |
| производитель | vendor | The other Russian word, held apart from *provider*: whoever publishes the documentation being quoted. The RU deck removed the loanword «вендор» from the visible layer on purpose — *vendor* in English renders «производитель», never that removed word. |
| эндпойнт | endpoint | |
| пересказ | a retelling | What a second session hands back instead of the thing itself; the named defect of that move. |
| неполадка | fault | |
| тариф / тарифы | plan / pricing plans | The scene of the second miss. Mind the collision with *plan* in the production sense (a lecture plan): inside seminar text *plan* is the subscription tier. |
| участник / лимит участников | member / the limit on members | **Not *the member limit*** — the two halves settled on *the limit on members*. |
| одностраничник | one-pager | The screen a block returns to three or four times. |
| разбор проведения | the delivery breakdown | Follows Part C's `разбор` → *breakdown*. Not *review*. |
| отраслевой разворот | the industry's reversal | |
| целевой (о собранном файле) | a target state | «сам собранный файл при этом целевой» → *the assembled file itself is a target state, with no commit behind it*. |
| вытеснить (работу чтением) | to crowd (the work) out | «по сигналу вытеснения работы чтением» → *on a signal that reading has crowded the work out*. |
| Мостик / MCP / Субагент / Сборка (блоки занятия) | Bridge / MCP / Subagent / Wrap-up | The four block names of Seminar 6. Two of them (*MCP*, *Subagent*) are **rendered on the slides** — they are the roadmap pills on every macro divider — so a renderer that leaves them in Russian ships a Cyrillic visible layer. `Сборка` is the closing block (the axis recap, what appeared in the repository, the question asked a second time, how the class ends): *Wrap-up*, **not** *assembly* / *build* (which would read as building the deck), and `со-сборка` stays *co-building*. |
| хук | hook | Course term from Seminar 5, which the lock carried only inside a sentence («The mechanics of hooks and skills…», E.1) and never as a row. It is **drawn on the Seminar 6 cover** — one of the four axis segments — so an unlocked variant ships on the first screen of the class. |
| скилл | skill | Same source, same reason. The axis pairs them: *hook* and *skill* closed last time, *MCP* and *subagent* settled today. |
| форма (экран ввода на платформе) | form | The object of the second subagent case, paired with `справочник` → *lookup list*; the two zones of the boundary figure are *lookup list* and *form*. Lower case, as in the RU: these are box labels, not product names. |
| витрина отчётов | reporting mart | One of the four external systems a server can reach (n08). Not *report showcase* (literal), not *dashboard* (a different object — the seminar names a data store, not a screen). |
| коннектор | connector | The product's own name for the sixth rung of scope precedence. Kept as is; the RU is itself the loanword. |
| сервер из плагина | server from a plugin | The fifth rung. Not *a plugin server*, which reads as a server for plugins rather than one a plugin brought with it. |
| только итог | only the result | What comes back from a subagent, and the chip under the subagent column of the three-tier figure. The pair below states the other side. |
| можно зайти руками | you can walk in by hand | What a child session allows and a subagent does not — already the prose form in the `дочерняя сессия` row above; locked here as its own row because it is **drawn on a figure** as a chip and had been re-invented each time. |

### E.3 — Production and layout vocabulary

This is the largest single gap the Seminar 6 EN pass found, and the one with the worst
consequences, because it is invisible: these words almost never reach the screen. They live in
`visual.primary` and `visual.backup` of nearly every slide, which both translation halves had to
render in full (that text is prose, not metadata, so the mirror rule covers it), and until now
every translator re-invented them. Two halves of one deck describing the same layout in two
vocabularies is not a reading problem for a student — it is a reading problem for the next round
of edits, which is where this costs money.

Parts C already fixed two of these (`плашка` → *plate*, `дивайдер` → *divider*, `слот` → *slot*,
`мостик` → *the bridge*); the rest are locked here. Every row below is a **record of what the two
halves actually used**, verified against `slides-en/`, not a proposal.

| RU | EN (US) | Note |
|---|---|---|
| подпись-итог | the closing line | The one line that closes a screen. |
| формула-итог | the closing formula | The gold bar. Distinct from the closing line: a formula is quotable on its own. |
| тихая реплика | a quiet aside | The teal bar — a speaker's line, not a conclusion. The pair *closing formula* / *quiet aside* is the one the builder decides by punctuation; see the note in `rendered/build_sem06.py`. |
| дорожка кейсов | the case track | |
| полотно | the canvas | The drawable area of a slide. |
| ярус | tier | A horizontal level inside a figure. |
| полоса (схемы) | band | |
| коробка-таблица | a table-box | |
| кружок-номер | a number circle | |
| рисовалка | the figure script | The `make_figures_*.py` family. Not *drawing tool*. |
| сторож (проверки сборки) | the guard | A build-time check that prints a warning, e.g. *the "DIAGRAM SQUEEZED" guard was firing on the longer wording*. Held apart from `сторож поставщика` → *the provider's watchdog*, which is a thing in the world, not in the build. |
| круг правок | a round of edits | |
| сведение | the consolidation pass | **Not *consolidation session***: `сессия` is a defined term of this seminar (E.1), and *session* in this position collides with it. |
| разборщик | the parser | `slide_parts.py`. |
| сборщик | the builder | `build_semNN.py`. |
| кегль | the point size | |
| золотая коробка | the gold box | |
| подпись на схеме | a figure label | Text **drawn in pixels** by a `make_figures_*.py` script, not laid out by the builder. Two consequences the translator has to carry: a label has **no word wrap** (it does not re-flow, it overruns), and it keeps the **case of the source** — an ALL-CAPS Russian header stays ALL-CAPS. Labels on boxes drop the article (`разговор` → *conversation*, not *the conversation*); labels that are sentences keep it. |
| словарь схем | the figure strings file | `rendered/fig_strings_en.py` — the RU→EN table the figure scripts translate through, one entry per drawn label. It is a **record** of the lock, never a second place to decide terminology: a term that is not in this glossary is added here only after it is added above. |

### E.4 — The one legitimate *fork*

Part C locks `развилка` → *decision point* and bans *fork* outright: a seminar spent inside a git
repository reads *fork* as a repo fork. **That ban stands** — in the Seminar 6 EN deck `развилка`
is *decision point* everywhere, including the half that works with real branches.

There is exactly one place where the ban must not be applied, and it is worth stating as an
exception rather than letting a translator either violate the lock or lose a product's name:

| RU | EN (US) | Note |
|---|---|---|
| форк (режим субагента, наследующий всё) | fork | **The only exception to Part C's `never fork`.** This is not a translation of «развилка» — it is the name of a documented subagent mode (the one that inherits everything from the calling session) as the harness's own documentation spells it, and the slide quotes that documentation. One occurrence, on the subagent one-pager. The consequence for checking: `grep -ci 'fork'` over a Seminar 6 EN deck must come back **1** — a 0 means a product's name was translated away, a 3 means `развилка` leaked. |
