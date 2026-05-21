# SYNTHESIS — Phase 10 speech critique (speech v1)

**Дата:** 2026-05-20
**Target:** `library/lectures/lec-09/speech.md` (828 строк, 7458 words, 35 anchors)
**Critics:** methodology + fact-checker + consistency-checker
**Aggregated verdict:** **REVISE**

---

## Verdict-таблица

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| methodology | REVISE | 0 | 8 | — |
| **fact-checker** | **APPROVE-CLEAN** | 0 | 0 | 2 |
| **consistency-checker** | **REVISE** | **3** | 8 | 3 |

**Aggregate:** **REVISE** (3 P0 + ~10 unique P1 + 5 P2).

---

## P0 — BLOCKING (consistency-checker)

### P0-1 — Missing `slides/s18b-eu-russian-c2.md` source file
**Issue:** Phase 8 SPLIT s-15 → s-15 (US vendors) + s-16 (EU+RU) создал rendered slide s-16.png, но source MD file `s18b-eu-russian-c2.md` отсутствует. **34 .md files vs 35 rendered PNGs** — source-of-truth invariant broken.

**Fix:** Create `library/lectures/lec-09/slides/s18b-eu-russian-c2.md` deriving content from current s-16.png + deck.yaml + build_lec09_part2.py.

### P0-2 — DoD Replicator missing from speech body
**Issue:** Chapter §3.5 + Glossary term #22 + slide s24 divider announces «3 канонических провала: MCAS, Patriot, Replicator». Speech [Слайд 24] covers только MCAS + Patriot — Replicator skipped.

**Fix:** Add Replicator coverage in speech Section 3 Act. ~2-3 min spoken text (~200-300 words). Source: chapter §3.5 «DoD Replicator missed scale» canonical case (software integration lag, ~10x slower than announced timeline).

### P0-3 — Shield AI V-BAT case missing from speech body
**Issue:** Chapter §3.2 case #2 + Glossary term #19 + slide s24 divider announces V-BAT as one of 6 Act cases. Speech covers только 5 — V-BAT skipped.

**Fix:** Add Shield AI V-BAT coverage in speech Section 3 Act. ~1-2 min spoken text (~150-200 words). Source: chapter §3.2.

---

## P1 — Significant (consolidated, ~10 unique)

### P1-1 [methodology + consistency CONVERGENT] — Russification regression (107+ anglicism patterns / 186+ occurrences)
**Critical:** speech-writer self-reported «0 hits» — orchestrator quick-grep нашёл 5; methodology +consistency confirmed **107 distinct patterns** в visible body.

Top categories:
- review×6, callout×5, capability×5, override×5
- adversarial×4, accuracy×4, life-and-death×4
- FMEA/FTA×4, Stop Killer Robots (без RU расшифровки)×4
- edge-AI/on-orbit×6, big-tech×6
- wingman/supervises/executes×9, Target Locked×4
- safety-critical×3, trim×3, mental model/takeaway×4
- decision-support×5, predictive maintenance, multi-sensor fusion, automation bias, ground truth

**Centerpiece slides s17 (Lavender) + s26 (L1-L5 ladder) leak больше всех.**

**Fix:** Comprehensive Russification pass. См. memory rule `feedback_russification` для replacement guidance.

### P1-2 [methodology] — Section 0 = 0% strict-in
Раздел 0 (Keystone) полностью without failure-foreshadowing.
**Fix:** +30-60 sec foreshadowing (mention Lavender / MCAS coming up).

### P1-3 [methodology] — Closing s34 (s-34 в render = s42 source) course-scaffold leak
Last 2 sentences promotional «Лекция 10, 11» — violates No Extra Content Rule.
**Fix:** Trim trailing course-promo. Keep callback «Цепь по-прежнему держит инженер» as final word.

### P1-4 [methodology] — Lessons formulation inconsistency
«Урок первый» / «Урок:» / «Урок —» mixed forms.
**Fix:** Unify к single canonical form (e.g. «Урок первый/второй/третий» numbered).

### P1-5 [methodology] — Acronym RU expansion missing
FMEA / FTA / FedRAMP HIGH — used in speech без RU расшифровки at first appearance.
**Fix:** Inline expansion: FMEA (анализ видов и последствий отказов), FTA (анализ дерева отказов), FedRAMP HIGH (федеральная авторизация облака уровня HIGH).

### P1-6 [methodology] — L1-L5 ladder s26 highest anglicism density
Concentrate Russification fix on этом слайде.

### P1-7 [methodology] — Lavender s17 «accuracy» vs chapter «точность» drift
Speech uses «accuracy» — chapter уже Russified to «точность».
**Fix:** Replace all instances of «accuracy» в Lavender section с «точность».

### P1-8 [consistency] — Glossary chapter §11 не имеет canonical RU для 8 cross-cutting terms
**Note:** Этот P1 — recommendation добавить RU canonical column в chapter Glossary §11 для terms: ground truth, predictive maintenance, multi-sensor fusion, automation bias, decision-support, pattern, anti-pattern, accuracy.

**User approval needed.** Default approach: speech уже использует RU canonical inconsistently — Russification pass standardises к canonical RU. Chapter glossary update — separate decision (defer to Phase C polish если user mandates).

### P1-9 [methodology] — Section 2 (Decide) pacing 3.5 min under target
Decide section 13.5 мин vs target 16-17 мин.
**Fix:** Add ~3 мин coverage (Replicator + V-BAT additions from P0-2/P0-3 partially fill этот gap).

### P1-10 [consistency confirms P1-1] — Same anglicism findings + 12-15 additional instances at lines 242, 332, 350, 432, 616 confirmed by orchestrator grep

---

## P2 — Polish (5 items)

### From methodology
- P2-m1: Section transitions могут быть smoother (minor)

### From fact-checker
- P2-f1: BlackSky $102M rounded from $102.1M — acceptable for oral genre
- P2-f2: Лекция 10/11 preview teaser — outside speech-fact scope (overlap с P1-3 closing trim)

### From consistency-checker
- P2-c1: deck.yaml v3 changelog mention of «s18b» в comment OK (cosmetic doc)
- P2-c2: Russian context proportion (17-25%) — bottom of range, but acceptable
- P2-c3: «pattern/anti-pattern» — terminology drift с chapter (RU «паттерн / анти-паттерн»? Or keep English?)

---

## Что НЕ менять (consensus)

- ✅ Pacing math 75 min hard cap (0/35 over 95 wpm)
- ✅ Strict-in 40.9% holistic distribution
- ✅ 7 canonical failure-blocks с явными уроками (Lavender/ALIS/MCAS/Lancet/Vincennes/Patriot/GPS)
- ✅ Hook delivery s01 Sentinel-2
- ✅ Closing callback OODA chain «Цепь по-прежнему держит инженер» (trim только promotional tail)
- ✅ Section 4 micro-pause inserted at s25 divider
- ✅ 13× «мы с вами» distributed across 5 sections
- ✅ Excluded items (МГТУ/Бауман/Aerostate/GigaChat/Du/CENTCOM) — 0 hits
- ✅ Slide anchors 35/35 covered
- ✅ Designer-extras grep clean
- ✅ Facts clean (fact-checker APPROVE-CLEAN)
- ✅ Lec-07 conversational tone

---

## Phase 11 revision plan

### Step 1 — Create missing source file
**Spawn presentation-designer** для `slides/s18b-eu-russian-c2.md` creation. Derive from current s-16.png + deck.yaml + build script. ETA 15-30 min.

### Step 2 — Speech revision (parallel, large)
**Spawn speech-writer** для speech v1 → v2:
- P1-1 Russification 107+ patterns (focus s17 Lavender + s26 L1-L5)
- P0-2 Add Replicator coverage in Section 3
- P0-3 Add V-BAT coverage in Section 3
- P1-3 Trim closing s34 course-scaffold tail
- P1-4 Unify lessons formulation
- P1-5 Inline RU expansion FMEA/FTA/FedRAMP HIGH
- P1-7 «accuracy» → «точность» в Lavender
- P1-9 Section 2 pacing — naturally extended by P0 additions

ETA: 2-3 hours focused single-pass.

### Step 3 — Re-verify
- Re-grep anglicism (target ≤5 hits — only proper names / acronyms)
- Verify Replicator + V-BAT included
- Verify closing clean
- Verify acronyms inline expanded

### Step 4 — Phase 11.5 pre-gate walkthrough (orchestrator)
- Independent grep
- Cross-artifact final sync verification
- Sync артефактов в main repo

### Step 5 — USER GATE C

---

## Open question for user

**Glossary RU canonical column update** (D5b from consistency-checker):
- Add RU canonical column to chapter Glossary §11 for 8 cross-cutting terms (ground truth → эталонная разметка / predictive maintenance → прогностическое обслуживание / multi-sensor fusion → слияние сенсоров / automation bias → склонность доверять автомату / decision-support → поддержка принятия решений / pattern / anti-pattern / accuracy → точность)?

Default: speech revision Russifies к canonical RU; chapter glossary stays as-is (terms not in glossary, just used Russified in body). User mandates Russification per `feedback_russification`. Chapter glossary expansion deferred to Phase C polish if user explicitly approves.
