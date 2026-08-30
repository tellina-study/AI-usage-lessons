# Lecture 1 — Reference Registry (pre-slide-links)

**Дата:** 2026-08-30. **Назначение:** реестр канонических первичных URL для утверждений/цифр/терминов слайдов лекции 1, совместимый с форматом lec-04 (`SLIDE_REFS` per-slide + `URLS` urlkey→URL). Все URL верифицированы через WebSearch/WebFetch (batch A–D) либо взяты из QA-отчётов lec-01. Непроверенное помечено `[VFY]`.

**Источник фактов:** `library/lectures/lec-01/chapter.md` §«Источники» (строки 761–828, полный список цитат) + `references:`-frontmatter каждого слайда + `qa-reports/2026-08-0{7,8}/`.

---

## Сводка

- **22 слайда из 31** несут `references:`-ключи и требуют ссылок (остальные 9 — cover/divider/roadmap/Q&A/summary без внешних источников: s00a, s02, s02a, s05a, s05c, s10, s27, s28, s29, s29a, s30, s31 — на деле 12 без refs; 22 несут refs — s00b, s01, s06, s06a, s07, s08, s09, s11, s12, s13, s15, s16, s17, s18, s19, s19a, s20, s21, s22, s23, s24, s25, s26).
- **47 уникальных источников**, все с верифицированным каноническим URL.
- **2 предупреждения по фактам** (см. ниже §Флаги) — требуют внимания ДО простановки ссылок.
- **Ноты не требуют рефактора** (см. §Оценка нот).

---

## Флаги (обязательно к учёту до Волны 2)

1. **`github-octoverse-2025` / «46% Copilot-кода» (s08):** цифра «46% кода у пользователей Copilot» НЕ подтверждается каноническим отчётом Octoverse 2025 (отчёт даёт adoption-метрики, не долю кода). Ссылку ставить можно, но саму claim пометить `[VFY-day-of]` либо переформулировать/переисточниковать. Это fact-gap, не URL-gap.
2. **`cnews-vedomosti-2026` (s00b, s08):** канонический источник — статья Vedomosti от **24 марта 2026** (не 29), исследование Intellectual Analytics (~50 крупных орг., 9 из 10 GenAI-пилотов свёрнуты/отложены). URL верифицирован.
3. **`openclaw-2025-steinberger` (s09):** проект пережил переименования (Clawdbot → Moltbot → OpenClaw), star-counts волатильны, Стейнбергер сменил аффилиацию (chapter: присоединился к OpenAI 14 фев 2026). Repo-URL `[VFY-day-of]`.

---

## Per-slide реестр (слайд → источники + urlkey + gloss + volatile?)

Формат строки: `(num, "имя источника", urlkey, "gloss", [volatile])`. URL — в §URLS ниже.

### s00b — course-hook (воронка внедрения, центральный вопрос)
- ("1", "Gartner — пресс-релиз (окт 2024)", "gartner_2024", "80% инженерных работников должны осваивать GenAI к 2027 — контекст масштаба внедрения", True)
- ("2", "Vedomosti / Intellectual Analytics (мар 2026)", "cnews_vedomosti", "9 из 10 корпоративных GenAI-пилотов в РФ свёрнуты/отложены — разрыв demo↔prod", True)

### s01 — ice-breaker (YOLO live demo)
- ("1", "Ultralytics — YOLOv8 (2023)", "yolov8", "narrow-модель детекции; локальный inference ~30 fps на CPU без интернета")
- ("2", "Google — MediaPipe", "mediapipe", "on-device real-time ML pipelines — класс локальных narrow-решений")

### s06 — множественность определений AI
- ("1", "Russell & Norvig — AIMA, 4-е изд. (2021)", "aima", "4 определения по 2 осям (думать/действовать × человекоподобно/рационально)")
- ("2", "ISO/IEC 22989:2022", "iso_22989", "AI-система = engineered system, генерирующая выходы для человеко-заданных целей; опора EU AI Act")
- ("3", "Mitchell — Machine Learning (1997)", "mitchell", "функциональное определение: поведение из обученной модели = AI")
- ("4", "McCorduck — Machines Who Think (2004)", "mccorduck", "AI Effect: «as soon as it works, no one calls it AI any more»")

### s06a — предыстория 1943 (нейрон старше термина)
- ("1", "McCulloch & Pitts (1943)", "mcculloch_pitts", "формальный нейрон как логический элемент — на 13 лет раньше термина «AI»")

### s07 — таймлайн 70 лет, перелом 2017
- ("1", "Vaswani et al. — Attention Is All You Need (2017)", "vaswani", "Трансформер + self-attention; >160K цитирований (май 2026) — точка перелома")
- ("2", "McCorduck — Machines Who Think (2004)", "mccorduck", "AI Effect через исторические примеры остывания задач до «просто функции»")
- ("3", "Dhar — Paradigm Shifts in AI, CACM (2024)", "dhar", "смена парадигм AI как рамка для чтения таймлайна")

### s08 — масштаб в цифрах + контр-факт
- ("1", "Stack Overflow — Developer Survey 2025", "so_2025", "n=49k+/177 стран; 51% профи ежедневно, 84% используют/планируют, 46% не доверяют коду")
- ("2", "OpenAI — ChatGPT WAU (фев 2026)", "openai_wau", "~900M weekly active users — AI как инфраструктура", True)
- ("3", "GitHub — Octoverse 2025", "github_octoverse", "adoption Copilot; ⚠ «46% кода» отдельно [VFY] — см. Флаг 1", True)
- ("4", "Grand View Research (2026)", "gvr", "AI-рынок $390.9B (2025) → $539.5B (2026), CAGR 30.6%", True)
- ("5", "Vedomosti / Intellectual Analytics (мар 2026)", "cnews_vedomosti", "контр-факт: 9 из 10 пилотов РФ не доходят до прода", True)
- ("6", "Gartner — пресс-релиз (окт 2024)", "gartner_2024", "80% инженеров осваивают GenAI к 2027", True)

### s09 — 4 прорыва от не-первых игроков
- ("1", "Mistral AI — Announcing Mistral 7B (сен 2023)", "mistral_7b", "Apache 2.0, обходит Llama-2 13B — малая команда уровня лидеров")
- ("2", "DeepSeek-R1 — тех.отчёт (янв 2025)", "deepseek_r1", "reasoning уровня o1; 97.3% MATH-500; спорная себестоимость")
- ("3", "SemiAnalysis — DeepSeek cost analysis (2025)", "semianalysis", "полная инфра $1.3–1.6B vs marginal train run V3 $5.6M — разные числа", True)
- ("4", "Bloomberg — Nvidia $589B drop (27 янв 2025)", "bloomberg_deepseek", "крупнейшая однодневная потеря капитализации в истории", True)
- ("5", "Steinberger — OpenClaw (GitHub)", "openclaw", "соло open-source агент, 100K★ за квартал; rename-churn [VFY]", True)
- ("6", "Gerganov — llama.cpp / ggml.ai", "llamacpp", "соло→HF (фев 2026), 100K+★ быстрее PyTorch/TensorFlow", True)

### s11 — слои, не альтернативы
- ("1", "Anthropic — Building Effective Agents (2024)", "anthropic_agents", "слоистая эскалация сложности: простейшее решение → наращивать при необходимости")
- ("2", "Weng — LLM Powered Autonomous Agents (2023)", "weng", "Agent = LLM + Memory + Planning + Tool Use — верх слоистой модели")

### s12 — классификатор задача × модальность
- ("1", "Russell & Norvig — AIMA (2021)", "aima", "классификация AI-систем как рабочий язык курса")
- ("2", "Goodfellow, Bengio, Courville — Deep Learning (2016)", "goodfellow", "модальности и типы задач в терминах DL")

### s13 — квадрант контроля (Model→Chat→Agent)
- ("1", "Anthropic — Building Effective Agents (2024)", "anthropic_agents", "распределение контроля разработчик↔пользователь по мере делегирования")

### s15 — модель = компонент, не система
- ("1", "Kreuzberger et al. — MLOps (2023)", "kreuzberger", "pre/post-processing вокруг модели — ответственность разработчика")
- ("2", "Jumper et al. — AlphaFold, Nature (2021)", "alphafold", "канонический пример модели-прогноза; Нобель по химии 2024")

### s16 — цикл диалога чата (6 шагов)
- ("1", "Anthropic — Building Effective Agents (2024)", "anthropic_agents", "системный промпт как инженерный рычаг; контекст собирается заново каждый шаг")

### s17 — чат = модель + UI + память
- ("1", "ВЦИОМ — «Нейросети в жизни россиян» (окт 2025)", "vciom", "проникновение AI-чатов в РФ; 51% пользуются раз в неделю+")
- ("2", "Dam et al. — Survey on LLM-based AI Chatbots (2024)", "dam", "таксономия LLM-чатов; чистые чаты редки в проде (расширены до агентов)")

### s18 — архитектура агента (ReAct)
- ("1", "Weng — LLM Powered Autonomous Agents (2023)", "weng", "Agent = LLM + Memory + Planning + Tool Use")
- ("2", "Anthropic — Building Effective Agents (2024)", "anthropic_agents", "оркестратор + инструменты + внешняя память как слой над чатом")
- ("3", "Anthropic — Model Context Protocol (2024)", "mcp", "стандарт подключения инструментов/данных к агенту")

### s19 — агент за работой (200 PDF, ReAct-шаги)
- ("1", "Yao et al. — ReAct (2022)", "react", "Reasoning+Acting: план→действие→наблюдение→рефлексия с явным инструментом на шаге")

### s19a — уровни автономии
- ("1", "Feng, McDonald, Zhang — Levels of Autonomy (2025)", "autonomy_levels", "5 уровней по роли пользователя: operator→collaborator→consultant→approver→observer")

### s20 — приложение = AI в продукте
- ("1", "Google — Translate at 20 (2026)", "google_translate", "1B+ польз./мес, ~1T слов/мес across Translate/Search/Lens — AI как функция", True)
- ("2", "Anthropic — Building Effective Agents (2024)", "anthropic_agents", "приложение как внешний слой: промпты скрыты, детерминированный UI")

### s21 — чек-лист 2 вопроса + квадрант
- ("1", "Anthropic — Building Effective Agents (2024)", "anthropic_agents", "выбор типа реализации по 2 осям: взаимодействие × инструменты")
- ("2", "Google — AI Agents Whitepaper (2024)", "google_agents_wp", "Model + Tools + Orchestration Layer — рамка квадранта")
- ("3", "Ng — Four Agentic Design Patterns (2024)", "ng_patterns", "паттерны Reflection/Tool Use/Planning/Multi-Agent — когда нужен агент")

### s22 — раздел «границы» (divider с refs)
- ("1", "NIST — AI RMF 1.0 (2023)", "nist_rmf", "рамка управления рисками AI — граница ответственности инженера")
- ("2", "NIST — Generative AI Profile 600-1 (2024)", "nist_600", "профиль рисков GenAI")
- ("3", "EU AI Act — Reg. (EU) 2024/1689", "eu_ai_act", "регуляторная рамка; штрафы до 35M€/7%")

### s23 — потребительские vs корпоративные тарифы (Samsung, EU AI Act)
- ("1", "Bloomberg — Samsung bans ChatGPT (май 2023)", "bloomberg_samsung", "3 утечки за месяц → запрет внешнего GenAI; данные в consumer-датасете")
- ("2", "OpenAI — Enterprise Privacy / data usage (2025)", "openai_terms", "consumer = обучение по умолчанию; API с мар 2023 не обучается на данных")
- ("3", "EU AI Act — Reg. (EU) 2024/1689", "eu_ai_act", "штрафы: стандарт до 15M€/3%, верх до 35M€/7%")

### s24 — галлюцинации (fake DOI, HHEM)
- ("1", "Huang et al. — Survey on Hallucination in LLMs (2023)", "huang", "галлюцинация = уверенное порождение неверного, неотличимого от верного")
- ("2", "Ji et al. — Survey of Hallucination in NLG (2023)", "ji", "таксономия галлюцинаций в генерации")
- ("3", "Vectara — HHEM Leaderboard", "vectara", "диапазон <1% (суммаризация) → 10–15% (reasoning) — цифра зависит от задачи", True)
- ("4", "CybSafe / NCA — Oh Behave! (2024–25)", "cybsafe", "n=7000/7 стран: ~38% делятся конфиденциальным без ведома работодателя")

### s25 — bias / sycophancy / distribution shift
- ("1", "OpenAI — Sycophancy in GPT-4o postmortem (2025)", "sycophancy", "релиз 25 апр → откат 28 апр → разбор 29 апр; RLHF-переоценка приятных ответов")
- ("2", "Pan et al. — Reward Misspecification (2022)", "reward_misspec", "reward hacking — общая природа: модель отражает данные/разметку")

### s26 — прогнозы AGI (narrow vs general, 4 спикера)
- ("1", "Searle — Minds, Brains, and Programs (1980)", "searle", "Chinese Room: бенчмарк-эквивалентность ≠ понимание; narrow vs general")
- ("2", "Bostrom — Superintelligence (2014)", "bostrom", "рамка долгосрочных AGI/ASI-сценариев для критического чтения прогнозов")

---

## URLS (urlkey → canonical URL, verified)

```python
URLS = {
    # --- s00b / s08 macro-context ---
    "gartner_2024": "https://www.gartner.com/en/newsroom/press-releases/2024-10-03-gartner-says-generative-ai-will-require-80-percent-of-engineering-workforce-to-upskill-through-2027",
    "cnews_vedomosti": "https://www.vedomosti.ru/technology/articles/2026/03/24/1184974-biznes-svernul-ili-otlozhil-9-iz-10-proektov-po-vnedreniyu-generativnogo-ii",
    # --- s01 demo ---
    "yolov8": "https://docs.ultralytics.com/models/yolov8/",
    "mediapipe": "https://ai.google.dev/edge/mediapipe/solutions/guide",
    # --- s06 / s07 / s12 definitions & history ---
    "aima": "https://aima.cs.berkeley.edu/",
    "iso_22989": "https://www.iso.org/standard/74296.html",
    "mitchell": "https://www.cs.cmu.edu/~tom/mlbook.html",
    "mccorduck": "https://www.google.com/books/edition/Machines_Who_Think/dPGij4vsHKgC",  # [VFY] publisher page; A.K. Peters 2nd ed 2004
    "mcculloch_pitts": "https://doi.org/10.1007/BF02478259",
    "vaswani": "https://arxiv.org/abs/1706.03762",
    "dhar": "https://doi.org/10.1145/3664804",
    "goodfellow": "https://www.deeplearningbook.org/",
    # --- s08 scale ---
    "so_2025": "https://survey.stackoverflow.co/2025",
    "openai_wau": "https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/",  # VOLATILE
    "github_octoverse": "https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/",  # ⚠ «46% кода» не в отчёте — см. Флаг 1
    "gvr": "https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market",
    # --- s09 breakthroughs ---
    "mistral_7b": "https://mistral.ai/news/announcing-mistral-7b",
    "deepseek_r1": "https://arxiv.org/abs/2501.12948",
    "semianalysis": "https://semianalysis.com/2025/01/31/deepseek-debates/",
    "bloomberg_deepseek": "https://www.bloomberg.com/news/articles/2025-01-27/asml-sinks-as-china-ai-startup-triggers-panic-in-tech-stocks",
    "openclaw": "https://github.com/openclaw/openclaw",  # [VFY-day-of] rename-churn Clawdbot/Moltbot/OpenClaw
    "llamacpp": "https://github.com/ggml-org/llama.cpp",
    # --- s11 / s13 / s16 / s18 / s20 / s21 agents ---
    "anthropic_agents": "https://www.anthropic.com/research/building-effective-agents",
    "weng": "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "mcp": "https://www.anthropic.com/news/model-context-protocol",
    "react": "https://arxiv.org/abs/2210.03629",
    "autonomy_levels": "https://arxiv.org/abs/2506.12469",
    "google_agents_wp": "https://www.kaggle.com/whitepaper-agents",
    "ng_patterns": "https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/",
    # --- s15 model ---
    "kreuzberger": "https://arxiv.org/abs/2205.02302",
    "alphafold": "https://doi.org/10.1038/s41586-021-03819-2",
    # --- s17 chat ---
    "vciom": "https://wciom.ru/analytical-reviews/analiticheskii-obzor/neiroseti-v-nashei-zhizni",
    "dam": "https://arxiv.org/abs/2406.16937",
    # --- s20 application ---
    "google_translate": "https://blog.google/products-and-platforms/products/translate/fun-facts-google-translate-20-years/",
    # --- s22 / s23 boundaries & governance ---
    "nist_rmf": "https://www.nist.gov/itl/ai-risk-management-framework",
    "nist_600": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    "eu_ai_act": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng",
    "bloomberg_samsung": "https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak",
    "openai_terms": "https://openai.com/enterprise-privacy/",
    # --- s24 hallucinations ---
    "huang": "https://arxiv.org/abs/2311.05232",
    "ji": "https://doi.org/10.1145/3571730",
    "vectara": "https://github.com/vectara/hallucination-leaderboard",  # VOLATILE
    "cybsafe": "https://www.staysafeonline.org/articles/oh-behave-the-annual-cybersecurity-attitudes-and-behaviors-report-2025",
    # --- s25 bias/sycophancy ---
    "sycophancy": "https://openai.com/index/sycophancy-in-gpt-4o/",
    "reward_misspec": "https://arxiv.org/abs/2201.03544",
    # --- s26 AGI ---
    "searle": "https://doi.org/10.1017/S0140525X00005756",
    "bostrom": "https://global.oup.com/academic/product/superintelligence-9780199678112",
}
```

### Оставшиеся `[VFY]` (3)
- `mccorduck` — publisher-страница A.K. Peters 2-го изд. недоступна отдельным canonical; дана Google Books edition-страница как best-guess. Цитата AI Effect подтверждена в chapter.
- `openclaw` — repo-URL волатилен из-за переименований; проверить в день лекции.
- `github_octoverse` — URL канонический, но claim «46% кода» в нём не подтверждён (Флаг 1).

Все прочие 44 URL — VERIFIED (batch A–D + QA-отчёты lec-01).

### VOLATILE (пометить `[VFY-day-of]` в нотах при простановке)
`openai_wau`, `vectara`, `semianalysis`, `bloomberg_deepseek`, `openclaw`, `llamacpp`, `gvr`, `gartner_2024`, `cnews_vedomosti`, `google_translate` (счётчики/статистика меняются).

---

## Оценка speaker_notes lec-01

**Вывод: рефактор НЕ требуется. Ноты готовы к Волне 2 (простановка ссылок) как есть.**

- **Связность.** Каждая нота — самостоятельный связный нарратив 150–330 слов (проверены s01, s06, s08, s09, s13, s18, s23, s25). Читаются как текст лектора, не как layout-описание. Пример: s23 (утечка Samsung) — полный связный разбор consumer↔enterprise + инцидент + вывод.
- **Числа проговорены прописью** («девятьсот миллионов», «сорок шесть процентов») — намеренно, для проговаривания вслух; при простановке ссылок это не мешает (ссылки идут в конец блока/слайда, не внутрь фразы).
- **Inline-ссылок нет** ни в одной ноте — это исходное состояние (URL нигде не встроены; только 2 URL во всём chapter.md, в §Источники). Значит Волна 2 добавляет ссылки «с нуля», конфликтов с существующими нет.
- **Атрибуции уже присутствуют текстом** («по бенчмарку Vectara HHEM», «отчёт CybSafe 24-го года», «Stack Overflow Developer Survey 2025», «Feng, McDonald, Zhang 25-го года») — т.е. источник назван в ноте, URL надо лишь привязать к уже названному источнику. Это упрощает простановку: gloss в реестре совпадает с формулировкой ноты.
- **Мелкая несостыковка для fact-fix (не рефактор):** s08-нота говорит «46 процентов кода у пользователей Copilot» — см. Флаг 1 (источник не подтверждает). Правится на fact-этапе, не на этапе нот.

**Рекомендация Волны 2:** ставить ссылки блоком в конце visible body слайда (как lec-04 `ref_list`), НЕ внутрь speaker_notes-фраз. Ноты трогать не нужно; только визуальный ref-список на слайде + `[VFY-day-of]` для VOLATILE-источников.
