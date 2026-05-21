# methodology-critic — speech v1 (Phase 10)
**Дата:** 2026-05-20
**Reviewer:** methodology-critic
**Target:** `library/lectures/lec-09/speech.md` (828 строк, 7458 слов, 35 slide-якорей, version v1 draft, status=draft)
**Source-of-truth:** `library/lectures/lec-09/chapter.md` v4 (finalized) + `library/lectures/lec-09/deck.yaml` v3 (35 rendered slides).

---

## VERDICT: REVISE

**Counter-check applied:** 8 P1 issues найдено → правило ≥5 P1 = REVISE сработало. Не «APPROVE-WITH-POLISH».

**Главная причина REVISE:** массовая Russification regression. Self-report «0 hits anti-anglicism» оказался **ложным** — независимый orchestrator-grep дал 5 hits, а полный сканер этого критика дал **107 distinct anglicism patterns / 186 occurrences** в видимом body речи. Это структурный regression относительно chapter v4 + slides v3 (которые прошли anti-anglicism cleanup) и прямое нарушение memory rule `feedback_russification` («owner Лекции 8 sent feedback "обилие англицизмов в презе! это просто трындец! убирай все!!! это провал"»). Это не polish — это revision-level fix.

**Прочие artefacts ENFORCED-bars cleared:** WPM ≤ 95 (max 89.3, avg 76.1), strict-in 40.9% (verify confirmed), 7 canonical failure-blocks present с явными уроками + альтернативами, micro-pause inserted в правильной позиции (s25 divider перед L1-L5), 35/35 anchors covered, designer-extras grep clean (0 hits), excluded items 0 body hits.

---

## TL;DR

| Metric | Self-report | Independent verify | Status |
|---|---|---|---|
| WPM ≤ 95 cap (0/35 over) | ✅ | ✅ max 89.3, avg 76.1 | PASS |
| Strict-in ≥ 30% | ~40% holistic | **40.9%** computed; distributed Sec 1=39% / Sec 2=51% / Sec 3=29% / Sec 4=82% / Sec 5=36% | PASS (Sec 3 borderline) |
| 7 canonical failure blocks | 7 | 7 verified (Lavender×19, ALIS×9, MCAS×14, Lancet×7, Vincennes×5, Patriot×8, GPS-spoof×8) | PASS |
| 35 slide anchors covered | 35 | 35 sequential, 1-35 | PASS |
| Micro-pause at s25 divider | ✅ | ✅ correctly between MCAS (s24) and L1-L5 (s26) | PASS |
| Closing callback с «Цепь по-прежнему держит инженер» | ✅ | ✅ s34 | PASS |
| Anti-anglicism «0 hits» | **0** | **107 distinct patterns / 186 occurrences** | **FAIL — P1×4** |
| Designer-extras leak | 0 | 0 | PASS |
| Excluded items 0 body hits | ✅ | ✅ (Aerostate — только в Q&A explanatory backup, ОК) | PASS |
| Pacing math | 75 min total | **63 min active + 12 min Q&A = 75 min internally consistent** BUT task-brief section budgets (Section 2=16-17, Section 3=14-15, Section 4=15-17) MISMATCH frontmatter design (63 min active) → Section 2/3/4 actual under task-brief targets by ~3 min каждый | P2 — internally OK, but flag |

---

## Counter-check (ENFORCED)

- **8 P1 issues** logged below. ≥5 P1 правило сработало → verdict REVISE (не APPROVE-WITH-POLISH).
- **5 anglicism hits known apriori (task brief)**: decision-support / wargaming / fine-tuned / cost-asymmetry / big-tech / predictive maintenance — все подтверждены. **+102 additional patterns** обнаружены (см. P1#1-4).
- AI-Failure & Judgment ≥30% strict-in: **PASS holistic** (40.9%), Section 3 на 29% — marginally under-budget, но section содержит MCAS+Patriot canonical block (s24, 82% strict-in single-slide), не структурный gap.
- Lec-07 pattern reference: lec-07 speech 6745 слов; lec-09 = 7458 слов (+10%). Length proportional к 5-section structure + 7 failure blocks.

---

## P0 issues

**Нет.** Speech методически пригоден к чтению. Failure-bucket present, lessons explicit, OODA keystone preserved, judgment-frame не «магическая пилюля». Все P0-grade structural bars cleared.

---

## P1 issues (8 — REVISE trigger)

### P1.1 — Anti-anglicism regression: **107 distinct patterns / 186 occurrences в visible body**
**Severity:** P1 (структурный regression относительно chapter v4 + slides v3 standards; memory rule `feedback_russification` ENFORCED)
**Evidence:** speech-writer self-report «Anti-anglicism reported 0 hits» — false. Полный сканер обнаружил:

**Топ-20 by frequency (полный список — см. Appendix A):**
| # | Pattern | Hits | Sample line |
|---|---|---|---|
| 1 | review (formal) | 6 | l.378, 382, 506 «20 секунд проверки — это формальное подтверждение, не review» — «не для повторной проверки» |
| 2 | callout | 5 | l.306, 314, 432, 540 — везде описание слайда (можно «выноска» / «вставка») |
| 3 | capability (English) | 5 | l.338 «AI capability и authorization stack» |
| 4 | override | 5 | l.492 «operator override»; l.512 «не мог override» — «не мог переопределить» |
| 5 | adversarial / adversarial-атаки | 4 | l.274, 278 — «состязательные атаки» / «противоборствующие сигнатуры» в литературе РУ |
| 6 | accuracy (lowercase + Accuracy capitalized) | 6 total | l.278, 316, 378 «Accuracy 90%» / «правильная метрика» — оставлять «точность» (chapter использует «точность 90%») |
| 7 | life-and-death | 4 | l.316, 378, 416, 714 — «жизнь-смерть» / «решения о жизнях людей» |
| 8 | FMEA / FTA | 4 | l.524, 528, 808 — допустимы как technical acronyms, но без расшифровки при первом появлении (l.524 первое появление); добавить inline |
| 9 | Stop Killer Robots (без расшифровки) | 4 | l.584, 600, 672, 746 — раз есть «МККК» русский, нужен и «Stop Killer Robots — кампания за запрет автономного оружия» при первом появлении (нет) |
| 10 | edge-AI / edge AI / on-orbit | 6 total | l.206, 208, 220, 740 — chapter использует «edge AI on-orbit» с inline expansion; speech не объясняет |
| 11 | big-tech / big-tech return | 6 total | l.616, 618, 638 — slide header + body |
| 12 | wingman / supervises / executes | 9 total | l.454, 572, 576 — «AI executes lethal action без human authorisation» — chunk untranslated |
| 13 | Target Locked / target lock / autonomous-locking | 4 | l.392, 396, 478 |
| 14 | safety-critical | 3 | l.516, 808 — «безопасностно-критичный» (chapter использует) |
| 15 | trim, nose-down | 4 | l.512 «MCAS повторно командовал nose-down»; «MCAS автоматически корректирует trim вниз» — есть русский эквивалент: «балансировку», «нос вниз»; в авиа-литературе РУ используется «триммер» |
| 16 | trust-but-verify | 1 | l.98 — критический tonal marker, без русского — хотя в chapter §0 есть «доверяй, но проверяй» |
| 17 | hype | 1 | l.96 «где hype далеко впереди реальности» — есть «хайп» (русифицированное), но в строке «LLM-хайп опаснее всего» рядом — inconsistent |
| 18 | mental model / Pedagogical takeaway / Engineering takeaway | 4 | l.546, 588, 662 — академический клише, есть РУ эквивалент: «ментальная модель» (русифицировано), «педагогический итог», «инженерный итог» |
| 19 | Maven walkout → vendor consolidation → big-tech return | 3 phrases на одном слайде | l.616, 618, 638 — narrative arc построен на 3 untranslated phrases |
| 20 | rolling text | 3 | l.602, 658, 824 — это UN GGE term, можно «рабочий текст резолюции» |

**Anti-anglicism mandate сработал в:** brand names (Maxar Sentry, Palantir MSS, Anduril Fury, Helsing, etc.) — ОК; technical acronyms с inline расшифровкой при первом появлении (SAR, ATR, ISR, EW, LAWS, OODA в s04) — ОК.

**Anti-anglicism mandate НЕ сработал в:**
- Глубокие structural phrases («Maven walkout → big-tech return» становятся section headers / line 616);
- Lessons formulations («Accuracy %» — не та метрика); chapter использует «точность» — speech использует «accuracy»;
- L1-L5 ladder descriptions (s26 lines 568-576): «AI executes в pre-authorised envelope» / «Currently debated, not deployed» / «AI executes lethal action без human authorisation» — это semantic core страны, не brand names;
- HITL/HOOL/HOTL panel descriptions (l.650-654): «AI не действует без явной авторизации. Mapping: L1, L2» — «Mapping» можно «соответствие»;
- Q&A backup: l.808 «MCAS — canonical anti-pattern для всех safety-critical AI: single-point-of-failure, opacity, software-cures-hardware, FMEA failure» — каждое слово анг.

**Recommendation:** Полная russification revision. Target — close to 0 distinct patterns в visible body, оставлены только brand names + acronyms-with-RU-inline-expansion при первом появлении. Минимум — 8-10 specific phrases которые повторяются 3+ раз (top-20 above).

**Why P1, not P0:** Содержание лекции методически правильно — failure blocks, lessons, criteria, OODA keystone — все present и работают. Только tonal regression. Студент может прочитать речь с pauses на anglicism — но это создаёт friction, противоречит chapter+slides cleanup, нарушает memory rule. Нужен revision pass до GATE C.

---

### P1.2 — Section 2 (Decide) pacing under task-brief target by 3.5 min
**Severity:** P1 — может вырезать важный contents block
**Evidence:** Task brief target Section 2 = 16-17 min. Actual:
- Section 2 (s13 divider → s18 end at 33:00): **20:30 → 33:00 = 12.5 min** active.
- Под-budget на 3.5-4.5 min.

Section 2 — самый важный концептуально (Lavender canonical block, 3 уроки, archetypal anti-pattern для всего курса). 3.5 min недоозвучивания = потеря possibility lengthen Lavender lessons или vendor caveat.

**Reconcile note:** Speech frontmatter `pacing_target: "≈63 мин активной речи + 12 мин Q&A"` — внутренне consistent с 35-anchor design. Но task brief budgets (Section 2 = 16-17) предполагают 75-минутную лекцию с минимальной Q&A (5 min). Текущая структура — 63+12 = 75. Это намеренный design decision (speech is 63 min active + 12 min Q&A), не bug.

**Однако:** decision should be explicit, и user должен знать, что Section 2 (Lavender — canonical block лекции) занимает 12.5 min — не 16-17. Sections 3, 4, 5 тоже underbudget. Total 63 min vs 73 min implied by task brief.

**Recommendation:**
- **Если 63 min active по design** — это OK (frontmatter so states), но flag в pre-gate walkthrough.
- **Если task-brief budgets были target** — добавить ≥3 min в Section 2 (s17 Lavender = 3:30 currently, добавить minute на 4th lesson или на Lieber Institute / AOAV academic verification). И прorate Sections 3, 4.

**Decision needed from owner.**

---

### P1.3 — Section 0 (Раздел 0) — 0% strict-in failure content
**Severity:** P1 — но не структурный gap, объяснимо
**Evidence:** Per-section breakdown:
- Section 0 (s01-s06, 9 min): **0% strict-in** — setup, OODA keystone, glossary, dual-use intro.

CLAUDE.md AI-Failure rule требует **холистичности** distribution. Section 0 = 0% означает первые 9 минут не имеют failure-bucket content.

**Why P1, не P0:** Total strict-in 40.9% holistic. Section 0 — pure setup (cover, lecture-map, keystone, glossary, dual-use band) — по design не несёт failure content. Это допустимо в setup section.

**However:** Section 0 mentions в l.91 «AI вошёл в каждое звено, но не заменил человека» (judgment frame) и l.140 «провалы случаются на стыках» (foreshadowing). Это **partial-bucket** content (упоминание, не разбор). 

**Recommendation:** Добавить 30-60 сек в s05 (Keystone OODA) с явным foreshadowing failure-block, чтобы Section 0 ≥ 5% strict-in. Один-два sentence «Decide на Лавендере показал, что accuracy 90% — это 3700 ошибок при 37 тыс целей; Act на MCAS — single sensor + 346 жертв» — anchors лекции, не spoiler. Это разрядит Section 0 0% → ~5-10%.

**ИЛИ** — accept текущий design как «keystone setup, failure разбор в Sections 1-5». Frontmatter может это явно zafiksiruet.

---

### P1.4 — Closing callback s34: «Цепь по-прежнему держит инженер» — judgment OK, но last 2 sentences (l.768-770) — promotional, не engineering
**Severity:** P1 (тонко)
**Evidence:**
```
И последнее. Курс продолжается. В Лекции 10 — AI в энергетике. В Лекции 11 — транспорт и логистика.
И в каждой из них вы будете узнавать паттерны из этой главы. Потому что цепь Sense → Decide → Act работает везде, где есть инженерное решение и физический мир.
```

CLAUDE.md «No Extra Content Rule» — нет cross-reference в visible body без curriculum-relevance check. «Лекция 10, 11» — forward-pointing к будущим лекциям. Это допустимо если установлено в chapter (chapter §5.4 проверяет это), но здесь в speech это становится course-scaffold leak.

**Recommendation:** Сохранить keystone takeaway («Цепь по-прежнему держит инженер»), но переформулировать last sentence. Options:
- (A) Remove l.768-770 entirely. Закончить на «инструмент в инженерных руках, не автономный субъект» (l.766).
- (B) Заменить на single sentence «В оставшихся лекциях курса вы будете видеть тот же паттерн в других областях — потому что инженерное решение в physical world всегда раскладывается на наблюдение, выбор и действие.» (без числовых отсылок к будущим лекциям).

**Why P1:** Это «closure marketing» tone, не engineering. Снижает gravitas каноничного финала «Цепь по-прежнему держит инженер».

---

### P1.5 — Lessons formulation inconsistency — «Урок номер один» vs «Урок:» vs «Урок первый»
**Severity:** P1 (cosmetic, но влияет на retrieval practice)
**Evidence:**
- l.258 «**Урок номер один**. Прогностическое обслуживание...»
- l.278 «**Урок:** benchmark accuracy обманчив...»
- l.284 «**Урок:** GNSS — single point of failure...»
- l.378 «**Урок первый**. «Accuracy %»...»
- l.380 «**Урок второй**. AI снимает фрикцию...»
- l.382 «**Урок третий**. Human-in-the-loop...»
- l.402 «**Урок:** демо не равно продакшен...»
- l.410 «**Урок** — не про автоматизацию...»
- l.516 «**Четыре урока.** Первый: ... Второй: ... Третий: ... Четвёртый: ...» (MCAS)
- l.532 «**Урок:** когда automation «лучше человека»...»
- l.628 «**Урок первый**. Личная этика не равна индустриальному регулированию.»
- l.630 «**Урок второй**. «Не работать на DoD» теперь редкая роскошь.»

3 разных formats: «Урок номер один», «Урок:», «Урок первый». В пределах одного speech это создаёт listener-side confusion — нужны ли они all enumerated, или это просто tag «вот сейчас будет lesson».

**Recommendation:** Unify на ONE pattern. Suggest:
- Multi-lesson block (3, 4 lessons): «**Урок первый/второй/третий/четвёртый.** ...»
- Single-lesson block: «**Урок.** ...»
- Eliminate «Урок номер один» (l.258), «Урок:» colon-form (l.278, 284, 402, 532), «Урок —» dash-form (l.410).

**Why P1:** Lessons — core takeaway лекции (LO3 = «5 critеriев когда AI плохая идея»). Inconsistent framing reduces memorability.

---

### P1.6 — Acronym RU expansion missing для FMEA/FTA + FedRAMP HIGH at first appearance
**Severity:** P1 (orphan terms; reader-simulator P0-trigger)
**Evidence:**
- l.524 первое появление FMEA + FTA: «FMEA и FTA не пройдены. Single-point-of-failure должен был быть пойман на этой стадии.» — никакой RU расшифровки. Студент не знает, что это «Failure Mode and Effects Analysis» / «Fault Tree Analysis».
- l.332 первое появление FedRAMP HIGH: «Авторизация FedRAMP HIGH.» — без расшифровки в speech. Chapter §2.2 содержит «(federal cloud security framework)».
- l.338 повтор «FedRAMP HIGH, авторизация на нескольких classified networks» — снова без RU.
- l.660 «engineering decision: сколько миллисекунд у оператора есть на intervention» — «intervention» untranslated.

**Recommendation:** Inline RU expansion at first appearance:
- l.524: «FMEA и FTA — анализ отказов и анализ дерева отказов — не пройдены.»
- l.332: «Авторизация FedRAMP HIGH — высший уровень федеральной cloud-сертификации в США.»
- l.660: «engineering decision — конструктивное решение — сколько миллисекунд...»

Самые тонкие — `Mapping`, `mental model`, `Pedagogical/Engineering takeaway` — должны быть RU.

---

### P1.7 — L1-L5 ladder slide (s26) — major Russification leak с structural impact
**Severity:** P1 (high-impact для centerpiece slide лекции)
**Evidence:** Lines 568-576 — L1-L5 reading. Это THE центральная mental model лекции (по student-sim Phase 7, fonarь 4-го раздела).

```
L1, Assistive. AI выдаёт детекции. Человек решает. Пример — Palantir MSS. ms-to-intervention — минуты-часы.
L2, Semi-auto perception. AI рекомендует action. Человек авторизует каждое. Пример — Saker Scout. ms-to-intervention — секунды.
L3, Supervised autonomy. AI executes в pre-authorised envelope. Человек supervises. Пример — Anduril Fury wingman. ms-to-intervention — 100-1 000 миллисекунд.
L4, Pre-authorised auto-engage. AI engages по pre-set ROE. Человек может intervene, но не required в loop. Пример — Patriot auto mode. ms-to-intervention — менее 100 мс.
L5, Full LAWS. AI executes lethal action без human authorisation. Человек вне loop. Currently debated, not deployed.
```

5 levels × 3-4 untranslated terms each = ~17 anglicism patterns на ONE slide. Это самый высокий density density в speech. Lec 8 memory rule precedent — это **provala-level** для русско-speaking аудитории.

**Recommendation:** Полная RU revision s26 reading:
- L1, **Помощник** (Assistive). AI выдаёт детекции. Человек принимает решение. Пример — Palantir MSS. Время на вмешательство — минуты-часы.
- L2, **Полу-автономный** (Semi-auto perception). AI рекомендует действие. Человек авторизует каждое. Пример — Saker Scout. Время на вмешательство — секунды.
- L3, **Supervised autonomy / Управляемая автономия.** AI **исполняет** в **заранее авторизованном диапазоне**. Человек **наблюдает за циклом**. Пример — Anduril Fury wingman. Время на вмешательство — 100-1 000 миллисекунд.
- L4, **Pre-authorised auto-engage / Авто-удар по заранее заданным правилам.** AI **открывает огонь** по заранее установленным правилам применения силы. Человек может **вмешаться**, но не **обязан быть в петле**. Пример — Patriot в автоматическом режиме. Время на вмешательство — менее 100 мс.
- L5, **Full LAWS / Полностью автономное оружие.** AI **применяет летальную силу** без авторизации человеком. Человек вне петли. **Currently debated, not deployed → На сегодня обсуждается в ООН, не развёрнуто нигде.**

**Why P1:** Это THE центральный slide лекции. Untranslated leak = студент уносит anglicism phrasing вместо RU mental model, что НЕ соответствует chapter v4 phrasing (chapter §4.1 использует RU).

---

### P1.8 — Lavender s17 reading: «Accuracy %» untranslated несмотря на chapter «точность 90%»
**Severity:** P1 (centerpiece consistency with chapter)
**Evidence:**
- chapter §2.4 (line 354): «По собственному признанию ЦАХАЛ, **точность около 90%**». Chapter использует «точность».
- speech l.378 (s17 урок 1): «**«Accuracy %»** — не та метрика для life-and-death.»
- speech l.316 (s14 setup): «**«Accuracy 90%»** звучит хорошо. Но **accuracy** проектировалась под симметрию»

Это inconsistency между chapter (RU «точность») и speech (анг «accuracy»). Centerpiece lesson 1 (Lavender) — самый важный takeaway лекции. RU phrasing должен быть identical между chapter, slides и speech.

**Recommendation:** Заменить:
- l.316 «"Точность 90%" звучит хорошо. Но точность проектировалась под симметрию...»
- l.378 «"Точность %" — не та метрика для жизни-смерти ситуаций.»

Это part of P1.1 общий Russification, но flag separately because Lavender — canonical LO2 illustration лекции и должен быть identical to chapter wording.

---

## P2 issues (minor polish)

### P2.1 — Inconsistent Q&A backup numbering (В1, В2, ...) vs ranges of Q questions
**Evidence:** l.786 «В1.», l.790 «В2.», ... — Russian «В» (Вопрос). lec-07 speech использует «В1» для consistency. **OK, не issue**, проверил.

### P2.2 — Stage direction inside [пауза 3 секунды] inconsistent format
**Evidence:**
- l.58 `[пауза 3 секунды]` 
- l.252 `[пауза, смена тона]`
- l.288 `[пауза]`
- l.404 `[пауза, переход]`
- l.764 `[пауза 3 секунды]`

Acceptable — stage directions, не visible body. **Not flag.**

### P2.3 — l.768 «И последнее.» — может быть оверкилл («Спасибо» уже достаточно)
**Evidence:** Уже P1.4. Skip.

### P2.4 — l.778 (s35 Q&A welcome) «У меня в запасе есть готовые ответы на типичные каверзные вопросы» — wording «каверзные» tonally good, retain.

### P2.5 — Q&A backup В3 «Aerostate» — Q&A explanatory backup допустим (excluded item rule = «Q&A backup OK same as chapter»). **Not flag.**

### P2.6 — Closing salutation «Спасибо.» (l.770) — single word, lec-07 has more elaborate ending. Acceptable — short respects time. **Not flag.**

---

## Strengths (что хорошо)

1. **WPM math impeccable.** 0/35 fragments over 95 cap, avg 76.1, max 89.3. Pacing math empirically verified — внутренне consistent с 75-min lecture format.

2. **7 canonical failure blocks present + lessons:** Lavender (3 уроки + alternative — l.376-386), MCAS (4 уроки — l.516-524), ALIS (3 conditions — l.260-264), Lancet (демо ≠ продакшен — l.402), Vincennes (UI under combat stress — l.408-414), Patriot (automation bias — l.530-532), GPS spoofing (single-source-of-failure — l.284). Каждый block имеет explicit lesson + alternative.

3. **AI-Failure & Judgment Share ≥30% holistic:** 40.9% strict-in computed (matches self-report 40%). Distribution: Sec 1=39%, Sec 2=51%, Sec 3=29% (borderline под 30%), Sec 4=82%, Sec 5=36%. Holistic ENFORCED bar cleared.

4. **Micro-pause at s25 inserted correctly** (Phase 7 student-sim feedback): «Давайте на секунду переведём дух. Раздел четыре — самый плотный концептуально...» (l.546-550). Идеально между MCAS (s24, dense Act failure) и L1-L5 ladder (s26, conceptual).

5. **35/35 slide anchors covered.** Sequential `### [Слайд N — title] MM:SS-MM:SS` formatting consistent.

6. **Closing callback s34 work:** «Цепь по-прежнему держит инженер» (l.752) с triple replay (positive / critical / regulation) — strong gravitas. Engineering-judgment framing, не AI-восторг и не технофобия. (Last 2 sentences l.768-770 — P1.4 polish.)

7. **Excluded items 0 body hits:** МГТУ/Бауман/ИУ/Можайск/Aerostate/GigaChat — 0 visible body mentions (Aerostate only в Q&A explanatory backup as expected, accept).

8. **«мы с вами» distributed 13 hits across 5 sections** (l.56, 74, 90, 118, 182, 202, 254, 338, 376, 378, 508, 562, 584). Slight under-representation в Section 3 (1 hit) but distributed.

9. **Engineering judgment frame** explicit (4 places):
   - l.98 «тон — trust-but-verify. Не евангелизм, не диссидентство»
   - l.710 «семь критериев "когда не AI"»
   - l.722 «это не "нельзя", это "нужен redesign"»
   - l.762 «инженер выбирает контур»

10. **Designer-extras grep clean** — 0 hits. No «Лектору», no «Вы здесь», no `[VFY-day-of]`, no LO codes, no §X.X в visible body.

11. **Assertion-evidence pattern preserved** во всех sections. Lavender block (l.366-386) — exemplar: assertion → 6 facts → 3 lessons → alternative architecture.

12. **Anti-hype oговorки intact:** l.200-202 (Maxar Sentry «не одна foundation-модель»), l.470 (X-62A «narrow scripted scenario»), l.490 (Lancet «демо не равно продакшен»). Strict-in count benefited.

---

## Recommendations (приоритизировано)

### Top-3 must-fix перед GATE C

**1. (P1.1 + P1.7 + P1.8) — Russification revision pass.**
Цель: с 107 distinct patterns / 186 occurrences → < 20 patterns / < 30 occurrences (target close to slides v3 0-hit standard, минус допустимые brand names + acronyms-with-inline-RU).

Specific revision:
- s26 L1-L5 ladder reading (l.568-576) — full RU rewrite (P1.7 above).
- s17 Lavender lessons (l.378) — «точность» вместо «accuracy».
- s11 ALIS lesson (l.260-266) — RU version of 3 conditions.
- s24 MCAS 4 lessons (l.516-524) — RU version с FMEA/FTA inline.
- s28 Maven 3 eras (l.616-638) — «уход / консолидация подрядчиков / возвращение big-tech» — last needs RU.
- s29 HITL/HOOL/HOTL panel reading (l.650-654) — «Mapping» → «соответствие», «execution-loop» → «петля исполнения», «decision-point» → «точка принятия решения».

Estimated effort: 1-2 hours focused pass. **Не major rewrite** — substitutions table.

**2. (P1.4) — Closing callback s34 last 2 sentences.**
Удалить или переформулировать l.768-770 («Курс продолжается. В Лекции 10... Лекции 11... паттерны из этой главы»). Закончить на l.766 «инструмент в инженерных руках, не автономный субъект.»

Estimated effort: 5 min.

**3. (P1.5) — Lessons formulation consistency.**
Unify «Урок X» / «Урок:» / «Урок —» / «Урок номер X» в ONE pattern. Suggest «Урок первый/второй/...» для multi-lesson blocks, «Урок.» для single-lesson.

Estimated effort: 15 min.

### Should-fix (low cost, high pedagogical value)

**4. (P1.6) — Acronym RU expansion at first appearance.**
Add inline RU для:
- l.332 FedRAMP HIGH — «высший уровень федеральной cloud-сертификации»
- l.524 FMEA / FTA — «анализ отказов и анализ дерева отказов»
- l.660 intervention — «вмешательство»

Estimated effort: 10 min.

**5. (P1.3) — Section 0 strict-in foreshadowing.**
Add 30-60 sec foreshadowing failure-blocks в s05 (Keystone OODA). Brief mention «Lavender 3700 ошибок» / «MCAS 346 жертв». Distributes strict-in более evenly: Section 0 with 5-10% vs 0%.

Estimated effort: 10 min.

### Optional (defer if time-constrained)

**6. (P1.2) — Section 2 pacing decision.**
Decide: (a) accept 63-min active design (current), or (b) lengthen Section 2 (Lavender) к 16 min target. **Owner choice.**

---

## Appendix A — Anglicism patterns full list (107 distinct, 186 occurrences)

See body of P1.1. Top-20 most-frequent listed. Full list:

```
6x  review / 5x  callout / 5x  capability / 5x  override / 4x  adversarial / 4x  accuracy / 4x  life-and-death / 4x  FMEA / FTA / 4x  Stop Killer Robots (raw EN) / 3x  edge-AI/edge AI / 3x  on-orbit / 3x  big-tech / 3x  Target Locked / target lock / 3x  wingman / 3x  executes / 3x  supervises / 3x  safety-critical / 3x  trim / 3x  Engineering design / 3x  rolling text / 3x  Mapping / 3x  Maven walkout / 3x  big-tech return / 2x  Adoption / 2x  predictive intelligence / 2x  Accuracy / 2x  decision-support / 2x  long-tail / 2x  operator-in-loop / operator-guided / 2x  pre-authorised envelope / 2x  dogfight / 2x  combat-tested / 2x  strikes / 2x  anti-pattern / 2x  single-point-of-failure / 2x  opacity / 2x  mental model / 2x  Full LAWS / 2x  decision-point / 2x  intervene / 2x  vendor consolidation / 2x  drone footage / 1x  trust-but-verify / 1x  hype / 1x  Predictive maintenance / 1x  no-fly / 1x  benchmark / 1x  pathway абстракции / 1x  fusion / 1x  pipeline / 1x  input / 1x  output / 1x  wargaming / 1x  fine-tuned / 1x  cost-asymmetry / 1x  authorization stack / 1x  classified networks / 1x  AI-guidance / 1x  autonomously / 1x  autonomous-locking UI / 1x  combat stress / 1x  climbing / 1x  descending into attack / 1x  fluent, confident output / 1x  low-data / 1x  combat-strikes / 1x  collaborative pilots / 1x  supervised AI / 1x  counter-drone autonomy / 1x  AI-perimeter-defence / 1x  explosive growth / 1x  narrow scripted scenario / 1x  BVR / 1x  AI mother-drone / 1x  AI-FPV strike / 1x  anti-radiation seeker / 1x  Wreckage-анализ / 1x  onboard ML / 1x  operator override / 1x  GPS-guided / 1x  supply chain / 1x  nose-down / 1x  redundancy / 1x  automated mode / 1x  automation / 1x  Supervised autonomy / 1x  Pre-authorised auto-engage / 1x  pre-set ROE / 1x  lethal action / 1x  human authorisation / 1x  Currently debated, not deployed / 1x  Pre-authorisation envelope / 1x  L4-edge / 1x  Pedagogical takeaway / 1x  Engineering takeaway / 1x  execution-loop / 1x  real-time intervention capability / 1x  engineering decision / 1x  narrative arc / 1x  revenue stream / 1x  military use / 1x  classified deployments / 1x  defense partnerships / 1x  legal regulation / 1x  human approval / 1x  partnership / 1x  intervention / 1x  recommendation pre-set ROE / ...
```

**Acceptable / kept English** (not in above count): brand names (Maxar Sentry, BlackSky, Planet, Capella, ICEYE, Slingshot, Φ-sat-2, Pony Express, Lockheed, ESA, Rolls-Royce, Airbus Skywise, easyJet, F-35, ALIS, ODIN, GAO, Palantir, Maven, Scale, Donovan, Defense Llama, Thunderforge, Anthropic, AWS, IL6, Helsing, Altra, Centaur, Saab Gripen E, Anduril, Fury YFQ-44A, Lattice, Hivemind, Arsenal-1, AIM-120, X-62A, VISTA, DARPA ACE, Saker Scout, Brave1, Geran-2, Shahed, Cognitive Pilot, NVIDIA Jetson, Dell PowerEdge, Boeing 737 MAX MCAS, USS Vincennes, Iran Air, Aegis, Tornado GR4, F/A-18C, Lavender, IDF, ЦАХАЛ, +972, Lieber Institute, AOAV, UN GGE, UNGA, МККК, DoD Directive 3000.09, FAR, DO-178C, ARP4754A, Stop Killer Robots; acronyms with RU при первом появлении: SAR, ATR, ISR, EW, LAWS, OODA, HITL, HOOL, HOTL, IFF, ROE — все present in s04 glossary slide).

---

## Closing note

Speech v1 — методически правильный артефакт с ENFORCED ≥30% AI-Failure share, корректным OODA keystone, 7 canonical failure blocks, явными уроками, alternative architectures, и engineering-judgment framing. **WPM math перепроверен — 0/35 over cap.**

Главный gap — **Russification regression**. Speech-writer self-report «0 hits» оказался ложным (нарёок 107 distinct patterns). Это не «polish» — это **revise-level fix** перед GATE C, особенно для centerpiece slides s17 (Lavender lessons) и s26 (L1-L5 ladder) где RU phrasing должен matching chapter v4 + slides v3.

Estimated revision effort: 2-3 hours focused single-pass:
1. Russification substitutions (1-2 h)
2. Closing s34 sentences trim (5 min)
3. Lessons formulation unify (15 min)
4. Acronym RU expansion (10 min)
5. Section 0 strict-in foreshadowing 30-60 sec (10 min)

Готов к Phase 11 revision (single batched speech-writer agent pass).

---

*Конец methodology-critic report. Verdict: REVISE.*
