---
critique_of: chapter v3 ↔ slides v1 alignment
critic: consistency-checker
verdict: REVISE
created: 2026-05-22
---

# Summary

Slides v1 (39 слайдов) demonstrate **very strong alignment** with chapter v3 (~30k слов, 4 parts) на уровне:
- Coverage parity (каждый chapter § покрыт slide-блоком; каждый slide производный от chapter)
- Keystone phrasing (A0→A1→A2→A3 + «цифровой двойник — мост» — 1:1 везде)
- Kritzinger taxonomy (3 уровня + ГОСТ Р 57700.37 — exact match)
- Все locked numbers ($36.19B, $180.28B CAGR 37.87%, $155.04B, $17.15B, 75%/11%/14%, 40%/30%, 99%+/0.1-2%, 35 days, $12M/18 мес, Lighthouse 220+/35/23/90%/+16%) — exact match between chapter and slides
- Bridge к Лекции 13 — canonical phrasing «AI в логистике, цепях поставок и транспорте»
- Section structure (8 разделов + 8 dividers) — exact match с chapter §0.3 roadmap

**Однако найдено 4 issues, блокирующих APPROVE:**

1. **P0 factual contradiction** на s17 rendered (MOV %M99999 «PLC откажется компилировать»): chapter §3.4 explicitly says код **скомпилируется** в TIA Portal, а проблема — STOP-mode при runtime, не compile-time. Это противоречит ключевому уроку §3.4 («код выглядит правдоподобно и компилируется, но не запустится»).
2. **P1 phantom LO8** в speaker notes на s28 + s03 + s39: chapter frontmatter declares только `[LO2, LO5, LO7]`. LO8 — orphan reference.
3. **P1 unverified award attribution** на s20: speaker notes assert «премию премьер-министра Японии в 2023» **definitively**, но chapter имеет explicit `[FACT-CHECK]` marker на этом факте.
4. **P2 terminology drift Edge AI ↔ Крайний AI ↔ ИИ на границе сети**: chapter §6.3 canonical = «Крайний AI», но s33 visible body uses bare English «Edge AI» в одном из 7 layers + s38 «edge AI engineer». Glossary lock желателен.

Coverage parity и numbers ARE excellent. Main issue — **factual claim mismatch on s17 (P0)**, остальное revise-level.

# Terminology drift table

| Term | Chapter canonical | Slide form(s) | Verdict |
|---|---|---|---|
| Шкала автономии A0→A3 | «шкала автономии AI в производстве A0→A1→A2→A3» (§0.1) | s04 «Шкала автономии AI в производстве: A0→A3»; s39 «шкала автономии A0–A3» | OK |
| Цифровой двойник как мост | «цифровой двойник — мост между ступенями» (§0.1) | s04 «Цифровой двойник — мост между A1 и A2»; s39 «двойник как мост» | OK |
| Kritzinger Digital Twin | «Digital Model / Digital Shadow / Digital Twin» (§1.1) | s06 «Цифровая модель / Цифровая тень / Цифровой двойник» + EN labels | OK (RU+EN inline) |
| ГОСТ Р 57700.37-2021 | «ГОСТ Р 57700.37-2021 „Цифровые двойники изделий. Общие положения"» (§1.1 + §7.1) | s06: «ГОСТ Р 57700.37-2021 „Цифровые двойники изделий. Общие положения"»; s37: «ГОСТ Р 57700.37-2021» | OK |
| Edge AI / Крайний AI | «Крайний AI» (§6.3 title) + «ИИ на границе сети» (parenthetical gloss) | s33 visible body «Edge AI» (bare English); s38 «edge AI engineer»; s04/s25 speaker notes «edge AI»; s34 «edge AI inference <10 мс» | **P2 drift** — 3 forms across artifacts; chapter canonical is RU «Крайний AI», deck uses EN «Edge AI» as primary surface form. Glossary lock recommended. |
| Защитная зона действия / safety envelope | «защитная зона действия (safety envelope)» (§4.1, chapter-part2) | s04 «safety guardrails» (для A3); s25 «safety envelope» (component of full-stack для A3) | OK — chapter has both («safety envelope» для A2 + «safety guardrails» для A3); slides preserve same distinction |
| Closed-loop / замыкать петлю | «замыкать петлю» (§4 title) + «closed-loop control» (gloss) | s04/s19 «замыкать петлю»; s33 «замкнутая петля»; assertion s23 «закрытая петля» nowhere | OK |
| sandbox / песочница | «песочница» (RU, §4.3) + «safe sandbox» (EN gloss) | s19/s20/s21 «песочница»; s20 «twin-as-sandbox angle» (EN in designer description) | OK |
| sim-to-real gap / разрыв «симуляция → реальность» | «разрыв "симуляция → реальность" (sim-to-real gap)» (§4.4) | s22 «Разрыв „симуляция → реальность"»; s22 desc «Sim-to-real concrete gap» | OK |
| ИИ на границе сети / edge AI | chapter intro defines «edge AI (крайний / локальный ИИ-инференс)» as gloss | s33 «inference <10 мс»; s38 «edge AI engineer» | OK — gloss preserved |
| FKDPP | «Factorial Kernel Dynamic Policy Programming» (§4.2, chapter-part2) | s20 same + addition «Алгоритм разработан в NAIST в 2018» | OK |
| Yokogawa FKDPP «35 дней» | «35 дней непрерывной работы под RL-контролем» (§4.2) | s04 «Yokogawa FKDPP в JSR химическом заводе в 2022»; s20 «35 дней в 2022»; s39 «JSR 35 дней» | OK |
| Southeast Asian Port $12M / 18 мес / 2024 | «$12 миллионов, 18 месяцев, списан 2024» (§1.5) | s09 same; s27 same | OK |

# Numbers consistency table (15 sampled)

| Claim | Chapter location | Slide location | Match |
|---|---|---|---|
| $36.19B → $180.28B CAGR 37.87% | chapter.md §1.3 + Введение | s08 visible chart («36.19» → «180.28») + speaker notes («36,19 → 180,28 миллиарда, темп 37,87%») | ✓ exact |
| $155.04B AI mfg 2030 | chapter.md Введение | s08 visible («155.04») + notes «155,04 миллиарда долларов к 2030» | ✓ exact |
| $17.15B OPC UA + MQTT AI 2026 | chapter.md Введение + §6.2 | s08 visible («17.15») + notes «17,15 миллиарда в 2026» | ✓ exact |
| 75% twin fail / 11% O&G / 14% expectation | chapter.md §1.4 | s08 notes («75%, 11%, 14%») + s30 («75% twin без ROI / 11% O&G / 14% соответствие») | ✓ exact |
| 40% Gartner agentic / 30% GenAI PoC | chapter.md §1.4 + §5.2 бонус | s30 («40% к 2027 / 30% PoC прекращены к 2025») | ✓ exact |
| 99%+ vision tuned / 0.1-2% FP / 1%×10K=100 | chapter.md §2.1 + §2.2 | s12 chart («10000» / «100 годных отвергнуто») + assertion «99%+ при 0,1–2%» | ✓ exact |
| PdM ROI 10:1 за 2 года | chapter.md §2.3 | s13 visible + assertion + notes «ROI 10 к 1 за 2 года» | ✓ exact |
| PdM $200K-$600K → $1.2M-$3.5M / 18-36 мес | chapter.md §2.3 | s13 visible chart side panel + notes | ✓ exact |
| Cement 57× ROI за 6 месяцев / Chemical $2M | chapter.md §2.3 | s13 visible «Cement plant 57× ROI за 6 месяцев» + «Chemical plant $2 миллиона» | ✓ exact |
| Yokogawa FKDPP / JSR / 35 days / 2022 | chapter-part2 §4.2 | s20 visible + notes «35 дней... JSR в 2022»; s04 notes; s39 notes | ✓ exact |
| Sim-to-real T=300°C / T=315°C / 10% excursion | chapter-part2 §4.4 («через 2 месяца» / «315°C» / «excursion 10%») | s22 «через 60 дней температура расходится до 315°C — excursion на 10%» | ✓ exact (60 дней = 2 месяца, equivalent) |
| Toyota Digit 7+ units RAV4 | chapter-part2 §4.5.1 | s25 «7+ единиц гуманоидов» | ✓ exact |
| PLC code 3-4 дня → 10 мин / 85% точность | chapter-part2 §3.3 | s17 «3–4 дня → 10 минут / 85% точности» | ✓ exact |
| Lighthouse 220+ / 35 стран / 23 новых / 90% / +16% EBIT | chapter-part3 §6.4 | s35 same all 5 + s33 footer «220+ заводов 35 стран» | ✓ exact |
| Pharma FDA ±0.1% vs AI ±0.5% (gap 5×) | chapter-part3 §5.3 | s29 visible matrix + assertion «±0,5% vs ±0,1%» | ✓ exact |

**15/15 numbers match.** Exceptional fidelity на quantitative claims.

# Coverage gaps

**Chapter § → slides coverage:**

| Chapter section | Required slides | Actual slides | Verdict |
|---|---|---|---|
| §0 Вход в шкалу | s02 cover + s03 lecture-map + s04 keystone | ✓ s02 + s03 + s04 (+ hero s01) | ✓ complete |
| §1 DT 2026 (1.1–1.7) | s05 div + s06 Kritzinger + s07 4-layer + s08 market + s09 SE Asian Port + s10 audit | ✓ s05 + s06 + s07 + s08 + s09 + s10 | ✓ complete |
| §2 A0 (2.1–2.5) | s11 div + s12 vision + s13 PdM + s14 limits | ✓ s11 + s12 + s13 + s14 | ✓ complete |
| §3 A1 (3.1–3.6) | s15 div + s16 MES/alarm + s17 PLC Copilot + s18 engineer-in-loop | ✓ s15 + s16 + s17 + s18 | ✓ complete |
| §4 A2 (4.1–4.6) | s19 div + s20 Yokogawa + s21 twin sandbox + s22 sim-real + s23 RL limits | ✓ s19 + s20 + s21 + s22 + s23 | ✓ complete |
| §4.5 A3 (4.5.1–4.5.4) | s24 div + s25 cases+blockers | ✓ s24 + s25 | ✓ complete |
| §5 Где AI НЕ (5.1–5.5) | s26 div + s27 port + s28 matrix + s29 pharma + s30 Gartner + s31 vendor Q | ✓ s26 + s27 + s28 + s29 + s30 + s31 | ✓ complete |
| §6 OT/IT (6.1–6.5) | s32 div + s33 7-layer + s34 protocols + s35 Lighthouse | ✓ s32 + s33 + s34 + s35 | ✓ complete |
| §7 РФ + карьерный мост (7.1–7.5) | s36 div + s37 РФ + s38 career | ✓ s36 + s37 + s38 | ✓ complete |
| §8 Closing | s39 closing hero | ✓ s39 | ✓ complete |

**Coverage: 39/39 slides derive from chapter §; 8/8 chapter sections + roadmap covered.**

**Q&A backup (14 questions):** chapter-part4 §Q1–Q14. Verified — questions remain in chapter as backup (correct pattern — Q&A backup не нужны в slides, available для лектора в Q&A фазе). No drift; no orphan question references in slides.

# Orphan slides (no chapter source)

None. All 39 slides trace back to chapter v3 sections via `<!-- for-slide-sNN -->` markers AND content derivation. Verified comment markers cover s01-s06, s10-s17, s20, s25-s28, s30-s33, s35-s36, s38-s39 (26 markers); remaining slides (s07-s09, s18-s19, s21-s24, s29, s34, s37) derive from explicitly named chapter sub-sections matching slide assertions.

# Orphan references (slides → deleted slide IDs)

**None.** All s01-s39 IDs present in deck.yaml. No slide content references non-existent slides. Cross-references in speaker notes only point to existing IDs (s10, s09, s31).

# Cross-refs / cross-lecture leaks

**Cross-lecture refs (intentional, expected):**
- Lec-11 §2.4 (Tesla 2018) — referenced in s27 + chapter Введение. ✓ in scope (prerequisite explicitly declared in chapter frontmatter).
- Lec-11 §3.2 (FKDPP алгоритмический) — referenced in s20 speaker notes. ✓ in scope.
- Lec-11 §3.5 (Норникель) — referenced in s37 speaker notes. ✓ in scope.
- Lec-11 §5.2 (vendor questions) — referenced in s31. ✓ in scope.
- Lec-11 §5.3 (ISA-95 + ГОСТ) — referenced in s04 + s37. ✓ in scope.
- Lec-7 (FDA HITL) — referenced in s29. ✓ in scope (prerequisite).
- Lec-13 (bridge) — referenced in s39 closing. ✓ canonical phrasing «AI в логистике, цепях поставок и транспорте».

No unauthorized cross-lecture leaks.

# DISCREPANCIES

## D1 — s17 ChatGPT MOV %M99999: «PLC откажется компилировать» factually wrong vs chapter

**Severity:** P0 (factual contradiction on rendered slide)

**Where:** s17 (rendered visible body + speaker notes) vs chapter-part2.md §3.4

**Issue:** s17 rendered slide (визуальный body, см. s-17.png) гласит: «Адрес %M99999 не существует — PLC откажется компилировать». Speaker notes повторяют: «PLC откажется компилировать программу. Это не „иногда галлюцинирует", это структурное ограничение». **Однако chapter §3.4 явно говорит обратное:**

> «На вид — правдоподобно. Команда `MOV` существует в STL (Statement List), таймер `T1` существует, операнд `%M99999` синтаксически валиден. Этот код **скомпилируется** в Siemens TIA Portal без видимых ошибок синтаксического анализатора. **Что не так.** Этот код **не запустится на S7-1500**. Причина — **архитектурная**: в Siemens S7-1500 область памяти M (флаги, Merker) имеет физический размер до адреса **M65535**. Адрес `M99999` — **за пределами адресного пространства**... Адрес вне адресного пространства приводит к остановке PLC в режим STOP — то есть остановке всего оборудования.»

Точка урока chapter — что код **выглядит правильно и компилируется**, поэтому опасен (false confidence); проблема видна только в runtime (STOP mode). Slide инвертирует этот ключевой урок, говоря, что compile-time check спасёт.

**Recommendation:** Fix s17 — заменить «PLC откажется компилировать» на «**Скомпилируется**, но при запуске уйдёт в STOP (M99999 > M65535)» в visible body + правка speaker notes. Это структурно важно: vendor pitch часто говорит «AI генерирует код, который компилируется», и студент должен понять, что **compile ≠ run safely**. Severity P0 because: (а) factual contradiction with chapter source-of-truth, (б) inverts pedagogical message, (в) appears on rendered visible slide (not just notes).

## D2 — LO8 phantom reference in 3 slides (notes)

**Severity:** P1 (significant drift; orphan code referenced in pedagogy)

**Where:** s03 speaker notes + s28 speaker notes + s39 speaker notes

**Issue:** Chapter frontmatter declares `learning_outcomes: [LO2, LO5, LO7]`. **LO8 не существует** для Лекции 12. Однако speaker notes 3 слайдов гласят:
- s03 (lecture-map): «Это центральный payoff лекции для LO7 и LO8»
- s28 (10 criteria matrix): «Десять структурных критериев — payoff лекции для LO7 и LO8»
- s39 (closing): «Десять критериев „AI не нужен" — payoff лекции для LO7 и LO8»

Это, вероятно, copy-paste от другой лекции / черновика с расширенным LO-набором.

**Recommendation:** Удалить «и LO8» из 3 мест, оставить «LO7». Severity P1 — speaker notes, not visible body, но критик в self-study увидит несоответствие с frontmatter declaration.

## D3 — Yokogawa premier minister 2023 award asserted definitively on s20 despite FACT-CHECK in chapter

**Severity:** P1 (unverified factual claim presented as confirmed)

**Where:** s20 speaker notes vs chapter-part2.md §4.2 line 222

**Issue:** s20 speaker notes: «За эту работу команда Yokogawa получила премию премьер-министра Японии в 2023». Это presented как факт **без caveat**. Однако chapter has explicit:

> «Премии и признание. Алгоритм FKDPP был отмечен индустриальными наградами за вклад в промышленный AI [FACT-CHECK: точная награда (Японская премия министерства экономики, торговли и промышленности METI / премия премьер-министра / отраслевая премия) — verify через press release Yokogawa]. Точная атрибуция не критична для дальнейшего изложения...»

Slide делает definitive claim, который chapter explicitly помечает как unverified.

**Recommendation:** Заменить в s20 speaker notes на «За эту работу команда Yokogawa получила индустриальную награду в Японии за вклад в промышленный AI (точная атрибуция — METI или премьер-министра — verify pre-day-of)». Или: удалить упоминание награды вовсе (chapter notes «не критично для изложения»). Severity P1 — лектор может произнести фактически ложное утверждение.

## D4 — Edge AI / Крайний AI terminology drift across artifacts

**Severity:** P2 (minor inconsistency, glossary lock pending)

**Where:** chapter §6.3 vs s33 + s34 + s38 visible body + multiple speaker notes

**Issue:** Chapter canonical (per §6.3 title + русский body): «**Крайний AI**: ИИ на границе сети». Slides используют 3 формы:
- s33 visible body: layer name «**3. Edge AI**» (English-only label на rendered PNG)
- s38 visible body: «**edge AI engineer**» (English term для роли)
- s34 speaker notes: «edge AI inference <10 мс» (mixed)
- s04/s25 speaker notes: «edge AI» (English)
- Chapter-part4 §7.4 (career path): «**Крайний AI engineer** (edge AI engineer)» — gloss-style.

Это не fatal P1 потому что: (а) chapter intro §Введение defines «edge AI (крайний / локальный ИИ-инференс)» как gloss-pair, allowing both surfaces; (б) deck.yaml + slides s33 + chapter §6.3 ALL gloss EN+RU consistently. Но **на rendered s33 visible body LABEL — bare EN «Edge AI»** без RU equivalent. Это потенциальный glossary-lock issue для финализации.

**Recommendation:** Pre-USER-GATE — добавить в `library/lectures/lec-12/glossary.yaml` (если ещё не существует) canonical: «Крайний AI» (RU primary) с aliases_allowed=[«Edge AI», «ИИ на границе сети»]. Для s33 — рассмотреть «3. Крайний AI / Edge AI» в layer label или оставить «Edge AI» (consistent с industry term). Severity P2 — это glossary decision, не factual contradiction.

# Self-checks

- [x] Terminology drift: **1 P2 drift item** (Edge AI surface form on rendered s33 visible body)
- [x] Numbers exact match: **15/15** ✓
- [x] §-coverage holistic: **complete** (все 8 chapter sections + intro + closing + 4 sub-sections of §1, 5 of §2, 6 of §3, 6 of §4, 4 of §4.5, 5 of §5, 5 of §6, 5 of §7 покрыты слайдами или явно остаются в Q&A backup)
- [x] Roadmap alignment: **exact match** (chapter §0.3 → s03 lecture-map 8 sections in same order)
- [x] Bridge to lec-13 canonical: **exact match** «AI в логистике, цепях поставок и транспорте» (locked phrasing per chapter-part4 §8 + s39)
- [x] Orphan slide refs: **none**
- [x] Cross-lecture leaks: **all intentional + within prerequisite scope** (lec-11, lec-07, lec-13)
- [x] Pharma worked example FDA ±0,1% / AI ±0,5%: **exact match** chapter §5.3 ↔ s29
- [x] Toyota Digit 7+ units RAV4: **exact match** chapter-part2 §4.5.1 ↔ s25
- [x] Yokogawa FKDPP 35 days JSR 2022: **exact match** в s04 + s20 + s39
- [x] Visible body grep on rendered PNGs (sampled s04, s06, s08, s09, s10, s12, s13, s14, s17, s20, s22, s23, s25, s28, s29, s33, s37): **no LO codes, no § symbols, no FACT-CHECK markers**; § appears только в slide `.md` source "Visible content" sections (designer description, NOT rendered)

**Verdict: REVISE.** Coverage, structure, numbers, roadmap, keystone phrasing — все excellent (APPROVE-WITH-POLISH level). Но **P0 D1 (s17 compile/run contradiction inverts §3.4 key lesson)** требует fix перед APPROVE. D2 (LO8 phantom), D3 (unverified award), D4 (glossary lock) — добавить в same revision round, поскольку все 4 — quick fixes на стороне slides без затрагивания chapter.

**Recommendation per artifact:**
- **Chapter v3:** no changes (source of truth, internally consistent).
- **Slides v1 → v1.1:** fix D1 (s17 critical), D2 (3× LO8 removal), D3 (s20 award caveat), D4 (glossary lock + s33 label decision).
- **Speech.md:** not yet drafted; ensure speech-writer references corrected slides + chapter, not v1 slides.
