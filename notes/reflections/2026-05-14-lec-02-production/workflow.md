# Workflow — Lec-2 production observations

## Iteration cycle inefficiency

**Phase 8 evolved into 6 sub-iterations** (8.0 → 8.5 → 8.6 → 8.7 → 8.8 → 8.9) driven by 5 user feedback rounds. Each sub-iteration:
- Designer agent spawn (~30-60 min)
- Manual sync to main repo (~3-5 min)
- Visual sweep by orchestrator
- USER GATE B presentation
- User reviews
- Feedback received

Total wall-clock Phase 8 → GATE B approved: ~5-6 hours.

**Compare:** Phase 11 batched revision — single speech-writer spawn covered 3-artifact touches (chapter + slides + speech metadata) in 40 min. Closed 6/6 P1 + 9/16 P2 in one pass.

**Lesson:** for polish rounds — **single batched revision agent** is 5-10× more efficient than per-artifact spawns.

## Sequential vs concurrent reality

Pipeline doc (`tools/lecture-production/README.md`) describes:
```
Phase 1 → 2 → 3 → 4 → USER GATE A → 5 → 6 → 7 → 8 → USER GATE B → 9 → 10 → 11 → USER GATE C
```

Reality в session:
- 3 параллельные lectures (Lec-01 retro / Lec-02 mine / Lec-04 other)
- Shared `.git` + shared agent definitions
- Some critics ran simultaneously (3-5 critics parallel в Phase 3/7/10)

**Sequential phases assumption works** for single-lecture mode. For multi-lecture parallel → worktree isolation + per-lecture branch refs + sync points before GATEs.

## Pre-USER-GATE walkthrough effectiveness

3 pre-USER-GATE walkthroughs were done (before A / B / C). All caught some issues, but:
- **Pre-GATE A (chapter):** caught Pearl spelling drift + cross-ref accuracy. Missed «hook engagement» since chapter doesn't have hook.
- **Pre-GATE B (slides):** caught [VERIFY-DAY-OF] in spec body but not in rendered PNG initially. Caught some «магнит» / glossary issues. **Did NOT catch Lec-1 pattern deviations** (top bar, missing lecture-map, missing Q&A) — those weren't in checklist.
- **Pre-GATE C (full):** caught «Пёрла» × 1 in changelog (acceptable), «авторегрессивный» в terminological note (acceptable), «Forward pass» in body (canonical exception). Clean.

**Lesson:** pre-USER-GATE walkthrough checklist needs **Lec-N-1 pattern compliance** items для Phase B.

## Critic agent file visibility issues

3 of 5 Phase 7 critics reported «slides/*.md missing». Caused by branch contention (mid-session checkout from parallel lec-04 session). Workarounds:
- consistency-checker used `git show issue-74:<path>` workaround successfully
- Others reported and stopped (correct behavior per brief)

**Lesson:** agent prompts should include explicit recovery instruction: «if files missing, try `git show <branch>:<path>` OR report state; do not assume git checkout needed».

## Agent spawn pattern — what worked

**Per-agent type:**
- `book-editor` (Phase 2, 4, 11): reliable, draft + revision both worked
- `presentation-designer` (Phase 5, 6, 8, 8.5, 8.6, 8.7, 8.8, 8.9): designer had file visibility issues 3× until worktree isolation; once isolated — reliable
- `speech-writer` (Phase 9, 11): reliable
- `methodology-critic`, `fact-checker`, `consistency-checker`, `presentation-critic`, `student-simulator`, `reader-simulator`: all reliable BUT had file visibility issues twice due to branch contention

**Parallel spawns:** 5 critics в Phase 7 — 2 reported missing files, 3 completed. Parallel spawn timing matters when branch state unstable.

**Lesson:** for parallel critic spawns — ensure branch state stable BEFORE spawning. Worktree isolation eliminates this concern.

## 3 GATE structure worked

Despite 5 feedback rounds on slides — GATE A (chapter) и GATE C (final) каждый took 1 round. GATE B (slides) took 5 rounds — это структурное проблема specifically для visual artifact (subjective + complex pattern matching).

**Lesson:** GATE A + C structure adequate; GATE B needs **Lec-N-1 reference comparison** + **engagement check** built into pre-walkthrough.

---

## Action

→ improvements.md P1-3 (single batched revision pattern), P0-4 (sync precondition), P0-5 (worktree policy).
