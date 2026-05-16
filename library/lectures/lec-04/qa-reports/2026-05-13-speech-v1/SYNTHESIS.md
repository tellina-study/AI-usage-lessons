# Phase 10 Synthesis — Speech v1 Critique → Revision Brief для Phase 11

**Date:** 2026-05-13
**Critics:**
- `methodology-critic.md` — REVISE (0 P0 + 9 P1 + 8 P2)
- `fact-checker.md` — APPROVE-WITH-POLISH (1 P0 + 5 P1 + 3 P2)
- `consistency-checker.md` — REVISE (2 P0 + 3 P1 + 2 P2)

**Consolidated verdict: REVISE** (2 critics REVISE; 3 P0). Speech v1 структурно solid — WPM cap PASS, 34/34 slides covered, 5/5 dividers, 12 inclusive markers, central question chain intact, all 25 glossary terms canonical-locked. Revision is targeted — 2 critical issues + 17 P1 polish.

---

## P0 — 3 critical issues

### P0-1 (fact-checker) — s22 Gallup/Rock Health attribution swap
**Location:** `speech.md` L528 — s22 LLM anti-patterns block
**Issue:** Speech says «По **Gallup** — трое из пяти взрослых...». Per sources.md §6.3 — «3 in 5» = OpenAI/Rock Health 2025 survey; Gallup actually = 25% American adults.
**Fix:** «По OpenAI и Rock Health 2025 — трое из пяти взрослых обращаются к LLM с вопросами о здоровье. По Gallup — четверть взрослых регулярно.» OR drop Gallup и оставить OpenAI/Rock Health 60%.

### P0-2 (consistency-checker) — Chapter §Раздел 4 + LO4 sync drift — USER DECISION
**Location:** `chapter.md` L11 (frontmatter), L67 (§Учебные цели), L413-443 (§Раздел 4 «Микро-упражнение»)
**Issue:** Chapter v2 (APPROVED at GATE A `5c4b06c`) declares LO4 and has full §Раздел 4 «Микро-упражнение: AI как объяснение» с 3-step apply-based exercise + 2 self-check questions. **После** Phase 8.8 Fix 9, slides v5.1 (`2d45771`) и speech v1 dropped LO4 entirely:
- deck.yaml: `[LO1, LO2, LO3, LO8]` (LO4 missing)
- s18a section divider «Раздел 4: Микро-упражнение» **removed entirely** (commit Phase 8.8)
- s19 transformed: micro-exercise → lecture content «AI как объяснитель»
- Speech §Раздел 4 = «Этика и ответственность» (was «Микро-упражнение»)

**Result:** Chapter 7 sections (0-6) vs slides+speech 6 sections (0 + 5 numbered).

**Options:**
- **Option A:** **Sync chapter к current lecture format.** Drop LO4 declaration; remove §Раздел 4 «Микро-упражнение» as separate section; refold content (LLM-как-объяснитель pattern + anti-pattern) into §5 «Этика и ответственность» как didactic case study. Chapter SoT updates → matches slides+speech.
- **Option B:** **Keep chapter с LO4 + §Раздел 4 как optional self-study material.** Add note в chapter §Раздел 4: «Этот раздел — optional self-study apply-based упражнение. В live-lecture формате (slides v5.1 + speech) micro-exercise был заменён на didactic content "AI как объяснитель" в §5.» Format-divergence acknowledged.
- **Option C:** **Light-touch transitional note.** Chapter keeps as-is, add 1-paragraph header note: «Формат in-class lecture может отличаться: speech v1 trims micro-exercise apply-based step.» Minimal change.

**Recommended:** **Option A** — chapter SoT должен match actual lecture. Cleaner для downstream (если переиздание lecture). LO drop also simplifies — LO4 systematized в Lec 7 Практикум 1, not Lec 4.

### P0-3 (consistency-checker, second instance of same issue) — same as P0-2
Actually P0-2 covers both §D и §E. So effective P0 count = 2 (Gallup swap + chapter sync).

---

## P1 — 17 polish issues consolidated

### Methodology-critic P1 (9):
1. **s24 anglicism density** — 9 English-loan terms в 4 предложениях (control / liability / input / decision-maker / AI-suggestion / full context / AI-output). Trim к 2-3 terms максимум.
2. **Plan-v2 vs chapter v2 conflict on Лекция 5** — Speech correctly follows chapter (Лекция 5 = Коллоквиум 1), но plan-v2 stale. **Orchestrator note**, не speech edit.
3. **s09/s10/s13 dense cluster 88-90 wpm** — 3 consecutive heavy slides без cognitive rest. Add 2-3 sec pause between OR slow down один из них к 75 wpm.
4. **s19 placement в Раздел 4 «Этика» создаёт semantic mismatch** — applied LLM-explainer content под ethics divider. Решение: либо переименовать divider в «Раздел 4: AI как объяснитель и его границы», либо move s19 in section 5.
5. **«design choice» 4× repeated без Russian gloss** (lines 58, 150, 302, 416) — gloss «design choice — инженерное решение» на первом упоминании, потом OK reuse.
6. **«Generative AI не равно rule-based AI»** — awkward oral form. Use conversational: «Generative AI — это не rule-based AI» OR «Это два разных типа AI».
7. **«augmentation gap» replaced с «парадокс совместной работы» в s11** без cross-artifact sync (chapter §2.3 uses «augmentation gap» canonical EN form). Either sync chapter к Russian OR keep EN с italic + Russian gloss.
8. **s17a RU drug discovery context overload** — 5 named entities + 2 venues + 1 absence claim crammed. Trim к 3 main: «MADD (ITMO + Сбер AI Lab), AIDD center (Сбер + AIRI), Alliance #1 CD137 (May 2024).» Drop secondary.
9. **s23 Change Healthcare numbers run-on** — $22M / $2.457B без pause. Add «[пауза 2 сек]» between major numbers.

### Fact-checker P1 (5):
10. **s07 FDA per-year «6 в 2015 / 64 в 2020»** — not in primary sources. Verify or replace с aggregate timeline.
11. **s13 Daneshjou specific «20-30%»** — not directly cited. Soften к «значительно ниже» OR find exact figure.
12. **s22 Cass «март 2023» date** — not anchored in research. Soften к «начало 2023» (already noted в Phase 8.8 P1-15).
13. **s24 Price «Stanford» affiliation** — Price is at **U Michigan Law School** (not Stanford). Fix.
14. **s24 Gerke «Elsevier» affiliation** — Gerke is at **Penn State Dickinson Law / formerly Harvard Petrie-Flom** (not Elsevier — Elsevier was publisher of one journal). Fix attribution.

### Consistency-checker P1 (3):
15. **speech.md L390 [s17a]** — «минус двадцать миллилитров» → «минус двадцать и три десятых миллилитра» (canonical −20.3 мл per Phase 4 P0 fix).
16. **speech.md L610 [s26]** — «семидесяти трёх с половиной» (73.5%) → «семидесяти трёх и восьми десятых» (73.8% MASAI canonical). Internal speech inconsistency: s11 L262 correctly says 73.8%, но s26 L610 says 73.5%.
17. (P0-2 above repeats §D/§E here — already counted)

---

## P2 — 8 polish items (apply where compatible)

- Divider numerator/denominator (Раздел 0 не excluded from «X из 5» — say «X из 6» including opening)
- Лекция 2/3 callbacks dropped from s19 (could mention prior micro-exercises)
- Gallup verification not в pre-flight (если оставляем Gallup, добавить flag)
- s12 «маммография, маммография» duplicate word
- Sweeney 1997 attack vs 2002 paper year — clarify
- Goh «50 врачей» n=50 verification ОК
- Лекция 5 stale plan v2 — separate orchestrator task
- Minor punctuation cleanup

---

## What speech does WELL

1. **WPM hard rule respected** — max 90 wpm (cap 95); no violations.
2. **34/34 slides covered** в deck order with section dividers handled.
3. **5/5 section transitions** с «X из 5» bridge phrases.
4. **12 «мы с вами» inclusive markers** distributed naturally.
5. **0 forbidden hard-list anglicisms** (стейкс/фоллбек/пайплайн/кейс/инсайт/workflow/edge case).
6. **Central question chain intact** s05→s12→s14→s17a→s17b→s24→s27.
7. **8-item pre-flight checklist** с actionable URLs + commands.
8. **No fabricated cross-refs** (Лекция 5 = Коллоквиум 1 correctly per chapter, not stale plan).
9. **Cornerstone numbers cleanly verified** — Rentosertib +98.4/−20.3, Obermeyer 17.7→46.5, MASAI 80.5/73.8, FDA 1451, mosmed operational, Change Healthcare 190M/$2.457B/$22M.
10. **Engineering tone consistent** — «инженер строит», «engineer выбирает» — no moralizing.

---

## Recommended Phase 11 execution

**Step 1 — USER DECISION on P0-2** (chapter §Раздел 4 + LO4 sync). 3 options presented. Recommend Option A.

**Step 2 — Spawn speech-writer revision** addressing:
- P0-1 Gallup swap (1 line fix)
- P1 affiliations (Price + Gerke)
- P1 number drift (−20.3 / 73.8%)
- P1 anglicism reduction s24
- P1 pacing pauses s09/s10/s13/s23
- P1 «design choice» gloss
- P1 «не равно» conversational fix
- P1 «augmentation gap» sync
- P1 s17a RU overload trim
- P1 s19 placement (depends on user P0-2 choice)
- P1 verify FDA per-year + Daneshjou + Cass date

**Step 3 — If user Option A:** spawn book-editor для chapter §Раздел 4 refold + LO4 removal.

**Step 4 — Re-run consistency-checker** на all 3 artifacts post-revision.

**Step 5 — Pre-USER-GATE C walkthrough** (cross-artifact grep terminology + cornerstone numbers + central question payoff).

**Estimated revision time:** 30-60 min for speech P0 + P1; +30 min if chapter refold required (Option A).

---

## Hand-off

Agent: **speech-writer** для speech revision (Phase 11).
Optional agent: **book-editor** if user chooses Option A (chapter §Раздел 4 refold).
Output: `library/lectures/lec-04/speech.md` (in place); optionally `library/lectures/lec-04/chapter.md`.
After revision: consistency-checker re-run → USER GATE C.
