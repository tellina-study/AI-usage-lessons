---
title: "Lecture 5 — Arc / Meme / Layout audit"
date: 2026-09-07
scope: "library/lectures/lec-05/rendered/snapshots/slide-01.png … slide-56.png + slides/s*.md speaker_notes"
method: "Direct vision inspection of all 56 rendered PNGs + full read of speaker_notes/frontmatter in slides/*.md. Slide-number↔file mapping reconstructed from rendered/build_lec05.py build order (deck.yaml/deck-part2.yaml alone omit the 7 sNNb ELI5 slides)."
---

## Slide-number ↔ file map (for reference)

01 s01-hook-paradox · 02 s02-cover-roadmap · 03 s03-lecture-map-loop · 04 s04-bridge-lec4-central-question ·
05 s05-keystone-loop · 06 s06-keystone2-asymmetry · 07 s07-divider-discovery · 08 s07b-discovery-eli5 ·
09 s08-base-customer-development · 10 s09-base2-mom-test · 11 s10-ai-discovery-tools · 12 s11-ai-limits-discovery ·
13 s12-failure-synthetic-users · 14 s13-failure-fabricated-research · 15 s13a-failure-ibm-watson ·
16 s14-divider-design · 17 s14b-design-eli5 · 18 s15-base-double-diamond · 19 s16-base2-heuristics-design-system ·
20 s17-ai-design-tools · 21 s18-ai-limits-nondeterministic-ux · 22 s19-failure-character-ai · 23 s20-failure-itutorgroup ·
24 s21-divider-build-launch · 25 s21b-build-launch-eli5 · 26 s22-base-mvp-release-mechanics · 27 s23-ai-build-review-bottleneck ·
28 s24-ai-launch-control-transfer · 29 s25-ai-limits-review-not-scaling · 30 s26-failure-google-ai-overviews ·
31 s27-failure-mcdonalds-drive-thru · 32 s28-divider-measure-experiment · 33 s28b-measure-eli5 ·
34 s29-base-controlled-experiment-oec · 35 s30-base2-experiment-traps · 36 s31-ai-evals-as-experiments ·
37 s32-ai-limits-goodhart · 38 s33-failure-facebook-msi · 39 s34-failure-benchmark-not-reality · 40 s35-synthesis-section4 ·
41 s36-divider-support-operate · 42 s36b-support-eli5 · 43 s37-base-sre-support-ops · 44 s38-ai-llmops-agentops ·
45 s39-ai-limits-silent-drift · 46 s40-failure-zillow-drift · 47 s41-failure-air-canada · 48 s42-failure-klarna-nyc-mycity ·
49 s43-synthesis-section5 · 50 s44-divider-governance-roi · 51 s44b-governance-eli5 · 52 s45-base-portfolio-governance ·
53 s46-ai-operating-model · 54 s47-failure-macro-reality · 55 s48-failure-just-walk-out-matrix · 56 s49-keystone-payoff-checklist-qa

---

## AXIS 1 — Narrative arc

### Verdict: arc HOLDS end-to-end, verified good. No missing bridges, no ordering defects, no orphan sections. Keystone is actively re-invoked at 4 later checkpoints, not just planted and forgotten. Two soft spots below are polish, not structural gaps.

### Slide-by-slide arc trace

- **s01 (hook):** paradox stated cleanly — "недели→часы" (Anthropic) vs "~95% pilots return nothing" (MIT) — with explicit "payoff s47" deferred-open-loop instruction in frontmatter, and speaker_notes literally say "мы вернёмся к нему в самом конце." Strong open loop.
- **s02 (cover):** re-scopes from Lecture-4 (code cycle) to Lecture-5 (product cycle), states the 6-section roadmap. Clean bridge.
- **s03 (lecture-map loop):** reframes the 6 sections as one closed loop (discover→build→measure→learn→decide→discover), explicit return-arrow Governance→Discovery. This is the structural device the whole lecture hangs on.
- **s04 (bridge from L4):** nests L4's code-loop inside the Build segment of the L5 product-loop — correct scale relationship, and states the lecture's **central question** ("что стало настоящим узким местом, когда ИИ обнулил стоимость сборки") that s06/s35/s43/s53/s55/s56 all answer pieces of. This is the actual thesis statement of the lecture, and it is placed correctly (Section 0, before section 1).
- **s05 (keystone-1, loop):** 3 independent-origin loop formalisms (PDCA/OODA/BML) converge on one shape — establishes the loop is structural, not a course artifact. Also plants a Chekhov's gun (single-loop vs double-loop / reward-hacking foreshadow) that **pays off exactly** at s32 (Goodhart's law / reward hacking slide explicitly reads as the s05 double-loop payoff).
- **s06 (keystone-2, asymmetry):** the actual analytical instrument of the lecture — cost/trust asymmetry per loop-arrow (Build≈free, Measure/Learn=trust drops, Observe/Orient=faster-but-more-attackable). Explicitly axis_slide:true. This is the thesis the 6 sections repeatedly cash out.
- **Sections 1–6, structural pattern hold:** each section follows divider → ELI5 "простыми словами" overview → classical base ×2 → AI capability → AI limits → failure case(s) → (sections 4–6 add an explicit synthesis slide). This pattern is followed with zero deviation across all 6 sections — a real strength; nothing breaks the through-line.
- **Keystone re-invocation checkpoints (the asymmetry thesis is NOT "asserted and forgotten" — it is paid off repeatedly):**
  - s27 (+200% code volume, only 16% PRs get substantive review) — direct numeric proof of the s06 "Build→free, review doesn't scale" claim.
  - s32 (Goodhart's law / reward hacking) — direct payoff of the s05 double-loop foreshadow.
  - s35 (Section-4 synthesis) — title literally re-quotes s06 ("Измерение = стрелка, которой ИИ снизил доверие") and shows the eval/guardrail stack sitting *on top of*, not replacing, classical A/B — this is the asymmetry thesis stated as a conclusion.
  - s43 (Section-5 synthesis) — loop diagram again, "Наблюдать, интерпретировать, решать — эти шаги остаются человеческими... даже когда исполнение почти бесплатно" — same asymmetry thesis in operations language.
  - s53 (operating-model maturity) — "Узкое место сместилось с технологии на операционную модель" — the answer to s04's central question, backed by 5 independent analyst sources.
  - s55 (checklist matrix, 6 columns = 6 sections × "что ИИ меняет / что остаётся классика") — collapses the whole lecture into one matrix using the s06 vocabulary verbatim.
  - **s56 (closing):** explicitly resolves the s01 paradox — "Сборка бесплатна — дефицит теперь: суждение, а не исполнение" — with an 8-item pre-flight checklist. This is a genuine, non-hand-wavy payoff, not just a recap slide.
- **s54 (MIT 95% debunked):** important and correctly placed near the end — reframes the *hook's own MIT statistic* (60% explored → 20% piloted → 5% success = 25% success **among those who reached pilot**, not "95% failure" of everyone). This directly interrogates the s01 hook's own claim, which is intellectually honest and strengthens rather than undercuts the arc — but it lands only 2 slides before the very end (s54 of 56), quite late relative to how prominently the "~95%" figure was used to open the lecture.

### Arc gaps / fixes (both minor — no REVISE-level structural break found)

1. **[P2 — pacing/emphasis]** The MIT-95%-debunk (s54) is the single most important payoff of the s01 hook (the hook's own headline number turns out to be a mis-citation of "25% success among those who piloted," not "95% failure overall") but it arrives very late (slide 54/56) and is visually just one card among three on a busy slide. **Fix:** either (a) foreshadow at s01 with a one-line "[we'll debunk this number later]" cue (already present in speaker_notes but not visible on slide), or (b) promote s54's core reframe visually — it currently competes for attention with a MIT campus stock photo and a 4-question sidebar; the actual "60%→20%→5%, i.e. 25% not 95%" bar chart should be the dominant visual, not one-third of the slide.
2. **[P3 — cosmetic]** s04's "Цикл продукта" comparison box is visually the weakest carrier of the central-question payload (see Axis 3 for the layout defect) — the load-bearing thesis statement of the entire lecture sits in a visually underweighted box. Not an arc defect per se, but the arc's key sentence deserves better visual weight than it currently gets.
3. **[P3 — no fix required, note only]** Sections 1–3 each end on a "failure" note (2 failures) while sections 4–6 explicitly add a "synthesis" slide before moving on (s35, s43, and implicitly s55 for section 6). This asymmetry is intentional per the "2 базы · N провала" tags visible on each divider (2/3/2/2/2/2 — governance divider says "2 провала · развязка" instead of "N база"), and works fine dramatically (early sections build appetite, later sections start summarizing) — flagged only so it's confirmed deliberate, not an oversight.

---

## AXIS 2 — Memes

### Full meme inventory (56 slides scanned; only 15 carry an actual internet meme template — the rest use plain icons/diagrams per Axis 3 notes)

| Slide# | id | Meme template used | Lec-2 collision? | Internal dup? | Size | Caption fit | Verdict |
|---|---|---|---|---|---|---|---|
| 01 | s01 | **This Is Fine** (dog in burning room) | **YES** (lec-02 used this-is-fine) | — | Good (~45% width) | Weak: "this is fine" = denial-while-disaster; the s01 claim is "build is cheap, but 95% capture nothing" — a paradox of *effort without payoff*, not denial of an ongoing catastrophe. Tonal mismatch on top of the collision. | **REPLACE** |
| 02 | s02 | **Boromir / "One does not simply"** | No | No | Moderate-small (~30% width) | Good: "One does not simply take-and-turn build into value" fits the cover's roadmap framing well | **KEEP** |
| 07 | s07 | **Distracted Boyfriend** | No | No | Good | Good: team ogling "friends' opinion" while "real users" walk by — sharp fit for Discovery-divider's "informal validation vs real research" point | **KEEP** |
| 13 | s12 | **Surprised Pikachu** | **YES** (lec-02 used pikachu) | — | Moderate (~30% width, ~55% height of its box) | Weak-moderate: caption is fine (synthetic panel "changes everything," real users say "far-fetched") but Pikachu's "shocked" affect doesn't map cleanly onto a 7/7-vs-3/7 statistics contrast | **REPLACE** |
| 16 | s14 | **Drake** (disapprove/approve) | No | No | Good (large, ~55% width) | Good: "jump straight to a solution" (reject) vs "problem first" (approve) is a textbook Drake use-case | **KEEP** |
| 19 | s16 | **Bernie Sanders "I am once again asking"** | No | **YES — dup #1 of 2** (also implicitly listed at s09 by owner, but actual second use is not present there; real duplicate is none within the deck — see note) | **Small — ~165×220px in a 2000×1125 canvas, <10% of slide area** | Good/clear: "I'm once again asking [for a live user test]" fits "heuristics ≠ substitute for testing" perfectly | **ENLARGE** (fit and caption are fine; the owner's "мемы оч мелкие" complaint is confirmed exactly here) |
| 21 | s18 | **"Is this a pigeon?"** | No | No | Good (~40% width) | Good: "AI interface generator" mislabeling a non-accessible UI as "an accessible interface?" is a clean fit for the meme's "is this X?" misclassification joke | **KEEP** |
| 24 | s21 | **Expanding Brain** | **YES** (lec-02 used expanding-brain) | — | Good (large, ~40% width, tall) | Good fit (escalating brain-glow = code-writing automation escalating from manual→autocomplete→agent→"build≈free") but still a collision | **REPLACE** |
| 30 | s26 | **Balloon Popping ("Boy about to pop girlfriend's balloon")** | No | No | Good (~30% width) | Good: "Google jumped straight to 100% rollout" vs "canary at 1%" — the popping-balloon anticipation fits "about to blow up in public" | **KEEP** |
| 32 | s28 | **Woman Yelling at Cat** | No | No | Good (~35% width) | Good: "metric went up!" (yelling woman) vs "is the effect real?" (confused cat) is an on-the-nose fit for the Measure-divider's causality theme | **KEEP** |
| 38 | s33 | **Change My Mind** | No | No | Good (~30% width) | **Weak (confirmed, matches student-simulator flag):** "Change My Mind" is a debate-provocation format (controversial opinion inviting pushback); the actual claim ("Facebook amplified all 5 reactions ×5, not just anger") is a settled factual finding, not an opinion up for debate — format/content mismatch | **REPLACE** |
| 41 | s36 | **Disaster Girl** | No | No | Good (~30%, tall) | Good: "product in prod 24/7" (burning house) / "but the dashboard is green" (smiling girl) — sharp, well-matched | **KEEP** |
| 45 | s39 | **Hide the Pain Harold** | No | No | Good (~28% width, 2 panels) | **Weak (confirmed, matches student-simulator flag):** Harold's meaning is "smiling to hide personal suffering"; the caption "all metrics green while user trust has been dropping for weeks" is a monitoring-gap claim, not a hidden-suffering-behind-a-smile claim — connection requires an extra inferential step vs. the sharper matches elsewhere (Disaster Girl, Woman-Yelling-Cat) | **REPLACE** |
| 50 | s44 | **"Waiting Skeleton" / old man on a swing waiting** | No | No | Good (3-panel, ~48% width) | Good: "waiting for ROI... from the AI pilot" — a genuinely strong fit for the governance-divider's "waiting for return that (may) never come" | **KEEP** |

**Note on the owner's original list vs confirmed inventory:** the owner's list named "s09 bernie" and "s44 sad-pablo" — direct inspection shows **s09 has no meme** (icons only) and the actual second Bernie-style slide the owner may have had in mind does not exist as a duplicate; **Bernie appears exactly once, at s16**. **s44 uses a "waiting/old-man" template, not sad-Pablo.** No true internal duplicate was found in the final 15-meme inventory (the "bernie ×2" collision the owner flagged does not reproduce against the current render — worth a quick owner re-confirm in case an earlier build had a second Bernie that was already fixed).

### Collision / dedupe summary

- **3 confirmed Lecture-2 collisions to replace:** s01 (this-is-fine), s13/s12 (pikachu), s24/s21 (expanding-brain). A 4th collision template named by the owner, two-buttons, does **not** appear anywhere in lec-05 — nothing to fix there.
- **No internal duplicate found** in the current render (the suspected "bernie ×2" did not reproduce; only one Bernie instance exists, at s16/s19).
- **2 confirmed weak fits** (independently corroborating student-simulator): s33/s38 (Change My Mind) and s39/s45 (Hide the Pain Harold).
- **1 confirmed undersized meme:** s16/s19 (Bernie) — visually the smallest of the 15, well under half the area of comparable memes elsewhere in the deck (Drake, Disaster Girl, Distracted Boyfriend all run 40–55% slide width; Bernie runs under 10% of slide area). This is the concrete instance behind the owner's "местами мемы оч мелкие" note; the other 14 are all reasonably sized.

### Suggested replacement templates (avoiding this-is-fine / pikachu / expanding-brain / two-buttons, avoiding new duplicates against the other 14 kept memes)

| Slide | Replace | Suggested new template | Why |
|---|---|---|---|
| **s01 (hook)** | This Is Fine | **"Two paths" fork / "the math ain't mathing" astronaut-gun format, OR "Galaxy-brain size comparison inverted" is already used (expanding brain, being replaced) — best fit is actually "Spider-Man pointing at Spider-Man"** (two identical-looking things — "cheap to build" AND "no value captured" — pointing at each other, both true, neither cancels the other) — captures "two facts simultaneously true, seemingly contradictory" far better than This-Is-Fine's denial framing. Alternative: **"Always Has Been" (astronaut with gun, realizing a long-standing truth)** — "wait, it's always been about the last mile, not the build?" / "always has been." | Directly matches the *paradox-of-two-simultaneous-truths* structure of the s01 claim, which This-Is-Fine (denial-of-single-disaster) does not. |
| **s13/s12 (synthetic users)** | Pikachu | **"Two Buttons" is excluded — use "NPC wojak / Confused math lady" or better: "Galaxy Brain" is excluded (=expanding brain) — recommend "Trade Offer" meme (two-panel: 'you get 7/7 synthetic approval' / 'I get 3/7 real approval and it's the one that matters')** or simpler: **"Reaction: Skeptical Fry (Futurama 'Not sure if X or Y')"** — "not sure if synthetic panel is a breakthrough or just agreeing with itself" | Keeps the "two verdicts, one truth" contrast without reusing a lec-02 template. |
| **s24/s21 (build/launch divider)** | Expanding Brain | **"Escalating" alternative: subway Wojak-style "increasingly buff" progression is same joke family — safer pick: numbered "Power Levels" bar-chart-style meme is redundant with existing charts. Recommend "This is Brilliant, but I like this" (two-panel preference-flip)** contrasting "write code by hand" (dismissed) vs "sborka ≈ free" (preferred) | Preserves the escalation joke without reusing the exact lec-02 template. |
| **s33/s38 (Facebook MSI)** | Change My Mind | **"Math checks out" (calculator-lady / "the math is mathing") or "Galaxy-brain" excluded — best: "Corporate Needs You to Find the Difference" (Spot-the-difference meme)** — "corporate needs you to find the difference between these 5 reactions" / "they're the same picture" (all weighted ×5) | Directly dramatizes the "all 5 reactions were boosted equally, not just anger" finding — a factual reveal, not a debate-provocation, matching the Spot-the-Difference format's own logic. |
| **s39/s45 (silent drift)** | Hide the Pain Harold | **"Woman Yelling at Cat" is already used at s28 — avoid dup. Recommend "Submarine sonar ping meme" or, simpler and evergreen: "This is Fine" would fit PERFECTLY here (green dashboard while trust burns) — but it's now freed up if s01 is replaced. If s01 keeps a different template, route This-Is-Fine here instead**, since "everything is labeled fine while it quietly isn't" is exactly This-Is-Fine's actual meaning (unlike its current forced use at s01). | This is the single best fix in the whole set: This-Is-Fine's actual semantic meaning (calm/green surface while disaster is real) is a **perfect** match for "dashboards stay green while trust has been dropping for weeks" — better than its current s01 placement. Recommend swapping This-Is-Fine from s01 → s39, and using the Spider-Man/Always-Has-Been suggestion for s01 instead. |

### Enlarge

- **s16/s19 — Bernie ("I am once again asking")** — increase to at least 30–35% of slide width (in line with Drake/Disaster-Girl/Distracted-Boyfriend sizing) so it isn't visually the smallest meme in the deck relative to its neighbors.

---

## AXIS 3 — Layout / verstka

### Confirmed known issue

- **s04 ("Цикл продукта" comparison box) — CONFIRMED large empty upper-left void.** The outer "Цикл продукта (Лекция 5)" box only contains a small nested "Цикл кода (Лекция 4)" card in its upper-right and a one-line icon+caption at the very bottom; roughly 45–50% of the box's vertical space (upper-left quadrant) is blank white/pale-blue with nothing in it. **Fix:** either (a) add a compact visual of the 6-segment loop (reuse the s03 icon-loop at small scale) in the empty upper-left quadrant so "Цикл продукта" is *shown*, not just named, or (b) shrink the outer box to hug its content and let the central-question callout box below grow to fill the reclaimed space (this slide carries the lecture's thesis sentence — see Axis 1 note — and deserves the strongest possible layout, not the weakest).

### Deck-wide structural pattern: large bottom-of-slide voids

The single most common layout defect in this deck, present on **at least 27 of the 56 slides**, is a large empty band (typically 20–40% of slide height) at the bottom of the slide, below the last content box. This recurs in two flavors:

1. **All 7 "простыми словами" (ELI5) slides** (s07b/08, s14b/17, s21b/25, s28b/33, s36b/42, and s44b/51 renders — i.e. slide# 08, 17, 25, 33, 42, 51) share one template with a fixed-height icon card on the left and 3 stacked info-boxes on the right; the template leaves 25–30% of vertical space empty below both columns on every single instance. **Fix once, apply everywhere:** either grow the 3 info-boxes' internal padding/line-height to use the freed space, or add a 4th "Пример" (example) mini-box under the icon card, since all 7 ELI5 slides currently look identical in their emptiness.
2. **Many `case_study` / `base` / `ai` content slides** (confirmed on slide# 04, 05, 08(loop icons), 09, 11, 12, 14, 15, 17, 20, 21, 22, 23, 26, 27, 28, 29, 33, 34, 42, 43, 44, 51) leave 15–35% of vertical space empty below the yellow/callout box at the bottom, because the two/three-column card row above does not extend the full available height. This is not fatal (no overlap, no cramping) but it reads as unfinished/sparse compared to the denser, fully-balanced slides (e.g. s06, s09/s10 process-diagram slides, s35, s49, s55, s56). **Fix:** either enlarge card row height by ~20–25% deck-wide, or add a consistent 4th footer element (e.g. a one-line source/citation strip) to absorb the space uniformly — should be a single template change, not per-slide.

### Other distinct defects (not the systemic void)

| Slide# | Defect | Fix |
|---|---|---|
| 18 (s15, Double Diamond) | Text overlap/cramping: "Расширяем проблему" sits very close to/overlapping the diamond's upper vertex; "Сужаем: одна проблема" crowds the lower vertex — both text blocks are tightly boxed inside a shape not really sized for 2 lines of centered text | Widen the diamonds ~15%, or move the "Расширяем/Сужаем" labels outside the diamond outline (as side annotations) rather than centered inside it |
| 28 (s24, launch control-transfer v1/v2/v3) | The v1/v2/v3 stacked cards (ordered v3 top → v1 bottom) sit flush left while the "CC/CD vs CI/CD" sidebar box floats high with a large gap below it, misaligned against the stack's bottom edge | Either bottom-align the sidebar box with the v1 card's bottom edge, or move its content to vertically center against the 3-card stack |
| 52 (s45, portfolio funnel) | The narrow "профинансированы" box (bottom of the funnel) is visibly narrower than "гейт 1"/"гейт 2" above it, forcing the label to wrap awkwardly onto 2 lines for a single word split mid-phrase ("профинансиро-ваны") | Either widen the bottom box to match the funnel taper more gracefully, or shorten the label ("Профинансировано") and keep it on one line |
| 04 | (see "Confirmed known issue" above — largest single void in the deck, and on the highest-stakes slide) | See fix above |

### Slides confirmed clean / well-balanced (no notable defect)

s02, s03, s06, s07, s10 (mom-test 2×2), s13/s13a, s16, s19, s24 (mostly, minor sidebar issue noted above), s25, s30, s31, s32, s35, s36, s37, s38, s39, s40, s41, s45, s46, s47, s48, s49, s50, s53, s54, s55, s56.

---

## Priority summary (top items if only fixing a subset)

**Arc (P2/P3 only — no P0/P1 found):**
1. Promote/foreshadow the s54 MIT-95%-debunk payoff — currently underweighted for how central the s01 hook statistic is.
2. Strengthen s04's visual weight — it carries the lecture's central question in its weakest-designed box.

**Memes (P1 — collisions + weak fits, should fix before next use of this deck):**
1. Replace 3 Lecture-2 collisions: s01 (this-is-fine → recommend routing to s39 instead, use Spider-Man/Always-Has-Been at s01), s13/s12 (pikachu), s24/s21 (expanding-brain).
2. Replace 2 weak fits: s38/s33 (change-my-mind → Spot-the-Difference), s45/s39 (harold → freed-up this-is-fine, semantically much stronger here).
3. Enlarge 1 undersized meme: s19/s16 (Bernie) to ~30-35% slide width.

**Layout (P1 — systemic, one template fix cascades to 27+ slides):**
1. Fix the ELI5-template bottom void (7 slides, one shared template).
2. Fix the general card-row-leaves-bottom-empty pattern (~20 more slides, likely one shared card-height convention).
3. Fix s04's upper-left void specifically (highest-stakes single slide).
4. Three isolated cosmetic fixes: s18/text-overlap, s28/sidebar-misalign, s52/label-wrap.
