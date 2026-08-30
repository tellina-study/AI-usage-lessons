# 3-way consistency check — chapter ↔ slides ↔ speech Лекция 16

**Date:** 2026-05-27
**Phase:** 10 (post-speech draft)
**Artifacts reviewed:**
- Chapter v2.1 (5 parts, 32 309 слов)
- Slides v3 (42 slides, deck.yaml + slides/*.md, rendered/lec-16.pptx)
- Speech v1 (7 795 слов)

**Verdict:** **REVISE**

## Summary

Cross-artifact 3-way check found **2 значимых terminology drift'а P1**, **1 значимое coverage misalignment P1** + ряд P2. **Numbers / cornerstones / failure cases / vendor names / slide-маркеры / orphan refs — все aligned**. Главная проблема — chapter v2.1 не был обновлён после Phase 8.6 owner feedback rename (Item 4 «процессов» + Item 6 «новые опоры»); slides s02/s03/s40 — частично обновлены (s04 keystone обновлён, но s02 cover + s03 lecture-map + s40 cornerstones остались на old labels); speech полностью обновлён. Третье — s01 hook visual radically changed (VIIRS flares → YOLOv8 tank detection) per Phase 8.6 Item 1, но chapter Introduction остался про Permian VIIRS.

**Net assessment.** Все 3 артефакта смотрят на одну и ту же лекцию с одинаковыми тезисами / цифрами / failure caseset. Drift — на уровне terminology cascade incomplete после Phase 8.6 owner rename. **Phase 11 cascade-revise rectify**, не структурная переработка. После 3 точечных правок (chapter axis labels + chapter Q4 naming + chapter Introduction hook OR ack note + s02/s03/s40 slides labels) → APPROVE-WITH-POLISH.

## Severity counts

- **P0 (factual contradiction / missing coverage):** 0
- **P1 (significant drift):** 3
- **P2 (minor inconsistency):** 4

## Check results (10 zones)

### 1. Keystone axis terminology — **P1 DRIFT**

**Expected (per Phase 8.6 Item 4 owner rename):**
- «доступность данных × **определённость процессов**» (NEW canonical)
- ❌ NOT «определённость физики» / «данные × физика» (OLD)

**Actual usage (cross-artifact grep):**

| Artifact | NEW «процессов» | OLD «физики» / «физика» |
|---|---|---|
| `chapter.md` | 0 | **5 hits** (frontmatter, TOC, intro, §0 title, §7.3) |
| `chapter-part2.md` | 0 | 0 |
| `chapter-part3.md` | 0 | **2 hits** (Q4 R4 references) |
| `chapter-part4.md` | 0 | **3 hits** (R7 closing + cornerstone) |
| `chapter-part5.md` | 0 | **1 hit** |
| `slides/s04-keystone-matrix.md` (canonical keystone slide) | **8 hits** ✓ | 0 |
| `slides/s02-cover.md` | 0 | **4 hits** ❌ |
| `slides/s03-lecture-map.md` | 0 | **2 hits** ❌ |
| `slides/s40-three-cornerstones.md` | 0 | **1 hit** ❌ |
| `speech.md` | 4 hits ✓ | 0 |

**Issue:** keystone-axis рename per Phase 8.6 Item 4 был **partial cascade** — обновлены только s04 + speech; chapter (все 5 частей, 11 hits) + slides s02, s03, s40 (7 hits) остались на «определённость физики» / «данные × физика». Student увидит на cover (s02) one axis label, на keystone (s04) — другой, в speech лектор скажет третье consistent с s04, а в chapter Q&A backup — четвёртое.

**Examples:**
- `chapter.md` L22 frontmatter: `keystone_axis: "Матрица «доступность данных × определённость физики»"`
- `chapter.md` L65 TOC heading: «Несущая ось: матрица «данные × физика»»
- `slides/s02-cover.md` L30: «Шесть разделов через матрицу данные × физика»
- `slides/s04-keystone-matrix.md` L20: «Матрица «доступность данных × **определённость процессов**»»
- `speech.md` L65: «матрица **доступность данных × определённость процессов**»

**Severity:** **P1** — student-facing inconsistency на keystone оси, которая является **главным** конструкцией лекции и используется на каждом 8-10 минутном returns (per s04 speaker notes).

**Recommendation:** chapter v2.1 → v3 cascade `s/определённость физики/определённость процессов/g` + `s/данные × физика/данные × процессы/g` (11 hits) + slides s02/s03/s40 (7 hits). Speech уже clean. **Effort:** ~15 мин cascade edit.

---

### 2. Q4 quadrant naming — **P1 DRIFT**

**Expected (per Phase 8.6 Item 6 owner rename):**
- «Q4 — **Новые опоры (CCS + EGS)**» (NEW canonical)
- ❌ NOT «Q4 — Энергетический переход» (OLD)

**Actual usage:**

| Artifact | NEW «новые опоры» | OLD «энергетический переход» |
|---|---|---|
| `chapter.md` | 0 | **1 hit** (§0.3 «Q4. Энергетический переход») |
| `chapter-part2.md` | 0 | **1 hit** (cross-link «Q4 energy transition») |
| `chapter-part3.md` | 0 | **3 hits** (chapter-part3 title, §4 section heading, R4 title) |
| `chapter-part4.md` | 1 hit | **1 hit** (§7.1 synthesis still says «Q4 energy transition») |
| `chapter-part5.md` | 0 | 1 hit |
| `slides/s28-q4-divider.md` | 3 hits ✓ | 0 |
| `slides/s31` + others | 2+ hits ✓ | 0 |
| `speech.md` | 3 hits ✓ | 0 |

**Issue:** аналогично keystone — Phase 8.6 Item 6 rename cascade был incomplete. Chapter удерживает «энергетический переход» в:
- `chapter.md` §0.3 keystone definition (L197): «**Q4. Энергетический переход (low data + low physics).** CCS и EGS.»
- `chapter-part3.md` L5 title: «Часть 3: Раздел 3 — Q2 метановая MRV + Раздел 4 — Q4 энергетический переход»
- `chapter-part3.md` L28: «§ Раздел 4. Q4 — энергетический переход: AI и физика struggle вместе»
- `chapter-part3.md` L275: section heading «## § Раздел 4. Q4 — энергетический переход»
- `chapter-part4.md` L279 §7.1 synthesis: «**Q4 (energy transition — low data + low physics):**»

Slides и speech полностью обновлены на «новые опоры (CCS + EGS)». Frontmatter `slide_map: Q4_new_pillars` обновлён, но body text — нет.

**Severity:** **P1** — second-most-prominent keystone label, student увидит «Q4 новые опоры» на section divider (s28) + cornerstone slide (s40 bottom) + speech, но в chapter §0.3 и §4 — «энергетический переход».

**Recommendation:** chapter v2.1 → v3 cascade `s/Q4. Энергетический переход/Q4. Новые опоры (CCS + EGS)/g` + `s/энергетический переход/новые опоры/g` где speaks про Q4 (be careful: «энергетический переход» as general industry term — KEEP; only Q4 *label* renames). **Effort:** ~10 мин.

---

### 3. s01 Hook — chapter Introduction misalignment — **P1**

**Expected:** s01 visual + speech opening describes same hook material that chapter Введение sets up.

**Actual:**
- **s01 slide** (per Phase 8.6 Item 1 re-acquisition): **YOLOv8-OBB oil tank detection** on Ultralytics blog image. Title: «YOLOv8 видит каждый резервуар.»
- **Speech [s01 · 2 мин]:** opens with «реальный output модели YOLOv8 — computer vision, который видит каждый резервуар». Matches slide. ✓
- **Chapter Введение** (chapter.md L99-107, `[for-slide-s01]` marker L103): describes **Permian basin VIIRS flares — 2 593 факельных шлейфа / 34 000 тонн метана в час**. **Completely different hook** about gas flares (ESG/scale framing), NOT about computer vision / YOLOv8.

**Issue:** chapter Введение was not updated when Phase 8.6 Item 1 re-acquired s01 hero from VIIRS flares to YOLOv8 tanks. Student reading chapter and slides separately gets 2 different opening hooks. The for-slide marker `[for-slide-s01]` in chapter points to Permian VIIRS section, but the slide is about YOLOv8.

**Severity:** **P1** — coverage gap. If owner intended VIIRS Permian as backup material for chapter (still works as cost-asymmetry / scale anchor), then chapter Введение is fine but needs a paragraph acknowledging «slide hook is YOLOv8 — see also s01 speaker notes». If VIIRS was meant deprecated, chapter Введение needs rewrite to YOLOv8 hook.

**Recommendation (book-first per CLAUDE.md):**
- **Option A (preferred):** keep chapter Введение's Permian VIIRS material as standalone deep-context. Add a 2-3 sentence opening paragraph: «На презентационном слайде s01 студент увидит другой hook — реальный output YOLOv8-OBB на резервуарах нефтепромысла, иллюстрирующий production-grade AI. Здесь в главе мы расширяем эту картину до отраслевого масштаба: Permian flares как cost-asymmetry якорь.»
- **Option B:** rewrite chapter Введение opening к YOLOv8 hook to match slide+speech. More work, loses VIIRS context.

**Effort A:** ~10 мин. **Effort B:** ~30-40 мин + revisits §1.4 Ambyint Permian context.

---

### 4. Number consistency — **OK**

Sample 12 measurable claims verified across all 3 artifacts:

| Claim | Chapter | Slide | Speech | Aligned? |
|---|---|---|---|---|
| Aramco $1,8B / $436,6B = 0,41% | ✓ part1 L125 + part5 | s14 L15 visible_numbers + L41 | s01 L37, s14 L300-302 | ✓ |
| MethaneSAT 15,5 мес / $88M / $5,7M/мес | ✓ part3 L96, L102 | s23 L16, L33 | s23 L498, L512 | ✓ |
| MethaneSAT loss date «20 июня 2025» | ✓ part3 | s23 L25 | s23 L494 | ✓ |
| Fervo IPO $27/share / $1,89B / $7,7B / ~30% pop | ✓ part3 L327, part5 L279 | s30 L15, L32 | s30 L662 | ✓ |
| Fervo dual scale (40× US / 0,2% IEA 2050) | ✓ part3 L327, L337 | s30 L40, L41 | s30 L666-668 | ✓ |
| Northern Lights 1,5 Mt / 7,6 Gt / 190× | ✓ chapter §0.3 L197, part3 | s29 L29, L38-41 | s29 L638 | ✓ |
| 86% pilot stuck (BCG/McKinsey) | ✓ chapter §1.2 L257 | s06 + bottom bar многих | s06 L121, L141 | ✓ |
| 4× discrepancy 15 Mt vs 4 Mt | ✓ part3 | s25 L20, L31-33 | s25 L548-552 | ✓ |
| Deepwater Horizon 11 deaths / $60B / 20% rev | ✓ part4 L233-234 | s38 L41 | s38 L853 | ✓ |
| 2020 crash 107k jobs / 1,1M / 9,7% | ✓ part4 L207 | s38 L30 | s38 L847 | ✓ |
| Cyber +935% | ✓ part4 L169 | s37 | s37 L815 | ✓ |
| Colonial $4,4M / 5 500 миль / 6 days | ✓ part4 L169 | s37 | s37 L821 | ✓ |

**Net:** numbers cleanly aligned. Phase 8 cascade fix-up для numerical claims прошёл well.

---

### 5. Slide-маркеры reverse mapping — **OK**

Chapter содержит **39 уникальных `[for-slide-sNN]` маркеров** (s01-s41 covered кроме s02, s03, s42 — meta slides). Все 39 → resolved к existing slide IDs в deck v3. Нет orphan-маркеров.

Speech содержит slide refs `[s01 · ... · s42 · ...]` для всех 42 slides — все match deck.yaml IDs. **No orphans.**

---

### 6. 10 documented failures — **OK**

All 10 failures + bonus Deepwater Horizon historical anchor present в всех 3 артефактах:

| # | Failure | Chapter | Slide | Speech |
|---|---|---|---|---|
| 1 | BP + Beyond Limits | ✓ part2 §2.5 | ✓ s17 | ✓ s17 L350-374 |
| 2 | IBM + Repsol Kalimba | ✓ part2 §2.6 | ✓ s18 | ✓ s18 L380-404 |
| 3 | Cognite IPO postpone | ✓ part1 §1.7 | ✓ s11 | ✓ s11 L244-254 |
| 4 | C3.ai O&G declining | ✓ part1 §1.7 | ✓ s11 | ✓ s11 L250 |
| 5 | MethaneSAT loss | ✓ part3 §3.3 | ✓ s23 | ✓ s23 L490-516 |
| 6 | 86% pilot stuck | ✓ part1 §1.2 | ✓ s06 | ✓ s06 L121 |
| 7 | Aspen alert fatigue + refinery stagnation | ✓ part1 §1.3 + part3 §4.5 | ✓ s07 + s32 | ✓ s07 + s32 |
| 8 | 2020 oil crash | ✓ part4 §6.2 | ✓ s38 | ✓ s38 L847 |
| 9 | 4× discrepancy | ✓ part3 §3.5 | ✓ s25 | ✓ s25 L548 |
| 10 | Cyber +935% | ✓ part4 §6.1 | ✓ s37 | ✓ s37 L815 |
| bonus | Deepwater Horizon 2010 | ✓ part4 §6.3 | ✓ s38 | ✓ s38 L853 |

All 11 failure references resolved. Recap on s40 + s41 also matches speech recap.

---

### 7. Vendor consistency — **OK**

Spot checks:
- **SLB / Schlumberger:** SLB primary (35 chapter + 35 slides + 11 speech); Schlumberger appears 6+7+2 in historical context («Roxar от Schlumberger», «E&P software от Schlumberger»). Both forms intentional и consistent.
- **Газпром нефть:** single canonical form across all 3 artifacts (24+12+4 hits). No drift «Газпромнефть» / «Газпром-нефть» / «GazpromNeft».
- **Aramco / Saudi Aramco:** Aramco primary (56+34+12); «Saudi Aramco» 5+1+0 — in first-mention contexts. Consistent.
- **Роснефть** — single form (21+24+5).
- **Сургутнефтегаз** — single form (6+7+2).

**No vendor name drift.**

---

### 8. Quadrant naming Q1 / Q2 / Q3 — **OK** (Q4 see Zone 2)

Q1, Q2, Q3 labels consistent:
- Q1 — «Зрелое производство» (or «mature production» in chapter parenthetic gloss) — all 3 artifacts
- Q2 — «Метановая MRV» — all 3
- Q3 — «Разведка фронтиров» — all 3 (chapter occasionally uses «frontier exploration» gloss; OK as gloss not primary name)
- Q4 — **DRIFT, see Zone 2**

---

### 9. Cross-references / orphan refs — **OK** + 1 P2

- **Speech slide refs:** все [s01]-[s42] → exist в deck.yaml ✓
- **Speech chapter refs:** speech doesn't explicitly reference chapter sections (relies on chapter as backing only via implicit narrative) — clean.
- **Slides chapter_ref:** spot-checked s04 → chapter.md §0.1-§0.3; s40 → chapter-part4.md §7.3; s41 → chapter-part4.md §7.3 — all resolve.
- **Slide-to-slide refs:** speech s07 references «вернёмся к этой формулировке в самом конце, когда будем говорить про Deepwater Horizon» → maps to s38 ✓
- **Lecture cross-refs:** chapter §7.3 + s40 reference Лекции 11-17. Chapter part4 L320 lists keystones для Лекций 11-15 + 16 (this) + Лекция 17 (forward). Consistent.

**P2 minor:** chapter part4 L323 says Лекция 15 keystone = «шкала автоматизации» — but per project memory, Лекция 15 is energy. Actual keystone for Лекция 15 not verified в этом скоупе (out of scope; flag for Лекция 15 author if produced). **Not blocking.**

---

### 10. Russification asymmetry — **P2**

Rough latin token count (unique tokens, includes brand allowlist):

| Artifact | Unique latin tokens | Per-1k-words rate |
|---|---|---|
| Chapter (5 parts, ~32k words) | 2 660 | ~83 per 1k |
| Slides (42 visible body .md) | 1 711 | (mixed corpus, not directly comparable) |
| Speech (~7,8k words) | 950 | ~122 per 1k |

**Issue:** speech has higher per-word latin density than chapter (122 vs 83) and slides. Inspection shows speech contains uppercase-italicised English terms used inline без gloss («closed-loop driver», «vendor concentration», «anchor customer», «multi-physics», «augmentation», «essential», «alert fatigue», «structural gap», «underestimates», «intermittent superemitters», «out-of-distribution», «paradigmatic», «mismatch incentives», etc.).

Many are technical terms that work in spoken Russian academic context, но **density выше** chapter's. Chapter uses inline gloss «(англ. ... — RU translation)» pattern consistently; speech uses bare English. Not P0/P1 because (a) speech is conversational lecturer voice (more code-switching natural), (b) terms are technical jargon student уже видел в slides/chapter, (c) project owner has not flagged speech russification as a stop condition for Лекция 16.

**Severity:** **P2** — quality refinement, not blocking. Comparable to Лекция 14 v2 baseline.

**Recommendation:** Phase 11 polish pass on speech — replace 30-40 worst offenders with inline RU equivalent or first-use «(англ. X)» gloss. Brand names + established acronyms (MRV, OGI, LDAR, SIS, ESP, RL, ML, HPC, CCS, EGS) — keep. Sample worst-offenders for speech polish:
- «out-of-distribution» → «вне обучающего распределения»
- «alert fatigue» → «усталость от тревог» (RU equivalent уже в chapter)
- «anchor customer» → «якорный клиент» (RU equivalent в chapter)
- «multi-physics» → «многослойная физика» (используется в s14 speech speaker notes)
- «mismatch incentives» → «рассогласование стимулов»
- «paradigmatic case» → «парадигматический случай» (transliterate OK)

**Effort:** 30-40 мин editing pass. **Optional для Phase 11**, can defer to GATE C cleanup.

---

## Cross-artifact matrix (sample)

| Concept / LO / Number | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|
| LO1 «когда применять» | ✓ Учебные цели L94 | ✓ embedded in s04 + s12 | ✓ implicit | ✓ |
| LO2 «когда отказаться» (6 criteria Q1) | ✓ §1.8 | ✓ s12 | ✓ s12 L260-278 | ✓ |
| LO3 6 alternatives | ✓ §7.1 + per-section | ✓ s19, s27, s33 | ✓ s19 L410, s27 L598, s33 L727 | ✓ |
| LO7 regulatory | ✓ §3 + §0.4 | ✓ s26 | ✓ s26 L572 | ✓ |
| Keystone-axis label | **OLD «физики»** | ❌ MIXED (s04 NEW, s02/s03/s40 OLD) | NEW «процессов» | **DRIFT** |
| Q4 naming | **OLD «энерг. переход»** | NEW «новые опоры» | NEW «новые опоры» | **DRIFT** |
| s01 hook material | VIIRS flares | YOLOv8 tanks | YOLOv8 tanks | **MISMATCH** |
| Cornerstone 1/2/3 | ✓ §7.3 | ✓ s40 | ✓ s40 L909-915 | ✓ |
| Closing single message «10→3» | ✓ part4 §7.3 closing | ✓ s41 | ✓ s41 L932-933 | ✓ |

## DISCREPANCIES (consolidated)

### D1 — Keystone axis label drift «определённость физики» vs «определённость процессов»
**Severity:** P1
**Where:** chapter (11 hits) + slides s02, s03, s40 (7 hits) vs slides s04 + speech (NEW canonical)
**Issue:** Phase 8.6 Item 4 rename was partial cascade. Chapter holds OLD label in frontmatter, TOC, §0 title, §7.3, and 3 chapter parts. Slides s02 (cover) + s03 (lecture-map) + s40 (cornerstones) still show OLD label.
**Recommendation:** Phase 11 chapter v3 cascade `s/определённость физики/определённость процессов/g` (and «данные × физика» → «данные × процессы») + 3 slide files. **Effort:** ~15 мин.

### D2 — Q4 naming drift «энергетический переход» vs «новые опоры (CCS + EGS)»
**Severity:** P1
**Where:** chapter (10 hits across parts 1/2/3/4/5) vs slides + speech (NEW canonical)
**Issue:** Phase 8.6 Item 6 rename was partial cascade. Chapter parts 1, 2, 3, 4, 5 all hold OLD label in section titles, frontmatter, cross-links.
**Recommendation:** Phase 11 chapter v3 cascade `s/Q4. Энергетический переход/Q4. Новые опоры (CCS + EGS)/g` + section heading renames in chapter-part3 (heading + TOC + L275). Be careful: «энергетический переход» as general industry concept (e.g., Cognitive Pilot transition discussion) — leave alone; only Q4 label rename. **Effort:** ~10 мин.

### D3 — s01 hook material misalignment (VIIRS Permian vs YOLOv8 tanks)
**Severity:** P1
**Where:** chapter.md Введение L99-107 (Permian VIIRS flares) vs slide s01 (YOLOv8 oil tanks) + speech [s01 · 2 мин] (YOLOv8).
**Issue:** Phase 8.6 Item 1 re-acquired s01 hero from VIIRS to YOLOv8; slide + speech updated; chapter Введение was not.
**Recommendation:** Option A (preferred, lower effort) — add 2-3 sentence acknowledgment paragraph at chapter intro top stating «s01 slide opens с другим hook (YOLOv8 tanks); это раздел расширяет картину до отраслевого scale через VIIRS flares». **Effort:** ~10 мин. Option B (heavier) — rewrite chapter Введение to YOLOv8 hook, repurpose VIIRS Permian as §1.* secondary material.

### D4 — Speech Russification density slightly higher than chapter — P2
**Severity:** P2
**Where:** speech.md (~122 latin tokens per 1k words vs chapter ~83).
**Recommendation:** Phase 11 optional polish — replace 30-40 anglicisms with RU equivalent (alert fatigue → усталость от тревог, anchor customer → якорный клиент, etc.). **Effort:** 30-40 мин. Can defer to GATE C cleanup.

### D5 — chapter part4 L323 «Лекция 15 keystone = шкала автоматизации» — possibly stale — P2
**Severity:** P2
**Where:** chapter-part4.md L323 (Лекция 17 bridge synthesis enumeration).
**Issue:** chapter lists Лекции 11-15 keystones; Лекция 15 listed as «шкала автоматизации» — out of scope to verify; flag for cross-check when Лекция 15 chapter is finalized.
**Recommendation:** verify against Лекция 15 actual keystone if produced; update if needed. Not blocking for Lec-16.

### D6 — Frontmatter `keystone_axis` chapter.md L22 — P2 (subset of D1)
**Severity:** P2
**Where:** chapter.md L22 frontmatter `keystone_axis: "Матрица «доступность данных × определённость физики»"`
**Recommendation:** part of D1 cascade fix.

### D7 — `slide_map: Q4_new_pillars` in chapter frontmatter is correct BUT R4 section body in part3 not — P2 (subset of D2)
**Severity:** P2
**Where:** chapter.md L34 frontmatter `Q4_new_pillars: [s28-s33]` (NEW canonical, ✓), но chapter-part3.md §4 body still «энергетический переход» (OLD).
**Recommendation:** part of D2 cascade fix.

## Coverage gaps

**No coverage gaps detected** for keystone-relevant material. All 10 failure cases, 3 cornerstones, 4 quadrants, 6 alternatives (LO3), 6 «когда AI не нужен» criteria (LO2), regulatory EU 2024/1787 + EPA Subpart W (LO7) — present in all 3 artifacts.

## Top fixes per artifact (Phase 11)

### Chapter v2.1 → v3 (~30-40 мин cascade)
1. **(D1) Rename axis label** in chapter.md frontmatter L22 + L65 TOC + L143 §0 heading + L94 LO1 + L129 + L197 Q4 definition + chapter-part4.md §7.1/§7.3 (5 hits) + chapter-part3.md (2 hits) + chapter-part5.md (1 hit). Pattern: «определённость физики» → «определённость процессов»; «данные × физика» → «данные × процессы».
2. **(D2) Rename Q4 label** in chapter.md L197 §0.3 + chapter-part2.md L351 cross-link + chapter-part3.md L5 part-title + L28 TOC + L275 R4 section heading + chapter-part4.md L279 §7.1 synthesis. Pattern: «Q4. Энергетический переход» → «Q4. Новые опоры (CCS + EGS)»; «Q4 energy transition» → «Q4 новые опоры (CCS + EGS)».
3. **(D3) Add chapter Введение acknowledgment** — 2-3 sentence top paragraph noting s01 slide opens с YOLOv8 hook; VIIRS Permian section extends к industry scale. **OR** rewrite intro to YOLOv8 hook (heavier).

### Slides v3 → v3.1 (~5-7 мин cascade)
1. **(D1) Rename axis label** in slides/s02-cover.md (4 hits) + slides/s03-lecture-map.md (2 hits) + slides/s40-three-cornerstones.md (1 hit). Pattern same as chapter.

### Speech v1 → v1.1 (optional, ~30-40 мин polish)
1. **(D4) Russification polish** — 30-40 anglicism replacements. Brand names + acronyms keep; conversational filler English replace with RU.
2. Otherwise speech is **clean** post-cascade.

## Verdict & Recommendation для Phase 11

**REVISE** — cascade-fix D1 + D2 (P1) + D3 (P1). D4 + D5 + D6 + D7 are P2, can defer.

After D1-D3 fix:
- chapter v3 (cascade D1 + D2 + D3 only — content unchanged, ~30-40 мин)
- slides v3.1 (cascade D1 across s02/s03/s40 — ~5 мин)
- speech unchanged (already on NEW canonical)

→ Re-run consistency check. Expected next-iteration verdict **APPROVE-WITH-POLISH** (P2 D4 Russification can polish during GATE C if owner requests).

**No structural re-design needed.** This is a clean Phase 8.6 cascade-completion issue — fixable in <1 hour total across 3 artifacts.

---

**Report by:** consistency-checker
**Date:** 2026-05-27
**Phase:** 10 (post-speech draft)
**Next:** Phase 11 cascade-revise (chapter v3 + slides v3.1)
