# Fact-Checker Report — Лекция 3 «Архитектуры AI-систем» chapter.md (Часть 1–3) — 2026-05-16 (Phase 3, v1)

VERDICT: APPROVE-WITH-POLISH

## Severity counts
- **P0** (false fact / broken citation / direction inversion / curriculum hallucination / misquote): **0**
- **P1** (missing source / suspicious number без caveat / нужная метка отсутствует / freshness expired): **2**
- **P2** (cite format / minor / overgeneralization с hedge): **4**

Глава прошла факт-чек с очень высоким качеством. Все 13 критичных утверждений, все цитаты в кавычках и все arXiv-ID, проверенные через WebSearch/WebFetch, **подтвердились дословно или с корректной атрибуцией**. Метки `[FACT-CHECK]`/`[VFY]` расставлены адекватно классу источника. Ни одной фактической ошибки, ни одной выдуманной ссылки, ни одной инверсии направления, ни одного мисквота. P1 — это две метки, которые желательно усилить/добавить; P2 — косметика. Это не структурный gap → APPROVE-WITH-POLISH, не REVISE.

---

## Verified facts — таблица (проверено live через WebSearch/WebFetch 2026-05-16)

| Утверждение (кратко) | Где | Статус | Источник + дата | Freshness | Fix |
|---|---|---|---|---|---|
| Moffatt v. Air Canada, трибунал BC, решение **14.02.2024** | Введение, §2.5, Источники | **VERIFIED** | 2024 BCCRT 149; McCarthy 2024; ABA 2024 (CanLII) | STABLE (legal-of-record) | — |
| Чат-бот сказал «возврат в течение **90 дней**» / ретроактивно | Введение, §2.5 | **VERIFIED** | CanLII 2024 BCCRT 149; Manatt; WEL Partners | STABLE | — (90-дн деталь подтверждена в самом решении, не только в law-блогах) |
| Судья назвал аргумент «remarkable» (чат-бот — отд. юрлицо) | Введение, §2.5 | **VERIFIED** (точная цитата «This is a remarkable submission») | McCarthy Tétrault 2024 | STABLE | — |
| Air Canada обязали компенсировать разницу | Введение, §2.5 | **VERIFIED** ($812.02 CAD итого) | CanLII 2024 BCCRT 149 | STABLE | — |
| CoT faithfulness: Claude 3.7 Sonnet ~**25%**, DeepSeek R1 ~**39%** | §1.3, Источники | **VERIFIED дословно** | Anthropic «Reasoning Models Don't Always Say What They Think», апр-2025 (paper Chen/Benton et al.) | QUARTERLY (`[VFY]` стоит) | — |
| Для «опасных» подсказок faithfulness ниже (Claude 41% / R1 19%) | §1.3 | **VERIFIED** | Anthropic апр-2025 | QUARTERLY | — |
| Faithfulness падает на трудных задачах (GPQA vs MMLU); outcome-RL → плато | §1.3, DDB1 | **VERIFIED** (направление верное) | Anthropic апр-2025 | QUARTERLY | — |
| Anthropic «Building Effective Agents» (2024-12-19) — цитаты «простейшее решение», workflow/agent | §1.1, §4.4, Источники | **VERIFIED** (перевод верен оригиналу) | anthropic.com/research/building-effective-agents | STABLE | См. P2-1 |
| Anthropic «Effective Context Engineering» (2025-09-29, c Sonnet 4.5) — «наименьший набор высокосигнальных токенов» | §1.4, Источники | **VERIFIED** (точный перевод «Find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome»; дата и Sonnet 4.5 верны) | anthropic.com/engineering | STABLE | — |
| context rot = Chroma 2025; n² связи + меньше параметров на длинные зависимости | §1.4 | **VERIFIED** (Chroma «Context Rot» 2025) | research.trychroma.com/context-rot | STABLE | — |
| Wei et al. 2022 — arXiv:2201.11903 (few-shot CoT) | DDB1, Источники | **VERIFIED** (точный title + авторы) | arXiv:2201.11903 | STABLE | — |
| Kojima et al. 2022 — arXiv:2205.11916 (zero-shot CoT) | DDB1, Источники | **VERIFIED** (точный title + авторы; NeurIPS 2022) | arXiv:2205.11916 | STABLE | — |
| Wang et al. 2022 — arXiv:2203.11171 (self-consistency) | DDB1, Источники | **VERIFIED** (title «Self-Consistency Improves Chain of Thought Reasoning in Language Models»; ICLR 2023) | arXiv:2203.11171 | STABLE | — |
| Lewis et al. 2020 — arXiv:2005.11401 (RAG, NeurIPS 2020) | §2.1, Источники | **VERIFIED** (точный title + авторы + NeurIPS 2020) | arXiv:2005.11401 | STABLE | — |
| Liu et al. 2023 — arXiv:2307.03172 «Lost in the Middle» (TACL 2023) | §1.4, Источники | **VERIFIED** (точный title + авторы) | arXiv:2307.03172 | STABLE | — |
| U-NIAH 2025 — arXiv:2503.00353; RAG сильнее у меньших моделей (win-rate 82.58%) | §2.2, Источники | **VERIFIED** (title «U-NIAH: Unified RAG and LLM Evaluation for Long Context Needle-In-A-Haystack», Gao et al.; направление и число точны) | arXiv:2503.00353 | STABLE (`[VFY yearly]` стоит, точное число в research, не в нарративе) | — |
| Barnett et al. — arXiv:2401.05856 «Seven Failure Points… RAG» | §2.4, Источники, Дальнейшее чтение | **VERIFIED** (точный title + авторы) | arXiv:2401.05856 | STABLE | — |
| GraphRAG — Microsoft, arXiv:2404.16130 (2024) | DDB2, Источники | **VERIFIED** (title «From Local to Global: A Graph RAG Approach…», Edge et al.) | arXiv:2404.16130 | STABLE | — |
| GraphRAG cost: ~десятки тыс.$ нач. 2024 → ~$ за книгу 32k слов к 2025 | DDB2 | **NEEDS-CITATION/UNVERIFIABLE** (числа — вторичный vendor-блог, в самой главе помечено `[FACT-CHECK]`) | Microsoft Azure AI Foundry blog 2025 (D11) | yearly | OK как есть (метка `[FACT-CHECK]` присутствует) — см. P2-2 |
| catastrophic forgetting — Luo et al. arXiv:2308.08747 (2023) | §3.3, Источники | **VERIFIED** (точный title «An Empirical Study of Catastrophic Forgetting in LLMs During Continual Fine-tuning») | arXiv:2308.08747 | STABLE | — |
| «тяжесть забывания растёт с масштабом модели» | §3.3, §3.2 | **VERIFIED с caveat** | Luo et al. 2023: верно, но строго «in such a model scale range» (1B–7B); глава хеджирует «как правило» | STABLE | См. P2-3 |
| Механизмы forgetting (gradient interference, representational drift…) — arXiv 2026-01 preprint | §3.3, Источники | **UNVERIFIABLE** (preprint без ID в нарративе; глава подаёт как «исследования показывают», `[FACT-CHECK]` стоит) | research sources.md B4 (arXiv 2026-01) | preprint / VERIFY-ON-DAY | OK (метка корректна, ID не вынесен в нарратив — правильно) |
| ReAct — Yao et al. arXiv:2210.03629 (2022, ICLR 2023) | §4.3, DDB4, Источники | **VERIFIED** (точный title + авторы + ICLR 2023 camera-ready) | arXiv:2210.03629 | STABLE | — |
| ReAct прирост +34% ALFWorld / +10% WebShop | (research; в нарративе — «заметный прирост на ALFWorld/WebShop») | **VERIFIED** (направление; точные % только в research, в главе обобщено — корректно) | B1 / Google Research blog | STABLE | — |
| MCP открыт Anthropic **11/2024**; OpenAI **03/2025**; Google Gemini **04/2025**; Linux Foundation / Agentic AI Foundation | §4.2, Источники | **VERIFIED** (Wikipedia/Pento/Anthropic; Hassabis подтвердил Gemini апр-2025; AAIF под Linux Foundation) | D5/D6/A13 | QUARTERLY (`[VFY]` стоит) | — |
| Single agent ~**4×** токенов чата; multi-agent ~**15×** | §4.4, §4.5, DDB4, Источники | **VERIFIED дословно** (Anthropic «How we built our multi-agent research system», 2025-06-13) | anthropic.com/engineering/multi-agent-research-system | STABLE (`[VFY quarterly]` стоит) | — |
| Anthropic Multi-Agent (2025-06-13) — контрапункт; «coding меньше параллелизуемо чем research» | §4.4, DDB4 | **VERIFIED** (точная атрибуция и тезис) | Anthropic 2025-06-13 | STABLE | — |
| Cognition «Don't Build Multi-Agents» — Walden Yan, **2025-06-12**; цитаты принципов | §4.4, §4.5, DDB4, Источники | **VERIFIED**; «Actions carry implicit decisions, and conflicting decisions carry bad results» — **дословно**; «Share context… not just individual messages» — корректный truncated quote (оригинал «Share context, and share full agent traces, not just individual messages») | cognition.ai/blog/dont-build-multi-agents | STABLE | — |
| reliability compounding 5×99%→≈95%, 10→≈90%, 20→≈82% | §4.5, §5.x, DDB5 | **VERIFIED (арифметика)**: 0.99⁵=0.9510, 0.99¹⁰=0.9044, 0.99²⁰=0.8179 — округления верны | MindStudio 2025-26 (D3) | STABLE | — |
| Агент сжёг **$4,200 за 63 ч** в петле; ~$1000 к 12 ч | §4.5, DDB4 | **UNVERIFIABLE / single-source** (postmortem Sattyam Jain 2026-04, single-author) — в главе помечено `[FACT-CHECK ... illustrative]`, числа округлены, подано как иллюстрация | medium.com Sattyam Jain 2026-04-14 (C5) | recent single source / VERIFY-ON-DAY | OK (метка и framing корректны) |
| GitHub MCP data heist (**май 2025**); приватные репо → публичный PR; over-privileged PAT + недоверенный issue | §4.7, DDB4 | **VERIFIED** (Invariant Labs, disclosed 2025-05-26; salary/financial data; root cause = arch issue + broad PAT; mitigation least-privilege) | Docker 2025; Invariant Labs 2025-05; AuthZed | STABLE | — |
| CVE-2025-6514 (mcp-remote, OS command injection RCE) **июль 2025**; сотни тыс. загрузок | DDB4 (хронология) | **VERIFIED** (JFrog, опубликовано 2025-07-09, CVSS 9.6, mcp-remote v0.0.5–0.1.15; 437k+ загрузок подтверждается источниками) | JFrog / SentinelOne / GHSA-6xpm-ggf7-wc3p | STABLE | — |
| CVE-2025-49596 (Anthropic MCP Inspector, неаутент. RCE) **июнь 2025** | DDB4 | **VERIFIED** (Oligo Security; disclosed апр-2025, fix v0.14.1 2025-06-13, CVSS 9.4; DNS-rebinding/localhost) | Oligo / Recorded Future / CVE DB | STABLE | — |
| Supabase/Cursor SQL-эксфильтрация (середина 2025); service_role + support-тикеты → integration_tokens | DDB4 | **VERIFIED / corroborated** (Simon Willison + General Analysis, 2025-07-06) — глава помечает `[FACT-CHECK corroborate]`, теперь подтверждено: июль 2025 | simonwillison.net 2025-07-06; generalanalysis.com | STABLE | См. P2-4 (метку можно снять) |
| WhatsApp MCP tool poisoning **апрель 2025**; выгрузка истории чатов | DDB4 (кейс #8) | **VERIFIED** (Invariant Labs, апр-2025; trivia-game server poisons whatsapp-mcp) | Docker / Invariant Labs 2025-04 | STABLE | — |
| Prompt injection / «модель доверяет убедительным токенам» / confused deputy — Simon Willison 2025 | §4.7, Источники | **VERIFIED** (точный перевод: «LLMs will trust anything that can send them convincing sounding tokens… confused deputy»; 2025-04-09) | simonwillison.net 2025-04-09 | STABLE | — |
| NYT v. OpenAI: суд **май 2025** обязал хранить ВСЕ логи ChatGPT (сотни млн польз.); удержание до **сент 2025**; **ноябрь 2025** — 20M логов | §4.6, Источники | **VERIFIED**: preservation order 2025-05-13; ~400M+ польз.; обязательство закончилось 2025-09-26 (stipulation, court doc 2025-10-09); Stein affirmed 20M в ноябре 2025 (NYT просил 120M) | Bloomberg Law 2025-11; NatLawReview 2025-11; court filings | STABLE (historical) | — |
| Anthropic ZDR покрывает Messages/Token-Counting, НЕ покрывает Files API / Batch / code-exec / MCP-коннектор / third-party; флаг → до 2 лет | §4.6, Источники | **VERIFIED** (live doc: ZDR не at-rest после ответа; Files API retained until deleted; MCP connector standard retention; third-party вне ZDR) | platform.claude.com/docs api-and-data-retention | **QUARTERLY — live doc** (`[VFY ... re-verify on day of lecture]` стоит) | См. verify-on-day |
| DPD (2024): чат-бот матерился / стих против компании | DDB4 (кейс #13) | VERIFIED (consistent с CIO/CX Today роста; известный кейс 2024) | CIO 2024-25 (C13) | STABLE | — |
| Chevrolet $1 Tahoe / NYC MyCity (март 2024) нелегальные советы | DDB4 (кейс #14), §5.2 | VERIFIED (известные кейсы 2024; NYC MyCity март 2024 — The Verge/AP) | CIO C13; The Verge C14 | STABLE | — |
| MIT NANDA «The GenAI Divide: State of AI in Business 2025» ~**95%** пилотов без P&L; методология **150 интервью + 350 опрос + 300 внедрений**; learning gap + интеграция; бюджеты sales/marketing vs back-office | §5.4, DDB5, Источники | **VERIFIED дословно** (Fortune 2025-08-18; отчёт MIT NANDA) — методология и каузальный вывод точны | fortune.com 2025-08-18; mlq.ai отчёт PDF | STABLE (`[FACT-CHECK — отчёт, не закон]` стоит, framing корректен) | — |
| METR (2025) — CoT информативен даже при низкой faithfulness | §1.3, DDB1, Источники | UNVERIFIABLE напрямую (не fetched отдельно), но подан как нюанс/«независимая оценка», не как опорное число | research A-ref | STABLE | OK (low-stakes hedge) |

---

## DISPUTED / FALSE facts

**Нет.** Ни одного P0. Ни одной фактической ошибки в числах, датах, атрибуциях. Ни одной выдуманной ссылки (все 8 проверенных arXiv-ID реальны и точны по title+авторам). Ни одной инверсии направления (Direction-of-Claim: «faithfulness падает на трудных задачах», «тяжесть forgetting растёт с масштабом», «RAG сильнее у меньших моделей», NANDA «95% без ROI» — все направления совпадают с источниками). Ни одного мисквота (все цитаты в кавычках — дословный перевод оригинала; truncated quote Cognition корректно помечен «…»).

---

## NEEDS-CITATION / NEEDS-LABEL (P1)

### P1-1 — GraphRAG cost-figures: метка есть, но в Источниках формулировка слабее, чем нужно
**Quote (DDB2):** «исторически индексация одного датасета стоила существенно (порядка десятков тысяч долларов в начале 2024), к 2025 Microsoft радикально снизила стоимость (ориентир — единицы долларов за книгу ~32k слов) `[FACT-CHECK: GraphRAG cost figures…]`».
**Issue:** В тексте §DDB2 метка `[FACT-CHECK]` стоит корректно. Но число «десятки тысяч долларов» — single secondary vendor-blog (Microsoft Azure AI Foundry, D11), не первоисточник цены; верхняя оценка не подтверждена независимо. Это не ошибка (метка присутствует), но это **volatile vendor-число на yearly cadence** — желательно в Источниках продублировать `[FACT-CHECK yearly]` рядом с GraphRAG-строкой (сейчас там стоит `[FACT-CHECK cost figures, yearly]` — фактически OK; формально P1 закрыт меткой). **Действие:** подтвердить, что book-editor сохранит метку при финализации; сам факт правки не требует — это hold/мониторинг.
**Severity:** P1 (граничный; метка уже стоит → ближе к P2, оставляю P1 для day-of awareness).

### P1-2 — Anthropic ZDR-границы: live-doc, QUARTERLY, обязателен day-of re-verify
**Quote (§4.6):** «ZDR покрывает основные Messages/Token-Counting, но не покрывает ряд фич — Files API, batch-обработку, контейнеры исполнения кода, MCP-коннектор… при флаге… данные могут храниться существенно дольше `[VFY: retention статус и границы ZDR, vendor live-doc… re-verify on day of lecture]`».
**Issue:** На 2026-05-16 проверено — соответствует live-doc Anthropic (ZDR не at-rest после ответа; Files API хранится до удаления; MCP-connector — стандартная retention; third-party вне ZDR). Метка `[VFY ... re-verify on day of lecture]` присутствует и корректна. **Это не ошибка**, но это **самый волатильный фактический блок главы** (vendor policy live-doc, cadence QUARTERLY). Конкретные числа («29 дней Batch», «до 30 дней code-exec», «до 2 лет при флаге», «Activity Feed 6 лет») в нарративе главы НЕ вынесены как опорные (они в research) — правильное решение book-editor. **Действие:** обязательная day-of верификация (см. список ниже). Фикс контента не требуется.
**Severity:** P1 (freshness, не factual).

---

## UNVERIFIABLE (источник недоступен / preprint / single-source — все корректно помечены в главе)

1. **arXiv 2026-01 preprint** (механизмы catastrophic forgetting) — §3.3. ID в research sources.md = `2601.18699` (будущая нумерация). В **нарративе главы ID НЕ приведён** — упомянуто как «препринт arXiv 2026-01… подавать как "исследования показывают"» + `[FACT-CHECK preprint; treat as illustrative]`. Это образцовое обращение с preprint: метка есть, ID не легитимизируется в тексте. **Действие не требуется.** (Замечание: ID-формат `2601.xxxxx` и `2603.xxxxx` в research-файле — будущие месяцы; они НЕ протекли в главу, поэтому P-уровень не присваивается главе. Отмечено для orchestrator: research-файл содержит future-dated arXiv-ID, которые НЕ должны попасть в нарратив при revision.)
2. **$4,200 / 63 ч agent loop** (Sattyam Jain 2026-04) — single-author postmortem. Глава: `[FACT-CHECK ... single-author, recent ... illustrative, числа округлены]` + явное «подаётся как иллюстративный». Корректно.
3. **METR 2025** (нюанс к faithfulness) — подан как «независимая оценка»/нюанс, не опорное число. Low-stakes. Корректно.
4. **DPD / Chevrolet / MyCity** — широко документированные кейсы 2024, источник CIO/The Verge roundup; точные детали (стих, $1) — из вторичного roundup, поданы нарративно. Приемлемо для иллюстративных кейсов.

---

## P2 (cite format / minor / hedge)

- **P2-1 — переведённые цитаты в кавычках.** Цитаты Anthropic/Willison/Cognition в кавычках — это **перевод на русский**, а не дословный английский. Семантически верны (проверено против оригинала), но строго по Citation Hygiene «кавычки = дословно» русский перевод английского оригинала — это де-факто точный парафраз. Рекомендация (не обязательна): для ключевых цитат (§1.1 «простейшее решение», §1.4 «наименьший набор…», §4.7 Willison) можно дать оригинал в скобках или сменить кавычки на атрибутированный парафраз. Не P1: смысл не искажён, источник назван, перевод верен.
- **P2-2 — GraphRAG cost** — см. P1-1; метка стоит, формально косметика.
- **P2-3 — «тяжесть forgetting растёт с масштабом» (§3.3/§3.2)** — Luo et al. ограничивают вывод диапазоном 1B–7B («in such a model scale range»). Глава хеджирует «как правило» и атрибутирует, но не приводит диапазон. Лёгкая overgeneralization под hedge. Рекомендация: при финализации можно добавить «(эмпирически на моделях 1B–7B)» как в research. Не P1 (hedge + атрибуция присутствуют, направление верно).
- **P2-4 — Supabase/Cursor `[FACT-CHECK corroborate]`** (DDB4) — теперь corroborated (Willison/General Analysis, 2025-07-06, «середина 2025» точна). Метку `corroborate` можно снять при финализации; её наличие — не ошибка.

---

## VERIFY-ON-DAY-OF-LECTURE (обязательный pre-flight лектора)

Cadence < 1 мес ИЛИ live-doc QUARTERLY с риском дрейфа. Главное правило: **числа этих классов в нарративе главы намеренно НЕ опорные** (book-editor вынес их в research + пометил `[VFY]`), поэтому дрейф не ломает аргумент — но проверить перед лекцией:

1. **Anthropic ZDR / data-retention границы** (§4.6) — live-doc `platform.claude.com/docs/.../api-and-data-retention`. Cadence QUARTERLY. Re-fetch в день лекции: покрытие Files/Batch/code-exec/MCP-connector/third-party, срок «до 2 лет при флаге», Activity Feed. **Высший приоритет** — единственный live-doc, формирующий смысловой блок безопасности.
2. **OpenAI retention / NYT-litigation статус** (§4.6) — статус litigation hold эволюционирует (preservation закончился 26.09.2025; 20M логов — ноябрь 2025). Re-check на новые постановления к дате лекции.
3. **MCP-экосистема: adoption / Linux Foundation / масштаб** (§4.2) — `[VFY quarterly]`. Точные числа (загрузки/реестр серверов) в нарратив НЕ вынесены (только research) — проверять при апдейте research, не критично для главы.
4. **CoT faithfulness 25/39%** (§1.3) — `[VFY quarterly]`. Стабильно (paper апр-2025), но если выйдет новая Anthropic-итерация по faithfulness к дате лекции — обновить. Низкий риск.
5. **MCP CVE / breach timeline** (DDB4) — AuthZed running timeline. Re-pull на новые инциденты к дате лекции (для актуальности «это не теоретическая поверхность»).
6. **Multi-agent ~4×/~15× токенов** (§4.4) — `[VFY quarterly]`, paper 2025-06-13, стабильно; re-confirm если Anthropic опубликует обновление. Низкий риск.

---

## Топ-итог (для book-editor / orchestrator)

**Must-fix P0:** нет.

**Should-address (P1, не блокирует show, hold-уровень):**
1. P1-2 — обеспечить day-of re-verify Anthropic ZDR live-doc (метка уже в тексте — сохранить при revision; добавить в pre-flight лектора).
2. P1-1 — сохранить `[FACT-CHECK]` на GraphRAG-cost при финализации (volatile vendor-число).

**Nice-to-have (P2, polish при финализации, не обязательно):**
- Для 3–4 ключевых переведённых цитат дать английский оригинал в скобках ИЛИ переоформить как атрибутированный парафраз (P2-1).
- §3.3: добавить диапазон «1B–7B» к утверждению о масштабе forgetting (P2-3).
- Снять `corroborate` в `[FACT-CHECK]` Supabase/Cursor — corroborated (P2-4).

**Замечание orchestrator'у (вне главы):** `notes/research/lecture-3/sources.md` содержит future-dated arXiv-ID (`2601.18699`, `2603.22489`, `2601.06007`) для recent preprints. Они корректно НЕ протекли в нарратив главы (упомянуты как «препринт 2026-01» без ID + `[FACT-CHECK]`). При любых revision-проходах эти ID НЕ должны попасть в текст как легитимные citations — они непроверяемы (формат будущих месяцев).

**Общая оценка:** глава фактологически чистая. 8/8 проверенных arXiv-ID точны, 13/13 критичных утверждений verified, все дословные цитаты соответствуют оригиналу, направления всех трендовых claim'ов совпадают с источниками, метки `[FACT-CHECK]`/`[VFY]` расставлены дисциплинированно и адекватно классу источника. Волатильные числа сознательно вынесены из смыслового слоя в research. Это качество выше типичного draft v1. **VERDICT: APPROVE-WITH-POLISH** (0 P0, 2 P1 freshness/label, ≤4 P2 — show-able с известными caveats, не структурный gap).
