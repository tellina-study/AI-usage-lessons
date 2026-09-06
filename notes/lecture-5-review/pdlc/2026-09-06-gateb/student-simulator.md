# Student-simulator review — Lec-05 «AI-продукт: полный жизненный цикл»

Дата: 2026-09-06. Роль: студент 3 курса ИУ6, вайбкодит, работает в ИТ, НЕ имеет опыта в продуктовом менеджменте. Смотрел `rendered/snapshots/slide-01..56.png`, слушал (читал) `speaker_notes` из соответствующих `slides/s*.md`.

Slide↔file order used (per `rendered/build_lec05.py`): 01 s01, 02 s02, 03 s03, 04 s04, 05 s05, 06 s06, 07 s07, 08 s07b, 09 s08, 10 s09, 11 s10, 12 s11, 13 s12, 14 s13, 15 s13a, 16 s14, 17 s14b, 18 s15, 19 s16, 20 s17, 21 s18, 22 s19, 23 s20, 24 s21, 25 s21b, 26 s22, 27 s23, 28 s24, 29 s25, 30 s26, 31 s27, 32 s28, 33 s28b, 34 s29, 35 s30, 36 s31, 37 s32, 38 s33, 39 s34, 40 s35, 41 s36, 42 s36b, 43 s37, 44 s38, 45 s39, 46 s40, 47 s41, 48 s42, 49 s43, 50 s44, 51 s44b, 52 s45, 53 s46, 54 s47, 55 s48, 56 s49.

## 1. Understanding — what landed clearly, where I got lost

Landed clearly (no re-read needed):
- s01 (hook paradox), s02/s03 (cover + loop map), s05/s06 (keystone loop + asymmetry) — the loop metaphor and "cost vs trust asymmetry" is crisp and repeatable.
- s08/s09 (Customer Dev + Mom Test) — "there are no facts inside the office" and the good/bad question example land immediately.
- s15 (double diamond), s19 (heuristics = linter for UX) — the linter metaphor is genuinely great for this audience.
- s22/s26 (feature flag → canary → staged rollout, framed as "valve not switch") — direct bridge to what we already know from CI/CD.
- s29/s34 (randomization = causality, pass@k vs pass^k chart) — the chart with two diverging curves is one of the clearest visuals in the whole deck.
- s37 (SLI/SLO/error budget) — good bridge from known SRE vocabulary to the AI-specific gap.
- s54 (deconstructing "95% failure" into 60%→20%→5%) and s56 (final loop + 8-question checklist) — excellent closing payoff, ties back to s01 hook exactly.

Where I got lost or had to stop and think:
- **Slide 3** (`s03-lecture-map-loop`): the hexagon nodes are floating boxes with no visible connecting lines/arrows between them — it does NOT read as a loop the way slide 2's hexagon or slide 56's hexagon do. I had to take the speaker's word for "this is a loop, not a list" because the picture doesn't show it. Direct visual contradiction with the text: "Лекция — это петля, а не список" but the diagram looks exactly like an unconnected list of 6 boxes.
- **Slide 4** (`s04-bridge-lec4-central-question`): the "code cycle nested inside product cycle" idea is described as nesting, but visually it's two side-by-side boxes with a lot of empty space in the big one — doesn't read as "one is inside the other."
- **Slide 35** (`s30-base2-experiment-traps`, "Три вопроса ловят все восемь ловушек"): three unexplained jargon terms (SRM, peeking, Twyman's law) each get only a 4-6 word gloss. As someone with zero experimentation background, I could tell these were important but couldn't reconstruct what SRM actually means from the slide alone — I'd need the speaker note (which does explain it) but the slide itself under-explains for a first-timer.
- **Slide 44** (`s38-ai-llmops-agentops`, "Трейсинг ловит дрейф"): the header text overlaps slightly with one of the magnifying-glass icons over "Langfuse" — minor visual glitch, momentarily distracting.
- **Slide 46** (`s40-failure-zillow-drift`): the bar chart mixes units — top bar is in thousands ($80K), bottom bar in millions ($304-408M) — on first glance the two bars look comparable in scale, and I had to read the axis footnote twice to realize they're not the same unit. The explicit number labels rescue it, but a skimming student could misread this as "$80M vs $304M."
- **Slide 49** (`s43-synthesis-section5`, "Эксплуатация — точка, где петля замыкается"): this is a **rendering bug**, not just unclear content — the "Измерение" (Measure) node at the bottom of the hexagon is missing/cut off, hidden behind the bottom yellow callout box. The two lines from Support and Build converge into empty white space with no node and no label. This needs a fix before GATE.

## 2. «Простыми словами» (ELI5) slides — do they help?

Yes, consistently. s07b, s14b, s21b, s28b, s36b, s44b all follow the same three-box template (Что это / Зачем / Ментальная модель) and each one gives me, the weaker half of the audience, a plain-language anchor before the jargon starts. Standouts:
- s07b: "внутри офиса нет фактов" — memorable, sets up the whole Discovery section.
- s21b: "кран, а не рубильник" (valve not switch) for rollout — very clear mental image.
- s28b: explains randomization in one paragraph better than some textbooks.
- s44b: correctly previews the capstone payoff without spoiling it.

None of them felt too vague or "too obvious" for what they're doing — they're short (appropriately) and don't repeat content that's about to be covered in depth. My only note: the left-hand icon box on these slides (e.g. s08, s17, s25, s33, s42, s51) has a lot of unused white space — visually a bit unfinished/sparse compared to the busier right-hand column, but this is a design/polish note, not a comprehension problem.

## 3. Memes — do they land?

Mostly yes, and several are genuinely excellent:
- **s01** "This is Fine" dog — apt for the hook paradox.
- **s02** "One does not simply" (Boromir) — good, "you cannot just turn assembly into value."
- **s07** Distracted Boyfriend (team looking at friends' opinions instead of real users) — perfect fit.
- **s13** Surprised Pikachu applied to the NNG 3/7 vs 7/7 result — great, the check/x row makes the point land even without the meme.
- **s16** Drake — well-applied to double-diamond ("jump to solution" vs "right problem first").
- **s21** "Is this a pigeon?" applied to "is this an accessible interface?" — one of the best meme-content matches in the deck.
- **s24** Expanding Brain applied to code-writing evolution — very on-target for this technically literate audience.
- **s30** Balloon-catch-fail meme for "0%→100% in one step, skipping canary" — excellent, visually explains the failure mode without needing the caption.
- **s32** Woman-yelling-at-cat ("metric grew!" vs "is the effect real?") — clean fit for the Measure divider.
- **s41** Disaster Girl ("dashboard is green" while house burns) — great fit for silent-drift/observability theme.
- **s50** Pablo-waiting-style meme ("waiting for ROI") — creative but slightly more obscure a reference; still works as "waiting."

One meme is a **real tonal risk**, not just a style note:
- **s22** (`s19-failure-character-ai`): the clown-makeup transformation meme sits directly next to a case where a 14-year-old died by suicide after months of engagement with an AI companion. Every other meme in the deck is applied to an abstract mechanism or a corporate/financial failure — this is the one case where the meme is paired with a real minor's death. Even though the meme's literal point ("we added the protection makeup only after the tragedy") is coherent, the format reads as flippant next to a fatality, and stands out uncomfortably compared to the more serious/sober treatment given to other failures (e.g., s31/47's dollar-figure sobriety). I'd flag this for the orchestrator to reconsider — either swap the visual for something non-meme (e.g., a plain timeline like s15's Watson slide) or confirm this was a deliberate, owner-approved choice.
- **s45** (`s39-ai-limits-silent-drift`, Hide-the-Pain-Harold): weaker than the deck's other memes — both panels show the same smiling face, so there's no visual contrast to anchor the "everything looks fine on the surface" point, and the caption text is small. Not offensive, just the least effective meme in the deck.
- **s38** (Facebook "Change My Mind" meme correcting the "anger was weighted higher" misconception): functional but more inside-baseball; a student not already primed with the myth may not immediately get why the guy is "changing minds."

## 4. Boredom / attention

Attention holds well through most of the deck — the divider→ELI5→base→AI→limits→failure rhythm is consistent and the failure cases are genuinely gripping (the dollar figures and stark headlines do a lot of work: "$62M and zero patients treated," "$440,000 report with fabricated quotes," "10 of 10 journalists got the same illegal advice").

Where attention could drop:
- **Slide 35** (three-question / eight-traps slide) is the densest, most jargon-heavy slide for someone with no experimentation background — three technical terms in one slide with minimal explanation. This is the most likely point where a weaker student mentally checks out.
- **s33/s34/s39** (Facebook MSI, Med-PaLM/Mata v. Avianca, macro-reality slide) — three slides in a row each built around "the commonly told story is wrong, here's the corrected version." Intellectually this is one of the deck's best features (models fact-checking discipline), but three "well, actually" corrections back-to-back risk feeling repetitive rather than building momentum, especially for a student who didn't know the myth in the first place and now has to hold both the myth and the correction in their head.
- **s52** (portfolio funnel with generic placeholders "X₽ to Y₽, N tickets, M weeks, owner Ivanov") reads flatter than the rest of the deck, which is otherwise full of concrete real numbers — this one slide feels like a template rather than a worked example.

Strongest slides for holding attention: s01, s13 (Pikachu), s21 (pigeon), s30 (balloon), s37 (SLI chain), s41 (disaster girl), s54 (95%-myth deconstruction), s56 (closing loop + checklist).

## 5. Keystone (loop + cost/trust asymmetry) — got it?

**Yes.** s05 (three independent people drawing the same diagram — Deming/Boyd/Ries) is a strong, memorable justification for why the loop is a structural property and not a fad framework. s06's three-row table (Build: cost→0, Measure/Learn: cost same/trust down, Observe/Orient: faster but more attackable) is exactly the right level of abstraction and gets referenced constantly and correctly through the rest of the deck (every section divider explicitly names which arrow AI cheapened vs which stayed human). By the time I reached s43 and s49, the callback to keystone was completely legible and satisfying — s56's version of the loop hexagon (with visible connecting lines and "человек в центре") is what s03's loop diagram should have looked like from the start.

The one weak point is purely visual, not conceptual: **s03's loop diagram doesn't visually loop** (see §1), so the very first time the keystone shape is shown, the picture undercuts the claim. By s05/s06 the concept is rescued verbally and visually, but a sharper first impression would help.

## 6. Failure cases — do they teach "when NOT to use AI"?

Yes, consistently and rigorously. Every failure case in the deck follows the same disciplined pattern: mechanism tied to the specific phase → lesson → operational criterion → alternative. This is far more useful than a simple "AI messed up" story. Standouts:
- Synthetic users (NNG 3/7 vs 7/7) and IBM Watson ($62M, 0 patients) — both teach "synthetic source accepted as validated ground truth" as one class of failure, explicitly named as such.
- Character.AI vs iTutorGroup — deliberately paired as two different failure classes (missing safeguard vs. hard-coded harmful rule), and this contrast is genuinely pedagogically sharp.
- Google AI Overviews vs McDonald's — mirror-image failures (skip the canary entirely vs. correctly kill after a long pilot) — very effective paired teaching.
- Zillow, Air Canada, Klarna/NYC MyCity — correctly separated into Measure vs Support/Operate failures, each with a distinct operational lesson (calibration was fine, monitoring wasn't; you own every bot answer; throughput metrics need a guaranteed human fallback).
- MIT "95%" and Just Walk Out — land especially well because they close the loop back to the opening hook (s01) and explicitly demonstrate the "denominator/definition/conflict-of-interest/traceability" fact-checking skill the whole lecture is trying to instill.

The self-correcting fact-checks (Facebook didn't specifically weight anger; Med-PaLM chemo story isn't traceable; Mata v. Avianca was ChatGPT not Harvey) are valuable but clustered three-in-a-row (§4) — consider spacing them or flagging explicitly as "we're now doing three myth-corrections in a row" so the pattern itself becomes the teaching point rather than accumulating fatigue.

## 7. Dual audience calibration

For me (weaker half): the ELI5 slides do their job, and the "простыми словами" pattern is predictable enough that I know where to look for the plain-language anchor each section. The densest point for me was slide 35 (SRM/peeking/Twyman in one slide) — everything else was paced fine, including the SRE/CI-CD material which leans on things I already half-know from engineering.

A strong practitioner peer would likely find the classical-base slides (Customer Dev four steps, Double Diamond, SLI/SLO/error budget, feature-flag/canary/rollback) too slow if they already have PM/SRE experience — but per the lecture's own framing ("most of you have never seen these as formal disciplines"), that pacing is deliberate and probably correct for this specific audience's actual gap (strong engineers, weak on product-process formalism). The AI-specific material (pass@k vs pass^k, Goodhart/reward hacking, CC/CD agency ladder, Guardian Agents) is pitched at a good level for both halves — dense enough to reward the stronger half, explained enough not to lose the weaker half.

## Meme-got-it / ELI5-got-it / Keystone-got-it summary

- ELI5 slides: **Yes** — help comprehension, right length, no vagueness complaints.
- Memes: **Mostly yes** — several are excellent (s01, s13, s21, s24, s30, s32, s41); one is a genuine tonal-risk flag (s22, Character.AI clown meme next to a minor's death); two are weaker/less effective (s38, s45) but not harmful.
- Keystone: **Yes, got it** — clear by s06, consistently reinforced, strong payoff at s49/s54/s56. Only ding: s03's loop diagram doesn't visually loop, which is a rendering/design issue, not a conceptual one.
