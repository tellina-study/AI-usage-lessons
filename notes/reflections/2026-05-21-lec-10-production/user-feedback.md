# User-feedback — Лекция 10 production retrospective

**Дата:** 2026-05-21. **Issue:** #126 closed. **PR:** #136 merged.

## Explicit corrections от пользователя (4 owner overrides)

### Override 1: «делай chapter длинным! сейчас кажется короткий» (Phase 2 trigger)

**Context:** Phase 2 brief target был ~10k слов, я расширил до 20-22k per memory `feedback_chapter_depth`. User intervened mid-Phase 2.

**Action taken:**
1. Stopped running Phase 2 agent (TaskStop — agent had not yet written meaningful content)
2. Updated memory `feedback_chapter_depth.md` с new target «выше 8-12k → 20-22k»
3. Re-spawned book-editor с explicit target 20-22k

**Pattern:** Initial target из memory rule был **conservative**; user wants chapter as deep reference, not concise overview. Memory updated immediately.

### Override 2: «должен быть как в лекциях 4-5 и зафиксируй это в общих инструкциях» (Phase 2 trigger v2)

**Context:** Just after Override 1 re-spawn. Lec-04/05 chapters are **3-part structure** (8.9k + 8.3k + 8.6k = ~26k для L4; 8.7+6.5+7.8 = ~23k для L5).

**Action taken:**
1. Stopped running Phase 2 agent again (TaskStop — partial progress lost)
2. Added new CLAUDE.md ENFORCED section: **«Chapter Multi-Part Pattern (ENFORCED — Lec-4/5 lesson)»**
3. Updated memory `feedback_chapter_depth` с lec-4/5 reference
4. Re-spawned book-editor с 3-part brief

**Pattern:** User wants infrastructure (CLAUDE.md ENFORCED rules + memory), не one-off fix. «И зафиксируй в общих инструкциях» — explicit signal: this is permanent rule, not session-specific.

### Override 3 (memory update by user/linter): chapter ≥30k слов для L4+ (Phase 4b trigger)

**Context:** Chapter v2 at 26 519 слов (within Lec-4/5 baseline 20-26k). User had separately worked on Лекция 11 (issue #128) — set baseline ≥30k. Linter or user updated memory `feedback_chapter_depth.md` mid-session: «L4+ chapter — минимум 30 000 слов».

**Action taken:**
1. Updated CLAUDE.md с new section **«Chapter Depth Baseline (ENFORCED — фундаментальное, issue #128)»** (≥30k для L4+)
2. Updated Anti-Patterns table: chapter <30k для L4+ = P0 BLOCKING REVISE
3. Updated `tools/lecture-production/README.md` §1 + §6
4. Spawned Phase 4b chapter expansion v2 (26.5k → v3 31.2k target met)

**Pattern:** User propagates rules across parallel lectures (Лекция 11 → Лекция 10) for consistency. Memory rule is authoritative; I apply immediately when memory updated.

### Override 4: «почему во всех лекциях ты проставляешь время раздела/слайда и свои методические комментарии?! убери и строго запрети себе так делать в будущем! в каждой лекции правлю» (Phase 8 trigger — most critical)

**Context:** Pre-USER-GATE B presentation. Phase 7 critic verdicts ready (slides v1 REVISE). I presented slides + asked for OK to Phase 8. User intervened with **explicit frustration signal**.

**Action taken:**
1. Stopped Phase 8 agent that was running on different brief
2. Independent grep: confirmed widespread timing leak (s02 cover «75 минут», s03 lecture-map (5 мин)/(14 мин), s06/s15/s22/s27/s33/s36 section dividers «14 минут · X cases», s38 Q&A «10 минут»). Methodology leak в s12/s17/s25/s33/s35/s37 speaker notes («методически важно», «главный методический пункт», «методическая ценность»).
3. Created memory `feedback_no_timing_no_methodology_in_slides.md` с full forbidden list
4. Added MEMORY.md entry
5. Added CLAUDE.md **«No Timing / No Methodology in Slides (ENFORCED — фундаментальное)»** section
6. Extended Pre-USER-GATE Walkthrough Rule §5 с 3 groups grep patterns (scaffold + timing + methodology)
7. Added Anti-Patterns table +2 rows
8. Re-spawned Phase 8 v2 с explicit MUST-FIX list для timing+methodology removal в дополнение к 8 P0 + 32 P1

**Pattern signals:**
- **«в каждой лекции правлю»** — meaning rule violated systematically across L1-L9; user has been correcting manually каждый раз. Cost ~2-3h wasted across 10 lectures. **Infrastructure fix mandatory** (otherwise L11+ will repeat).
- **«строго запрети себе так делать в будущем»** — explicit signal: ENFORCED rule, не «try to remember». Memory + CLAUDE.md + Pre-USER-GATE grep — все 3 layers needed.
- **Frustration tone (`?!`, capslock-equivalent through bold markers)** — высокий signal weight; should have caught in Pre-USER-GATE walkthrough before opening GATE.

### Override 5 (in same message as 4): «во многих оценках эффектов/потерь не хватает базы. а сколько на человека или без робота? а сколько было?»

**Context:** Sent within Phase 8 v2 brief discussion (same message as Override 4). Substantive content issue, не narrative scaffold.

**Action taken:**
1. Created memory `feedback_baseline_counterfactual.md`
2. Added CLAUDE.md **«Baseline / Counterfactual Mandate for Measurable Claims (ENFORCED)»** section
3. Added Pre-USER-GATE Walkthrough точка 12 — baseline coverage check (sample 5-7 measurable)
4. Added Anti-Patterns table +1 row
5. Added MEMORY.md entry
6. Extended Phase 8 v2 brief с MUST-ADD baselines для 18+ measurable claims (See & Spray 0.55% US ag, Plenty $940M from $1B+ raised, Plantix 10M из 120M Indian smallholders, Cognitive Pilot 1.3% из ~130k комбайнов РФ, Магнит 46 из ~55 РЦ ≈83%, etc.)

**Pattern:** Substantive engineering question («сколько на человека или без робота?») exposes pedagogical gap. Measurable claims без base impressive but engineering-insufficient. User has high signal: «AI сэкономил 50%» без baseline = пустое утверждение для инженера. **Infrastructure baked.**

## Implicit approval signals (без correction)

- **«о чем должна быть лекция 10?»** — initial scoping question; не correction
- **«запускай задачу в отдельном worktree...»** — implicit approval после initial scoping; instructs my workflow choices
- **«иди»** — после plan-v2 presentation (GATE 0); plan approved
- **«давай»** — после chapter v3.1 presentation (GATE A); chapter approved
- **«давай»** — после slides v2 presentation (GATE B); slides approved
- **«аапрув, мерж закрывай и рефлексируй»** — после GATE C presentation; final approve + merge + reflect command

**Pattern:** User uses **«давай» / «иди»** для quick GATE approval; **«аапрув»** для final state. NO «выглядит ок» / «продолжай» — always concrete approval/correction. Communication style — **terse**, decision-focused.

## Patterns about user preferences

### Communication style
- **Terse:** 1-2 word approvals («давай», «иди»), 1-line corrections («должен быть как в лекциях 4-5 и зафиксируй»)
- **Frustration explicit:** uses `?!` / capslock-equivalent / explicit «убери и строго запрети» — when corrected pattern violated repeatedly across multiple lectures
- **Substantive corrections:** не cosmetic; user catches structural gaps (baselines, multi-part structure, timing leaks)

### Level of detail expected
- **High detail in artifacts** (chapter ≥30k, baselines required, methodological honesty)
- **Low detail в communication** (Claude должен infer pattern + apply across all lectures)
- **Infrastructure-first preference:** «зафиксируй в общих инструкциях» — не fix only this lecture

### Autonomy vs confirmation
- User trusts orchestrator to plan + execute через GATEs
- BUT corrects systematic patterns (rules violations across lectures)
- Confirmation needed на **subjective decisions** (Hook choice, vertical farming structure, Р5 restructure — 3-question AskUserQuestion at GATE 0)
- Autonomous execution **between** gates expected

## New behavioral rules adopted from this session

1. **Pre-USER-GATE walkthrough — orchestrator independent grep MANDATORY** with 3 groups patterns (scaffold + timing + methodology) + baseline coverage check. Self-report НЕ accepted as verification. **→ already in CLAUDE.md PR #136.**

2. **Memory-rule update immediate response:** when user updates memory file mid-session, apply rule immediately to current work (Phase 4b chapter expansion responded к memory update ≥30k от Лекция 11 user override).

3. **Infrastructure-bundle pattern:** when user signals «в каждой лекции правлю» — fix not just current lecture, но infrastructure (CLAUDE.md + memory + Pre-USER-GATE rule). Bundle in same PR as production work (precedent Лекция 9 #123, Лекция 11 #129).

4. **Concrete MUST-FIX list in brief:** when intervening with explicit rule violation, brief subsequent agent с specific slides + specific text changes (not abstract «apply rule»). Phase 8 v2 brief had concrete edit list для каждого affected slide → 0/0 hits independent grep после fix.

## Frustration triggers

**User frustration was triggered ONCE — Override 4 («?!»)** — by repeated timing+methodology leaks across L1-L10 despite existing No Extra Content Rule. **Root cause:** existing rule too abstract («timing on visible content — FORBIDDEN»); subagents systematically slipped because no concrete forbidden pattern list, no independent grep check. **Fix:** explicit forbidden pattern list + Pre-USER-GATE Walkthrough Rule §5 grep groups + Anti-Patterns table rows. **Verified after Phase 8 v2:** 0 hits independent grep.

## Summary

4 explicit user corrections, each producing infrastructure-level improvement (not one-off fix). 1 frustration trigger handled через memory + CLAUDE.md + Pre-USER-GATE grep updates. User trusts orchestrator between gates; corrects systematic patterns when violated. Communication terse, decision-focused; high signal-to-noise ratio.

**Net learning:** when user says «в каждой лекции правлю» — это сигнал для ENFORCED infrastructure rule + Pre-USER-GATE independent grep + Anti-Patterns table, не для one-shot fix. Bundle во same PR as production work.
