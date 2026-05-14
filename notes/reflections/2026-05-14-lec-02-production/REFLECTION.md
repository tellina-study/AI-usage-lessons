# Reflection — Лекция 2 production (Phase 0 → GATE C)

**Date:** 2026-05-14
**Lecture:** Лекция 2 «Как работают современные большие модели»
**Pipeline:** 12 phases (0 → 11), 3 USER GATEs, PR #75 merged 2026-05-14T06:43Z
**Branch:** issue-74-lec-02-llm-internals (deleted post-merge)
**Issue:** #74 (closed)
**Final artifacts:** chapter v1.2 (11,477 слов) + slides v1.7 (36) + speech v1.1 (4,417 active words, max WPM 90.5)

---

## Executive summary

Lec-2 production completed but at **significant overhead**: ~80 fixes across 6 sub-iterations of slides (Phase 8 / 8.5 / 8.6 / 8.7 / 8.8 / 8.9), driven by **5 rounds of substantive user feedback**. Phase 10 critic verdicts were APPROVE-WITH-POLISH but the journey to get there was 2-3× longer than expected.

**5 root cause categories:**

1. **A. Git infrastructure brittleness** — parallel lec-04 production session caused branch contention; my own commits (`2b64e90` / `d2d913d`) got overwritten when lec-04 agent did `git checkout` in shared `.git` folder; multiple subagents reported «slides/*.md missing» mid-session.
2. **B. Visual design pattern drift** — designer made independent decisions inconsistent with Lec-1 pattern (top progress bar on every slide vs only on dividers; missing lecture-map; missing section dividers for 4 of 5 sections; missing dedicated Q&A slide).
3. **C. Content methodology gaps** — fundamental concepts missing in initial draft that user had to flag: attention matrix concept (matrix vs linear), end-to-end flow schema (words ↔ vectors ↔ LLM), embedding space introduction before similarity.
4. **D. Designer-added content despite explicit «No Extra Content Rule»** — VERIFY-DAY-OF markers leaked to visible body (s16, s27); LO codes (LO4, LO7) visible to students; § cross-references visible.
5. **E. Artifacts sync gap** — pptx/pdf лежали в `/tmp/lec02-wt` worktree only, не в main repo; user openеd lec-04.pptx by mistake; chapter.md not synced until fact-checker complained.

**Net cost:** initial estimate 1 sub-iteration after Phase 8 → actually 6 sub-iterations. User feedback rounds: target 1 → actual 5.

**ROI of fixes:** if methodology issues here are addressed BEFORE Лекция 3 starts → estimate 3-4× speedup on subsequent lectures (Lec-2 took ~15 hours, Lec-3+ target ~4-5 hours after lessons).

---

## Timeline of user feedback rounds

**R1 (post-Phase 8 GATE B v1):**
> «ты потерял содержание и промежуточные слайды с тем как по нему идем/подзаголовками, некоторые иллюстрации непропрорционально сжаты, квадранты плохо читаются, есть англицизмы типа accuracy, есть кривые переносы слов когда верхняя строка сдвинута налево от второй. короче очень сыро перепроверяй и улучшай. и начальный слайд не понятно о чем... это должен быть хук, а сейчас на отвали сделано»

7 issue categories — substantial polish needed despite all 5 critics having approved with polish.

**R2 (post-Phase 8.6 GATE B v3):**
> «нахрена этот хедер сверху везде?! посмотри как было сделано в лекции 1. надо только на промежуточных слайдах. многие иллюстрации по прежнему сжаты вертикально, нет иллюстраций»

Designer's solution (top progress bar on every slide) was wrong — should have referenced Lec-1 first.

**R3 (post-Phase 8.7 GATE B v4):**
> «где слайд с содержанием? убери футер на титуле»

Missing lecture-map (Lec-1 has s02a) + cover footer redundant.

**R4 (post-Phase 8.8 — wrong feedback for lec-04):**
> [13 пунктов по медицинской лекции]

User opened wrong PPTX (lec-04 in main repo тоже присутствует) — symptom of artifacts sync gap.

**R4 corrected:**
> «1 strawberry test устарел... 2 убери "Подумайте 15 сек"... 3 не хватает фразой что это BPE — компромисс... 4 [s10 cosine] нужна иллюстрация с векторами + отдельный слайд про пространство... 5 [s11] убрать, defer Lec-3... 6 [s12] reformulate + word↔vector schema... 7 матрицу внимания пропустили! 8 докинь 5-10 картинок»

8 substantive content gaps — these should have been flagged at PLAN critique stage by methodology-critic, not 5 phases later.

**R5 (post-Phase 8.8 GATE B v5):**
> «1 начальная часть - введение и убери там Открытие Hook + recap + центральный вопрос. 2 сделай отдельный слайд QA как в лекции 1»

Section label rename + dedicated Q&A slide (Lec-1 has s31 standalone Q&A) — last polish round.

**Pattern:** all 5 rounds caught issues that:
- A) Were Lec-1-pattern deviations (R2, R5 Q&A)
- B) Were content methodology gaps (R4 — attention matrix, flow schema, hook outdated)
- C) Were designer extras / synchronization issues (R1 anglicisms, R3 cover footer)

Critics didn't catch ANY of these — all 5 critics gave APPROVE-WITH-POLISH on v1.0 Phase 7.

---

## 5 categories of failures (detailed)

### A. Git infrastructure brittleness

**Symptoms:**
- Branch `issue-74-lec-02-llm-internals` repeatedly switched back to `issue-73-lec-04-medicine-production` mid-session (caught by `git branch --show-current` 7+ times)
- Lec-04 commits (`9529839`, `aa4567d`, `6d91e26`) landed ON issue-74 branch (via lec-04 agent doing `git checkout issue-74` mid-work)
- 3 of 5 Phase 7 critics reported «slides/*.md, deck.yaml, chapter.md missing» — files existed на disk but not visible to agent (likely .git index out of sync with branch HEAD they read)
- Phase 8 first 2 designer attempts halted with «file not found»
- Required manual `git update-ref` 4 times to recover

**Root cause:** Shared `.git` folder between parallel session (lec-04) and current session (lec-02). When parallel agent does `git checkout`, it affects main worktree's HEAD which is what other agents read via `git branch --show-current` and file system.

**Resolution that worked:** `git worktree add --detach /tmp/lec02-wt 981fb36` — separate working directory с own HEAD, immune to parallel session checkouts. After Phase 8.5 onwards — no more contention.

**Cost:** ~2 hours wasted in Phase 7-8.5 area + 3 retry attempts of Phase 8 designer.

### B. Visual design pattern drift (Lec-1 not referenced)

**Symptoms:**
- Designer added top progress bar to every content slide (R2: «нахрена это везде?»)
- Cover slide had bottom roadmap-bar footer (R3: «убери футер»)
- Only Раздел 3 had section divider (Lec-1 has dividers for всех 5 sections + s02a map + s31 Q&A)
- Missing lecture-map slide (R3: «где слайд с содержанием?»)
- Missing dedicated Q&A slide (R5: «сделай отдельный QA как в лекции 1»)

**Root cause:** Designer brief in Phase 5 contained palette + motif + slide-types BUT did NOT mandate «read Lec-1 deck structure first». Designer made independent design decisions that diverged from established Lec-1 pattern.

**What Lec-1 had that Lec-2 missed initially:**
- `s02a-lecture-map.md` — 5-card lecture roadmap
- `s10-section3-divider.md`, `s22-section4-boundaries.md`, `s27-section5-divider.md` — section dividers for 3 of 5 sections (Lec-2 had only 1)
- `s31-qa.md` — dedicated Q&A slide

**Cost:** Phase 8.5 + 8.6 + 8.7 + 8.9 — 4 sub-iterations to align с Lec-1 pattern.

### C. Content methodology gaps (caught by user, not critics)

**Gaps user identified in R4:**

1. **Hook outdated (strawberry test).** In 2026, top models reliably answer «3 r in strawberry». Hook fails methodologically. Should have been flagged at PLAN stage (Phase 1) since strawberry was central to plan v1 s07 + payoff §5.3.

2. **Missing attention matrix slide.** Plan + chapter described attention as «distribution» (s14) but never as MATRIX. User: «механизм же не линейный а матричный!» — fundamental concept absent.

3. **Missing end-to-end flow schema.** No slide showed words → tokens → vectors → LLM → vectors → words flow. Plan covered each stage but no synthesizing schema.

4. **Embedding space concept assumed.** s10 used cosine similarity без preceding «what is embedding space?» — vector space dimensions, projection assumptions etc. User: «нужно пояснение, может даже отдельный слайд до этого про пространство».

5. **s11 «3 uses of embeddings» too forward-looking.** Listed RAG application which belongs in Lec-3. User: «defer Lec-3».

6. **s12 framing wrong.** «Semantic search vs full-text» was framed as search comparison; should be framed as «эмбеддинги — фундамент понимания LLM».

7. **Insufficient stock illustrations.** Plan had text-heavy slides без visual support. User: «докинь 5-10 картинок».

**Critics that should have caught these:**
- methodology-critic at plan stage (Phase 1): should have asked «is hook 2026-evergreen? is hook engaging vs just educational?»
- methodology-critic on chapter (Phase 3): «is attention covered as MATRIX? is end-to-end flow shown?»
- presentation-critic on slides (Phase 7): «for embedding section, is vector space introduced before similarity used?»
- student-simulator (Phase 7): «do I (3rd year student) get a sense of full pipeline from s01 to s28?»

**None of 5 critics flagged these.** User-perspective check (R4) caught all 8.

### D. Designer-added content despite «No Extra Content Rule»

**Anti-patterns 16-35 in `notes/decisions.md` should have prevented:**

1. `[VERIFY-DAY-OF]` markers rendered onto visible PNG body for s16 + s27 (Phase 7 P0 issue) — lecturer cue leaked
2. «§5.3 — LO7» visible footer in s24 body (Phase 7 P1)
3. «LO4 — подобрать параметры обоснованно» visible in s20 subtitle (Phase 7 P1)
4. 14 designer-extras across 11 slides: §-numbers, LO codes, forward-refs «→ sNN», «вы здесь» bars outside authorized (Phase 8 fix)
5. Top progress bar on every content slide (Phase 8.6 fix) — designer's «навигация» решение, не в brief

**Why rule didn't work:** Anti-pattern catalog exists в `notes/decisions.md` and CLAUDE.md «No Extra Content Rule». But:
- Brief sent to designer doesn't ALWAYS include explicit grep checklist
- Designer interprets «navigation» broadly when not constrained
- Pre-USER-GATE walkthrough caught some but not all

### E. Artifacts sync gap

**Symptoms:**
- pptx/pdf лежали в `/tmp/lec02-wt` worktree throughout Phase 8.5-8.9
- Main repo `/home/levko/AI-usage-lessons/library/lectures/lec-02/rendered/` initially only had snapshots/, no pptx
- User opened wrong PPTX (lec-04.pptx, parallel session) when reviewing GATE B → gave feedback on wrong lecture (R4 false-start)
- chapter.md not synced until fact-checker complained «chapter.md does not exist»

**User's explicit instruction:**
> «и запрети приходить на ревью слайдов без PPTX и pdf сейчас их нет»

Memory rule saved: `feedback_pre_gate_render_artifacts.md`.

**Resolution that worked:** After each phase commit in worktree → manual `cp` from /tmp to main repo path BEFORE opening GATE.

---

## Patterns observed

### P1. Critics check for problems WITHIN scope; user catches OUT-OF-scope absences

Each critic agent has specific checklist (methodology / fact / visual / consistency). Together they cover ~80% of problems. But:
- **Hook engagement quality** — not in any critic's explicit checklist
- **Concept absences** (matrix, flow schema, vector space) — methodology-critic checks LO coverage but not «what's missing that should be there?»
- **Pattern-deviation from previous lectures** — no critic agent has «Lec-1 reference pattern» loaded

### P2. Iteration cycle inefficiency

After Phase 8 v1.1 each round was Phase 8.X polish (5 sub-iterations). Each round:
- 1 designer spawn (~30-60 min)
- 1 sync to main repo (~3-5 min)
- 1 visual sweep by orchestrator
- 1 USER GATE B presentation
- User feedback received → next round

Total wall-clock from Phase 8 v1.0 to GATE B v6 approval: ~5-6 hours.

**Could have been compressed if:**
- Phase 7 critics had broader checklist (catch Lec-1 pattern deviations, hook engagement, missing fundamentals)
- Plan stage methodology-critic had «pattern compliance» check
- Designer brief had explicit «read Lec-1 first» mandate

### P3. Sequential phases vs concurrent reality

Pipeline assumes sequential: Plan → Chapter → Slides → Speech. Reality:
- 3 lectures (lec-01, lec-02, lec-04) in parallel sessions
- Shared git infrastructure → contention
- Shared agent definitions → agents see all 3 contexts если plain prompts
- Worktree isolation solved git contention but not agent confusion

### P4. Phase 11 «batched revision» worked well

7 P1 + 16 P2 closed в single revision pass (~40 min). Speech-writer agent handled 3-artifact touch points (chapter + slides + speech) competently. This is the right model for polish rounds — not 5 sub-iterations с separate designer spawns each time.

### P5. Glossary lock + WPM hard rule worked

Throughout all 12 phases:
- 17/17 canonical terms preserved (0 forbidden hits в final body)
- WPM ≤95 для всех 36 speech fragments (max 90.5 s21)
- Anti-pattern grep clean («магия LLM», «пайплайн», «Decision tree» = 0 in final body)

These mechanical checks are reliable. Soft checks (hook quality, pattern compliance) need work.

---

## Top-10 action items (prioritized by impact × effort)

| # | Action | Priority | Effort | Files affected | Impact |
|---|---|---|---|---|---|
| **1** | **Add «Lec-1 pattern compliance check»** в methodology-critic (plan) + presentation-designer + presentation-critic. Mandatory read of Lec-N-1 deck structure before designing Lec-N. | P0 | 60 min | 3 agent prompts | Prevents R2, R3, R5 entire categories. |
| **2** | **Hook engagement quality check** в methodology-critic. Add criterion: «is hook 2026-evergreen? does it grab emotionally vs just educate? is it «висит на экране» worthy?» | P0 | 30 min | methodology-critic.md | Prevents R1, R4 hook complaints. |
| **3** | **Missing-fundamentals check** в methodology-critic + presentation-critic. Add explicit questions per section: «attention covered as MATRIX (not just distribution)?», «end-to-end flow shown somewhere?», «vector space introduced before similarity?» | P0 | 45 min | 2 agent prompts | Prevents R4 content gaps. |
| **4** | **Artifacts main-repo sync as USER GATE B precondition** — enforced check in `pre-user-gate` skill. PPTX + PDF must exist в main repo path before GATE opens. | P0 | 20 min | pre-user-gate skill, CLAUDE.md | Prevents wrong-lecture-opened class of user-feedback false starts. |
| **5** | **Git worktree as DEFAULT for multi-lecture production** — when starting Lec-N while Lec-N-1 still in production, mandatory `git worktree add --detach`. Document в tools/lecture-production/README.md. | P0 | 30 min | README + ad-hoc orchestration policy | Prevents branch contention disasters. |
| **6** | **Stock illustrations baseline** в presentation-designer brief. «Aim for 5-10 supportive visual assets across deck» as DoD item. | P1 | 15 min | presentation-designer.md | Prevents R4 «нет иллюстраций». |
| **7** | **VERIFY-DAY-OF / LO codes / § cross-refs grep** в pre-user-gate as mandatory check. Currently text-grep is done but should be ENFORCED with «STOP, fix BEFORE gate» on hits. | P1 | 20 min | pre-user-gate skill | Prevents «designer extras» leaks. |
| **8** | **Single batched revision pattern** для polish rounds. After Phase 7 (or any post-GATE feedback round) — use single agent spawn (book-editor OR speech-writer) doing 3-artifact touches, NOT separate designer/writer spawns. Phase 11 proved this works. | P1 | 30 min | tools/lecture-production/README.md | Compresses 5 sub-iterations → 1-2. |
| **9** | **Anti-pattern grep on chapter v1.X changelog** to catch stale «два токена» — type residuals after fixes. (P2-C-3 in Phase 10 found by consistency-checker but should be auto-flagged.) | P2 | 20 min | consistency-checker.md | Prevents stale facts in self-check questions. |
| **10** | **Production status skill** `/lecture-prod-status N` — shows current state of all artifacts, gates passed, fixes pending. Reduces orchestrator overhead. | P2 | 60 min | new skill | Process visibility. |

---

## Specific agent prompt updates (priority order)

### 1. `.claude/agents/methodology-critic.md` — add 3 new check categories

**ADD section «Lec-N-1 Pattern Compliance Check» (for plan + slides critique modes):**

```markdown
## Lec-N-1 Pattern Compliance Check (ENFORCED)

For any lecture N > 1 — read Lec-N-1 deck structure BEFORE critique:
- `library/lectures/lec-(N-1)/slides/*.md` — slide list
- `library/lectures/lec-(N-1)/rendered/build_lec(N-1).py` — design patterns
- `library/lectures/lec-(N-1)/deck.yaml` — palette / motif

**Mandatory checks:**
- [ ] Lecture-map slide present (Lec-1 had `s02a-lecture-map.md`)?
- [ ] Section dividers для ALL major sections (not just one)?
- [ ] Dedicated Q&A slide at end (Lec-1 had `s31-qa.md`)?
- [ ] Roadmap-bar only on dividers + cover, NOT on every content slide?
- [ ] Same palette + motif locked?
- [ ] Same typography conventions (font sizes, line heights)?

If pattern-divergence found без explicit user authorization → P1 issue «Lec-N-1 pattern deviation: ...».
```

**ADD section «Hook Engagement Quality Check» (plan + chapter critique modes):**

```markdown
## Hook Engagement Quality Check

For lecture opening (s01 / hook slide):

1. **Time-evergreen?** Will hook still work in 12 months? Specific tests (strawberry, math, ROT-13) outdated when models improve. Visualizations / cost-asymmetry / concept-reveal hooks are more stable.

2. **Emotionally engaging?** Does hook surprise / provoke curiosity / create cognitive dissonance? Pure educational facts ≠ hook.

3. **«Висит на экране» worthy?** Hook stays visible during introduction (~1-3 min). Visual richness needed.

4. **Connected to assertion of lecture?** Hook should foreshadow main concept, not standalone fact.

5. **Counter-example check:** Compare draft hook to Lec-1 s01 «AI вокруг нас live demo».

If hook fails any check → P1 «Hook engagement quality». Recommend specific replacement.
```

**ADD section «Missing-Fundamentals Check» (chapter + slides critique modes):**

```markdown
## Missing-Fundamentals Check (per section)

For each major concept introduced — verify dependencies and full-picture presence:

**Attention:**
- [ ] Matrix nature explained (not just «distribution»)?
- [ ] N×N quadratic cost shown?
- [ ] Multi-head mentioned (even brief)?

**Embeddings:**
- [ ] Vector space introduced BEFORE similarity?
- [ ] Dimensions clarified (1536 / 3072 / 12288 etc.)?
- [ ] Training process briefly mentioned?

**Tokenization:**
- [ ] End-to-end flow shown somewhere (words → tokens → vectors → LLM → vectors → words)?
- [ ] BPE compromise nature (alphabet vs vocabulary) stated?

**Sampling:**
- [ ] Distribution → token explicit?
- [ ] Local vs cloud parameter comparison?

For each missing fundamental → P1 «Missing-fundamental: <concept>».
```

### 2. `.claude/agents/presentation-designer.md` — strengthen Lec-N-1 reference + extras prevention

**ADD section «Lec-N-1 Reference Read (MANDATORY)» — before any new lecture design:**

```markdown
## Lec-N-1 Reference Read (MANDATORY before Lec-N design)

Before designing any lecture N > 1 — read these from Lec-N-1:

1. `library/lectures/lec-(N-1)/slides/sNN-*.md` — all slide files (skim for structure)
2. `library/lectures/lec-(N-1)/rendered/build_lec(N-1).py` — Python builder
3. `library/lectures/lec-(N-1)/deck.yaml` — full deck metadata

Identify:
- **Slide types used** (cover, lecture-map, section divider, content variants, Q&A)
- **Navigation pattern** (where roadmap-bar appears, where it doesn't)
- **Typography conventions** (title sizes, body sizes, axis sizes)
- **Section divider design** (font sizes, layout, background number)
- **Cover design** (decorative number, subtitle handling, footer)

**Default rule:** match Lec-N-1 pattern unless explicitly told otherwise. Pattern divergence requires orchestrator approval before applying.
```

**STRENGTHEN «No Extra Content Rule» — add explicit grep checks:**

```markdown
## Pre-render grep (MANDATORY)

Before declaring slide PNG done — run these greps on slide visible_content (NOT speaker_notes):

```bash
# Forbidden in visible body:
grep -nE "\[VERIFY-DAY-OF\]|\[FACT-CHECK\]" slides/sNN-*.md  # 0 hits in body
grep -nE "LO[1-9]|§[0-9]\.[0-9]" slides/sNN-*.md             # 0 hits in body (frontmatter OK)
grep -nE "→ s[0-9]+|см\. s[0-9]+|якорь:" slides/sNN-*.md      # 0 hits in body
```

If grep finds hits в visible content → MOVE to speaker_notes OR remove. NEVER render meta-references onto student-facing PNG.
```

**ADD section «Stock illustrations baseline»:**

```markdown
## Stock illustrations baseline

Each deck должен иметь **5-10 supportive visual assets** beyond functional charts:

- Hero illustrations on cover / hook
- Section divider visuals (icons or stock images)
- Concept-supporting imagery (brain for attention, network for transformer, etc.)
- Decorative-but-semantic icons on payoff cards

NOT just functional charts. Use Lucide/Phosphor/Heroicons (one set) + Unsplash CC0 / Pexels / AI-generated stock.

DoD: minimum 5 supportive illustrations per deck (counted alongside charts + diagrams).
```

### 3. `.claude/agents/presentation-critic.md` — add Lec-N-1 + missing-fundamentals checks

Mirror methodology-critic additions:
- Lec-N-1 Pattern Compliance Check (visual variant)
- Missing-Fundamentals Visual Check («is matrix shown? flow schema?»)

### 4. `.claude/agents/student-simulator.md` — broaden checklist

**ADD question to student perspective:**

```markdown
- **Big picture clear?** Do I as student get sense of full pipeline from s01 to s_last? Are there places where I'm «введён в эмбеддинги без понимания пространства» / «слышу про attention но не знаю что это матрица»?
- **Hook grabs me?** s01 — am I excited / curious / confused? If just «interesting fact» — flag P1.
```

### 5. `.claude/skills/pre-user-gate/SKILL.md` — strengthen pre-GATE-B checks

**ADD as MANDATORY pre-GATE-B sequence:**

```markdown
## Pre-USER-GATE-B (slides) MANDATORY checks

1. **Artifacts in main repo path:**
   - `ls -la /home/levko/AI-usage-lessons/library/lectures/lec-NN/rendered/lec-NN.pptx`
   - `ls -la /home/levko/AI-usage-lessons/library/lectures/lec-NN/rendered/lec-NN.pdf`
   - If either missing → STOP, sync from worktree, re-verify before opening GATE.

2. **Lec-N-1 pattern compliance:**
   - Same slide types present (lecture-map, section dividers for all sections, Q&A)?
   - Roadmap-bar only on dividers (no top-bar on content)?
   - Cover clean (no redundant footer)?

3. **Visual sweep 5 random PNGs:**
   - 5-second test passes
   - Title-body alignment
   - No designer extras (LO codes, § refs, VERIFY-DAY-OF in body)

4. **Speaker notes sample 3 random:**
   - 150-300 words readable text
   - No layout descriptions
   - No «Лектору:» / director cues

5. **Glossary lock grep clean** + anti-pattern grep clean.

If ANY check fails → fix BEFORE presenting GATE.
```

---

## CLAUDE.md updates

### ADD section «Multi-lecture parallel production policy»:

```markdown
## Multi-Lecture Parallel Production (ENFORCED)

When starting Lec-N production while Lec-(N-1) or Lec-(N+k) is still in active production:

1. **Use git worktree isolation** mandatory:
   ```bash
   git worktree add --detach /tmp/lec-NN-wt <base-commit>
   git checkout -b phase-X-Y inside worktree
   ```

2. **Agent prompts must include explicit working directory:**
   - «cd /tmp/lec-NN-wt FIRST»
   - «git branch --show-current should return phase-X-Y»
   - «If branch changes mid-session → STOP, report»

3. **Artifacts sync to main repo BEFORE every USER GATE:**
   - Copy from worktree to `/home/levko/AI-usage-lessons/library/lectures/lec-NN/rendered/`
   - Verify via `ls -la`
   - GATE cannot open without main-repo artifacts accessible

4. **Branch ref management:**
   - After phase commits in worktree → `git update-ref refs/heads/issue-NN-lec-NN <commit-sha>` from main repo
   - This propagates branch HEAD without requiring main worktree checkout

5. **Final merge:** push branch + create PR + merge after USER GATE C.
```

### UPDATE «Anti-Patterns» table — add rows 36-50:

```markdown
| VERIFY-DAY-OF markers visible to students | Strip from visible_content; speaker_notes only |
| LO codes / § cross-refs visible to students | Frontmatter only; never visible body |
| Top progress bar on every content slide | Only on section dividers + cover (Lec-1 pattern) |
| Missing lecture-map slide | Add s02a-style map after cover (Lec-1 pattern) |
| Missing dedicated Q&A slide | Add s29 (or equivalent) standalone Q&A (Lec-1 pattern) |
| Insufficient section dividers (only 1 of 5 sections) | Dividers for ALL major sections (Lec-1 pattern) |
| Outdated empirical tests as hook (strawberry-type) | 2026-evergreen visualization / cost-asymmetry / concept-reveal preferred |
| Missing concept fundamentals (attention matrix, flow schema, vector space) | Missing-Fundamentals checklist in methodology-critic |
| Insufficient stock illustrations (text-heavy deck) | 5-10 supportive visual assets baseline |
| Artifacts only in temp worktree (not main repo) | Sync MANDATORY before GATE |
| Branch contention from parallel session | Git worktree isolation mandatory |
| 5+ user feedback rounds on slides | Phase 7 critics + plan critique broadened to catch BEFORE user |
| Hook «на отвали» (educational not engaging) | Hook engagement quality check at plan stage |
| Designer independent decisions diverging from Lec-N-1 | Lec-N-1 reference read MANDATORY at start of design |
```

---

## Final summary

**What worked well:**
- Phase 11 batched revision (single agent, 3-artifact touch) — efficient model
- Glossary lock + WPM hard rule — mechanically reliable
- Git worktree isolation после Phase 8.5 — completely solved branch contention
- 5 critic agents on slides + 3 on speech — caught most P0/P1 issues
- pre-user-gate walkthrough caught some designer extras

**What needs to change (in priority order):**
1. **Lec-N-1 pattern compliance MANDATORY** — designer + critic + plan stages
2. **Hook engagement quality** as explicit critic check
3. **Missing-fundamentals check** в methodology-critic
4. **Artifacts main-repo sync** as GATE precondition (memory rule exists; extend to CLAUDE.md)
5. **Git worktree isolation default** for multi-lecture parallel
6. **Stock illustrations baseline** in designer brief
7. **Pre-GATE grep enforcement** для designer extras
8. **Single batched revision** для polish rounds (Phase 11 pattern)

**Estimated time savings for Lec-3+ if implemented:**
- 5 feedback rounds → 1-2 rounds
- 6 sub-iterations of slides → 2-3 sub-iterations
- 15h Lec-2 wall-clock → 5-7h Lec-3
- Net savings ~50-60% per subsequent lecture × 15 remaining lectures = ~100 hours saved.

---

**End of reflection.** Action items in `improvements.md`; per-area details in `tools.md`, `workflow.md`, `content.md`, `user-feedback.md`.
