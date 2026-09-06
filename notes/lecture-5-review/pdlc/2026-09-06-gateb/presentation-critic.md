# Presentation-critic review — Lecture 5 deck (GATE B), 2026-09-06

**Scope:** all 56 rendered PNGs (`library/lectures/lec-05/rendered/snapshots/slide-01.png`…`slide-56.png`), cross-checked against `deck.yaml` + `deck-part2.yaml` + `slides/*.md` + `tools/presentation-build/README.md`.

**Verdict: REVISE**

Structurally strong deck (assertion-evidence headlines, real baselines on nearly every measurable claim, correct fact fixes for MSI/Bing/Mata/Med-PaLM/Guardian all confirmed on-slide), but there are two P0 visual/asset defects, one P0 hero-image gap the team's own iteration-log already flags as unresolved, a pervasive/systemic anglicism ("AI" vs "ИИ") regression across ~15-20 slides, and a repeated small anti-pattern (gold accent-line under divider headings) present on **all 7 dividers**. This is a structural-gap profile, not polish — REVISE, not APPROVE-WITH-POLISH.

---

## P0 (blocking)

1. **s12 "Синт-панель 7 из 7" meme is broken/illegible (slide-13.png).** The top caption text overlaid on the white card ("синт-панель сказала «7 из 7 задач»") is tiny, low-contrast and effectively unreadable at slide scale; the Pikachu image is stretched/cropped oddly and its bottom caption ("реальные — 3 из 7") sits at the very edge of the frame, nearly clipped. This is the flagship meme for Discovery-failure #1 (NN/g synthetic users) and currently fails the "reads clearly" bar outright. **Fix:** rebuild the meme with proper caption sizing/positioning and un-stretched image, or replace with a cleaner two-panel comparison.

2. **s38 (deck s38, LLMOps/AgentOps, slide-44.png) — caption text collides with icons.** The italic line "Трейсинг (камера над каждым узлом): LangSmith · Langfuse · Arize Phoenix · Helicone" is positioned directly behind/through the row of magnifying-glass icons above the process boxes — "Langfuse" and "Helicone" visually overlap the icon glyphs. **Fix:** move the caption above the icon row or increase vertical spacing.

3. **s49/slide-56 (closing/keystone-payoff slide) has no real hero image — violates hero≥40% requirement.** The slide uses a schematic hexagon-loop diagram + checklist, not a photo. The team's own `iteration-log.md` already documents this as an unresolved gap ("Real-image acquisition for s49 (closing hero, ≥40% area) — Band 1 had no [real image]"), i.e., a known, admitted miss, not an oversight to discover. Per the brief's Hero mandate (s01 + closing require ≥40% real image via 6-tier acquisition), this must be fixed before GATE, not deferred. **Fix:** run 6-tier acquisition (og:image / Wikimedia / press release / YouTube thumb / Wayback / image search) for a real closing visual, or get an explicit owner-documented waiver if none can be found.

4. **s01 hero coverage is borderline.** The Anthropic/MIT comic occupies roughly a third of the slide width in the right-hand box — likely under the 40% area bar once the two stat cards on the left are counted as the "primary" content. Recommend measuring actual area and enlarging the comic panel or restructuring so the hero image is unambiguously ≥40%.

---

## P1

5. **Systemic "AI" (Latin) vs "ИИ" (Cyrillic) inconsistency — not a one-off, appears in headline assertions.** Confirmed via direct grep of `slides/*.md` (137 raw hits of standalone "AI" outside brand names) and visually confirmed on slide headlines themselves (not just body text), e.g.:
   - s02 (slide-02): assertion "AI-продукт: полный жизненный цикл…", subtitle "Курс «Осознанное применение AI»"
   - s06 (slide-06): headline "AI меняет стоимость и доверие…", body "AI её не отменяет"
   - s17 (slide-20): headline "AI для дивергенции, человек для конвергенции"
   - s28 (slide-32, divider): headline "Измерение — стрелка, которой AI снизил доверие"
   - s35 (slide-40): floating label "Measure = стрелка, которой AI снизил доверие" (also stray English word "Measure" with no box motif around it — visual inconsistency vs. every other slide)
   - s39 (slide-45): "усилены автономностью AI, не отменены ею"
   - s46 (slide-53) / s45 (slide-52): "Unit-экономика AI-продукта", "У AI-продукта новая переменная"
   - s47 (slide-54): "4 вопроса к любой громкой цифре провала AI", "цифры провалов AI"
   - s48 (slide-55): dark banner "Фаза × что AI меняет × что остаётся из классики", "автономный AI»"
   - s49/closing (slide-56): "Чек-лист «прежде чем делать фазу AI-first»", "AI-продукте"
   
   Meanwhile several other slides already correctly use "ИИ": s10/slide-11 ("используют ИИ"), s12/slide-14 body uses "AI" (inconsistent with its own title which correctly says "ИИ-синтеза"), s42/slide-48 ("только ИИ», «ИИ не работает»). This split shows partial remediation happened but was not applied deck-wide. **Fix:** cascade-of-changes find/replace "AI" → "ИИ" across all slide headlines/body/callouts (excluding brand names: Character.AI, Guardian Agent (Gartner uses "AI" as part of category name — verify), IBM Watson, product names). Also fix the floating unboxed "Measure" label on s35/slide-40.

6. **"Каков денаминатор?" (s47/slide-54) is not a real Russian word.** Correct term is "знаменатель" (denominator). This reads as an anglicism-hybrid typo, worse than a plain English loanword. **Fix:** replace with "знаменатель".

7. **Gold accent-line-under-heading anti-pattern present on all 7 dividers.** Confirmed on s07 (slide-08, "РАЗДЕЛ 1"), s14 (slide-17, "РАЗДЕЛ 2"), s21 (slide-25, "РАЗДЕЛ 3"), s28 (slide-33, "РАЗДЕЛ 4"), s36 (slide-42, "РАЗДЕЛ 5"), s44 (slide-51, "РАЗДЕЛ 6"). This is the explicitly-named course anti-pattern ("decorative gold accent-line-under-heading"). **Fix:** remove the gold underline rule from the divider template; if a visual separator is wanted, use the rounded-box motif instead.

8. **s49/slide-49 (synthesis "Эксплуатация — точка, где петля физически замыкается") — hexagon loop diagram appears cut off at the bottom of frame.** The "Поддержка" and "Сборка" nodes' connector lines converge toward a point below the visible canvas with no visible bottom node — looks like a clipped/incomplete render, distinct from the (already-flagged) s56 closing-slide loop issue. **Fix:** verify the full hexagon renders within the box bounds; increase box height or shrink the diagram.

---

## P2

9. **s10 (slide-11) mixes English labels with Russian on a single content slide:** "Desk research (кабинетное исследование)" and "Reference dataset (эталонный набор)" — the parenthetical Russian glosses are good practice per the anglicism rule (keep-list with inline gloss), but consider leading with the Russian term and parenthetical English for consistency with how other slides gloss terms.

10. **Divider memes are somewhat mixed in creative quality/uniqueness.** s21/slide-24 (expanding-brain meme for Build/Launch) and s50/slide-50 (Narcos-still triptych for Governance) are competent but generic/widely-recycled templates; s28/slide-32 (Woman-yelling-at-cat) and s41/slide-41 (girl-with-fire meme) are stronger, more on-point choices. No outright duplication across dividers was found, satisfying the no-duplication rule, but recommend a pass to swap the two weaker ones for something more specific to the section's exact claim.

11. **s45 (slide-52) meme (old man reacting to laptop, two near-identical frames)** is low-effort/generic relative to the "тихий дрейф" (silent drift) claim it's meant to support — the two frames look almost the same, undermining the "before/after" contrast the meme intends. Consider a clearer two-state contrast.

12. **Minor terminology mix on v3 slide (s24/slide-28):** "CC/CD против привычного CI/CD" box mixes an English acronym gloss ("Continuous Calibration/Development") inline — acceptable as an established technical-jargon exception per keep-list, no action required, flagged for awareness only.

---

## What's strong (do not regress)

- **Baselines/counterfactuals:** essentially every sampled measurable claim carries an inline baseline or denominator (McDonald's 0.7% of ~13,786 restaurants; Google canary 1%→10%→25%→50%→100% explicitly shown; Zillow $304-408M against $80k/home; Just Walk Out 700/1000 vs. target 50/1000; MIT 60%→20%→5% funnel recast as 25% among those reaching pilot). This is a clear, deliberate strength.
- **Fact-integrity regressions all clear:** MSI shown correctly as all-5-reactions-×5 (s33/slide-38); Bing shown as ≈$100M, explicitly disclaiming the "$300M button" myth (s30/slide-35); Mata v. Avianca correctly attributed to ChatGPT, not Harvey (s34/slide-39); Med-PaLM slide makes no chemo claim; Guardian Agent correctly labeled "(категория Gartner)" (s38/slide-44).
- **ELI5 slides (s07b/s14b/s21b/s28b/s36b/s44b)** are clean, genuinely beginner-level, and follow an identical, easy-to-scan template (icon + "Что это" / "Зачем" / "Ментальная модель" cards + gold "простыми словами" chip). No complaints here.
- **No visible timing/methodology/LO-codes/§-refs/[VFY] markers** were found on any visible slide body or speaker-adjacent text in the sampled set.
- **Roadmap bar** correctly appears only on cover (s02) and the 6 dividers, not on content slides.
- **Gold ≥1×/slide** consistently satisfied throughout the sample.
- **pass@k vs pass^k chart (s31/slide-36)** and the **PDCA/OODA/BML three-source keystone (s05/slide-05)** are excellent assertion-evidence execution — clear headline claims backed directly by the visual.

---

## Recommendation

Fix the 3 P0 asset/layout defects (s12 meme, s38 caption overlap, s49 closing hero) plus the P1 systemic AI→ИИ cascade and the 7-divider gold-line removal, then re-run the pre-gate walkthrough (deep latin-token scan + hero check + independent grep) before presenting GATE B.
