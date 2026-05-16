# Phase 10 SYNTHESIS — speech v1 Лекции 3

**Дата:** 2026-05-16 · **Issue:** #87 · **Артефакт:** `speech.md` v1 (~5.5k произносимых слов).

## Сводный вердикт: **APPROVE-WITH-POLISH** (0 P0 у всех 3)

| Критик | Verdict | P0 | P1 | Ключевое |
|---|---|---|---|---|
| methodology-critic | APPROVE-WITH-POLISH | 0 | 1 | WPM все ≤95 (худший 94.7, не 92 — мета неточна); strict-in **43.7%** (≥35% PASS), 5 разделов; conversational ✓; ЦВ-арка ✓ |
| fact-checker | APPROVE-WITH-POLISH | 0 | 3 | **0 фактов сверх главы** (47 групп — все в chapter v1.1); book-first ✓; Air Canada/forgetting live-verified |
| consistency-checker | APPROVE-WITH-POLISH | 0 | 1 | 3 артефакта cornerstone-aligned; 0 orphan; 0 forbidden-англицизмов; «кейс» без drift |

build-deck/pipeline условие «critics APPROVE-WITH-POLISH/CLEAN, 0 P0» — выполнено. Все правки downstream в speech (chapter/slides — source-of-truth, НЕ трогать).

## Phase 11 fix-list (speech-writer, точечно)

**P1 (must-fix):**
1. **[consistency D1] speech L65 — восстановить дословный ЦВ.** Сейчас: «доступ к **большой языковой модели**»; chapter §0 / deck.yaml / s04 (×2) дословно: «доступ к **LLM**». ЦВ — cornerstone, читается «медленно» как якорь возвратов; на экране s04 «LLM», лектор говорит иначе → book-first: speech L65 → «…доступ к **LLM**. Какую архитектуру выбрать — и когда правильный ответ "не ИИ"?» дословно. (Если нужен устный гло сс — «доступ к LLM — большой языковой модели», как aside, НЕ замена канона.)
2. **[methodology P1-1] синхронизировать карту «точек возврата ЦВ».** frontmatter (L17) + pre-flight (L526) — без нумерации `s08/s12/s17/s22/s23`; тело — нумерация №1–№5 (s23=№5). Привести к единой нумерованной форме во всех 3 местах (включая s23 как №5).
3. **[fact-checker P1-1] s07 — добавить устную оговорку к 25%/39%.** Число верное (== глава), но произносится без хеджа, в отличие от s23 («иллюстративно») и s29 («заголовок отчёта»). Добавить 1 полуфразу симметрично (хедж есть в pre-flight, нужен и в произносимом тексте).

**P2 (polish, тот же проход):**
- [meth] s28 worked-example (8-звенная цепочка, 92–93 WPM) — разбить на 2–3 «глотка» с микропаузой; варьировать зачин «давайте» (11×); s23 «ноль-девяносто-девять в пятой» → «ноль целых девяносто девять сотых в пятой степени»; поправить мету «худший WPM 92» → факт (40–94.7).
- [consistency D3, опц.] s23 — добавить клаузу «к двенадцатому часу — около тысячи долларов, дальше быстрее» (зеркало chapter/s23 escalation). Низкий приоритет.

**Не артефактная правка (orchestrator, plan-hygiene):**
- [consistency D2] `plan-v2-final.md` §2.1/LO7 таблица: `s08/s12/s17/s22` (4) → `s08/s12/s17/s22/s23` (5) — chapter+speech уже корректны (5), устаревший только план. Оркестратор фиксит план напрямую (planning artifact).

**chapter/slides:** изменений НЕТ (source-of-truth корректен; всё downstream в speech).

**После speech-fix:** status draft→reviewed, v1→v1.1, changelog в speech.md. → Phase 11.5 pre-gate (mode=final, cross-artifact grep) → USER GATE C.
