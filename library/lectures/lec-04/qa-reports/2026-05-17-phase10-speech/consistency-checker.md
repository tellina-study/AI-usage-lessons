# Consistency Checker Report — Лекция 4 «AI в разработке ПО» — 2026-05-17

**Phase:** 10 (full 3-artifact alignment: chapter ↔ deck ↔ speech)
**Mode:** full
**Issue:** #99
**Artifacts:**
- `library/lectures/lec-04/speech.md` (v1 draft, новый артефакт Phase 9)
- `library/lectures/lec-04/chapter.md` + `chapter-part2.md` + `chapter-part3.md` (v1.1 finalized — **source of truth**)
- `library/lectures/lec-04/deck.yaml` + `deck-part2.yaml` (v1, 35 слайдов, GATE B finalized)
- `library/lectures/lec-04/glossary.yaml` (Glossary LOCK 2026-05-16)
- `notes/lecture-4-software-review/final/plan-v2-final.md` §2.1/§2.2/§4/§5

---

## VERDICT: APPROVE-WITH-POLISH

3-artifact alignment **YES** · book-first **YES** · Discrepancy #1 (curl) **RESOLVED** · Discrepancy #2 (s05 dual-role) **RESOLVED** · drift count **0 cross-artifact (chapter↔speech)** · orphan count **0** · terminology **CLEAN** (1 pre-existing P2 slide↔chapter gloss variant, frozen at GATE B, flag-only per Glossary LOCK).

APPROVE-WITH-POLISH (не CLEAN) исключительно из-за 1 P2 — pre-existing s23 slide-body Russian gloss «сбитый-с-толку посредник» vs chapter/speech canonical «запутанный посредник». Это slide↔chapter variant из Phase 7 scope (slide frozen GATE B), НЕ chapter↔speech drift и НЕ Phase-10 regression. Speech↔chapter alignment на этом термине идеальна. 0 P0, 0 P1.

## Severity counts
- **P0** (factual contradiction / missing coverage / book-first violation / orphan): **0**
- **P1** (significant drift / tone / missing cite in one artifact): **0**
- **P2** (minor — pre-existing slide-body gloss variant, flag-only): **1**

---

## Cross-artifact matrix (sample, несущие концепты + числа)

| Концепт / Число | Chapter (SoT) | Deck | Speech | Aligned? |
|---|---|---|---|---|
| Слайд-фрагменты (35: s01–s04, s04a, s05–s13, s14–s24, s24a, s25–s28, s28a, s29–s32) | [for-slide-sNN] s01–s32 | 35 ID (21+14) | 35 фрагментов, идентичный порядок | ✓ |
| Центральный вопрос | §0.3 | deck.central_question | s04 verbatim | ✓ |
| Лестница A→D (keystone) | §0.4 | s03 keystone | s03 4 уровня | ✓ |
| s05 dual-role (цена ошибки + 4-вопрос-рамка) | §1.1 (оба элемента в одной §, +§0.4 cost/radius) | s05 «цена ошибки растёт A→D», in_bucket=true (Реш.#100 ЗАКРЫТО) | s05 несёт оба, backed §1.1 | ✓ (Discr.#2 resolved) |
| curl #5 (AI-slop DDoS) | §4.5 deep-narrative + §5.4/Заключение payoff-якорь + §5.1 vibe-coding | НЕТ curl-слайда (s22=slopsquatting) | устный якорь s25/s32/Q&A, verbatim §-фразы; НЕ изобретает слайд | ✓ (Discr.#1 resolved) |
| 5 точек возврата ЦВ | §0.3 (§1.4/§2.3/§3.5/§4.4+§4.7/§5.2) | НЕ на слайдах (Реш.#100) | s08/s13/s17/s21+s23/s26 «N-е из пяти» | ✓ (plan §2.1 [P2-1 fix] = s21+s23, s26 — синхрон) |
| 6 дивайдеров (Р1–Р6) | §1/§2.1/§3.1/§4/§5/§6 | s04a/s10/s14/s18/s24a/s28a | «Раздел перв…шест из шести» | ✓ |
| METR прогноз −24% / вера −20% / факт +19% времени | §0.1, §3.5 | s01/s17 | s01 hook + s17 разбор (spelled) | ✓ |
| Copilot лаб ~56% / поле +7–22% | §1.2 | s06 | s06 spelled | ✓ |
| SWE-bench Verified ~88,7% / Pro ~64,3% | §2.2 | s12 ([VFY-day-of]) | s12 spelled + `[VERIFY-DAY-OF]` | ✓ |
| GitClear 211M / клоны 8,3→12,3 / реф 24→9,5 / churn 5,5→7,9 | §2.3 | s13 | s13 spelled | ✓ |
| SO-2025 «почти правильный» 66% | §1.4 | s08 | s08 spelled | ✓ |
| Replit 95/100 + Kiro 13ч + PocketOS 9 сек | §3.4, §3.6 | s16 | s16 spelled | ✓ |
| NYU ~40% / 12,1% CWE | §4.4 | s21 | s21 spelled | ✓ |
| Slopsquatting 576k / ~20% / 43% воспроизв. | §4.6 | s22 | s22 spelled | ✓ |
| Anthropic junior −17% | §6.3 | s30 | s30 spelled | ✓ |
| DORA n~5000 / adoption ~90% / stability↓ | §5.2 | s26 | s26 spelled | ✓ |
| confused-deputy → «запутанный посредник» | §3.4 canonical gloss | s23 body: «сбитый-с-толку посредник» (variant) | s23: «запутанный посредник» (=chapter) | ⚠ P2 slide↔chapter only |
| vibe-coding строгое определение | §5.1 | s25 | s25 (semantically identical) | ✓ |
| Backref Лекция 3 | «Лекция 3 §X» | «Лекции 3 §X» | «прошлая лекция» (7×, conversational) | ✓ |
| Forbidden anglicisms (пайплайн/фоллбэк/эдж-кейс/инсайт) | 0 в контенте | 0 в контенте | 0 в произносимом | ✓ |

---

## book-first verification (D1)

`git diff HEAD -- library/lectures/lec-04/chapter*.md` → **пусто** (0 строк). Глава НЕ тронута в Phase 9. Только `speech.md` — новый untracked файл. Speech derive строго из finalized chapter v1.1 + deck. **book-first соблюдён.**

Spot-check verbatim phrasing (speech ← chapter, не overclaim):
- speech s32 «curl — это AI, масштабирующий шум там, где валидация лежит на людях» = chapter-part3.md L291 **verbatim**.
- speech s25 «Replit, Lovable, curl как продукт slop-кода» ≈ chapter-part3.md L46 «Replit, Lovable/Moltbook, curl-slop как продукт slop-кода».
- speech s05 рамка 4 вопросов + «уровень A на каждом токене / D только вход-выход / каждый подъём оплачивается ослаблением контроля» = chapter §1.1 L151-159.
- METR подаётся как «+19% больше времени» = chapter §0.1 framing (не изобретённый знак).

Речь НЕ вводит утверждений вне chapter/deck. Числа == chapter v1.1 (spelled-out устные формы, сверены: METR/Copilot/SWE-bench/GitClear/SO/Replit/NYU/slopsquatting/Anthropic/DORA — 0 рассинхрона).

---

## DISCREPANCIES

### D1 (Brief Discrepancy #1) — curl #5 как устный якорь, не слайд-нарратив — **RESOLVED**
**Severity:** none (correctly resolved by speech-writer)
**Where:** chapter §4.5 (deep-narrative) ↔ deck (no curl slide; s22=slopsquatting) ↔ speech s25/s32/Q&A
**Анализ:**
- chapter §4.5 (`chapter-part2.md` L197-206) — полный curl-slop кейс #5 (DDoS на мейнтейнеров, асимметрия валидации, не-AI альтернатива). Backed.
- chapter-part3.md L46 (vibe-coding §5.1) + L289/L291 (Заключение payoff) — curl как несущий якорь.
- deck.yaml/deck-part2.yaml: s22 = slopsquatting (deck-part2 L153-167); curl собственного слайда НЕ имеет — подтверждено.
- speech: curl упомянут устно в s25 (vibe-coding-якорь, verbatim chapter-part3 L46) и s32 (payoff, **verbatim** chapter-part3 L291) + Q&A-backup. Речь НЕ изобретает curl-слайд, НЕ добавляет нарратив, которого нет в deck.

**Вывод:** No-Extra-Content соблюдён, book-first/deck-first соблюдён (verbatim chapter-фразы), strict-in устная доля держится ~46% минут и без полного curl-нарратива (speech-writer self-assessment). Расхождение разрешено в пользу deck-порядка корректно. Якорная форма curl в s25/s32 + Q&A достаточна и согласована с chapter.

### D2 (Brief Discrepancy #2) — s05 несёт И «цена ошибки» И 4-вопрос-рамку — **RESOLVED**
**Severity:** none (no semantic conflict)
**Where:** chapter §1.1 (+§0.4) ↔ deck s05 ↔ speech s05
**Анализ:**
- chapter §1.1 (`chapter.md` L148-159, оба `[for-slide-s05]`) содержит **оба** элемента в одной секции: (1) рамка 4 вопросов L151-156 («Что делает AI / Кто решает / Где человек обязателен / Типичный риск»); (2) принцип «цена ошибки растёт с автономией» L159 («каждый подъём оплачивается ослаблением контроля; A — каждый токен, D — только вход/выход»). §0.4 L132 дублирует cost/radius («чем выше уровень, тем строже критерий»).
- deck s05 assertion: «Цена ошибки растёт вместе с автономией A→D» + `chapter_ref: §1.1` + `in_bucket: true` (Решение #100 ЗАКРЫТО, methodology-critic v3 re-QA 2026-05-17, count 14→15).
- speech s05: несёт несущий принцип «цена ошибки растёт» (verbatim §1.1 L159 формулировки) + ввод рамки 4 вопросов.

**Вывод:** оба элемента backed одной chapter-секцией §1.1 (не разные §; `[for-slide-s05]` оба указывают на §1.1). Семантического конфликта нет. Не overclaim. deck s05 (Решение #100) НЕ противоречит речи. Один speech-фрагмент корректно покрывает §1.1 (внутри которого cross-ref на §0.4 cost/radius). Резолюция корректна.

### D3 — confused-deputy: slide s23 body Russian gloss variant — **P2 (pre-existing, flag-only)**
**Severity:** P2 (minor; slide↔chapter, НЕ chapter↔speech; frozen at GATE B; Glossary LOCK = MAY flag, MAY NOT rename)
**Where:** chapter §3.4 (`chapter-part2.md` L71 canonical) ↔ slide s23 body ↔ speech s23 L382
**Issue (с цитатами):**
- chapter §3.4 canonical gloss: `confused-deputy` («запутанный посредник» — привилегированный компонент, которого склоняют выполнить действие).
- speech L382: «Механизм — ровно "запутанный посредник" из прошлой лекции» — **точно совпадает с chapter canonical** ✓.
- slide s23 **visible body**: `confused-deputy` + `(сбитый-с-толку посредник: агент исполняет чужую инструкцию своими правами)` — другой русский глосс «сбитый-с-толку посредник».
- slide s23 **speaker notes**: `confused deputy` (без дефиса) — chapter Deep-dive box L228 тоже без дефиса (chapter-internal вариант, не cross-artifact).

**Анализ:** Это slide↔chapter glossary variant, относящийся к Phase 7 (chapter↔slides) scope, slide финализирован на GATE B. Для Phase 10 ключевое — chapter↔speech: speech использует ровно canonical «запутанный посредник» (book-first соблюдён). Это НЕ Phase-10 regression и НЕ chapter↔speech drift.

**Recommendation:** Фикс в slide (больший impact-артефакт), НЕ в chapter/speech: s23 visible body «сбитый-с-толку посредник» → «запутанный посредник» (canonical chapter §3.4). Speaker notes «confused deputy» → «confused-deputy» (canonical дефисная форма). Glossary LOCK: только REPORT, rename требует USER approval / orchestrator decision. Поскольку slide заморожен GATE B и расхождение P2 (термин из Л3, не вводимый этой лекцией) — допустимо deferred/owner-discretion, не блокер Phase 10.

---

## Coverage parity

- **35/35 слайдов имеют речевой фрагмент.** Speech ID list ≡ deck canonical ID list (s01–s04, s04a, s05–s13, s14–s24, s24a, s25–s28, s28a, s29–s32). 0 пропусков, 0 orphan, идентичный порядок.
- **0 orphan references:** каждый `sNN`-токен в speech соответствует существующему deck-слайду. Нет ссылок на удалённые/несуществующие слайды/разделы (cascade-safe; s01–s32 нумерация неизменна + 3 suffix-дивайдера Решение #101).
- **5 точек возврата ЦВ** консистентны chapter §0.3 ↔ plan §2.1 [P2-1 fix] ↔ speech: s08 (1-я), s13 (2-я), s17 (3-я), s21+s23 (4-я part+full), s26 (5-я). На слайдах кодов нет (Решение #100 соблюдён), в речи названы живым языком — корректно.
- **6 дивайдеров** (s04a/s10/s14/s18/s24a/s28a) = устные «Раздел N-й из шести», консистентны. Раздел 0 (открытие) без дивайдера — по plan §2.2, корректно.
- **LO замкнуты:** LO1 (s03 keystone + рамка на каждом уровне), LO7 (s29 «решающая ось, не сумма баллов» + s31 worked example), LO4 (s31 think-pair-share entry-Apply + мост к Семинару 4 на s32) — все присутствуют в речи и согласованы с deck learning_outcomes / chapter §0.5.
- **5 retrieval/интерактив-моментов** (s01 open-Q 30с / s08 think-pause 30с / s17 retrieval 30с / s22 poll 20с / s31 think-pair-share 2мин) — присутствуют в речи, совпадают с deck `interaction:` полями (s01 open_question, s08 think_pause, s17 retrieval, s22 poll, s31 apply). ✓

## Terminology (Glossary LOCK — terminology-only sub-check)

- **Forbidden anglicisms (пайплайн/фоллбэк/эдж-кейс/инсайт):** 0 в произносимом тексте speech, 0 в slides/*.md, 0 в deck-контенте. Единственные хиты — self-documentation (speech L571 самооценка «не часть произносимого», deck.yaml L76-77 glossary_lock комментарий) — exempt.
- **Canonical терминология chapter↔deck↔speech CLEAN:** лестница A–D, «автодополнение» (не автокомплит — 0 hits), «кодинг-агент» (speech 6×, slides 19×, 0 «coding-агент»), «оркестратор», «"почти правильный" код», «70/80%-проблема», «perception-gap» (speech 8× + «разрыв восприятия» 2× inline-gloss = chapter pattern), «SWE-bench Verified/Pro», «vibe-coding», «slopsquatting», «supply-chain», «accountability», «docs-as-code», «AGENTS.md/CLAUDE.md», «привнесённая/существенная сложность (Brooks)», «least-privilege» — все консистентны, drift речь↔глава↔deck = 0.
- **1 P2 exception:** confused-deputy Russian gloss — slide s23 «сбитый-с-толку посредник» vs canonical «запутанный посредник» (см. D3). speech↔chapter на этом термине идеально совпадает.

## Tone consistency

- Универсальная audience сохранена во всех 3 (без локального binding «инженер ИУ6» в произносимом/visible-контенте; deck.audience комментарий — frontmatter, exempt).
- Без «магической пилюли»: речь явно держит анти-страшилка + анти-карго-культ баланс (s24, s30, s32 — «не бойтесь AI и не доверяйте слепо»; «иногда правильный ответ — AI здесь не нужен»). Согласовано с chapter тезисом и deck assertions.
- Уважительная «вы»-форма во всех 3.

---

## Топ-фиксы (per artifact)

- **Chapter:** нет (source of truth, не тронута, своих P0/P1 в scope Phase-10 нет — chapter-internal «confused deputy» L228 без дефиса = fact-checker/book-editor домен, не cross-artifact drift, информационно).
- **Slides:** [P2, deferred/owner-discretion — frozen GATE B] s23 visible body «сбитый-с-толку посредник» → «запутанный посредник» (canonical §3.4); speaker notes «confused deputy» → «confused-deputy». НЕ блокер Phase 10; Glossary LOCK = REPORT only, rename требует USER/orchestrator approval.
- **Speech:** нет cross-artifact фиксов. Speech v1 draft согласован с chapter (book-first) и deck (структура/порядок/числа/термины). Готов к Phase 11 (speech revision → finalize) без consistency-блокеров. (Speech-writer's 2 «открытых расхождения» — оба верифицированы как корректно разрешённые, см. D1/D2.)

---

## PROPOSED GLOSSARY UPDATE
Нет. confused-deputy уже в glossary.yaml (canonical, note «глосс при 1-м упоминании §3 Replit»). Canonical форма оптимальна; проблема — drift slide-варианта, не glossary canonical. Никаких изменений canonical-формы не предлагается.

---

**Сводка для оркестратора:** VERDICT **APPROVE-WITH-POLISH**. 3-artifact alignment **YES**, book-first **YES** (chapter 0 diff), Discrepancy #1 (curl) **RESOLVED**, Discrepancy #2 (s05) **RESOLVED**, drift count **0** (chapter↔speech), orphan count **0**, terminology **CLEAN** (1 pre-existing P2 slide↔chapter gloss variant — frozen GATE B, flag-only per Glossary LOCK, не блокер Phase 10). 0 P0, 0 P1, 1 P2.
