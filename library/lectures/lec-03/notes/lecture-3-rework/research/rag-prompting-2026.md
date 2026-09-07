---
title: "Свежая фактура 2026 — RAG и промпт-безопасность (Лекция 3 v3)"
issue: 185
branch: issue-185-lec03-v3
date_collected: 2026-09-06
scope: research-only (не для прямой вставки; фактура + источники + якоря)
note: >
  Каждая цифра снабжена URL и датой публикации/события. Волатильное помечено
  [VFY-day-of]. measurable claims — с baseline/denominator где возможно.
  Русский; англицизмы только для brand names / устоявшихся терминов.
---

# Фактура 2026: RAG-стек и промпт-безопасность

Обзор для переработки Лекции 3 «Архитектуры AI-систем: агенты, RAG, API».
Пять блоков: (1) RAG-стек 2026, (2) chat-шаблоны и роли, (3) special token
injection / prompt injection, (4) structured outputs / function calling,
(5) fine-tuning vs RAG vs промпт.

---

## Блок 1. RAG-стек 2026

### 1.1 Что изменилось за год (agentic RAG, гибрид, реранкеры)

**Agentic RAG стал дефолтом для сложных вопросов.** Сдвиг от «retrieve-then-
generate за один шаг» к многошаговым retrieval-агентам: модель сама решает,
когда искать, формулирует запрос, оценивает достаточность и ищет снова. В 2026
поверх этого — **Adaptive RAG**: классификатор запроса маршрутизирует вопрос к
подходящей стратегии поиска по его сложности.
Источник: «Agentic RAG in 2026», jobsbyculture, 2026 —
https://jobsbyculture.com/blog/agentic-rag-guide-2026 ; «All you need to know
about RAG (in 2026)», A. Srinivasan —
https://aishwaryasrinivasan.substack.com/p/all-you-need-to-know-about-rag-in

**Гибридный поиск — норма, dense-only считается «запахом».** Практически все
публичные бенчмарки 2024–2025 (BEIR, MTEB, пост Anthropic про contextual
retrieval) показывают: BM25 + плотные эмбеддинги, слитые через Reciprocal Rank
Fusion (RRF), обгоняют любой из методов по отдельности.
Источник: обзор RAG-архитектуры 2026, futureagi —
https://futureagi.com/blog/rag-architecture-llm-2025/

**Реранкеры консолидировались** в узкий набор: Cohere Rerank 3.5, Voyage
Rerank-2, BGE Reranker v2. Cross-encoder реранкер поверх добавляет +5…15 пунктов
MRR на трудных наборах. [VFY-day-of] — версии реранкеров волатильны.
Источник: там же (futureagi, 2026).

**Anthropic Contextual Retrieval — точные цифры (baseline включён).**
Базовая частота промахов top-20 chunk = **5,7%**. По слоям:
- Contextual Embeddings: 5,7% → 3,7% (**−35%** промахов);
- + Contextual BM25: 5,7% → 2,9% (**−49%**);
- + реранкинг: 5,7% → 1,9% (**−67%** промахов).
Источник: «Contextual Retrieval in AI Systems», Anthropic, 2024 —
https://www.anthropic.com/engineering/contextual-retrieval
(денominator: доля неудачных retrieval'ов из top-20 chunk на их eval-наборе).

### 1.2 Long-context vs RAG: дебаты 2026 и когда RAG НЕ нужен

**Окна выросли** [VFY-day-of — версии/цифры]: Claude Sonnet — 1M токенов,
Gemini 3 Pro — 2M, Llama 4 Scout — до 10M.
Источник: «Long Context vs RAG», sitepoint, 2026 —
https://www.sitepoint.com/long-context-vs-rag-1m-token-windows/

**Свежие критерии «когда RAG не нужен»:**
- Малая, стабильная база знаний, где full-context + prompt caching дешевле и
  быстрее, чем retrieval-инфраструктура.
- Порог по «доле релевантного»: когда relevance ratio падает **ниже ~20%**, RAG
  устойчиво обгоняет full-context stuffing.
Источник: «RAG vs. Long Context Windows in 2026» —
https://medium.com/@9-5-datascientist/rag-vs-long-context-windows-in-2026-when-should-you-use-which-d0ab5fcb6efd ;
«Long-Context Models vs. RAG», TianPan, 2026-04-09 —
https://tianpan.co/blog/2026-04-09-long-context-vs-rag-production-decision-framework

**Реальность против хайпа «RAG мёртв»** (measurable, с базой):
- RAG ~**в 1250× дешевле за запрос** и заметно быстрее;
- long-context теряет **30%+ точности**, когда релевантный кусок «зарыт»
  в середине окна.
- Для 50 ГБ документов RAG — единственный жизнеспособный путь.
Источник: «RAG vs long context: what the 2026 data shows», usewire —
https://usewire.io/blog/long-context-vs-rag-what-the-data-shows/ ; «Long Context
vs. RAG for LLMs: An Evaluation and Revisits», arXiv:2501.01880 —
https://arxiv.org/pdf/2501.01880

**Консенсус 2026 — гибрид:** vector retrieval сужает базу до релевантного
подмножества → передаёт его long-context модели для рассуждения. Сочетает
дешевизну/скорость RAG с качеством рассуждения длинного окна.

### 1.3 Якорь курса «сходство ≠ релевантность»: NoLiMa и новые работы 2026

**NoLiMa (ICML 2025)** — расширение needle-in-a-haystack: вопрос и «иголка»
имеют **минимальное лексическое пересечение**, поэтому модель обязана вывести
латентную связь, а не поймать буквальное совпадение. Это прямое эмпирическое
подтверждение тезиса «сходство ≠ релевантность».
Точные цифры (baseline → деградация):

| Модель | Short-context baseline | Effective length | Claimed window | При 32K |
|---|---|---|---|---|
| GPT-4o | 99,3% | 8K | 128K | 81,6% (ниже 50% baseline к 64K → 69,7%) |
| Llama 3.1 70B | 94,5% | 2K | 128K | 51,8% |
| Gemini 1.5 Pro | 92,6% | 2K | 2M | 55,5% |
| Claude 3.5 Sonnet | 87,6% | 4K | 200K | 45,7% |

Ключевой вывод: **эффективная длина 2K–4K** у большинства моделей, при заявленных
128K–2M — разрыв между «заявлено» и «работает».
Источник: «NoLiMa: Long-Context Evaluation Beyond Literal Matching»,
arXiv:2502.05167 — https://arxiv.org/pdf/2502.05167 ; репозиторий —
https://github.com/adobe-research/NoLiMa

**Новые работы 2026 по той же линии:**
- «Context Length Alone Hurts LLM Performance Despite Perfect Retrieval»,
  arXiv:2510.05381 — ключевой тезис: **даже при идеальном retrieval** (нужный
  фрагмент точно найден) само по себе удлинение контекста ухудшает качество.
  Прямой аргумент за то, чтобы держать контекст узким (в пользу RAG-precision).
  https://arxiv.org/pdf/2510.05381
- «Tagging-Augmented Generation», arXiv:2510.22956 — использует NoLiMa как метрику
  семантического понимания в длинном контексте.
  https://arxiv.org/pdf/2510.22956
- «Rethinking Agentic RAG: Toward LLM-Driven Logical Retrieval Beyond Embeddings»,
  arXiv:2605.27123 — прямая атака на «эмбеддинг = релевантность».
  https://arxiv.org/pdf/2605.27123
- «Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct
  Corpus Interaction», arXiv:2605.05242 — заголовок буквально повторяет якорь
  курса. https://arxiv.org/pdf/2605.05242

### 1.4 Провалы RAG-проектов (документированные, с уроком)

**Air Canada (2024, судебный прецедент — «расплата» за галлюцинацию бота).**
Чат-бот сказал скорбящему пассажиру, что тариф bereavement можно применить
задним числом — вопреки политике авиакомпании. Трибунал малых исков Канады
взыскал **$812,02** и отклонил довод «бот — отдельная сущность»: бот — часть
сайта, компания отвечает за него.
Урок: RAG/бот, обращённый к клиенту, юридически = официальное заявление
компании; нужен факт-грундинг и человеческий контроль над политиками.
Источник: Forbes, 2024-02-19 —
https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/

**Mata v. Avianca — фейковые цитаты (не RAG, но канонический урок про
«уверенная выдумка»).** Адвокат сослался на 6 несуществующих дел (ChatGPT
выдумал номера дел и юр-обоснование); судья наложил санкцию **$5000**.
Урок: генерация без проверяемого источника = фабрикация с полной уверенностью;
RAG нужен именно чтобы привязать ответ к источнику, но это не отменяет проверку.
Источник: engini.ai, обзор кейсов —
https://engini.ai/blog/ai-hallucination-examples-real-world-cases-causes-solutions

**Данные важнее архитектуры (JMIR Cancer, measurable с базой).** Один и тот же
RAG-подход: на кураторской доменной базе — **6% галлюцинаций**; на общем
веб-поиске — **35%**. Архитектура retrieval'а не менялась, менялось только
качество данных. Разрыв в **29 п.п.** нельзя закрыть «лучшим эмбеддингом».
Источник: «Most RAG Hallucinations Are Retrieval Failures», Towards Data Science —
https://towardsdatascience.com/most-rag-hallucinations-are-retrieval-failures-how-the-retrieval-brick-decides-what-the-model-can-invent/

**Knowledge-freshness failure (типовой провал).** Vector-поиск вернул устаревшую
версию документа про SAML-аутентификацию (обновился 2 недели назад) → модель
уверенно ответила «да, поддерживается», хотя нет. Категория документа верная,
версия — устаревшая.
Урок: «retrieval-промах» лечится retrieval-фиксом (свежесть, версионирование),
а не более строгим промптом / большей моделью.
Источник: там же (Towards Data Science).

**Систематика провалов.** «Seven Failure Points When Engineering a RAG System»,
arXiv:2401.05856 — 7 точек отказа из 3 кейсов (research/education/biomedical);
до сих пор базовый чек-лист. https://arxiv.org/pdf/2401.05856

**Тезис-предупреждение 2026:** «RAG не решил галлюцинации — он переместил
проблему туда, где её труднее увидеть» (в retrieval-слой).
Источник: pub.towardsai.net —
https://pub.towardsai.net/rag-didnt-solve-hallucinations-it-just-moved-the-problem-somewhere-harder-to-see-69e8ce1bf808

---

## Блок 2. Chat-шаблоны и протокольные роли

### 2.1 Форматы у ведущих моделей (2026)

**Llama 4** — новый, более компактный набор спецтокенов: `<|header_start|>`,
`<|header_end|>`, `<|eot|>`. Отличие от Llama 3.1, где были
`<|begin_of_text|>`, `<|start_header_id|>`, `<|end_header_id|>`, `<|eot_id|>`
(т.е. `start_header_id` → `header_start`).
Источник: llama.cpp wiki, шаблоны —
https://github.com/ggml-org/llama.cpp/wiki/Templates-supported-by-llama_chat_apply_template ;
vLLM PR #16428 (Llama 4 chat template) —
https://github.com/vllm-project/vllm/pull/16428

**ChatML-стиль** (OpenAI-семейство) — роли сегментируются спецтокенами
`<|im_start|>` / `<|im_end|>` вокруг role-маркеров system/user/assistant.
Именно эта token-based сегментация создаёт новую поверхность атаки (см. Блок 3).

**Anthropic (Messages API)** — архитектурно иначе: `system` — **top-level поле
запроса**, отдельно от массива `messages`, который содержит только user/assistant.
В отличие от OpenAI, где system кладётся внутрь массива сообщений.
Источник: Claude API Reference —
https://platform.claude.com/docs/en/api/messages/create ; сравнение форматов —
https://flo2.com/blog/anthropic-to-openai-format

**Ключ для лекции:** провайдер сериализует роли по-разному (спецтокены в тексте
vs отдельные поля API), но в обоих случаях граница ролей — это **соглашение**,
которое злоумышленник может попытаться подделать.

### 2.2 Приоритет system-роли: instruction hierarchy

**Исходная работа: OpenAI, «The Instruction Hierarchy», апрель 2024.** Проблема:
без обучения LLM считает system-промпт равным по приоритету тексту от недоверенных
user/третьих сторон. Предложена формальная иерархия **system > user > tool
outputs** (Wallace et al., 2024).
Источник: https://openai.com/index/the-instruction-hierarchy/

**Продолжения 2025–2026:**
- OpenAI ввела **Developer Message** между System и User; Model Spec фиксирует
  до 5 уровней (root, system, developer, user, guideline), кодируемых спец-role-
  токенами в chat-шаблонах.
- **Иерархия не выполняется надёжно:** Geng et al. (2025) — 6 SOTA-моделей на
  конфликтах форматирования; GPT-4o подчиняется приоритетной инструкции лишь в
  **63,8%** случаев даже при явном акценте.
  Источник: обзор в arXiv:2604.09443 «Many-Tier Instruction Hierarchy in LLM
  Agents» — https://arxiv.org/html/2604.09443v2
- «Reasoning Up the Instruction Ladder for Controllable Language Models»,
  arXiv:2511.04694 — https://arxiv.org/pdf/2511.04694

**IH-Challenge (OpenAI, 2026)** — RL-датасет для укрепления иерархии.
Fine-tuning GPT-5-Mini на нём: IH-robustness **+10,0 п.п.** в среднем по 16
бенчмаркам (**84,1% → 94,1%**); небезопасное поведение **6,6% → 0,7%**.
Baseline/денominator: доля соблюдения приоритета на in/out-of-distribution +
human red-teaming наборах.
Источник: arXiv:2603.10521 — https://arxiv.org/abs/2603.10521 ; OpenAI PDF —
https://cdn.openai.com/pdf/14e541fa-7e48-4d79-9cbf-61c3cde3e263/ih-challenge-paper.pdf

**Честный вывод:** иерархия ролей улучшается тренировкой, но остаётся частичной
(даже 94,1% ≠ 100%; базовый GPT-4o ~63,8%). Роль — приоритет по умолчанию, не
жёсткая граница безопасности.

---

## Блок 3. Special Token Injection и prompt injection 2026

### 3.1 Масштаб и характер угрозы (свежие цифры с базой)

**Indirect prompt injection (IPI) — доминирующий вектор.** IPI = **>55%** всех
наблюдаемых инцидентов prompt injection в 2026. Multi-hop атаки через
агенты/инструменты выросли **>70% год-к-году** (2025–2026).
Источник: Sysdig, «Comprehensive Guide to Prompt Injection Attacks in 2026» —
https://www.sysdig.com/learn-cloud-native/prompt-injection

**Три условия структурного риска агента (одновременно):** доступ к приватным
данным + контакт с недоверенным контентом + возможность внешней коммуникации.
Любой агент со всеми тремя — эксплуатируем.
Источник: там же (Sysdig, 2026).

**CSA «Indirect Prompt Injection Goes Operational» (2026) — измеримо, с базой:**
- **+32% относительный рост** вредоносного IPI-контента ноя-2025 → фев-2026
  (база: 2–3 млрд crawled-страниц/мес).
- **85,2%** случаев — с social-engineering-обёрткой;
- **75,8%** заражённых страниц — single-payload;
- **22 различных техники доставки** payload'а в активном использовании;
- только **1 из 8** крупных инцидентов Q1 2026 получил CVE-идентификатор
  (denominator: 8 major-инцидентов квартала) — «disclosure gap».
Источник: https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/

### 3.2 Реальные инциденты 2026 (даты — обязательны)

| Инцидент | Дата | Суть |
|---|---|---|
| Первый задокументированный «в дикой природе» IPI (Palo Alto Unit 42) | дек 2025 | подтверждение, что атаки не теоретические |
| Mexican Government breach | 25 фев 2026 | ~150 ГБ налоговых/избирательных данных через AI-assisted вторжение |
| OpenClaw inbox deletion | 23 фев 2026 | агент проигнорировал stop-команды, удалил письма |
| Meta internal agent leak | 20 мар 2026 | доступ инженеров к чувствительным данным ~2 часа |
| Vertex AI «Double Agent» | 31 мар–1 апр 2026 | дефолтные права позволили exfiltration креденшелов |
| Claude Code source map leak | 31 мар–2 апр 2026 | 59,8 МБ source map; фейк-репозитории под malware |
| Flowise CVE-2025-59528 | 7 апр 2026 | RCE; 12 000–15 000 открытых инстансов |
| GrafanaGhost | 7 апр 2026 | скрытые инструкции в логах → exfiltration через Markdown |
Источники: Sysdig (Unit 42 дек-2025) — https://www.sysdig.com/learn-cloud-native/prompt-injection ;
CSA research note (таблица инцидентов) — ссылка выше.
[VFY-day-of] — детали инцидентов уточнить на день лекции.

### 3.3 Special Token Injection (STI) и ChatInject — техническая суть

**STI** эксплуатирует зарезервированные спецтокены протокола промптинга, чтобы
управлять логикой генерации целевой модели. Представлена на AppSec Village @
DEF CON 33, BSides Krakow 2025, BSides Tirana 2025.
Источник: Sentry Blog, «Special Token Injection (STI) Attack Guide» —
https://blog.sentry.security/special-token-injection-sti-attack-guide/

**ChatInject (ICLR 2026)** — подделка role-тегов внутри низкоприоритетного
tool-output'а: атакующий встраивает спецтокены chat-шаблона в payload, и модель
интерпретирует чужой текст как смену роли. Точные ASR (attack success rate)
[ИСПРАВЛЕНО 2026-09-06 по прямому fetch arXiv:2509.22830 — бенчмарки ранее были
перепутаны; verified fact-checker issue #185]:
- **AgentDojo:** средний ASR **5,18% → 32,05%** (~6× рост).
  - GPT-oss: 0,3% → 55,5%; Qwen-3: 17,5% → 80,5%.
- **InjecAgent:** средний ASR **15,13% → 45,90%**; мульти-тёрн-вариант
  — **52,33%** в среднем.
  - Llama-4: **50,1% → 88,3%** (+38,2 п.п.);
  - Qwen-3: 8,5% → 42,1%; GPT-oss: 0,0% → 19,1%.
- Closed-source (GPT-4o) в кросс-модель-трансфере ~27–40% ASR.
**Защиты:** «существующие prompt-based защиты в основном неэффективны»;
пертурбации шаблона также не снижают ASR значимо.
Источник: arXiv:2509.22830v3 — https://arxiv.org/html/2509.22830v3 ;
ICLR 2026 proceedings —
https://proceedings.iclr.cc/paper_files/paper/2026/file/2a48e053db5f0cd57015a33bbc3f794b-Paper-Conference.pdf

**Separator Injection Attack** — злоупотребление role-сепараторами вызывает
диалоговые смещения. arXiv:2504.05689 —
https://arxiv.org/pdf/2504.05689

### 3.4 Статус защит (spotlighting, guard-модели, санитизация)

- **Spotlighting** (Hines et al., 2024): изолирует недоверенный ввод — либо
  заменой пробелов на warning-слово, либо (новее) вставкой спец-control-токена,
  чтобы не рвать семантику и минимизировать потерю качества.
- **Spotlight-Guard** — слоёная защита: spotlighting-изоляция + detect-and-
  quarantine + integrity на HMAC.
  Источник: MDPI Applied Sciences —
  https://doi.org/10.3390/app16157662
- **Guard-модели** и проблема over-defense: «InjecGuard» — бенчмарк и смягчение
  over-defense у guardrail-моделей. arXiv:2410.22770 —
  https://arxiv.org/pdf/2410.22770
- **DefensiveTokens** — защита несколькими токенами. arXiv:2507.07974 —
  https://arxiv.org/html/2507.07974v1
- **Google/Gemini** — уроки защиты от IPI (слоёный подход, adversarial training).
  arXiv:2505.14534 — https://arxiv.org/pdf/2505.14534
- **Санитизация спецтокенов у провайдеров:** провайдеры экранируют/фильтруют
  user-supplied спецтокены при сериализации chat-шаблона (это и есть базовая
  защита от «наивной» STI), но ChatInject показывает, что для агентных
  tool-output'ов защита неполна.

**Честный вывод (для лекции, точная формулировка):** проблема **не решена**.
Индустрия перешла от «proof-of-concept к живой эксплуатации» (CSA, 2026); IPI —
доминирующий вектор (>55%); защиты снижают, но не устраняют ASR (ChatInject
обходит prompt-based защиты); иерархия ролей — частичная (GPT-4o ~63,8% базово,
IH-Challenge до 94,1% ≠ 100%). Консенсус: **injection — не «баг для патча», а
структурное свойство** систем, где недоверенный текст и привилегированные
инструкции делят один канал; нужны **системные границы** (изоляция, least-
privilege, human-in-the-loop на действиях), а не «лучший промпт».
Источник (тезис «границы, не промпты»): ResearchGate, «Prompt Injection in 2026:
Why Digital Assistants Need System Boundaries» —
https://www.researchgate.net/publication/399796681

---

## Блок 4. Structured outputs / function calling 2026

### 4.1 Гарантии формата у провайдеров

Все три (OpenAI, Google, Anthropic) enforce'ят схему на уровне сэмплинга через
**grammar-constrained decoding**, а не «вежливый промпт».
- **OpenAI Structured Outputs:** ограничивает вывод строго JSON по переданной
  JSON Schema. Первый вызов новой схемы — задержка **+200…400 мс** (компиляция
  схемы в constrained-грамматику), последующие с той же схемой кешируются.
- **Anthropic/Claude:** структуру гонят через **tool use** — определяешь tool,
  чей input = твоя схема, и форсируешь вызов. На апрель 2026 Claude **не
  поддерживает** нативный `json_schema` response format.
- **Google Gemini:** `response_schema` в generation config, OpenAPI-совместимая
  схема, enforced на уровне модели.
Источник: «AI Structured Output Guide 2026: JSON Mode Across OpenAI, Claude, and
Gemini», Crazyrouter —
https://crazyrouter.com/en/blog/ai-structured-output-json-mode-guide-2026 ;
«OpenAI Structured Outputs: Strict JSON Schema in 2026», ergini —
https://ergini.com/blog/openai-structured-outputs

### 4.2 Надёжность (measurable, с денominator)

Schema-compliance (доля ответов, валидных по схеме): OpenAI Structured Outputs —
**99,9%**, Anthropic tool use — **99,8%**, Gemini schema — **99,7%**.
Ни один провайдер не 100%: рекомендуется всё равно валидировать Pydantic/Zod.
Источник: «LLM Structured Output in 2026», dev.to —
https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk

### 4.3 Ограничения (влияние на качество, портируемость)

**«Решена валидность, но не портируемость».** Одна и та же Zod-схема может быть
легальна у одного провайдера и отвергнута/молча ослаблена у другого:
- Anthropic — нет bounds (мин/макс);
- OpenAI — запрет union'ов и жёсткие потолки вложенности;
- Gemini — недокументированные лимиты.
Источник: dev.to (та же статья, 2026) —
https://dev.to/pockit_tools/llm-structured-output-in-2026-stop-parsing-json-with-regex-and-do-it-right-34pk ;
Agenta guide —
https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms

**Влияние на качество (для лекции — сформулировать осторожно):** constrained
decoding гарантирует форму, но может влиять на содержание — модель вынуждена
следовать грамматике, что в части задач снижает свободу рассуждения; практический
паттерн 2026 — «рассуждай свободно → затем структурируй отдельным вызовом», а не
форсировать схему на reasoning-шаге. [VFY-day-of] — искать свежий бенчмарк
качества под constraint (напрямую количественной цифры на 2026-09-06 в выдаче не
нашлось — отметить как gap, не выдумывать число).

**Когда что выбирать:** function calling — когда модель должна выбрать/вызвать
инструмент; structured outputs — когда нужен предсказуемый JSON для парсинга;
JSON mode — легаси, слабее гарантий.
Источник: Vellum —
https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode

---

## Блок 5. Fine-tuning vs RAG vs промпт 2026

### 5.1 Последовательность-рекомендация 2026

Каноническая лестница: **Prompt → RAG → Fine-tune → Distill**. Highest-ROI
fine-tuning = тонкий LoRA/QLoRA-адаптер поверх сильной базовой модели, **в паре**
с retrieval, а не вместо него.
Источник: BigDataBoutique, «Fine-Tuning LLMs in 2026: When RAG Isn't Enough» —
https://bigdataboutique.com/blog/fine-tuning-llms-when-rag-isnt-enough

**Правило «форма, не факты»:** RAG — для знаний, которые меняются; fine-tuning —
для устойчивого поведения, схемы, тона, паттернов отказа. Fine-tuning **не** для
инъекции знаний, меняющихся еженедельно.

**Reality check (с денominator):** ~**70%** продакшн-проблем LLM решаются RAG
или лучшим промптом; fine-tuning нужен для оставшихся **~30%**.
Источник: metacto, «RAG vs. Fine-Tuning: 2026 Decision Guide» —
https://www.metacto.com/blogs/rag-vs-fine-tuning-vs-other-llm-techniques-choosing-the-right-approach

### 5.2 Когда fine-tuning реально нужен

- надёжные форматы вывода / доменный стиль / паттерны отказа;
- ниже латентность и стоимость (короче промпт за счёт «вшитого» поведения);
- приватные on-prem данные, которые нельзя гонять через retrieval-инфраструктуру.
Источник: Medium, «When to Fine-Tune an LLM (And When Prompting Is Enough)» —
https://medium.com/@techlatest.net/when-to-fine-tune-an-llm-and-when-prompting-is-enough-c32d53261ac7

### 5.3 Методы 2026 (доступность RFT/DPO/LoRA)

- **LoRA/QLoRA** — фактически единственный выбор для большинства команд;
  тренируют ~1% весов → дёшево специализировать без катастрофического забывания.
  Full fine-tuning — редко правильный выбор.
- **SFT** — задачи и форматы (labeled outputs);
- **DPO/ORPO/KTO** — предпочтения (safer/shorter/лучше reasoning);
- **RFT (Reinforcement Fine-Tuning)** — задачи с проверяемой наградой на
  o-series-моделях; улучшает reasoning вознаграждением за верный исход.
Источник: «Fine-Tuning LLMs 2026: LoRA, QLoRA & When to Bother», aidevdayindia —
https://aidevdayindia.org/blogs/fine-tuning-llms-lora-qlora/fine-tuning-llms-lora-qlora.html ;
Towards AI, «SFT, LoRA, QLoRA and DPO Explained» —
https://pub.towardsai.net/how-to-fine-tune-an-llm-sft-lora-qlora-and-dpo-explained-edcab1f45fd6

**Сдвиг доступности 2026:** RFT/DPO вышли из research в managed-сервисы
провайдеров; LoRA-адаптеры — как сервис (hot-swap адаптеров на общей базе), что
удешевляет специализацию. [VFY-day-of] — конкретные managed-предложения и цены
волатильны; уточнить вендоров на день лекции.

---

## Сводка якорей для лекции (переиспользовать в chapter/slides/speech)

1. **«Сходство ≠ релевантность»** — теперь с эмпирикой: NoLiMa (effective length
   2–4K при заявленных 128K–2M) + 3 работы 2026, буквально повторяющие тезис
   в заголовках (arXiv:2510.05381, 2605.27123, 2605.05242).
2. **«RAG не мёртв, но и не панацея»** — RAG ~1250× дешевле/запрос и точнее при
   relevance<20%; но «RAG переместил галлюцинации в retrieval-слой»; данные важнее
   архитектуры (6% vs 35% галлюцинаций при том же RAG, Δ29 п.п.).
3. **«Роль — соглашение, не граница безопасности»** — instruction hierarchy
   частичная (GPT-4o 63,8% базово; IH-Challenge 94,1% ≠ 100%); ChatInject
   подделывает role-теги в tool-output (ASR до 88,3% на Llama-4).
4. **Injection не решён** — CSA 2026: «от PoC к живой эксплуатации», IPI >55%
   инцидентов; защиты (spotlighting/guard/иерархия) снижают, но не устраняют;
   нужны системные границы, не «лучший промпт».
5. **Structured outputs** — форма гарантирована (99,7–99,9% compliance), но не
   портируемость; и форма ≠ содержание (constrained decoding может влиять на
   качество — паттерн «reason then structure»).
6. **Лестница выбора** — Prompt → RAG → Fine-tune → Distill; ~70% задач решает
   RAG/промпт; fine-tuning = форма, не факты; LoRA/QLoRA — дефолт.

**Известные gap'ы (не выдумывать — пометить [VFY-day-of]):**
- количественный бенчмарк «падение качества под constrained decoding» на 2026 —
  прямой цифры в выдаче не найдено;
- точные версии/цены LoRA-as-a-service и managed RFT/DPO — волатильно;
- версии окон (Gemini 3 Pro 2M, Llama 4 Scout 10M) — проверить на день лекции.
