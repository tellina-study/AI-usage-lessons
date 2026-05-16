# Phase 7 Synthesis — Slides v1 Critique → Revision Brief для Phase 8

**Date:** 2026-05-13
**Critics:**
- `presentation-critic.md` — REVISE (0 P0 + 8 P1 + 14 P2)
- `student-simulator.md` — APPROVE-WITH-POLISH (0 P0 + 6 P1 + 13 P2)
- `reader-rendered.md` — APPROVE-WITH-POLISH (0 P0 + 6 P1 + 9 P2) — 27/29 self-containedness
- `fact-checker.md` — APPROVE-WITH-POLISH (0 P0 + 3 P1 + 4 P2)
- `consistency-checker.md` — REVISE (1 P0 + 6 P1 + 9 P2)

**Consolidated verdict: REVISE** (2 REVISE; 1 P0). Solid foundation — palette 22/29, motif consistent, assertion-evidence pattern strong, central question chain works, s24 + s11 + s17a/b architectures praised. Revision focuses on convergent multi-critic findings.

---

## P0 (1 issue) — DECISION REQUIRED

### P0-1 — Glossary self-contradiction «medical AI» (consistency-checker D1)

**Issue:** Chapter glossary #1 declares «medical AI» as **forbidden synonym** for AI-диагностика («слишком широко»). Однако chapter (25 mentions) + slides (18+ mentions) использует «medical AI» / «медицинский AI» как legitimate umbrella term (s22, s26, s18 visible content).

**Options:**
- **Option A (Recommended):** Update glossary entry — «medical AI» allowed как **umbrella term** for AI in medicine (broader than AI-диагностика). 0 cascade в slides + chapter. Methodologically cleaner — original «forbidden» caveat was over-restrictive.
- **Option B:** Mass-rename 40+ occurrences in chapter + slides. Heavy cascade.

**Recommended choice:** A.

---

## P1 — must fix в Phase 8 (consolidated cross-critic, prioritized by convergence count)

### Multi-critic convergent issues (фиксим в первую очередь)

| # | Issue | Critics | Severity | Fix |
|---|---|---|---|---|
| 1 | **s05/s20/s27 schematic placeholders вместо real stock photos** (user spec violation: «активно используй иллюстрации из стока, новостей, сайтов и статей») | presentation + student + reader (3×) | P1 critical | Re-fetch Unsplash CC0 URLs already in frontmatter, OR use ImageMagick-generated photoreal mockups, OR remove illustration с note |
| 2 | **s24 Vendor/Operator quadrant position vs notes contradiction** (Vendor placed bottom-left but notes say «high control») | presentation + student + reader + fact-checker (4×) | P1 critical | **Swap Vendor ↔ Operator positions.** Also fix regulator card (student-simulator flagged «high liability на схеме vs не несёт liability в notes»). Critical для РК prep. |
| 3 | **s10 Bayes math inconsistency** — slide visual headline «sens 0.96 / spec 0.93» дают PPV 12% / 85%, но slide shows «PPV ~8% / ~78%» (this corresponds to chapter lower-bound sens 0.94 / spec 0.89) | fact-checker + consistency-checker | P1 critical | Align slide: либо использовать sens 0.94/spec 0.89 (chapter lower-bound), либо update PPV outputs (12%/85%). Recommended: use lower-bound for didactic consistency. |
| 4 | **Cream-yellow card backgrounds** (s14 Rentosertib/DSP cards; s17a June 2025 pivot; s17b Phase 1 pivot; s18 EU column) — designer-added secondary palette | presentation | P1 | Replace с Ocean surface `#F4F7FA` + gold accents only |
| 5 | **s17b RED «Phase 1 DISCONTINUED»** — anti-pattern #3 (red palette violation) | presentation | P1 | Navy bold (#21295C) + Ocean rounded box |
| 6 | **s10 confusion matrix red/green/yellow palette** — anti-pattern #3 | presentation | P1 | Recolor to Ocean (teal/navy/gold) per palette lock |

### Visibility / readability issues

| # | Issue | Critic | Fix |
|---|---|---|---|
| 7 | **s22 truncated bottom** — last «Self-diagnosis at scale» card + bottom callout at/past safe area | presentation | Fix render OR redistribute content (student-simulator P1-3 also recommends split if density overload) |
| 8 | **s06 matrix axes hidden** (Modality/Scope), gold dots непонятны без caption | student | Move axes INSIDE matrix (Schema Readability) + add caption legend |
| 9 | **s09 gold on wrong pipeline stage** («4. Workflow», но assertion = «CV, не LLM») — anti-pattern #21 inconsistent gold-emphasis | presentation | Move gold к stage 2 «Model» OR remove |
| 10 | **s09 «3. Output» text overlap edges** (Grad-CAM italic tight) | presentation | Restructure layout / increase padding |
| 11 | **s11 WIN badge on MASAI row too small at 50% projector zoom** | reader | Increase 1.5× OR move to header |

### Designer-added extras (No Extra Content Rule violations)

| # | Issue | Critic | Fix |
|---|---|---|---|
| 12 | **LO codes visible to students** (s19 «LO4», s26 «LO1/LO2, LO2/LO3, LO3/LO8») | presentation P2 | Remove from visible content; speaker notes only |
| 13 | **Slide IDs visible to students** (s14 «(s12)/(s17a)/(s17b)», s06 «s9-s13 + s15-s17») | presentation P2 | Remove |
| 14 | **«10 мин» timing visible on s19** | presentation P2 | Remove (duration_min только в deck.yaml) |
| 15 | **«(schematic, CC0-style)» caption markers** | student | Remove |
| 16 | **s28 navigation badge 1-2-3-4-K1-6** | student | Verify first appearance в курсе; remove if confusing |

### Other P1 issues

| # | Issue | Critic | Fix |
|---|---|---|---|
| 17 | **s17a missing RU drug discovery context** (chapter §3.3 has 300-word block: Alliance #1 CD137, Alliance #2 Alzheimer, MADD, DiMA) | consistency | Add 1-2 bullet «RU context» card к s17a OR speaker notes addition |
| 18 | **s11 Goh numbers mismatch** — slide «76.3%/73.7%», chapter «76%/74%» | consistency + fact-checker | Round к «76%/74%» в slide (chapter median framing) |
| 19 | **deck.yaml LO mapping sync** — 5 slides need [LO3, LO8] update (s18/s20/s21/s22/s23) | consistency | Update YAML frontmatter |
| 20 | **s11 frame_mapping «LLM pattern»** should be «LLM anti-pattern (augmentation gap)» per plan-v2 | consistency | Update YAML frontmatter |
| 21 | **s22 «Март 2023» NEDA Tessa unanchored date** | fact-checker | Soften к «начало 2023» OR find primary source |
| 22 | **Vocabulary disclaimers missing** для Grad-CAM (s09), DenseNet (s09), SaMD (s08/s18), FVC (s17a), MDR (s18) | reader | Add inline 11pt italic disclaimer на slide |
| 23 | **s23 AI connection прячется внизу** | student | Strengthen visible content: AI training datasets inherit security risk → move к top of slide |
| 24 | **s04 + s07 duplicate FDA cumulative bar chart** — cross-slide redundancy | presentation | Differentiate: s04 как poll-reveal context (smaller), s07 as primary growth chart |

---

## P2 — apply where compatible (~40 items condensed)

- s05/s27 illustration replacement (already P1-1)
- s18 «4 декабря 2024» PCCP date precision (already в chapter; verify slide)
- Сводка arithmetic / time math display polish
- Glossary candidate #25 «Healthcare operator role» visible name consistency
- s06 4-type matrix axes justification в speaker notes
- s14 mid-callback positioning
- s28 Cognitive Agro phrasing exact match per course doc
- ... (see individual critic reports for full lists)

---

## What works WELL (do not disturb)

1. **s10 self-check Q1 PPV calculation** — strongest Apply question (student aha-moment per student-simulator)
2. **s11 augmentation gap Goh JAMA** — main «open-mind moment» per student
3. **s17a + s17b twin timelines paired narrative** — «best teaching pattern лекции» per student
4. **s24 quadrant axes INSIDE + direction-of-scale «◄ low control TECHNICAL CONTROL high control ►»** — textbook-perfect per presentation-critic (despite Vendor swap needed)
5. **Speaker notes contract** — best notes quality of any lecture per reader-rendered (200-450 words, connected prose, 0 layout descriptions, 0 «Лектору» sections)
6. **Cross-references through 2 weeks** — PASS (Lec 1/6/9/14 callbacks все parse for self-study reader)
7. **No 4 млрд руб mosmed claim** — 0 mentions in slides (P0 from Phase 3 correctly propagated)
8. **All 7 key number sets verified consistent** chapter ↔ slides (FDA 1,451, mosmed operational, Rentosertib, MASAI, Obermeyer, Change Healthcare, AlphaFold)

---

## Recommended Phase 8 execution

**Spawn ONE presentation-designer revision pass** addressing все P1 issues выше + selected P2 (No Extra Content extras removal + glossary D1 Option A).

**Estimated revision time:** 1-2 hours wall-clock (mostly s10 redraw, s24 swap, illustration re-fetch, palette fixes).

**After revision:** pre-USER-GATE walkthrough → present USER GATE B.

**Glossary D1 decision:** Recommend Option A (update glossary к umbrella term — methodological cleanup, 0 cascade).

---

## Open items требующие user decision

1. **Glossary D1**: Option A (update umbrella) vs Option B (mass-rename 40+ occurrences). **Recommended A.**
2. **Illustration sourcing**: re-fetch Unsplash URLs (если accessible) OR use ImageMagick photoreal mockups OR pure schematic? **Recommended: try Unsplash fetch first, fall back к photoreal mockup if blocked.**

Other issues can be auto-applied per SYNTHESIS recommendations.
