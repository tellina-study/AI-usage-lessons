# Methodology Critique — Chapter v1 — Лекция 4

**Date:** 2026-05-13
**Critic:** methodology-critic
**File reviewed:** `/home/levko/AI-usage-lessons/library/lectures/lec-04/chapter.md` (12,502 слов, 782 строк)
**Cross-ref:** plan-v2.md, sources.md + sources-ru-drug-discovery.md, course-program (`catalog/exports/docs/ai-v-raznyh-industriyah.md`), REFLECTION-CONSOLIDATED.md, Lec 1 chapter (style baseline)

## Verdict: REVISE

Chapter v1 — методически крепкая основа: LO покрытие явное, assertion-evidence work, self-checks Apply/Analyze, LO8 framing correctly «input для Lec 9 черновика». Но три структурные проблемы заслуживают **REVISE** (не APPROVE-WITH-POLISH): **(1) [for-slide-sXX] markers** scattered throughout — это designer-additions violation, contaminating source-of-truth artifact; **(2) two fabricated cross-references** в §6.2 и §4.2 — «следующая лекция AI в производстве» (на самом деле Коллоквиум 1) и «на Лекции 9 будет Практикум 1» (Практикум 1 = Лекция 7); **(3) Bloom-mismatch wording в §6.3** — chapter does correctly say «частный материал», но затем называет LO8 «summative-уровень (Evaluate/Create)», что transit мог bы взять reader как «мы здесь уже делаем Evaluate». Counter-check: 7 P1 issues; per counter-check rule (≥5 P1 → REVISE), confirms REVISE.

## Issue counts
- **P0:** 0
- **P1:** 7
- **P2:** 11

## Author-flagged open questions — addressed

**1. Word count 12,502.** Compress to ~11,500. Specific recommendations:
- **§5.3 LLM-анти-паттерны (630 слов)** — Tessa narrative is well-structured but Case 3 (Patient self-diagnosis) repeats statistics (40M, 32% Rock Health, 3/5 adults Gallup). Consolidate to 60–80 слов. Savings: ~70 слов.
- **§3.5 Регулирование** — ФЗ-152/ФЗ-23 sentences in §3.5 (lines 423–425) duplicate §5.4 «Регуляторика». Drop in §3.5. Savings: ~80 слов.
- **§5.4 Sweeney 1997** — compress to 1 sentence (drop year detail). Savings: ~40 слов.
- **§5.1 «Зачем инженеру»** — duplicates section headings already in TOC. Cut to single paragraph. Savings: ~70 слов.
- Aggregate: ~260 слов → final ~12,240 слов.

**3. Лекция 9 cross-reference paraphrase.** ACCEPTABLE PARAPHRASE; recommend in §6.3 one occurrence with full title «AI, этика и регулирование: кто отвечает за AI?» — это central question Лекции 4. P2 polish.

**7. Other fabricated cross-references — TWO FOUND.** See P1-2 and P1-3.

**8. RU drug discovery tone в §3.3.** OK, BALANCE IS DEFENSIBLE. «РФ preclinical vs Insilico peer-reviewed Phase IIa» — correct rhetorical position. No shift recommended. One small wording fix in P2-3.

## P0 Issues

**None.** Chapter does not have «методически непригодной» content.

## P1 Issues

### P1-1. Designer-additions: `[for-slide-sXX]` markers scattered throughout chapter (27 occurrences)
**Sections:** lines 98, 108, 124, 149, 170, 186, 212, 227, 257, 286, 308, 335, 357, 371, 395, 413, 442, 458, 479, 492, 512, 542, 573, 614, 624, 630, 638.
**Issue:** Chapter v1 has 27 `[for-slide-sXX]` annotations. Per "No Extra Content Rule" + book-first principle, chapter should be **prose narrative**, не annotated with slide mappings. Лекция 1 chapter has 0 such markers.
**Why P1:** Markers leak deck structure в canonical learning artifact; bind chapter prose к specific slide numbers (s17a, s18-merged), maintenance burden if deck restructured. Reader of chapter alone (e.g., student готовится к Коллоквиуму 1) sees noise.
**Fix:** Strip all `[for-slide-sXX]` annotations. Store mapping в отдельный `library/lectures/lec-04/slide-bindings.yaml` если нужно.

### P1-2. Fabricated cross-reference: «Следующая лекция — AI в производстве и сельском хозяйстве»
**Section:** §6.2 (lines 630–634)
**Issue:** §6.2 says «Следующая лекция — "AI в производстве и сельском хозяйстве"». Per course program: **Лекция 5 = Коллоквиум 1**, «AI в производстве» = **Лекция 6**. Same paragraph correctly notes «Между этой лекцией и лекцией о производстве... проходит Коллоквиум 1» — self-contradiction.
**Fix:** «Следующее занятие — **Коллоквиум 1** (Лекция 5), охватывающий первые четыре содержательные лекции. После него — **Лекция 6 "AI в производстве и сельском хозяйстве"** с российскими данными (Cognitive Agro Pilot: 1 500+ машин, +30–40%)».

### P1-3. Fabricated cross-reference: «на Лекции 9 будет Практикум 1»
**Section:** §4.2 (line 466)
**Issue:** «...на Лекции 9 будет Практикум 1». Per course program: **Практикум 1 = Лекция 7** («Анализ индустриальных кейсов с помощью AI»). Лекция 9 = **лекция** «AI, этика и регулирование», not a practikum.
**Fix:** «на **Лекции 7** будет Практикум 1 ("Анализ индустриальных кейсов с помощью AI"), а на Лекции 12 — Практикум 2».

### P1-4. LO8 framing inconsistency: §6.3 calls LO8 «summative-уровень (Evaluate/Create)» creating premature synthesis impression
**Section:** §6.3 (line 642)
**Issue:** «Это **summative-уровень (Evaluate/Create по Bloom)**, и финальный синтез делается на Лекции 9 и 14. Лекция 4 даёт **частный материал**...». §6.3 has already enumerated 3 concrete principles (lines 646–648). To reader, looks like synthesis is completed here.
**Fix:** Rewrite §6.3 line 642: «LO8 требует **Evaluate-уровень мышления** (Bloom), который достигается через **синтез нескольких индустриальных кейсов**. На Лекции 4 вы накапливаете один такой кейс; финал — Лекции 9 и 14. Принципы ниже — **сырьё**, не финал». Rename «принципы» → «наблюдения» before numbered list. Add: «Три **наблюдения** из этой лекции для копилки Лекции 9:».

### P1-5. Self-check (Раздел 1) question 3 meta-reflective, not Apply-level
**Section:** §1 self-check, question 3 (line 204)
**Issue:** «Объясните, почему "4 млрд руб/год экономии в ОМС от mosmed.ai" не упоминается в этой главе как факт.» Meta-question about chapter editorial choices, not LO1.
**Fix:** Replace с LO1/LO2 question: «Сравните scale FDA-списка (1 451 устройств) и mosmed.ai (14M исследований / 70 сервисов на 43 области): что эти два числа измеряют по-разному, и почему их нельзя напрямую сравнивать?».

### P1-6. AlphaFold user count «2M+ researchers» — epistemic inconsistency
**Section:** §3.2 (line 361)
**Issue:** Chapter rejects 2M Hassabis Nobel speech number while citing other industry self-disclosures (Insilico's «18 months» в §3.3, AlphaProteo wet-lab numbers). Inconsistent epistemic standard.
**Fix:** Either include 2M с same caveat-pattern («DeepMind заявляет 2M+ researchers, источник Nobel speech 2024; verifiable peer-reviewed alternative — 200M structures»). OR state methodological rule once в §3 introduction.

### P1-7. §5.5 «5 практик» drift from §6.3 «3 принципа»
**Section:** §5.5 (line 597) and §6.3 (line 644)
**Issue:** §5.5 line 597: «**три (или пять)** принципов» — vague hedge. §5.5 actually enumerates 5 practices: Transparency / Calibration / Audit-trail / Post-market monitoring / Disclosure. §6.3 collapses to 3 без explanation. Reader confused.
**Fix:** Make §5.5 enumerate same 3 as §6.3 (combine items: 1=Transparency+Calibration, 2=Validation set/population — currently missing, add, 3=Audit-trail+Post-market). OR change §6.3 to «**пять** принципов» и renumber.

## P2 Issues

### P2-1. Лекция 9 title — 1× full title в §6.3
«Лекция 9 "AI, этика и регулирование: кто отвечает за AI?"» — subtitle = central question Лекции 4.

### P2-2. §6.2 Cognitive Agro Pilot teaser — должен быть «Лекция 6 sneak peek», не «Лекция 5»
Embed в P1-2 fix.

### P2-3. §3.3 «российский Rentosertib некорректно» — phrasing as strawman
No one in chapter/sources actually says «российский Rentosertib».
**Fix:** «Сравнение Russia preclinical vs Insilico Phase IIa нельзя описать как "российский Rentosertib"».

### P2-4. §0.2 «почти никто не поднимет» — chapter narrative outside lecture-hall context
**Fix:** «Третий вопрос — большинство людей отвечает "нет"; эта интуиция готовит к Разделу 5...».

### P2-5. §0.3 narrative duplicates §Введение
Reader gets same 4-block map twice within 50 lines.

### P2-6. §1.1 typo «geomic AI» → «genomic AI»; «persona-driven» → «patient-specific»

### P2-7. §2.2 inline LaTeX — defer to reader-simulator (author Q6)

### P2-8. §5.3 typo «лозу 1–2 фунта» → «терять 1–2 фунта»

### P2-9. §1.3 «три причины» but content has 4
EU AI Act 2 авг 2026 = 4th implicit reason.

### P2-10. §3.1 vs §3.4 phrasing tension
«marginally helps» vs «не имеет отношения к attrition rate». Harmonize: «AI ассистирует workflow, не влияет на attrition rate».

### P2-11. §5.3 visible `[FACT-CHECK]` annotation в chapter
Same issue as P1-1 — leaks editorial workflow в reader-facing artifact.

## Structural observations

**LO coverage — complete.** All 5 LOs explicitly stated, referenced throughout, recapped in §6.1. LO8 framing «частный материал → синтез на Lec 9 → финал Lec 14» articulated 3 times. P1-4 risk is wording-level, не framing-level.

**Sequence — strong arc, two seam issues.** §2.5 forward-reference к §5.2 (Obermeyer) creates anticipation. §3.5 (regulation) stranded between §3.4 (DSP) and §4 (micro-exercise) — optional transition sentence.

**Frame integrity — all 6 frames present**, concentrated в structurally important sections.

**Tone calibration — engineer-perspective consistent.** «Вы» mode maintained. No moralizing. «Trust-but-verify» repeated motif.

**Russian-context substantive.** mosmed retraction of «4 млрд» — methodologically excellent. RU drug discovery balance defensible. ФЗ-152 + ФЗ-23 substantively tied к engineering implication.

**Curriculum relevance** — все content within intermediate Bloom band.

**Terminology — minimal drift.** Glossary discipline holds.

## What chapter v1 does WELL (для context revision agent)

1. **mosmed.ai «4 млрд» retraction** (§1.2) — turns sourcing gap в teachable moment. Best paragraph в chapter.
2. **Self-check Раздел 2 Q1** — strongest Apply question. Replicate numerical-computation pattern.
3. **§3.3 RU drug discovery framing** — neither boosterism nor dismissal. Model для future RU sections.
4. **§5.5 4-actor framework** — Analyze-level deliverable promised by LO3.
5. **§6.3 LO8 framing — 90% there.** P1-4 fix completes.
6. **Sources block** — 62 references with primary URLs, industry-grade.

## Priority for Phase 4 revision

1. P1-2 + P1-3 (fabricated cross-refs — easy factual fixes)
2. P1-1 (strip `[for-slide-sXX]` markers — find/replace)
3. P1-4 (LO8 wording + rename «принципы» → «наблюдения»)
4. P1-7 (§5.5 / §6.3 5-vs-3 unification)
5. P1-5 (replace §1 self-check Q3)
6. P1-6 (AlphaFold 2M epistemic consistency)
7. Compression pass −260 слов
8. P2 batch
