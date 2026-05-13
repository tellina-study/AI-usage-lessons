# SYNTHESIS — speech v3 — Phase 12.5 critics — 2026-05-13

**Issue:** #70.
**Артефакт:** `library/lectures/lec-01/speech.md` v3 (~5035 слов, 31 slide blocks, 61 active min + 14 buffer).
**3 critics (Opus 4.7):** methodology-critic + fact-checker + consistency-checker.

## Общий verdict

**✅ APPROVE-WITH-MINOR** во всех 3 критиках. **0 фактических ошибок** (0 drift на 50 verified claims). **Closure 17.5/18 user fixes** (methodology). **Все 5 cornerstone концептов** (central question / DeepSeek teachable / 4 типа реализации / чек-лист / roadmap) **полностью aligned** между chapter ↔ slides ↔ speech.

| Critic | P0 | P1 | P2 | Verdict |
|---|---|---|---|---|
| methodology-critic | 1 | 4 | 6 | APPROVE-WITH-MINOR |
| fact-checker | 0 | 2 | 6 | APPROVE-WITH-MINOR |
| consistency-checker | 1 | 4 | 5 | APPROVE-WITH-MINOR |
| **После дедупликации** | **1** | **~7 уникальных** | **~12** | APPROVE-WITH-MINOR |

## P0 (1) — convergent, должен быть исправлен

### P0-1 — Speech [s26 pre-flight для ARC-AGI] orphan reference (methodology + consistency)
**Где:** `speech.md` line 48, секция «Подготовка перед лекцией».
**Что:** Pre-flight checklist инструктирует лектора перед лекцией обновить ARC-AGI цифры на arcprize.org для slide s26. **Но s26 теперь = «Прогнозы AGI: 4 спикера, 4 материальных интереса»** (Altman/Amodei/Hassabis/LeCun таблица) — ARC-AGI slide удалён в v3.1 (см. deck.yaml line 463).
**Эффект:** лектор за 15 минут до лекции пойдёт делать non-existent task, теряет время и доверие к pre-flight.
**Fix:** удалить блок «[s26 pre-flight для ARC-AGI]» из speech preparation section. Опционально: добавить новый pre-flight для актуальных quotes 4 спикеров (свежие выступления Альтмана/Амодея/Хассабиса/ЛеКуна — могут поменяться).

## Convergent P1 (≥2 critics)

### КОНВЕРГЕНЦИЯ A — «Приложение-робот» / «Приложение-автоматизация» / «Приложение (автоматизация)» terminology drift
- **methodology** P1 + **consistency** P1: 3 разных формы для одного концепта.
- **Где:**
  - chapter §3.6 (line 426): «**Приложение-робот**»
  - s21 visual (slide): «**Приложение (автоматизация)**»
  - s21 speaker notes (line 29): «приложение-робот» + (line 35) «приложение в режиме автоматизации» — internal split
  - speech [s21] (lines 547, 551): «**приложение-автоматизация**»
- **Fix:** unify on **«Приложение в режиме автоматизации»** (long form) или **«Приложение-автоматизация»** (compact, matches speech). Update в trio: chapter §3.6 + s21 speaker notes + speech (если нужно).

### КОНВЕРГЕНЦИЯ B — «Раздел N из 5» bridge phrases в dividers (methodology)
- **methodology** P0/P1 (assigned P0, понижено до P1 по re-read).
- **Что:** speech на dividers s10/s22/s27 говорит timing («22.5 минуты», «12 минут», «6.5 минут»), но **отсутствует устная фраза «Вы здесь — раздел N из 5»** (per REQUIREMENTS DoD §10).
- **Fix:** добавить 5-секундную фразу в каждый divider: «Вы здесь — Раздел 3 из 5» / «Раздел 4 из 5» / «Раздел 5 из 5». Создаёт continuous carry-over от карты лекции (s02a).

## Уникальные P1

### От methodology
- **s13 axis labels рассинхрон с deck.yaml.** Speech говорит «X = делегирование от пользователя, Y = контроль разработчика» — это после Fix-16 переориентации. Но deck.yaml line 210 всё ещё «X = контроль разработчика, Y = контроль пользователя» (старая формулировка). **Fix:** либо обновить deck.yaml (правильно), либо переписать speech (НЕ рекомендую, ось-orientation в Fix-16 правильная). Recommend: update deck.yaml.

### От fact-checker
- **s09 Mistral founders «Meta и DeepMind»** — speech (line 263) отбрасывает «Google» из «Google DeepMind». Listener may infer independent DeepMind (которое не существует с 2014). **Fix:** изменить «Meta и DeepMind» → «Meta и Google DeepMind» в speech [s09].

### От consistency
- **Pearl asymmetry в s28 speaker notes vs speech.** s28 speaker notes (line 34) упоминают «Три уровня Перла» как объяснение третьего вывода. Speech [s28] (lines 729-735) Pearl reference опускает. **Fix:** удалить Pearl reference из s28 speaker notes (для консистентности с речью; chapter §4.8 retains Pearl для self-study readers — book-first asymmetry OK).
- **s09 Llama-3 MMLU rounding в speech** — chapter+notes говорят «79.5 vs 68.9», speech (line 267) говорит «семьдесят девять с половиной против шестидесяти девяти» (округление 68.9 → 69). **Fix:** speech «шестидесяти восьми и девяти десятых» или «почти шестидесяти девяти».
- **s17 «Le Chat» без «Mistral»** — chapter+slide notes говорят «Mistral Le Chat», speech (line 445) только «Le Chat». Listener может не понять provenance. **Fix:** speech «Mistral Le Chat».

## P2 (selection)

- **s05a placeholder** «practitioner» в speech — acknowledged exclusion §0.3.
- **deck.yaml learning_outcomes incomplete** — declares `[LO1, LO4, LO6]`, но slides s18/s19/s24 list LO7. **Fix:** add LO7 в deck-level metadata.
- **chapter typo «promtpinging» → «промптингом»** на line 686.
- **chapter §3.6 quadrant orientation flipped** vs s21 visual (semantically same, spatially flipped). Optional: добавить cross-reference note в chapter.
- **s07 cognitive load** — 7 эпох в 4 минутах, 5 имён в одном предложении (line 205). Optional: подсветить только McCarthy + Vaswani, остальных в notes.
- **s11 «к этой модели мы будем возвращаться весь курс»** без конкретных лекций. Optional: добавить «лекции 3, 12, 16».
- **Critical reading attitude** — английская фраза в speech [s24] line 645 (намеренный «термин искусства»).

## Сильные стороны (НЕ менять)

✅ **Closure 17.5/18 user fixes** (methodology).
✅ **0 фактических ошибок** на 50 verified claims (fact-checker).
✅ **Все 5 cornerstone concepts aligned** (consistency).
✅ **0 неестественных англицизмов** в speech body.
✅ **«Мы с вами» count 12-15** (target ≥10, distribution равномерная).
✅ **WPM** average 74-82.5, max 95.0 (на пределе target ≤95 — OK).
✅ **Average sentence length 8.5 слов** (target ≤20).
✅ **Diagnostic, не magic-pill** — 0 «попадёшь в 10%», «секреты», «по всему зоопарку».
✅ **Pre-flight checklist + Резерв** в начале/конце.
✅ **Fallback phrases** для s01 backup, s03 silence, s13 demo overrun, s24 retrieval.
✅ **GPT-4o sycophancy timeline 25/28/29 апреля 2025** идеально sync во всех 3.
✅ **Mistral 7B / Llama-3 / DeepSeek R1 / MCP** все critical numbers verified.
✅ **Roadmap 17×3 модуля + РК1/2/3 на С8/12/17** sync.
✅ **Лекция 2 «Как работают современные большие модели» + 4 концепта по-русски** sync.
✅ **Tone diagnostic, мотивирующий на s09** «не отчаивайтесь».

## Топ-N правок для Phase 12.5 revision (приоритезированно)

### Critical (must-fix перед GATE C — 1 правка)
1. **P0 — s26 orphan pre-flight** — удалить блок «[s26 pre-flight для ARC-AGI]» из speech preparation. ~30 сек работы.

### High-value P1 (рекомендую — 6 правок)
2. **«Приложение-автоматизация» unify** в chapter §3.6 + s21 speaker notes + speech. ~5 мин.
3. **«Раздел N из 5» bridge phrases** в speech [s10/s22/s27]. ~5 мин.
4. **s13 axis labels** — update deck.yaml line 210 (X=Делегирование, Y=Контроль разработчика — sync с Fix-16). ~2 мин.
5. **Mistral «Google DeepMind»** в speech [s09]. ~1 мин.
6. **Pearl reference** удалить из s28 speaker notes. ~2 мин.
7. **Llama-3 MMLU 68.9** не округлять в speech [s09]. ~1 мин.
8. **«Mistral Le Chat»** в speech [s17]. ~1 мин.

### P2 (на усмотрение, ~10 минут)
9. **deck.yaml** add LO7 to learning_outcomes.
10. **chapter typo** «promtpinging» → «промптингом».
11. **s11 references** к лекциям 3/12/16.

## Recommendation orchestrator'у

✅ **GATE C — APPROVE-WITH-FIXES** возможен.

**3 пути:**

**Путь 1 (рекомендую) — Targeted P0+P1 revision v3.1.**
- Применить 1 P0 + 6 high-value P1 = 7 правок (~15-20 минут общими усилиями).
- Может сделать сам orchestrator (текстовые правки speech + 1 deck.yaml line + 1 chapter line + 1 slide notes).
- Не нужен sanity check (правки точечные, low-risk).
- USER GATE C → close-out.

**Путь 2 — Critical only (1 правка).**
- Только P0 — удалить orphan pre-flight в speech.
- Skip всё остальное (terminology drift, bridge phrases, ось sync etc).
- USER GATE C → close-out.
- **Risk:** «Приложение-робот» путаница останется в чате/seminar 1.

**Путь 3 — Approve as-is.**
- Принять speech v3 как есть.
- Все P0/P1 → polish iteration после first delivery (на основе real student feedback).
- Immediate GATE C → close-out.
- **Risk:** P0 orphan pre-flight может смутить лектора при первой подготовке.

**Estimated:** Путь 1 — ~30 мин. Путь 2 — ~5 мин. Путь 3 — 0 мин.

## Decisions для USER GATE C

**Вопросы пользователю:**
1. Какой путь revision — 1 / 2 / 3?
2. После approval speech → close-out лекции 1: branch push, PR, merge, update decisions.md, close issue #70 + #69 + EPIC #64?
