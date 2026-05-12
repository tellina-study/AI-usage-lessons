# SYNTHESIS — chapter.md v1 — Phase 3 critique — 2026-05-12

**Issue:** #67 (Phase 3 of EPIC #64).
**Артефакт:** `library/lectures/lec-01/chapter.md` (10,762 слова, 499 строк).
**3 критика:** methodology-critic + fact-checker + reader-simulator text-only (все Opus 4.7).

## Общий verdict

**APPROVE-WITH-MINOR-FIXES.** Все 3 критика — verdict положительный, исправления конкретные и точечные. Chapter v1 — методически крепкий академический draft, реализующий все 11 consolidated notes из v5 plan. Universal tone выдержан идеально (0 mentions ИУ6).

| Critic | P0 | P1 | P2 | Verdict |
|---|---|---|---|---|
| methodology-critic | 1 | 7 | 9 | APPROVE-WITH-MINOR-FIXES |
| fact-checker | 1 | 5 | 8 | APPROVE-WITH-MINOR-FIXES |
| reader-text-only | 2 | 8 | 7 | self-study ready ~85% |
| **Convergent** | **3-4** | **8-10** | ~10 | — |

## Convergent findings (≥2 критика согласны)

### КОНВЕРГЕНЦИЯ A — §4 перегружен (P0/P1)
- **methodology:** «§4 — 3122 слова, 8 подразделов, 15+ концептов» (P1 «граница с P0»).
- **reader:** «§4 ПЕРЕГРУЖЕН» (P0).
- **Fix:** разбить §4 на два или добавить mid-point recap. **Подкреплено сильно** — оба согласны.

### КОНВЕРГЕНЦИЯ B — §4.5 «Полная картина»: каталог без объяснений (P0/P1)
- **methodology** (P1): «Полная картина» обещает больше, чем даёт. Переименовать «Расширенный каталог».
- **reader** (P0): «свалка терминов» — model inversion / adversarial examples не объяснены, студент не подготовится к РК.
- **Fix:** канонические примеры (panda+noise=gibbon для adversarial; SSN из training data для model inversion) + переименовать.

### КОНВЕРГЕНЦИЯ C — Orphan terms (P1)
- **methodology:** scaling laws, эмбеддинги, индуктивные смещения, RLHF (поздно).
- **reader:** self-attention, scaling laws, MATH-500, бенчмарк, RLHF, inductive bias, model inversion, adversarial examples.
- **Fix:** глоссарий мини-определений / сноски при первом упоминании.

### КОНВЕРГЕНЦИЯ D — frontmatter references_count 32 vs 53 (P2)
- **methodology** + **reader**: оба заметили. **Fix:** обновить до 53.

## Уникальные P0 (требуют фикса)

### От methodology — P0-M1: §4.1 «5 тем vs 7 подразделов»
- §4.1 заявлено «5 основных тем в порядке роста абстракции», перечислено 7. «Рост абстракции» не выполняется.
- **Fix:** число 5→7 + переформулировать «в порядке от практической безопасности к концептуальным границам AI». 5 минут.

### От fact-checker — P0-F1: ⚠️ Унаследованная ошибка про DeepSeek 43%
- **Важное:** v4 fact-checker сам ошибся, когда советовал «43% — это Russia's share of global downloads». Реально по Microsoft Threat Intelligence (январь 2026 «Global AI adoption in 2025»): **43% — это market share DeepSeek в России** (telemetry/network data), измеренное иначе чем self-report ВЦИОМ (20%).
- Chapter v1 унаследовал ошибку из v5 plan.
- **Fix:** переписать §2.1 как **teachable moment** про две методологии измерения: ВЦИОМ self-report 20% (что респонденты признаются) vs Microsoft telemetry 43% (что фактически работает на устройстве). Это **усилит** educational value.

### От reader — P0-R1: §4.5 model inversion / adversarial без примеров (см. КОНВЕРГЕНЦИЯ B — duplicates)

### От reader — P0-R2: §4 перегружен (см. КОНВЕРГЕНЦИЯ A — duplicates)

**Итого уникальных P0 после дедупликации: 2** (§4.1 расхождение + DeepSeek 43% reinterpretation). КОНВЕРГЕНЦИЯ A/B уже учтены.

## Уникальные P1 (выборочно — главные)

### От methodology
- **§1.4 нет mini-worked-example** классификации одного инструмента по 4 осям. LO1 остаётся remember.
- **§3.7 порядок 4 вопросов не объяснён** (но Self-check 3.2 спрашивает об этом).
- **§3.7 vs §3.8 inconsistency Q4** «есть ли приложение» — порядок в чек-листе vs прогон.
- **§3.5 cognitive overload** — 3 связанных тезиса в одном абзаце про уровни автономии.
- **§4.4 RLHF определён поздно** (в §4.5, использован в §4.4).
- **§4.8 Pearl 3 уровня — недостаточно примеров** (только level 2, нужен level 3).

### От fact-checker
- **§2.2 «90% AI-пилотов в РФ»** — добавить direct URL Intellectual Analytics report.
- **Sycophancy timeline:** 28 апр начало rollback, не 29 апр (29 — postmortem date).
- **PARTS prompt-engineering** acronym — canonical source не найден.
- **Google Translate 1T words/month** — caveat «across Search/Lens/Circle».
- **Bloomberg/Reuters $589B** — конкретный article URL.

### От reader
- **§2.1 Gartner 80% workforce должно «осваивать GenAI»** — что значит «осваивать»? Размытый предикат.
- **§4.3 готовый пример галлюцинации** — нужен в главе, не отсылка к лекции.
- **§4.7 финальный тезис «прогнозы про стимулы»** — категоричен без нюанса Hassabis.
- **§4 self-check №2** «приведите пример в вашей сфере деятельности» — у 3-курсника нет сферы.
- **§2→§3 переход слабый.**

## Уникальные P2 (не блокеры — на усмотрение book-editor inline)

- LeCun ушёл из Meta 19 ноября 2025, основал AMI Labs (fact-checker).
- §1.2 timeline cognitive load (21 фактоид).
- §3.6 Copilot ambiguity без критерия.
- §5 камера-демо forward-reference.
- §3.4 PARTS Reasoning/Specification orphan.
- §1.1 обещание «явно называть какое определение» неисполнено.
- composite citations «Bloomberg / Reuters» — унифицировать.

## Сильные стороны (что НЕ менять)

✅ **Layered model (§3.1)** — закрывает КОНВЕРГЕНЦИЮ 8 из Phase 1. Сильное методическое решение.
✅ **Worked example §3.8 (конвейер)** — РАБОТАЕТ. Reader смог применить шаблон за 30 секунд. LO4 на apply.
✅ **Universal tone** — 0 mentions ИУ6 / Бауманка. **Идеально выдержано.**
✅ **Diagnostic tone** — magic-pill отсутствует, явно сформулирован в Введении и Заключении.
✅ **Reflection moment в §4.4** — retrieval practice в середине раздела.
✅ **17 self-check вопросов** — большинство retrieval/apply, не пересказ.
✅ **Honest framing §4.6 ARC-AGI** — diagnostic open question, не gotcha.
✅ **53 sources** — solid academic backing.
✅ **9 из 11 P0/P1 fixes из v4/v5 применены корректно** (fact-checker verified).

## Топ-10 правок для Phase 4 revision (приоритизировано)

| # | Слайд/Раздел | Правка | Severity | Effort |
|---|---|---|---|---|
| 1 | §4.1 | «5 тем» → 7 + переформулировать «в порядке роста абстракции» | P0 | 5 мин |
| 2 | §2.1 | DeepSeek 43%: переписать как teachable moment о двух методологиях (ВЦИОМ self-report 20% vs Microsoft telemetry 43%) | P0 | 15 мин |
| 3 | §4 | Разбить на 2 раздела (§4 проблемы внутри модели + §5 границы AI) ИЛИ добавить mid-point recap | P0/P1 | 30-60 мин |
| 4 | §4.5 | Канонические примеры для model inversion + adversarial examples + переименовать «Расширенный каталог» | P0/P1 | 20 мин |
| 5 | §1.4 | Mini-worked-example по 4 осям (например GitHub Copilot) | P1 | 15 мин |
| 6 | §3.7 | Объяснить порядок 4 вопросов + разрешить inconsistency Q4 | P1 | 15 мин |
| 7 | §3.5 | Разделить определение агента и уровни автономии | P1 | 15 мин |
| 8 | §4.4 | RLHF определить перед первым использованием в sycophancy | P1 | 5 мин |
| 9 | §4.8 | Развёрнутые примеры для levels 2 и 3 Pearl | P1 | 15 мин |
| 10 | Глоссарий | Сноски при первом упоминании: self-attention, scaling laws, эмбеддинги, MATH-500, бенчмарк, inductive bias | P1 | 15 мин |

**Total effort:** ~3-4 часа book-editor работы на v2.

**P2 (не блокеры):** LeCun affiliation, frontmatter `references_count: 53`, composite citations, forward-promises, cognitive load дробление — на усмотрение book-editor inline в v2.

## Recommendation orchestrator'у

✅ **USER GATE 1: APPROVE-WITH-FIXES.** Все 3 критика согласны: chapter v1 — крепкий draft, но требует 10 правок (3 P0, 7 P1) перед финализацией.

**Phase 4 plan:**
1. Спавнить `book-editor` (Opus 4.7) с топ-10 правок выше → chapter v2.
2. Optional: 1 sanity-check critic на v2 (methodology или fact-checker).
3. USER GATE 1 final → Phase 5 (slides update from chapter).

**Альтернатива (быстрее):** orchestrator применяет 10 правок направильно через Edit'ы (4 часа работы → ~30 минут с явными diffs). Скорее всего книжный draft нуждается в более вдумчивых правках от book-editor — рекомендую агент.
