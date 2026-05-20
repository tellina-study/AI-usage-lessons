# consistency-checker — chapter ↔ slides (Phase 7)

**Дата:** 2026-05-20
**Targets:** `library/lectures/lec-09/chapter.md` v3 finalized (994 строки, 104 sources, 28 glossary terms) + slides v2 (`deck.yaml` v2 + `slides/s01..s43-*.md` — 34 файла + `rendered/snapshots/iter7/s-*.png`)
**Speech:** не в scope этой phase
**Verdict:** **REVISE**

## TL;DR

Цифры, термины, voting counts, key failure-cases — **полностью консистентны** (37 000 / 3 700 / 290 KIA / 346 KIA / 164/6/7 / 11 600 / $1,3B / €12B / 23 марта 2026 / 31 октября 2025 совпадают строка-в-строку). Glossary (28 terms) дисциплинированно перенесён в slides — Lavender canonical lessons, OODA звенья, L1-L5 ladder, HITL/HOOL/HOTL триада, 7 критериев матрица — все формулировки matchat.

Однако обнаружены **2 P0 структурных gap'а**, выходящих за полирующий уровень:

1. **deck.yaml декларирует «MERGED s09+s10» (constellation + edge-AI on one slide)**, но фактический файл `s09-blacksky-planet-constellation.md` содержит ТОЛЬКО таблицу из 4 EO/SAR-вендоров (BlackSky/Planet/Capella/ICEYE) — **нет ни одной строки про edge AI on-orbit / Φ-sat-2 / Pony Express / Slingshot TALOS** (chapter §1.3 целиком). Эта подсекция главы — отдельный educational block с тремя категориями программ — отсутствует в визуальном слое полностью. В speaker notes s06 divider lecturer обещает «edge AI on-orbit: ML-вычисления прямо на спутнике через ESA Φ-sat-2, Lockheed Pony Express, Slingshot Aerospace», но соответствующего слайда нет.
2. **deck.yaml декларирует s18 «MERGED: Decide vendor landscape (Palantir+Scale+Helsing+Anthropic+RU)»**, но фактический файл `s18-palantir-mss.md` посвящён ТОЛЬКО Palantir MSS. Scale Donovan/Defense Llama/Thunderforge, Helsing Altra/Centaur, Anthropic-Palantir IL6, Russian C2 (Svod/Glaz-Groza) — **визуально отсутствуют как dedicated case**; упоминаются только устно в speaker notes s16 и s17, либо frament-only в timeline s35.

Кроме того — 5 P1 issues с локальными drift'ами (Anduril valuation rounding, Shield AI V-BAT details lost, Anduril Lattice $20B контракт из chapter intro не отражён в slides, цифра «30 миллиардов» в s25 vs «$30,5 млрд» в s35 и chapter §4.5, F-35 ALIS $42-44k/h cost-per-hour из chapter §1.6 не в s12).

Cited sources, terminology, key numbers — **в основном консистентны** (P2-уровень). Структурный coverage gap по двум кейс-блокам Decide vendor landscape и Edge-AI on-orbit — **требует либо добавления слайдов (s10 edge-AI + s19-20 Decide vendors), либо документального обновления deck.yaml comment-блока + явного решения «эти подсекции — speaker-notes-only»**. На текущем состоянии deck.yaml lies about what slides actually carry.

---

## Structural alignment (chapter sections ↔ slides)

Полная матрица covered/missing per §:

| Chapter § | Тема | Slide(s) | Coverage статус |
|---|---|---|---|
| Учебные цели LO1a/b, LO2, LO3, LO7 | LOs | frontmatter всех slides | ✓ полное |
| Центральный вопрос | central question | s03 lecture-map (bottom italic) | ✓ полное |
| Введение (§Anduril Lattice $20B / Palantir $1,3B contracts) | infrastructure metrics intro | s18 ($1,3B), но **$20B Anduril Lattice — отсутствует** | ⚠ P1 gap |
| §0.1 Maxar Sentry открытие | hook satellite | s01 hook satellite | ✓ полное |
| §0.2 Keystone OODA | keystone OODA | s05 keystone OODA | ✓ полное |
| §0.3 6 аббревиатур (SAR/ATR/ISR/EW/LAWS/OODA) | glossary mini | s04 glossary mini | ✓ полное |
| §0.4 Dual-use гражданское ↔ военное | dual-use band | s05 (band на keystone) | ✓ полное |
| §0.5 Дорожная карта | lecture map | s03 lecture-map | ✓ полное |
| §1.1 Что такое Sense (4 типа сигнала + 3 причины) | sense intro | s07 sense intro | ✓ полное |
| §1.2 Спутниковая аналитика 4 игрока | constellation table | s08 Maxar Sentry + s09 4-vendor table | ✓ полное |
| §1.3 SAR + edge-AI on-orbit (Slingshot, Φ-sat-2, Pony Express, AI-eXpress, TerraTech) | edge-AI on-orbit | **отсутствует как dedicated slide** (deck.yaml v2 декларирует MERGED s09+s10, но фактический s09 — только constellation) | **✗ P0 missing coverage** |
| §1.4 Predictive maintenance (Rolls-Royce, Airbus Skywise) | predictive maintenance | s12 predictive maintenance | ✓ полное |
| §1.5 Российский слой (ТЕРРА ТЕХ, СКАНЭКС, СПУТНИКС) | Russian sat layer | s11 russian sat layer | ✓ полное |
| §1.6 F-35 ALIS → ODIN (3 условия PdM) | F-35 ALIS failure | s12 (footer caption only) + s39 row #2 | ⚠ P1 partial; ALIS canonical case заслуживает dedicated slide или прямого place в s12; в s12 footer лишь one-liner «об этом — следующий слайд» — но следующий слайд (s14) уже adversarial SAR. ALIS slide отсутствует physically (s13 deleted per deck.yaml notes). 3 условия PdM (быстрый feedback / ground truth / FP-cost) перечислены только в s12 speaker notes, не на visible body. |
| §1.7 Adversarial SAR ATR + GPS-spoofing | adversarial + GPS | s14 adversarial SAR + GPS | ✓ полное |
| §1.8 Критерии 1-2 Sense | criteria 1-2 | s39 row #1,#2 | ✓ полное (consolidated) |
| §2.1 Что такое Decide | decide intro | s17 decide intro | ✓ полное |
| §2.2 Пять рабочих кейсов (Palantir + Scale + Helsing + Anthropic + Russian C2) | Decide vendor landscape | s18 (Palantir only) + s35 (Anthropic in timeline) + s16 divider notes (Helsing, Russian C2 mentioned verbally) | **✗ P0 missing coverage** — deck.yaml декларирует s18 = MERGED vendor landscape, но фактический файл — Palantir-only. Scale Donovan/Defense Llama/Thunderforge table (chapter §2.2 case 2), Helsing Altra/Centaur €12B/Daniel Ek (chapter case 3), Anthropic-Palantir IL6 (case 4), Russian Svod/Glaz-Groza-ZOV с явным single-source caveat (case 5) — все 4 кейса не имеют dedicated visual presence |
| §2.3 «И что ещё на полке» список | brief vendor list | отсутствует (acceptable — это speaker-notes-friendly footnote-list) | ✓ acceptable |
| §2.4 IDF Lavender | Lavender canonical | s21 Lavender | ✓ полное |
| §2.5 Lancet ATR rollback | Lancet failure | s22 Lancet + Vincennes (left) | ✓ полное |
| §2.6 USS Vincennes 1988 | Vincennes UI | s22 Lancet + Vincennes (right) | ✓ полное |
| §2.7 Критерии 3-4 Decide | criteria 3-4 | s39 row #3,#4 | ✓ полное (consolidated) |
| §3.1 Что такое Act + counter-drone $300/$3M | act intro | s25 act intro | ✓ полное |
| §3.2 case 1 Anduril Fury YFQ-44A | Fury CCA | s26 Anduril Fury | ✓ полное |
| §3.2 case 2 Shield AI V-BAT + Hivemind ($198M USCG, Индия janv 2026) | Shield AI V-BAT | **отсутствует как dedicated slide** | **✗ P0 missing coverage** — deck.yaml упоминает s27 (X-62A + Saker), s28 (Geran-2 + Cognitive Pilot), но V-BAT case с $198M USCG / Индийская армия / Hivemind autonomy stack / L2-L3 уровень — отсутствует. В s24 divider speaker notes lecturer обещает «Shield AI V-BAT плюс Hivemind», но соответствующего slide нет. V-BAT упоминается только в s26 (Hivemind brand-mention в spec sidebar), s40 career (карьерный перечень). |
| §3.2 case 3 DARPA X-62A VISTA | X-62A | s27 X-62A + Saker | ✓ полное |
| §3.2 case 4 Saker Scout | Saker Scout | s27 (right) | ✓ полное |
| §3.2 case 5 Geran-2 + supply chain caveat (Shreya Life Sciences) | Geran-2 | s28 Geran-2 + Cognitive Pilot | ✓ полное |
| §3.2 case 6 Cognitive Pilot (civilian dual-use) | Cognitive Pilot | s28 (right) | ✓ полное |
| §3.3 Boeing 737 MAX MCAS (4 урока) | MCAS canonical | s29 MCAS + Patriot | ✓ полное |
| §3.4 Patriot 2003 + украинский F-16 2024 (automation bias) | Patriot callback | s29 (footer Teal-tint mini-callback) | ✓ полное (consolidated) |
| §3.5 DoD Replicator missed scale | Replicator | **отсутствует как dedicated slide** (упоминается только в s24 divider notes и s40 footer); CETC Atlas 96 дронов / 1 планшет из §3.5 — также отсутствует | ⚠ P1 partial — chapter урок «software масштабируется медленнее железа» + DAWG succession — заметная провальная история, ушедшая в speaker notes |
| §3.6 Критерии 5-6 Act | criteria 5-6 | s39 row #5,#6 | ✓ полное (consolidated) |
| §4.1 Лестница L1-L5 | L1-L5 ladder | s32 L1-L5 ladder | ✓ полное |
| §4.2 UN GGE + DoD Directive 3000.09 | UN GGE timeline | s33 UN GGE + DoD | ✓ полное |
| §4.3 ICRC + Stop Killer Robots (30 стран, ICRC position) | ICRC + SKR civil society | deck.yaml v2 декларирует s33 = MERGED «UN GGE timeline + ICRC/SKR civil society», но **фактический s33 содержит только UN GGE timeline + DoD sidebar** — ICRC «prohibit/restrict» позиция + ethical/procedural core + Stop Killer Robots 30 стран — отсутствует. Только в s37 speaker notes и s33 speaker notes verbal. | ⚠ P1 partial — chapter §4.3 — substantial block (ICRC quote «It is not the weapon system that must comply with IHL...» — central ethical formulation), но не visible на slide |
| §4.4 Project Maven 2018 walkout | Maven walkout | s35 timeline era 1 + s18 footer history | ✓ полное |
| §4.5 Big-tech defense posture shift | big-tech timeline | s35 Maven → vendor replacement → big-tech | ✓ полное |
| §4.6 HITL/HOOL/HOTL триада | HITL/HOOL/HOTL | s36 HITL/HOOL/HOTL | ✓ полное |
| §4.7 Позиция России + Критерий 7 | Russia votes context | s37 Russia votes + cross-cutting | ✓ полное |
| §5.1 7 критериев матрица | 7 criteria | s39 7-criteria matrix | ✓ полное |
| §5.2 Карьерный угол | career angle | s40 career | ✓ полное |
| §5.3 Список для чтения (7 источников) | reading list | s40 (right side?) — НЕ ВИДНО в slide content; deck.yaml v2 декларирует s40 = MERGED career + reading list, но фактический s40 content — только 5 профилей + 3 контура | ⚠ P1 partial — 7 reading sources (Scharre Army of None, CSIS Bondar, Abraham Lavender, ICRC Position Paper, DARPA ACE, GAO ALIS, SKR briefs) — отсутствует как visible content |
| §5.4 Замыкание | closing callback | s42 closing callback | ✓ полное |
| Q&A backup B1-B10 | Q&A | s43 Q&A (3 backup prompts из B1, B5, B7) | ✓ полное (selective — что и ожидаемо) |

**Итого по structural coverage:**
- ✓ полное coverage: 27 § / разделов из 35.
- ⚠ P1 partial: 5 (ALIS partial, Replicator partial, ICRC/SKR partial, reading list partial, $20B Anduril Lattice intro).
- ✗ P0 missing: 3 (edge-AI on-orbit §1.3, Decide vendor landscape s18 MERGED-as-declared, Shield AI V-BAT case 2).

---

## Terminology consistency (glossary check)

Канонические термины из chapter ## Глоссарий — 28 terms. Проверка drift:

| # | Канонический термин | Slide usage | Drift? |
|---|---|---|---|
| 1 | OODA | s05, s42, all dividers | ✓ identical |
| 2 | Sense → Decide → Act | s03, s05, s42 | ✓ identical |
| 3 | SAR | s04, s09, s14 | ✓ identical |
| 4 | ATR | s04, s22 | ✓ identical |
| 5 | ISR | s04, s09 (implicit) | ✓ identical |
| 6 | EW | s04, s14, s27, s28 | ✓ identical |
| 7 | LAWS | s04, s32-s37 | ✓ identical |
| 8 | Dual-use | s05, s11, s28 | ✓ identical |
| 9 | Лестница L1–L5 | s25, s26, s27, s32, s36, s37 | ✓ identical |
| 10 | HITL | s17, s21, s32, s33, s36, s39 | ✓ identical |
| 11 | HOOL | s32, s36, s37 | ✓ identical |
| 12 | HOTL | s21, s32, s36, s37, s39 | ✓ identical |
| 13 | Pre-authorisation envelope | s26, s32 | ✓ identical |
| 14 | Maxar Sentry | s01, s08 | ✓ identical |
| 15 | Palantir MSS | s18, s32, s35 | ✓ identical |
| 16 | Scale Donovan/Defense Llama/Thunderforge | s16 (verbal), s17 (verbal) — **никакого dedicated visual mention** | ⚠ P1 visual mismatch — chapter §2.2 имеет detailed table 3-product line, в slides — ноль visible presence |
| 17 | Helsing Altra/Centaur | s16 (verbal), s17, s35 (€12 млрд), s40 (карьерный footer) — **dedicated visual mention отсутствует** | ⚠ P1 visual mismatch |
| 18 | Anduril Lattice + Fury YFQ-44A | s26 (Fury), s35 (Anduril in vendor list) — Lattice как brand упомянут только в s26 spec sidebar | ⚠ P1 partial — Lattice как proprietary OS для mesh-coordination объясняется только speaker notes s26; в visible body — это просто часть spec sidebar |
| 19 | Shield AI V-BAT + Hivemind | s26 (Hivemind упомянут как stack для Fury), s40 (career footer) — **V-BAT case с $198M / Индия — отсутствует** | **✗ P0 missing coverage** |
| 20 | DARPA X-62A VISTA | s27 | ✓ identical |
| 21 | CCA | s24, s26, s32, s36 | ✓ identical |
| 22 | Replicator / DAWG | s24 (divider notes verbal), s40 (career mention) — **dedicated slide отсутствует** | ⚠ P1 partial |
| 23 | SDA Tracking Layer / PWSA | Не упомянут ни в одном slide | ⚠ P2 — chapter §1.3 + glossary вводят, но slides пропустили; acceptable если SDA рассматривается как часть edge-AI block, который тоже отсутствует |
| 24 | F-35 ALIS → ODIN | s12 (footer one-liner), s29 (callback в speaker notes), s39 (criterion #2 illustration), s42 (callback Sense payoff) — **dedicated slide отсутствует** | ⚠ P1 partial — ALIS canonical failure имеет 3 уроки PdM, $42-44k/h cost-per-hour, переход на ODIN — но в visible body одна строка. Speaker notes s12 говорит «об этом — следующий слайд», но «следующий слайд» (s14) — adversarial SAR, не ALIS |
| 25 | IDF Lavender | s17 (callout 10%×37 000=3 700), s21 (canonical), s32 (boundary L4↔L5), s36 (degraded HITL), s39 (criterion #4), s42 (closing payoff Decide) | ✓ identical |
| 26 | Boeing 737 MAX MCAS | s29, s32 (implicit), s36 (callback), s39 (criterion #5), s42 (closing) | ✓ identical |
| 27 | Demo ≠ production | s22 (Lancet card), s27 (X-62A anti-hype) | ✓ identical |
| 28 | Accuracy as wrong metric | s17 (callout), s21 (canonical) | ✓ identical |

**Anti-anglicism mandate (deck.yaml v2):** Проверил выборочно — большая часть англицизмов в visible body заменена («voorkomen events» → «непланированных событий», «detections» осталось в visible body s32 — minor P2). Несколько остатков в visible body:
- `[VFY]` маркеры виды в s09 «$100M+ subscription», s28 «~2 700-3 000 / месяц» — это intentional «verify day of» markers per repo convention.
- В s17 visible callout: «10% × 37 000 = 3 700» (без англ). ✓
- s22 visible card: «**LO2 canonical case**» (gold badge) — слово «canonical» в visible body. ⚠ P2 minor.
- s27 visible: «**Anti-hype caveat**» в gold-tint box, «narrow scripted scenario · 1-на-1 dogfight · BVR исключён · fuel management не покрыт · ROE не учитывался». — «narrow scripted scenario» / «fuel management» — anglicism residue in visible. ⚠ P2 minor.
- s33 visible: «UN press: 164/6/7 · Stop Killer Robots: 156/5/8 — расхождение методик» — OK.

---

## Numerical claims cross-check

Все ключевые цифры — **консистентны** между chapter и slides:

| Цифра | Chapter location | Slide location | Match? |
|---|---|---|---|
| 37 000 Lavender помечены | chapter §2.4 (line 354), Введение (line 94), Глоссарий #25 | s17 callout, s21 funnel, s17 speaker notes | ✓ |
| 90% accuracy / ~3 700 FP | chapter §2.4 | s17 callout «10% × 37 000 = 3 700», s21 funnel | ✓ |
| 20 секунд review per target | chapter §2.4, Введение | s21 funnel шаг 4 + speaker notes | ✓ |
| 15-20 civilian casualties | chapter §2.4 line 354 | s21 funnel шаг 5 | ✓ |
| 11 600 ВС Skywise | chapter §1.4 line 217, Введение line 92 | s12 chart + speaker notes | ✓ |
| 1 500 ВС SFP+ | chapter §1.4 | s12 chart | ✓ |
| ~400 Rolls-Royce предотвращённых событий | chapter §1.4 | s12 info-card | ✓ |
| easyJet 8,1 тонны топлива/ВС/год + 44 отмены | chapter §1.4 | s12 caption + speaker notes | ✓ |
| 290 KIA Iran Air 655 | chapter §2.6 | s22 timeline | ✓ |
| 346 KIA MCAS (189 + 157) | chapter §3.3, Введение line 106, Глоссарий #26 | s29 timeline | ✓ |
| F-35 ALIS $42-44k/h flight cost | chapter §1.6 line 240, Глоссарий #24 | **отсутствует на slides** | **✗ P1 chapter detail dropped** |
| 250 ПБ Maxar архив | chapter §0.1 line 118, §1.2 line 187 | s01 sidebar, s08 «250 ПБ архив» | ✓ |
| NRO EOCL $146M | chapter §1.2 line 191 | s09 table «NRO EOCL $146M+» | ✓ |
| BlackSky $100M+ subscription | chapter §1.2 line 189 | s09 table | ✓ |
| 820 GPS interference (Latvia 2024 vs 26 в 2022) | chapter §1.7 line 268 | s14 chart + assertion + speaker notes | ✓ |
| 1 111 Dell PowerEdge XE9680 через Shreya | chapter §3.2 line 444 | s28 supply-chain caveat | ✓ |
| Geran-2 ~2 700-3 000 / месяц | chapter §3.2 line 440 | s28 «~2 700-3 000 / месяц `[VFY]`» | ✓ |
| Geran-2 plan-capacity 5 000+ | chapter §3.2 line 440 | s28 speaker notes (but not visible card) | ⚠ P2 minor — visible card отсутствует «plan-capacity 5 000+», только в speaker notes |
| Geran-2 >26 000 произведено к весне 2025 | chapter §3.2 | s28 visible card | ✓ |
| Geran-2 >40 000 plan к концу 2025 | chapter §3.2 | s28 visible card | ✓ |
| Anduril Fury serial 23 марта 2026 + $1B Arsenal-1 | chapter §3.2 line 430 | s26 production card | ✓ |
| Fury первый полёт 31 октября 2025 | chapter §3.2 + Введение line 92 | s26 assertion + caption | ✓ |
| Fury 9g / M 0.95 / 50 000 футов | chapter §3.2 | s26 spec sidebar | ✓ |
| Williams FJ44-4M 4 000 фунтов тяги | chapter §3.2 | s26 spec sidebar | ✓ |
| AIM-120 AMRAAM | chapter §3.2 | s26 spec sidebar | ✓ |
| Saker Scout 64 цели / 10 км дальность | chapter §3.2 line 438 | s27 right card | ✓ |
| Brave1 300+ AI dev, 70+ AI/CV в combat | chapter §3.2 | s27 right card | ✓ |
| AI-mother-drone 2 AI-FPV strike дрона за 300 км | chapter §3.2 | s27 right card | ✓ |
| Lancet 2022-2024 timeline | chapter §2.5 | s22 left card timeline | ✓ |
| Palantir MSS $480M / +$99.8M / +$795M / **$1,3B до 2029** | chapter §2.2 line 312, Введение | s18 timeline | ✓ |
| UNGA Nov 2024: 161/3/13 (Беларусь/КНДР/Россия против) | chapter §4.2 + §4.7 | s33 timeline + s37 | ✓ |
| UNGA Dec 2024 пленар: 166/3/15 (resolution 79/62) | chapter §4.2 line 553 | s33 timeline | ✓ |
| UNGA Nov 2025: **164/6/7 UN press (156/5/8 по SKR)** + США в «против» | chapter §4.2 line 554, §4.7 line 644 | s33 timeline + s37 left | ✓ |
| UN GGE Сентябрь 2025: 42 государства joint statement | chapter §4.2 line 555 | s33 timeline | ✓ |
| Цель Генсека ООН договор к 2026 | chapter §4.2 line 556 | s33 timeline + speaker notes | ✓ |
| Maven walkout 4 000+ подписей / ~12 инженеров резигнировали | chapter §4.4 line 587 | s35 era 1 | ✓ |
| Anduril valuation $30,5 миллиарда к 2024 | chapter §4.5 line 601 | s35 era 2: «$30,5 млрд к 2024» — ✓ | **но s25 speaker notes говорят «Anduril оценивается в 30 миллиардов» — drift round vs $30,5** ⚠ P2 |
| Palantir market cap $60+ миллиардов `[VFY]` | chapter §4.5 line 601 | s35 era 2 | ✓ |
| Helsing €600M Series D → €12B valuation | chapter §2.2 line 324 + Глоссарий #17 | s35 era 2 «€12 млрд (Series D, июнь 2025)» | ✓ |
| Anthropic-Palantir-AWS IL6 ноябрь 2024 | chapter §2.2 line 326, §4.5 line 606 | s35 era 3 | ✓ |
| OpenAI policy edit январь 2024 | chapter §4.5 line 606 | s35 era 3 | ✓ |
| Anduril Lattice контракт **до $20 миллиардов на 10 лет (Army Recognition 2026)** | chapter Введение line 106 | **отсутствует на slides** | **✗ P1 chapter intro number dropped** |
| Shield AI V-BAT: $198M USCG (июль 2024) | chapter §3.2 line 432 | **отсутствует на slides** | **✗ P0 (part of V-BAT case missing) — упомянут только в Глоссарии #19** |
| Shield AI Индийская армия январь 2026 ($35M emergency procurement) | chapter §3.2 | **отсутствует на slides** | **✗ P0** |
| Shield AI valuation $5,6-12,7B `[VFY]` | chapter §3.2 | **отсутствует на slides** | **✗ P0** |
| 30 стран Stop Killer Robots полного запрета | chapter §4.3 line 579 | **отсутствует на slides** | ⚠ P1 — ICRC/SKR block отсутствует как dedicated visual |
| X-62A: 100 000+ строк software changes, 21 испытательный полёт | chapter §3.2 line 434 | s27 stats | ✓ |
| X-62A: 2 000 футов nose-to-nose / 1 200 миль/ч | chapter §3.2 | s27 timeline + speaker notes | ✓ |

**Сводный count цифр:**
- ✓ Совпадают: 32.
- ⚠ P2 минор (round / в speaker notes only): 3.
- ✗ P1/P0 dropped (есть в chapter, отсутствуют в slides): 5 (ALIS $42-44k/h, Anduril Lattice $20B, Shield AI 3 цифры из V-BAT case, 30 стран SKR).

---

## Source attribution consistency

Chapter содержит 104 ref. Slides ссылаются на цитаты в `references:` frontmatter + visible source-footers. Сверка:

| Chapter source | Cited в slides | Match? |
|---|---|---|
| Boyd 1976 | s05 frontmatter `[boyd-1976]` | ✓ |
| Osinga 2007 | s05 frontmatter `[osinga-2007]` | ✓ |
| Defense One 2025 Maxar | s01, s08 frontmatter | ✓ |
| BusinessWire 2025 Maxar Sentry | s01, s08 | ✓ |
| Military Aerospace 2025 | s01 | ✓ |
| BlackSky 8-K Q4 2024 | s09 `[blacksky-2024-8k]` | ✓ |
| Planet IR 2024 | s09 `[planet-ir-2024]` | ✓ |
| Airbus 2024 Skywise | s12 | ✓ |
| Klover.ai 2024 + CIO 2024 (Rolls-Royce) | s12 | ✓ |
| TASS 2024 BRICS | s11 | ✓ |
| Aviation Week 2024 + Sputnix 2025 | s11 | ✓ |
| Du et al. 2024 arXiv:2312.02912 (SAR adversarial) | s14 | ✓ |
| Stanford SCPNT 2025 | s14 | ✓ |
| Foreign Policy 2024 GPS spoofing | s14 | ✓ |
| GAO-20-316 / GAO-22-105128 (ALIS) | **отсутствует в slides** (ALIS dedicated slide отсутствует) | ✗ |
| DefenseScoop 2024-2025 Palantir MSS | s18 | ✓ |
| GovConWire 2024 Palantir | s18 | ✓ |
| Abraham 2024 +972 Lavender | s21 `[abraham-2024-972]` | ✓ |
| Lieber 2024, AOAV 2025 | s21 | ✓ |
| USNI Proceedings 2018 Vincennes + Foreign Affairs 2024 | s22 | ✓ |
| CSIS 2025 Lancet | s22 | ✓ |
| Wikipedia YFQ-44 + Air & Space Forces 2026 + The Aviationist 2026 | s26 | ✓ |
| DARPA 2024 ACE + Aviationist 2024 | s27 | ✓ |
| MWI 2025 Saker Scout + CSIS 2025 Ukraine + Kyiv Independent 2025 | s27 | ✓ |
| CSIS 2026 Bondar (Russia drone ecosystem) | s28 | ✓ |
| Autonomy Global 2025 Geran-2 + Meta-Defense 2026 + ISW 2025 + HUR 2025 | s28 | ✓ (Autonomy упомянут frontmatter; ISW/HUR в speaker notes) |
| Tom's Hardware 2024 + Fortune 2026 (Shreya) | s28 | ✓ |
| Cognitive Pilot 2025 + TASS 2024 | s28 | ✓ |
| PMC 2020 Boeing + ThinkReliability 2019 | s29 | ✓ |
| Trenchart 2018 Patriot + SOFREP 2003 | s29 | ✓ |
| Stop Killer Robots 2024-2025 | s33, s37 | ✓ |
| UN Press ga12736 (Nov 2025) | s33 | ✓ |
| US Mission Geneva 2025 (explanation of vote) | s33 speaker notes | ✓ |
| DoD Directive 3000.09 (2023) | s33 sidebar | ✓ |
| ICRC Position Paper 2024 + Vienna 2024 + 2025 updated | **отсутствует в slides** (ICRC dedicated slide отсутствует) | ✗ — нарушение P1 |
| HRW 2024-2025 (UN treaty 2026, country positions) | **отсутствует в slides** (отсылка только в s40 reading list speaker notes) | ⚠ P1 partial |
| TechPolicy Press 2018 Maven walkout | s35 | ✓ |
| Intercept 2024 OpenAI | s35 | ✓ |
| BusinessWire 2024 Anthropic | s35 | ✓ |
| CNBC 2025 | s35 | ✓ |
| DefenseScoop 2025 Replicator + Responsible Statecraft 2025 + Breaking Defense 2025 DAWG | **отсутствует** (Replicator dedicated slide отсутствует) | ✗ — нарушение P1 |
| Scharre Army of None 2018 | **отсутствует в slides** (reading list block missing) | ⚠ P1 partial |
| Russell & Norvig 2021 | n/a (cross-course ref) | ✓ acceptable |
| Roediger & Karpicke 2006 | n/a (course-method ref) | ✓ acceptable |

**Source mismatch P0/P1:**
- GAO ALIS reports (104 chapter source) — отсутствует в slides.
- ICRC Position Paper / Vienna Statement (3 chapter sources) — отсутствует в slides.
- DoD Replicator / DAWG (3 chapter sources) — отсутствует в slides.
- Reading list Scharre, HRW, GAO, SKR briefs (5 chapter §5.3 sources) — отсутствует в slides.

Это последствия 3 P0 + 2 P1 structural gaps (ALIS-без-слайда, ICRC-без-слайда, Replicator-без-слайда, reading-list-без-блока).

---

## Strict-in distribution per artifact

**Chapter strict-in (per Phase 4 reports):** ~46% holistic, distributed:
- §1.6 ALIS (~3% of глава), §1.7 SAR + GPS (~3%), §1.8 criteria 1-2 (~1%).
- §2.4 Lavender (~4%), §2.5 Lancet (~2%), §2.6 Vincennes (~2%), §2.7 criteria 3-4 (~1%).
- §3.3 MCAS (~4%), §3.4 Patriot (~2%), §3.5 Replicator (~2%), §3.6 criteria 5-6 (~1%).
- Раздел 4 целиком strict-in (~16% of глава) — L1-L5, UN GGE, ICRC, Maven shift, HITL/HOOL/HOTL, Russia position.
- §5.1 7 criteria matrix (~1%).
- Q&A backup B1-B10 (~5% — все strict-in).
Sum strict-in chapter: ~46%.

**Slides strict-in (по визуальному и speaker-notes contribution):**
- s14 adversarial SAR + GPS — strict-in (2.5 min из 75 = 3.3%).
- s21 Lavender — strict-in (3.5 min = 4.7%).
- s22 Lancet + Vincennes — strict-in (3 min = 4%).
- s24-s31 Section 3 (s25, s26, s27, s28 содержат anti-hype/caveat блоки + s29 целый failure slide MCAS+Patriot) — ~50% strict-in из 14 min = 7 min = 9.3%.
- s31-s38 Раздел 4 (s32 L1-L5, s33 UN GGE, s35 Maven shift, s36 HITL/HOOL/HOTL, s37 Russia votes) — целиком strict-in = 15 min = 20%.
- s39 7 criteria — strict-in (2 min = 2.7%).
- s42 closing payoff — strict-in (1.5 min = 2%).
- s43 Q&A Lavender prompt — strict-in (~0.5 min = 0.7%).

**Sum slides strict-in:** ~50% (per duration).

**Per-section breakdown chapter ↔ slides:**

| Section | Chapter strict-in % | Slides strict-in % | Match? |
|---|---|---|---|
| Sense (Раздел 1) | ~7% holistic (ALIS + SAR + GPS + criteria) | ~5% (s14 + criteria) — но **без ALIS dedicated slide drop ~3%**, что снижает Sense strict-in в slides | ⚠ Под-страх |
| Decide (Раздел 2) | ~9% (Lavender + Lancet + Vincennes + criteria) | ~11% (s17 callout + s21 + s22 + s39) | ✓ matched, slides даже усиливают |
| Act (Раздел 3) | ~9% (MCAS + Patriot + Replicator + caveats + criteria) | ~7% — но **без Replicator slide drop ~2%** | ⚠ Под-страх |
| Раздел 4 целиком | ~16% | ~20% | ✓ matched, slides усиливают (целиком strict-in раздел) |

**Verdict per strict-in distribution:** Holistic ≥30% threshold **выполняется в обоих артефактах**. Distribution **balanced — не concentrated в одном артефакте**. Однако оба пропуска (ALIS-без-slide + Replicator-без-slide) **снижают** strict-in slides в Sense и Act — не разрушают threshold, но «pinch» distribution. Решения P0/P1 missing coverage помогут восстановить «matched per-section distribution» chapter↔slides.

---

## Keystone-axis preserved

✓ **OODA как несущая ось** — preserved:
- chapter §0.2 «Sense → Decide → Act» = s05 «Три звена цепи. AI входит в каждое — по-разному» (identical assertion).
- Pre-keystone visuals: s03 lecture-map шесть карточек = §0.5 «Дорожная карта» — identical content order (Р0 / Р1 Sense / Р2 Decide / Р3 Act / Р4 Граница / Р5 Сборка).
- Section dividers s06 / s16 / s24 / s31 / s38 — соответствуют структуре глав §1 / §2 / §3 / §4 / §5.
- Closing callback s42 — repeats Sense→Decide→Act с 3 payoff-строками — соответствует §5.4 «Замыкание».

✓ **L1-L5 ladder** — preserved:
- chapter §4.1 таблица «L1-L5 операциональные определения» = s32 schema с identical content (L1 Palantir MSS, L2 Saker Scout, L3 Fury, L4 Patriot/S-400, L5 debated not deployed).
- ms-to-intervention column matches: human-paced / seconds / 100-1000 ms / <100 ms / N/A — все identical.
- Границы L3↔L4 (engineering debate) и L4↔L5 (treaty debate) — identical formulation.

✓ **HITL/HOOL/HOTL** — preserved:
- chapter §4.6 mapping = s36 triada — identical (HITL=L1,L2 / HOOL=L3,L4 / HOTL=L5).
- Examples identical: Palantir MSS analyst (HITL), Saker Scout operator (HITL), Fury wingman (HOOL), Patriot auto ROE (HOOL).
- Engineering takeaway «сколько ms у оператора на intervention» = «формальная категоризация» — identical in s36 callout.

✓ **Dual-use bridge** — preserved:
- chapter §0.4 «Гражданское и военное: одни модели, два контура» = s05 dual-use band + s11 caveat + s28 Geran-2/Cognitive Pilot pair + s40 career «контуры» — identical thread.

**Verdict:** Keystone axis **полностью consistent** между chapter и slides. Это сильное место.

---

## Excluded items honored

Chapter v3 mandate (§5.2 anonymized 2026-05-20):
- ✗ МГТУ/Бауман/ИУ/ВКА/Можайский/МАИ/СПбГУ — **0 hits в slides** ✓ (anonymized)
- ✗ Aerostate — **0 hits в slides** ✓
- ✗ Sber GigaChat ISS / МКС — **0 hits в slides** ✓

Все Q&A backup B2-B4 — соответствующие caveats — присутствуют в speaker notes s43 (verbal); как visible body отсутствуют (acceptable). chapter §5.2 «Российский академический контур» в s40 career card — generalised формулировка «Профильные технические университеты + военно-космические академии» (без named refs) — соответствует chapter Q&A B4.

**Verdict:** все excluded items **дисциплинированно соблюдены**. Это сильное место.

---

## Russian context proportion

**Chapter Russian context** ~22-25% (per fact-checker reports phase 4):
- §1.5 ТЕРРА ТЕХ / СКАНЭКС / СПУТНИКС (~2%)
- §2.2 case 5 Svod / Glaz-Groza-ZOV (~1.5%)
- §3.2 case 5 Geran-2 (~3%)
- §3.2 case 6 Cognitive Pilot (~1.5%)
- §1.7 GPS-spoofing атрибуция (~1%)
- §3.5 Russian supply chain через Shreya (~0.5%)
- §4.7 Россия votes context (~1.5%)
- Q&A B2 (GigaChat caveat), B4 (closed programmes caveat) (~2%)
- §5.2 Russian academic + dual-use (~2%)

**Sum: ~15-17% explicit Russian content; ~22-25% holistic если включить mentions в comparative blocks.**

**Slides Russian context** (по time / slide-content):
- s11 Russian sat layer (2 min из 75 = 2.7%)
- s14 RU EW attribution для GPS-spoofing (mention в visible card + 0.5 min)
- s16 divider speaker notes (Svod / Glaz-Groza verbal) — visual: 0.
- s28 Geran-2 + Cognitive Pilot (2.5 min = 3.3%)
- s37 Russia votes context (1.5 min = 2%)
- s40 career card «Российский dual-use» (~10s в visible)
- s11/28 caveats verbal in speaker notes

**Sum slides:** ~9-10% explicit visible + ~3-4% verbal-only — холистически ~13%.

**Drift:** chapter ~22-25%, slides ~13% — **slides under-represent Russian context relative to chapter**. Это P2-level concern: связано с тем, что (a) §2.2 case 5 Svod/Glaz-Groza-ZOV не имеет dedicated visual (последствие s18 missing coverage), (b) §1.5 sat layer урезан до 2-min slide, (c) Russian supply chain caveat в s28 — компактный, не expansive.

**Verdict:** Russian context distributed в slides в правильных местах (s11 / s14 / s28 / s37), но quantitatively under-represented vs chapter. **P2**, не P1: учебный баланс сохранён, но «полнота» снижена. Связано с structural gap §2.2 case 5 → s18 visual.

---

## P0 / P1 / P2 issues — итог

### P0 (factual contradiction / missing structural coverage)

**P0-1: Edge-AI on-orbit (§1.3) — отсутствует как slide.**
- **Where:** chapter §1.3 (Slingshot Agatha+TALOS, ESA Φ-sat-2, Lockheed Pony Express, AI-eXpress, TerraTech) — full subsection с 4 категориями программ. deck.yaml v2 декларирует «MERGED: s09+s10 → s09 (constellation + edge-AI on one slide)», но фактический `s09-blacksky-planet-constellation.md` содержит **только** 4-vendor constellation table. Никаких mentions of Φ-sat-2 / Pony Express / Slingshot TALOS / edge AI в s09 visible body или speaker notes.
- **Issue:** chapter §1.3 — full educational block (~5% Sense раздела), отсутствует визуально и устно. s06 divider speaker notes говорит «во-вторых, edge AI on-orbit: ML-вычисления прямо на спутнике через ESA Φ-sat-2, Lockheed Pony Express, Slingshot Aerospace» — orphan reference на отсутствующий следующий slide.
- **Recommendation:** добавить s10 edge-AI on-orbit (4 категории: Demonstrators / Production telemetry / SDA tracking / Commercial archive) **или** обновить s09 с реальным merged content **или** обновить deck.yaml comment чтобы не lying about «merged» когда фактический slide — только constellation. Также fix s06 divider speaker notes (orphan reference).

**P0-2: Decide vendor landscape (§2.2 — 5 cases) — частично отсутствует.**
- **Where:** chapter §2.2 имеет 5 detailed cases: (1) Palantir MSS, (2) Scale Donovan/Defense Llama/Thunderforge, (3) Helsing Altra/Centaur (€12B / Daniel Ek), (4) Anthropic-Palantir-AWS IL6, (5) Russian C2 Svod/Glaz-Groza-ZOV (single-source caveat). deck.yaml v2 декларирует «s18 — MERGED: Decide vendor landscape (Palantir+Scale+Helsing+Anthropic+RU)», но фактический `s18-palantir-mss.md` посвящён только Palantir MSS.
- **Issue:** 4 из 5 кейсов §2.2 не имеют dedicated visual presence. Scale Donovan/Defense Llama/Thunderforge table (chapter §2.2 case 2) — substantial 3-product progression history с FedRAMP HIGH / SC2S/SIPR/IL4/JWICS auth stack — отсутствует. Helsing €12B + Centaur AI-pilot — упомянут в s35 vendor list one-liner, но не как dedicated Decide-кейс. Anthropic-Palantir IL6 — упомянут только в s35 era 3 timeline (а не в Decide раздела). Russian C2 — verbal-only в s16 divider speaker notes.
- **Recommendation:** либо добавить s19 (Scale + Helsing + Anthropic vendor card matrix) + s20 (Russian C2 с single-source caveat), либо обновить s18 фактическим merged content (как декларирует deck.yaml), либо обновить deck.yaml comment чтобы не lying about MERGED state. Связано: глоссарий term #16 (Scale stack), term #17 (Helsing) — введены в chapter, ноль visible presence в slides.

**P0-3: Shield AI V-BAT case (§3.2 case 2) — отсутствует.**
- **Where:** chapter §3.2 line 432 — Shield AI V-BAT + Hivemind с $198M USCG / Индийская армия январь 2026 / $35M emergency / JSW Defence $90M в Хайдерабаде / Shield AI $2B раунд 2025 / $5,6-12,7B valuation `[VFY]` / уровень L2/L3. Glossary term #19. s24 divider speaker notes говорит «Shield AI V-BAT плюс Hivemind» — обещает кейс, который не появляется.
- **Issue:** V-BAT — substantial case в chapter Act-разделе (~1.5% всей лекции). В slides — только brand-mention в s26 spec sidebar («Hivemind (Shield AI)» как stack для Fury) + один-liner в s40 career card («Perception (Shield AI)»). $198M USCG / Индийская армия / $5,6-12,7B valuation — все ушли.
- **Recommendation:** добавить V-BAT slide (можно в виде split-card вместе с другими minor Act vendors) **или** explicit decision что V-BAT не покрывается (тогда снять обещание из s24 speaker notes — orphan reference).

### P1 (significant drift)

**P1-1: F-35 ALIS canonical failure (§1.6) — нет dedicated slide.**
- **Where:** chapter §1.6 — full subsection (~3% Sense раздела), 3 уроки PdM (быстрый feedback / ground truth / FP-cost), $42-44k/h cost-per-hour, переход ALIS → ODIN июнь 2024 (government-owned / disconnected mode / отдельный HITL для flight-clearance). GAO-20-316 + GAO-22-105128 + Defense Daily 2024 + Air & Space Forces 2024 — cited в chapter. Glossary term #24.
- **Issue:** в slides ALIS как canonical Sense-failure представлен только как footer caption в s12 («В обороне аналог — F-35 ALIS → ODIN. Об этом — следующий слайд»), но «следующий слайд» (s14) — adversarial SAR ATR, не ALIS. Orphan reference. Cost $42-44k/h из chapter §1.6 — dropped. 3 уроки PdM (которые работают как cross-cutting шаблон в Лекции 14) — не visible.
- **Recommendation:** либо вернуть s13 ALIS failure (deck.yaml v2 указывает s13 deleted в merge), либо expand s12 right column добавив ALIS 4-row failure timeline, либо снять orphan reference из s12 footer.

**P1-2: ICRC + Stop Killer Robots civil society (§4.3) — нет dedicated visual.**
- **Where:** chapter §4.3 — full subsection: ICRC position (Prohibit unpredictable AWS + AWS used against people; Restrict остальные; ethical core «Ceding life-and-death decisions to machine sensors and software is a dehumanizing process»; procedural core «It is not the weapon system that must comply with IHL, but the humans using it»). Stop Killer Robots — coalition 270 НКО / 70 стран, 30 стран явно поддерживают полный запрет.
- **Issue:** deck.yaml v2 декларирует «s33 — MERGED: UN GGE timeline + ICRC/SKR civil society», но фактический s33 — только UN GGE timeline + DoD Directive sidebar. ICRC «It is not the weapon system that must comply with IHL...» — central ethical formulation chapter, отсутствует в slides. 30 стран SKR — отсутствует.
- **Recommendation:** добавить s34 ICRC + SKR slide или expand s33 sidebar чтобы включить ICRC 2-quote + 30 стран list.

**P1-3: DoD Replicator missed scale (§3.5) — нет dedicated visual.**
- **Where:** chapter §3.5 — failure case: Replicator-1 missed scale «сотни вместо тысяч» к августу 2025, Replicator-2 (сентябрь 2024) перефокусирован на counter-UAS, DAWG (декабрь 2025) — succession. CETC Atlas 96 дронов / 1 планшет — анти-пример «не truly decentralized swarm». DefenseScoop 2025 + Responsible Statecraft 2025 + Breaking Defense 2025 cited.
- **Issue:** s24 divider speaker notes обещает «три канонических провала: Boeing 737 MAX MCAS, Patriot friendly fire, DoD Replicator missed scale», но s29 покрывает только MCAS + Patriot. Replicator — отсутствует как visual; упомянут только в s24 verbal и s40 career footer.
- **Recommendation:** добавить s30 Replicator failure (deck.yaml v2 указывает s30 deleted в merge — но фактический content не consolidated в другом slide).

**P1-4: Reading list 7 источников (§5.3) — нет visible content.**
- **Where:** chapter §5.3 — 7 reading sources: Scharre Army of None, CSIS Bondar 2026, Abraham Lavender, ICRC Position 2024, DARPA ACE briefings, GAO-20-316/GAO-22-105943 ALIS, Stop Killer Robots briefs 2025.
- **Issue:** deck.yaml v2 декларирует «s40 — MERGED: career profiles + reading list», но фактический s40 содержит только 5 профилей + 3 контура. Reading list — упомянут только в s40 speaker notes briefly («NASA, ESA — космическая наука, FDL программа»), но не как visible block. 7 reading sources — отсутствуют.
- **Recommendation:** добавить s41 reading list (deck.yaml указывает s41 deleted) или expand s40 нижней частью.

**P1-5: Anduril Lattice $20B army contract (Введение line 106) — отсутствует.**
- **Where:** chapter Введение line 106 — «контракт Anduril Lattice с армией США имеет потолок до 20 миллиардов долларов на 10 лет (Army Recognition, март 2026)». Это infrastructure-scale число параллельно с Palantir MSS $1,3 миллиарда.
- **Issue:** s18 Palantir MSS показывает $1,3 миллиарда как infrastructure scale, но parallel-scale Anduril Lattice $20B — не отражён. Это chapter intro number — драматичный «infrastructure not future» сигнал — dropped.
- **Recommendation:** добавить упоминание в s35 era 2 либо в s26 Anduril slide.

### P2 (minor inconsistencies)

**P2-1: Anduril valuation rounding drift.**
- chapter §4.5 line 601: «$30,5 миллиарда к 2024».
- s35 era 2: «$30,5 млрд к 2024» — ✓.
- но s25 act intro speaker notes: «Anduril оценивается в 30 миллиардов долларов» — drop «.5» (rounding drift).
- **Recommendation:** sync s25 speaker notes к «$30,5 млрд» или явный «~30 миллиардов» как round.

**P2-2: Anglicism residue в visible body.**
- s22 visible badge «**LO2 canonical case**» — слово «canonical» в visible.
- s27 visible: «narrow scripted scenario · 1-на-1 dogfight · BVR исключён · fuel management не покрыт · ROE не учитывался» — «narrow scripted scenario» / «fuel management» в visible body.
- s32 «Currently debated, not deployed» — английская строка в visible.
- deck.yaml v2 декларирует «~50+ англицизмов в visible body заменены на русские». Проверка — это «mostly done», но эти 3 residues остались.
- **Recommendation:** замена на «канонический», «узкий заскриптованный сценарий», «расход топлива не покрыт», «обсуждается, не развёрнуто».

**P2-3: Russian context proportion drift.**
- chapter ~22-25%, slides ~13%. Связано с P0-2 (Russian C2 в s18 missing) и P1-4 (no reading list).
- **Recommendation:** покрывается P0-2 fix.

**P2-4: SDA Tracking Layer / PWSA не упомянут.**
- chapter §1.3 + Glossary term #23 introduces SDA Tranche 3 / PWSA.
- В slides — 0 mentions.
- **Recommendation:** связано с P0-1 (edge-AI slide); SDA — часть того же missing block.

**P2-5: Geran-2 «plan-capacity 5 000+» — только speaker notes.**
- chapter §3.2 line 440: «производительность около 2 700-3 000 дронов в месяц с plan-capacity 5 000+».
- s28 visible card: «~2 700-3 000 / месяц» — без plan-capacity. Speaker notes: «с план-capacity 5 000 плюс».
- **Recommendation:** добавить «(plan-capacity 5 000+)» в visible card.

---

## Recommendations (приоритезированный список для presentation-designer)

**Must-fix перед USER GATE B (P0):**

1. **Resolve edge-AI on-orbit gap (P0-1).** Variant A: добавить s10 (4-cell matrix: Demonstrators / Production telemetry / SDA tracking / Commercial archive). Variant B: expand s09 фактическим merged content. Variant C: обновить deck.yaml + s06 divider убрать orphan reference. Decision — за дизайнером + куратором.
2. **Resolve Decide vendor landscape gap (P0-2).** Variant A: добавить s19 (Scale + Helsing + Anthropic 3-card matrix) и s20 (Russian C2 Svod/Glaz-Groza с single-source caveat). Variant B: expand s18 фактическим MERGED content. Variant C: обновить deck.yaml + s16 divider убрать orphan reference про Helsing/Anthropic/Russian C2 cases.
3. **Resolve Shield AI V-BAT gap (P0-3).** Добавить V-BAT card (можно split вместе с другим Act-кейсом) либо снять обещание из s24 speaker notes.

**Should-fix перед USER GATE B (P1):**

4. **F-35 ALIS dedicated slide или expanded s12 (P1-1).** Восстановить s13 или expand s12 right column с 3 PdM-условиями + $42-44k/h + ODIN transition.
5. **ICRC + SKR civil society slide (P1-2).** Добавить s34 либо expand s33 sidebar чтобы покрыть ICRC «Procedural core» + 30 стран SKR.
6. **DoD Replicator slide (P1-3).** Добавить s30 либо integrate в s29.
7. **Reading list (P1-4).** Expand s40 нижней секцией с 7 источниками.
8. **Anduril Lattice $20B intro number (P1-5).** Добавить в s26 либо в s35.

**Nice-to-fix (P2):**

9. Anduril valuation s25 → «$30,5 млрд» (P2-1).
10. Anglicism residues s22 / s27 / s32 (P2-2).
11. SDA Tranche 3 mention (P2-4, depends on P0-1).
12. Geran-2 «plan-capacity 5 000+» в s28 visible card (P2-5).

---

## Top-N фиксов per artifact

- **Chapter (фактически меняется только если slide gap отражается обратно):** ничего не менять, chapter v3 finalized. (Один nuance: если Decide vendor cases 2-5 решено выкинуть из slides из-за временного бюджета, **проверить, что chapter их сохраняет** для self-study — что и есть текущее состояние, OK.)
- **Slides (приоритет):**
  1. **s09 / s10** — explicit edge-AI on-orbit block либо обновить deck.yaml + s06 notes.
  2. **s18 / s19+s20** — Decide vendor landscape (Scale, Helsing, Anthropic, Russian C2) либо обновить deck.yaml + s16 notes.
  3. **s24 / s27 / s28** — V-BAT presence (либо new slide, либо expand existing Act-card).
  4. **s12 / s13** — ALIS PdM-неудача (либо new slide, либо expand s12).
  5. **s33 / s34** — ICRC + SKR civil society.
  6. **s29 / s30** — Replicator missed scale.
  7. **s40 / s41** — reading list (либо expand s40).
- **Speech (Phase 10):** будет проверяться отдельно. Текущая важная заметка: speech должна **синхронизироваться со final slide list** — если P0-1/P0-2/P0-3 не зафиксованы, speech не должна обещать «edge-AI on-orbit» / «Scale Donovan / Defense Llama / Helsing» / «V-BAT» из verbalisation, потому что соответствующих slides нет.

---

## Verdict rationale

**REVISE** (не APPROVE-WITH-POLISH), потому что:
- 3 P0 missing-coverage issues с orphan references в speaker notes (≥1 case на каждый = ≥3 явных «lecturer обещает кейс, slide не показывает» moments) — это **structural** mismatch, не polish.
- 5 P1 issues с substantial chapter blocks (ALIS / ICRC / Replicator / reading list / $20B Anduril) полностью отсутствующих как visible content в slides.
- 4 P2 minor drift.
- Per Critic Verdict Rule (CLAUDE.md): если ≥5 P1 issues но verdict = APPROVE-WITH-POLISH — STOP, change to REVISE. Имеем 5 P1.
- deck.yaml v2 в comments ОБЕЩАЕТ что MERGED-слайды s09/s18/s33/s40 содержат указанный content, но фактические файлы slides не несут декларируемый MERGED content. Это **deck.yaml ↔ slides** мис-alignment в добавок к chapter ↔ slides.

Положительные стороны (сильные основания для финального APPROVE после fix):
- Keystone-axis OODA + L1-L5 + HITL/HOOL/HOTL — **полностью consistent**, identical formulations.
- Numerical claims 32 из ~40 — **полностью consistent**, no drift (37 000 / 3 700 / 290 / 346 / 164/6/7 / 11 600 / $1,3B / €12B / 30,5 / 23 марта 2026 / 31 октября 2025 — все совпадают).
- Glossary 28 terms — большинство **identical** в slides; drift только там, где соответствующий case-slide отсутствует.
- Excluded items mandate (МГТУ/Бауман/Aerostate/GigaChat) — **дисциплинированно соблюдён**.
- Strict-in distribution **balanced** между chapter (~46%) и slides (~50%), holistic ≥30% — ✓ AI-Failure & Judgment threshold passed в обоих артефактах.
- Cited sources — большая часть **identical**; missing sources — следствие missing slides, не self-contradiction.

После fix P0-1 / P0-2 / P0-3 + 2-3 P1 — verdict перейдёт в **APPROVE-WITH-POLISH**.

---

*Конец отчёта. Готов к передаче в orchestrator + presentation-designer для revision round.*
