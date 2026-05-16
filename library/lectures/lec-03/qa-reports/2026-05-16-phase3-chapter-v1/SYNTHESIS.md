# Phase 3 SYNTHESIS — chapter v1 Лекции 3

**Дата:** 2026-05-16 · **Issue:** #87 · **Артефакт:** `library/lectures/lec-03/{chapter.md,chapter-part2.md,chapter-part3.md}` v1.

## Сводный вердикт: **APPROVE-WITH-POLISH** (0 P0 у всех 3)

| Критик | Verdict | P0 | P1 | Ключевое |
|---|---|---|---|---|
| methodology-critic | APPROVE-WITH-POLISH | 0 | 4 (→2 действия) | strict-in честно **58.4%** (≥40% pass, распределён по 5 разделам); арка замкнута; LO7×4 моделирует; Forbidden соблюдён |
| fact-checker | APPROVE-WITH-POLISH | 0 | 2 | 13/13 critical claims + 8/8 arXiv verified live; 0 инверсий/мисквотов; метки дисциплинированы |
| reader-text-only | APPROVE-WITH-POLISH | 0 | 4 | без структурных блокеров; failure-разборы не страшилки; ЦВ окупается; связь с Л2 корректна |

## Phase 4 fix-list (book-editor, точечные правки, БЕЗ переписывания нарратива)

**P1 (обязательно):**
1. **§5.3 mini-apply разомкнуть** [meth-P1-1]: задача B (LO4 Apply, part3:~244) полностью разобрана тут же в Q&A В2 → Apply вырождается в узнавание. Вставить разделитель-ремарку «сформулируй ответ ДО сверки с В2» (~2 предложения). Mastery в Семинаре 3 не трогать.
2. **§4.1 cascade-ремарка** [meth-P1-2]: §4.1 (~819 слов, плотный, → слайд s19) — добавить ~1 предложение «на слайд выносится только assertion-уровень, разбор — в главе» (защита downstream-деривации).
3. **Нумерация кейсов сквозь шов part2→part3** [reader-P1-1]: part2 (~стр.238) анонсирует «#1, #3, #15», part3 §4.5 называет «Провал 1/2/3»; «#15» нигде не присвоен (реальный max #12). Унифицировать: использовать канонические номера из `notes/research/lecture-3/failures-and-limitations.md` (#1 $4,200, #3 reliability compounding, #15 multi-agent хрупкость) ВЕЗДЕ — и в анонсе, и в заголовках §4.5; либо убрать «#»-нумерацию и сделать сквозные «Провал N» консистентно с анонсом. Главное — анонс = заголовки.
4. **§4.5 возврат контекста на шве файла** [reader-P1-2]: в начале part3 §4.5 — 1–2 предложения recap «4 режима отказа цикла из §4.3» (внимание провисает между файлами).
5. **`golden set` inline-define** [reader-P1-3]: part1 §2.4 — определить при первом употреблении (сейчас только в Q&A-резерве, поздно для self-study).
6. **`BAA` расшифровать** [reader-P1-4]: первое употребление (§4.6) + чек-лист §5.3 п.8 — дать расшифровку/глосс (Business Associate Agreement — договор об обработке данных; не общеизвестно студенту ИУ6).
7. **`prompt injection` / `least-privilege` inline** [reader-P2→повышено]: оба в §7-списке inline-required, но употреблены за ~30 стр. до формального определения — добавить inline-фразу при первом упоминании (part2 §4.1 / part1 §2.4).

**P2 (polish, в тот же проход):**
8. Glossary cascade-lock [meth-P2-3]: сверить 13 inline-required терминов дословно с glossary §6 (Glossary Lock, Phase 4).
9. §1.4 Q&A В4 [meth-P2-4]: убрать дублирующий повтор механизма context rot (есть в §1.4 и в В4).
10. Метки при финализации [fact-P1]: сохранить `[VFY]` на Anthropic ZDR (§4.6, day-of) + `[FACT-CHECK]` на GraphRAG cost-figures (DD box 2).

**Orchestrator-нота (не правка book-editor):** `notes/research/lecture-3/sources.md` содержит future-dated arXiv-ID (2601.18699, 2603.22489, 2601.06007) — fact-checker подтвердил: в нарратив НЕ протекли. Следить при revision, чтобы не попали (непроверяемы).

**После правок:** status `draft → reviewed`, version `v1 → v1.1`, changelog в `chapter.md`. → Phase 4.5 pre-gate walkthrough (orchestrator) → USER GATE A.
