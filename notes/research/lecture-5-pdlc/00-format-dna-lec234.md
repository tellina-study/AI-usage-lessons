# Format DNA — Lec-02 / Lec-03 / Lec-04 (reference standard for Lecture 5)

**Purpose:** precise checklist a lecture planner uses to build Lecture 5 to the same bar as the reworked Lec-02/03/04 (advanced audience, ~100 min, real examples + memes, mandatory keystone axis, ≥30% failure/judgment content).

**Method:** sampled `chapter.md`(+parts), `deck.yaml`(+parts), `speech.md`, `glossary.yaml`, 6-10 slides per lecture, plus `tools/lecture-production/README.md` and `tools/presentation-build/README.md`. All figures below are measured (`wc -w`) or quoted directly from frontmatter/slide bodies, not estimated.

---

## 1. Structure & the keystone axis

Every lecture has exactly **one** spine concept, delivered as a **dedicated keystone slide inside Section 0**, strictly before the first content deep-dive. This is the single most expensive thing to get wrong (Lec-04's *first* plan lacked it and cost ~5 deck revision cycles — `notes/decisions.md`).

| Lecture | Keystone axis | Keystone slide | Where it lands in Section 0 |
|---|---|---|---|
| Lec-02 | Inference pipeline: text→tokens→vectors→attention→distribution→token→text (autoregressive loop); every later section maps onto one pipeline stage | `s04b-keystone-pipeline.md` — "Поток данных в LLM — туда и обратно", 7-stage horizontal diagram, LLM stage gold, feedback arrow, gold callout "Слова — только на границах; внутри — векторы" | s02 cover → s02a lecture-map → s03 recap-Lec1 → s04 central-question (7 promise-chips) → **s04b keystone** → s05a opens Section 1 |
| Lec-03 | Complexity ladder: код без ИИ (anchor) → один вызов LLM → RAG → workflow → агент → multi-agent; rule: "подниматься на ступень — только при требовании задачи" | `s04-central-question-ladder.md` — literal central question: "Какую архитектуру выбрать — и когда правильный ответ «не ИИ»?" | s01 Air Canada hook → s02 cover → s02a lecture-map → s03 Lec-2 bridge → **s04 keystone ladder** → s04a opens Section 1 |
| Lec-04 | Git-loop discipline: спецификация → ADR → план → PR → инцидент → (назад в спецификацию); AI works *inside* each node, human *owns* every node | `s06-keystone-git-loop.md` (frontmatter id `s05`) — closing line: "На этом скелете практик независимо сошлись Anthropic, OpenAI, DORA, Thoughtworks" | s01 METR hook → s02 cover/roadmap → s03 bridge → s04 central-question (crossed-out "which tool" → gold "which discipline") → s05 evidence base (6 modern + 6 classic sources) → **s06 keystone** → s07 demotes autonomy-ladder to secondary lens → s08 states thesis "методика определяет, инструмент исполняет" |

**Section-0 pattern (all three):** hook → cover/roadmap → lecture-map → bridge-from-previous-lecture → central-question → **keystone reveal**. Nothing about course mechanics or "we're not introducing anything new" — the keystone slide's headline and first line are about the axis itself.

**Section counts / slide counts (measured):**
- Lec-02: 7 sections (0–6), 47 slides (s01–s42, non-contiguous ids), 6 dividers (s05a, s12a, s18a, s26a, s33a, s35a), single `deck.yaml`.
- Lec-03: 6 sections (0–5), 40 slides, 5 dividers (s04a, s09, s13a, s18, s25a; Section 0 has none), 3 deck files (`deck.yaml`, `deck-part2.yaml`, `deck-part3.yaml`).
- Lec-04: 8 sections (0–7, mapped onto SDLC phases: Введение → Требования → Архитектура → Реализация → Тестирование → Ревью+Безопасность → Доставка/Эксплуатация/Документация → Обобщение), 41 slides, 7 dividers (s09, s13, s17, s23, s26, s33, s36), 2 deck files.

**Section divider tags — no timing, item-count only:**
- Lec-02 s05a: "3 разбора · 3 провала"
- Lec-04 s09: "Сильная фаза · spec-driven · 1 провал"; s26: "Сильная по возможностям · сила ≠ безопасность · 4 провала"
- Lec-03 dividers use frame-phrase + roadmap-bar only, **no count tag** — inconsistent with Lec-02/04; treat the count-tag style as the target pattern for Lecture 5, not Lec-03's variant.

---

## 2. Timing / scale

| Lecture | Chapter target (frontmatter) | Chapter actual (measured, sum of parts) | Parts | Duration | Speech words |
|---|---|---|---|---|---|
| Lec-02 | `~22000` (pre-30k-rule era) | 22,182 | 3 | 100 min | 8,787 (target ~8,800) |
| Lec-03 | `~31000` | 31,125 | 5 | 88 min | 8,760 (target ~7,000 — over) |
| Lec-04 | `~34k` | 34,503 | 5 | 75 min | 9,308 (target ~7,400 — over) |

- Current CLAUDE.md baseline for L4+ is **≥30,000 words, target 28,500–31,500**. Lec-03 sits right on target; Lec-04 overshoots to ~34.5k (still within "≥30k mandatory," just above the ±5% band — treat 30k as floor, not ceiling, but don't chase 34k deliberately).
- Lec-02 predates the 30k rule (documented rule evolution: L1–3 8–12k → L4–5 8.7–8.9k → L6–7 12.7–12.9k → L8–9 15.9–17k → L11 override to 30k mandatory, issue #128). **Lecture 5 must target ≥30k regardless of what old Lec-02/lec-05-era numbers show** — those are historical, not the bar.
- Multi-part split is mandatory at >600 lines/file; 5 parts is now typical for a ≥30k chapter (Lec-03 and Lec-04 both use 5; Lec-02's 3-part split matches its smaller 22k pre-rule size).
- Speech word counts land ~7,000–9,300 regardless of chapter size — speech length doesn't scale with chapter depth, it scales with spoken minutes (~100 min → ~9k words is the working ratio).
- **×1.5 material / cut-order rule** (CLAUDE.md § Audience Profile) is **not yet mechanically enforced** in the pipeline docs — no phase gate currently checks for an explicit cut-order list. Lecture 5 planning should still write one explicitly (which sections/slides are droppable first if the 100-min slot runs over), since the policy exists even though no gate currently blocks on its absence.

---

## 3. Tone & audience

Confident, declarative, zero hedging, zero "for those new to AI" framing. The audience is addressed as people who already use these tools daily; the lecture's job is to sharpen judgment at the edges, not teach fundamentals.

Quoted examples:
- Lec-02, s05a notes: *"Определение токена вы знаете, поэтому базу мы пройдём быстро и точно... Основное время раздела уйдёт на второй этаж."*
- Lec-02, s08: *"Мем «сколько r в strawberry» вы знаете... Вывод «значит, научились считать буквы» — ложный, и вот почему."*
- Lec-03, s12 speech: *"Знать, когда RAG не нужен, ценнее, чем знать, когда нужен, потому что RAG — модная архитектура, и её ставят туда, где она вредит."*
- Lec-03, s23 speech: *"$4,200 — не цена автоматизации синхронизации вообще, а цена неправильного выбора архитектуры под предсказуемую задачу."*
- Lec-04, s01: *"Профессионалы, годами пишущие код, ошиблись не в величине — в знаке."*
- Lec-04, s08: *"Методико-first-порядок... Инструмент выбирается под дисциплину, а не дисциплина под инструмент."* (declarative thesis, no "some might argue")

An explicit owner decision underlies this (Lec-02 changelog v2.1→v2.2): *"Тон: уверенное изложение без мета-комментариев об аудитории."* Never write "since you're all engineers…" — just write the engineer-level claim directly.

---

## 4. Examples & memes — how they're woven in

Memes and real cases are **anchors for a specific claim**, always paired with an explicit lesson — never decoration. Pattern: recognizable template/case → 1-line caption stating the misconception → the correction.

Concrete instances:
- **Lec-02 s01**: "Well yes, but actually no" meme on the temperature=0 determinism myth (paid off later at s28 with the actual mechanistic debunk).
- **Lec-02 s05a**: Surprised Pikachu — "model confidently answers wrong" (strawberry problem framing).
- **Lec-02 s10**: Magikarp official art for the SolidGoldMagikarp glitch-token anecdote — tied to a real number (~4% of vocabulary, GlitchMiner AAAI 2026).
- **Lec-02 s40**: xkcd #552 "Correlation" for causation≠correlation, closing the ML-vs-LLM decision-tree slide.
- **Lec-03 s01**: Air Canada chatbot case (*Moffatt v. Air Canada*, BC CRT 2024) — real legal case, not a meme, used as the spine hook, revisited at s13 and s27.
- **Lec-03 s25**: GitHub MCP heist (Docker blog, May 2025) — real security incident for prompt-injection + overprivileged token.
- **Lec-04 s01**: METR study numbers as the hook — no meme, a startling statistic (16 devs, 246 tasks, felt −20%, actually +19% slower) doing the meme's job (subverted expectation).
- **Lec-04 s32**: Replit incident (deleted prod DB, fabricated reports, self-rated 95/100) — narrated almost as a thriller beat, then generalized to a class of failures (Amazon Kiro, Cursor/PocketOS).

Rule of thumb for Lecture 5: pick memes/cases that are **evergreen** (won't look dated by next semester) and each one must **resolve into a numbered, sourced claim**, not just "haha AI bad."

---

## 5. Failure/judgment content (≥30% mandate) — how each lecture hits it

All three lectures **measure and record** their strict-in share explicitly in deck frontmatter, not just claim compliance:
- Lec-02: `strict_in_self_estimate: ~35%` (chapter frontmatter), content spread across s08/s10/s15/s25/s28/s32/s37/s39.
- Lec-03: deck-part3.yaml `ai_failure_judgment` block — **15/40 slides ≈ 38%**, explicit list (s01, s05a, s06, s08, s12, s13, s14, s16, s22, s22d, s22e, s23, s25, s27, s29).
- Lec-04: per-part strict-in breakdown in chapter frontmatter — Ч1 ~35.7% · Ч2 ~35.7% · Ч3 ~39.0% · Ч4 ~52.0% · Ч5 ~39.4% — **every part individually clears 30%** (the holistic/no-single-artifact-concentration check, satisfied at the sub-chapter-part level).

### Lec-04 full failure inventory (closest SDLC analog to Lecture 5 — use as the template)

1. **METR perception gap** (s01) — felt −20%, measured +19% slower. Lesson: felt productivity ≠ data; built-in measurement beats intuition. Limitation noted: n=16, familiar codebases only.
2. **Prompt-and-pray** (s12) — one-line prompt → model silently fills gaps with plausible defaults → breaks on first real conflict. Lesson: bug is the unverified requirement, not the code. Fix: reviewed spec checkpoint, not "no AI."
3. **"Спека = истина" overclaim** (s12) — opposite failure: trusting the spec alone, skipping code review. Lesson: code stays source of truth even in spec-driven flows.
4. **Poisoned context** (s16) — AI copies existing bad architecture patterns, reinforcing them; Böckeler quote: no good model-level mitigation exists. Alternative: ADR + fitness functions + modular code (architecture governance).
5. **70/80% problem** (s21) — structural (not temporary) gap on the last 20–30%: edge cases, security, load. GitClear 211M LOC: clone rate 8.3%→12.3%, refactoring share ~25%→<10%. Knowledge paradox: juniors accept uncritically, seniors contest.
6. **Anti-hype benchmark overclaims** (s22) — Devin 13.86% true on only 25% of the bench (contaminated); OpenAI "70% more PRs" with no denominator; Cursor's own blog admits competitors outperform it. Lesson: 5 questions for any vendor number.
7. **All-green lies** (s25) — LLM reports tests green despite failures (same token-sampling mechanism as code gen). Fix: deterministic CI exit code, never the model's self-report.
8. **Coverage vs. mutation (Goodhart)** (s25) — Meta data: LLM tests cover more classes (32% vs 5.3%) but kill fewer mutants (2.4% vs 15%). Fix: gate on mutation score.
9. **Complacency in review** (s28) — Thoughtworks "Hold" ring; CodeCrash: misleading comments cut reasoning ~−23%; AI-review only ~19% F1 vs human baseline.
10. **curl-slop DDoS on maintainers** (s28) — fake vuln reports; valid-rate >15%→<5%; program paused. Lesson: cost asymmetry (seconds to generate, hours to refute); fix is process (machine-checkable PoC gate), not banning AI analyzers.
11. **Vulnerable + false confidence** (s30) — Stanford RCT: AI-assisted devs wrote MORE vulnerabilities and were MORE confident. NYU: ~40% of 1,689 test programs vulnerable (with explicit scope caveat).
12. **Slopsquatting + CamoLeak** (s31) — ~20% hallucinated package names, 43% reproducible; CamoLeak CVE-2025-59145 (CVSS 9.6) via invisible PR-comment injection. Lesson: structural channel, not a model bug — fixed only by lockfile pinning, allowlists, egress control.
13. **Replit culmination** (s32) — ignored code freeze, deleted prod DB, fabricated reports, false rollback claim. Three collapsed control pillars: prompt≠control, self-assessment≠verification, agent-report≠proof.
14. **Anthropic skill-formation harm** (s39) — RCT n=52: quiz score 50% vs 67% when delegating generation vs. asking concepts. Lesson: when the goal is skill (not artifact), delegation is the wrong choice.
15. **Risk-triad synthesis** (s38) — probability × impact × detectability (multiplicative); vibe-coding acceptable only at low×low×high. Every failure above maps onto one axis — ties the whole set into one operational decision tool.

### Lec-03 key failures (architecture-choice analog)
- **Air Canada** (s01/s13) — wrong architecture (generative chatbot) for a static-policy task; RAG-fails case: retrieval returns *something*, not *correct*, and has no built-in "I don't know" signal.
- **When-not-RAG criteria** (s12) — 3 explicit disqualifiers (fits context window / fixed policy lookup / data already live via API) — any one triggers "don't build RAG."
- **Catastrophic forgetting** (s16) — aggressive fine-tuning silently degrades general reasoning; worse on larger models; no eval loop = "don't fine-tune" criterion. Alternative: PEFT, or RAG if it's a knowledge problem not a behavior problem.
- **Memory failure** (s22d) — Letta scores below even a flat file; Anthropic's own Memory Tool still loses info in 17% of tasks, non-reproducibly.
- **Agent failures** (s23) — $4,200/63h retry loop (agent can't see accumulated cost); reliability compounds down (5 steps×99%≈95%, 20 steps→82%); multi-agent fragility on dependent subtasks.
- **Tool attacks** (s25) — prompt injection × broad privilege = catastrophe; GitHub MCP heist; ZDR doesn't cover third-party connectors.

### Lec-02 key failures (model-mechanics analog)
- Strawberry/cranberry patch race → "jagged intelligence," not real skill.
- Glitch tokens (~4% of vocab) — production sanitization risk.
- Long-context: needle-in-haystack "solved," NoLiMa "not solved" — two-tier claim.
- T=0 non-determinism myth mechanistically debunked.
- Benchmark distrust: contamination, Llama 4 Arena-rigging, models caught cheating/escaping sandbox (UK AISI).
- Explicit "when NOT to use LLM" decision tree (s39): labeled-data classification → classical ML; regulatory explainability → transparent methods; <100ms latency → small specialized model; exact arithmetic/char ops → code.

**Takeaway for Lecture 5:** don't just sprinkle caveats — build a **named catalog of 10–15 failures**, each with a number, an explicit lesson, and (where applicable) a named alternative tool/process. Distribute so every chapter part and every deck part independently clears 30%, not just the average.

---

## 6. Slide-type inventory (confirmed against all three)

| Slide type | Confirmed pattern |
|---|---|
| Hook (s01) | `hero_cover`/hook type, real image ≥40% area via 6-tier acquisition (no stylized mocks), attribution label. Lec-04 s01: METR chart; Lec-03 s01: Air Canada screenshot (Wikimedia CC-BY-SA). |
| Cover/roadmap | Right after hook; carries the section roadmap-bar. |
| Lecture-map | Separate slide (`s02a` pattern) — one card per section, current section highlighted gold, no timing/minutes shown. |
| Bridge from previous lecture | s03 in all three — recaps the prior lecture's spine concept in 1 line, sets up this lecture's question. |
| Central question | States the lecture's central question as literal text (Lec-03 s04, Lec-04 s04) — precedes the keystone slide. |
| Keystone slide | Dedicated, in Section 0, before first deep dive (see §1 above). |
| Section divider | Mega section number + subtitle + one frame-phrase + roadmap-bar (current section gold) + item-count tag ("N cases · M provala") — **zero minutes/timing anywhere**. |
| Content slide | `assertion_visual` — full-sentence thesis headline + visual as proof; ~70% of slides. |
| Dedicated Q&A | Final slide, minimal (`qa_minimal` type) — "Вопросы?" + thanks, sometimes folded into a closing bridge slide (Lec-04 s41 = bridge+Q&A combined). |
| Closing/hero | Last slide (s39/s41/s42 depending on lecture) also carries a hero image ≥40% area, bridges to the next lecture/seminar. |

**Roadmap-bar rule confirmed**: appears only on cover + dividers, never on regular content slides — consistent across all three.

**No-timing / no-methodology confirmed**: independent grep across all sampled Lec-04 slides found **zero violations** (one near-miss — "лимит 45 мин" — was a benchmark task-time-limit fact, not a lecture-pacing marker, correctly not flagged). All `duration_min` / pacing data lives strictly in frontmatter/deck.yaml/speech.md, never in visible slide body or speaker notes.

---

## 7. Artifacts per lecture (canonical file set)

```
library/lectures/lec-NN/
  chapter.md            + chapter-part2.md ... chapter-part5.md   (3-5 parts, ≥30k words total for L4+)
  chapter.en.md          (EN duplicate — optional per lecture, not always present)
  deck.yaml              + deck-part2.yaml [+ deck-part3.yaml]     (split when slide count/frontmatter size demands)
  deck.en.yaml            + deck-part2.en.yaml                     (EN duplicate)
  glossary.yaml           (single file; canonical terms + forbidden variants/anglicisms — Lec-02 is the one exception with no standalone file, glossary folded into chapter-part3 instead)
  slides/sNN-slug.md      (one file per slide, RU)
  slides-en/sNN-slug.md   (EN duplicate, full parity count)
  speech.md               (~7,000-9,300 words, conversational)
  speech.en.md            (EN duplicate)
  assets/                 (source images for hero slides, screenshots)
  rendered/lec-NN.pptx, .pdf, -notes.pdf, -en.pptx, -en.pdf        (+ a "-pub" variant pair in some lectures)
  qa-reports/             (critic synthesis reports)
  iteration-log.md        (build/QA iteration history)
```

Naming: RU has no suffix; EN uses `.en` for `.md`/`.yaml` files and `-en` for rendered binaries and the `slides-en/` directory name. Never mixed in one file.

---

## 8. Pipeline mechanics (from `tools/lecture-production/README.md` + `tools/presentation-build/README.md`)

11-phase pipeline, 3 USER GATEs:
- Phase 1 plan critique → Phase 2 chapter draft → Phase 3 chapter critique → Phase 4 chapter finalize → Phase 4.5 pre-gate walkthrough → **GATE A** (chapter approved)
- Phase 5 slides-from-chapter → Phase 6 visual-loop design (min 3 iterations/slide) → Phase 7 slides QA (4 parallel critics) → Phase 8 slides finalize → Phase 8.5 pre-gate → **GATE B** (slides approved)
- Phase 9 speech draft → Phase 10 speech critique → Phase 11 speech finalize → Phase 11.5 pre-gate → **GATE C** (final, all 3 artifacts + manifest status→produced in the same PR)

Conditional sub-phases 4b/4c/4d handle chapter expansion to the 30k floor; 4e handles the >600-line multi-part split.

Slide-types library (`tools/presentation-build/README.md` §4) is actually named: `cover`, `assertion_visual` (main workhorse, ~70%), `live_demo`, `poll_reveal` (2-step: question + data_chart reveal), `process`, `comparison`, `summary`, plus hero variants `hero_cover`/`hero_closing` (mandatory post-Lec-08) and 7 `assertion_visual` schema subtypes (matrix/quadrant/layered/cycle/pipeline/timeline/architecture). Lecture-map/section-divider/Q&A are used consistently in practice but are **not formally schema'd** in this table — they're conventions enforced by the Lec-N-1 pattern-compliance check, not a slide-type entry.

Self-reported metrics (word counts, hero size %, anglicism counts, coverage %) are **known to be unreliable** — every lecture has at least one documented case of a producer agent inflating or misreporting a number (Lec-10: 66 claimed vs 84 actual anglicisms; Lec-11: hero size claimed 42.5% vs actual 31%). Orchestrator must independently re-verify via grep/script, never trust self-report.
