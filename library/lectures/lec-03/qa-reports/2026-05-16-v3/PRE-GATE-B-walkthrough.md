# Pre-USER-GATE walkthrough — Лекция 3, mode=slides (GATE B)

**Дата:** 2026-05-16 · **Артефакт:** deck v3.1 (36 слайдов) · **Issue:** #87

## Summary
- Автопроверок: 8 · Passed: 8
- Визуальный sweep (vision, 5-сек тест): s04a, s13a, s13b, s23a, s25a, s30, s31, s14, s27 (новые/изменённые/watch) + выборка контентных.
- **P0: 0 · P1: 0 · P2: 1**

## Проверки (pass)
- designer-extras (Лектору/Вы здесь/тайминг/[пауза]) = **0**; forbidden англицизмы (пайплайн/фоллбэк/файнтюнинг/воркфлоу…) = **0**.
- speaker notes — все 36 в [150,300] слов (программная проверка).
- 36 slide-entries в deck.yaml+deck-part2.yaml; per-slide Σ duration ≈75.7 (≈75 с буфером s31; divider'ы ~0.3); 0 orphan-ссылок (только s07 — существует).
- U-6: s30 title «AI-архитектура — несущая ось отраслевых лекций» (контент, не функция) ✓; s13b/s14/s31 — контентные/канон; divider'ы — section_divider (норма канона).
- Визуал: 6 новых слайдов 5-сек PASS; divider-язык единый (s04a/s09/s13a/s18/s23a/s25a — teal eyebrow + gold line + giant цифра + roadmap-маркер); s23a (sub-div безопасности) отличим, но того же семейства; s13b schema PASS (веса≠контекст за 5 сек); s14 dedupe — отсылка к s13b, без повтора; s27 5×5 читаемо, solid gold/teal, нижняя gold-плашка = доминанта; s31 canon lec-02 dedicated Q&A. Палитра Ocean+Teal+Gold, gold на content, 0 off-palette.
- Cross-artifact (из v3 QA): consistency-checker APPROVE-CLEAN — глава не правилась (book-first), 11/11 case-refs verbatim, deck-split целостен, 0 drift/orphan.

## P2 (polish, НЕ блокер GATE)
1. s30 визуально чуть разрежён (мелкий текст vs плотность колоды) — closing-summary, приемлемо; кандидат на polish при GATE C, не блокирует.

## Известный owner-call → выносится решением на USER GATE B (не скрытый дефект)
- **P1-2 [presentation-critic v3]:** s04 title «Центральный вопрос лекции» = функция-в-title (U-6). Пограничный: работает как канон-eyebrow (s04 central-question есть и в lec-02). Решение владельца: оставить (канон-метка) vs ретайтл на контентный тезис ЦВ. По принципу pre-gate — explicit decision item, surfaced, не P0/P1-блокер.

## Recommendation
- [X] **PRESENT USER GATE B** (P0=0, P1=0; визуальный sweep выполнен; failure-share/terminology/палитра pass; s04-title — explicit owner-decision на гейте).
