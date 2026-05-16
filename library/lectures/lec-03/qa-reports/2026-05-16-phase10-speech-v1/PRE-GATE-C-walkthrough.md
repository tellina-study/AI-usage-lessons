# Pre-USER-GATE walkthrough — Лекция 3, mode=final (GATE C)

**Дата:** 2026-05-16 · **Артефакты:** chapter v1.1 finalized · deck v3.1 final · speech v1.1 reviewed · **Issue:** #87

## Summary
- Cross-artifact grep + cornerstone-alignment + pre-flight actionability проверены.
- **P0: 0 · P1: 0 · P2: 1**

## Cornerstone alignment (chapter ↔ slides ↔ speech) — PASS
- **Центральный вопрос — дословно идентичен** в 3 артефактах: chapter §0 == deck.yaml `central_question` == slide s04 == speech L65: «У меня есть задача и доступ к **LLM**. Какую архитектуру выбрать — и когда правильный ответ "не ИИ"?». D1 (Phase 10 P1) закрыт.
- **Точки возврата ЦВ:** 5, нумерованы, синхронны в 3 местах speech (frontmatter L17 / тело №1–№5 L143/187/279/349/359 / pre-flight L536); s23=№5. Совпадает с chapter (§1.5…§4.5) и plan (D2-fix). 
- **s07 faithfulness:** хедж добавлен устно (L127, симметричен s23/s29); числа 25%/39% неизменны, == глава/источник.
- **Лестница 6 ступеней / матрица / чек-лист 8 / «когда НЕ»** — единые формулировки/счёт во всех 3 (Phase 10 consistency-checker APPROVE-WITH-POLISH подтвердил).
- **Числа/даты/атрибуции** (Air Canada 14.02.2024 BC CRT; CoT 25/39%; $4,200/63ч; 5×99%→95%; NANDA ~95%; MCP 11/2024→03/2025→04/2025; NYT v.OpenAI май 2025) — идентичны chapter↔slide↔speech (Phase 10 fact-checker: 0 фактов сверх главы).

## Pre-flight actionability — PASS
- speech pre-flight: actionable; **0 orphan-ссылок** в произносимом теле и pre-flight (slide_covered L9 = 36 valid IDs == deck v3.1; pre-flight L536 — только валидные).
- **[VFY-day-of]** явные: s07 (CoT 25/39%), s20 (MCP adoption/принятие), s24 (retention/ZDR/NYT статус) — каждый actionable, cross-ref на существующий слайд.
- WPM: все фрагменты ≤95 (s07/s23 ровно 95.0 — на потолке, но compliant ≤95 HARD); s31 — реактивный Q&A-буфер (не таймируется, явная темп-нота).

## Чистые проверки
- 0 forbidden-англицизмов в speech; canonical-термины glossary дословно; «кейс» консистентен (book-first, без drift).
- chapter/slides — НЕ правились на Phase 9–11 (source-of-truth; все правки downstream в speech). book-first соблюдён.
- speech status=reviewed v1.1, Changelog v1→v1.1 присутствует.
- AI-Failure/Judgment holistic ≥30% в каждом артефакте: chapter ~58%, slides 12/36 strict-in, speech 43.7% мин — сохранён.

## P2 (НЕ блокер GATE C — фикс при финализации post-GATE-C)
1. `speech.md` L554 (Changelog v1→v1.1, editorial-нота про вариацию «давайте»): «s05a→«Посмотрим на числа» (s07)» — мислейбл `s05a` (несуществующий ID; имелся в виду s07). **Только в editorial-строке changelog** — НЕ в произносимом тексте, НЕ в pre-flight, НЕ лекторская, нулевое влияние на доставку. Исправить на «s07» при финализации speech (status reviewed→finalized).

## Recommendation
- [X] **PRESENT USER GATE C** (P0=0, P1=0; cross-artifact cornerstone aligned; pre-flight actionable, 0 orphan в deliverable; единственный P2 — editorial-typo в changelog, фикс при финализации, не блокирует).
