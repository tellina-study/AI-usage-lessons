# Лекция 11 — User feedback reflection

**Дата:** 2026-05-21
**Issue:** #131

## Owner interventions (по хронологии)

### 1. Launch (start of session)
> «запускай задачу в отдельном worktree. смотри тенденции 2026, смотри как ИИ влияет на индустрию, как он реально применяется где хорош, а где нет. приводи максимум возможных примеров использования, помни про наши правила с неудачами. Наполни презу медиа - не менее 50% слайдов должны быть с медиа вставками. обязательно яркий хук с картинкой в начале и в конце»

**Effective:** clear constraints upfront — worktree isolation / 2026 trends / max use cases / failure rule / ≥50% media / hero hooks. Carry-forward as Phase 1 plan-checklist mandates → carried through Phase 5+6 deck design successfully (56% media achieved, hero s01+s39 real Wikimedia).

### 2. Chapter depth mid-stream
> «ты же делаешь чаптер таким же длинным как частях 4 и 5?»

**Effective:** Honest gap-flag. I answered «нет, L11 на 50%+ длиннее L4/L5 (13.4k vs 8.9k), но short of L8/L9 (16-17k)». Owner ответил «30к цель твоя».

**Mid-stream re-direct:** +16k expansion (122% от v2) — book-editor v3 spawn. Это cost 1 extra Phase (4b) но владелец явно хотел textbook-level depth. Worth it.

### 3. Rule recording explicit instruction
> «ты же запишешь 30к минимум чаптер в базовые правила для всех през»

**Effective:** Clean recording → PR #129 (CLAUDE.md «Chapter Depth Baseline» ENFORCED + tools/lecture-production/README.md §6 + memory `feedback_chapter_depth.md`).

**Lesson:** owner expects new rules to propagate to infrastructure immediately. Carry-forward: when user invents new rule, capture в CLAUDE.md + README + memory в same session, не defer.

### 4. Slides revision direction (Phase 8 brief)
> «вноси все правки + убери методические и временные комментарии (lo в начале оставь), убери англицизмы, переведи цитаты!»

**Effective + structural:** Three explicit owner mandates M1/M2/M3 — became spine of Phase 8 brief.
- **M1 «убрать методические и временные комментарии»** — carried into pre-USER-GATE B walkthrough as independent regex check. Caught timing markers leak (designer self-report FALSE).
- **M2 «убери англицизмы»** — 620 unique → 143 (77% reduction). Deep latin-token scan post-revision.
- **M3 «переведи цитаты»** — 5 quotes RU primary (Musk / Bainbridge / Foxconn Liu / Trump / Toyota GAIA).

**Lesson:** owner mandates М-numbered (M1/M2/M3) — clear, actionable, testable. Pattern carry-forward для future lectures: when user gives multi-part mandate, label each piece with M-number, propagate в agent prompts.

### 5. Multi-part split decision (GATE A v4)
> «Split на 3 parts → потом slides»

**Effective:** Clean structural decision. Chapter 1438 lines (>600 doc-size-limit). User chose to set precedent for new PR #129 rule via L11 split. Multi-part split delivered (409/510/592 lines, ≤600 each).

**Lesson:** new rules need *first concrete implementation* to be the precedent. L11 multi-part split → reference pattern for L4-L17 prospective compliance.

### 6. GATE C approval
> «мерж, рефлексируй, закрывай»

**Effective:** Compact final approval. Three commands. Carry-forward как paradigm: «merge + reflect + close» is the standard GATE C closing.

## Patterns from owner behavior

### Owner preference: directness + decisiveness
- Short imperative instructions («запускай», «вноси все», «30к», «мерж»)
- Doesn't tolerate hedging — when I asked «hero quality?» owner said «вноси все правки» rather than per-item review
- Owner trusts orchestrator to handle execution, but expects checks + verification (especially via pre-USER-GATE walkthroughs)

### Owner preference: structural rule changes via explicit recording
- «запишешь в базовые правила» — owner wants rule changes propagated to CLAUDE.md / README / memory in same session, not deferred
- Carry-forward: ANY new rule introduced mid-session goes to infrastructure immediately

### Owner preference: failure-bucket emphasis (course mission)
- «помни про наши правила с неудачами» — owner consistently anchors AI-Failure rule ≥30%
- This matches CLAUDE.md «AI-Failure & Judgment Content Rule» — фундаментальное правило курса
- L11 delivered 41.1% chapter words (margin +11pp над 30%) — owner satisfied

### Owner preference: real images, no mocks
- «обязательно яркий хук с картинкой» — implied no-mock-fallback rule
- Memory rules `feedback_hero_images` + `feedback_no_mock_fallbacks` enforced
- 10 Wikimedia CC-BY-SA Tier 2 acquisitions on slides — owner satisfied

### Owner preference: anti-anglicism for RU audience
- «убери англицизмы» — explicit
- Memory rule `feedback_russification` reinforced
- Deep latin-token scan post-revision now mandatory

### Owner preference: quote translation для RU audience (NEW pattern)
- «переведи цитаты!» — explicit, exclamation
- This **extends** Russification beyond narrative — to direct quotes too
- Carry-forward: foreign-language quotes на RU slides → RU primary + English original optional в speaker notes parenthetical
- Update memory rule `feedback_russification` to include quote translation mandate

### Owner pattern: M1/M2/M3 mandates
- Three explicit owner mandates in Phase 8 — became central spine of revision
- This pattern of multi-part mandate works well — owner can pack 3+ unrelated issues into single brief, each becomes its own check

## What I should improve in user communication

### 1. Be more direct about gaps before user spots them
- Owner had to flag chapter depth gap («ты же делаешь чаптер таким же длинным?»). I should have proactively flagged «L11 chapter currently 13.4k — below L8/L9 16-17k recent norm; option to deepen» before owner asked.
- Carry-forward: at each GATE, proactively compare с прецедентами L_{N-1}, L_{N-2} + flag any drop в quality metrics.

### 2. Acknowledge user mandates explicitly when carrying forward
- After M1/M2/M3, I should have said «принято — M1: methodology comments out / M2: Russification deep / M3: quotes RU. Carrying into Phase 8 brief» explicitly. I did some of this but inconsistently.

### 3. Distinguish между owner blocking concerns vs polish
- When proposing options, label «structural P0 (blocking)» vs «P2 polish (non-blocking)» — это reduces ambiguity.
- L11 did this in GATE C presentation. Carry-forward.
