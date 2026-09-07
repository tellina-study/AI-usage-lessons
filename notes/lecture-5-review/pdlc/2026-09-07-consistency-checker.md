# Consistency Check — Lecture 5 «AI-продукт: полный жизненный цикл — от намерения до эксплуатации»

**Date:** 2026-09-07
**Checked:** chapter.md + chapter-part2/3/4.md · deck.yaml + deck-part2.yaml + slides/s*.md · speech.md + speech-part2.md · glossary.yaml · plan-final.md
**Scope:** cross-artifact assertion coverage, numbers/facts, fact-integrity forms, terminology lock, keystone/structure parity, ≥30% failure-share per artifact, reused-case coherence, s07 nit, orphan references.

## Verdict: REVISE

One P1 structural gap (deck.yaml/deck-part2.yaml never wired in the 6 ELI5 slides that the plan mandated and that speech.md/speaker-notes already fully narrate) plus a handful of P2 polish items. Content-level fidelity (numbers, fact-integrity corrections, terminology, keystone, 13-failure set) is excellent — genuinely APPROVE-CLEAN quality — but the deck-structure/speech mismatch is a real, load-bearing inconsistency that will surface at render time (speech references 12 slides that don't exist in the deck's own slide list/totals), so the artifact set as a whole cannot pass without a fix.

---

## P1 — Blocking

### P1-1: deck.yaml / deck-part2.yaml never wired in the 6 ELI5 slides that plan + speech both treat as canonical
- **Artifacts:** `deck.yaml`, `deck-part2.yaml` (slide lists, `totals`, `ai_failure_judgment.partial_out`) vs. `slides/s07b-discovery-eli5.md`, `s14b-design-eli5.md`, `s21b-build-launch-eli5.md`, `s28b-measure-eli5.md`, `s36b-support-eli5.md`, `s44b-governance-eli5.md` vs. `speech.md`/`speech-part2.md`.
- **Finding:** `plan-final.md` line 18 ("Phase-6 owner additions... +6 слайдов: s07b/s14b/s21b/s28b/s36b/s44b... Итого ~56 слайдов") mandates 6 ELI5 overview slides, one after each section divider. The slide markdown files for all 6 exist, fully written, with frontmatter (`type: eli5_overview`, `duration_min: 1.5` each). `speech.md` frontmatter explicitly claims `derived_from: "...slides/s01..s49b (56 слайдов, включая 6 ELI5-обзоров...)"`, lists all 6 in `slides_covered_part1`/`slides_covered_part2`, and both speech files contain full spoken sections for each (`## [s07b] — ELI5: Discovery простыми словами`, etc.).
  However, **`deck.yaml` and `deck-part2.yaml` — the deck structure source of truth — never list any of the 6 `sNNb` slides** in their `slides:` arrays. `deck.yaml`'s own header still says `total_slides: 50` / `# (~50 слайдов: s01–s49 + s13a...)`, and `totals:` in deck-part2.yaml sums to `slides: 50`, `slide_times_sum_min: 96.4`, with a per-slide duration table that has no entry for any `sNNb`. `glossary_lock`/`ai_failure_judgment.partial_out` lists also omit them.
- **Why this matters:** this is not cosmetic. A renderer building off deck.yaml (the documented source of truth per `tools/presentation-build/README.md`) will produce a 50-slide deck; the speech was written for a 56-slide deck and narrates content (s07b/s14b/s21b/s28b/s36b/s44b) that won't exist on screen. Timing totals are also stale — 6 × 1.5 min = 9 extra minutes not reflected in `total_min: 100` / `slide_times_sum_min: 96.4`.
- **Fix:** add the 6 `sNNb` slide entries to `deck.yaml`/`deck-part2.yaml` `slides:` lists (right after each corresponding divider, per plan), recompute `totals.slides` (→56), `slide_times_sum_min` (+9 → ~105.4, requires re-checking cut-order budget against the 100-min target), add them to `ai_failure_judgment.partial_out` (they're all `partial_out_strict_in: true` per their own frontmatter, consistent with being course-scaffold not in-bucket), and update `total_slides` in the file header comment. This is a deck.yaml/deck-part2.yaml fix only — slides and speech are already correct and don't need touching.

---

## P2 — Polish

### P2-1: s07 divider tag wording — confirmed, not a real drift (matches the "known nit" flagged in the brief)
- **Artifacts:** `deck.yaml` s07 `learning_goal: "Section divider Р1: смысл фазы одной строкой, tag «3 провала»"` vs. slide's visible `## Tag` → `2 базы · 3 провала` vs. other dividers' short form.
- **Finding:** All 6 dividers are internally consistent in form: each `deck.yaml`/`deck-part2.yaml` `learning_goal` states a short "tag «N провала»" gloss, while each slide's actual visible `## Tag` line spells out the fuller "`X баз(ы) · Y провала`" (s07: "2 базы · 3 провала", s14: "2 базы · 2 провала", s21: "2 базы · 2 провала", s28: "2 базы · 2 провала", s36: "2 базы · 3 провала", s44: "2 провала · payoff"). The counts themselves are correct — Discovery genuinely has 3 on-point failures (#1 synth users, #2 Deloitte, #3 IBM Watson via s13a), Support/Operate genuinely has 3 (#9 Zillow, #10 Air Canada, #11 Klarna+NYC). This is just a metadata-gloss-vs-visible-text shorthand difference (deck.yaml's `learning_goal` field is a terse internal label, not meant to be rendered), not a factual drift. **No fix required**, but flagging per the brief's explicit ask — worth a one-line normalization (e.g. drop the "tag" quote from `learning_goal` or make it match the visible string exactly) purely for internal-doc hygiine.

### P2-2: `ai_failure_judgment.share_by_minutes` in deck.yaml carries unresolved uncertainty language into a "locked" artifact
- **Artifact:** `deck.yaml` line 121 — `share_by_minutes: "≈34.5 / ≈92 активных мин ≈ 37.5%... итог указан как диапазон 34-37.5%, точный пересчёт — Phase 7 methodology-critic по факту duration_min слайдов"`.
- **Finding:** Both bounds of the stated range clear the 30% bar, so this doesn't threaten the ENFORCED rule, but the field explicitly defers final computation to a later phase and is written as a range rather than a number — slightly unusual for a "locked" deck.yaml at this stage. Recompute once P1-1's slide/timing fix lands (adding 9 min of non-strict-in ELI5 content to the denominator will slightly *lower* the percentage — worth confirming it still clears 30% after the fix; back-of-envelope: 34.5 / (92+9) ≈ 34.2%, still comfortably over).

### P2-3: minor — `deck-part2.yaml` totals note references a cut-order that predates the ELI5 addition
- **Artifact:** `deck-part2.yaml` `totals.note` cut-order list (s16→s25→s43→s30→s45) doesn't mention the 6 ELI5 slides as a cut-order option, even though they're the most obviously cuttable content (course-scaffold, `partial_out_strict_in: true`, no on-point failure) if Phase 6 render time is tight. Cosmetic — surface if/when P1-1 is fixed and the 105.4-min raw sum needs trimming back toward the 100-min target.

---

## Detailed verification — no other issues found

### 1. Assertion coverage (chapter ↔ slides ↔ speech)
Every slide `assertion` in deck.yaml/deck-part2.yaml traces cleanly to a numbered chapter subsection via `chapter_ref` (`§1.7`, `§4.5`, `§6.3`, etc.), and I spot-checked ~20 of these against the actual chapter text — all accurate, no invented claims on slides, no dropped chapter assertions. Speech follows the identical section order (Р0 keystone → Р1 Discovery → ... → Р6 Governance) with no reordering, skips, or insertions relative to chapter/deck. The keystone payoff (§6.5/s49) closes the same parenthesis opened at the hook (§0.1/s01) in all three artifacts, with matching numbers (25% success-among-piloted, not the misreported "5%").

### 2–3. Numbers/facts + fact-integrity forms — sampled 15 claims, all three artifacts agree, all corrected forms hold
| Claim | Chapter | Slides | Speech | Match |
|---|---|---|---|---|
| Zillow write-downs | $304.4M Q3 / $407.9M FY; ~2000 (~25%) laid off; ~$80k/home loss | identical (s40) | identical (speech-part2 s40) | ✅ |
| MIT NANDA funnel | 60%→20%→5% = 25% success among piloted, not "95% fail" | identical (s47) | identical (s01 hook + s47 payoff) | ✅ |
| Gartner | 782 I&O leaders / 28% fully successful; separate 3400+ survey / >40% agentic cancelled by 2027 — explicitly flagged as **two different surveys** | identical, same "two different denominators" caveat (s47) | identical caveat preserved (speech-part2 s47) | ✅ |
| Klarna | 700 FTE-equiv (2024) → policy reversed (05/2025) → automation grew to 853 FTE-equiv (end 2025) | identical (s42) | identical (speech-part2 s42) | ✅ |
| McDonald's | ~100 of ≈13,786 US restaurants = 0.7% | identical (s27) | identical (speech s27) | ✅ |
| WCAG | 29.0% compliance / 21,880 evaluations; contrast 26.8%, color use 19.2% | identical (s18) | identical (speech s18) | ✅ |
| Bing test | ≈$100M / +12% revenue (Kohavi & Thomke, HBR 2017) — explicitly NOT the "$300M button" (Spool, different case) | identical distinction preserved (s30) | identical (speech-part2 s30) | ✅ |
| Air Canada | $812.02 CAD (Moffatt v. Air Canada, 2024 BCCRT 149) | identical (s41) | identical (speech-part2 s41) | ✅ |
| iTutorGroup | $365,000 EEOC settlement, first-ever AI discrimination settlement, age 55+/60+ | identical (s20) | identical (speech s20) | ✅ |
| Just Walk Out | 700/1000 manual review vs. target 50/1000 = ~14× target | identical (s48) | identical (speech-part2 s48) | ✅ |
| Anthropic PR review | +200% code volume YoY, ~16% substantive human review | identical (s23) | identical (speech s23) | ✅ |

Fact-integrity forms — all four "must not regress" corrections hold identically in all three artifacts:
- **Facebook MSI** = all 5 reactions weighted ×5 equally (not anger-specific) — chapter §4.5, s33 title bar "не только «гнев»", speech-part2 s33 all state the Techdirt-corrected form.
- **Bing ≠ $300M button** — kept as two distinct, explicitly-contrasted cases in chapter §4.2, s30, speech-part2 s30.
- **Mata v. Avianca = ChatGPT, not Harvey** — chapter §4.6, s34 "исправленная атрибуция: ChatGPT, не Harvey" (both in learning_goal and visible body), speech-part2 s34 all consistent.
- **Med-PaLM "chemo for headache" myth excluded** — chapter §4.6 explicitly states it "не прослеживается ни к какому первоисточнику", s34 and speech-part2 s34 both carry the same correction and substitute the verifiable adversarial-eval framing.
- **Guardian Agents = Gartner category, not a confirmed Sber product name** — chapter §5.2/glossary, s38, speech-part2 s38, and glossary.yaml `forbidden: ["Guardian Agents как продукт Сбера"]` all agree; GigaCowork consistently flagged `[VFY-day-of]` as the closest analog, not an equivalence.

No drift found on any sampled number or corrected-attribution case.

### 4. Terminology / glossary lock
Checked glossary.yaml's ~35 canonical terms against usage in chapter/deck/speech. No drift found: "reference dataset (эталонный набор)" used consistently across Р1/Р3/Р4 in all three artifacts; "guardrail-метрика" never conflated with "guardrails/policy-as-code" (kept as distinct glossary entries and used that way); "Double Diamond" consistently presented as *the* framework with Design Thinking as its 5-stage restatement (not two competing frameworks) in chapter §2.1, s15, and speech s15. Forbidden anglicisms (роллбэк, фича-флаг, деплой, дрифт, трейс, инсайт) — none found in visible slide body or speech text in the sampled sections; RU-gloss-on-first-use pattern for canary/feature-flag/guardrail respected.

### 5. Keystone + structure parity
Loop (PDCA/OODA/BML, 3 independent inventors) + cost/trust asymmetry (Build→≈0, Measure/Learn trust↓, Observe/Orient faster-but-vulnerable) keystone is presented identically in chapter §0.4–0.5, s05/s06, and speech s05/s06, including the single/double-loop nuance and its explicit forward-reference to reward hacking in Р4. Base→AI→limits→failure structure is followed in all 6 sections in chapter, deck, and speech with no section skipping the pattern. The 13 on-point failures are the identical set, in the identical phase-order, across all three artifacts: #1 synth users (NN/g) / #2 Deloitte Australia / #3 IBM Watson (Discovery, s12/s13/s13a) · #3(Р2) Character.AI / #4 iTutorGroup (Design, s19/s20) · #5 Google AI Overviews / #6 McDonald's (Build/Launch, s26/s27) · #7 Facebook MSI / #8 benchmark≠reality (Measure, s33/s34) · #9 Zillow / #10 Air Canada / #11 Klarna+NYC MyCity (Support/Operate, s40/s41/s42) · #12 macro-reality / #13 Just Walk Out (Governance, s47/s48). Matches the summary matrix in chapter §6.4/s48 exactly.

### 6. ≥30% failure/judgment share — per-artifact recount
- **Chapter:** frontmatter self-estimate ~40.5% holistic, all 4 parts individually ≥30% (Ч1 ~31.6%, Ч2 ~46.1%, Ч3 ~43.2%, Ч4 ~41.5%). Rough independent spot-check: Part 1 has §1.7/1.8/1.9 (3 full failure sections) out of §0+§1's ~9 subsections — plausible in the low-to-mid 30s by word count given each failure subsection runs long (mechanism + lesson + criterion + alternative). Holistic claim is credible; not recomputed to the word.
- **Slides (deck.yaml `ai_failure_judgment`):** `strict_in_slides` = 14 slides (13 canonical + s13a), `share_by_minutes: "≈34.5/≈92 ≈ 37.5%"` — clears 30% with margin, and per-section distribution is holistic (no single-section concentration: Р1=3, Р2=2, Р3=2, Р4=2, Р5=3, Р6=2 failures). Once P1-1's ELI5 slides are added to the minute denominator (92→~101 with the 9 extra ELI5 minutes, none of which are strict-in), recompute: 34.5/101 ≈ 34.2% — still clears 30%, flagged in P2-2 above for a formal recompute rather than back-of-envelope.
- **Speech:** no formal self-estimate field, but the same 14 case-study sections appear as dedicated `## [sNN]` blocks in speech.md/speech-part2.md, holistically distributed across all 6 sections (never batched into one place), consistent with the deck's per-section distribution. No artifact concentrates failure content in a single place — the holisticity requirement is met.

### 7. Reused-case check (Zillow, Air Canada, Klarna)
All three cases are reframed coherently under the new PDLC/Support-Operate framing, with no leftover finance/retail-specific language. Zillow is presented purely as an Support/Operate concept-drift/circuit-breaker case (not as a "proptech" or "finance AI" case); Air Canada as a support-accountability case; Klarna as a support-automation-metric-design case. Numbers match what's stated in the brief ($304–408M/~2000/25%/$80k for Zillow; $812 for Air Canada; 700→853 for Klarna) exactly, with no corruption found across chapter/deck/speech.

### 9. Orphan cross-references / dropped sections / ordering
Only orphan found is the ELI5 slide set (P1-1 above). No dropped chapter sections in deck/speech — all 6 chapter sections + capstone are represented on slides and in speech in matching order. No broken `chapter_ref` cross-links found in the sampled slides. `glossary.yaml`'s `forbidden_anglicisms` and `notes` are consistent with actual chapter/slide/speech usage.

---

## Summary of required fixes before next gate
1. **P1-1 (blocking):** Add s07b/s14b/s21b/s28b/s36b/s44b to `deck.yaml`/`deck-part2.yaml` `slides:` lists, recompute `totals`, update `ai_failure_judgment.partial_out`, resolve the resulting +9min against the 100-min budget (cut-order or accept ~105min raw with steeper cuts elsewhere).
2. P2 items are optional polish, no blocking action required.

No changes needed to chapter.md/-part2/3/4, slides/*.md content, speech.md/-part2, or glossary.yaml — all are already correct and mutually consistent; only the deck.yaml/deck-part2.yaml structural manifest needs to catch up to what slides + speech already assume.
