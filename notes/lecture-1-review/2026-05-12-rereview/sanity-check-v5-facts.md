# Sanity Check v5 — Facts — 2026-05-12

**Issue:** #67 (64.B Phase 1 of EPIC #64).
**Артефакт:** `notes/lecture-1-review/final/new-plan-v5-final.md`.
**База сравнения:** `fact-checker.md` (v4) + `SYNTHESIS.md`.
**Источник:** агент `fact-checker` (Opus 4.7). Сохранено orchestrator'ом.

## Verdict

**APPROVE-WITH-MINOR-FIXES.** Все 6 P0 facts закрыты (1 с micro-formula nuance), 8/8 P1 закрыты (1 с минорным caveat), 0 новых факт-ошибок. План v5 готов к Phase 2 (chapter draft).

## P0 fact-fixes verify

| P0 | v4 issue | v5 fix | Verified |
|---|---|---|---|
| **P0-1** s4+s14 LLM доли 108% | Wrong attribution + sum impossible | ВЦИОМ октябрь 2025 multi-select (n=1600): ChatGPT 27/YandexGPT 23/DeepSeek 20/GigaChat 15/Шедеврум 11. DeepSeek 43% явно убран на slide; в notes как «Russia 43% global downloads». Disclaimer multi-select на слайде. Сумма 96%. | ✅ CLOSED |
| **P0-2** s9 «92% разработчиков США» | Cifra неверна | Stack Overflow Developer Survey 2025 (n=49k+, 177 стран): 84% используют/планируют, 51% professional daily, 46% не доверяют точности (vs 31% в 2024) | ✅ CLOSED |
| **P0-3** s16 Chan→Feng | Wrong attribution | Feng/McDonald/Zhang arXiv:2506.12469 + 5 ролей user: operator → collaborator → consultant → approver → observer | ⚠️ CLOSED with caveat — формулировка «не уровни автономности AI» overcorrects (paper IS «Levels of Autonomy»). Корректнее: «5 levels of autonomy characterised by user role». **Не блокер**, micro-fix для chapter |
| **P0-4** s22 sycophancy март→апр 2025 | Wrong date | «апрель 2025 (update 25 апр, откат 29 апр)» | ✅ CLOSED — verified |
| **P0-5** s10 DeepSeek $5.6M misleading | V3/R1 conflated, full infra missed | V3 (декабрь 2024) marginal $5.6M, full infra **$1.3-1.6B** (SemiAnalysis); R1 (январь 2025) reasoning уровня o1 (97.3% MATH-500 vs 96.4%); 27 янв 2025 Nvidia −$589B капитализации | ✅ CLOSED — все 4 факта verified |
| **P0-6** s5 Gartner 80% | Конкретный отчёт не найден | «Gartner (октябрь 2024): к 2027 году 80% инженерного workforce должно осваивать GenAI» | ✅ CLOSED — точно соответствует Gartner press release 3 октября 2024 |

**Итого P0:** 6/6 закрыты.

## P1 fact-fixes verify

| P1 | Status |
|---|---|
| ВЦИОМ 51% методология | ✅ verified (n=3239, 13-15 декабря 2025) |
| Attribution «90%» | ✅ Vedomosti / Intellectual Analytics март 2026 (n=50 крупнейших организаций — можно упомянуть в notes для credibility) |
| ChatGPT WAU vs MAU | ✅ «900M WAU» |
| Copilot 46% кода attribution | ✅ «46% кода **пользователей Copilot**, Java — 61%» |
| Google Translate 2026 figures | ✅ «1B+ users monthly, ~1T слов в месяц» (verified Google blog April 2026) |
| Hallucination range | ✅ «<1% (Gemini 2.0 Flash) до 10-15% (reasoning)» (verified Vectara HHEM) |
| CybSafe 38% | ⚠️ CLOSED with caveat — 38% verified для «share sensitive work info без employer's knowledge». Также 43% для «share sensitive data with shadow AI». Обе из той же серии CybSafe «Oh Behave!». В chapter можно дать обе |
| ARC-AGI обновление | ✅ «54% @ $30 Gemini 3 Pro + Poetiq» + «37.6% @ $2.20 Opus 4.5 Thinking» — оба verified на arcprize.org |

**Итого P1:** 8/8 закрыты.

## New facts in v5 (verified)

| Новая формулировка | Verdict |
|---|---|
| s5 «30-40% closed без эффекта; 7-10% in production» | ✅ verified Vedomosti / Intellectual Analytics |
| s9 Stack Overflow «n=49k+ из 177 стран» | ✅ verified |
| s10 «Bloomberg / Reuters $589B 27 янв 2025» | ✅ verified largest single-day market cap loss in history |
| s10 DeepSeek-R1 release январь 2025 | ✅ verified (release date 20 января 2025) |
| s17 Google Translate «20-летие 28 апр 2026» | ✅ verified Google blog announcement |
| s23 «Средний человек ≈ 60% ARC-AGI-2» | ✅ verified arcprize.org standard human baseline |

**Все новые факты — verified.** Никаких необоснованных утверждений добавлено.

## Issues remaining (не блокеры)

### P0-fix-residual (1)
- **P0-3 формулировка:** v5 говорит «5 ролей пользователя, **не уровни автономности AI**» — overcorrect. Paper IS «Levels of Autonomy for AI Agents». Корректно: «5 levels of autonomy, each defined by a different user role». Action для **chapter author + presentation-designer**: переформулировать на «5 levels of autonomy characterised by user role».

### P2-residual (3)
- **s4 multi-select disclaimer на slide** — сумма 96%, в chapter упомянуть, что фактически possible >100% (есть 3+ инструмента users) для академической чистоты.
- **s7 «160K+ цитирований Google Scholar май 2026»** — динамическая цифра. Chapter author пометить «(на момент написания)».
- **s10 точная дата V3 release** — 26 декабря 2024. На slide достаточно «декабрь 2024»; в chapter точная дата.

### Verified для chapter (cleanup)
- UDIO note корректный — UDIO от David Ding (DeepMind), не от 8 авторов Attention. Chapter author исключит UDIO из перечня.
- s20 EU AI Act fines note (15M / 3% + 35M / 7%) — корректный.
- s24 «Давос 2026 LeCun vs Altman» удалено — корректно.

## Summary

| Severity | v4 found | Fixed in v5 | Outstanding |
|---|---|---|---|
| P0 | 6 | **6** ✅ | 1 micro-formula tweak (P0-3) |
| P1 | 8 | **8** ✅ | 1 minor caveat (P1-7 CybSafe two figures) |
| P2 | 5 | 0 (по дизайну) | 3 для chapter cleanup |
| New introduced | — | 0 ✅ | 0 |

**План v5 готов к Phase 2 (chapter draft).** Не блокеры:
1. book-editor должен переформулировать s16 Levels of Autonomy.
2. P2-residual (UDIO, цитирования, V3 date, EU AI Act fines) — учесть в chapter inline.

## Recommendation orchestrator'у

✅ **APPROVE v5 для USER GATE 0**. План factually robust для chapter draft.
