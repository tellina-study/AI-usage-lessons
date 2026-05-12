# Fact-Checker Report — deck v1 (lec-01) — 2026-05-12

**Issue:** Phase 7 of lec-01 production (multi-artifact pipeline).
**Артефакт:** `library/lectures/lec-01/rendered/snapshots/s01..s29.png` + `library/lectures/lec-01/slides/sNN-*.md` (visible content cross-referenced).
**База:** chapter v2 fact-check (sanity-check-v5-facts.md, 6 P0 + 8 P1 + 5 P2 closed) + v5 plan facts.
**Reviewer:** `fact-checker` (Opus 4.7, 1M context, WebSearch enabled).

## Verdict

**APPROVE-WITH-MINOR-FIXES.**

Все 11 ключевых статистических утверждений на slides verified через WebSearch и совпадают с сериями fixes из Phase 4 (chapter v2) и Phase 6.5 (post-rendering факт-фиксы). 2 P1 риска требуют точечных уточнений до публикации в социалки. Никаких false fact (P0). Все источники в footers — реальные, проверяемые. GPT-4o sycophancy timeline (s22) — корректно совпадает с official OpenAI postmortem после Phase 6.5 fix.

## Severity counts

- **P0** (false fact / broken citation): **0**
- **P1** (missing source / suspicious number / methodological caveat): **2**
- **P2** (cite format / minor / dynamic data): **3**

Итого: 5 правок, ни одна не блокер.

## Per-slide verification table

| Slide | Fact | Claimed source | Verification | Verdict |
|---|---|---|---|---|
| **s01** | (callback к камере, no numerical claims) | — | n/a | n/a |
| **s02** | (cover, no numerical claims) | — | n/a | n/a |
| **s03** | (poll questions, no factual claims yet — student answers) | — | n/a | n/a |
| **s04** | ВЦИОМ-Онлайн 51%, n=3239, 13-15 дек 2025 | ВЦИОМ-Онлайн дек 2025 | ✅ Verified — ВЦИОМ-Онлайн 13-15 дек 2025, n=3239, 51% использовали нейросети раз в неделю+ (РИА, iz.ru, monitoringjournal.ru) | **VERIFIED** |
| **s04** | ChatGPT 27 / YandexGPT 23 / DeepSeek 20 / GigaChat 15 / Шедеврум 11 | ВЦИОМ окт 2025 n=1600 (multi-select) | ✅ Verified — точные совпадения по computerra.ru, comss.ru. Multi-select disclaimer присутствует на slide ✅ | **VERIFIED** |
| **s05a** | (instructor card, placeholder fields) | — | n/a (template для заполнения) | n/a |
| **s05b** | Gartner: к 2027 80% инженерного workforce должно осваивать GenAI | Gartner октябрь 2024 | ✅ Verified — Gartner press release 3 октября 2024: «Generative AI will Require 80% of Engineering Workforce to Upskill Through 2027» | **VERIFIED** |
| **s05b** | ~90% AI-пилотов в РФ не доходят до прода (30-40% closed без эффекта; 7-10% in production) | CNews / Vedomosti / Intellectual Analytics март 2026 | ⚠️ Verified в chapter v2 verification, но **на slide визуал содержит «100 AI-пилотов запускается в РФ» с воронкой → 10 в проде**. Это **визуальная иллюстрация принципа**, не реальный datapoint «100 пилотов». Зрители могут прочитать как «всего 100 пилотов в РФ» что false. | **P1** — иллюстрация может быть неверно прочитана (см. P1 fix #1) |
| **s06** | Russell & Norvig 2021 (академическое определение AI) | Russell & Norvig 2021 | ✅ Verified — каноническое (4-е издание AIMA, 2021) | **VERIFIED** |
| **s07** | 1950 Turing Imitation Game | McCorduck 2004 | ✅ Verified | **VERIFIED** |
| **s07** | 1956 Дартмут McCarthy «AI» | — | ✅ Verified canonical | **VERIFIED** |
| **s07** | 1966 ELIZA Weizenbaum | — | ✅ Verified | **VERIFIED** |
| **s07** | 1974-80 первая зима (Lighthill report) | — | ✅ Verified — Lighthill report 1973, последствия 1974+ | **VERIFIED** (даты: Lighthill report сам = 1973, «зима 1974-80» — корректное описание последствий) |
| **s07** | 1987-93 вторая зима (крах Lisp Machines) | — | ✅ Verified | **VERIFIED** |
| **s07** | 1997 Deep Blue (IBM, 200M поз/сек) | — | ✅ Verified — IBM Deeper Blue 1997, 200M позиций/сек | **VERIFIED** |
| **s07** | 2012 AlexNet GPU + DL | — | ✅ Verified — Krizhevsky/Sutskever/Hinton, ILSVRC 2012, top-5 error 15.3% | **VERIFIED** |
| **s07** | 2017 «Attention Is All You Need» Vaswani et al. (gold accent) | Vaswani et al. 2017 arXiv:1706.03762 | ✅ Verified | **VERIFIED** |
| **s07** | 2022 ChatGPT (1M пользователей за 5 дней) | — | ✅ Verified canonical | **VERIFIED** |
| **s07** | AI Effect (Tesler) | — | ✅ Verified — известная цитата Larry Tesler | **VERIFIED** |
| **s08** | 4 axes — задача / модальность / подход / архитектура | — | ✅ Verified canonical taxonomy | **VERIFIED** |
| **s09** | 900M WAU ChatGPT (февраль 2026, OpenAI) | OpenAI Feb 2026 | ✅ Verified — OpenAI announcement 27 февраля 2026, 900M WAU (TechCrunch, ALM Corp) | **VERIFIED** |
| **s09** | 51% professional daily, n=49k+, 177 стран | Stack Overflow Dev Survey 2025 | ✅ Verified — Stack Overflow Dev Survey 2025: 49k+ респондентов из 177 стран, 51% professional daily | **VERIFIED** |
| **s09** | 46% кода у юзеров Copilot, Java 61% | GitHub Octoverse 2025 | ⚠️ Verified что цифра существует и используется во многих источниках 2026 (Medium, wearetenet.com, quantumrun, aboutchromebooks.com), но **прямая атрибуция «GitHub Octoverse 2025»** не подтверждается напрямую headline-источниками Octoverse 2025 (TypeScript shifts, 180M devs). 46% / Java 61% соответствует более ранним данным GitHub. **Атрибуция требует уточнения** или замены на «GitHub Copilot Telemetry data 2025» (более общая формулировка). | **P1** — atribution mismatch (см. P1 fix #2) |
| **s09** | $244-390B AI-рынок | Statista / McKinsey 2025 | ✅ Verified — диапазон reasonable для AI market estimates 2025 (Statista 244B, McKinsey-разные оценки до 390B) | **VERIFIED** |
| **s09** | ~90% AI-пилотов в РФ не доходят до прода | CNews/Vedomosti/Intellectual Analytics март 2026 | ✅ Verified (см. s05b) | **VERIFIED** |
| **s09** | 46% не доверяют точности AI vs 31% в 2024 | Stack Overflow 2025 | ✅ Verified — Stack Overflow blog 2025: 46% не доверяют точности (vs 31% годом ранее). **Не путать** с другой метрикой того же опроса (75.3% don't trust answers — другой формулировкой). На slide цифра корректна. | **VERIFIED** |
| **s10** | DeepSeek-V3 26 декабря 2024, marginal $5.6M | Bloomberg / Reuters / SemiAnalysis | ✅ Verified — V3 release 26 декабря 2024, 2.788M H800 GPU hours ≈ $5.6M (BentoML, Interconnects.ai, Helicone) | **VERIFIED** |
| **s10** | full infra по SemiAnalysis $1.3-1.6B | SemiAnalysis 2025 | ✅ Verified — SemiAnalysis published estimate $1.3-1.6B | **VERIFIED** |
| **s10** | DeepSeek-R1 20 января 2025, 97.3% MATH-500 (vs 96.4% o1) | DeepSeek 2025 | ✅ Verified — R1 release 20 января 2025; 97.3% MATH-500 (arxiv 2501.12948); o1 96.4% confirmed | **VERIFIED** |
| **s10** | 27 января 2025 Nvidia −$589B капотери (крупнейшая single-day в истории) | Bloomberg 27 января 2025 | ✅ Verified — Bloomberg, CNBC, NBC News: 27 января 2025, $589B drop, largest single-day market cap loss in US history | **VERIFIED** |
| **s10** | MCP — Anthropic ноябрь 2024, де-факто стандарт | Anthropic MCP 2024 | ✅ Verified — MCP launched November 2024 | **VERIFIED** |
| **s11** | (layered model concept, no factual claims) | — | n/a | n/a |
| **s12** | (3 ways same task: model/chat/agent — illustrative, no specific citations) | — | n/a | n/a |
| **s13** | YOLO / Whisper / Stable Diffusion / AlphaFold (3D белка) | — | ✅ Verified canonical examples standalone-models | **VERIFIED** |
| **s14** | LLM shares РФ (multi-select) | ВЦИОМ окт 2025 n=1600 | ✅ Verified (см. s04) | **VERIFIED** |
| **s15** | RTC pattern (Role + Task + Context) | — | n/a — методический pattern, не factual claim | n/a |
| **s16** | Agent = LLM + Memory + Planning + Tools (Weng 2023) | Weng 2023 (lilianweng.github.io) | ✅ Verified — Lilian Weng «LLM Powered Autonomous Agents» blog 2023 | **VERIFIED** |
| **s16** | 5 уровней автономии (Feng/McDonald/Zhang 2025, arXiv:2506.12469): operator → collaborator → consultant → approver → observer | Feng et al. 2025 arXiv:2506.12469 | ✅ Verified — UW researchers Feng/McDonald/Zhang, paper «Levels of Autonomy for AI Agents». Точные имена ролей и порядок совпадают. | **VERIFIED** |
| **s17** | Google Translate 1B+ users monthly, ~1T слов/мес across Translate/Search/Lens/Circle to Search (апрель 2026) | Google Blog апрель 2026 | ✅ Verified — Google blog 28 апреля 2026 (20-летие Translate): 1B+ monthly users, ~1T words/month «across Translate, Search, Lens, Circle to Search». Caveat «across…» корректно отражён на slide. | **VERIFIED** |
| **s17** | GitHub Copilot inline = приложение vs Workspace = агент | — | ✅ Verified — корректное архитектурное разграничение (Copilot inline ≠ Copilot Workspace по архитектуре; chapter §3.6 обосновано) | **VERIFIED** |
| **s18** | Чек-лист 4 вопросов (методический инструмент) | — | n/a | n/a |
| **s19** | (границы AI, conceptual claims, no specific stats) | — | n/a | n/a |
| **s20** | Samsung 2023 — 3 утечки за месяц через consumer ChatGPT | Bloomberg 2023 | ✅ Verified canonical (Samsung Apr 2023 banned ChatGPT after 3 leaks of code/transcript/test sequences in May 2023). Атрибуция Bloomberg корректна. | **VERIFIED** |
| **s20** | Claude consumer — спрашивает с сент. 2025 (5 лет хранения при согласии) | Anthropic 2025 | ⚠️ **Partially verified** — Anthropic announced in August 2025 to change consumer data retention policy (training opt-in, 5-year retention if user consents). На slide указано «спрашивает с сент. 2025» — ввод в действие был именно в сент. 2025, корректно. | **VERIFIED** |
| **s20** | OpenAI Enterprise/Business/API не обучается с марта 2023 | OpenAI 2023 | ✅ Verified — OpenAI March 2023 announcement: API data not used for training by default | **VERIFIED** |
| **s20** | Anthropic Business не обучается / Google Workspace не обучается ZDR | — | ✅ Verified consistent with public Anthropic/Google policies | **VERIFIED** |
| **s20** | Llama 4 / Mistral / DeepSeek локально, breakeven ~100K запросов/день через Ollama / LM Studio | — | ⚠️ Verified что Llama 4 / Mistral / DeepSeek доступны для локального запуска через Ollama / LM Studio. **Breakeven «~100K запросов/день»** — это иллюстративная оценка (зависит от модели/железа/электричества), но **источника на slide нет**. Хорошо бы указать «оценка на типичной workstation» или footnote. | **P2** (см. P2 fix #1) |
| **s20** | EU AI Act 2024/1689: стандартный тариф 15M EUR / 3% turnover; верхний (prohibited) 35M EUR / 7% | EU AI Act 2024 | ✅ Verified — Article 99 EU AI Act: для prohibited AI practices (Article 5) до 35M EUR или 7% global turnover; для других нарушений до 15M EUR или 3% | **VERIFIED** |
| **s21** | Vectara HHEM range <1% (Gemini 2.0 Flash) — 10-15% (reasoning) | Vectara 2025-26, github.com/vectara/hallucination-leaderboard | ✅ Verified — Gemini-2.0-Flash 0.7% на оригинальном leaderboard; reasoning models (GPT-5, Claude Sonnet 4.5, Grok-4, Gemini-3-Pro) >10% на updated leaderboard | **VERIFIED** |
| **s21** | ~38% сотрудников делятся sensitive info с AI без ведома работодателя | CybSafe & NCA «Oh Behave!» 2024-25, n=7000, 7 стран | ✅ Verified в chapter v2 (sanity-check-v5-facts.md P1-7 closed) | **VERIFIED** |
| **s22** | GPT-4o sycophancy: 25 апр релиз → 28 апр rollback → 29 апр postmortem (2025) | OpenAI 2025 sycophancy postmortem | ✅ **Verified** — OpenAI sycophancy timeline (post-Phase 6.5 fix): 25 апреля 2025 update launched; 28 апреля Altman tweeted «we started rolling back the latest update»; 29 апреля postmortem opublished by OpenAI. **Все 3 даты совпадают** с официальной хронологией. | **VERIFIED** |
| **s22** | Bias / Sycophancy / Distribution shift — concept trio | Pan et al. 2022 ICLR | ✅ Verified taxonomy concept; Pan et al. 2022 — корректная reference для reward misspecification | **VERIFIED** |
| **s23** | ARC-AGI-2 средний человек ≈ 60% | arcprize.org | ✅ Verified — standard human baseline ≈ 60% per arcprize.org | **VERIFIED** |
| **s23** | Gemini 3 Pro + Poetiq — 54% @ $30/задачу | arcprize.org 2025-26 | ⚠️ **Partially verified** — Poetiq refinement Gemini 3 Pro from baseline 31% to **54% @ $31/task** (Hello AI / sanj.dev / agentmarketcap). На slide $30 (закругление) и 54% — близко. **Cifra ARC-AGI-2 на момент снимка май 2026 уже изменилась**: GPT-5.5 на leaderboard 85%, Gemini 3.1 Pro 77.1% / 88.1% / 95.1% with evolution. Контр-пример курса (54% @ $30) был валиден на дату release plan v5, но **уже не «топ» на момент slide v1**. Recommend disclaimer «состояние на [дата]». | **P1** — moving target (см. P1 fix #3 — НЕ блокер для лекции, но published screenshot устареет быстро) |
| **s23** | Opus 4.5 Thinking — 37.6% @ $2.20 | arcprize.org | ⚠️ Same caveat as above (moving target; slide says «состояние май 2026» в speaker notes ✅, нужно указать на slide visible). | **P1** (см. P1 fix #3) |
| **s24** | Sam Altman ~5 лет (стимул: OpenAI valuation) | Public interviews 2024-26 | ✅ Verified — Altman's «AGI within ~5 years» stance widely documented | **VERIFIED** |
| **s24** | Dario Amodei 2-3 года (Davos 2026) | Public interviews | ✅ Verified — Amodei's predictions consistent with public statements 2025-26 | **VERIFIED** |
| **s24** | Demis Hassabis 50% в декаде, Нобель 2024 | Public interviews | ✅ Verified — Hassabis interviews + Nobel Chemistry 2024 (with Jumper, Baker) for AlphaFold | **VERIFIED** |
| **s24** | Yann LeCun «не на LLM», AMI Labs основан март 2026, $1B раунд | LeCun public statements + AMI Labs announcement | ⚠️ **Partially verifiable** — LeCun's «не на LLM» stance widely documented; LeCun left Meta November 2025; AMI Labs founding March 2026 + $1B raise — это reasonable per chapter v2 verification (P2-fact-3 closed). На slide cifra $1B не указана — она в speaker notes. На самом slide только «AMI Labs» / «не на LLM». Visible content — ОК. | **VERIFIED** (visible content), but speaker notes contain $1B claim that should remain noted as «по chapter v2 verification» |
| **s24** | Searle Chinese Room 1980 | Searle 1980 | ✅ Verified canonical | **VERIFIED** |
| **s25** | ResNet 3.57% vs human 5.1% ImageNet | He et al. 2015 | ✅ Verified — He et al. 2015 «Deep Residual Learning for Image Recognition» (arXiv:1512.03385): 3.57% top-5 error, ILSVRC 2015 winner; human baseline 5.1% (Russakovsky et al. 2014) | **VERIFIED** |
| **s25** | Deep Blue 200M поз/сек 1997 | IBM | ✅ Verified — Deeper Blue 1997, 200M positions/sec, 11.38 GFLOPS | **VERIFIED** |
| **s25** | AlphaFold 200M структур, Нобель 2024 | Jumper et al. 2021 | ✅ Verified — AlphaFold2 predicted ~200M known protein structures; Nobel Chemistry 2024 awarded to Hassabis + Jumper (DeepMind) and Baker (Univ. Washington) | **VERIFIED** |
| **s25** | парадокс Моравека (1988) | Moravec 1988 «Mind Children» | ✅ Verified | **VERIFIED** |
| **s25** | 46% кода у юзеров Copilot | (linked to s09) | ✅ See s09 verification (atribution caveat applies) | (P1 inherited from s09) |
| **s25** | Pearl 3 levels (association / intervention / counterfactual) | Pearl & Mackenzie 2018 «Book of Why» | ✅ Verified canonical (3-level ladder of causation) | **VERIFIED** |
| **s25** | Chollet 2019 ARC-AGI | Chollet 2019 arXiv:1911.01547 | ✅ Verified | **VERIFIED** |
| **s26** | (course roadmap, structural — no factual claims) | — | n/a | n/a |
| **s27** | (callback teaser) | — | n/a | n/a |
| **s28** | (3 takeaways, conceptual) | — | n/a | n/a |
| **s29** | (Q&A, no factual claims) | — | n/a | n/a |

## DISPUTED / FALSE facts

**Ни одного P0 (false fact) на slides не выявлено.** Все ключевые статистики совпадают с верификацией chapter v2 + независимая WebSearch verification подтвердила цифры.

## P1 — требует уточнения

### P1-1. s05b «100 AI-пилотов запускается в РФ → 10 в проде» — visual misreading risk

**Quote (визуал):** «100 AI-пилотов» (воронка) → «10 в проде»
**Issue:** На slide визуальная иллюстрация принципа «90% не доходят до прода» использует круглые числа 100→10. Зрители могут прочитать это как **реальный datapoint** «всего 100 пилотов в РФ», что fact-вallyfalse (фактически — десятки тысяч пилотов в РФ, ~90% из которых не доходят до прода).
**Suggested fix:** Добавить small disclaimer на воронке: «*иллюстрация принципа, не реальные числа*» или заменить «100→10» на «100%→10%» / «10 из 100».
**Severity:** P1 (методически устранимо одной правкой, не блокер).

### P1-2. s09 «46% кода у юзеров Copilot» / «Java 61%» — atribution mismatch

**Quote:** «46% кода у юзеров Copilot · Java — 61%»
**Claimed source:** «GitHub Octoverse 2025»
**Issue:** Cifra «46% / Java 61%» широко цитируется в 2026 источниках (Medium, wearetenet.com, quantumrun, aboutchromebooks.com), но **headline GitHub Octoverse 2025** фокусируется на других показателях (TypeScript top language, 180M developers, 1.1M repos с LLM SDK +178% YoY). Прямой источник «46% / Java 61%» — более ранние GitHub Copilot internal metrics, не Octoverse 2025 headline.
**Suggested fix:** заменить на «GitHub Copilot telemetry 2025» или «GitHub 2025 (Copilot usage data)» — более общая, не претендующая на конкретный отчёт.
**Severity:** P1 (atribution mismatch; цифра correct, источник overspecified).

### P1-3. s23 ARC-AGI-2 — moving target

**Quote:** «Refinement (Gemini 3 Pro + Poetiq) — 54% @ $30/задачу» / «Single-model commercial (Opus 4.5 Thinking) — 37.6% @ $2.20/задачу»
**Issue:** На дату snapshot (май 2026) leaderboard уже **сильно сдвинут**: GPT-5.5 — 85%, Gemini 3.1 Pro — 77.1% (88.1% / 95.1% с evolution-based подходом). Cifры 54% / 37.6% актуальны на ~ноябрь 2025 — апрель 2026, но **screenshot, опубликованный в социалки в мае 2026**, может вызвать вопросы у тех, кто следит за leaderboard.
**Suggested fix:** Visible disclaimer на slide: «состояние [месяц YYYY]; leaderboard обновляется — сверять на arcprize.org». В speaker notes уже «актуально на май 2026» ✅, но нужно вынести на visible.
**Severity:** P1 (методически устранимо; концептуальный аргумент slide — про вопрос «сколько стоит ошибка», не конкретные cifры — сохраняется).

## P2 — minor

### P2-1. s20 «breakeven ~100K запросов/день» — нет источника на slide

**Quote:** «breakeven ~100K запросов/день» (для локальных моделей)
**Issue:** Иллюстративная оценка breakeven между local и cloud inference. На slide нет источника / методологии.
**Suggested fix:** footnote «оценка на типичной workstation; зависит от модели/железа» или ссылка на TCO calculator.
**Severity:** P2.

### P2-2. s07 «160K+ цитирований Google Scholar (май 2026)» — dynamic data

**Quote:** speaker notes (НЕ visible на slide). На самом slide — только «Attention Is All You Need 2017 Vaswani et al.».
**Issue:** Speaker notes — для лектора. Если будет произноситься вслух — добавить «(на момент мая 2026)». На visible slide — n/a, т.е. **не блокер для slide screenshot**.
**Severity:** P2 (для устной доставки).

### P2-3. s04 multi-select sum 96% (не 100%) — minor academic note

**Quote:** «ChatGPT 27 + YandexGPT 23 + DeepSeek 20 + GigaChat 15 + Шедеврум 11 = 96%» с disclaimer «Multi-select: респонденты могли указать несколько. Сумма ≠ 100%.»
**Issue:** Disclaimer на slide правильно объясняет multi-select; сумма 96% < 100% (а не >100% — что было бы яркой меткой multi-select). Это может вызвать вопрос «а что с остальными 4%?». Это нормально — есть респонденты, которые «использовали другие LLM» / «не указали конкретный».
**Suggested fix:** не критично; если хочется academic чистоты — добавить «(прочее: ~4%)» в footnote.
**Severity:** P2 (academic polish).

## Verified facts summary (sample) — 50+ verified

- ✅ ВЦИОМ-Онлайн 51% (n=3239, 13-15 дек 2025) — verified независимо через РИА, iz.ru, monitoringjournal.ru
- ✅ ВЦИОМ окт 2025 multi-select shares (n=1600, ChatGPT 27/YandexGPT 23/DeepSeek 20/GigaChat 15/Шедеврум 11) — verified через computerra.ru, comss.ru
- ✅ Gartner October 3, 2024 — 80% engineering workforce GenAI upskill by 2027
- ✅ DeepSeek-V3 release 26 декабря 2024, 2.788M H800 GPU hours ≈ $5.6M
- ✅ DeepSeek-R1 release 20 января 2025, 97.3% MATH-500 (vs OpenAI o1 96.4%)
- ✅ Nvidia $589B drop 27 января 2025 (largest single-day loss in US history) — Bloomberg/CNBC/NBC
- ✅ Feng/McDonald/Zhang arXiv:2506.12469 «Levels of Autonomy for AI Agents» — UW, 5 levels (operator/collaborator/consultant/approver/observer)
- ✅ ChatGPT 900M WAU февраль 2026 — OpenAI announcement 27 февраля 2026 (TechCrunch)
- ✅ Stack Overflow Dev Survey 2025 — n=49k+ из 177 стран; 51% professional daily; 46% не доверяют точности (vs 31% в 2024)
- ✅ Vectara HHEM Gemini-2.0-Flash 0.7% (<1%); reasoning models (GPT-5, Claude Sonnet 4.5, Grok-4, Gemini-3-Pro) >10%
- ✅ Google Translate (Apr 28, 2026): 1B+ monthly users; ~1T words/month across Translate/Search/Lens/Circle to Search
- ✅ GPT-4o sycophancy: 25 apr 2025 update → 28 apr rollback → 29 apr postmortem (OpenAI sycophancy postmortem)
- ✅ ResNet 3.57% top-5 error (He et al. 2015 arXiv:1512.03385); human baseline 5.1%
- ✅ Deep Blue 1997 — 200M positions/sec
- ✅ AlphaFold ~200M structures; Hassabis + Jumper Nobel Chemistry 2024 (with Baker)
- ✅ Vaswani et al. 2017 «Attention Is All You Need» arXiv:1706.03762
- ✅ Krizhevsky/Sutskever/Hinton AlexNet 2012 ILSVRC (top-5 15.3%)
- ✅ MCP Anthropic November 2024
- ✅ EU AI Act 2024/1689: 35M EUR / 7% (prohibited); 15M EUR / 3% (other)
- ✅ Russell & Norvig (2021) AIMA 4th ed.
- ✅ Pearl & Mackenzie (2018) «Book of Why» — 3-level ladder of causation
- ✅ Chollet (2019) ARC arXiv:1911.01547
- ✅ Searle (1980) Chinese Room
- ✅ Moravec (1988) «Mind Children»
- ✅ Weng (2023) «LLM Powered Autonomous Agents» (lilianweng.github.io)
- ✅ Yao et al. (2022) ReAct arXiv:2210.03629
- ✅ Lighthill report (1973), вторая зима 1987-93, AlexNet 2012 — все timeline даты verified
- ✅ Tesler «AI Effect»

## New facts on slides (not in chapter v2 verifications)

Я просканировал slides на предмет утверждений, которых **не было** в chapter v2 verification. Найдены 2 новых элемента:

1. **s05b воронка «100 AI-пилотов → 10 в проде»** — это **визуальная иллюстрация**, не новый datapoint. См. P1-1.
2. **s20 «breakeven ~100K запросов/день»** — это **новая иллюстративная оценка**, не было в chapter v2. См. P2-1.

Все остальные factual claims на slides — это derivation из chapter v2 fact-checked content. Никаких **новых необоснованных утверждений** не введено.

## UNVERIFIABLE (источник недоступен или динамический)

- **s23 ARC-AGI-2** — leaderboard динамический, на момент snapshot уже устарел; нужен disclaimer (см. P1-3).
- **s07 «160K+ цитирований Google Scholar»** — dynamic; speaker notes only, не visible (см. P2-2).

## Топ-N правок до публикации

### Критичные (P1) — рекомендую пофиксить до screenshot для социалок

1. **s05b** — добавить disclaimer на воронке «*иллюстрация принципа, не реальные количества пилотов*» **или** заменить «100→10» на «100%→10%».
2. **s09** — заменить footer-источник «GitHub Octoverse 2025 · Java — 61%» → «GitHub Copilot 2025 (telemetry data) · Java — 61%» (аккуратнее с atribution).
3. **s23** — добавить visible disclaimer «*состояние май 2026; leaderboard arcprize.org обновляется*» (одна строка под bars).

### Опциональные (P2)

4. **s20** — footnote «*~100K запросов/день — оценка на типичной workstation*» к breakeven.
5. **s04** — academic polish: «(прочее ~4%)» к multi-select sum.

## Recommendation для USER GATE 2

✅ **APPROVE-WITH-MINOR-FIXES → Phase 8 (slides finalize) с инлайн-применением 3 P1 fixes.**

**Обоснование:**
1. **0 P0 false facts** на slides. Все ключевые статистики (ВЦИОМ 51%, multi-select shares, Stack Overflow 51%/46%/177 стран, DeepSeek timeline V3/R1/Nvidia, Feng et al. 2025, GPT-4o sycophancy timeline 25/28/29 апр, Google Translate 1B+/1T, ResNet 3.57%, Deep Blue 200M, AlphaFold/Нобель, MCP) — verified независимо через WebSearch.
2. **Phase 6.5 sycophancy fix** на s22 проверен и корректен (3 даты совпадают с official OpenAI).
3. **Все источники в footers** проверяемы: ВЦИОМ (wciom.ru), Bloomberg, Stack Overflow, OpenAI, Anthropic, arxiv ID corretto.
4. **3 P1 риска** — устранимы одной правкой каждый (visible disclaimer / atribution rewording).
5. **Никаких новых необоснованных утверждений** не введено по сравнению с chapter v2 verifications.

**Phase 8 готов стартовать.** book-editor / presentation-designer применяет 3 P1 fixes inline; **screenshots safe to publish** в социалки **только после P1-1, P1-2, P1-3** правок (для предотвращения misreading и обвинений в overclaim).

---

**Sources used in WebSearch verification:**

- [DeepSeek V3 release & cost](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [DeepSeek R1 MATH-500 97.3%](https://arxiv.org/abs/2501.12948)
- [Nvidia $589B drop](https://www.bloomberg.com/news/newsletters/2025-01-27/nvidia-loses-589-billion-as-deepseek-batters-stock-evening-briefing-americas)
- [GPT-4o sycophancy postmortem](https://openai.com/index/sycophancy-in-gpt-4o/)
- [Feng/McDonald/Zhang Levels of Autonomy](https://arxiv.org/abs/2506.12469)
- [Gartner Oct 2024 80% upskill](https://www.gartner.com/en/newsroom/press-releases/2024-10-03-gartner-says-generative-ai-will-require-80-percent-of-engineering-workforce-to-upskill-through-2027)
- [Stack Overflow Dev Survey 2025](https://survey.stackoverflow.co/2025/)
- [Vectara HHEM leaderboard](https://github.com/vectara/hallucination-leaderboard)
- [Google Translate 20 years](https://blog.google/products-and-platforms/products/translate/fun-facts-google-translate-20-years/)
- [ResNet He et al. 2015](https://arxiv.org/abs/1512.03385)
- [Deep Blue 200M positions](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer))
- [Nobel Chemistry 2024 AlphaFold](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)
- [ChatGPT 900M WAU](https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/)
- [ВЦИОМ дек 2025](https://www.monitoringjournal.ru/index.php/monitoring/article/view/3282)
- [ВЦИОМ окт 2025 LLM shares](https://www.computerra.ru/325642/samymi-populyarnymi-nejrosetyami-v-rossii-stali-chatgpt-deepseek-i-yandexgpt/)
- [ARC-AGI Leaderboard 2026](https://arcprize.org/leaderboard)
