---
synthesis_of: notes/lecture-12-review/plan-v1.md
critics_input:
  - critique-of-plan-v1-methodology.md (verdict: REVISE, P0=0, P1=7, P2=6)
  - critique-of-plan-v1-reader-text.md (verdict: APPROVE-WITH-POLISH, ~5 P1-level)
created: 2026-05-21
status: input для plan v2 после owner decisions
---

# SYNTHESIS — plan v1 → plan v2 inputs

> **Composite verdict:** REVISE. Methodology REVISE (7 P1) wins over reader APPROVE-WITH-POLISH per CLAUDE.md verdict scale rules. Plan v1 — крепкий черновик, но нужны 7 strategic + 5 reader-side concrete edits перед Phase 2 (chapter draft).

## 1. Сводная таблица issues

| # | Critic | Severity | Issue | Тип решения |
|---|---|---|---|---|
| **P1-A** | Methodology | P1-2 | **L0–L2 collision с ISA-95** (lec-11 §5.3 использует L0–L2 для архитектурных слоёв). Студент 3 курса спутает. | **Owner decision** — rename axis в A0–A3 (рекомендация critic) ИЛИ оставить L0–L3 + disclaimer? |
| **P1-B** | Methodology | P1-1 | **Anti-overlap с lec-11**: Yokogawa FKDPP, Tesla 2018, ChatGPT-PLC дублируются без differentiation. | **Owner decision** — переориентировать Yokogawa angle (twin-as-sandbox), заменить Tesla 2018 hero на fresh failure ИЛИ оставить с явной cross-reference? |
| **P1-C** | Methodology | P1-7 | **L3 fragmentation** — humanoid распылён по 3 mention без dedicated content. | **Owner decision** — dedicated §4.5 «L3 в 2026» (2 мин) ИЛИ disclaimer-only на s02 keystone? |
| **P1-D** | Methodology | P1-6 | **РФ context** — отсутствует carry-forward от lec-11: ГОСТ Р 57700.37-2021 + Норникель flotation. | **Recommended add** — concrete edit, не strategic. |
| **P1-E** | Methodology | P1-3 | **Pacing §2/3/4 tight** — 10 минут heuristic-tight для assertion + 4-мин failure-bucket + transition. | **Owner choice** — расширить §2/3/4 до 11–12 мин за счёт сжатия §6 (8→6) ИЛИ убрать redundant evidence? |
| **P1-F** | Methodology | P1-4 | **Locked numbers** — 4 missing ($155B AI mfg 2030, $17.15B OPC UA, PdM $200K-$600K + $1.2M-$3.5M + 18-36 мес, Tesla 10% target). | **Concrete edit.** |
| **P1-G** | Methodology | P1-5 | **Twin taxonomy** — Kritzinger 2018 (Model / Shadow / Twin) отсутствует в §1. | **Concrete edit.** |
| **R-1** | Reader | P1 | **Unexplained jargon** в plan body: TSN, FKDPP, GAMP 5, ATEX Zone 0, scan-based execution, Lighthouse Network, SHAP/LIME, MTBF, RCM (в таблице без повтора расшифровки). | **Concrete edit** — inline gloss первого упоминания. |
| **R-2** | Reader | P1 | **Альтернативы AI без определений** — MPC, formal verification, RCM, IEC 61508 SIL — упомянуты как «магические заклинания». | **Concrete edit** — 1 фраза-якорь на каждую альтернативу. |
| **R-3** | Reader | P1 | **§7 Career section слишком тонкий** — 4 названия профессий без «что делает день за днём». LO7 gap. | **Concrete edit** — расширить §7 (но в рамках 5-мин бюджета). |
| **R-4** | Reader | P2 | **Section 1 ↔ Section 5 partial duplication** — Big Idea «вторая мысль» (про границы AI) повторно раскрывается в §5. | **Concrete edit** — сжать Section 1 «вторую мысль» в одну строку с forward-pointer на §5. |
| **R-5** | Reader | P2 | **Failure cases без концретики** — ChatGPT для PLC без конкретного MOV %M99999 примера; RL sim-to-real без конкретного gap-кейса; data-layer audit без 5-вопросного checklist. | **Concrete edit.** |
| **P2-a** | Methodology | P2-1 | **Hero s07 (Siemens Composer) — только 2 tier**, расширить до 6-tier. | Concrete edit. |
| **P2-b** | Methodology | P2-2 | **s05 «3D ≠ twin» composite** — risk mock-fallback в дисguise. | Owner choice — single real screenshot ИЛИ vector diagram «4 layers required»? |
| **P2-c** | Methodology | P2-3 | **Russification таблица — 4 missing patterns**: cascade, expectation gap, data layer audit, worked example. | Concrete edit. |
| **P2-d** | Methodology | P2-4 | **Bridge text на s39 — terminology drift** с lec-11 §5.3 framing. | Concrete edit — lock «AI в логистике, цепях поставок и транспорте». |
| **P2-e** | Methodology | P2-5 | **s02 keystone-table — 5 столбцов**, density risk. | Designer-level decision (Phase 5) — vector diagram of ladder. |
| **P2-f** | Methodology | P2-6 | **Q&A backup mention** не записан в carry-forward (Section 11). | Concrete edit + tied to owner Q#6 decision. |

## 2. Strengths preserved (plan v2 НЕ должна потерять)

- ✅ **Keystone-axis формулировка эталонная** (Section 2 dedicated keystone-слайд ДО первого погружения, 5 пунктов обоснования)
- ✅ **Failure-share 44%** распределено по 6 разделам (holistic, не single-section concentration)
- ✅ **Anonymization 0 named institutions** verified by grep
- ✅ **Hero plan для s01 + s39** с 6-tier acquisition strategies
- ✅ **Media plan 61% ≥50% target**
- ✅ **10 явных «не применяй AI / альтернатива лучше»** правил в Section 5 (failure inventory)
- ✅ **Frontmatter clean** (audience, target words, hero plans)
- ✅ **Locked numbers convention** (нужно дозаполнить 4 missing — P1-F)

## 3. 6 strategic decisions для owner

| Q# | Decision | Critic recommend | Critic source | Cost-of-defer |
|---|---|---|---|---|
| **Q1** | **Rename keystone axis L0–L3 → A0–A3?** | **YES — переименовать в A0–A3** (Autonomy levels, anchor SAE J3016 + ISO 22989). Убирает collision с ISA-95. | methodology P1-2 | Если defer → каждый downstream агент должен повторять «не путать с ISA-95» disclaimer. Cumulative drift risk. |
| **Q2** | **Tesla 2018 в §5 — оставить, заменить на Southeast Asian Port, или Foxconn deep-dive?** | **Заменить hero на Southeast Asian Port 2024** — direct relevance к keystone twin + fresh (не дублирует lec-11). Tesla 2018 — single line + cross-reference lec-11. | methodology P1-1 | Студент видит Tesla 2018 дважды (lec-11 + lec-12) → восприятие «повтор» → engagement drop. |
| **Q3** | **L3 humanoid: dedicated §4.5 (2 мин) vs disclaimer-only?** | **Hybrid: §4.5 в 2 мин** (Toyota Digit + BMW Leipzig — существующие + «почему остальные не L3») + explicit «L3 = единицы кейсов» на s02 keystone. Бюджет: компенсировать сжатием §6 (8→6). | methodology P1-7 | Если оставить fragmented → ось «L0-L3» ощущается incomplete (3 ступени раскрыты, 4-я только namedrop). |
| **Q4** | **Добавить ГОСТ Р 57700.37-2021 + Норникель flotation в §7 РФ context?** | **YES** — carry-forward от lec-11 §3.5. ГОСТ — формальная RU регуляторика для «цифровых двойников» (мандатно для лекции про двойники); Норникель — process-control L2 case в РФ (синергия с §4). | methodology P1-6 + reader Q3 (студент хочет RU failure cases) | Без ГОСТ — лекция про «цифровые двойники» без российской регуляторной базы воспринимается как «оторванная от РФ инженерной реальности». |
| **Q5** | **§2/3/4 pacing: extend до 11–12 мин (за счёт §6 8→6) ИЛИ drop redundant evidence (например, automotive -30%/+40% дубль cement 57x)?** | **Drop redundant evidence (default)** — automotive ROI и cement plant — duplicate metric class; оставить cement+chemical; не трогать §6 (там architecture важна). | methodology P1-3 | Cognitive overload в §2/3/4 → студент пропустит ключевые transitions к keystone. |
| **Q6** | **Worked example в §5: (a) фарма + дозировка / FDA, (b) металлургия RL печи, (c) автолиния vision tight tolerance?** | **(a) фарма** — strongest pedagogical case (FDA 21 CFR Part 11 connect к lec-07 prerequisite + concrete dosing math + clear «AI не подходит для финального release»). | methodology Section 10 op Q#5 (открытый) | Без worked example §5 = abstract rules; с примером — actionable. |
| **Q7** | **Q&A backup 14 вопросов в chapter (как lec-11)?** | **YES** — lec-11 established pattern, owner explicit «глубже как L8/L9» в lec-11 reflection. 14 Q&A добавляют ~3-4k слов к 30k target. | methodology P2-6 + book-editor open Q#6 | Без Q&A backup — chapter теряет «лектор-ready» quality (быстрые ответы на ожидаемые студентские вопросы). |

## 4. Concrete edits для book-editor plan v2 (no owner decision needed)

После owner decisions Q1-Q7, book-editor должен в plan v2:

1. **Apply axis decision (Q1)** во все слова «лестница» / keystone-axis / s02 / minute budget table / Section 2 / Section 4 §-headings.
2. **Apply anti-overlap decisions (Q2)** — переписать §4 Yokogawa angle на twin-as-sandbox; заменить §5 intro hero per Q2 choice; добавить cross-reference на lec-11 §1.2 / §2.4 / §5.3 везде где случай дублируется.
3. **Apply L3 decision (Q3)** — если §4.5 — добавить раздел с тайм-бюджетом; если disclaimer — расширить s02 keystone descriptive text.
4. **Add ГОСТ Р 57700.37-2021 + Норникель** в §7 (если Q4=YES).
5. **Apply pacing decision (Q5)** — либо drop evidence, либо сжать §6.
6. **Add worked example (Q6)** в §5 в выбранной форме (фарма / металлургия / авто).
7. **Add Q&A backup carry-forward** в Section 11 (если Q7=YES).
8. **Add Kritzinger 2018 taxonomy** (Model / Shadow / Twin) в §1 evidence + s06 mini-table.
9. **Add 4 missing locked numbers** в Section 11: $155.04B AI mfg market 2030, $17.15B OPC UA, PdM $200K–$600K + $1.2M–$3.5M + 18–36 мес, Tesla 2018 ~10% target.
10. **Inline gloss первого упоминания** для: TSN (Time-Sensitive Networking, IEEE 802.1, детерминированный Ethernet), FKDPP (Factorial Kernel Dynamic Policy Programming, NAIST 2018, off-policy RL), GAMP 5 (Good Automated Manufacturing Practice v5), ATEX Zone 0 (взрывоопасная среда категории 0 — постоянное присутствие), scan-based execution (PLC выполняет программу циклами фиксированной длительности, не event-driven), Lighthouse Network (программа WEF + McKinsey для образцовых заводов), SHAP/LIME (методы post-hoc explainable AI), MTBF (Mean Time Between Failures), RCM повтор расшифровки в таблице.
11. **1-фраза-якорь** для каждой альтернативы: MPC (модельное предиктивное управление с явной оптимизацией на горизонте, гарантии устойчивости через теорию Ляпунова), formal verification (математическое доказательство свойств кода — TLA+ / SPIN / Coq / SCADE для safety-critical), RCM (Reliability-Centered Maintenance, методология Nowlan-Heap 1978 из авиации), IEC 61508 SIL 2/3 (вероятностные категории отказоустойчивости: SIL 2 = 10⁻⁶..10⁻⁷, SIL 3 = 10⁻⁷..10⁻⁸ на час).
12. **Расширить §7 career** — 4 названия → 4 описания «что делает день за днём + ключевые навыки + где учиться» (но в рамках 5-мин бюджета).
13. **Сжать Section 1 «вторую мысль»** в 1 строку + forward-pointer на §5.
14. **Add concrete examples failure cases**: ChatGPT для PLC «MOV %M99999» illegal address; RL sim-to-real example with thermal loss + surface fouling drift; data-layer audit 5-вопросный checklist (доступ к историческим данным / sampling rate sufficient / labeling provenance / sensor drift documented / governance owner identified).
15. **Russification 4 missing**: cascade → каскад срабатываний, expectation gap → разрыв ожиданий, data layer audit → аудит слоя данных, worked example → проработанный пример.
16. **Расширить hero s07 fallback до 6-tier**.
17. **Fix s05 mock-risk** — если не single real screenshot, то vector diagram «4 layers required» (методически чище).
18. **Lock bridge text** на s39: «AI в логистике, цепях поставок и транспорте» — single canonical phrasing.

## 5. Path to APPROVE-CLEAN

После plan v2 — re-spawn methodology-critic + reader-text-only для verification. Expected verdict: APPROVE-CLEAN (все 7 P1 + 6 P2 + 5 reader-side closed).

Если ≥1 P1 остаётся — plan v3 (но это unusual для quality plan v1). Если APPROVE-CLEAN — go Phase 2 (chapter draft, ≥30k words).
