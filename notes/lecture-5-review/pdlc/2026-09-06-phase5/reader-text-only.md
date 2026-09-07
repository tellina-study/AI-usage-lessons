# Reader-simulator (text-only) — Лекция 5 deck, Phase 5 pre-render review

**Mode:** text-only (markdown source, no PPTX render yet)
**Persona:** advanced 3rd-year IT-working, vibe-coding student, new to product management
**Scope:** s01–s49 + s13a (50 slides) + deck.yaml + deck-part2.yaml + spot-check vs chapter*.md
**Date:** 2026-09-06

## Overall verdict: **APPROVE-WITH-POLISH**

The deck is structurally strong and unusually disciplined for a first pre-render pass: the base→AI→limits→failure rhythm is genuinely present in every one of the 6 sections, the keystone (s05/s06) lands before any phase dive, baselines/counterfactuals are present on nearly every measurable claim, and the 8-10 sampled facts against the chapter all check out faithfully, including the specific corrections the course cares about (MSI ×5-to-all-reactions not just anger, Bing ≈$100M not "$300M button", Mata v. Avianca = ChatGPT not Harvey, Med-PaLM chemo-for-headache myth explicitly debunked, Guardian Agents correctly scoped as a Gartner category not a confirmed Sber product name). No REVISE-level structural gap found. The issues below are real but polish-tier: a handful of slides where visible-body text is thinner than the speaker notes can support standing alone, one dual-audience framing slide that undersells its "you already know this" hook in the visible body, and a few speaker-notes length/tone checks worth another pass before render.

---

## 1. Minimal text vs. meaning — per-slide thin/thick check

Most slides pass: headline + 2-4 bullet fragments + one gold callout is enough for a student to state the slide's claim without opening notes. Flagged exceptions:

**Slides whose visible body is too thin to stand alone (would need the callout alone parsed correctly, no supporting frame):**
- **s03** (lecture-map-loop): six one-line phase labels + a return arrow is fine as a map, but "Discovery — откуда гипотеза" etc. are too compressed to convey *why* the loop matters without notes — acceptable for a orientation slide, borderline.
- **s28/s36/s44 dividers**: tag lines ("2 базы · 2 провала") plus one narrative-bridge sentence is intentionally minimal per divider spec — these work because dividers are meant to be quick, but s44's "Governance — капстоун, отвечающий на хук-парадокс" alone doesn't hint at *what* governance actually is to a reader who hasn't seen s45 yet. Low risk, this is by design for dividers.
- **s25** (ai-limits-review-not-scaling): visible body is a single asymmetry metaphor + one callout line ("отгрузка без eval-гейта или плана отката — это не скорость, а отложенная цена") — reads well, but the "70% problem" (a genuinely important sub-claim in the notes) is entirely absent from visible body. A student skimming slides only would miss the senior/junior review-quality distinction that's this slide's second half.
- **s43** (synthesis-section5): the visible-body "Support → Product" one-liner is dense shorthand (dataset/guardrail/намерение in one line) — needs the notes to unpack; acceptable as a synthesis slide but on the thin edge.

**Slides that are still too text-heavy for "minimal text" intent (candidates to trim further):**
- **s08** (base-customer-development): 4 numbered steps + a boxed hypothesis format is a lot of reading for one slide; the four CD steps could be reduced to icon+1-word each with detail entirely in notes.
- **s22** (base-mvp-release-mechanics): three bullet lines plus the "явная плашка" overlay text is doing double duty (both dual-audience framing AND content) — slightly crowded for a slide whose whole point is "you already know this, skim it."
- **s37**: similar — SRE flow + explicit callout + error-budget arithmetic in one visible body is a lot of numbers to read live, though it's clearly gated as "you know this, this is the new part."

None of these are "structural gap" territory — they are polish-level trims a designer pass can fix in one round.

## 2. Speaker notes — connected prose check

Sampled all 50; overall notes read as genuine derived-from-chapter prose, not layout description. No "слева график, справа таблица" style violations found anywhere — good discipline.

Length check (target 150-300 words is the *rendered/PNG-mode* rubric, but text-only notes here run longer — 3-4 paragraphs, roughly 220-420 words per slide by rough count) — notes are consistently on the **long side of the range**, especially the case-study slides (s12, s13a, s19, s20, s26, s33, s34, s40, s42, s47 all run 4 paragraphs / ~350-450 words). This is not a violation of the "layout-talk" ban, but flag for the speech-writer/render phase: at 100 slides × ~100 min total, notes this dense per case-study slide will either get cut live or force the lecturer to speed-read. Recommend a trim pass at Phase 9 (post-render) rather than blocking now — text-only mode is supposed to be dense (chapter-derived), rendered mode is where 150-300 word discipline gets enforced.

No notes drift from the chapter that I could find in the sampled cross-references (see §7).

## 3. Meme/visual concepts

All 6 section dividers (s07/s14/s21/s28/s36/s44) + cover (s02) each specify a distinct, non-decorative meme concept that resolves to that section's actual claim, and none duplicate s01's hourglass/leaky-funnel hook or each other:
- s02: circular 6-node loop + lightbulb→gear (intent→operation) — good, genuinely different from s01's split-paradox visual.
- s07: magnifying glass over blank page ("where does the hypothesis even come from") — resolves well.
- s14: pencil sketch turning into a screen — resolves well, evergreen.
- s21: compressing spring (Build arrow visually shorter) — resolves well and reinforces the keystone-2 asymmetry point without repeating s06's art.
- s28: trust-scale tilted toward "доверие ниже" — resolves to the section's actual thesis (Measure = trust, not cost, arrow).
- s36: conductor + orchestra of small ticket/prompt icons — resolves to "product as 24/7 orchestra."
- s44: organizational scale (capital vs portfolio) + compass — resolves to governance-as-navigation.

None flagged as confusing or dated-fragile — all are evergreen geometric/metaphorical concepts, not tied to a specific screenshot or UI that will age out. This is a real strength versus the Lec-8 lesson about stylized mocks; text-only mode can't verify actual image sourcing (that's a Phase 6 designer concern), but the *concepts* as specified are sound and abstract enough to survive real-image acquisition later.

One thing to flag forward to Phase 6 designer: s01 and s49 hero concepts are explicitly cross-referenced as non-duplicative (s01 = split paradox, s49 = closed golden loop with human figure) — this pairing is well-designed as a bookend and should be preserved through rendering.

## 4. Sequence & keystone

Confirmed: s05 (loop, 3 independent sources — Deming/Boyd/Ries) and s06 (cost/trust asymmetry, explicitly marked `axis_slide: true`, NOT counted as strict-in per Decision #78) are presented in Section 0 **before** any phase dive begins at s07. This satisfies the Keystone-axis check in CLAUDE.md's Pre-USER-GATE rule — the axis is given its own dedicated slide pair up front, not deferred or wrapped in scaffold/defensive framing. s04 bridges cleanly from Lecture 4 and states the central question explicitly before the keystone, which is good sequencing (bridge → central question → keystone form → keystone mechanism).

Every section divider (s07/s14/s21/s28/s36/s44) states the section's meaning in one line plus a "N bases · M failures" tag and a narrative-bridge sentence connecting back to the previous section — this consistently orients the student. s43 and s35 (mid-deck synthesis slides for sections 4 and 5) explicitly callback to the keystone loop, and s49 closes by resolving the s01 hook. The loop metaphor (s03) is reused with modification at s05, s06, and s43 (highlighted return arrow) rather than redrawn from scratch each time — good visual continuity per spec, though I can't verify actual visual distinctness until rendered.

No sequencing problems found.

## 5. Base→AI→limits→failure rhythm at deck level

Checked systematically per section against deck.yaml's structural principle:

| Section | Base(s) | AI | Limits | Failure(s) | Complete? |
|---|---|---|---|---|---|
| Р1 Discovery | s08 (Customer Dev), s09 (Mom Test) | s10 | s11 | s12, s13, s13a | Yes |
| Р2 Design | s15 (Double Diamond), s16 (heuristics) | s17 | s18 | s19, s20 | Yes |
| Р3 Build/Launch | s22 (MVP/release mech) | s23, s24 | s25 | s26, s27 | Yes |
| Р4 Measure | s29 (OEC), s30 (traps) | s31 | s32 | s33, s34 | Yes |
| Р5 Support/Operate | s37 (SRE) | s38 | s39 | s40, s41, s42 | Yes |
| Р6 Governance | s45 (portfolio gov) | s46 | (folded into s46/s47) | s47, s48 | Yes, with a caveat |

Every section has its classical-base slide(s) present and on-topic, and every failure is on-point to its phase (no orphan/off-topic failures — even the two "positive" case studies, s27's McDonald's kill-decision and s48's Just Walk Out, are framed as the *phase's* governance/build lesson, not decoration).

**Caveat on Р6:** Section 6 doesn't have a clearly separated "AI-limits" slide the way Р1-Р5 do — s46 (AI operating model) transitions almost directly into s47 (macro-reality failure) without an intermediate "here's where AI-operating-model claims break down" beat. This is likely intentional since Р6 is explicitly the capstone/synthesis section rather than a parallel phase, but it's worth an explicit owner confirmation that the base→AI→limits→failure rhythm is deliberately compressed here rather than accidentally dropped — flag this specifically for methodology-critic Phase 7 sign-off.

## 6. Dual audience framing

The "you know X, here's the difference" framing is explicitly present exactly where the CLAUDE.md context calls it out:
- **s22**: "Явная плашка: примитивы вы знаете из CI/CD. Новое здесь — чьё и по каким критериям решение они обслуживают." — present and clear.
- **s37**: "Явная плашка: on-call/SLO вы можете знать — новое здесь: недетерминированная модель в проде" — present and clear.

Both land well in notes; in visible body s22's framing is a little cramped (see §1) but present. No other slides seem to need this framing (they're mostly genuinely new material for the audience — Customer Development, Mom Test, Double Diamond, OEC, SRE are all called out in speaker notes as "probably your first exposure").

**Weak/jargon-dense spots for the weaker half of the audience:**
- **s31** (evals-as-experiments): pass@k vs pass^k notation is introduced compactly and could read as pure notation-soup on first pass without the notes' explanit — the visible body's "хотя бы 1 успех из k" / "все k успешны" gloss helps, but a weaker student skimming only the body text plus the graph may still not immediately grasp why this matters for reliability claims. Not a blocker — the callout does define both terms — but worth a designer check that the graph itself (pass@k rising, pass^k collapsing) is legible without narration.
- **s24** (CC/CD vs CI/CD): introduces a new acronym pair (CC/CD) that could be confused with CI/CD by a skimming reader; visible body handles this reasonably (explicit "против привычного CI/CD" framing) but this is a term worth glossary-locking carefully (it is — confirmed in glossary.yaml headline_terms as "CC/CD vs CI/CD").

**Too trivial for the strong half:** none found — even the "you know this" slides (s22, s37) earn their place by immediately pivoting to the actually-new content, and case studies throughout carry enough specificity (exact settlement amounts, exact percentages, named sources) to reward a technically strong reader who already knows the AI landscape.

## 7. Faithfulness spot-check (10 slides against chapter)

Sampled: s01 (Anthropic/MIT), s12 (NN/g synthetic users), s13 (Deloitte Australia), s18 (WCAG), s23 (Anthropic 200%/16%), s30 (Bing/$300M split), s33 (Facebook MSI), s34 (Med-PaLM/Mata v. Avianca), s38 (Guardian Agents), s47 (MIT 60/20/5 funnel).

All 10 check out faithfully against chapter.md / chapter-part3.md / chapter-part4.md, including every fact-integrity item CLAUDE.md context specifically calls out as historically fragile:
- **MSI**: slide correctly states all 5 reactions weighted ×5 equally, not just "anger" — matches chapter §4.5 correction exactly, with the same ~1.5-2 year lag detail and the 50%-more-hidden-posts counterfactual.
- **Bing/$300M**: slide s30 correctly separates Bing (~$100M, Kohavi/Thomke HBR 2017) from Spool's "$300M button" (usability finding, not RCT) — matches chapter-part3.md §"Канонический пример" verbatim in substance.
- **Mata = ChatGPT**: s34 correctly attributes to ChatGPT not Harvey — matches chapter's explicit "не Harvey" correction, including the reused "gigiena tsitirovaniya" framing.
- **Med-PaLM**: s34 correctly reports 86.5% MedQA and explicitly does NOT repeat the "recommended chemo for headache" myth (chapter explicitly flags this as unsourced) — instead uses the verified/stronger point about the separate adversarial safety set. Good discipline.
- **Guardian Agents**: s38 correctly frames as "категория Gartner" (Market Guide, Feb 2026), does not claim a confirmed Sber product name — matches chapter's explicit hedge and its `[VFY-day-of]` treatment of GigaCowork as the closest analog (though the slide's visible body doesn't mention the Sber-name-not-confirmed caveat — that's carried only in the deck.yaml `verify_day_of_items` list, not shown to students, which seems correct since visible body doesn't need meta-caveats — see also §5 caveat above).

Baselines/counterfactuals: present on nearly every measurable claim sampled — s12 (3/7 vs 7/7 — same test), s27 (0.7% denominator explicit, contrasted with s26's 100%), s40 ($80k/home loss with unit count basis), s48 (700/1000 vs target 50/1000, explicit 14× framing), s47 (60→20→5 funnel vs raw "95%" framing) — this is unusually disciplined baseline hygiene and a clear strength versus the Lecture 10 lesson that motivated the Baseline/Counterfactual Mandate.

No fact-integrity regressions found in the sample.

---

## Slides too thin to stand alone (visible body only)
- s25 (70%-problem sub-claim missing from visible body)
- s43 (dense one-liner needs notes to unpack)
- s03 (acceptable for orientation slide, borderline)

## Notes that are layout-talk / off-target
None found. All sampled/full-read notes are connected prose derived from chapter content; no "слева/справа" layout description anywhere in the 50 files.

## Meme concerns
None blocking. All divider/cover memes are distinct, evergreen, and resolve to their slide's claim; s01 uniqueness is preserved throughout (no duplication found on any other slide).

## Section-level notes
- Р6 (Governance) compresses the AI-limits beat into s46→s47's transition rather than giving it a dedicated slide — flag for methodology-critic to confirm this is deliberate capstone compression, not a dropped structural element.
- Text-heavy candidates for a further-trim pass at render time: s08, s22, s37 (see §1).
- Speaker notes run longer than the 150-300 word rendered-mode target across most case-study slides — expected for text-only/chapter-derived mode, but flag for Phase 9 trim.
