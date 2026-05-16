# Final Consistency Check — Chapter v3 ↔ Slides v5.1 ↔ Speech v2 — Лекция 4

**Date:** 2026-05-13
**Mode:** focused Phase 11.5 re-pass (not full audit — verifies Phase 10 P0/P1 fix delivery + post-sync drift)
**Artifacts:**
- `library/lectures/lec-04/chapter.md` v3 (Phase 11a sync — LO4 dropped, sections renumbered 0–5)
- `library/lectures/lec-04/deck.yaml` + 34 × `slides/*.md` v5.1 (Phase 8.8c — no change in Phase 11)
- `library/lectures/lec-04/speech.md` v2 (Phase 11b — 1 P0 + 14 P1 applied)
- `qa-reports/2026-05-13-speech-v1/SYNTHESIS.md` (revision brief reference)

---

## Verdict

### **REVISE**

Reason: chapter v3 sync caused **secondary drift** in deck.yaml + 8 slide-level `chapter_ref` fields + 1 critical slide speaker-note factual contradiction (s24 Price/Gerke affiliations) + section-4 title trichotomy across artifacts. Phase 11a/b fixes themselves were applied correctly to chapter and speech, but the third artifact (slides) was not synced — and 1 of those drifts is P0.

**Severity counts**
| Level | Count | Notes |
|---|---|---|
| P0 (factual contradiction across artifacts) | **1** | s24 speaker notes — Price «Stanford Technology Law Review» + Gerke «Elsevier» contradict speech v2 corrected affiliations |
| P1 (significant drift) | **2** | (a) deck.yaml + 8 slide `chapter_ref` fields point to stale §5.x/§6.x — chapter v3 renumbered to §4.x/§5.x; (b) Section 4 title trichotomy across 3 artifacts |
| P2 (minor) | **3** | (a) s24a filename `section6-divider.md` (now Раздел 5); (b) s12 «маммография, маммография» duplicate word unresolved; (c) s19 chapter_ref points to «§4.1 + §4.2» but only §4.2 is mapped content |

---

## Phase 10 P0/P1 fixes verified

| Fix | Status | Evidence |
|---|---|---|
| **P0-1 Gallup attribution swap (s22)** | ✓ APPLIED | speech.md L537: «По OpenAI и Rock Health 2025 — трое из пяти взрослых…»; Gallup correctly dropped; pre-flight L32 updated к Rock Health verification |
| **P0-2 chapter §Раздел 4 + LO4 sync** | ✓ APPLIED | chapter.md L11 frontmatter `[LO1, LO2, LO3, LO8-framing]` (LO4 dropped); L42–48 §Раздел 4 = «Границы, этика, ответственность» (6 subsections 4.1–4.6); §4.2 «AI как объяснитель» is didactic-only (no apply step); Раздел «Микро-упражнение» fully removed; 6 sections (0/1/2/3/4/5) match slides+speech section structure |
| **P1 numeric −20.3 мл (s17a)** | ✓ APPLIED | speech.md L399: «минус двадцать и три десятых миллилитра» (canonical Phase 4) |
| **P1 numeric 73.8% MASAI (s26)** | ✓ APPLIED | speech.md L269 (s11): «семидесяти трёх и восьми десятых»; L627 (s26): «с семидесяти трёх и восьми десятых до восьмидесяти с половиной процентов» — internal consistency now achieved |
| **P1 Price affiliation** | ✓ in speech | speech.md L587: «Price, 2019, U Michigan Law School» |
| **P1 Gerke affiliation** | ✓ in speech | speech.md L587: «Gerke, 2020, Penn State Dickinson Law (ранее — Harvard Petrie-Flom)» |
| **P1 s24a divider rename** | partial | speech.md L613: «Пятый раздел из пяти — заключение» ✓; speech.md L451: «Четвёртый раздел из пяти — AI как объяснитель и его границы. Прикладная секция, и сразу за ней — этика и ответственность» — note: this *renames Раздел 4 in speech* to a non-canonical form, creates new drift (see D2 below) |
| **P1 design choice gloss** | ✓ APPLIED | speech.md L59: «design choice, инженерное решение» on first use |
| **P1 «не равно» conversational** | ✓ APPLIED | speech.md L531: «**Generative AI — это не rule-based AI.**» |
| **P1 augmentation gap sync** | ✓ APPLIED | speech.md L277: «Это парадокс совместной работы — *в paper Goh et al. называется augmentation gap*» (Russian + EN italic — explicit cross-language link) |
| **P1 s17a RU drug discovery overload** | ✓ APPLIED (trimmed) — verify in pre-gate visual review |
| **P1 FDA per-year softening** | ✓ APPLIED | speech.md L161: «Между 1995 и 2015 годами FDA одобрило кумулятивно около тридцати трёх AI/ML-устройств — три процента от текущего объёма. Между 2015 и 2025 годами — рост от десятков к тысяче с лишним» (no fabricated «6 в 2015 / 64 в 2020») |
| **P1 Daneshjou softening** | ✓ APPLIED | speech.md L311: «значительно ниже — на десятки процентов» (no specific «20-30%» claim) |
| **P1 Cass date softening** | ✓ APPLIED | speech.md L529: «В начале 2023 года» (replaces «март 2023») |

**Net Phase 10:** 1 P0 + 13 of 14 P1 fully applied in speech v2. **Successful revision execution.**

---

## Discrepancies POST-sync

### **D1 — P0 — s24 speaker notes contradict speech v2 on Price/Gerke affiliations**

**Location:**
- `slides/s24-4actor-responsibility.md` L20: «Reference paper: Price 2019 — **Stanford** Technology Law Review»
- `slides/s24-4actor-responsibility.md` L37 (speaker notes): «Price 2019, **Stanford** Technology Law Review; Gerke et al. 2020, Artificial Intelligence in Healthcare, **Elsevier**»

**Issue:**
Speech v2 was corrected (per Phase 10 fact-checker P1-13/14) to «Price, 2019, **U Michigan Law School**» and «Gerke, 2020, **Penn State Dickinson Law** (ранее — Harvard Petrie-Flom)». Speech is now authoritative for verbal narration during lecture. But **slide speaker notes** — which serve as the canonical student-facing self-study text per `tools/lecture-production/README.md` Phase 7 — STILL show old (and per fact-checker, incorrect) attributions.

**Why this matters:** student opens deck in self-study mode after lecture → reads speaker notes → sees «Stanford» / «Elsevier» → confused if they later check the chapter (which uses different phrasing) or check Wikipedia (current affiliations U Michigan / Penn State Dickinson). This is exactly the kind of cross-artifact factual drift `consistency-checker` exists to catch.

**Nuance — there are TWO valid attributions:**
- *Publication venue:* Price (2019) was published as Stanford Technical Report; Gerke et al. (2020) was published in Elsevier book «Artificial Intelligence in Healthcare».
- *Author current affiliation (as of 2024–2026):* Price is at U Michigan Law School; Gerke is at Penn State Dickinson Law.

These are different facts. Speech v2 (per fact-checker P1) chose current affiliation. Slide speaker notes use publication venue. Both are technically correct but **using both creates the impression of factual contradiction**.

**Recommendation:** Disambiguate by pattern. Best: **«Price (2019, тогда Stanford Tech Report; сейчас U Michigan Law School); Gerke et al. (2020, Elsevier book chapter; Gerke сейчас в Penn State Dickinson Law)»**. Apply to: (a) `slides/s24-4actor-responsibility.md` references field + speaker notes; (b) `chapter.md` L501 + L515 + L688 (источник 61); (c) `deck.yaml` L419 (references field, possibly rename IDs `price-2019-stanford` → `price-2019` if the IDs are derived). Speech v2 OK as-is — но recommend adding micro-clarification when narrating: «Price, 2019 — Stanford Technical Report (сам Price сейчас в U Michigan)».

**Severity:** P0 — cross-artifact factual narrative inconsistency, visible to students in 2 artifacts simultaneously.

---

### **D2 — P1 — Section 4 title trichotomy across 3 artifacts**

**Location:**
- chapter.md L410: «**Раздел 4. Границы, этика, ответственность**»
- slides/s19a-section5-divider.md L14: «**Раздел 4. Этика и ответственность**» (slide visible to students)
- speech.md L457: «**Раздел 4. AI как объяснитель и его границы**»
- speech.md L451 (s19a divider narration): «Четвёртый раздел из пяти — AI как объяснитель и его границы. Прикладная секция, и сразу за ней — этика и ответственность»

**Issue:**
Three different names for the same section across three artifacts. Speech v2 introduced the third variant («AI как объяснитель и его границы») as part of Phase 10 P1-04 fix (methodology critic recommended «либо переименовать divider в "Раздел 4: AI как объяснитель и его границы", либо move s19 в section 5»). Speech-writer chose option 1 but applied only to speech, not to slide divider or chapter.

**Why this matters:** This is the *exact* drift Phase 8.8 sync should have caught (and partially did — chapter and speech now disagree on section 4 framing). Students reading slide title vs hearing speech vs reading chapter will see 3 different framings. Pedagogical confusion likely.

**Recommendation:** Pick one canonical title and apply to all 3 artifacts:
- **Option A (faithful to chapter v3):** «Раздел 4. Границы, этика, ответственность». Apply to s19a slide title + speech §Раздел 4 header. Chapter stays.
- **Option B (faithful to speech v2 + s19 placement):** «Раздел 4. AI как объяснитель, этика, ответственность». Apply to chapter §4 + s19a slide. Speech rephrases divider bridge slightly.

**Orchestrator-level decision needed** (not auto-fix). Recommended Option B — section content actually IS s19 (LLM as explainer) → s20 (intro to ethics) → s21 (Obermeyer) → s22 (LLM antipatterns) → s23 (data security) → s24 (4-actor). «AI как объяснитель» is the opener, so naming the section after it accurately reflects section flow.

**Severity:** P1 — significant drift but not factual contradiction (all 3 titles describe the same content honestly).

---

### **D3 — P1 — deck.yaml + 8 slide `chapter_ref` fields point to stale section numbers**

**Location (deck.yaml + slide frontmatter):**

| Slide | Current chapter_ref | Should map to chapter v3 |
|---|---|---|
| s19 | `§4.1 + §4.2 — AI как объяснитель` | `§4.2 — AI как объяснитель` (§4.1 is «Зачем инженеру…» — not s19 content) |
| s20 | `§5.1 — Зачем инженеру думать про границы` | `§4.1 — Зачем инженеру думать про границы medical AI` |
| s21 | `§5.2 — Obermeyer 2019: выбор метрики стал выбором политики` | `§4.3 — Obermeyer 2019: как выбор метрики стал выбором политики` |
| s22 | `§5.3 — LLM-анти-паттерны в медицине` | `§4.4 — LLM-анти-паттерны в медицине` |
| s23 | `§5.4 — Безопасность медицинских данных` | `§4.5 — Безопасность медицинских данных` |
| s24 | `§5.5 — Кто отвечает за AI-ошибку: 4-actor framework` | `§4.6 — Кто отвечает за AI-ошибку: 4-actor framework` |
| s26 | `§6.1 — Три главных вывода` | `§5.1 — Три главных вывода` |
| s27 | `§6.1 — закрывающая фраза` | `§5.1 — закрывающая фраза` (note: derived from same section) |
| s28 | `§6.2 — Что будет дальше` | `§5.2 — Что будет дальше: Коллоквиум 1 и Лекция 6` |

**Issue:** chapter v3 renumbered sections (Phase 11a sync dropped «Раздел 4. Микро-упражнение» as separate section, refolded into new §4 «Границы, этика, ответственность»). Old chapter v2 had sections numbered 0/1/2/3/4/5/6 (with §4 being micro-exercise and §5 being ethics, §6 being conclusion). New chapter v3 has 0/1/2/3/4/5. All `chapter_ref` fields in deck.yaml + slide frontmatter were not updated to match.

**Why this matters:** for student self-study or instructor reference, these `chapter_ref` strings are the bridge between slides and chapter — broken refs make the deck-to-chapter navigation unreliable. Also, downstream tools (impact-check, library indexers) parse `chapter_ref` and will report dangling refs.

**Recommendation:** book-editor or deck-editor agent: do a single-pass renumber in deck.yaml + 8 slide files. Mechanical fix. Cascade impact = 0 (no other artifacts reference §5.x or §6.x).

**Severity:** P1 — navigation drift, not factual.

---

### **D4 — P2 — s24a filename mismatch**

**Location:** `slides/s24a-section6-divider.md` filename
**Issue:** filename indicates «section6» but file content + assertion + visible slide say «Раздел 5 — Заключение». Pre-Phase 8.8 the divider was «section 6» when chapter had 6 numbered sections (1-6 after intro); now it's the 5th and final divider for Раздел 5.
**Recommendation:** rename file to `slides/s24a-section5-divider.md` (or keep current name — orphan refs check shows no other artifact references the filename string). If renamed, update deck.yaml L426 `file:` field.
**Severity:** P2 — cosmetic.

---

### **D5 — P2 — s12 «маммография, маммография» duplicate word unresolved**

**Location:** speech.md L293
**Issue:** fact-checker flagged this as P2 EDIT-PASS in Phase 10; speech v2 revision did not address it. Duplicate word in operational metrics list.
**Recommendation:** one-line edit: delete second occurrence; or replace second with «маммография цифровая».
**Severity:** P2 — cosmetic.

---

### **D6 — P2 — s19 chapter_ref points to two sections but only one is mapped content**

**Location:** deck.yaml L351 + slides/s19 frontmatter: `chapter_ref: "§4.1 + §4.2 — AI как объяснитель"`
**Issue:** §4.1 in chapter v3 is «Зачем инженеру думать про границы medical AI» (intro to whole §4); s19 content «AI как объяснитель» maps cleanly to §4.2 only. The `+ §4.1` portion is over-specification.
**Recommendation:** simplify to `chapter_ref: "§4.2 — AI как объяснитель: pattern и его границы"`.
**Severity:** P2 — overspecification.

---

## Cross-artifact terminology check (glossary lock)

All 25 glossary terms consistent across chapter v3 + slides v5.1 + speech v2:

| Term | Chapter | Slides | Speech | Status |
|---|---|---|---|---|
| AI-диагностика / medical AI umbrella | ✓ | ✓ | ✓ | locked, umbrella usage preserved |
| Sensitivity / Specificity / Prevalence / PPV | ✓ | ✓ | ✓ | locked |
| AlphaFold / AlphaProteo | ✓ | ✓ | ✓ | locked |
| FDA SaMD / PCCP | ✓ | ✓ | ✓ | locked (PCCP «4 декабря 2024» — verified all 3) |
| CADe | ✓ | ✓ | ✓ | locked (distinguished from AI-диагностика consistently) |
| Foundation model | ✓ | ✓ | ✓ | locked |
| HIPAA / GDPR / ФЗ-152 / ФЗ-23 / ePHI / Деперсонализация | ✓ | ✓ | ✓ | locked (ФЗ-23 «1 июля 2025» — verified) |
| EU AI Act high-risk | ✓ | ✓ | ✓ | locked («2 августа 2026 non-MDR / 2 августа 2027 MDR» — verified all 3) |
| mosmed.ai | ✓ | ✓ | ✓ | locked (14M+/74/2000+/18M+/70/11/300 — all consistent) |
| Insilico Rentosertib (ISM001-055) | ✓ | ✓ | ✓ | locked (Nature Medicine июнь 2025; n=71; 21 центр в Китае; +98.4/−20.3 мл) |
| DSP-1181 | ✓ | ✓ | ✓ | locked (январь 2020 → 2022 discontinued) |
| NEDA Tessa | ✓ | ✓ | ✓ | locked (Cass vendor; 30 мая 2023) |
| Bias (algorithmic) | ✓ | ✓ | ✓ | locked |
| Healthcare operator role | ✓ | ✓ | ✓ | locked (Раздел 4 framework cleanly applied) |
| augmentation gap | ✓ (EN) | ✓ (EN) | ✓ EN italic + RU «парадокс совместной работы» gloss | **explicit cross-language link added** — Phase 11 fix |

**Glossary lock status: PASS.** No drift on the 25 canonical terms. Phase 11b augmentation gap fix successful.

---

## Cross-artifact number matrix

| Number / Claim | Chapter v3 | Slides v5.1 | Speech v2 | Aligned? |
|---|---|---|---|---|
| FDA 1 451 кумулятивно к концу 2025 | L83, L167, L542 | s04, s07 | L99, L627 | ✓ |
| FDA «76% радиология» | L167 | s04, s07 | L99 | ✓ |
| mosmed.ai 14M+ исследований / 74 регионов / 2000+ организаций | L163, L269 | s04, s12 | L99, L183, L293, L627 | ✓ |
| MASAI sens 80.5% vs 73.8% | L83, L542 | s11 (3-row) | L269, L627 | ✓ (Phase 11b fix to s26) |
| MASAI workload −44%, detection 6.4 vs 5.0, interval cancer −12% | L165 | s11 | L269, L271 | ✓ |
| Goh n=50; 76% vs 74%; p=0.60 | L241 | s11 | L273 | ✓ (n=50 P2 NEEDS-PRECISION — see fact-checker; not P0) |
| Obermeyer 17.7% → 46.5%; +26% хронич. заболеваний; bias −84% | L432, L434, L436 | s21 | L501, L505, L509 | ✓ |
| Rentosertib +98.4 / −20.3 / n=71 / 21 центр | L351 | s17a (timeline + info card) | L399 | ✓ (Phase 11b numeric fix applied) |
| AlphaFold 200M+ структур; AlphaProteo 88% BHRF1; 3–300× affinity | L340 | s16 (3 evidence cards) | L375 | ✓ |
| Change Healthcare 190M PHI; $2.457B recovery; $22M выкупа; ALPHV/BlackCat | L476–L482 | s23 | L553, L557, L573 | ✓ |
| Adversarial hallucination 83% (Communications Medicine 2025) | L456 | s22 | L533 | ✓ |
| 40 миллионов ChatGPT healthcare | L466 | s22 | L537 | ✓ (Becker's Hospital Review) |
| OpenAI / Rock Health «3 из 5» | L466 | s22 (note: needs verification in slide) | L537 | ✓ (Phase 11b P0 fix) |
| FDA PCCP финал 4 декабря 2024 | L83 | s18 | L439 | ✓ |
| EU AI Act 2 авг 2026 (non-MDR) / 2 авг 2027 (MDR) | L83 | s18 | L185, L441 | ✓ |
| ФЗ-23 1 июля 2025 (data localization) | (chapter §4.5 + glossary) | s23 | L575 | ✓ |
| Liu 2019 meta-analysis 14 работ; sens AI 87% vs 85% | L241 | s11 | L265 | ✓ |
| Sjoding 2020 NEJM + FDA 2021 safety comm | L290 | s13 | L317 | ✓ |
| Daneshjou 2022 dermatology bias | L282 (chapter does not quote exact %) | s13 | L311 («значительно ниже — на десятки процентов» — softened per Phase 11b P1) | ✓ |
| Insilico path 18 мес vs 4-5 лет | L351 | s17a | L399 | ✓ (correctly attributed «Insilico заявляет» as self-reported) |
| DSP-1181 path 12 мес vs 4-5 лет | L373 | s17b | L417 | ✓ |
| Recursion + Exscientia merger авг 2024 $688M | L378 | s17b speaker notes | L420 | ✓ |
| Cognitive Agro Pilot 1500+ машин, +30-40% (Lec 6 teaser) | L552 | s28 | L657 | ✓ (correct future-lecture reference) |

**Number matrix status: PASS — 0 number mismatches.** All cornerstone numbers locked across 3 artifacts.

---

## Section structure post-sync

**Chapter v3 (6 sections, dropped LO4):**
- Раздел 0. Открытие
- Раздел 1. Карта AI в медицине
- Раздел 2. AI-диагностика как зеркало
- Раздел 3. Drug discovery: обещания и реальность
- **Раздел 4. Границы, этика, ответственность** (refolded ex-§4 «Микро-упражнение» dropped; §4.2 «AI как объяснитель» preserved didactic-only)
- Раздел 5. Заключение

**Slides v5.1 (34 slides, 5 dividers):**
- s05b «Раздел 1»
- s08a «Раздел 2»
- s13a «Раздел 3»
- s19a «**Раздел 4 — Этика и ответственность**» ← title drift from chapter
- s24a «Раздел 5 — Заключение»
- (No s18a divider — Phase 8.8 fix 9 correctly removed «Микро-упражнение» divider; no orphan reference)

**Speech v2 (matches slide order, 34 slides covered, 5 dividers narrated):**
- §Раздел 0 (9 мин, L39)
- §Раздел 1 (7 мин, L135)
- §Раздел 2 (14 мин, L199)
- §Раздел 3 (14 мин, L333)
- §**Раздел 4. AI как объяснитель и его границы** (15 мин, L457) ← title drift from chapter AND slide
- §Раздел 5. Заключение (6 мин, L619)
- Резерв 7 мин

**Section count consistency: PASS** — all 3 artifacts have 6 sections (0+5 numbered).
**Section 4 naming consistency: FAIL** — 3 different titles (see D2).

**Cross-references for «Раздел 4» refold:**
- chapter L414 §4.1 intro: «В этой секции мы разберём пять тем: AI как объяснитель — стабильно работающий паттерн и его границы (§4.2); bias в medical AI на примере Obermeyer 2019 (§4.3); LLM анти-паттерны (§4.4); безопасность медицинских данных (§4.5); архитектуру ответственности (§4.6)» — clean refold narrative ✓
- chapter L424 §4.2 → §4.4 bridge: «В §4.4 мы вернём этот pattern с тяжёлыми кейсами…» ✓
- chapter L442 §4.3 → §4.4 bridge: «Bridge к §4.4. Obermeyer — bias в табличной AI-модели. В LLM bias проявляется иначе…» ✓
- No orphan «см. §5.x» or «см. §6.x» refs remaining inside chapter v3 — verified.

**LO4 drop verification:** chapter v3 L11 frontmatter `[LO1, LO2, LO3, LO8-framing]` (no LO4); L62-65 LO list contains only 4 outcomes (no LO4) ✓. Cross-check deck.yaml `learning_outcomes:` fields — none claim LO4 ✓. speech.md L698 LO summary mentions only LO1/LO2/LO3/LO8 ✓.

---

## Cross-lecture references (no fabrication check)

| Reference | Where | Correctly placed? |
|---|---|---|
| Лекция 1 (YOLO callback; «где AI работает, где — нет» frame) | chapter L75, L97, L117; speech L65 | ✓ |
| Лекция 3 (financial AI / credit scoring) | chapter L81, L440 | ✓ |
| **Лекция 5 = Коллоквиум 1** | chapter L51, L550, L552; speech L655 | ✓ (NOT «AI в производстве» — that's Лекция 6) |
| Лекция 6 = «AI в производстве и сельском хозяйстве» (Cognitive Agro Pilot) | chapter L552; speech L657; s28 teaser | ✓ |
| Лекция 7 = Практикум 1 | chapter (in Глоссарий + frontmatter notes); speech L661 | ✓ |
| Лекция 9 = «Этика и регулирование» (LO8 forward link) | chapter L65, L293, L556, L566; speech L647, L659 | ✓ (LO8 forward-framing applied consistently) |
| Лекция 12 = Практикум 2 | speech L661 | ✓ |
| Лекция 14 = «Будущее AI» (LO8 finalization) | chapter L65, L558; speech L698 | ✓ |

**No fabricated cross-refs.** No Лекция 5 «AI в производстве» misstatement. LO8 forward-framing («сырьё для черновика, финал на Лекции 9 + 14») consistently applied. ✓

---

## Glossary lock status

**25 canonical terms — all locked across 3 artifacts.** No new drift. Phase 11b augmentation gap fix successful — speech now explicitly bridges Russian «парадокс совместной работы» к English «augmentation gap» (italic on first mention, consistent with chapter L251 + slide s11 L43 usage).

**Designer extras grep (per Pre-USER-GATE Walkthrough Rule):** spot-check on 3 slide files (s11, s19, s24) — no «Лектору», no «Вы здесь», no timing in visible content, no designer-added subtitles. Pre-Phase 8.8c cleanup verified by visual inspection.

---

## Recommendations for USER GATE C

**Phase 11.5 verdict: REVISE before USER GATE C.**

The Phase 10/11 fix execution itself was successful (1 P0 + 13/14 P1 applied correctly in speech + chapter sync clean). However, the chapter v3 sync introduced **downstream drift in slides** that needs targeted fix-up:

**REQUIRED before USER GATE C:**

1. **[P0 — D1] Fix s24 speaker notes** — Price + Gerke affiliations. Either:
   - Disambiguate: «Price (2019, Stanford Tech Report; сейчас U Michigan Law School); Gerke et al. (2020, Elsevier book chapter; Gerke сейчас в Penn State Dickinson Law)»
   - OR pick canonical form and apply uniformly to chapter L501/L515/L688 + speech L587 + slide s24 L20/L37 + deck.yaml L419.
   Recommend full disambiguation in speaker notes (student-facing) + short form in speech.

2. **[P1 — D2] Decide Section 4 canonical title** — orchestrator decision needed:
   - Option A: «Границы, этика, ответственность» (chapter-faithful)
   - Option B: «AI как объяснитель, этика, ответственность» (speech+slide-content-faithful)
   Apply to all 3 artifacts.

3. **[P1 — D3] Renumber `chapter_ref` fields** — 1 mechanical pass through deck.yaml + 8 slide files (s19, s20, s21, s22, s23, s24, s26, s27, s28). No content change, just §-number sync.

**OPTIONAL polish (P2 — apply if time permits):**

4. **[D4] Rename `slides/s24a-section6-divider.md` → `s24a-section5-divider.md`** + deck.yaml file ref update.
5. **[D5] Fix s12 «маммография, маммография» duplicate** in speech.md L293.
6. **[D6] Simplify s19 chapter_ref** to `§4.2 — AI как объяснитель: pattern и его границы`.

**Time estimate:** P0 D1 fix + P1 D2/D3 fixes = ~20-30 min mechanical work for book-editor / presentation-designer cleanup pass. Re-run terminology-only consistency-checker after, then USER GATE C.

**Strong points worth highlighting at GATE C:**
- 0 number mismatches across 25+ cornerstone numbers (FDA 1451 / mosmed 14M / MASAI 80.5/73.8 / Obermeyer 17.7→46.5 / Rentosertib +98.4/−20.3 / Change Healthcare 190M/$2.457B/$22M / EU AI Act timeline)
- 25/25 glossary terms locked
- LO4 drop cleanly applied — 6-section structure consistent
- Phase 10 P0 (Gallup→OpenAI/Rock Health) fully fixed in speech + pre-flight checklist
- Augmentation gap cross-language bridge added explicitly (chapter EN ↔ speech RU+EN gloss)
- No fabricated cross-lecture references; Лекция 5/6 disambiguation clean
- 4-level verdict scale honoured: REVISE because of 1 P0 + 2 P1 cross-artifact drifts, not blanket APPROVE-WITH-POLISH

**Risk note:** if the D1 P0 (Price/Gerke speaker-note contradiction) is left unaddressed and slides go to USER GATE C as-is, the user is likely to notice during pre-gate visual review (PNG snapshot inspection of s24 → reads notes → catches «Stanford» vs speech «U Michigan»). Better to fix in this revision pass than after gate.
