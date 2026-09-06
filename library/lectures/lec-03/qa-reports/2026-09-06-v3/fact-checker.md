# Fact-Checker Report — Глава 3 v3.0 (chapter.md + part2..5) — 2026-09-06

VERDICT: REVISE

Scope: полный citation-sweep по всей главе (5 частей, ~39 400 слов, 64 источника). Весь контент v3 — новый или обновлённый. Live-верификация через WebSearch/WebFetch: **17 claims** проверено на реальных источниках (список в конце).

## Severity counts
- **P0 (false fact / broken citation / wrong attribution):** 1
- **P1 (missing/weak source / suspicious number / wrong denominator):** 3
- **P2 (cite-format / ID mismatch / minor):** 5

Итог: 1 P0 → REVISE минимум. P0 — неверная атрибуция бенчмарка к measurable claim, повторённая в 3 местах главы.

---

## Verified facts (live через WebSearch/WebFetch) — 17 total

- ✓ **Air Canada / Moffatt** — трибунал BC, 14.02.2024, взыскано **$812,02** («разница» между bereavement- и full-fare). Chapter §4.10 указывает $812,02 верно; введение/§2.5 говорят «компенсировать разницу» — согласовано, инверсии нет. (BC CRT / McCarthy Tétrault / ABA)
- ✓ **NoLiMa** — arXiv:2502.05167, ICML 2025, 12 моделей ≥128K, effective length деградирует, «сходство ≠ релевантность». Цифры (короткий 87–99% → 45–82% на 32K) согласованы с research-таблицей.
- ✓ **CoT faithfulness** — Anthropic *Reasoning Models Don't Always Say What They Think* (апр 2025, arXiv:2505.05410): Claude 3.7 Sonnet **25%**, DeepSeek R1 **39%**; faithfulness падает на GPQA vs MMLU. Exact match.
- ✓ **Contextual Retrieval** — Anthropic 2024: промахи top-20 **5,7% → 1,9% (−67%)**; поэтапно 5,7→3,7→2,9→1,9. Reranking-шаг 2,9→1,9 (Deep-dive box 2) — верно.
- ✓ **EchoLeak / CVE-2025-32711** — первый zero-click IPI в проде (M365 Copilot), arXiv:2509.10540, раскрытие июнь 2025. ~40 сек эксфильтрация — согласовано.
- ✓ **OLG Hamm** — 12 мая 2026, медкомпания ответственна за ошибочные ответы своего чатбота о квалификации врачей. Exact match (Library of Congress, 2026-06-09).
- ✓ **ReAct** — arXiv:2210.03629, Yao et al., ICLR 2023. Верно.
- ✓ **Mata v. Avianca** — санкция **$5000**, шесть выдуманных дел, 2023 (SDNY). Exact match.
- ✓ **Slopsquatting** — 576 000 сэмплов, 16 моделей, **19,7%** галлюцинированных пакетов, 205 474 уникальных (Spracklen et al., USENIX Security 2025). Exact match.
- ✓ **Instruction hierarchy GPT-4o 63,8%** — Geng et al. 2025, конфликты форматирования, при явном акценте. Exact match.
- ✓ **IH-Challenge 84,1% → 94,1% (+10,0 п.п.)** — arXiv:2603.10521, GPT-5-Mini, 16 бенчмарков; небезопасное 6,6%→0,7%. Exact match.
- ✓ **Hinton, Vinyals, Dean, Distilling the Knowledge** — arXiv:1503.02531, 2015. Верно; дистилляция как самостоятельная техника — корректно.
- ✓ **Cyera** — 7 246 инцидентов (сен 2023–май 2026), 188 autonomous-damage, 65 code-deletion. Raw-числа верны (но см. P1-1 про denominator).
- ✓ **JMIR Cancer** — 6% (кураторская база) vs 35% (веб-поиск) галлюцинаций (cancer.jmir.org/2025/1/e70176). Числа реальны (но см. P2-3 про смешение условий GPT-3.5/GPT-4).
- ✓ **ChatInject** — arXiv:2509.22830, ICLR 2026 (см. P0 — benchmark-атрибуция неверна).
- ✓ **PocketOS** — 24–25 апр 2026, Cursor/Claude Opus 4.6, том+бэкапы удалены за 9 сек (Zenity/Euronews). Согласовано.
- ✓ **Contextual Retrieval staged breakdown** — подтверждён independent (35%/49%/67%).

---

## P0 — DISPUTED / FALSE (blocking)

### P0-1. ChatInject: неверная атрибуция ASR-числа к бенчмарку (3 локации)

**Quote (chapter.md:200, §1.2 s05c):** «средний attack success rate на бенчмарке **InjecAgent** вырос с **5,18% до 32,05%** (примерно шестикратно), а на Llama-4 — с **50,1% до 88,3%**».
Также: **chapter-part4.md:76** (§4.8 s25) — идентичная формулировка «на бенчмарке InjecAgent с 5,18% до 32,05%»; **chapter-part5.md:309** (Sources) — «5,18% → 32,05% (InjecAgent)».

**Claimed source:** arXiv:2509.22830 (ChatInject, ICLR 2026).

**Issue:** Проверено прямым fetch abstract + HTML статьи. Реальная attribution:
- **AgentDojo:** средний ASR **5,18% → 32,05%**.
- **InjecAgent:** средний ASR **15,13% → 45,90%** (multi-turn 52,33%).
- **Llama-4:** 50,1% → 88,3% — это на **InjecAgent**.

Chapter (вслед за research-файлами `rag-prompting-2026.md` §3.3 и `agents-mcp-2026.md` §3.3, где бенчмарки уже перепутаны) приписал число 5,18→32,05 бенчмарку **InjecAgent**, тогда как оно принадлежит **AgentDojo**. Более того, в §1.2 и §4.8 «средний 5,18→32,05» (AgentDojo) склеен в одном предложении с «Llama-4 50,1→88,3» (InjecAgent) — два разных бенчмарка поданы как один. Это wrong-attribution measurable claim (P0 по definition: неверная атрибуция цифры).

**Correct version (suggested):** «средний ASR на **AgentDojo** вырос с 5,18% до 32,05%, на **InjecAgent** — с 15,13% до 45,90% (multi-turn 52,33%); на Llama-4 (InjecAgent) — с 50,1% до 88,3%». Либо, если нужен один якорь: «на InjecAgent средний ASR 15,13%→45,90%, до 88,3% на Llama-4». Исправить все 3 локации + обе research-заметки (источник ошибки). Оригинальный тезис («кратный рост, prompt-based защиты неэффективны») остаётся верным — правится только benchmark-label.

**Severity:** P0 (wrong attribution of measurable claim, повторено ×3 + В7 «вплоть до 88,3%»).

---

## P1 — missing source / suspicious number / wrong denominator

### P1-1. Cyera «2,6% всех инцидентов» — неверный знаменатель
**Quote (part4:117):** «из **7 246** … в **188** … База: 188 из 7 246 = **2,6%** всех инцидентов».
**Issue:** Источник (cyera.com) framing: из 7 246 публичных инцидентов **verified-relevant to enterprise — 344**, и уже из этих 344 в 188 автономная система нанесла ущерб. То есть 188 — доля от 344 enterprise-relevant, а не от всех 7 246. «188 из 7 246 = 2,6% всех инцидентов» — математически считается, но подаёт wrong denominator (188 не скринились против всех 7 246). Raw-числа (7 246 / 188 / 65) — верны.
**Recommendation:** Либо убрать «2,6% всех инцидентов», либо переформулировать: «188 из 344 enterprise-relevant инцидентов (≈55%); 344 отобраны из 7 246 публичных». Флаг `[VFY-day-of]` уже стоит.
**Severity:** P1 (baseline/denominator — правило курса «measurable claim → корректная база»).

### P1-2. «RAG ~1250× дешевле за запрос» — single blog-источник, помечен, но экстраординарен
**Quote (chapter.md:395, §2.3):** «RAG обходится примерно **в 1250× дешевле за запрос**» (usewire, 2026; arXiv:2501.01880).
**Issue:** Цифра 1250× — из блог-поста usewire (не из arXiv:2501.01880, который про long-context vs RAG в целом). Экстраординарная величина (×1250) опирается на один вторичный источник; помечена `[VFY-day-of]`. arXiv:2501.01880 подтверждает направление (RAG дешевле/выигрывает при низкой relevance), но конкретную кратность 1250× я в нём live не подтвердил.
**Recommendation:** Оставить с флагом, но подать как «по одному отраслевому замеру (usewire, 2026) — порядка 1000× дешевле», не как установленный факт; либо развести источник цифры (usewire) от arXiv (направление). Не блокер — направление верно, помечено волатильным.
**Severity:** P1 (suspicious magnitude, single secondary source).

### P1-3. Ряд future-dated arXiv ID (2026) не верифицируемы live — по design, но требуют day-of recheck
**Quote:** arXiv:2510.05381, 2605.27123, 2605.05242, 2605.29420, 2602.11988, 2605.29463, 2604.09443, 2603.10521 (часть — 2026-датированные).
**Issue:** 2603.10521 (IH-Challenge) и 2502.05167 (NoLiMa) live подтверждены. Остальные 2026-ID (2510.05381 «Context Length Alone Hurts…» — подтверждён в поиске; 2605.27123 / 2605.05242 / 2605.29420 / 2602.11988 / 2605.29463) — существование заголовков правдоподобно, но не все подтверждены прямым fetch в этой сессии. Presence paradox (Gloaguen, 2602.11988) и Honest Lying (2605.29463) — вторичной верификации не получил.
**Recommendation:** Orchestrator: day-of recheck 2602.11988 (presence paradox), 2605.29463 (Honest Lying), 2605.27123, 2605.05242 — это несущие claims §4.7/§2.2. Не P0, т.к. заголовки согласованы с research-файлами и помечены свежими.
**Severity:** P1 (unverifiable-in-session, несущие claims).

---

## P2 — cite-format / ID mismatch / minor

### P2-1. arXiv:2604.09443 conflated с «OpenAI, The Instruction Hierarchy, 2024»
**Quote (chapter.md:194):** «(… OpenAI, «The Instruction Hierarchy», 2024; arXiv:2604.09443)».
**Issue:** 63,8% — из **Geng et al. (2025)**, surveyed в arXiv:2604.09443 («Many-Tier Instruction Hierarchy in LLM Agents», 2026). Оригинальная OpenAI-работа Wallace et al. «The Instruction Hierarchy» (2024) — это arXiv:2406.13208, НЕ 2604.09443. В одной скобке склеены две разные работы (OpenAI 2024-origin и survey 2026, содержащий Geng-цифру).
**Recommendation:** Развести: «Geng et al. (2025), в обзоре arXiv:2604.09443» для 63,8%; отдельно «OpenAI/Wallace et al. 2024 (arXiv:2406.13208)» для origin-иерархии.
**Severity:** P2.

### P2-2. ChatInject — неверное название в Sources
**Quote (part5:309):** «ChatInject: *Faking Role Tags in Tool Outputs*».
**Issue:** Реальное название — «*Abusing Chat Templates for Prompt Injection in LLM Agents*» (arXiv:2509.22830). «Faking Role Tags…» — вольный парафраз, не title.
**Recommendation:** Заменить на официальный title.
**Severity:** P2.

### P2-3. JMIR 6% vs 35% — смешение условий (GPT-3.5 / GPT-4 / covered-not-covered)
**Quote (part1:418, §2.4):** «6% галлюцинаций на кураторской … и 35% — по общему веб-поиску».
**Issue:** В источнике 35% — это GPT-3.5 на вопросах, НЕ покрытых кураторской базой, через Google-retrieval; 6% — GPT-3.5 на CIS-базе. Пара 6%↔35% валидна (обе GPT-3.5), но 35% специфичен для «uncovered questions», а не общий «веб-поиск vs курируемый». Направление и урок («данные важнее архитектуры», Δ~29 п.п.) — верны. Помечено `[VFY-day-of]`.
**Recommendation:** Уточнить: «6% (кураторская) vs до 35% (веб-retrieval на вопросах вне базы)» — чтобы не читалось как контролируемый A/B при прочих равных.
**Severity:** P2 (упрощение, не инверсия).

### P2-4. STI arXiv:2603.12277 — существование не подтверждено прямым fetch
**Quote (chapter.md:200):** «(Sentry Security, 2026; arXiv:2603.12277; HiddenLayer, 2025)».
**Issue:** arXiv:2603.12277 «Prompt Injection as Role Confusion» появляется в поиске (html/2603.12277v2 в выдаче ChatInject-related), но прямой fetch title/content я не делал. Transfer-dossier помечает его как «подтверждён на 2026-09-05». Вероятно валиден.
**Recommendation:** Day-of подтвердить title/авторов 2603.12277.
**Severity:** P2.

### P2-5. Air Canada сумма отсутствует во введении и §2.5, появляется только в §4.10
**Quote:** Введение и §2.5 — «компенсировать разницу», без суммы; §4.10 — «$812,02».
**Issue:** Не ошибка, но $812,02 (конкретика) даётся поздно, тогда как кейс — сквозной якорь введения. Consistency/полнота, не факт.
**Recommendation:** Опционально добавить «(разница $812,02)» в §2.5 при первом полном разборе. Не обязательно.
**Severity:** P2 (полнота, не факт).

---

## NEEDS-CITATION / волатильное (проверено на пометки, замечаний нет)

Корректно помечены `[VFY-day-of]` / `[FACT-CHECK]` (не требуют правки, только day-of recheck): coding-агенты Claude Code ~39% (с 18%), Copilot ~21%, Cursor 5M; SWE-bench Verified 75–80% vs Pro 23%; MCP-реестры 9,6k/20k/56k/90k, ~10k запускаемых; 30+ CVE / path traversal 82% / command injection 43%; postmark-mcp 1 643 загрузки; каскад 61%/73 инцидента; runaway $48k/14ч, $47k/11дн, $1,3M/603 млрд токенов; prompt-caching цены; MCP-спека 2026-07-28; MIT NANDA ~95%; $4,200-петля (single-author, помечен illustrative); catastrophic-forgetting механизмы (preprint, помечен illustrative); GraphRAG cost (помечен FACT-CHECK); LoRA 98,4% из 20 834 (помечен, с обязательным denominator-caveat — сделано корректно); 70/30 RAG-vs-FT (помечен «экспертная оценка вендора» — сделано корректно, правило соблюдено).

Отдельно: **OpenHands / «OpenClaw»** (§4.9) — honest-flagged как рабочая гипотеза, требует подтверждения владельца. Корректная обработка, не P-issue.

## UNVERIFIABLE (в сессии не подтверждено, требуют orchestrator/day-of live check)
- arXiv:2602.11988 (presence paradox), 2605.29463 (Honest Lying) — несущие §4.7; см. P1-3.
- agent-harness-registry (workain lab) числа Letta Tier D / Anthropic Memory Tool 17% — primary-источник (github реестр) в сессии не проверен; помечен `[VFY]` в тексте.
- usewire 1250× — см. P1-2.

---

## Топ-правок до публикации

1. **[P0]** Исправить benchmark-атрибуцию ChatInject в 3 местах (chapter.md:200, part4:76, part5:309) + В7 (part1:329) + обе research-заметки: 5,18→32,05 = **AgentDojo**, не InjecAgent; InjecAgent = 15,13→45,90; Llama-4 88,3 = на InjecAgent.
2. **[P1]** Cyera: убрать/переформулировать «2,6% всех инцидентов» (188 из 344 enterprise-relevant, не из 7 246).
3. **[P1]** «1250× дешевле» — развести источник (usewire blog ≠ arXiv:2501.01880), подать как один отраслевой замер.
4. **[P2]** Развести arXiv:2604.09443 (Geng-survey) и OpenAI Wallace 2024 (2406.13208) в цитировании 63,8%.
5. **[P2]** ChatInject title в Sources → «Abusing Chat Templates for Prompt Injection in LLM Agents».
6. **[P2]** JMIR: уточнить условия 6% vs 35% (uncovered-questions).
7. **[day-of]** Live recheck: 2602.11988, 2605.29463, 2603.12277, agent-harness-registry числа.

## Live-verification tally
**17 claims** проверено через WebSearch/WebFetch (12 exact-confirmed, 1 P0 разоблачён прямым fetch статьи ChatInject, 1 denominator-nuance найден у Cyera, 1 условие-nuance у JMIR, 2 подтверждены с оговоркой). Оставшиеся measurable claims — волатильные с корректными `[VFY-day-of]` пометками, требуют day-of recheck (не блокируют).
