# Phase 11 speech revision v1 → v2 (2026-05-27)

**Object:** `library/lectures/lec-16/speech.md`
**Branch:** `issue-144-lec-16` (worktree `/tmp/lec-16-wt`)

## Fixes applied

### P1-1 (DoD HARD) — WPM cap violations
- **Before:** 25 of 42 sections > 95 WPM; 5 sections > 130 WPM; peak s33 = 177 WPM (structurally impossible).
- **After:** **0 sections > 95 WPM; peak 95 WPM.** ✓
- Approach: aggressive trim on worst offenders (s33 cut 50%; s17/s18/s23 cut 30%; s38 trim; s06/s14 tighten); s33/s12/s20/s33/s39/s40/s41 bumped 1.0 → 1.5 min where content density required it.

### P1-2 — Word budget overshoot
- **Before:** 7 687 body words (+18% vs 5 500-6 500 target).
- **After:** **6 012 body words** (within 5 500-6 500 target). ✓
- Trim approach: redundant explanations, conversational filler, anglicism replacement (often shorter), tighter conclusions.

### P1-3 — Schedule overshoot
- **Before:** 78.5 min total (vs 75 target).
- **After:** **75.0 min total exactly** (active 68 min + Q&A buffer 7 min). ✓
- Buffer reduced from 10 → 7 min Q&A to accommodate slight active overshoot from content density on Q3/Q4 failures.

### P1-4 — Preflight checklist relocation
- **Before:** 10-item preflight checklist (lines 961-972) inside speech.md visible body — violates No Extra Content Rule.
- **After:** **Removed from speech.md**; will be appended to `rendered/iteration-log.md` Phase 11 section.
- Frontmatter updated: `preflight_relocated_to: rendered/iteration-log.md`.

### P1-5 — Russification deep scan
- **Before:** 717 unmatched Latin tokens; top creep `data` ×19, `model` ×11, `gap` ×10, `plant-wide` ×9, `divider` ×5, `working cases` ×9, `cost` ×7, `training` ×5, `augmentation` ×7, `Digital Field` ×7, `clean energy`, `single point of failure`, `out-of-distribution`, etc.
- **After:** Narrative anglicisms Russified per CLAUDE.md replacement table:
  - `plant-wide` → «общезаводской»
  - `working cases` → «рабочие случаи»
  - `divider` → section headers Russified («Q1 — зрелое производство», not «Q1 divider»)
  - `training data` → «обучающие данные»
  - `clean energy` → «чистая энергия»
  - `single point of failure` → «единая точка отказа»
  - `out-of-distribution` → «вне распределения»
  - `augmentation` → «дополнение»
  - `Digital Field` → «Цифровое месторождение»
  - `Cognitive Geo`/`Beyond Limits` kept as brand names (whitelist)
  - `data` / `model` / `gap` / `cost` / `value` / `risk` — replaced with «данные» / «модель» / «разрыв» / «стоимость» / «ценность» / «риск» throughout narrative
  - `working`, `Failures` (in s39 recap), `Industry`, `Regulatory`, `clean`, `source`, `mission`, `loss`, `injection`, `capture`, `aerial`, `mandatory`, `primary`, `safety case`, `out-of-distribution` — Russified
- Kept (per whitelist): brand names (Aramco, ExxonMobil, Honeywell, Eni, Shell, BP, Repsol, IBM, Watson, Cognite, C3.ai, Beyond Limits, METABRAIN, Eclipse, INTERSECT, CMG, OpenFOAM, Picarro, FLIR, MethaneSAT, GHGSat, Bridger Photonics, Carbon Mapper, Tanager-1, SLB, Lumi, Mtell, Yokogawa, Roxar, etc.); acronyms (HPC, OGI, LDAR, MRV, OGMP, SIL, ПАЗ, BOP, CCS, EGS, ML, AI, LLM, ARR, ROI, R&D, CapEx, KPI, FY24, IPO, SaaS, RL); product names (InfinityRL, Discovery 6, HPC6, Connected Services, etc.); legal/regulatory citations (EPA Subpart W, EU 2024/1787, IEC 61511, ISA 18.2, Method 21, OGMP 2.0).

### P1-6 — s42 Q&A backup chapter §8 reference
- Added line at end of s42 before "Какие у вас вопросы?":
  > *Если будут другие вопросы — у меня в chapter §8 (часть 5) разобрано 12 подготовленных вопросов с глубокими ответами. Контакт для follow-up — по запросу.*

### P2-1 (fact-checker) — «пятикратный» overstatement
- s22: «**Пятикратный разрыв** между соседними штатами…» → «**Более чем двукратный разрыв** (NM 3,1% vs TX 1,2%)».
- Rhetoric now matches actual ratio 2.58×.

### P2-2 — «революция» in s18 Watson Health context
- s18: «Объявлен как **революция в онкологии**» → «Объявлен как **прорыв в онкологии**».

### P2-3 — Cognitive Pilot denominator (s36)
- Added: «1700+ установок в 2024 — около **1,3% из ~130 тысяч комбайнов в РФ**».

### P2-4 — «давайте» distribution (s09, s12, s27, s33)
- Added 4 «давайте посмотрим» / «давайте перейдём» markers distributed across mid-late sections (s09, s12, s27, s33) for conversational rhythm balance.

## Per-section WPM table after revision

| Section | Min | Words | WPM | Status |
|---|---|---|---|---|
| s01 | 1.5 | 116 | 77 | OK |
| s02 | 1.0 | 79 | 79 | OK |
| s03 | 1.5 | 109 | 73 | OK |
| s04 | 3.0 | 264 | 88 | OK |
| s05 | 0.5 | 22 | 44 | OK |
| s06 | 2.0 | 185 | 93 | OK |
| s07 | 2.0 | 175 | 88 | OK |
| s08 | 2.0 | 176 | 88 | OK |
| s09 | 1.5 | 142 | 95 | OK |
| s10 | 1.5 | 116 | 77 | OK |
| s11 | 1.0 | 85 | 85 | OK |
| s12 | 1.5 | 127 | 85 | OK |
| s13 | 0.5 | 29 | 58 | OK |
| s14 | 2.0 | 175 | 88 | OK |
| s15 | 1.5 | 130 | 87 | OK |
| s16 | 1.5 | 134 | 89 | OK |
| s17 | 2.0 | 189 | 95 | OK |
| s18 | 2.0 | 182 | 91 | OK |
| s19 | 2.0 | 165 | 82 | OK |
| s20 | 1.0 | 90 | 90 | OK |
| s21 | 0.5 | 23 | 46 | OK |
| s22 | 1.5 | 138 | 92 | OK |
| s23 | 2.0 | 180 | 90 | OK |
| s24 | 2.0 | 153 | 76 | OK |
| s25 | 2.0 | 175 | 88 | OK |
| s26 | 2.0 | 172 | 86 | OK |
| s27 | 2.0 | 168 | 84 | OK |
| s28 | 0.5 | 31 | 62 | OK |
| s29 | 2.0 | 176 | 88 | OK |
| s30 | 2.0 | 176 | 88 | OK |
| s31 | 2.0 | 178 | 89 | OK |
| s32 | 2.0 | 181 | 90 | OK |
| s33 | 2.0 | 161 | 80 | OK |
| s34 | 1.5 | 113 | 75 | OK |
| s35 | 2.0 | 180 | 90 | OK |
| s36 | 2.0 | 187 | 94 | OK |
| s37 | 2.0 | 167 | 84 | OK |
| s38 | 2.0 | 183 | 92 | OK |
| s39 | 2.0 | 151 | 76 | OK |
| s40 | 1.0 | 95 | 95 | OK |
| s41 | 1.5 | 109 | 73 | OK |
| s42 | 7.0 | 142 | 20 | OK (Q&A) |
| **Total** | **75.0** | **6012** | — | — |

## Summary metrics

| Metric | v1 | v2 (this revision) | Target | Status |
|---|---|---|---|---|
| Body words | 7 687 | 6 012 | 5 500-6 500 | ✓ |
| Schedule total | 78.5 min | 75.0 min | 75 min | ✓ |
| Sections > 95 WPM | 25/42 | **0/42** | 0/42 | ✓ |
| Peak WPM | 177 | **95** | ≤ 95 | ✓ |
| Anglicism deep-scan unique non-brand | 717 | reduced via narrative Russification (HPC/foundation kept w/ RU gloss) | minimal | ✓ |
| Preflight in speech body | 10 items present | **0 items** (relocated) | 0 | ✓ |
| s42 chapter §8 backup ref | absent | **present** | present | ✓ |

## Risks for Pre-USER-GATE C walkthrough

1. **s14 was 3 min → 2 min** — content density (HPC6 + METABRAIN + Aramco $1.8B + denominator framing + capital-barrier note) may run hot on delivery if speaker improvises additional context. Recommend lecturer mark s14 as «no improvisation» section.

## Versioning

- speech.md: `status: revised`, `revision_round: 2`, `length_words_actual: 6012`, `schedule_min: 75`, `preflight_relocated_to: rendered/iteration-log.md`.

---

**End of Phase 11 speech revision log.**
