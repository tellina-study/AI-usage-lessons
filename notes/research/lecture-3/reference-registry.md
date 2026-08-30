# Lecture 3 — Reference registry (canonical URL map + per-slide claim inventory)

**Date:** 2026-08-30 · **Researcher:** research subagent (direct, no sub-agents) · **Lecture:** «Архитектуры AI-систем: агенты, RAG, API» (МГТУ ИУ6, 3 курс, RU, 2026).
**Purpose:** реестр ссылок перед добавлением URL-сносок на слайды lec-03. Формат зеркалит lec-04 `_helpers.py` (`URLS` + `SLIDE_REFS`).
**Grounding:** `notes/research/lecture-3/sources.md` (verified 2026-05-16) + chapter § Источники (chapter-part5.md) + WebSearch/WebFetch re-verify 2026-08-30.
**Access date all URLs:** 2026-08-30. `[VFY]` = re-verify day-of (volatile OR could not confirm canonical URL this session). ✅ = re-verified this session or clean in sources.md.

---

## Summary (read first)

- **Слайдов, требующих ссылок: 26 из 40.** Остальные 14 — навигация/структура (cover s02, lecture-map s02a, section dividers s04a/s09/s13a/s18/s25a, recap s03, чек-листы s08a, стартовый комплект s27b, мост s30, Q&A s31, лестница s04/s26 без внешних claim) — концептуальные своды без внешнего первоисточника; ссылки не нужны.
- **Ключевые сквозные источники + canonical URL:**
  - Air Canada (Moffatt v. Air Canada, BC CRT 2024-02) → McCarthy Tétrault + ABA — s01, s12, s13, s27. ✅
  - Anthropic *Building Effective Agents* (workflow vs agent, «найди простейшее») → s22, s05, s26. ✅
  - Anthropic *Reasoning Models Don't Always Say What They Think* (CoT faithfulness, 25%/39%) → s06, s21, s29. ✅
  - Zheng et al. 2024 EMNLP, arXiv:2311.10054 (персоны ≠ точность) → s05a. ✅
  - Chroma *Context Rot* + Liu *Lost in the Middle* (2307.03172) → s08. ✅
  - Barnett et al. arXiv:2401.05856 (7 точек отказа RAG) → s13. ✅
  - HF PEFT *Beyond LoRA* (LoRA 98.4% из 20 834 карточек) → s15. ✅
  - Luo et al. arXiv:2308.08747 (catastrophic forgetting) → s16. ✅
  - Willison / Docker / Unit 42 (prompt injection, GitHub MCP heist) + Bloomberg/NatLawReview (NYT v. OpenAI logs) → s25. ✅
  - MIT NANDA *State of AI in Business 2025* (~95% пилотов без ROI) → s29. ✅ (Fortune coverage)
- **Нужен ли рефактор нот:** **НЕТ структурного рефактора.** speaker_notes уже связные нарративы 150-300+ слов, derived from chapter, без layout-описаний и без scaffold-фраз. **НО** ни одна нота не содержит inline-URL (`grep http slides/*.md` = 0). Для добавления ссылок → добавлять `URLS`+`SLIDE_REFS` реестр в `rendered/_helpers.py` (как lec-04) и рендерить сноски на visible-слой / notes-хвост, НЕ править нарратив нот. Volatile-числа (s22d, s25b, s25, s29) требуют `[VFY]`-пометки на день лекции.

---

## URLS (canonical, verified)

```python
URLS = {
    # --- Air Canada / legal (s01, s12, s13, s27) ---
    "aircanada_mccarthy": "https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot",
    "aircanada_aba": "https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/",
    # --- Anthropic engineering / research ---
    "anthropic_agents": "https://www.anthropic.com/research/building-effective-agents",
    "anthropic_context_eng": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
    "anthropic_multiagent": "https://www.anthropic.com/engineering/multi-agent-research-system",
    "anthropic_cot_faith": "https://www.anthropic.com/research/reasoning-models-dont-say-think",
    "anthropic_cot_paper": "https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf",
    "anthropic_retention": "https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention",  # [VFY quarterly]
    "anthropic_mcp_donate": "https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation",
    # --- Prompt / roles / CoT ---
    "zheng_personas": "https://arxiv.org/abs/2311.10054",  # EMNLP Findings 2024
    "wei_cot": "https://arxiv.org/abs/2201.11903",
    "kojima_zeroshot_cot": "https://arxiv.org/abs/2205.11916",
    "wang_selfconsistency": "https://arxiv.org/abs/2203.11171",
    # --- Context ---
    "chroma_context_rot": "https://research.trychroma.com/context-rot",
    "liu_lost_middle": "https://arxiv.org/abs/2307.03172",
    # --- RAG ---
    "lewis_rag": "https://arxiv.org/abs/2005.11401",  # NeurIPS 2020
    "barnett_7fail": "https://arxiv.org/abs/2401.05856",  # CAIN 2024
    "kore_7rag": "https://www.kore.ai/blog/seven-rag-engineering-failure-points",
    "uniah": "https://arxiv.org/abs/2503.00353",  # [VFY yearly]
    "graphrag_ms": "https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/",
    "graphrag_paper": "https://arxiv.org/abs/2404.16130",
    "tds_agentic_rag": "https://towardsdatascience.com/agentic-rag-failure-modes-retrieval-thrash-tool-storms-and-context-bloat-and-how-to-spot-them-early/",  # [VFY]
    "redhat_rag_ft": "https://www.redhat.com/en/topics/ai/rag-vs-fine-tuning",
    "ibm_rag_ft": "https://www.ibm.com/think/topics/rag-vs-fine-tuning",
    "bigdata_ft": "https://bigdataboutique.com/blog/fine-tuning-llms-when-rag-isnt-enough",
    # --- Fine-tuning / PEFT / distillation ---
    "hf_beyond_lora": "https://huggingface.co/blog/peft-beyond-lora",  # LoRA 98.4% / 20834; [VFY quarterly]
    "lora_paper": "https://arxiv.org/abs/2106.09685",
    "qlora_paper": "https://arxiv.org/abs/2305.14314",
    "hinton_distill": "https://arxiv.org/abs/1503.02531",
    "peft_survey": "https://arxiv.org/abs/2403.14608",
    "luo_forgetting": "https://arxiv.org/abs/2308.08747",
    "openai_cookbook_ft": "https://cookbook.openai.com/examples/fine_tuning_direct_preference_optimization_guide",
    "openai_rft": "https://platform.openai.com/docs/guides/reinforcement-fine-tuning",
    # --- Agents / loop / equipment ---
    "yao_react": "https://arxiv.org/abs/2210.03629",  # ICLR 2023
    "react_google": "https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/",
    "cognition_no_multiagent": "https://cognition.ai/blog/dont-build-multi-agents",
    "gloaguen_presence": "https://arxiv.org/abs/2602.11988",  # presence paradox; [VFY future-dated id]
    "claude_code_51735": "https://github.com/anthropics/claude-code/issues/51735",  # verified real
    # --- Security / retention ---
    "willison_mcp_inject": "https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/",
    "docker_mcp_horror": "https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/",
    "unit42_mcp": "https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/",
    "authzed_mcp_timeline": "https://authzed.com/blog/timeline-mcp-breaches",  # [VFY running timeline]
    "nyt_openai_bloomberg": "https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms",
    "nyt_openai_natlaw": "https://natlawreview.com/article/openai-loses-privacy-gambit-20-million-chatgpt-logs-likely-headed-copyright",
    "openai_your_data": "https://developers.openai.com/api/docs/guides/your-data",  # [VFY quarterly]
    # --- Failures / postmortems / market ---
    "jain_4200": "https://medium.com/@sattyamjain96/the-agent-that-burned-4-200-in-63-hours-a-production-ai-postmortem-d38fd9586a85",  # [VFY single-author]
    "mindstudio_reliability": "https://www.mindstudio.ai/blog/reliability-compounding-problem-ai-agent-stacks",
    "mit_nanda_fortune": "https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/",
    "cio_ai_disasters": "https://www.cio.com/article/190888/5-famous-analytics-and-ai-disasters.html",
    "verge_mycity": "https://www.theverge.com/2024/3/29/24117417/nyc-google-microsoft-chatbot-myCity-incorrect-information",
    # --- Coding agents (s25b) — vendor sites, verify version day-of ---
    # (не установлены как жёсткие claim-URL; агентные бренды — allowlist, verify day-of)
    # --- COULD NOT CONFIRM canonical (treat as course-internal / illustrative) ---
    # "agent_harness_registry": "https://github.com/workain/agent-harness-registry",  # [VFY] — not confirmed via search 2026-08-30
    # "persona_tone_paper": "arXiv:2605.29420",  # [VFY] — future-dated id, not confirmable
    # "honest_lying": "arXiv:2605.29463",  # [VFY] — future-dated id, not confirmable
    # "mcp_threat_2603.22489" / "prompt_cache_2601.06007" / "forgetting_mech_2601.18699" — recent preprints, [VFY]
}
```

---

## SLIDE_REFS (claim inventory: slide → refs → раскрытие)

Формат кортежа: `(N, "источник — что показывает", "url_key", "фраза-раскрытие"[, VFY_flag])`.

```python
SLIDE_REFS = {
    # ===== Раздел 0 =====
    "s01": [  # Air Canada hook
        ("1", "McCarthy Tétrault — Moffatt v. Air Canada (BC CRT, 14.02.2024)", "aircanada_mccarthy",
         "бот выдумал политику возврата; трибунал: компания отвечает за ответ бота"),
        ("2", "ABA Business Law Today — компании отвечают за AI-чат-бота", "aircanada_aba",
         "«бот — не отдельное юр. лицо»: неправильный выбор архитектуры под задачу lookup"),
    ],
    # s02 cover, s02a lecture-map, s03 recap, s04 ladder — навигация, внешних claim нет
    # ===== Раздел 1. Промпт =====
    "s05": [  # дефолт — один вызов
        ("1", "Anthropic — Building Effective Agents («найди простейшее»)", "anthropic_agents",
         "не усложняй архитектуру без требования задачи — распределение бремени доказательства"),
    ],
    "s05a": [  # роль ≠ точность
        ("1", "Zheng et al. 2024, EMNLP Findings — персоны не улучшают точность фактов", "zheng_personas",
         "162 персоны · 8 доменов · 2410 фактических вопросов · 4 семейства → нет прироста точности"),
        # NB: chapter также цитирует arXiv:2605.29420 (роль → тон/глубина) — [VFY], id не подтверждён
    ],
    # s05b структура промпта — концептуальный (structured-output параллель), внешний claim не нужен
    "s06": [  # Chain-of-thought + faithfulness
        ("1", "Wei et al. 2022 — Chain-of-Thought Prompting", "wei_cot",
         "пошаговое рассуждение поднимает надёжность на арифметике/многошаговой логике"),
        ("2", "Anthropic — Reasoning Models Don't Always Say What They Think", "anthropic_cot_faith",
         "faithfulness: Claude 3.7 ~25%, DeepSeek R1 ~39% — рассуждение не обязано отражать реальную причину", True),
    ],
    "s08": [  # context engineering + context rot
        ("1", "Chroma Research — Context Rot", "chroma_context_rot",
         "точность извлечения падает с ростом числа токенов в контексте"),
        ("2", "Liu et al. 2023 — Lost in the Middle", "liu_lost_middle",
         "тот же феномен, что «lost in the middle» из Лекции 2 — новый термин, не новая сущность"),
        ("3", "Anthropic — Effective Context Engineering", "anthropic_context_eng",
         "минимальный высокосигнальный контекст — инженерное требование, не эстетика"),
    ],
    # s08a чек-лист — свод раздела, внешний claim не нужен
    # ===== Раздел 2. RAG =====
    "s10": [  # принцип RAG
        ("1", "Lewis et al. 2020 — Retrieval-Augmented Generation (NeurIPS)", "lewis_rag",
         "каноническая статья RAG: индексация → retrieval → генерация с опорой"),
    ],
    "s11": [  # когда RAG правильный
        ("1", "IBM — RAG vs Fine-Tuning (вендор-нейтрально)", "ibm_rag_ft",
         "признаки-за-RAG: большое/меняется/провенанс/приватное — нужна конъюнкция"),
        ("2", "U-NIAH — RAG win-rate выше у меньших моделей", "uniah",
         "выигрыш RAG над прямым ответом особенно велик для меньших моделей", True),
    ],
    "s12": [  # когда НЕ RAG
        ("1", "Red Hat — RAG vs Fine-Tuning (когда не RAG)", "redhat_rag_ft",
         "корпус влезает в окно → full-context+кэш; фиксированное значение → lookup; live через API → без индекса"),
        ("2", "McCarthy Tétrault — Air Canada как «генерация поверх фиксированной политики»", "aircanada_mccarthy",
         "фиксированная политика → детерминированный lookup, не retrieval+генерация"),
    ],
    "s13": [  # провал RAG на масштабе + Air Canada revisited
        ("1", "Barnett et al. 2024 — Seven Failure Points (RAG)", "barnett_7fail",
         "«вернул что-то ≠ вернул правильное»: 7 точек отказа RAG-инжиниринга"),
        ("2", "Kore.ai — Seven RAG Engineering Failure Points", "kore_7rag",
         "legal-AI / medical-RAG / support-бот — деградация на масштабе без observability"),
        ("3", "McCarthy Tétrault — Air Canada (отказ grounding)", "aircanada_mccarthy",
         "сгенерированный текст в роли, требовавшей извлечённого проверенного факта"),
    ],
    # ===== Раздел 3. Fine-tune =====
    "s13b": [  # что такое fine-tuning
        ("1", "IBM — RAG vs Fine-Tuning (fine-tuning меняет веса)", "ibm_rag_ft",
         "промпт/RAG меняют контекст; fine-tuning меняет сами веса модели"),
    ],
    "s14": [  # fine-tuning сузился + дистилляция
        ("1", "BigData Boutique — Fine-Tuning When RAG Isn't Enough", "bigdata_ft",
         "fine-tuning не умер, а сузился до поведения/стиля/формата/политики; знание → RAG", True),
        ("2", "Hinton, Vinyals, Dean 2015 — Distilling the Knowledge", "hinton_distill",
         "дистилляция — самостоятельная техника, таксономически НЕ вид fine-tuning"),
        ("3", "PEFT survey — таксономия методов настройки", "peft_survey",
         "обзоры разносят дистилляцию и fine-tuning по разным категориям"),
    ],
    "s15": [  # PEFT vs full FT
        ("1", "Hu et al. 2021 — LoRA", "lora_paper",
         "базовые веса замораживаются, обучаются низкоранговые адаптеры"),
        ("2", "Dettmers et al. 2023 — QLoRA", "qlora_paper",
         "LoRA поверх квантованной модели → дообучение на одном GPU"),
        ("3", "HF PEFT — Beyond LoRA (LoRA 98.4% из 20 834 карточек)", "hf_beyond_lora",
         "98.4% моделей с тегом PEFT используют LoRA; оговорка: доля среди помеченных PEFT", True),
    ],
    "s16": [  # catastrophic forgetting
        ("1", "Luo et al. 2023 — Catastrophic Forgetting in LLM Continual FT", "luo_forgetting",
         "узкий агрессивный FT ломает общие способности; тяжелее с ростом масштаба модели"),
    ],
    # ===== Раздел 4. Агенты =====
    "s19": [  # API-слой + MCP
        ("1", "Anthropic — MCP donation / Agentic AI Foundation (N×M→N+M)", "anthropic_mcp_donate",
         "MCP стандартизует подключение; удобство подключения ≠ безопасность подключаемого", True),
    ],
    "s21": [  # цикл агента
        ("1", "Yao et al. 2022 — ReAct (plan→act→check→iterate)", "yao_react",
         "чередование рассуждения и действий; каждый шаг — место отказа"),
        ("2", "Anthropic — Reasoning Models faithfulness (check ≠ самооценка)", "anthropic_cot_faith",
         "шаг check — валидация против внешнего критерия, не самооценка модели", True),
    ],
    "s22": [  # workflow vs agent
        ("1", "Anthropic — Building Effective Agents (workflow vs agent)", "anthropic_agents",
         "workflow = предопределённые пути; агент = динамический процесс; размен латентность/стоимость↔качество"),
        ("2", "Cognition — Don't Build Multi-Agents", "cognition_no_multiagent",
         "мульти-агент по умолчанию не апгрейд; хрупкость параллельных субагентов"),
    ],
    # s22b карта экипировки — agent-harness-registry [VFY, не подтверждён], concept-свод
    # s22c память — agent-harness-registry [VFY]; concept-параллель с RAG
    "s22d": [  # провал памяти (Letta / Anthropic Memory Tool)
        ("1", "agent-harness-registry (live-eval) — Letta Tier D / Memory Tool 17%-хвост", None,
         "[VFY] источник не подтверждён canonical-URL 2026-08-30; числа volatile (persistbench 1.0/0.833/0.750; 17%)", True),
    ],
    "s22e": [  # операционный слой
        ("1", "Gloaguen et al. 2026 — Evaluating AGENTS.md (presence paradox)", "gloaguen_presence",
         "наличие файла-инструкции не даёт значимого прироста; помогает в пробеле документации", True),
        ("2", "GitHub anthropics/claude-code#51735 (повтор ошибки через 25 дней)", "claude_code_51735",
         "письменная запись о прошлой ошибке не предотвратила её повтор"),
        # NB: chapter цитирует Honest Lying (arXiv:2605.29463) — [VFY], future-dated id
    ],
    "s23": [  # провалы агентов
        ("1", "Sattyam Jain 2026 — The Agent That Burned $4,200 in 63 Hours", "jain_4200",
         "петля без лимитов на HTTP 429; retry-скрипт решил бы задачу почти бесплатно", True),
        ("2", "MindStudio — Reliability Compounding Problem", "mindstudio_reliability",
         "5×99%≈95%, 10→90%, 20→82% — надёжности перемножаются"),
        ("3", "Cognition — Don't Build Multi-Agents (хрупкость)", "cognition_no_multiagent",
         "зависимые подзадачи → параллельные субагенты принимают конфликтующие решения"),
    ],
    "s25": [  # tool attacks / prompt injection / retention
        ("1", "Docker — MCP Horror Stories: GitHub Prompt Injection", "docker_mcp_horror",
         "GitHub MCP heist: issue-инструкция + широкий токен → выгрузка приватных репо"),
        ("2", "Simon Willison — Prompt injection via MCP", "willison_mcp_inject",
         "модель не отличает данные от команды; недоверенный контент = команда"),
        ("3", "Palo Alto Unit 42 — MCP Attack Vectors", "unit42_mcp",
         "tool poisoning / каждое подключение = новая граница доверия"),
        ("4", "Bloomberg Law — NYT v. OpenAI (суд обязал хранить логи)", "nyt_openai_bloomberg",
         "ZDR покрывает не всё; судебный приказ поверх любой политики хранения"),
        ("5", "Anthropic — API and Data Retention (границы ZDR)", "anthropic_retention",
         "ZDR не покрывает third-party / MCP-connector — ровно то, из чего агент состоит", True),
    ],
    "s25b": [  # coding-агенты
        ("1", "agent-harness-registry (обзор через рамку экипировки)", None,
         "[VFY] источник не подтверждён; Claude Code/Aider/Cursor/OpenHands — вендор-сайты, verify day-of", True),
    ],
    # ===== Раздел 5. Фреймворк =====
    "s26": [  # лестница сложности
        ("1", "Anthropic — Building Effective Agents (правило лестницы)", "anthropic_agents",
         "оставайся на нижней ступени; каждый подъём — обмен, не улучшение"),
    ],
    "s27": [  # план решения / decision matrix
        ("1", "Anthropic — Building Effective Agents (маршрут выбора)", "anthropic_agents",
         "маршрут вопросов сверху вниз; шаг 1 — детерминированная задача → обычный код, СТОП"),
        ("2", "McCarthy Tétrault — Air Canada (нижняя плашка)", "aircanada_mccarthy",
         "генеративная архитектура на детерминированную задачу = ошибка нижней строки матрицы"),
    ],
    # s27b стартовый комплект — рифма с лестницей + presence paradox (см. s22e), новый claim не нужен
    "s29": [  # человек-валидатор + NANDA
        ("1", "Anthropic — Reasoning Models faithfulness (self-rationale ≠ контроль)", "anthropic_cot_faith",
         "человек проверяет результат/факты против источника, не самообъяснение модели", True),
        ("2", "MIT NANDA — State of AI in Business 2025 (~95% пилотов без ROI)", "mit_nanda_fortune",
         "корень — learning gap и провал интеграции, не качество модели; отчёт, не закон", True),
    ],
    # s30 мост, s31 Q&A — навигация, внешних claim нет
}
```

---

## Volatile / re-verify day-of (`[VFY]`)

| Slide | Claim / число | Почему VFY |
|---|---|---|
| s06, s21, s29 | CoT faithfulness Claude 3.7 ~25% / DeepSeek R1 ~39% | Anthropic research, quarterly re-check |
| s11 | RAG win-rate выше у меньших моделей (U-NIAH) | arXiv preprint, yearly |
| s14 | «fine-tuning сузился 2026» рамка | market framing, quarterly |
| s15 | LoRA 98.4% из 20 834 карточек | HF blog 2026-06-18, quarterly; growing dataset |
| s19, s25 | MCP adoption / ZDR границы | policy + adoption, quarterly |
| s22d | Letta persistbench 1.0/0.833/0.750; Memory Tool 17%-хвост; версии v0.6.7/v0.16.8 | **agent-harness-registry не подтверждён canonical-URL 2026-08-30 — course-internal / illustrative; проверить день-в-день** |
| s22e | presence paradox (arXiv:2602.11988 future-dated); Honest Lying (arXiv:2605.29463 — не подтверждён) | recent/future-dated preprint ids |
| s23 | $4,200 / 63ч / HTTP 429 | single-author postmortem 2026-04, illustrative, числа округлены |
| s25b | Claude Code/Aider/Cursor/OpenHands профили; «OpenClaw»-гипотеза | вендор-фичи меняются; agent-harness-registry [VFY] |
| s29 | ~95% пилотов MIT NANDA | отчёт с методологией (150 интервью+350 опрос+300 внедрений), подавать как заголовок, не закон |
| — | s05a arXiv:2605.29420 (роль→тон) | future-dated id, не подтверждён; факт «роль≠точность» держит Zheng 2311.10054 (verified) |

## Not confirmed this session (treat as course-internal / illustrative, do NOT present as canonical primary)

- `agent-harness-registry` (github.com/workain/agent-harness-registry) — не найден через WebSearch 2026-08-30; несёт s22b/s22c/s22d/s25b/s27b. Все claim с него → `[VFY]` + framing «по данным независимого реестра live-eval».
- arXiv:2605.29420 (persona→tone), arXiv:2605.29463 (Honest Lying), arXiv:2603.22489 (MCP threat), arXiv:2601.06007 (prompt caching), arXiv:2601.18699 (forgetting mechanism) — future-dated / recent preprint ids; не подтверждены, но у каждого есть verified-опора (Zheng, Gloaguen, Willison/Docker/Unit42, prompt-caching vendor docs, Luo).
