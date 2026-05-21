# fact-checker — speech v1 (Phase 10)

**Дата:** 2026-05-20
**WebSearch usage:** 0 (все speech-claims уже verified в chapter v4 + slides v3; no new claims в speech без chapter backing → live web verification не требуется)
**Verdict:** APPROVE-CLEAN

---

## TL;DR

Speech v1 — **полностью clean** по фактам. Прошёл по 35 slide-якорям + 10 Q&A backup entries: каждый numeric / date / attribution claim в speech имеет точное соответствие в chapter v4 (или slides v3, что matches chapter). **0 P0**, **0 P1**, **2 P2** (минорные rounding/wording polish).

Главное: оба ENFORCED-fixes из Phase 4/7 сохранены без drift в speech:
- **Ye et al. 2023 (arXiv 2312.02912)** для adversarial SAR ATR — speech line 276 ✓ (не Du 2024)
- **INDOPACOM + EUCOM** для Thunderforge — speech line 332 ✓ (не CENTCOM)

Все canonical failure-block numbers (Lavender 37k/90%/3700/20s/15-20; MCAS 189+157=346; Vincennes 290; F-35 $42-44k; Geran 2700-3000; UN GGE 161/3/13 → 164/6/7; Maxar 250 PB; Anduril $20B Lattice; Helsing €12B; Skywise 11 600; X-62A; Patriot 2003) — match chapter v4 1:1.

Speech-style citation acceptable («по данным CSIS», «согласно arXiv 2312.02912») — соблюдён по всему документу. Anti-hype оговорки на Maxar suite, X-62A scripted scenario, Geran autonomy unclear, Russian C2 single-source — все present.

Speech не вводит ни одного нового numerical claim, отсутствующего в chapter v4 — поэтому WebSearch на новые факты не понадобился. **Speech mirrors chapter, drift = 0.**

---

## P0 — chapter/slides drift или fact errors

**Нет.**

Полный pass по 35 slide-фрагментам:

### s01 hook + s05 keystone — Sense intro / OODA
- ✓ Maxar Sentry 250 PB (speech l.66 ↔ chapter l.118)
- ✓ Boyd 1976, John Boyd USAF (speech l.136 ↔ chapter l.126)
- ✓ Sense → Decide → Act упрощение Observe+Orient → Sense (speech l.138 ↔ chapter l.128)

### s08 Maxar / s09 BlackSky-Planet-Capella / s10 Russian sat layer
- ✓ Maxar Sentry «25 июня 2025 года» (speech l.198 ↔ chapter l.187)
- ✓ NGA Luno A D01 «детекции в часах» (speech l.198 ↔ chapter l.187)
- ✓ BlackSky выручка $102M в 2024 (speech l.212; chapter l.189 = $102,1M, speech rounded — P2 only)
- ✓ Planet EOCL $146M первый этап (speech l.214 ↔ chapter l.191)
- ✓ ICEYE финский / Capella SAR / «теневой флот» (speech l.216 ↔ chapter l.193)
- ✓ ESA Φ-sat-2 август 2024 (speech l.220 ↔ chapter l.201)
- ✓ Lockheed Pony Express 2 (speech l.220 ↔ chapter l.203)
- ✓ Slingshot TALOS июль 2025 (speech l.220 ↔ chapter l.205)
- ✓ ТЕРРА ТЕХ Роскосмос 2017, БРИКС 2024 (speech l.232 ↔ chapter l.225)
- ✓ СКАНЭКС 3,5M снимков, Яндекс.Карты (speech l.234 ↔ chapter l.227)
- ✓ СПУТНИКС АФК «Система», 100+ кубсатов, Зоркий-2М 3+3 спутника, камера 2,5м (speech l.236 ↔ chapter l.229)

### s11 ALIS-Skywise-RR
- ✓ Rolls-Royce IntelligentEngine 2018, ~400 unplanned/year (speech l.248 ↔ chapter l.215)
- ✓ Airbus Skywise ~11 600 ВС, easyJet 8,1 т топлива, 44 предотвращ отмены июль 2024 (speech l.250 ↔ chapter l.217)
- ✓ F-35 ALIS $42-44k/ч (speech l.254 ↔ chapter l.240, GAO-22-105128)
- ✓ ODIN finalization июнь 2024 (speech l.254 ↔ chapter l.242)

### s12 SAR ATR + GPS spoofing — **ENFORCED Ye et al. fix preserved**
- ✓ «Исследования Ye с соавторами в 2023 году» (speech l.276) — соответствует chapter l.258 «Ye et al., 2023; arXiv 2312.02912». **Не Du 2024 — ENFORCED fix sustained.**
- ✓ GPS интерференция в Латвии 820/2024 vs 26/2022 (speech l.282 ↔ chapter l.268)

### s14 Decide intro + s15 US vendors — **ENFORCED INDOPACOM+EUCOM preserved**
- ✓ Lavender 10% × 37 000 = 3 700 (speech l.316 ↔ chapter l.94)
- ✓ Palantir MSS $480M май 2024, $99,8M сентябрь, $795M май 2025, $1,3B ceiling до 2029 (speech l.326 ↔ chapter l.312) — 1:1 match
- ✓ Project Maven 2017 (speech l.324 ↔ chapter l.312)
- ✓ Scale Donovan 2022-2023 XVIII Airborne Corps (speech l.332 ↔ chapter l.318)
- ✓ Defense Llama ноябрь 2024 Llama 3 (speech l.332 ↔ chapter l.319)
- ✓ **Thunderforge март 2025 INDOPACOM и EUCOM** (speech l.332) — соответствует chapter l.320. **Не CENTCOM — ENFORCED fix sustained.**
- ✓ Anthropic-Palantir-AWS ноябрь 2024, Claude IL6 (speech l.334)

### s16 Helsing + Russian C2
- ✓ Helsing Altra + Centaur, Saab Gripen E июнь 2025 (speech l.346 ↔ chapter l.324)
- ✓ Helsing €600M Series D → €12B (speech l.346 ↔ chapter l.324)
- ✓ Prima Materia / Daniel Ek / Spotify co-founder (speech l.346 ↔ chapter l.324)
- ✓ Svod (август 2025), Glaz / Groza / ZOV Maps (speech l.350 ↔ chapter l.330-331)
- ✓ CSIS Bondar апрель 2026 + single-source caveat preserved (speech l.350-356 ↔ chapter l.333)

### s17 Lavender failure
- ✓ ~37 000 помечено (speech l.366 ↔ chapter l.354)
- ✓ ~90% accuracy, ~3 700 FP (speech l.366 ↔ chapter l.354)
- ✓ ~20 секунд review per target (speech l.370 ↔ chapter l.354)
- ✓ 15-20 гражд жертв allowance (speech l.370 ↔ chapter l.354)
- ✓ +972 Magazine 6 IDF officers, April 2024 (speech l.366 ↔ chapter l.354, Abraham, +972)
- ✓ Lieber Institute + AOAV «прецедент автоматизированных kill-lists» (speech l.372 ↔ chapter l.356)
- ✓ ЦАХАЛ опровержение (speech l.372 ↔ chapter l.356)

### s18 Lancet rollback + Vincennes 1988
- ✓ Lancet-3 Калашников/ZALA, маркетинг 2022-2023 «autonomously find» (speech l.396 ↔ chapter l.372)
- ✓ CSIS + Modern War Institute analysis 2023-2024 (speech l.396 ↔ chapter l.372)
- ✓ USS Vincennes 3 июля 1988, Iran Air 655, 290 погибших (speech l.406 ↔ chapter l.384)
- ✓ Aegis правильно записала «climbing», operators доложили «descending into attack» (speech l.408 ↔ chapter l.384)

### s21 Anduril Fury YFQ-44A
- ✓ Высота 50 000 ft, M 0.95, 9g, Williams engine (speech l.450 ↔ chapter l.430)
- ✓ Первый полёт 31 октября 2025 (speech l.450 ↔ chapter l.430)
- ✓ Серийное производство 23 марта 2026 (speech l.450 ↔ chapter l.430)
- ✓ Arsenal-1 в Огайо, $1B инвестиции (speech l.450 ↔ chapter l.430)
- ✓ Shield AI Hivemind + Anduril Lattice + AIM-120 (speech l.452 ↔ chapter l.430)
- ✓ L3 Supervised mapping (speech l.454 ↔ chapter l.430)
- ✓ Anduril Lattice contract до $20B / 10 лет (speech l.458 ↔ chapter l.106)

### s22 X-62A VISTA + Saker Scout
- ✓ Декабрь 2022 — начало (speech l.468 ↔ chapter l.434)
- ✓ Сентябрь 2023 — первый AI-vs-manned dogfight, 2 000 ft nose-to-nose, 1 200 mph (speech l.468 ↔ chapter l.434)
- ✓ Май 2024 — секретарь USAF Кендалл лично летал (speech l.468 ↔ chapter l.434)
- ✓ Anti-hype: narrow scripted, BVR excluded, fuel mgmt, ROE — (speech l.472 ↔ chapter l.436)
- ✓ Saker Scout 64 целей, ~10 км, EW-подавление (speech l.476 ↔ chapter l.438)
- ✓ Brave1 300+ AI разработок (speech l.476 ↔ chapter l.438)
- ✓ AI-mother-drone 2 AI-FPV strike дронов на 300 км (speech l.476 ↔ chapter l.438)
- ✓ L2 Semi-auto (speech l.478 ↔ chapter l.438)

### s23 Geran-2 + Cognitive Pilot
- ✓ Geran-2 на основе Shahed-136, Алабугская ОЭЗ (speech l.486 ↔ chapter l.440)
- ✓ ~2 700-3 000 дронов/мес к концу 2025, plan-capacity 5 000+ (speech l.486 ↔ chapter l.440)
- ✓ Total >26 000 к поздней весне 2025 (speech l.486 ↔ chapter l.440)
- ✓ NVIDIA Jetson, тепловизоры, FPGA, 2026 anti-radiation seeker (speech l.488 ↔ chapter l.440)
- ✓ 1 111 серверов Dell PowerEdge через Shreya Life Sciences апрель-август 2024 (speech l.494 ↔ chapter l.444)
- ✓ Cognitive Pilot = Сбер + Cognitive Technologies, до 50 000 систем/год (speech l.498 ↔ chapter l.446)

### s24 MCAS + Patriot
- ✓ Lion Air 610 октябрь 2018, 189 погибших (speech l.510 ↔ chapter l.454)
- ✓ Ethiopian Airlines 302 март 2019, 157 погибших (speech l.510 ↔ chapter l.454)
- ✓ 346 погибших, 20-месячная остановка (speech l.510 ↔ chapter l.454)
- ✓ Single AoA sensor без резервирования (speech l.512 ↔ chapter l.456)
- ✓ 4 урока: SPOF, opacity, software-cures-hardware, FMEA (speech l.518-524 ↔ chapter l.459-462)
- ✓ Patriot 2003 — британский Tornado GR4, F/A-18C — оба friendly fire (speech l.530 ↔ chapter l.478)
- ✓ IFF interrogated но не ответил (speech l.530 ↔ chapter l.478)
- ✓ Automation bias formulation (speech l.530 ↔ chapter l.478, l.482)

### s26-s27 L1-L5 + UN GGE
- ✓ L1 Assistive: Palantir MSS, минуты-часы (speech l.568 ↔ chapter l.530)
- ✓ L2 Semi-auto: Saker Scout, секунды (speech l.570 ↔ chapter l.531)
- ✓ L3 Supervised: Anduril Fury wingman, 100-1000 ms (speech l.572 ↔ chapter l.532)
- ✓ L4 Pre-authorised: Patriot auto, <100 ms (speech l.574 ↔ chapter l.533)
- ✓ L5 Full LAWS: currently debated not deployed (speech l.576 ↔ chapter l.534)
- ✓ 5 ноября 2024 UNGA: **161/3/13**, против — Беларусь/КНДР/Россия (speech l.598 ↔ chapter l.552)
- ✓ 6 ноября 2025: **164/6/7** UN ga12736, **156/5/8** Stop Killer Robots (speech l.600 ↔ chapter l.554)
- ✓ Против 2025: **Беларусь, Бурунди, КНДР, Израиль, Россия, США** (speech l.600 ↔ chapter l.554) — 6 стран match
- ✓ США сдвиг: 2024 «за» → 2025 «против» (speech l.600 ↔ chapter l.554)
- ✓ Россия — против с 2018 (speech l.674 ↔ chapter l.646)
- ✓ 42 государства подписали joint statement сентябрь 2025 (speech l.602 ↔ chapter l.555)
- ✓ ICRC «передача жизни/смерти машинам — дегуманизация» (speech l.608 ↔ chapter l.574)
- ✓ ICRC «не оружейная система должна comply с IHL, а люди» (speech l.610 ↔ chapter l.575)

### s28 Maven walkout → big-tech return
- ✓ Март 2018 leak Google participates (speech l.622 ↔ chapter l.587)
- ✓ 4 000+ сотрудников письмо, ~12 инженеров резигнировали (speech l.622 ↔ chapter l.587)
- ✓ Июнь 2018 Google не продлевает (speech l.622 ↔ chapter l.587)
- ✓ Январь 2024 OpenAI удалил military-use запрет (speech l.634 ↔ chapter l.605)
- ✓ Cohere classified deployments 2024 (speech l.634 ↔ chapter l.607)
- ✓ Mistral defense partnerships ЕС 2025 (speech l.634 ↔ chapter l.608)
- ✓ Сентябрь 2025 Google возвращается через Google Cloud (speech l.634 ↔ chapter l.609)

### s29 HITL/HOOL/HOTL триада
- ✓ HITL → L1, L2 (speech l.650 ↔ chapter l.623)
- ✓ HOOL → L3, L4 (speech l.652 ↔ chapter l.624)
- ✓ HOTL → L5 (speech l.654 ↔ chapter l.625)
- ✓ Engineering decision = ms-to-intervention (speech l.658-660 ↔ chapter l.627-629)
- ✓ Lavender 20 sec = «HOTL под маской HITL» (speech l.664 ↔ chapter l.640)
- ✓ MCAS opacity = «pilot мог override но не было информации» (speech l.664 ↔ chapter l.640)

### s32-s33 Семь критериев + карьера
- ✓ Критерий 1 — Sense low-data / distribution shift / adversarial SAR ATR (speech l.712 ↔ chapter l.679)
- ✓ Критерий 2 — Sense single-sensor HITL / F-35 ALIS (speech l.712 ↔ chapter l.680)
- ✓ Критерий 3 — Decide long-tail / mission planning ROE (speech l.714 ↔ chapter l.681)
- ✓ Критерий 4 — Decide life-and-death без HITL / Lavender (speech l.714 ↔ chapter l.682)
- ✓ Критерий 5 — Act autonomy not needed / MCAS (speech l.716 ↔ chapter l.683)
- ✓ Критерий 6 — Act COTS sensor cheaper / second AoA (speech l.716 ↔ chapter l.684)
- ✓ Критерий 7 — Cross-cutting HOOL→HOTL treaty (speech l.718 ↔ chapter l.685)

### Q&A backup (l.786-824)
- ✓ В1 — UN treaty 3 причины: capability / determinations / verification (speech l.788 ↔ chapter l.771)
- ✓ В2 — Russian LLMs space single Russian source, постоянно (speech l.792 ↔ chapter l.775)
- ✓ В3 — Aerostate not verified, excluded with disclaim (speech l.796 ↔ frontmatter excluded_items)
- ✓ В5 — Lavender +972 6 officers, Lieber + ICRC = серьёзный кейс (speech l.804 ↔ chapter l.789)
- ✓ В6 — MCAS = canonical anti-pattern для всех safety-critical AI (speech l.808 ↔ chapter l.458)
- ✓ В7-В8 — civilian options ТЕРРА ТЕХ/СКАНЭКС/СПУТНИКС/Maxar/Planet/BlackSky/Boeing/Airbus/Wisk Aero — все verified в chapter
- ✓ В10 — спекуляция договора к 2026 году явно помечена как «спекуляция, не прогноз»

---

## P1 — significant issues

**Нет.**

Speech не вводит ни одного нового numerical claim или attribution, отсутствующих в chapter v4. Все claims mirror chapter. Citation формат speech-style («по данным CSIS», «по данным Латвии», «согласно arXiv 2312.02912») — appropriate для устного жанра. Нет broken citations или suspicious unсiterd numbers.

---

## P2 — polish

### P2-1: BlackSky revenue rounding (l.212)
- **Speech:** «Выручка 2024 года — 102 миллиона долларов»
- **Chapter:** «$102,1 млн»
- **Verdict:** acceptable rounding для устной речи (один знак после запятой потерян). **Не нужно править** — речевой жанр.
- **Severity:** P2 polish only.

### P2-2: Lecture 10/11 preview teaser (l.768)
- **Speech:** «В Лекции 10 — AI в энергетике. В Лекции 11 — транспорт и логистика.»
- **Curriculum reality check (catalog/manifests/lectures.yaml):** Не верифицировано в текущей сессии (вне scope speech fact-check — это curriculum/sync вопрос, не speech-fact).
- **Verdict:** не speech fact issue. Если lectures.yaml утверждает иное — поднять отдельно в consistency-checker / curriculum sync, не здесь. Speech закрытие соответствует chapter l.703 («Лекция 10 покрывает X»).
- **Severity:** noted, not actionable в speech-критике.

---

## Strengths

1. **Zero drift от chapter v4.** Каждое factual утверждение в speech имеет точное соответствие в chapter v4 — 1:1 для всех 35 slide-anchors + 10 Q&A entries. Это образцовый book-first производственный цикл: speech действительно derived from chapter, не parallel-source.

2. **Оба ENFORCED-fixes сохранены без drift:**
   - Ye et al. 2023 (arXiv 2312.02912) — explicitly cited в speech l.276
   - INDOPACOM + EUCOM — explicitly named в speech l.332 (не CENTCOM)

3. **Anti-hype оговорки preserved во всех canonical местах:**
   - Maxar Sentry = «suite, не одна модель» (l.202)
   - X-62A = «narrow scripted scenario, BVR excluded» (l.472)
   - Geran «автономия» = «реальная роль autonomous decision unclear» (l.492)
   - Russian C2 Svod/Glaz = «single-source caveat» (l.354)
   - LLM hype в Decide = «accuracy 90% звучит хорошо, но в life-and-death — никогда» (l.316)

4. **Citation style appropriate для устной речи:**
   - «по данным CSIS от апреля 2026 года» — атрибутировано
   - «Исследования Ye с соавторами в 2023 году показывают» — proper attribution
   - «По свидетельствам шести офицеров израильской разведки, опубликованным в +972 Magazine в апреле 2024 года» — sufficient detail
   - «По данным Латвии, в 2024 году зарегистрировано 820 случаев интерференции — против 26 в 2022» — direction + magnitude both present

5. **Все 7 canonical failure-blocks (ALIS, GPS spoofing, Lavender, Lancet, Vincennes, MCAS, Patriot) — точные цифры и атрибуции без drift.**

6. **L1-L5 ladder + HITL/HOOL/HOTL triad mapping numbers (ms-to-intervention) — match chapter:** L1=минуты-часы, L2=секунды, L3=100-1000ms, L4=<100ms, L5=N/A. Lavender = «HOTL под маской HITL» preserved.

7. **UN GGE цифры match chapter:** 161/3/13 (2024) + 164/6/7 (2025) + 156/5/8 (Stop Killer Robots alternative count) + 6 названных стран против в 2025 + сдвиг США 2024→2025 — всё корректно.

8. **Q&A backup factually grounded** — каждый ответ либо derived из chapter, либо explicitly помечен как opinion / speculation («личное мнение», «спекуляция, не прогноз», «гипотезы избегаем»).

---

## Recommendations

**Для Phase 11 (final polish):** **никаких fact-fixes не требуется.** Speech v1 уже clean по fact-checker оси.

Если speech-writer будет делать минорные правки по результатам других critic-агентов (methodology / consistency / reader-simulator) — proceed without fact-check re-pass, поскольку content is locked against chapter v4. Если же речь будет существенно расширена (>5% новых формулировок numerical claim), потребуется delta fact-check.

---

## Verdict rationale

- P0 = 0 → не REJECT
- P1 = 0 → не REVISE
- P2 = 2 (rounding + curriculum preview ref) → не блокирующие
- Direction inversions: 0
- Curriculum hallucinations в lecture-9 scope: 0
- Misquotes: 0 (нет word-for-word цитат с кавычками вне chapter, а «officers devoted almost no resources to double-checking targets» в speech l.370 — exact quote из chapter l.354 / Abraham 2024 ✓)
- Broken citations: 0

**Final verdict: APPROVE-CLEAN.**

---

*fact-checker report end. speech v1, Phase 10.*
