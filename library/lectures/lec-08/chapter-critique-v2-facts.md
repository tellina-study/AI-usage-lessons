VERDICT: REJECT

# Fact-Checker Report — Lecture 8 chapter (Phase 3, rework issue #289, arch-v4) — 2026-10-21

**Scope.** Full sweep of all 8 files: `chapter.md`, `chapter-part2.md`, `chapter-part3.md`,
`chapter-part3b.md`, `chapter-part4.md`, `chapter-part4a.md`, `chapter-part5.md`,
`chapter-part5b.md` (~3,664 lines total). Cross-checked against `rework/architecture.md`,
`rework/decisions-owner.md`, `rework/decisions-orkestratora.md`, and all four
`rework/research/01-04*.md` files. Independent WebSearch/WebFetch verification performed for
every claim NOT already covered by the four research files, and for the three open
`[FACT-CHECK]` markers, per task instruction. This is a full sweep, not a subset rerun (per the
ENFORCED "Полная цитата-проверка на каждой revision" rule and the Л9 lesson that caused it).

This is **not** a review of REJECT-worthy content quality — the chapter is exceptionally
well-disciplined about bases/counterfactuals, honest about unresolved litigation, and transparent
about its own prior (May 2026) errors. The REJECT verdict is driven by exactly one P0: a single
arithmetic error in a theoretical statutory-damages calculation. Everything else checked is either
VERIFIED or a narrow, specific P1/P2 — see tallies below.

## Severity counts

- **P0 (false fact / broken citation / direction inversion / curriculum hallucination / misquote): 1**
- **P1 (missing source / suspicious number / methodology gap / freshness expired): 3**
- **P2 (cite format / bibliography hygiene / minor): 3**

---

## Resolution of the three open `[FACT-CHECK]` markers (mandatory, per task)

### 1. Sora shutdown / $1B Disney-deal-collapse (`chapter.md`, line 366, Part 1 sources)

**Quote:** "Веб- и мобильная версия приложения были закрыты 26 апреля 2026 года, а доступ через
программный интерфейс — 24 сентября 2026 года; партнёрство с Disney к этому моменту уже
распалось... По неофициальным данным... пиковая аудитория сервиса — около миллиона пользователей —
упала до менее чем пятисот тысяч при расходах компании на поддержку сервиса порядка миллиона
долларов в день."

**Verification (live WebSearch + WebFetch, 2026-10-21):**
- Variety, "OpenAI Will Shut Down Sora Video App; Disney Drops Plans for $1 Billion Investment" —
  https://variety.com/2026/digital/news/openai-shutting-down-sora-video-disney-1236698277/
- the-decoder.com, "Disney pulls out of OpenAI partnership after Sora app and API gets killed just
  months after launch" — confirms Disney's **$1B planned investment in OpenAI** (not a direct
  Sora-licensing fee), partnership signed **December 11, 2025**, for use of 200+ Disney/Marvel/
  Pixar/Star Wars characters; Disney learned of the shutdown less than an hour before the public
  announcement; no formal licensing agreement was ever executed and no payments changed hands.
- startupfortune.com / tech-insider.org corroborate: web/app discontinued **April 26, 2026**, API
  discontinued **September 24, 2026** — dates match the chapter exactly.
- Burn-rate figure (~$1M/day, user drop from ~1M peak to <500K) is consistent across multiple
  outlets cited by `research/03-freshness-october-2026.md`, which the chapter correctly traces to.

**Verdict: CONFIRMED.** Dates, the Disney $1B figure, and the shutdown sequence all check out
against live sources. **Action:** the `[FACT-CHECK]` bracket in `chapter.md` line 366 can be
closed — replace it with real citations: Variety (2026) and the-decoder.com (2026), both findable
and quotable as above. One precision note worth adding to the narrative (not an error, but a
sharpening): the "$1B" is specifically Disney's **planned investment in OpenAI**, not a
Sora-specific licensing fee — the chapter's phrasing ("партнёрство с Disney стоимостью порядка
миллиарда долларов... соглашение, которое должно было дать Sora доступ к узнаваемым персонажам
франшиз в обмен на лицензионные выплаты") blends these two things slightly; worth a one-clause fix
for precision, not severity-worthy.

### 2. Getty+Shutterstock merger synergy figure, $150–200M over 3 years (`chapter-part4.md`, lines 298–300, §5.3)

**Quote:** "Объявленная цель — экономия на издержках порядка $150–200 млн за три года (Getty
Images / Shutterstock, пресс-релиз сделки, январь 2025) [FACT-CHECK: точная сумма синергии
нуждается в сверке по первичному пресс-релизу слияния]."

**Verification (live WebSearch, 2026-10-21):** Getty Images' own investor-relations press release
(Jan 7, 2025, https://investors.gettyimages.com/news-releases/news-release-details/getty-images-and-shutterstock-merge-creating-premier-visual
), cross-confirmed via CNBC, CGChannel, InsideArbitrage, and Getty's own SEC 8-K filings: "run rate
synergies across SG&A and CAPEX between **$150 million and $200 million** achieved within the
first three years post-close, with approximately two-thirds expected to be delivered within the
first twelve to twenty-four months."

**Verdict: CONFIRMED EXACTLY** — the figure in the chapter matches the real, primary press release
word-for-word in substance. This also resolves `research/03-freshness-october-2026.md`'s own
implicit flag (it inherited this figure from the superseded `2026-landscape.md` research without
independently re-verifying it — the task's prompt correctly anticipated this needed a fresh check,
and it now checks out). **Action:** close the `[FACT-CHECK]` bracket; replace with the real
citation (Getty Images Investor Relations, Jan 7 2025 press release, or the SEC 8-K at
https://www.sec.gov/Archives/edgar/data/1898496/000162828025013092/gety-2024x12x31ex991.htm).

### 3. Contributor-photographer royalty treatment during Getty's Chapter 11 (`chapter-part4.md`, lines 385–387, §5.3)

**Quote:** "вопрос, выплачиваются ли и в каком порядке накопленные, но ещё не перечисленные
роялти во время самой процедуры реструктуризации, является стандартной частью любого дела о
защите от кредиторов по Chapter 11 [FACT-CHECK: точные условия выплат контрибьюторам Getty Images
в ходе реструктуризации 2026 года требуют сверки по первичным документам процедуры]."

**Verification (live WebFetch, 2026-10-21):** Photo Business News ("Squeezed Out: Getty Images
Files For Bankruptcy," https://photobusinessnews.substack.com/p/squeezed-out-getty-images-files-for
) — a specific, reportable, and more precise finding than what the chapter currently hedges
toward: **"The agreement itself has no class for contributors, no mention of royalties, and no
schedule of which contracts the company keeps."** The only language addressing contributors in the
plan is a single forward-looking sentence from Getty itself: "There is no anticipated impact on
content contributors, partners, customers, or employees" — which the source correctly
characterizes as "a forecast, not a promise." The real mechanism protecting near-term payouts is
indirect: Getty must honor contracts it chooses to retain in bankruptcy, which covers only
contracts already in the pipeline, and only for as long as the new private owners choose to keep
them — rate changes thereafter require no court approval, only 30 days' notice. PetaPixel
(already cited by the chapter) corroborates the general framing ("contributors... should see no
change to payouts" per Getty's own messaging) without this additional specificity.

**Verdict: the chapter's current text is NOT WRONG, but it is strictly weaker than the best
available source** — it hedges with a generic "this is standard Chapter 11 procedure" statement
where a specific, verified, and more newsworthy fact exists: the restructuring agreement itself
contains **no contributor creditor class and no mention of royalties at all**, and future rate
changes require no court approval. This is exactly the kind of concrete finding the chapter's own
AI-Failure/judgment content rule rewards (a documented gap in the protection, not just an
abstraction) and it directly strengthens the "что переехало" argument already being made about
Getty's contributors as "третий, самый тихий адресат цены." **Severity: P1** — recommend replacing
the hedge with the sourced, specific finding (cite Photo Business News alongside the already-cited
PetaPixel) rather than leaving a vague procedural generality.

---

## Keystone Row 2 (deepfake hiring fraud) — number-by-number verification against `research/04`

Every number in `chapter.md` §0.2 (Ряд 2) was checked against
`rework/research/04-keystone-row2-verification.md` for drift. **No drift found — all numbers
match exactly:**

| Claim in chapter | Chapter text | Research 04 | Match |
|---|---|---|---|
| KnowBe4 | "4 отдельных видеособеседования... проверку биографических данных... Подмену... поймала система обнаружения вторжений... спустя несколько дней" | "4 отдельных видео-собеседования + «стандартные» pre-hire проверки... EDR... спустя дни" | ✓ exact |
| Christina Chapman | "более 309 компаний... доход... превысил 17 миллионов долларов за три года" | "$17+ млн за 3 года, через 309 компаний" | ✓ exact |
| Nisos cell | "более 170 000 поданных заявок... 76 полученных офферов силами 22 операторов за девять месяцев" | "170 000+ заявок → 76 офферов, 22 оператора за 9 месяцев" | ✓ exact |
| Stolen identity cost | "около 120 долларов" | "≈$120" | ✓ exact |
| Deepfake build time | "около 70 минут" | "≈70 минут" | ✓ exact |
| Checkr survey | "с 31% годом ранее до 40%... с 62% до 68%" | "40% vs 31%... 68% vs 62%" | ✓ exact |
| Eleven-nation advisory | "31 июля 2026 года" | "31.07.2026" | ✓ exact |
| FBI repeat warning | "14 октября 2026 года" | "14.10.2026" | ✓ exact |
| Scale (100K operators, 40 countries, $250-600M/yr, $800M to weapons 2024) | matches `chapter-part4a.md` §6.2 exactly | matches §2.2 of research 04 exactly | ✓ exact |

**Verdict: VERIFIED, no drift.**

---

## CNET numbers — consistency check across Part 1 (keystone) and Part 2 (detailed)

Both tellings of the CNET case were compared clause-by-clause:

- Part 1 (`chapter.md` §0.2): "Из 77 опубликованных текстов 41, то есть 53%, потребовали
  исправлений" / baseline "40–61%" / correction rate "около 2%".
- Part 2 (`chapter-part2.md` §2.3): "Из 77 опубликованных AI-статей 41 (53%) потребовали
  исправлений" / "от 40% до 61%" / "лишь около 2%".

**Verdict: VERIFIED — identical in both tellings, including the methodological caveat (graph (б),
not (а)) being stated honestly in both places.** 41/77 = 53.2% rounds correctly to "53%."

---

## Coca-Cola / Toys "R" Us / System1 — verified against `research/03`, task 2

Checked: positive +12.2%→+3.4%, negative 13.5%→53.4%, neutral 74.3%→43.2% (source: CARMA via
Marketing-Interactive, 28.06.2024), System1 5.9★ (Silverside AI, 70,000 clips, 2025 reprise). All
figures match `research/03-freshness-october-2026.md` task 2 exactly, including the arithmetic
check the chapter performs itself (12.2+13.5+74.3=100.0; 3.4+53.4+43.2=100.0 — both checked,
correct). The chapter is explicit and honest about the CARMA platform/sample-size gap not being
publicly disclosed — this caveat is present in both `chapter-part2.md` §3.3 and repeated in
`chapter-part5.md` Q4. **Verdict: VERIFIED, no drift, caveat not silently dropped.**

---

## YouTube AI-thumbnails numbers — confirmed ABSENT from narrative

Grepped all 8 files for `47,3`/`47.3`/`61,8`/`61.8`/`−22%`/`−19%`/`-22%`/`-19%`. Result: **zero
live occurrences of the debunked chain.** The only hits are (a) `chapter-part5b.md`'s own
bibliography note, which exists specifically to document *why* the numbers were removed (quoting
them only to explain the retraction — this is the correct, transparent way to handle a retracted
claim, not a residual leak), and (b) an unrelated "−19%" in `chapter-part4.md` about Upwork job
postings YoY (a genuinely different statistic that happens to share a number). **Verdict: VERIFIED
clean — the debunked chain was fully and correctly purged from live narrative content.**

---

## Getty v Stability UK — verified against `research/02`

Checked: $2.5/image × 12.3M ≈ $30.75M (exact: $30,750,000); $130/image × 12.3M ≈ $1.6B (exact:
$1,599,000,000, chapter rounds to "$1.6 млрд," correct); the chapter adds its own arithmetic — "разница
в 52 раза" ($1.6B / $30.75M = 52.03) — **independently recomputed and confirmed correct**. Nov 4,
2025 verdict date — matches research exactly. CDPA "copy" reasoning (abandoned primary-infringement
claim on jurisdictional grounds; secondary-infringement claim on "copy" fails because model weights
are statistical influence, not reproduction; narrow trademark loss on early-version watermarks) —
matches `research/02-case-candidates-creative-industries.md` and goes further, correctly adding
nuance research/02 only implied (UK has no fair-use doctrine at all, unlike the parallel US case,
which the chapter explains clearly and correctly). US motion-to-dismiss mostly denied, April 2026 —
matches. January 2026 permission-to-appeal — matches. **Verdict: VERIFIED, no drift, and the
chapter's legal exposition is more careful than the source research file, not less.**

---

## Getty bankruptcy chronology — verified against `research/03`, task 4 (this week's news)

Checked every date and figure in `chapter-part4.md` §5.3 against `research/03-freshness-october-2026.md`:
merger terminated July 7, 2026 — match; NYSE trading halt September 29, 2026 — match; Chapter 11
filed October 12–13, 2026 — match; restructuring announced October 21, 2026 ($533M new capital,
$270M debt write-off) — match; subscribers 321,000→240,000 (−25%/year, independently recomputed:
(321,000−240,000)/321,000 = 25.2%, rounds correctly) — match; revenue −2.5% to $229.1M — match.
**Verdict: VERIFIED, no drift**, and the chapter correctly and explicitly flags its own prior
(May 2026) error on this exact topic ("защитная консолидация" → actually a failed defense + the
company itself names AI pressure as one of several causes) as a worked example of self-correction
— this is a strength, not a finding.

---

## Upwork numbers — verified against `research/03`, task 4

AI skills +109% YoY, AI video +329%, AI image +95% — all match exactly. Honest gap explicitly
preserved: the chapter states plainly, twice (§5.2 and again in `chapter-part5.md` Q1), that Upwork
does **not** publish a symmetric decline figure for traditional categories, and refuses to pair
"+109% AI / −N% traditional" into a false single statistic — using BLS's −2%/10yr as the only
(non-Upwork-specific) quantitative anchor, with the methodological caveat stated explicitly. The
old, unconfirmed "−17.01%" figure from `2026-landscape.md` was correctly dropped, not quietly
rounded down. **Verdict: VERIFIED, honest handling of the gap confirmed.**

---

## Cost-collapse figures (§1) — verified, correction instruction confirmed applied

Image $50–150 → $0.03–0.05 (Midjourney V8.1/V8.2, Firefly Image 5) — matches `research/03` task 1
pricing exactly. Voice $50–450/min → $0.04–0.20/min (ElevenLabs) — matches exactly. **Music: the
mandated correction (compare AI generation to stock-license, not to custom-studio-score) was
correctly applied** — `chapter.md` §1.4 explicitly states the custom-score comparison is forbidden
as a "выигрыш от нуля" and uses $20–100 stock license → $0.015–0.02/song (Suno) instead, exactly as
`research/03`'s task 1 instructed. This correction is also reinforced a second time in
`chapter-part5.md` Q8, with the custom-score comparison explicitly disavowed there too. **Verdict:
VERIFIED — the flagged correction was properly carried through, not left as the previously-flagged
incorrect comparison.**

---

## Arup duplication check (`chapter-part5b.md` bibliography vs. narrative)

**Grepped all 8 chapter files for "Arup" (and Cyrillic transliterations).** Result: **three hits,
all in `chapter-part5b.md`'s consolidated bibliography** (IDEMIA, PRMIA, SCMP entries) — **zero
hits in any narrative prose across all 8 files.** This confirms `architecture.md`'s explicit
decision (§1, §7) to remove Arup entirely was carried through correctly in the narrative: no
Arup numbers, no Arup story, no Arup lesson is retold anywhere in the chapter body. Lecture 14's
own Arup coverage (`lec-14/slides/s26-arup-deepfake.md`) is **not duplicated.**

**However:** the three orphaned bibliography entries are a genuine, if low-stakes, finding —
nothing in the chapter's live content cites IDEMIA/PRMIA/SCMP, so these three entries are leftover
artifacts from the Arup research pass that should have been struck when Arup was cut from the
architecture. This is **bibliography noise, not a duplication regression** — but it should be
cleaned up before publication, both because dead citations erode trust in the "every source is
load-bearing" norm this chapter otherwise holds to rigorously, and because a future reader cross-
referencing the bibliography against Lecture 14 could reasonably (if briefly) wonder whether Arup
content was supposed to be here. **Severity: P2.**

---

## New finding: NYT statutory-maximum arithmetic error — P0

**Quote** (`chapter-part3b.md`, lines 30–36): "У иска есть отдельная, куда более пугающая цифра —
статутные максимумы до **$150 000 за произведение**, применённые к более чем **10,8 миллионам**
произведений, заявленных всеми истцами по новостным делам совокупно, что в теории даёт потолок в
**десятки и сотни миллиардов долларов**."

**Independent recomputation:** 10,800,000 × $150,000 = **$1,620,000,000,000** — i.e., **≈$1.62
trillion**, not "tens and hundreds of billions." The chapter's own stated inputs, multiplied
exactly as the sentence instructs the reader to do, produce a number roughly **10× larger** than
the one printed. For comparison, the chapter gets the *analogous* calculation right elsewhere in
the same section: 61,026 × $150,000 = $9,153,900,000, correctly rounded to "свыше $9 млрд"
(`chapter-part3b.md` line 265) — so this is not a systemic misunderstanding of the statutory-cap
mechanism, just a single arithmetic slip on the NYT figure specifically.

**Why this is P0, not P1:** this is not a disputed estimate or an uncaveated speculative figure —
it is a specific, computed number, derived from inputs stated in the same sentence, that is
simply arithmetically wrong. The passage explicitly invites the reader to treat $150,000 and
10.8 million as the inputs to a multiplication; multiplying them correctly yields a figure an order
of magnitude larger than what is printed. The hedge ("это в теории... не оценка, которую кто-либо
всерьёз рассчитывает получить") correctly caveats the *realism* of the number, but does not excuse
the number itself being mis-computed.

**Recommendation:** change "десятки и сотни миллиардов долларов" to "свыше 1,6 триллиона долларов"
(or restate the sentence to avoid a specific magnitude claim if precision isn't wanted). This is a
single-clause fix, not a structural problem with the section — the surrounding reasoning (statutory
cap ≠ real recovery, contrast with the $9B Suno figure, contrast with the $250M News Corp deal) is
otherwise sound and well-constructed.

---

## New finding: human deepfake-detection-rate figures — uncited and unreconciled across two sections — P1

Two different figures for "how good are humans at spotting deepfakes" appear in the chapter, from
two different (uncredited, in the chapter's own bibliography) sources, without being reconciled:

1. **`chapter.md` §0.2** (keystone, Ряд 2): "человек, которого прямо предупредили... правильно
   определяет качественный видео-дипфейк лишь в **24–25% случаев**" — sourced in
   `rework/research/04-keystone-row2-verification.md` §2.3 to "агрегированные исследования deepfake
   detection, 2026 (brightdefense/adaptivesecurity сводки)" — i.e., industry blog aggregations, at
   least named as a source type in the research file (though not named in the chapter's own
   bibliography, `chapter-part5b.md`, at all).

2. **`chapter-part5.md`, Q3 self-check answer**: "по сводным исследованиям распознавания подделок в
   аудио — 62%, в видео — **57%**, на изображениях — 53%, в тексте — 52% правильных ответов."

**Verification:** this second figure set traces to `rework/research/02-case-candidates-creative-industries.md`
line 55 (originally gathered for the now-cut Arup case, Шаг 2, графа (б): "аудио 62.08%, видео
57.31%, изображения 53.16%, текст 52.00%" — attributed there only to "людям свойственно
распознавать дипфейк..." with **no named source at all**, not even in the research file). I traced
this independently via WebSearch and found it is a **real, citable academic result**: Diel et al.,
"Human performance in detecting deepfakes: A systematic review and meta-analysis of 56 papers"
(ScienceDirect / Computers in Human Behavior Reports, 2024; N=86,155 across studies) — reporting
exactly 62.08% (audio), 57.31% (video), 53.16% (image), 52.00% (text), with an overall deepfake-
specific detection accuracy of 55.54% vs. 68.08% for real stimuli. The number is **not fabricated —
it is real and traceable** — but:

- **It is not cited anywhere in the chapter's bibliography** (`chapter-part5b.md`), unlike nearly
  every other number in the chapter, which is unusual given how rigorously sourced the rest of the
  document is.
- **It is not reconciled with the 24–25% figure used elsewhere in the same chapter for the same
  underlying question** (human ability to detect video deepfakes specifically) — a reader
  encountering "24–25%" in the keystone and "57%" in the self-check Q&A, both about video, with no
  cross-reference, may reasonably read this as an internal inconsistency, even though the two
  figures likely come from different experimental conditions (explicitly primed/warned
  participants vs. general population across 56 pooled studies).
- This figure also appears to be a residual artifact of the cut Arup case (which `research/02`
  built it around) that survived into the final chapter via the Q&A section without its original
  context.

**Recommendation:** name the Diel et al. (2024) meta-analysis explicitly in the bibliography and in
the Q3 answer text, and add one sentence in either location reconciling why "24–25%" (video, primed
to look for fakes) and "57%" (video, pooled meta-analysis, general studies) are not the same
measurement and do not contradict each other.

---

## Anonymization check — Russian institutions

Grepped all 8 files for "Сбер", "ВЦИОМ", "Яндекс", "МГТУ", "Роскомнадзор", "Газпром", "Сколково."
**Zero hits.** "Kandinsky" is referenced only as a product/model name (not attributed to a specific
Russian corporate owner in the narrative), consistent with course convention. **Verdict: VERIFIED
clean.**

---

## Verified facts (sample, beyond those detailed above) — N≈40 total checked

- ✓ CDPA, UK statute name and function — correct.
- ✓ LAION-5B scale: ~5.85 billion image-text pairs, ~12.3M attributed to Getty (≈0.2% of dataset) —
  matches research/02, internally consistent arithmetic (12.3M/5.85B = 0.21%, chapter doesn't state
  this percentage explicitly but the implied math holds).
- ✓ Carlini et al. 2023 (USENIX Security), "Extracting Training Data from Diffusion Models" — real,
  correctly cited, correctly used to caveat the "no memorization" claim rather than oversell it.
- ✓ News Corp × OpenAI, up to $250M/5 years, May 2024 — well-known, publicly reported deal, matches
  bibliography citation (Deadline).
- ✓ RIAA v Suno/Udio matrix (Warner settled both; UMG settled Udio only, suing Suno; Sony suing
  both) — matches `research/02` and `research/03`'s own sourcing exactly, including the August 18,
  2026 denial of the amendment attempt and the September 2026 second Suno V6 suit.
- ✓ Suno training-data leak: 383,000+ hours, 2,013,545 clips from one YouTube Music sub-dataset —
  matches 404 Media reporting cited in bibliography.
- ✓ Sports Illustrated: 100 employees, stock −28–33.6%, license revoked citing missed payment (not
  officially the AI scandal) — matches `research/02`, and the chapter is careful (in both
  `chapter-part2.md` §2.4 and `chapter-part5.md` Q5) not to claim causation it can't support.
- ✓ Kling 4.0 (Oct 15, 2026, 30-sec clips vs. prior 15-sec), Veo 3.1 Lite (April 2026), Kandinsky
  6.0 Video (Oct 6, 2026, sound added) — match `research/03`'s freshness table exactly.
- ✓ C2PA / Content Credentials standard — real, correctly described (metadata provenance standard,
  coalition-based, not a complete solution since legacy content can't retroactively carry it).

---

## NEEDS-CITATION (beyond the deepfake-detection-rate gap above)

- The three now-resolved `[FACT-CHECK]` brackets (Sora/Disney, Getty synergy figure) need their
  placeholder text swapped for the real citations found in this report, per the "Action" notes
  above — not an error, but incomplete per the chapter's own bibliography standard.

## UNVERIFIABLE

- None found requiring a flag — every claim that lacked a clean primary source was already
  honestly marked as such by the chapter itself (e.g., CNET's undisclosed engine vendor, CARMA's
  undisclosed platform/sample size, the identity of the Arup deepfake tool in the cut material) —
  this is the chapter doing its job correctly, not a gap in this fact-check.

---

## Top-N правок до публикации

1. **(P0, mandatory before any sign-off)** Fix the NYT statutory-cap arithmetic in
   `chapter-part3b.md` (~line 32–36): "десятки и сотни миллиардов долларов" → "свыше 1,6 триллиона
   долларов" (10.8M × $150,000 = $1.62T), or rephrase to avoid stating a specific wrong magnitude.
2. **(P1)** Replace the Getty Chapter-11 contributor-royalty hedge in `chapter-part4.md` (lines
   385–387) with the more precise, sourced finding: the restructuring agreement has no contributor
   creditor class and no mention of royalties; only Getty's own forward-looking, non-binding
   statement addresses contributors at all (cite Photo Business News alongside the existing
   PetaPixel citation).
3. **(P1)** Name the Diel et al. (2024) meta-analysis explicitly for the 62/57/53/52% deepfake-
   detection figures (currently uncited anywhere in the bibliography) and add one sentence
   reconciling it with the differently-sourced 24–25% figure used elsewhere in the chapter for the
   same underlying question.
4. **(P2)** Close the two remaining `[FACT-CHECK]` brackets with the real citations found in this
   report: Sora/Disney (Variety 2026; the-decoder.com 2026) and the Getty+Shutterstock synergy
   figure (Getty Images Investor Relations press release, Jan 7 2025, or the corresponding SEC
   8-K).
5. **(P2)** Remove the three orphaned Arup bibliography entries (IDEMIA, PRMIA, SCMP) from
   `chapter-part5b.md` — nothing in the live narrative cites them, and the architecture's explicit
   decision to cut Arup was otherwise carried through cleanly; these three lines are the one loose
   end.
6. **(Not a correctness issue, minor precision polish)** In `chapter.md`'s Sora passage, separate
   the "$1B Disney investment in OpenAI" from "Sora-specific licensing revenue" — the current
   phrasing blends them slightly; the underlying facts in the chapter are otherwise accurate.

---

## Overall assessment

This chapter is one of the most rigorously self-policed documents of this kind I have checked:
it catches and corrects its own prior (May 2026) errors in public (Getty/Shutterstock, YouTube
thumbnails), names every honest gap rather than papering over it (CARMA methodology, CNET's
engine, Upwork's traditional-category non-measurement), and gets dozens of multi-step financial
and legal calculations right. The single P0 is a genuine, fixable, one-line arithmetic slip, not a
sign of systemic carelessness — but per the course's own enforced verdict rule, any P0 forces
REJECT regardless of how narrow the fix is, so REJECT stands until that line is corrected. With
items 1–3 above addressed, this chapter would be APPROVE-CLEAN or APPROVE-WITH-POLISH on a
re-check limited to those three spots.
