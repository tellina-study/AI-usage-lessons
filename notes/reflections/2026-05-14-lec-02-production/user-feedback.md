# User feedback — Lec-2 production

5 substantive feedback rounds на slides + 1 false-start (wrong lecture opened). All caught categories that critics didn't.

## R1 (post-Phase 8 GATE B v1) — 7 issue categories
- Designer extras (LO codes / § / forward-refs / «вы здесь» bars)
- Anglicisms «accuracy / pipeline / Decision tree» visible in body
- Visual scale issues (10+ slides body <14pt, ~50% canvas occupation)
- Quadrants/cards readability poor
- Line break asymmetry (top line shifted left of bottom)
- Missing intermediate / section transition slides
- s01 hook «на отвали» — strawberry tabular, not engaging

**Critic-blindspot:** all 5 Phase 7 critics gave APPROVE-WITH-POLISH. None caught hook quality OR Lec-1 pattern deviation.

## R2 (post-Phase 8.6 v3) — wrong navigation pattern
> «нахрена этот хедер сверху везде?! посмотри как было сделано в лекции 1»

Designer's «top progress bar on every slide» was independent decision. Lec-1 pattern: roadmap-bar ONLY on dividers + cover. Designer didn't reference Lec-1.

**Lesson:** Lec-N-1 reference read MANDATORY for designer.

## R3 (post-Phase 8.7 v4) — missing structural slides
> «где слайд с содержанием? убери футер на титуле»

Missing s02a-style lecture-map (Lec-1 had it). Cover had redundant bottom roadmap-bar.

**Lesson:** designer should match Lec-1 slide-type inventory by default.

## R4 false-start — wrong lecture
> [13 пунктов про медицинскую лекцию = Лекция 4 от параллельной сессии]

User opened `library/lectures/lec-04/rendered/lec-04.pptx` because lec-04 files присутствовали в main repo working tree (issue-73 branch). Lec-02 pptx сначала жил только в `/tmp/lec02-wt`.

**Lesson:** artifacts main-repo sync as GATE precondition (memory rule saved).

## R4 corrected — 8 content gaps
1. Strawberry hook outdated (2026 models pass)
2. «Подумайте 15 сек» feels classroom-exercise, remove
3. BPE compromise phrase missing
4. s10 cosine without vector illustration + missing «embedding space» slide
5. s11 «3 uses» too forward-looking → defer Lec-3
6. s12 framing wrong (search not understanding)
7. **Missing attention matrix slide** — fundamental concept absent
8. Insufficient stock illustrations

**Critic-blindspot:** methodology-critic checked LO coverage + Bloom level + cross-cutting frames — но did not check «is attention covered as matrix?» / «is end-to-end flow shown?» / «is vector space introduced before similarity?».

## R5 (post-Phase 8.8 v5) — polish
> «начальная часть - введение и убери Открытие Hook+recap+вопрос. Сделай отдельный QA слайд как в лекции 1»

«Открытие» → «Введение» rename. Q&A merged into s28 should be standalone (Lec-1 has s31).

**Lesson:** Lec-N-1 reference would have caught dedicated Q&A pattern at start.

---

## Patterns

1. **Critics check WITHIN scope; user catches OUT-OF-scope absences.** Critics didn't have «is hook engaging?» or «what's MISSING that should be there?» in their checklists.

2. **Lec-N-1 pattern reference missing.** Designer made independent decisions every time. Each Phase 8.X round was «aligning to Lec-1 pattern after divergence».

3. **Content fundamentals gaps.** «Attention matrix» / «embedding space» / «end-to-end flow» — these are domain expertise checks, not in critic prompts.

4. **Artifacts sync gap.** Worktree-only artifacts → user opens wrong file → noise feedback round.

---

## Action implied

→ improvements.md P0-1 (Lec-N-1 pattern), P0-2 (hook quality), P0-3 (missing-fundamentals), P0-4 (sync), P0-5 (worktree).
