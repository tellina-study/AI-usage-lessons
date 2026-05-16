# Phase 7 v3 SYNTHESIS — deck v3 Лекции 3 (структурная ревизия)

**Дата:** 2026-05-16 · **Issue:** #87 · **Артефакт:** deck v3 (36 слайдов: s01–s30 + s04a/s13a/s13b/s23a/s25a/s31).

## Сводный вердикт: **APPROVE-WITH-POLISH** (0 P0; 2×CLEAN + 1×WITH-POLISH)

| Критик | Verdict | P0 | P1 | Ключевое |
|---|---|---|---|---|
| presentation-critic | APPROVE-WITH-POLISH | 0 | 2 | 6 новых слайдов интегрированы; divider'ы единый язык; s13b §5.5 PASS; s31 canon lec-02; s30 ретайтл OK; PA-3/PA-4 приняты |
| reader-rendered | **APPROVE-CLEAN** | 0 | 0 | self-cont **36/36=100%**; s13b закрывает gap чисто; divider'ы несут смысл; refs повышают доверие; поток лучше v2 |
| consistency-checker | **APPROVE-CLEAN** | 0 | 0 | deck-split целостен (353+425≤600); глава НЕ правилась (book-first); 11/11 case-refs verbatim из главы; 0 orphan; терминология LOCK |

build-deck Phase 6 «все critics APPROVE-WITH-POLISH/CLEAN, 0 P0» — **выполнено**.

## Fix перед GATE B

**P1-1 [critic] (must-fix, 1 слайд, точечно) — s14 дублирует inline-define fine-tuning.** После v3 определение FT вынесено на новый s13b; s14 на видимом слое всё ещё несёт почти идентичный парафраз → back-to-back повтор И противоречит deck-part2.yaml note «s14 inline-define больше НЕ дублируется». Fix: убрать дубль-определение из видимого тела s14 (s14 опирается на s13b), переписать 1-й абзац s14 notes (без повторного определения), перерендерить s14. Slide-md s14 не обновили под решение v3 — это и есть причина.

**P1-2 [critic] (owner-call, U-6) — s04 title «Центральный вопрос лекции».** Designer-claim «function-as-title только s30» неточен: s04 title называет функцию слайда. Пограничный (работает как канон-eyebrow «центральный вопрос», как s04 в lec-02). → решение владельца на USER GATE B (менять на контентный тезис vs оставить как канон-метку).

## Принятые PROPOSED ADDITIONS
- **PA-3 (s31 без gold):** ПРИНЯТО — canon-consistent с lec-02 dedicated Q&A (qa_minimal намеренно визуально тих); НЕ дефект, правок не требует (подтвердили critic+reader).
- **PA-4 (s09/s18 bridge source-md parity с новыми divider):** НЕ требуется — critic подтвердил «6 divider'ов = единый визуальный язык» (s09/s18 включительно), reader «divider'ы 4/4 несут смысл, поток лучше». Сторителлинг U-8 удовлетворён. Форсить source-md паритет = No-Extra-Content риск без выигрыша. DECLINE (not-needed).

## Не фиксить (P2, намеренно/опционально)
- consistency D1: s13 notes цитируют Barnett напрямую vs глава «Kore.ai со ссылкой на Barnett» — факты/arXiv верны, форма задана deck `notes_case_refs_v3`; опционально Phase-8.
- reader P2: s12 observability inline только в notes; notes 5 слайдов на потолке 300 слов — НЕ утяжелять дальше (ограничение для будущих правок).

**После s14-fix → Phase 8.5 pre-gate walkthrough (mode=slides) → USER GATE B** (+ решение P1-2 s04-title).
