# Improvements — concrete action plan from Lec-2 production reflection

**Date:** 2026-05-14
**Linked:** REFLECTION.md, tools.md, workflow.md, content.md, user-feedback.md
**Goal:** prevent recurrence + raise quality для Lec-3..Lec-17

---

## P0 (must implement BEFORE Лекция 3 starts)

### P0-1. Lec-N-1 Pattern Compliance Check (3 agent prompts)

**Files affected:**
- `.claude/agents/methodology-critic.md` — ADD «Lec-N-1 Pattern Compliance Check» section (plan + slides critique modes)
- `.claude/agents/presentation-designer.md` — ADD «Lec-N-1 Reference Read (MANDATORY before Lec-N design)»
- `.claude/agents/presentation-critic.md` — mirror methodology check (visual perspective)

**Specific text changes:** см. REFLECTION.md «Specific agent prompt updates».

**Test:** for next lecture, designer/critic must report «Read Lec-N-1 deck: matches pattern except [list]» in their first message.

**Estimated effort:** 60 min.

### P0-2. Hook Engagement Quality Check

**File:** `.claude/agents/methodology-critic.md`

**ADD section «Hook Engagement Quality Check»** (plan + chapter critique modes). Specific criteria:
- Time-evergreen (12 month stability)
- Emotionally engaging (surprise / curiosity / dissonance)
- «Висит на экране» worthy (visual richness)
- Connected to lecture assertion
- Counter-example check vs Lec-1 hook

**Test:** plan critique on Lec-3 must include explicit «Hook engagement» verdict.

**Estimated effort:** 30 min.

### P0-3. Missing-Fundamentals Check per concept

**Files:**
- `.claude/agents/methodology-critic.md` — chapter + slides modes
- `.claude/agents/presentation-critic.md` — slides mode

**ADD section «Missing-Fundamentals Check»** with explicit per-concept questions:
- Attention: matrix nature? N² cost? multi-head?
- Embedding: vector space before similarity? dimensions? training?
- Tokenization: end-to-end flow? BPE compromise?
- Sampling: distribution → token? local vs cloud?

**Test:** chapter critique on Lec-3 must check each concept's fundamentals explicit.

**Estimated effort:** 45 min.

### P0-4. Artifacts main-repo sync as GATE precondition

**Files:**
- `.claude/skills/pre-user-gate/SKILL.md` (если exists) или create
- `CLAUDE.md` — Pre-USER-GATE B section update

**Add MANDATORY check:** `ls -la library/lectures/lec-NN/rendered/lec-NN.{pptx,pdf}` before opening GATE B. If missing → STOP, sync, re-verify.

**Memory rule already saved:** `feedback_pre_gate_render_artifacts.md`. Extend to formal documentation.

**Estimated effort:** 20 min.

### P0-5. Git worktree isolation policy for multi-lecture parallel

**Files:**
- `tools/lecture-production/README.md` — ADD section «Multi-Lecture Parallel Production policy»
- `CLAUDE.md` — ADD reference

**Content:** см. REFLECTION.md «CLAUDE.md updates → Multi-Lecture Parallel Production» section.

**Estimated effort:** 30 min.

---

## P1 (high value, implement в ближайшие 1-2 недели)

### P1-1. Stock illustrations baseline in designer brief

**File:** `.claude/agents/presentation-designer.md`

**ADD DoD item:** «Deck должен иметь 5-10 supportive visual assets beyond functional charts (heroes / icons / stock images / concept-supporting imagery).»

**Estimated effort:** 15 min.

### P1-2. Pre-GATE grep enforcement for designer extras

**File:** `.claude/skills/pre-user-gate/SKILL.md` или `.claude/agents/presentation-designer.md`

**ADD mandatory pre-render grep step** with explicit STOP-if-hits rule:

```bash
grep -nE "\[VERIFY-DAY-OF\]|\[FACT-CHECK\]" library/lectures/lec-NN/slides/*.md  # 0 in body
grep -nE "LO[1-9]|§[0-9]\.[0-9]|→ s[0-9]+|см\. s[0-9]+" body sections             # 0
```

**Estimated effort:** 20 min.

### P1-3. Single batched revision pattern for polish rounds

**File:** `tools/lecture-production/README.md`

**ADD section «Polish Round Workflow»:** after Phase 7 critic feedback OR any post-GATE feedback round:
- Use ONE agent spawn (book-editor for chapter touches, presentation-designer for slide touches, speech-writer for cross-artifact touches)
- NOT separate spawns per artifact
- NOT separate fix-iteration commits
- Phase 11 demonstrated efficiency

**Estimated effort:** 30 min.

### P1-4. Anti-pattern grep on chapter changelog

**File:** `.claude/agents/consistency-checker.md`

**ADD check mode:** scan chapter changelog entries vs current chapter body for stale references. (e.g., changelog says «strawberry: 2→3 токена» but Self-check still asks «почему два токена».)

**Estimated effort:** 20 min.

---

## P2 (medium value, nice-to-have)

### P2-1. Lecture production status skill

**New skill:** `.claude/skills/lecture-prod-status/SKILL.md`

**Recipe:** `/lecture-prod-status N` → shows:
- Current phase / sub-phase
- Artifacts state (file paths, word counts, slide counts)
- USER GATEs passed
- Pending fixes (from latest critic reports)
- Branch state + worktree state
- Suggested next action

**Estimated effort:** 60 min.

### P2-2. Lec-1 deck structure as canonical reference doc

**New file:** `tools/lecture-production/lec-1-reference-pattern.md`

**Content:** distilled patterns from Lec-1:
- Slide types used + count
- Navigation pattern
- Cover composition rules
- Section divider pattern
- Q&A pattern
- Typography table
- Cross-cutting frames placement

Referenced by methodology-critic + presentation-designer как single source instead of grep-через-slides.

**Estimated effort:** 90 min.

### P2-3. Hook gallery — reusable hooks per lecture-type

**New file:** `tools/lecture-production/hook-gallery.md`

**Catalog:** 5-10 evergreen hook patterns by lecture domain:
- Introductory: provocative question + visual reveal (Lec-2 Token Rainbow)
- Industry-focused: stat shock + cost implication (Lec-4 medical risk)
- Technical: live demo + counter-intuitive result
- Etc.

Reference в presentation-designer brief как starting points.

**Estimated effort:** 60 min.

### P2-4. WPM check on slide speaker notes (not just speech)

**Files:**
- `.claude/agents/presentation-designer.md`
- `.claude/agents/consistency-checker.md`

**ADD:** speaker notes per slide should have 150-300 words (already в contract), AND if read aloud should be ~95 WPM compatible. Add explicit WPM check для notes.

**Estimated effort:** 15 min.

---

## Application sequence (when to do what)

**Before Лекция 3 starts:**
1. Implement P0-1 (Lec-N-1 pattern) — 60 min
2. Implement P0-2 (hook quality) — 30 min
3. Implement P0-3 (missing-fundamentals) — 45 min
4. Implement P0-4 (artifacts sync) — 20 min
5. Implement P0-5 (worktree policy) — 30 min

**Total P0:** ~3 hours focused work.

**During Лекция 3 production (incremental):**
6. P1-1 (illustrations) — 15 min
7. P1-2 (pre-GATE grep) — 20 min
8. P1-3 (single batched revision) — 30 min
9. P1-4 (changelog anti-pattern grep) — 20 min

**Total P1:** ~1.5 hours.

**Defer to Лекция 4-5:**
10. P2-1 (status skill) — 60 min
11. P2-2 (Lec-1 reference doc) — 90 min
12. P2-3 (hook gallery) — 60 min
13. P2-4 (WPM on notes) — 15 min

**Total P2:** ~3.5 hours.

**Grand total:** ~8 hours methodology investment → estimated 100+ hours saved across remaining 15 lectures (Lec-3..Lec-17).

---

## Success metrics для Лекции 3

After P0 implementation, target metrics for Lec-3 production:
- **User feedback rounds:** ≤2 (vs 5 в Lec-2)
- **Slide sub-iterations:** ≤2 (vs 6)
- **Total wall-clock:** ≤5 hours (vs 15)
- **Critic verdicts after Phase 11:** APPROVE-CLEAN (vs APPROVE-WITH-POLISH в Lec-2)
- **Pattern compliance:** Lec-3 deck mirrors Lec-1+2 structure из коробки

If metrics not met → revisit P0/P1 effectiveness и iterate.

---

**End of improvements plan.**
