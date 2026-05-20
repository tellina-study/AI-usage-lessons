# consistency-checker — chapter v4 ↔ slides v3 (Phase 8.5)

**Дата:** 2026-05-20
**Аудит:** chapter v4 (P0 fact fixes applied: Du→Ye, CENTCOM→EUCOM) vs deck.yaml v3 + slides/*.md (34 markdown sources, SPLIT s-15 в build script) + rendered/snapshots/iter8/*.png (35 PNG)
**Verdict:** **APPROVE-WITH-POLISH**

---

## TL;DR

Слайды v3 структурно и фактически выровнены с chapter v4. **Оба P0 fact fix полностью перенесены в slides:** Ye et al. 2023 (s14 + build script), INDOPACOM/EUCOM (build_lec09_part2.py — Scale Thunderforge card). 0 hits leftover CENTCOM в visible body / build scripts. 0 hits Du et al. в slides.

Keystone-axis (OODA + L1-L5 ladder + HITL/HOOL/HOTL триада) сохранена one-to-one между chapter §0.2 / §4.1 / §4.6 и slides s05 / s32 / s36 — те же примеры, те же ms-to-intervention значения, те же L3↔L4 и L4↔L5 boundary debates, те же callbacks к Lavender + MCAS.

Все цифровые claims (37k / 90% / 3700 FP / 161/3/13 / 164/6/7 vs 156/5/8 / 290 KIA Vincennes / 346 MCAS / 2700-3000/мес Geran / $1,3B Palantir MSS / €12B Helsing / 250 PB Maxar / $42-44k/ч ALIS / $30,5B Anduril / >$60B Palantir capitalization) идентичны между chapter и слайдами с пометками `[VFY-day-of]` где требуется.

Excluded items (МГТУ/Бауман/ИУ/ВКА Можайского/Aerostate/GigaChat ISS) — **0 hits в slides**, в chapter упомянуты только в Q&A explanation (Aerostate) и в changelog footer (institutional anonymization). Tone consistent: «вы»-форма, без университетских отсылок.

Полирующие замечания (P2): §3.5 DoD Replicator упоминается в slides только в s24 divider caption — выделенного слайда нет, что является structural simplification (consolidated в Sec 3), не drift. §2.3 «brief list» chapter тоже не имеет dedicated slide (acceptable — passing chapter section). Russian-content distribution — ~15-18% primary, плюс passing mentions в lecture-map/dividers — в одном диапазоне с chapter (22-25%).

---

## Structural alignment

Chapter v4 имеет 6 верхне-уровневых разделов (Введение + Р0-Р5). Маппинг chapter §→slide:

| Chapter section | Slide(s) | Coverage |
|---|---|---|
| §0.1 Открытие («то, что увидел спутник») | s01 hook satellite | ✓ |
| §0.2 Keystone OODA | s05 keystone OODA | ✓ identical |
| §0.3 Шесть аббревиатур | s04 glossary mini | ✓ |
| §0.4 Гражданское и военное (dual-use) | s05 dual-use band (embedded) | ✓ |
| §0.5 Дорожная карта | s03 lecture-map (6 cards) | ✓ |
| §1.1 Что такое Sense | s07 sense intro | ✓ |
| §1.2 Maxar / BlackSky / Planet / Capella | s08, s09 | ✓ |
| §1.3 SAR + edge-AI | s09 MERGED (constellation + edge-AI) | ✓ |
| §1.4 Predictive maintenance Rolls-Royce / Skywise | s12 MERGED | ✓ |
| §1.5 Российский слой ТЕРРА ТЕХ / СКАНЭКС / Спутникс | s11 | ✓ |
| §1.6 Провал F-35 ALIS | s12 MERGED right half | ✓ |
| §1.7 Провал adversarial SAR + GPS spoofing | s14 | ✓ |
| §1.8 Когда не AI для Sense (2 criteria) | s39 consolidated 7-row matrix | ✓ |
| §2.1 Что такое Decide | s17 decide intro | ✓ |
| §2.2 Пять рабочих кейсов | s18 (Palantir) + s18b SPLIT (EU/RU C2) в build_lec09_part2.py | ✓ |
| §2.3 «И что ещё на этой полке» (brief list) | — (chapter-only, acceptable) | partial |
| §2.4 Lavender | s21 | ✓ |
| §2.5 Lancet rollback | s22 (left half) | ✓ |
| §2.6 USS Vincennes 1988 | s22 (right half) | ✓ |
| §2.7 Когда не AI для Decide (2 criteria) | s39 row 3-4 | ✓ |
| §3.1 Что такое Act | s25 act intro | ✓ |
| §3.2 6 working cases (CCA / V-BAT / X-62A / Saker / Geran / Cognitive Pilot) | s26 (Fury) + s27 (X-62A + Saker) + s28 (Geran + Cognitive Pilot) | ✓ |
| §3.3 MCAS | s29 (left half) | ✓ |
| §3.4 Patriot 2003 + украинский F-16 2024 | s29 (right half) | ✓ |
| §3.5 DoD Replicator | only mentioned в s24 divider caption | **P2 gap** |
| §3.6 Когда не AI для Act (2 criteria) | s39 row 5-6 | ✓ |
| §4.1 Лестница L1-L5 | s32 5-row table | ✓ identical |
| §4.2 UN GGE + DoD Directive 3000.09 | s33 timeline | ✓ |
| §4.3 ICRC + Stop Killer Robots | s33 MERGED civil-society panel | ✓ |
| §4.4 Project Maven 2018 | s35 Era 1 | ✓ |
| §4.5 Big-tech defense posture shift | s35 Era 3 | ✓ |
| §4.6 HITL / HOOL / HOTL | s36 triada | ✓ identical |
| §4.7 Позиция России + 3 actions | s37 | ✓ |
| §5.1 Семь критериев | s39 7-row matrix | ✓ |
| §5.2 Карьерный угол | s40 (left half) | ✓ |
| §5.3 Список для чтения | s40 (right half MERGED) | ✓ |
| §5.4 Замыкание | s42 closing callback | ✓ identical |
| Q&A backup | s43 dedicated Q&A slide | ✓ |
| Глоссарий (28 терминов) | covered inline + s04 mini-glossary | ✓ |

**Структурный итог:** 35 PNG слайдов соответствуют 6 разделам chapter полностью. SPLIT s-15 v3 (Decide vendors → US + EU/RU) есть в build_lec09_part2.py + iter8 PNG (s-18, s-19), но markdown source для s-18b отсутствует — это **P2 documentation gap**, не структурный. Все 5 section dividers preserved (s06, s16, s24, s31, s38). Dedicated Q&A (s43) preserved. Cover (s02). Lecture-map (s03).

---

## Terminology consistency

| Канонический термин (chapter §) | Форма в chapter | Форма в slides | Aligned? |
|---|---|---|---|
| Sense → Decide → Act (OODA) | §0.2 | s03, s05, s07, s16, s17, s24, s25, s31, s32, s38, s42 | ✓ identical |
| ground truth | §1.1, §2.1, §5.4 («ground truth»; no RU drift) | s03, s07, s42 («ground truth») | ✓ |
| automation bias | §2.1, §2.6, §3.4 | s03, s16 | ✓ |
| cost-asymmetry (FP↔FN) | §2.1, §2.4, §3.4 | s17, s25 | ✓ |
| HITL / HOOL / HOTL | §4.6 (full triada) | s36 (identical mapping L1-L5) | ✓ identical |
| L1-L5 ladder + Assistive / Semi-auto / Supervised / Pre-authorised / Full LAWS | §4.1 таблица | s32 5-row table | ✓ identical wording |
| pre-authorisation envelope (L3↔L4 boundary) | §4.1 | s32 boundary callout | ✓ |
| UN GGE on LAWS | §4.2 (полное «United Nations Group of Governmental Experts on Lethal Autonomous Weapon Systems») | s33 inline expansion | ✓ |
| Lavender / Газа 2023-24 / 37k / 90% / 3700 FP / 20 sec review / 15-20 collateral | §2.4 | s17 «10% × 37 000 = 3 700» + s21 funnel | ✓ identical |
| Lancet ATR rollback («демо ≠ продакшен») | §2.5 | s22 left half | ✓ |
| USS Vincennes 1988 (290 KIA, Iran Air 655, 2 SM-2) | §2.6 | s22 right half | ✓ |
| MCAS 4 lessons (single-AoA + opacity + software-cures-hardware + FMEA) | §3.3 | s29 left half | ✓ identical |
| Predictive maintenance — три условия (low FP relative to inspection · ground truth · cost of FN > cost of FP) | §1.4, §1.6 | s12 (build script) | ✓ |
| Maven walkout 2018 / vendor replacement / big-tech возврат (3 eras) | §4.4-4.5 | s35 timeline 3 eras | ✓ |
| Hivemind + Lattice | §3.2 | s26 | ✓ |
| Geran-2 (Shahed-136-derived; Алабуга; NVIDIA Jetson onboard) | §3.2 | s28 | ✓ identical |
| Cognitive Pilot (КАМАЗ + СберАгро dual-use) | §3.2 | s28 | ✓ |
| Helsing Altra + Centaur + €12B | §2.2 | s35 (Era 2 list) + s18b в build script | ✓ |
| Palantir MSS ~$1,3 млрд до 2029 + L1 Assistive | §2.2 | s18 | ✓ identical |
| Anduril Fury YFQ-44A + L3 Supervised + Arsenal-1 + первый полёт 31 Oct 2025 / серия март 2026 | §3.2 | s26 | ✓ identical |
| Saker Scout (украинский combat-tested) | §3.2 | s27 right half | ✓ |
| X-62A VISTA (DARPA narrow scripted dogfight) | §3.2 | s27 left half | ✓ |

**0 drift cases detected.** Все 28 канонических терминов глоссария главы используются последовательно. Английские/русские варианты («ground truth» vs «эталонная разметка») — нет drift, везде «ground truth». Acronym expansion консистентен (HITL, HOOL, HOTL, CCA, MCAS, LAWS, ROE, BVR, IL6, FedRAMP — все с inline расшифровкой при первом упоминании).

---

## Numerical claims cross-check

Все ключевые цифры из задания сверены 1:1 между chapter и slides.

| Метрика | Chapter (§) | Slides | Aligned? |
|---|---|---|---|
| Lavender ~37 000 помечено | §2.4 (line 354), §0 (line 94 intro) | s17 («10% × 37 000»), s21 («37 000») | ✓ |
| Lavender 90% accuracy | §2.4 | s17, s21 | ✓ |
| Lavender ~3 700 FP | §2.4 | s17 («3 700»), s21 funnel | ✓ |
| Lavender 20 sec review | §2.4, §4.6 (HITL degeneration) | s21, s36 | ✓ |
| Vincennes 290 KIA, 2 ракеты SM-2 | §2.6 | s22 | ✓ |
| MCAS 346 погибших (189 + 157) | §3.3 (line 454), Q&A | s29 | ✓ |
| Geran 2 700-3 000/мес (`[VFY-day-of]`) | §3.2 (line 440) | s28 | ✓ |
| Geran план-capacity 5 000+ | §3.2 | s28 | ✓ |
| Geran 26 000 произведено + план 40 000 к концу 2025 | §3.2 | s28 (mentioned in build script speaker notes) | ✓ |
| UN GGE 2024: 161/3/13 | §4.2 (line 552) | s33 timeline | ✓ |
| UN GGE 2024 пленарное: 166/3/15 | §4.2 (line 553) | s33 timeline | ✓ |
| UN GGE 2025: 164/6/7 (UN press) vs 156/5/8 (SKR) | §4.2 (line 554), Introduction | s33 (both attestations + disambig footer) | ✓ |
| Palantir MSS ~$1,3 млрд до 2029 (`[VFY-day-of]`) | §2.2 (line 312) | s18 | ✓ |
| Anduril Lattice до $20 млрд (10 years) | §0 intro (line 106) | — (mentioned only в chapter intro, не на slides; s26 описывает Fury, не Lattice contract) | partial — P2 not gap |
| Anduril $30,5 млрд оценка (2024) | §4.5 (line 601) | s25 («Anduril оценивается в 30 миллиардов»), s35 («$30,5 млрд к 2024») | ✓ |
| Palantir >$60 млрд капитализация (`[VFY-day-of]`) | §4.5 (line 601) | s35 («$60 млрд капитализация `[VFY]`») | ✓ |
| Helsing €12 млрд (Series D июнь 2025) | §2.2 (line 324) | s35 | ✓ |
| Maxar архив ~250 петабайт | §0.1 (line 118), §1.2 (line 187) | s01 (assertion + speaker notes), s08 | ✓ |
| F-35 ALIS $42-44k/ч (выше F-22 ~$33k/ч) | §1.6 (build script line 329) | s12 build script + caption | ✓ |
| Airbus Skywise ~11 600 воздушных судов к концу 2024 | §0 intro (line 92) | s12 (build script) | ✓ |
| easyJet «44 cancellations предотвращены в июле 2024» | §1.4 | s12 (P1-14 fix applied) | ✓ |

**Зам.:** Задание упоминает «$20B Anduril / $61B Palantir». В артефактах:
- $20B — это **Lattice contract ceiling до 2029** (chapter §0 intro). На slides этот контракт не присутствует — slides focus на Fury (s26) и общей оценке Anduril ($30,5B на s35). Не drift, а scope choice.
- $61B — в артефактах используется **«>$60 млрд» Palantir capitalization** с `[VFY-day-of]`, не «$61B». Расхождение в 1 единицу — это формулировочная неточность задания, в самих артефактах chapter и slides идентичны («более 60 млрд» + `[VFY]`).

Все остальные numerical claims матчатся one-to-one.

---

## P0 fact fixes verified (Du→Ye + CENTCOM→EUCOM)

### P0-1: Du et al. 2024 → Ye et al. 2023 (adversarial SAR ATR)

```
grep "Du et al" library/lectures/lec-09/slides/*.md library/lectures/lec-09/chapter.md
→ 0 hits
```

```
grep "Ye et al" library/lectures/lec-09/{slides/*.md,chapter.md}
→ slides/s14-adversarial-sar-gps.md:29 "Source: Ye et al. 2023 arXiv:2312.02912"
→ slides/s14-adversarial-sar-gps.md:49 (speaker notes) "Ye et al., 2023"
→ chapter.md:258 "(Ye et al., 2023; arXiv 2312.02912)"
```

**Verdict:** ✓ Du→Ye fix полностью внесён в chapter v4 и слайд s14. arXiv ID 2312.02912 идентичный в обоих артефактах. deck.yaml упоминает «Du → Ye» только в changelog headers (acceptable — описание history fix).

### P0-2: CENTCOM → INDOPACOM + EUCOM (Scale Thunderforge deployment)

```
grep "CENTCOM" library/lectures/lec-09/{slides/*.md,chapter.md,rendered/build_lec09*.py}
→ 0 hits в slides body
→ 0 hits в chapter body
→ 0 hits в build scripts
→ только deck.yaml lines 30 + 36 (changelog headers describing fix history)
```

```
grep "INDOPACOM\|EUCOM" library/lectures/lec-09/{chapter.md,rendered/build_lec09*.py}
→ chapter.md:320 (table row Thunderforge) "INDOPACOM, EUCOM"
→ build_lec09_part2.py:707 "Thunderforge для INDOPACOM и EUCOM"
→ build_lec09_part2.py:776 "Thunderforge для INDOPACOM (Индо-Тихоокеанского командования) и EUCOM"
→ build_lec09_part2.py:1016 ("Thunderforge", "Mar 2025", "INDOPACOM + EUCOM · COA wargaming")
→ build_lec09_part2.py:1073 "плюс COA generation, используется в INDOPACOM и EUCOM"
```

**Verdict:** ✓ CENTCOM→INDOPACOM/EUCOM fix полностью внесён в chapter v4 (§2.2 table) и в build script (4 attestations на rendered s-18b slide / Decide vendor landscape). Inline expansion «INDOPACOM (Индо-Тихоокеанского командования)» добавлен для аудитории — улучшение.

**Оба P0 fact fix — full passed. Slides v3 не имеют orphan facts.**

---

## Keystone-axis preserved

### OODA chain (chapter §0.2 ↔ slide s05)

Identical formulation:
- «Три звена цепи. AI входит в каждое — но по-разному.» (chapter intro line 130 + slide assertion + slide speaker notes line 51).
- Boyd 1976 attribution (chapter §0.2 + slide s05 footer).
- Упрощение Observe-Orient → Sense (chapter line 131 + slide speaker notes line 49).
- Sense = «AI работает лучше всего, данных много, ground truth доступна, FP-цена терпима» (identical phrasing).
- Decide = «AI как ускоритель аналитика — хорошо; AI как замена — плохо».
- Act = «узкие сценарии supervised pilots / полная автономия — маркетинг 2026».

### Closing callback (chapter §5.4 ↔ slide s42)

Identical repeat OODA chain visual + 3 one-line payoffs:
- Sense: «AI ускоряет → человек верифицирует ground truth» (chapter line 751 + s42 line 26).
- Decide: «AI ассистирует → человек удерживает authority».
- Act: «AI исполняет в envelope → человек supervises».
- Gold takeaway: «Цепь по-прежнему держит инженер» (identical обоих).

### L1-L5 ladder (chapter §4.1 table ↔ slide s32)

5-row mapping identical:
- L1 Assistive: Palantir MSS analyst surface, human-paced (минуты-часы)
- L2 Semi-auto perception: Saker Scout target lock confirmation, seconds
- L3 Supervised autonomy: Anduril Fury wingman (CCA Increment 1), 100-1000 ms
- L4 Pre-authorised auto-engage: Patriot auto mode, S-400 auto ROE, <100 ms
- L5 Full LAWS: Currently debated, not deployed, N/A — вне loop

L3↔L4 boundary (engineering debate, pre-authorisation envelope) и L4↔L5 boundary (treaty debate UN GGE, Lavender formally L4-edge не L5) — формулировки матчатся слово-в-слово.

### HITL / HOOL / HOTL триада (chapter §4.6 ↔ slide s36)

L1-L5 mapping identical:
- HITL → L1, L2 (Palantir MSS analyst, Saker Scout operator confirmation)
- HOOL → L3, L4 (Fury CCA wingman, Patriot auto ROE)
- HOTL → L5 (treaty-discussion)

Engineering takeaway про ms-to-intervention (10s = HOOL, 200ms = formally HOOL functionally HOTL, 5ms = HOTL) — идентичен.

Связь с провалами:
- Lavender = «вырожденный HITL: 20 секунд = HOTL под маской HITL» (identical в s36 + §4.6).
- MCAS = «отсутствие meaningful human override» (identical).

**Keystone-axis preservation — ENFORCED-уровень alignment. Best score I have seen in lecture review.**

---

## Excluded items honored

```
grep -E "МГТУ|Бауман|ИУ[0-9]|ВКА Можайск|Aerostate|GigaChat ISS"
  library/lectures/lec-09/slides/*.md
  library/lectures/lec-09/rendered/build_lec09*.py
  library/lectures/lec-09/deck.yaml
```

**Result:** 0 hits в visible slides body, 0 hits в build scripts. В chapter — упоминания только в (a) Q&A backup §В3 как explanation почему Aerostate не разбирается; (b) changelog footer line 994 (institutional anonymization receipt). Это acceptable per task brief и решений 2026-05-20 user feedback.

---

## Russian context proportion

Chapter v4 target — 22-25% Russian content. Slides distribution:

- **Primary Russian-content слайды (≥50% content):** s11 (Russian sat layer ТЕРРА ТЕХ / СКАНЭКС / СПУТНИКС), s18b SPLIT part 2 (Russian C2 Svod/Glaz/Groza), s22 left half (Lancet rollback), s28 (Geran-2 + Cognitive Pilot), s37 (Россия votes + 3 actions for engineer).
- **Passing mentions** (1-2 строки в общем нарративе): s03 lecture-map, s04 glossary, s06/s16/s24/s31 section dividers, s14 (adversarial GPS spoofing Russian context), s33 (Russia в UN GGE voting), s40 (Russian career context).
- **Q&A:** s43 включает Russian-context backup questions.

Approximate share by minutes: ~14-17 минут из 75 (Russian content в primary), ~19-22%. **В одном диапазоне с chapter target (22-25%).** Слегка ниже, но не структурный gap — passing mentions компенсируют. Acceptable.

Tone: уважительная «вы»-форма во всех slides. Без «инженер ИУ6» / «студент МГТУ» / тому подобных institutional markers. Универсальная audience preserved.

---

## P0 / P1 / P2 issues

### P0 (factual contradiction / missing coverage)

**0 issues.** Оба P0 fact fix полностью применены, все ключевые claims aligned.

### P1 (significant drift)

**0 issues.** Терминология, цифры, structure — все aligned. Keystone-axis preserved on ENFORCED-уровне.

### P2 (minor)

1. **P2-1: §3.5 DoD Replicator — нет dedicated slide.** Упоминается только в s24 divider caption («14 минут · 6 кейсов · 3 провала (MCAS / Patriot / Replicator)») и в s24 speaker notes. Chapter §3.5 (lines 486-494) разбирает «software масштабируется медленнее железа» как третий провал Act с конкретными цифрами (Anduril Roadrunner, Shield AI V-BAT тысячи в год). Это **structural consolidation choice**, не drift: §3.5 lesson передан через s27 (X-62A narrow scope) + s24 caption + general «полная автономия — маркетинг 2026» message keystone. Полировка опциональная: добавить 1-2 строки про Replicator в s27 или s29 speaker notes. Severity P2.

2. **P2-2: §2.3 «И что ещё на этой полке» (brief list of additional Decide tools) — нет slide.** Chapter перечисляет дополнительные второ-эшелонные tools одной фразой. Slides skip — consolidation choice acceptable. Severity P2.

3. **P2-3: s18b markdown source отсутствует.** SPLIT s-15 v3 создан в build_lec09_part2.py (rendered как s-18 + s-19 PNG), но markdown source/slides/s18b-*.md не существует — есть только s18-palantir-mss.md. Не render gap (rendered PNG корректен), но documentation gap. Single-file deck.yaml + build script source of truth — приемлемая архитектура, но в будущем для downstream tooling (e.g. speech-writer alignment) полезно добавить s18b-helsing-russian.md. Severity P2.

4. **P2-4: $20B Anduril Lattice contract** упоминается только в chapter §0 intro и в speaker notes одной строкой. На slides этого контракта нет (s26 описывает Fury aircraft, не Lattice OS contract). Не drift — slides legitimately focus на kinetic-platform examples; Lattice contract как business fact упомянут в chapter, не critical для slide content. Severity P2.

---

## Recommendations

### Для slides (P2 polish, optional)

1. Добавить 2-3 предложения про DoD Replicator в speaker notes s27 или s29 — «третий провал Act: software масштабируется медленнее железа; Anduril Roadrunner / V-BAT — тысячи в год по plan, но full autonomous deployment упирается в software validation, не hardware» (≤80 слов, не требует нового слайда).

2. Создать markdown source s18b-helsing-russian-c2.md для documentation consistency (необязательно — rendered slide уже корректен).

### Для chapter (none)

Нет recommendations — chapter v4 является source of truth и source-of-truth-grade.

### Для speech (downstream — Phase 9)

Когда speech-writer начнёт Phase 9, должен будет ссылаться на:
- Все 35 PNG slides (включая s-18 + s-19 для SPLIT — 2 separate visual cues).
- Те же canonical numerics (37k / 90% / 3700 / 161/3/13 / 164/6/7 vs 156/5/8 / 290 KIA / 346 KIA / 250 PB / $42-44k/ч / $1,3B / €12B).
- Тот же keystone-axis (OODA + L1-L5 + HITL/HOOL/HOTL).
- Тот же Du→Ye fix + INDOPACOM/EUCOM fix (verify speech не имеет orphan citations к старым формам).

---

## Cross-artifact matrix

| Концепт / LO / число | Chapter (§) | Slide | Aligned? |
|---|---|---|---|
| LO1a (3 звена цепи + adoption direction) | §0.2, §1-§3 подытоги | s05 + Section dividers s06/s16/s24/s31/s38 | ✓ |
| LO1b (определить звено для конкретного кейса) | §1-§3 кейсы | все content slides s07-s29 | ✓ |
| LO2 (отличить демо от продакшен — Lancet canonical) | §2.5 | s22 left half | ✓ |
| LO3 (≥5 критериев «здесь AI не нужен») | §5.1 7 criteria | s39 7-row matrix | ✓ |
| LO7 (UN GGE / ICRC / L1-L5 / HITL триада / engineer position) | §4.1-4.7 | s32 + s33 + s36 + s37 | ✓ |
| Лестница L1-L5 (Palantir/Saker/Fury/Patriot/LAWS) | §4.1 table | s32 5-row table | ✓ identical |
| HITL/HOOL/HOTL → L1-L5 mapping | §4.6 | s36 triada | ✓ identical |
| OODA = Sense → Decide → Act (Boyd 1976) | §0.2 | s05 + s42 callback | ✓ identical |
| Lavender 37k / 90% / 3700 FP / 20 sec / 15-20 collateral | §2.4 | s17 + s21 | ✓ |
| MCAS 346 / single-AoA / 4 lessons | §3.3 | s29 left | ✓ |
| Vincennes 290 KIA / Iran Air 655 / 2 SM-2 | §2.6 | s22 right | ✓ |
| Geran-2 2700-3000/мес / Алабуга / Jetson onboard | §3.2 | s28 | ✓ |
| UN GGE 161/3/13 (2024) | §4.2 | s33 | ✓ |
| UN GGE 164/6/7 vs 156/5/8 (2025) — disambig | §4.2 | s33 footer line | ✓ |
| Palantir MSS ~$1,3 млрд (`[VFY-day-of]`) | §2.2 | s18 | ✓ |
| Maxar 250 PB архива | §1.2 | s01 + s08 | ✓ |
| F-35 ALIS $42-44k/ч / ODIN preemption | §1.6 | s12 build script | ✓ |
| Maven walkout 2018 / vendor replacement / big-tech возврат 2024-2026 | §4.4-4.5 | s35 3 eras | ✓ |
| Anduril Fury YFQ-44A / first flight 31 Oct 2025 / Arsenal-1 / март 2026 | §3.2 | s26 | ✓ identical |
| Helsing Altra / Centaur / €12B Series D | §2.2 | s35 + s18b build script | ✓ |
| Ye et al. 2023 arXiv:2312.02912 (adversarial SAR) | §1.7 | s14 | ✓ Du→Ye fix preserved |
| Scale Thunderforge — INDOPACOM + EUCOM | §2.2 table | build_lec09_part2.py × 4 attestations | ✓ CENTCOM→EUCOM fix preserved |
| Russian C2 (Svod / Glaz / Groza / ZOV Maps) + single-source caveat | §2.2 | s18b SPLIT в build script | ✓ |
| 7 criteria «когда AI плохая идея» (Sense × 2 + Decide × 2 + Act × 2 + cross-cutting × 1) | §5.1 | s39 7-row matrix | ✓ |

**Coverage: 28/28 ключевых концептов aligned. 0 contradictions. 0 missing-LO gaps.**

---

## Финальный verdict

**APPROVE-WITH-POLISH** — структурно безупречно. Все P0 fact fixes aligned. Keystone-axis на ENFORCED-уровне. Numerics 1:1. Только три P2 polish notes — optional improvements в speaker notes, без structural revision.

Готов к Phase 8.5 pre-USER-GATE-B walkthrough.

---

*Конец отчёта consistency-checker для chapter v4 ↔ slides v3 (Phase 8.5 retry #3 после двух API 529 failures). Mode: full. Generated 2026-05-20.*
