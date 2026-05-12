# Fact-Checker Report — Лекция 1 v4 Plan — 2026-05-12

**Issue:** #67 (64.B Phase 1).
**Источник:** агент `fact-checker`. Сохранено orchestrator'ом.

## Severity counts
- **P0 (false fact / broken citation / misleading attribution):** 6
- **P1 (missing source / suspicious / methodology caveat):** 8
- **P2 (cite format / minor):** 5

## P0 — FALSE / MISLEADING (требуют немедленного фикса)

### P0-1 — s4 + s14 «Доли LLM-рынка РФ»: 108% и wrong attribution
- Сумма = **108%** (DeepSeek 43% + ChatGPT 27% + YandexGPT 23% + GigaChat 15%) — невозможно для market share.
- DeepSeek 43% = **доля Russia в global downloads DeepSeek** (Microsoft 2026), НЕ РФ market share.
- ВЦИОМ (окт 2025, n=1600) multi-select: ChatGPT 27%, YandexGPT 23%, **DeepSeek 20%**, GigaChat 15%, Шедеврум 11%.
- **Fix:** методология (multi-select, n, период) + правильная атрибуция. Убрать «43% DeepSeek» или вынести как «Russia 43% всех загрузок DeepSeek глобально».

### P0-2 — s9 «92% разработчиков США используют AI ежедневно (Stack Overflow 2025)»
- Stack Overflow 2025 = **84% globally** используют/планируют + **51% professional daily**. «92% США daily» нет.
- **Fix:** «84% globally use/plan AI; 51% professional developers — daily. Trust в AI tools упал: 46% не доверяют точности (vs 31% в 2024).»

### P0-3 — s16 «5 уровней автономности (Chan et al. 2025)»
- arXiv:2506.12469 — авторы **Feng, McDonald, Zhang**, не Chan.
- Уровни не L0-L4 autonomy, а **5 ролей пользователя**: operator → collaborator → consultant → approver → observer.
- **Fix:** обновить attribution + content.

### P0-4 — s22 «GPT-4o sycophancy rollback (март 2025)»
- Фактически **апрель 2025** (update 25 апр, откат 29 апр).
- **Fix:** «GPT-4o sycophancy rollback (апрель 2025).»

### P0-5 — s10 «DeepSeek $5.6M = open-source модель уровня GPT-4»
- $5.576M — это **DeepSeek-V3**, не R1 (который шокировал рынок).
- Это **marginal GPU cost only**; full infra (SemiAnalysis) ~$1.3-1.6B.
- R1 — reasoning model уровня **o1**, не general GPT-4.
- **Fix:** «DeepSeek-V3 (декабрь 2024) — marginal $5.6M training run; full infra $1.3-1.6B. R1 (январь 2025) — reasoning model уровня o1. 27 янв 2025 Nvidia −$589B капитализации.»

### P0-6 — s5 «Gartner 2025: 80% инженерных проектов с AI-компонентой через 3 года»
- Конкретный Gartner-релиз с такой формулировкой **не найден**.
- Близкие: «80% engineering workforce upskill GenAI by 2027» (октябрь 2024) или «40% enterprise apps with task-specific AI agents by 2026» (август 2025).
- **Fix:** заменить на одну из верифицируемых формулировок.

## P1 — Missing source / methodology caveat

### P1-1 — s4 «ВЦИОМ 51%»
- 51% = **интернет-пользователей старше 18 раз в неделю+**, не «россиян в целом».
- **Fix:** «51% российских интернет-пользователей старше 18 пользуются AI раз в неделю+ (ВЦИОМ-Онлайн 13-15 дек 2025, n=3239)».

### P1-2 — s9+s14 «90% AI-пилотов откатываются (АНО Цифровая экономика 2025)»
- Цифра подтверждена через CNews/Vedomosti/Intellectual Analytics (март 2026), не АНО ЦЭ.
- **Fix:** заменить attribution или найти прямую ссылку АНО ЦЭ.

### P1-3 — s9 «ChatGPT 1B+ MAU»
- OpenAI публикует **WAU**, не MAU. Февраль 2026: 900M WAU.
- **Fix:** «~900M WAU (OpenAI Feb 2026)».

### P1-4 — s9 «GitHub Copilot 46% кода»
- 46% кода **пользователей Copilot**, не «всего мирового кода».
- **Fix:** «46% кода, написанного пользователями Copilot (Octoverse 2025); Java — 61%.»

### P1-5 — s17 «Google Translate 500M пользователей, 100 млрд слов/день»
- Цифры **2016 года**. Сейчас: 1B+ users monthly, 1T+ слов в месяц.
- **Fix:** обновить.

### P1-6 — s21 «3-15% hallucination rate в топ-LLM (Vectara 2024)»
- Реальный range Vectara HHEM: **<1% для Gemini/GPT-4** до **10-15% для reasoning models**.
- **Fix:** «От <1% (standard summarization Gemini 2.0 Flash) до 10-15% (reasoning models на reasoning bench). Зависит от задачи.»

### P1-7 — s21 «34.8% пользователей вводят чувствительные данные (CybSafe 2024)»
- Точная цифра: **~38%** (CybSafe «Oh Behave!» 2024-2025, n=7000).
- **Fix:** «~38%».

### P1-8 — s23 «ARC-AGI-2 человек 60%, AI 54% при $30, чистые LLM 0%»
- Average human 60% ✓; top refinement Gemini 3 Pro + Poetiq 54% @ $30 ✓; top commercial Opus 4.5 Thinking 37.6% @ $2.20.
- «Pure LLMs 0%» устарело — есть ненулевые проценты сейчас.
- **Fix:** «Лучшее refinement-решение ARC-AGI-2: 54% @ $30 (Gemini 3 Pro + Poetiq). Лучший commercial один-в-один: 37.6% @ $2.20.»

## P2 — Minor

### P2-1 — s7 «UDIO основан кем-то из 8 авторов Attention»
- UDIO **не от автора Attention** (David Ding, DeepMind). Реально 4 компании от 5 авторов: Cohere (Gomez), Character.AI (Shazeer), Adept+Essential AI (Vaswani — основал 2), Sakana (Jones).
- **Fix:** убрать UDIO.

### P2-2 — s7 «173K+ цитирований»
- Google Scholar динамически растёт. Май 2026: ~160-180k.
- **Fix:** «более 160K цитирований (Google Scholar май 2026)».

### P2-3 — s20 «EU AI Act штрафы 15M / 3%»
- Это нижний tier. Верхний: **35M / 7%** за prohibited practices.
- **Fix:** добавить full structure.

### P2-4 — s14 «Dam 2024 (verify)»
- arXiv:2406.16937 VERIFIED. Снять flag.

### P2-5 — s10 «MCP появится в 2026»
- MCP — Anthropic ноябрь 2024.
- **Fix:** «MCP — Anthropic, ноябрь 2024; де-факто стандарт в 2025-2026».

## Particular orchestrator-claims

| Claim | Verdict |
|---|---|
| ВЦИОМ 51% | VERIFIED with caveat (методология) |
| Bloomberg DeepSeek 43% | DISPUTED (это Russia в global downloads, не market share) |
| Gartner 80% engineering | NEEDS-CITATION / DISPUTED |
| $5.6M DeepSeek | MISLEADING (V3, marginal cost only) |
| 900M ChatGPT / 1B+ MAU | VERIFIED with caveat (WAU, не MAU) |
| Davos 2026 LeCun vs Altman | reality OK, удалён из v4 excessively |
| Samsung 2023 leak | VERIFIED |

## Верифицированные факты (использовать as-is)
- Vaswani 2017 arXiv:1706.03762 (8 авторов) ✓
- AlphaFold Nobel 2024 ✓
- Dartmouth 1956 / Lighthill 1973 / Deep Blue 1997 ✓
- ResNet 3.57% vs human 5.1% ImageNet ✓
- Samsung March 2023 ChatGPT 3 leaks ✓
- DeepSeek R1 MATH-500 97.3% ✓
- YOLOv8 Ultralytics Jan 2023 ✓
- Searle 1980 Chinese Room ✓
- Pearl 2018 *Book of Why* ✓
- Moravec 1988 paradox ✓
- Huang 2023 arXiv:2311.05232 ✓
- ReAct (Yao 2022, ICLR 2023) ✓
- Anthropic «Building Effective Agents» 2024 ✓
- Anthropic MCP Nov 2024 ✓
- Bommasani 2021 arXiv:2108.07258 ✓
- Russell & Norvig AIMA 4th ed. 2021 ✓

## Финальный вердикт

**Не блокирующая остановка**, но **chapter author MUST address все 6 P0** до релиза. P1 сильно повышают кредибильность для инженерной аудитории (которая будет fact-checking сама — публичная лекция).

**Особое замечание методологическое:** план v4 несколько раз представляет multi-select percentages как «market shares» (sum 100%). Это типичная ошибка популяризации; в инженерной аудитории её заметят. Disclaimers обязательны.
