VERDICT: REJECT

# Presentation Critic Report — Лекция 8 — 2026-10-21

Reviewed: `library/lectures/lec-08/rendered/snapshots/s01.png`–`s76.png` (all 76, vision),
`library/lectures/lec-08/slides/s01-*.md`–`s76-*.md` (all 76, frontmatter + visible body +
speaker notes), `rework/deck/deck.yaml` + `deck-part2.yaml`, `rework/architecture.md`,
`rendered/iteration-log.md` (the build's own self-check), `chapter.md` + parts (spot cross-ref
for the two detailed cases). Cross-referenced against `library/lectures/lec-07` (immediate
predecessor, same `deckkit` core) for Lec-N-1 pattern compliance.

## Сводка

- Всего слайдов: 76
- P0 issues (блокеры): 1 (deck-wide, affects every slide + both hero slots)
- P1 issues (важные): 5
- P2 issues (мелочи): 4

## P0 — Blocker

### P0-1 — Hero-image rule violated on s01 and s76, and in fact `media` is empty on all 76 slides deck-wide

**Confirmed, not a maybe.** `deck.yaml` totals block states it explicitly: `media: {wired: 0,
needs_media: 60, no_decision: 16}` — zero slides in the entire deck carry a resolved `media`
asset. `s01-cover.md` frontmatter: `media: "" media_needed: "hero, не менее..."`. `s76-voprosy.md`
is a pure three-plate text slide with no image whatsoever (confirmed visually — see below).

**Visual confirmation:**
- `s01.png` — title + one-line subtitle + small gold underline bar on white background. No hero
  image, no full-bleed background, no decorative 200pt+ lecture number (the `hero_cover`
  slide-type spec in `tools/presentation-build/README.md` §4 calls for exactly these elements;
  none present). This is visually indistinguishable from the forbidden "Title+Body universal"
  anti-pattern (#2 in the course catalog).
- `s76.png` — three Ocean-boxed plates ("Три проверки — и вопрос в зал") + no image. No hero,
  no emotional payoff visual, no bridge illustration.

**This is not isolated to the two hero slots.** The build's own `iteration-log.md` says it
plainly: *"Во всей лекции нет ни одной иллюстрации — ни `media_hero` на обложке, ни одной
картинки нигде"* and separately, *"ни один из 76 кадров не объявляет `media`"*. Every one of
the 76 slides is built purely from text, Ocean-boxed "plates," two-column text blocks, tables,
and arrow-connected shape schemes — zero photographs, zero icons, zero charts (no `analitika`
chart-type slide is used anywhere, despite that type existing specifically for this course since
#244). This also breaks anti-pattern #4 in the course catalog ("every slide has ≥1 visual") in
spirit, even though shape-primitive plates technically satisfy "diagrams as shapes."

**Severity justification:** the task's own framing calls this a confirmed blocker, and the
4-level verdict table says any P0 → REJECT. I am not treating this as "maybe acceptable because
the content is abstract" — the hero rule is unconditional for s01/closing per
`tools/presentation-build/README.md` §4 "Hero slide types (ENFORCED, добавлено после Лекции 8
production)" and CLAUDE.md anti-pattern #27, both written explicitly because of this exact
lecture's prior production round. Shipping the rework with the identical gap the rule was
written to prevent is the single most serious issue in this deck.

**Recommendation:** run the 6-tier real-image acquisition workflow (§5.7) for at minimum s01 and
s76 before any GATE; strongly consider at least a handful of supporting images/icons across the
case-study sections (CNET, Coca-Cola, Getty, Lada Chizhova) given the course's established
"5-10 supportive visual assets" baseline expectation — right now this deck has zero.

---

## P1 — Important

### P1-1 — "Keystone" (unglossed English production-jargon) leaks into visible student-facing body text on s71 and s72

`s71-schet-skvoznoy-linii.md`, visible body: *"...и Ряд 2 keystone (нет числа со стороны
классического режима)"*. `s72-vyvod-razdela-sborka.md`, visible body, opening bolded sentence:
**"Keystone входа обещал: узнавание, стоившее доверия бесплатно, станет измеримым вопросом с
деньгами на обеих сторонах."** — confirmed visually on `s72.png`, this is literally the first
line students read under the slide title.

Two separate problems compound here:
1. **Russification/anglicism discipline** — "keystone" is an unglossed English loanword, never
   defined for the audience, in a RU-language lecture deck. It fails the `unique - whitelist = ∅`
   deep-scan standard for narrative body content (it is not a brand name, not a standard CS/AI
   acronym, not a case name).
2. **Scaffold leak** — "keystone" is this course's own internal production-methodology term
   (`architecture.md` §3: "Keystone — предъявляется во Входе..."). It names how the *lecture was
   built*, not a concept from the subject matter (creative-industries trust economics). Exposing
   it to students is the same class of defect as a stray `§4.3` or `LO5` marker bleeding into
   visible text — it belongs in `architecture.md`/`chapter_ref`/planning files, never on a slide
   students read.

**Recommendation:** replace both instances with content language — e.g. "Два ряда, с которых
начался разговор, обещали..." — no Russian lecture should ever need the word "keystone" to make
its own argument.

### P1-2 — No-Timing/No-Methodology: "методическ*" stem appears in speaker notes on s32, s34, s36

Grep of the literal ENFORCED pattern `(методическ|педагогическ)\s*\w+` across all 76 slide files'
`## Заметки лектора` sections returns three hits:
- `s32`: *"и в этом состоит центральная **методическая** находка раздела"*
- `s34`: *"...можно и **методически** необходимо, и именно в этом состоит контринтуитивная
  находка раздела"*
- `s36`: *"Урок здесь **методический**, а не только фактический"* / *"...ровно та **методическая**
  дисциплина, которую курс требует соблюдать"*

Per CLAUDE.md § "No Timing / No Methodology in Slides" and the memory rule
`feedback_speaker_notes_not_timing_exempt` (*only `speech.md` is exempt, not `slides/*.md`
speaker notes*), this pattern is zero-tolerance in `## Заметки лектора`, with no sampling —
I grepped the full set, not a sample.

**Context matters here, in fairness:** reading all three in full (done above), none of them are
the forbidden *pedagogical* meta-commentary the rule targets ("на этом этапе студент должен",
"методическая ценность для курса") — all three are using "методическ-" in the sense of
*research/measurement methodology* (System1's testing methodology vs. CARMA's, the methodology
behind a now-retracted YouTube-thumbnail statistic, a predrelease panel's measurement
methodology). That is a legitimate content register, not a lecturer-to-self teaching note. But
the rule as written is a literal, pattern-based, zero-tolerance gate specifically because context
judgment calls are exactly what let violations slip through in prior lectures — and the Pre-Gate
walkthrough mandate requires 0 hits of this pattern full stop. I am flagging it as P1 rather than
waving it through on my own judgment; whether to accept the "measurement methodology" reading or
require a stem-avoiding rewrite is a call for the orchestrator/owner, not for me to pre-clear.

**Recommendation:** reword the three instances to avoid the "методическ-"/"педагогическ-" stems
entirely (e.g. "это и есть то, на чём стоит разбор" instead of "методическая находка"), which
costs nothing in meaning and closes the literal grep cleanly.

### P1-3 — Lec-7 pattern deviation: zero hero images and zero chart/`analitika` slides, where the immediate predecessor lecture used both

Required Lec-N-1 comparison (this deck is Lecture 8, N>1). `library/lectures/lec-07/rework/deck/deck.yaml`:
- `s01` cover carries `media_asset: "rework/deck/assets/s01-hero-chtenie-mammogrammy.jpg"` — a
  real acquired hero photograph.
- `slide_types` includes `analitika: {count: 9, ...}` — nine slides built around real QuickChart
  diagrams in the course palette (template `templates/kadr-analitiki.md`, §"analitika" in the
  README, added specifically "per owner instruction... use templates with analytics and
  diagrams").

Lecture 8's `deck.yaml` `slide_types` has **no `analitika` entry at all** and, per P0-1 above, no
media anywhere. This is a visible regression from the immediately preceding lecture's own
established pattern, not a stylistic choice — the course's own Lec-N-1 compliance check exists
precisely to catch this kind of silent reversion. Pairs directly with P0-1; flagging separately
because it is a *pattern* finding (process regression), not just a missing-asset finding.

**Recommendation:** before GATE, decide explicitly whether this deck should adopt `analitika` for
at least the numeric-heavy case studies (CNET, Getty, Coca-Cola, cost-collapse table on s71) to
match Lec-7's now-established visual standard, or record an explicit, documented owner decision
to diverge (per CLAUDE.md's own rule: deviation from Lec-N-1 pattern requires explicit
authorization, not silent omission).

### P1-4 — Pacing-math cannot be verified: `timing_min` missing on 13 of 76 slides (all of §4 "Права и лицензирование")

`deck-part2.yaml` totals: `timing_missing: 13` — every slide in section 4 (s38–s50) has no
`timing_min` in its frontmatter, so the deck's own summed total (`sum_timing_min: 58.75`)
silently treats 13 real slides as 0.0 minutes. `architecture.md` §5 commits this lecture to an
88-minute content budget inside a 100-minute slot, with section 4 alone planned at 13 minutes
("Что не сокращается... разбор раздела 4 (Getty-UK, теперь подробный по решению владельца)").
Adding architecture's planned 13 minutes back in gives ≈71.75 actual minutes against an
88-minute target — still under budget, but the point is this cannot currently be verified from
the deck's own data, which is exactly the kind of cross-artifact pacing-math check the
Pre-USER-GATE walkthrough rule requires.

**Recommendation:** backfill `timing_min` on s38–s50 before GATE so the deck's own totals are
trustworthy, then re-check the 88-minute budget holds.

### P1-5 — Content density: 35 of 76 slides exceed the 140-word visible-text ceiling (build's own blocking finding, not mine)

`iteration-log.md`'s self-check reports this as a **blocking** `[плотность]` warning on 35/76
slides, median `case`-type slide at 136 words against a 90-word target, worst offenders `s73`
(217), `s74` (218), `s28` (201), `s34` (195). I independently opened `s73`, `s74`, `s28`, `s34`,
`s56` (snapshots) — visually, none of these are broken or illegible (no text overlapping shapes,
no clipped words); the self-check's own characterization — "content-density problem, not a
layout break" — holds up to inspection. I am surfacing this as P1 rather than dismissing it
because the build pipeline itself marked these as blocking, and because §5.12 ("форма подачи
кадра") explicitly removed the old 3-5 line ceiling but kept "text must not overlap itself" as
the only hard limit — these 35 slides sit right at that edge, several (`s34`) with font visibly
shrunk below sibling slides to fit. This is a content-editing decision (shorten body text or
split selected slides), not a rendering fix, and per the build log it is explicitly not the
builder's call to make.

**Recommendation:** orchestrator/owner decides whether to accept this density as a deliberate
choice for this content-heavy lecture (documented explicitly, per the course's own precedent for
accepting such calls) or spawn a trim pass on the worst ~10 offenders before GATE.

---

## P2 — Cosmetic

### P2-1 — s22 arrow-connector implies false sequential causality between 4 independent verification methods

`s22-bez-modeli-chetyre-sposoba-proverki.md` renders a 4-box chain with arrows ("читка → факты →
автор → лицензия") that visually reads as a pipeline, but the content is four **independent**,
parallel verification channels, not sequential steps. The build log flags this itself and
proposes the one-line fix (`arrows: false` on this slide only; the other five `[схема]`-flagged
slides — s21, s25, s30, s58, s65 — are genuinely sequential and correctly default to
`arrows: true`, confirmed by inspection of all five). Low-cost, easy fix, not blocking.

### P2-2 — s34 body text shrunk to ~0.66× sibling font size to fit three content layers on one slide

Same root cause as P1-5 (content density) on this specific slide: 3 plates + 2-column comparison
+ 4-paragraph conclusion compete for 5.36" of body height. Visually legible but noticeably
smaller than neighboring slides — worth folding into the P1-5 trim decision rather than treating
as a separate defect to fix in isolation.

### P2-3 — Keystone slide (s03) presents as one row of four plates, not a visually distinguished two-row structure

`architecture.md` §3 specifies the keystone as "один слайд, два ряда" (Ряд 1 — медиа/CNET, Ряд 2
— перенос/найм). On `s03.png`, the four summary plates ("CNET: статьи, потребовавшие правки" /
"Публично исправляется" / "Наём: проверок узнавания" / "Цена подделки личности") render as a
single undifferentiated horizontal row — a student scanning only the top strip would not see two
grouped rows; the Ряд 1/Ряд 2 split only becomes explicit in the paragraph text in the Ocean box
below. This is still an early, pre-deep-dive keystone slide (position confirmed correct — s03, well
before the first deep dive at s11), and the content itself is accurate and well-evidenced, so this
is a presentation nuance, not a structural failure. A light fix (e.g. a thin divider or two
differently-tinted sub-rows of 2 plates each) would make the two-row design legible at a glance.

### P2-4 — Minor unglossed English in body text: "errors & omissions" (s39), "fair use" (s44)

`s39-tri-sposoba-kupit-pravo.md`: *"клиринг прав перед публикацией плюс страхование от его
ошибки (errors & omissions)"* — the Russian gloss precedes the English term, which is an
acceptable glossing pattern, but the English stays unglossed-again inline; could drop the English
entirely since the Russian phrase already carries the meaning. `s44-getty-stability-chto-reshil-sud.md`:
*"Не через fair use"* — this is a recognized legal-doctrine name without a direct RU equivalent,
and the sentence that follows immediately explains what it means in UK law, so this one reads as
acceptable technical vocabulary rather than a loanword violation. Neither is close to the course's
"excessive anglicisms" failure mode seen in the original Lecture 8 production — a full
broad-regex scan of all 76 visible-body sections (excluding frontmatter, URLs, proper nouns,
brand/company names) turned up only these two plus already-covered brand names (System1, CARMA,
Upwork, etc.) — Russification discipline is otherwise clean across the sample.

---

## Checks that passed cleanly (worth recording, not just flagging problems)

- **Lecture question spoken exactly twice, verbatim.** Confirmed by direct string search: *"Лицо,
  голос и подпись автора стоили доверия бесплатно. Сколько это стоит теперь — и кто платит?"*
  appears in exactly two files, `s10-vopros-lektsii.md` (closing §0) and
  `s70-kto-platit-poimenno.md` (§6 "Сборка"), nowhere else.
- **Keystone position.** s03 is positioned correctly — early in §0 (3rd slide overall), well
  before the first deep-dive case (s11+), not as a recap.
- **No-Timing markers in visible body or notes.** Full-deck grep for `\d+\s*мин`, `⏱`, `⏰`
  returns matches only on s03/s05, and those are *content facts* ("≈70 минут на дипфейк реального
  времени" — the time to build a deepfake, part of the measured counterfactual), not lecture
  pacing markers. Zero hits on cover, dividers, lecture-map, or Q&A slide — exactly as required.
- **Case-breakdown form, CNET (s24–s26) and Getty v. Stability (s43–s47).** Both sequences
  faithfully follow "price of error → classical regime(s) in the same unit → model vs. regime,
  never vs. zero → what moved": CNET gives 41/77 (53%) vs. the 40–61% journalism baseline before
  concluding "AI is not worse by error rate, worse by what disclosure exposed"; Getty gives the
  $30.75M/$1.6B theoretical license cost vs. the court's actual ruling (0, license not required at
  all) before closing on "risk moved from market to court." Getty runs to five slides (s43–s47,
  the architecture's own explicit, owner-authorized exception to the "rule of three"), and every
  slide carries source attribution in the footer.
- **Baseline/counterfactual discipline**, sampled across 7 claims in different sections: CNET
  53%/40–61% baseline (s24); deepfake hiring "$120 + 70 min" vs. the old "hire a live actor"
  counterfactual (s03/s05); Getty $30.75M–$1.6B theoretical license vs. $0 actual (s43); UMG/Warner
  settlement $0.002–0.005/generation vs. the $20–100 stock-license baseline (s50/s71); Upwork
  +109/329/95% growth vs. the explicitly-named absence of a matching decline figure, called out as
  an honest gap rather than papered over (s56); Getty subscriber count 321k→240k, −25%/year (s58);
  cost-collapse table image/track/voiceover all carrying both classical and generated unit prices
  (s71). All seven carry an inline base or counterfactual; none is a bare number.
- **Ocean palette + gold accent + rounded-box motif**, spot-checked across ~20 slides spanning all
  8 sections (s01, s03, s08, s10, s11, s18, s21, s22, s24–s26, s28, s30, s34, s39, s43–s47, s49,
  s56, s58, s60, s62, s65, s70, s72–s76): consistent navy/teal/gold on every content slide, gold
  used exactly once per slide as the course requires, Ocean rounded-box motif present on every
  content slide and correctly absent on cover/dividers. The build's own contrast self-check (1363
  text/background pairs, 0 below WCAG AA) matches what I saw — no low-contrast gold-on-light text
  anywhere sampled (the known `project_ocean_palette_gold_contrast_defect` from earlier lectures
  does not reproduce here — `value_key_color=LIGHT` was deliberately carried over from the Lec-7
  fix).
- **Schema readability on the 6 `[схема]`-flagged slides** (s21, s22, s25, s30, s58, s65): all six
  render correctly and are not visually broken; five are genuinely sequential and the missing
  `arrows:` declaration is a config-hygiene gap, not a visual defect (see P2-1 for the one real
  exception).
- **Speaker notes depth.** Measured word count on `## Заметки лектора` across all 76 slides:
  median 570, min 501, max 796 — every single slide sits inside the course's 500–800-word norm,
  no "Лектору"/layout-description language found anywhere.
- **No other scaffold leaks.** Full-deck grep for `LO[1-9]`, `§[0-9]`, `→ s[0-9]+`, `(s[0-9][0-9])`,
  `VERIFY-DAY-OF`, `FACT-CHECK` in visible body returns zero hits (the one real scaffold leak found
  was "keystone" itself — P1-1 above, a different pattern the standard grep list doesn't cover).

---

## Overall Verdict

**VERDICT: REJECT**

One P0: the deck ships with `media: ""` on literally all 76 slides, including both mandated hero
slots (s01, s76) — a confirmed, non-negotiable blocker per the course's own ENFORCED hero rule,
which exists specifically because of this lecture's prior production round. Per the course's
4-level scale, any P0 forces REJECT regardless of how strong the rest of the deck is.

**What would need to change before this goes to a USER GATE:**

1. **Acquire and wire real hero images for s01 and s76** (6-tier acquisition, §5.7) — non-negotiable,
   this alone blocks GATE.
2. **Decide and act on the broader zero-media gap** — either run a real visual-asset pass across
   the case-heavy sections to match Lec-7's established `analitika`/photo standard, or get an
   explicit, documented owner decision to ship this lecture as text/shape-only (P0-1 + P1-3).
3. **Fix the two "keystone" leaks into visible body text** (s71, s72) — cheap, high-value fix
   (P1-1).
4. **Reword the three "методическ-" hits in speaker notes** (s32, s34, s36) to close the literal
   zero-tolerance grep, even though in context they read as content about measurement methodology
   rather than forbidden teaching meta-commentary (P1-2).
5. **Backfill the 13 missing `timing_min` values in §4** so the deck's own pacing math can
   actually be checked against the 88-minute architecture budget (P1-4).
6. **Decide on the 35 over-density slides** — accept explicitly or spawn a trim pass, especially
   `s73`/`s74`/`s28`/`s34` (P1-5).

The content itself — CNET, Coca-Cola/System1-vs-CARMA, Getty v. Stability, Lada Chizhova, the
deepfake-hiring keystone row 2, the three-to-four-orders-of-magnitude refrain — is well-sourced,
follows the mandated case-breakdown form faithfully, carries baselines on every sampled
measurable claim, and hits the lecture-question-twice and keystone-before-deep-dive structural
requirements cleanly. This is a strong draft let down entirely by a production-pipeline gap (no
visual-loop asset work happened at all) and a handful of cheap, mechanical text fixes — none of
the P1/P2 findings here require new research or a content rewrite.
