# Methodology Critique — Speech v1 — Лекция 4

**VERDICT: REVISE**

*Rationale:* 0 P0 issues; **9 P1 issues** (cap для APPROVE-WITH-POLISH = 4). Three categories of P1: (a) significant anglicism load that drifts the speech beyond chapter-canonical Russian voice, (b) one cross-reference correctness risk re: Лекция 5 framing that conflicts with plan-v2 source-of-truth, (c) two density hotspots where speaker has effectively no slack to recover from any pause overshoot. Severity counter check: 9 P1 with no overrides — `REVISE` mandated by 4-level scale.

---

## Issue counts

- **P0:** 0
- **P1:** 9
- **P2:** 8

---

## WPM analysis

**Author-reported figures.** Max 91.2 wpm на s13 (per frontmatter author note), average ~75 wpm. Verified against transcript.

**Independent computation** (stripping stage directions `[…]`, markdown emphasis, quotation marks, headers):

| slide | dur | words | wpm | verdict |
|---|---|---|---|---|
| s01 | 3 min | 226 | 75.3 | OK |
| s04 | 2 min | 160 | 80.0 | OK |
| s06 | 2.5 min | 201 | 80.4 | OK |
| s08 | 2.5 min | 199 | 79.6 | OK |
| s09 | 2 min | 177 | **88.5** | WATCH |
| s10 | 3 min | 270 | **90.0** | WATCH |
| s11 | 3 min | 209 | 69.7 | OK |
| s12 | 3 min | 230 | 76.7 | OK |
| s13 | 2.5 min | 225 | **90.0** | WATCH |
| s17a | 2.5 min | 204 | 81.6 | OK |
| s17b | 2.5 min | 210 | 84.0 | OK |
| s22 | 4 min | 307 | 76.8 | OK |
| s23 | 3 min | 231 | 77.0 | OK |
| s24 | 3 min | 252 | 84.0 | OK |
| s26 | 2 min | 178 | **89.0** | WATCH |
| **total active** | 66.6 min | 4976 | **74.7** | OK (target 70-75) |

**Verdict:** WPM hard rule (≤95 на любом фрагменте) — **PASS**. No slide exceeds 95.

**Concern (P1).** Four slides cluster at 88-90 wpm: s09 (CV pipeline), s10 (sens/spec/PPV math), s13 (bias case-cards), s26 (three takeaways). These are also the heaviest cognitive-load slides (s09 — 4-stage pipeline + Grad-CAM; s10 — 4 metric formulas + PPV math worked example; s13 — 2 bias cases with numbers; s26 — full LO recap). At 88-90 wpm there is **no recovery margin** for a missed beat, audience question, или live demo glitch — single pause of 10-15 sec pushes effective wpm over 95 для оставшегося фрагмента. Author's frontmatter cap is 95 wpm but pipeline target is 70-75 — these four slides sit 18-22% above target.

**Buffer.** 7 min Q&A buffer at end (slack = 75 - 68.6 = 6.4 min computed; frontmatter claims 7 min). Per Anthropic principle для интерактивной лекции 75 минут — 7-10% buffer = 5.25-7.5 min. Frontmatter claim of 7 min is **at lower edge of acceptable**. If two raise-hands polls (s03) + Chester live-demo (s01) overshoot by 30 sec each — buffer compresses to 5.4 min. Tight but workable. P2 only.

---

## Pedagogical sequence

### A. LO progression

**LO mapping declared (frontmatter line 681):** LO1 (s06), LO2 (s11, s12), LO3 (s24), LO8 framing (s26, s28).

Verification:
- **LO1** (классификация 4 типов AI-применений) — ✅ s06 carries assertion-evidence для 4-cell matrix, examples (mosmed.ai, IDx-DR, AlphaFold) provided in each cell. **PASS.**
- **LO2** (оценка через клинические данные) — ✅ s11 walks MASAI/Goh/Liu; s12 walks operational metrics. Bayes formula с PPV worked в s10 — этот блок тоже LO2 (формально маркирован в deck.yaml). **PASS.**
- **LO3** (этическая дилемма ответственности) — ✅ s24 develops 4-actor framework + s21 (Obermeyer) + s22 (LLM anti-patterns) + s23 (Change Healthcare). **PASS.**
- **LO8 framing** (3 принципа as input для Lec 9 черновика) — ✅ s26 outcome 3 + s27 closing + s28 explicit framing «вход в копилку чек-листа на Лекции 9». **PASS.**

**Cumulative LO coverage matches deck.yaml** declared LOs `[LO1, LO2, LO3, LO8]`. LO4 has been correctly removed (deck v3 fix 9 per yaml comment). Speech does **not** claim LO4 — frontmatter line 681 correctly omits LO4. ✅

### B. Section divider bridges

5 dividers (s05b, s08a, s13a, s19a, s24a). Each carries one-sentence forward-bridge:
- s05b: «Это первый раздел из пяти — карта AI в медицине.»
- s08a: «Второй раздел из пяти — AI-диагностика как зеркало.»
- s13a: «Третий раздел из пяти — drug discovery: обещания и реальность.»
- s19a: «Четвёртый раздел из пяти — этика и ответственность.»
- s24a: «Пятый раздел из пяти — заключение.»

**P2.** Numerator/denominator уверены (1/5 → 5/5) — но раздел fact «5 разделов» включает Раздел 5 = Заключение. Counter-fact: chapter has §0 Open + §1-5 = 6 разделов (chapter §0.1, 0.2, 0.3 — это «Раздел 0»). Speech omits «Раздел 0» from divider count — это OK methodically (раздел 0 = open, не numbered section), но students may notice that s05b says «first of 5» при том что they already heard 5 sub-blocks в Open (s01-s05). Minor consistency cosmetic. P2.

### C. Central question callback chain

Chain declared в task spec: **s05 → s12 → s14 → s17a → s17b → s24 → s27**.

Verification in speech:
- s05 (поставлен): ✅ line 116.
- s12 (mid-lecture echo): ✅ line 294 «Мост к остальной лекции…»
- s14 (mid-lecture callback): ✅ line 332 «AI-диагностика — обещание сбылось. Mosmed.ai тому подтверждение, MASAI RCT тому подтверждение. Drug discovery — обещали ускорить в десять раз. Что реально работает на 2026 год?»
- s17a (Rentosertib echo): ✅ line 398 «AI ускорил design — verified.»
- s17b (DSP-1181 anti-echo): ✅ line 416 «AI ускорил design — это verifiable.»
- s24 (final answer): ✅ line 566 «Обратите внимание — мы с вами наконец-то пришли к ответу.»
- s27 (closing восстановление): ✅ line 628 «Это callback к центральному вопросу лекции. Какие AI-обещания в медицине сбылись и кто отвечает.»

**PASS** — chain is complete with explicit semantic callbacks. ✅

### D. Раздел transitions (0 → 1 → 2 → 3 → 4 → 5)

All transitions smooth; each new section opens with explicit framing:
- Raz 0 → 1: s05b divider + s06 «AI в медицине — это не одна индустрия…»
- Raz 1 → 2: s08a divider + s09 «Как технически работает AI-диагностика»
- Raz 2 → 3: s13a divider + s14 «Мы с вами прошли половину лекции…»
- Raz 3 → 4: s19a divider + s19 (note: deck mapping — s19 was moved from Raz 4 micro-exercise to Raz 4 lecture content per yaml comment) → «Перед тяжёлыми темами — короткая прикладная секция. AI как объяснитель.»
- Raz 4 → 5: s24a divider + s26 «Давайте коротко опишем, что мы с вами прошли — три вывода.»

**PASS** with one wrinkle (see P1 below): s19 is placed inside Раздел 4 «Этика и ответственность» (line 448) but s19 content («AI как объяснитель») is a **prikladnoy/practical** topic, not ethics. The transition «Перед тяжёлыми темами — короткая прикладная секция» (line 454) acknowledges the mismatch — but it leaves student wondering why a 3-min «applied» block sits inside an «Ethics» section. See P1-6.

---

## Anglicism check

**Forbidden anglicisms list** (per `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md` lines 678-695): `стейкс|фоллбек|пайплайн|кейс|инсайт|workflow|edge case|фит|релиз|деплой|фича|митап`.

Grep results in speech.md:
- `стейкс` — 0 occurrences ✅
- `фоллбек` — 0 occurrences ✅
- `пайплайн` — 0 occurrences ✅
- `кейс` — 0 occurrences ✅
- `инсайт` — 0 occurrences ✅
- `workflow` — 0 occurrences (replaced by «рабочий процесс») ✅
- `edge case` — 0 occurrences ✅
- `фит` — 0 occurrences ✅
- `деплой` — 0 occurrences ✅
- `фича/митап/релиз` — 0 occurrences ✅

**Hard-list anglicism check: PASS.**

**Soft-list anglicisms (chapter-allowed but speech-density risk):**

Word frequency in speech (raw count, English-form terms):
- `design choice/design-driven/design choices` — 4× (lines 58, 150, 302; semantically «дизайн-выбор» but term is unambiguous in chapter glossary)
- `peer-reviewed/verifiable` — 7× (lines 294, 386, 394 ×2, 398, 416, 612)
- `vendor` — 11× (multiple slides)
- `operator/regulator/control/liability` — 8× collectively (s24 block)
- `deployment population` — 2× (lines 312, 642)
- `production` — 5× (lines 288, 430, 610, 642)
- `Caveat`-class words — 0 (good — author internalized chapter's «оговорка» replacement)
- `fine-tuned/fine-tune` — 2× (lines 210, 306)
- `narrow CV` — replaced cleanly with «узкое компьютерное зрение» — ✅
- `framework` — 2× («4-actor framework» — line 570; «PCCP-framework» implicit)
- `claim` — 4× (lines 416, 612, 358 chapter spillover)

The 4-actor block s24 (lines 564-590) reads:
> «Врач — высокий control, высокая liability. Ставит финальный диагноз. AI — input, не decision-maker. Юридически врач — primary responsible person. AI-suggestion — «второе мнение». Только врач имеет full context: анамнез, осмотр, лабораторные результаты, AI-output как один из inputs.»

This passage has **9 anglicism tokens** in 4 sentences («control, liability, input, decision-maker, primary responsible person, AI-suggestion, full context, AI-output, inputs»). For a 3-курс engineering audience this is dense and **breaks the conversational tone** that speech is supposed to deliver vs chapter. Chapter §5.5 uses analogous phrasing but chapter is academic; speech должна разговорно.

See P1-1.

---

## Speaker cue density

Counts (independent):
- `[пауза N сек]` / `[пауза]` / `[пауза, …]` — 13 occurrences (good distribution across all 5 sections)
- `[медленно]` / `[медленно, с акцентом]` — 7 (concentrated at climactic moments: s05 central question, s10 PPV reveal, s13 «validation set», s19 «trust-but-verify», s24 central principle, s27 closing). ✅
- `[с акцентом]` — 2 (s06 «design-driven», s15 «AI ускоряет stages 1-3»). ✅
- Section markers (`[Переход на sNN.]`) — 14 (one after each main slide). ✅
- Stage directions (`[Включаю ноутбук…]`, `[действие: drag-and-drop]`) — 3 (concentrated in s01 live demo). ✅

**Cue density: PASS** — well distributed, not robotic. No «как мы видели на s10» mechanical bridges; all bridges semantic.

**P2 nit.** s11 line 268 «Это парадокс совместной работы. Обратите внимание: пользователи не дозагружают AI: не доверяют, не умеют интегрировать, держат AI на роли «второго мнения», которое можно проигнорировать.» — the term «парадокс совместной работы» is introduced без explicit Russian equivalent of «augmentation gap». Chapter §2.3 uses «augmentation gap» as canonical term; speech translates it elegantly to «парадокс совместной работы», но это is potentially confusing if student later reads chapter and tries to map the term. Cross-artifact terminology drift (minor). See P2 list.

---

## Cross-references integrity

### Course-program compliance (CRITICAL section)

Per task spec: «Lec 5 = Коллоквиум 1, Lec 6 = AI в производстве, Lec 7 = Практикум 1, Lec 12 = Практикум 2, Lec 14 = индивидуальное задание».

Speech alignment:
- ✅ s28 line 638: «Следующее занятие — Коллоквиум 1, Лекция 5».
- ✅ s28 line 640: «После — Лекция 6, AI в производстве и сельском хозяйстве».
- ✅ s28 line 644: «Прогрессия практик: Практикум 1 на Лекции 7, Практикум 2 на Лекции 12».
- ✅ s27 line 630: «Финал — на Лекции 14, в индивидуальном задании».

**Chapter v2 §6.2 alignment:** ✅ Chapter line 576 says «Коллоквиум 1 (Лекция 5)» and line 578 says «После Коллоквиума 1 — Лекция 6 «AI в производстве и сельском хозяйстве»». **Chapter = speech: aligned.**

**Plan-v2 conflict (P1).** Plan v2 line 1216-1221 says «Слайд 28 — Тизер Лекции 5» and «Тизер Лекции 5: AI в производстве и сельском хозяйстве». Plan was approved at GATE 0 with that phrasing. But chapter v2 (GATE A approved) re-frames: «Лекция 5 = Коллоквиум 1, Лекция 6 = производство». Speech v1 follows chapter (correct per book-first source-of-truth rule), but plan is stale and inconsistent. This is **not** a fabricated cross-ref in speech (chapter has it), but it means **plan-v2 is now misaligned** with chapter+speech. Either plan needs an inline addendum или this must be flagged for downstream regression. P1-2 (book-first source of truth → speech correct; risk = downstream artifact uses stale plan).

### Cross-lecture callbacks (Lec 1/6/7/9/12/14)

- ✅ **Lec 1 callback** (YOLO bridge in s01 line 64): «В конце Лекции 1 у нас была камера-демо с YOLO-детектором людей. Chester — родственная история.» Concrete and useful.
- ✅ **Lec 1 callback** (Нобель 2024 in s16 line 366): «Это callback к Лекции 1.» — works if Лекция 1 indeed mentioned Нобель 2024. Chapter §3.2 line 338 confirms: «Это callback к Лекции 1, где Нобелевская премия упоминалась как индикатор зрелости поля». ✅ Assuming chapter is the source of truth.
- ✅ **Lec 6 teaser** (s28 line 640): «Cognitive Agro Pilot: тысяча пятьсот машин в полях, рост эффективности на тридцать-сорок процентов». Same numbers as plan v2.
- ✅ **Lec 7 forward-ref** (s28 line 644): «Практикум 1 на Лекции 7». Plain.
- ✅ **Lec 9 forward-ref** (s27 line 630, s28 line 642): «Это вход в копилку чек-листа на Лекции 9». Multiple consistent references.
- ✅ **Lec 12 forward-ref** (s28 line 644): «Практикум 2 на Лекции 12». Plain.
- ✅ **Lec 14 forward-ref** (s27 line 630): «Финал — на Лекции 14, в индивидуальном задании».

**No fabricated cross-references identified.** All forward refs match chapter §6.2 + course program.

### Missing chapter callbacks (P2)

Chapter §0.1 (line 100) mentions Лекция 1 YOLO callback — speech delivers ✅.
Chapter §4.2 line 437 mentions Лекции 2, 3 callbacks: «в Лекции 2 — на технических деталях, в Лекции 3 — на финансовых данных». Speech s19 (lines 451-472) — the corresponding place to deliver these callbacks — **drops** the Лекция 2/3 mention. Speech says (line 470) «правило для медицины — и для любого контекста с высокими ставками». OK as standalone but loses the cumulative-skill nature of chapter framing. P2 (minor, not load-bearing).

---

## Pre-flight checklist actionability

Lines 25-34 list 8 pre-flight items per author note. Verification:

| # | Item | URL/path/command present? | Freshness protection? | Actionable? |
|---|---|---|---|---|
| 1 | s01 Chester demo | `mlmed.org/tools/xray/` + `assets/test-xray.png` + backup-PNG path | N/A (tool, not data) | ✅ |
| 2 | s04 FDA freshness | `https://www.fda.gov/medical-devices/...aiml-enabled-medical-devices` URL + cached number «1 451» + acceptable bound «1 500-1 550» | ✅ explicit number + bound | ✅ |
| 3 | s12 mosmed freshness | `https://mosmed.ai/` + cached «14 миллионов» | ✅ check Q1 2026 update | ✅ |
| 4 | s19 LLM control-output | concrete prompt text quoted | N/A (sanity-check, not freshness) | ✅ |
| 5 | s22 ChatGPT 40M | `https://www.beckershospitalreview.com/` + search query «ChatGPT healthcare 40 million» | ✅ check ≥40M; if higher — update | ✅ |
| 6 | s07/s11/s17a vocal timing | «прогнать с секундомером» | N/A | ✅ |
| 7 | Wifi backup | concrete fallback (PDF deck + Adobe Reader + Chester backup-PNG) | N/A | ✅ |
| 8 | Часы + бумага | reminder | N/A | ✅ |

**Verdict:** All 8 items have concrete actionable steps. 4 of 8 protect against freshness risk explicitly with cached numbers + verification bound. ✅

**P2 nit.** Item 5 (s22 ChatGPT 40M) — author specifies «Becker's Hospital Review» but **chapter (line 488) cites both Becker's AND Gallup «3 из 5 взрослых»**. Speech (line 528) cites both. Pre-flight only verifies Becker's; if Gallup number has shifted, speech could be stale on Gallup line. Minor — Gallup number is structural («3 из 5» is a coarse fraction unlikely to shift dramatically), but pre-flight could note «verify both». P2.

---

## P0 / P1 / P2

### P0 — none.

### P1 — 9 issues

**P1-1. Anglicism density in s24 4-actor block.**
- **Slide:** s24 (lines 564-590).
- **Issue:** 9 English-loan technical terms in 4 sentences («control, liability, input, decision-maker, primary responsible person, AI-suggestion, full context, AI-output, inputs»). At wpm 84 + dense anglicism load, comprehension margin для 3-курс non-English-native student degrades.
- **Evidence:** «Врач — высокий control, высокая liability. … AI — input, не decision-maker. Юридически врач — primary responsible person. AI-suggestion — «второе мнение». Только врач имеет full context: анамнез, осмотр, лабораторные результаты, AI-output как один из inputs.» (lines 572-573).
- **Recommendation:** Replace minimum 5 of 9 with Russian equivalents. Suggested:
  - `control` → «контроль» / «технический контроль»
  - `liability` → «ответственность»
  - `decision-maker` → «принимающий решение»
  - `AI-suggestion` → «AI-подсказка»
  - `full context` → «полный контекст»
  - keep `liability` где она в parenthetical context («юридическая liability») для legal disambiguation only if necessary
- **Impact:** improves listenability; preserves chapter-canonical terms when needed.

**P1-2. Plan-v2 cross-ref staleness re: Лекция 5.**
- **Section:** s28 (lines 634-644).
- **Issue:** Speech correctly aligns with chapter v2 («Лекция 5 = Коллоквиум 1; Лекция 6 = AI в производстве»), but plan v2 line 1221 says «Тизер Лекции 5: AI в производстве и сельском хозяйстве». Plan v2 was GATE-0 approved; chapter v2 GATE-A approved later overrides. Speech follows chapter (book-first SoT — correct), но plan is now stale.
- **Evidence:** Speech line 638 vs plan-v2 line 1221.
- **Recommendation:** Не правка к речи (speech правильна). Орки/писатель главы должен note: plan-v2 needs inline addendum «Раздел 6.2 chapter v2 supersedes — Лекция 5 = Коллоквиум 1». Add к downstream issue list. Speech itself остаётся as is.

**P1-3. s09 + s10 + s13 cognitive-load cluster + high wpm.**
- **Slides:** s09 (88.5 wpm + 4-stage pipeline + Grad-CAM intro), s10 (90.0 wpm + 4 metrics + Bayes + worked example), s13 (90.0 wpm + 2 bias cases + numbers).
- **Issue:** Three consecutive high-density slides in Раздел 2 (s09 → s10 → s11 → s12 → s13) — pace stays at 88-90 wpm with no cognitive rest until s14 callback. Student attention deficit accumulates. Mayer multimedia learning: dense numerical content требует pause/recap every 3-5 minutes; speech compresses 14 min into back-to-back dense delivery.
- **Evidence:**
  - s10 line 222-248: 4 formulas + Bayes + sens/spec/PPV worked example в 270 words/3 min.
  - s13 line 298-312: dermatology case (Daneshjou 2022, Фитцпатрик scale, DDI) + pulse-ox case (Sjoding 2020, NEJM, FDA 2021) в 225 words/2.5 min.
- **Recommendation:** Add 2 explicit «[пауза 5-7 секунд для понимания]» moments — one after s10 line 248 PPV reveal, one between s13 dermatology and pulse-ox cases. Or — accept that this section requires lecturer to **rehearse with stopwatch** and consciously slow on these 3 slides (frontmatter pre-flight item 6 mentions this but not specifically for s09/s10/s13).

**P1-4. s19 placement inside Раздел 4 «Этика» creates semantic mismatch.**
- **Slide:** s19 (lines 451-474).
- **Issue:** s19 «AI как объяснитель» = prikladnoy/practical content about LLM explanation patterns. It sits inside «Раздел 4. Этика и ответственность» (line 448). Speech line 454 acknowledges this: «Перед тяжёлыми темами — короткая прикладная секция». But the divider s19a (line 442) declared «Четвёртый раздел из пяти — этика и ответственность» — s19 doesn't deliver ethics, it delivers an applied LLM-use pattern. Student gets dissonance: «I was promised ethics, I'm hearing about explain-as-for-student-N».
- **Evidence:** s19a (line 442) declares ethics theme; s19 (line 454) delivers «короткая прикладная секция» about LLM explanation.
- **Recommendation:** Two options:
  - **Option A (minor edit):** Reframe s19a divider to «Четвёртый раздел — границы LLM в медицине: от паттерна к ответственности». Anchors s19 (pattern) → s20 (transition) → s21-24 (ethics) as one continuous narrative.
  - **Option B (structural — defer for v2):** Move s19 to end of Раздел 2 (after s13) as «applied bridge». Risk: requires deck.yaml + slides re-ordering, expensive.
  - **Recommend Option A for v2 polish.**

**P1-5. «design choice» / «design-driven» / «design choices» repeated 4× without Russian equivalent.**
- **Locations:** lines 58, 150, 302, 416.
- **Issue:** Author uses the English «design» as carrier word but never provides Russian gloss. Chapter has both «design choice» and «дизайн-выбор» mixed; speech defaults to English form 4 times. For an oral lecture this term should be either accepted as canonical (then introduced once с явной формой) or replaced.
- **Evidence:** line 58 «design choice»; line 150 «design-driven»; line 302 «consequence design choices»; line 416 «Defect в design».
- **Recommendation:** On line 58 first occurrence, gloss it: «Это не случайность — это **сознательный архитектурный выбор**, design choice по-английски». Subsequent uses inherit context.

**P1-6. «Generative AI не равно rule-based AI» — translation of chapter's «≠» as «не равно».**
- **Location:** s22 line 522.
- **Issue:** «Generative AI не равно rule-based AI.» Reads awkward as oral. Chapter (line 480) uses «generative AI ≠ rule-based AI» as bullet shortcut for written form. Speech translates «≠» literally to «не равно». In Russian oral speech, more natural would be «генеративный AI — это не то же самое, что rule-based AI» or «generative AI — это другая природа системы, не rule-based».
- **Evidence:** speech line 522.
- **Recommendation:** Replace «не равно» with «это не то же самое, что» or similar oral form. Same edit applies to line 516 («LLM в медицине — это не то же самое, что medical AI») — actually that line is already phrased correctly. So this is single-edit fix.

**P1-7. s11 — «augmentation gap» term replaced без cross-artifact sync warning.**
- **Location:** s11 line 268.
- **Issue:** Chapter §2.3 line 254 uses canonical «augmentation gap» as named phenomenon. Speech translates to «парадокс совместной работы» (line 268). The student who reads chapter post-lecture will see «augmentation gap» and won't have anchoring to lecture's term. Term drift — minor but cumulative if multiple terms get this treatment.
- **Evidence:** speech line 268 vs chapter line 254.
- **Recommendation:** Introduce both terms once: «Этот парадокс совместной работы — augmentation gap по-английски — означает, что пользователи не дозагружают AI…». Single sentence fix.

**P1-8. s17a «российский контекст» — extra info-load not warranted by visible slide.**
- **Location:** s17a lines 400 (последние два paragraph).
- **Issue:** s17a is 2.5 min slide at 204 words. It already delivers Rentosertib core (Phase IIa, +98.4 mL FVC, 71 patients, design verifiable). Then speech adds **5 more sentences** of RU context (Центр AIDD, Сбер AI Lab + AIRI, Р-Фарм, MADD on EMNLP 2025, DiMA на ICML 2025, «ни одного российского AI-designed препарата в Phase 1 и выше»). At 81.6 wpm this is delivered but adds 5 named entities + 2 venues + 1 absence claim. Cognitive overload risk — student is still digesting +98.4 mL FVC when 5 new RU entities arrive.
- **Evidence:** speech lines 400-402.
- **Recommendation:** Either:
  - **Option A (preferred):** Move RU context to a separate beat — perhaps add s17c (15-sec mini-block) or merge with s28 «Что дальше». Speech currently makes 17a do double duty.
  - **Option B:** Trim RU context в s17a to one sentence: «В России — Центр AIDD (Сбер AI Lab + AIRI, 2024); RU-программы — пока на preclinical стадии, peer-reviewed Phase 1+ не зафиксировано». Saves ~30 sec; gives 17a recovery slack.

**P1-9. s23 — anglicism + technical density combined.**
- **Slide:** s23 (lines 542-558).
- **Issue:** 3 minutes / 231 words / 77 wpm — OK on paper. But content includes 15+ technical proper nouns/acronyms: «PHI, BlackCat, Citrix remote access, MFA, ransomware, эксфильтрация, Bitcoin, Sweeney 2002, HIPAA, GDPR, ФЗ-152, ФЗ-23, data localization, secure-by-design, OpenAI/Anthropic API noncompliance». For non-cyber-audience the term load is high. WPM is fine but **comprehension WPM** is effectively higher.
- **Evidence:** lines 544-558.
- **Recommendation:** Add «[пауза 3 секунды]» between «$22 миллиона выкупа» and «$2.457 миллиарда» — currently line 548 reads as run-on numbers. Helps anchor magnitude difference.

### P2 — 8 issues

1. **Divider numerator/denominator mismatch.** s05b «первый из пяти» counts Раздел 1-5 (excluding Раздел 0 = Open). Students may notice discrepancy with the 5-block Open. Cosmetic.
2. **«узкое компьютерное зрение» appears 2× in s01 (lines 60, 64) — could collapse to one usage.** Minor repetition.
3. **Lecture 2/3 callbacks dropped from s19.** Chapter §4.2 line 437 mentions «Лекция 2 — технические детали; Лекция 3 — финансовые данные»; speech s19 line 470 generalizes to «контекст с высокими ставками». Loses cumulative-skill framing.
4. **Pre-flight item 5 doesn't include Gallup verification** — chapter cites both Becker's 40M + Gallup «3 из 5». Speech repeats both. Pre-flight only verifies Becker's.
5. **«Бонус. Второго августа 2026 года…»** s08 line 184: «Бонус» is a coloquial conversational marker. OK but chapter uses «actionable timeline (бонус-причина)» — speech can be more deliberate с framing.
6. **«десять-пятнадцать лет и один-два миллиарда долларов» (line 342) — verbal numbers good, but «один-два миллиарда» reads as range; «миллиарда» genitive should be «миллиардов» (один-два миллиарда долларов).** Russian grammar nit — actually «один-два миллиарда» is OK (gen.sg. after numerals 2-4); not a real issue. Withdraw.
7. **s28 mini course-map.** Visual reference (line 636) «mini course-map + Лекция 6 teaser + Lec 9 arrow». Speech delivers Лекция 5 (colloquium), Лекция 6 teaser, Lec 9 forward, Lec 14 final. So visual «Лекция 6 teaser» matches speech (Лекция 6 = производство). Aligned. P2 because deck.yaml s28 entry was likely written before this re-framing; check that the rendered slide has correct labels.
8. **s12 line 286 «маммография, маммография» — duplicate word.** Likely typo from chapter content paste («маммография, оссеоденситометрия» appears in chapter line 276 once; speech repeats). Minor proof.

---

## Top-N приоритизированных правок

1. **(P1-1) Reduce anglicism density в s24 4-actor block.** Replace 5 of 9 English terms with Russian equivalents. ~10 min edit.
2. **(P1-4) Re-frame s19a divider to «Границы LLM в медицине».** Eliminates semantic mismatch between divider promise (ethics) and s19 content (applied LLM pattern). ~3 min edit.
3. **(P1-3) Insert 2 explicit pauses in dense Раздел 2 cluster (after s10 PPV reveal; between s13 dermatology and pulse-ox).** Buys cognitive recovery for student. ~3 min edit.
4. **(P1-8) Trim s17a RU drug discovery context to one sentence.** Saves ~30 sec; gives lecturer slack on overshoot risk. ~5 min edit.
5. **(P1-5) Gloss «design choice» on first occurrence (s01 line 58) with Russian equivalent.** ~2 min edit.
6. **(P1-7) Introduce «augmentation gap» canonical term alongside «парадокс совместной работы» in s11.** ~2 min edit.
7. **(P1-6) Replace «Generative AI не равно rule-based AI» с conversational form.** ~1 min edit.
8. **(P1-9) Add «[пауза 3 секунды]» between Change Healthcare $22M and $2.457B figures.** ~1 min edit.
9. **(P1-2) Cross-reference reconciliation — orchestrator note.** Speech remains as is; plan-v2 needs inline note that chapter v2 supersedes. Out-of-scope for speech revision per se, but flag downstream.

**Total estimated revision time:** ~30 min surgical edits. Не structural rewrite.

---

## What speech does WELL

1. **WPM hard rule respected** на каждом фрагменте — 0 of 30 active slides exceed 95 cap. Average 74.7 wpm matches chapter target.
2. **Source-of-truth discipline.** Speech follows chapter v2 (§6.2 framing: Лекция 5 = Коллоквиум 1, Лекция 6 = производство) rather than stale plan v2. Correctly applies book-first SoT rule.
3. **Central question callback chain complete** — all 7 declared callbacks (s05 → s12 → s14 → s17a → s17b → s24 → s27) present with explicit semantic anchoring («наконец-то пришли к ответу» on s24; «это callback к центральному вопросу лекции» on s27).
4. **LO mapping accurate and conservative** — LO8 framed as «input для черновика Лекции 9», not premature evaluative synthesis. Matches Bloom-level matrix для intermediate lecture (L4-12 = Apply/Analyze level). LO4 correctly omitted (deck v3 removal).
5. **Pre-flight checklist is operationally actionable** — 8 concrete items с URLs/paths/commands; 4 of 8 explicitly protect against freshness risk (FDA cumulative count, mosmed.ai 14M, ChatGPT 40M, Insilico Phase IIa). Author has clearly internalized lec-01 v3 reflection finding «freshness risk for AI-domain content».
6. **Speaker cue density natural** — 13 explicit pauses + 7 «медленно/с акцентом» markers, distributed at climactic moments (s05 central question, s10 PPV reveal, s13 validation set, s24 central principle). No mechanical robotic bridges.
7. **«Мы с вами» inclusivity** — 12 markers per author claim, verified. Distributed: opening (s01, s05), turning points (s12, s14, s17a), closing (s26, s27). No condescending markers, no «угадайте», no «ребята».
8. **No fabricated cross-references.** Every Lec 1/5/6/7/9/12/14 ref is traceable к chapter v2 §6.2 or to declared callback chain. Lec 1 YOLO callback (s01) is concrete and useful; Lec 9 forward-ref (s27, s28) is consistent across 3 mentions.
9. **No forbidden anglicism (hard list).** Zero occurrences of `стейкс/фоллбек/пайплайн/кейс/инсайт/workflow/edge case/фит/деплой/фича/митап`. Chapter's «workflow» was correctly translated к «рабочий процесс» in speech (lines 214, 272, 354). This shows author actively applied lec-01 v3 anglicism cleanup pass.
10. **mosmed.ai «4 миллиарда» caveat preserved** (line 290-292). Chapter §1.2 line 168 introduced the «4 миллиарда руб экономии» dis-claim; speech faithfully delivers it «спокойным тоном» (cue line 290). Honest scholarship made oral.
11. **DSP-1181 + Rentosertib symmetry** intact (s17a vs s17b). Engineering lesson «AI ускорил design — verifiable; clinical efficacy — отдельная биология» appears identically в обоих blocks (lines 398, 416). Methodologically clean pair.

---

## Cross-cutting issues

- **LO coverage gaps:** none — all 4 declared LOs covered.
- **Cognitive load hotspots:** s09-s10-s13 cluster (Раздел 2) — addressed in P1-3.
- **Sequence breaks:** s19 placement в Раздел 4 — addressed in P1-4.
- **Tone drifts:** anglicism density at s24 + scattered «design choice»/«verifiable» — addressed in P1-1, P1-5.
- **Cross-artifact terminology drift:** s11 «augmentation gap» / «парадокс совместной работы» — addressed in P1-7.
- **Source-of-truth conflict:** plan-v2 vs chapter v2 (Лекция 5 framing) — addressed in P1-2 (note for orchestrator, not for speech editor).

---

## DoD enforcement check

| Metric | Required | Actual | Pass? |
|---|---|---|---|
| WPM per fragment ≤ 95 | ≤95 | max 90.0 (s10, s13) | ✅ |
| Active speech length | ~68 min (75 - buffer) | 66.6 min | ✅ |
| Buffer Q&A | 7-10% (5.25-7.5 min) | 6.4-8.4 min (frontmatter claims 7) | ✅ borderline |
| Slide coverage | all 34 slides covered | 34/34 | ✅ |
| LO coverage | LO1, LO2, LO3, LO8 (deck.yaml) | All 4 covered | ✅ |
| Speaker cue distribution | ≥1 cue per 2-3 min | 13 pauses + 7 medlenno = 20 cues / 66.6 min = 1 cue / 3.3 min | ✅ |
| Forbidden anglicism (hard) | 0 occurrences | 0 | ✅ |
| Cross-ref integrity | no fabricated refs | 0 fabricated | ✅ |

**DoD: all metrics PASS. Verdict driven by P1 count (9 > 5), not by DoD failure.**

---

## Final summary

Speech v1 is **operationally show-ready** — пройдёт WPM hard rule, no fabricated cross-refs, LO coverage complete, pre-flight actionable, callback chain intact. However, **9 P1 issues** above APPROVE-WITH-POLISH threshold (4) trigger REVISE. Most issues are surgical 1-5 min edits; total revision budget ~30 min. No structural rewrite needed. The single semantic-mismatch issue (P1-4, s19 in «Этика» divider) is a 1-line divider re-frame.

After P1 fixes applied, speech should reach APPROVE-CLEAN at v2.

**Recommended next step:** apply 8 in-speech surgical edits (P1-1, 3, 4, 5, 6, 7, 8, 9) → re-run methodology-critic on speech v2 → if 0-3 P1 remain → APPROVE-CLEAN, proceed to consistency-checker (Phase 11).

Plan-v2 staleness (P1-2) is **separate downstream task** — does not block speech v2 approval.
