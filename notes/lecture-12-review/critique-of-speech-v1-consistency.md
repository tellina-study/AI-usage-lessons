---
critique_of: chapter v3 ↔ slides v3 ↔ speech v1 (triple alignment)
critic: consistency-checker
verdict: APPROVE-WITH-POLISH
created: 2026-05-22
worktree: /tmp/lec-12-wt
branch: issue-133-lec-12
artifacts_reviewed:
  chapter:
    parts: 4
    total_words: ~31480
    files: [chapter.md, chapter-part2.md, chapter-part3.md, chapter-part4.md, references.md]
  slides:
    deck: deck.yaml
    slide_count: 39
    snapshot_dir: rendered/snapshots/ (39 PNG)
  speech:
    file: speech.md
    words: 6126
    duration_min: 75
severity_counts:
  P0: 0
  P1: 6
  P2: 4
---

# Summary

Triple-artifact consistency check Лекции 12 (chapter v3 multi-part + slides v3 39-slide + speech v1).

**Core verdict: APPROVE-WITH-POLISH.** Major cornerstone concepts (keystone A0→A3, Kritzinger taxonomy, 10 criteria, worked example фарма+FDA, 4 career roles, bridge text к Лекции 13) align structurally across all 3 artifacts. **All locked numbers triple-match** (36→180 млрд / 155 / 17,15 / $12M Port / 35 days Yokogawa / 85% PLC Copilot / 220+ Lighthouse / +16% EBIT / 11% O&G / 14% expectation / 40% Gartner / 99% vision / 100 годных / 10:1 PdM / 57× cement). No P0 contradictions detected. No orphan slide references in speech — все 39 ссылок [sNN] существуют в deck.yaml.

**P1 issues (6):** (1) Карьерная роль 4 — 3 разных названия across artifacts; (2) внутренняя ошибка единицы измерения в chapter-part3 (мкм vs мм vs мм); (3) drift edge AI / крайний AI / AI на границе сети across 3 артефактов; (4) drift safety envelope / защитная зона / безопасная зона across артефактов; (5) timing-marker leaks в s01-hero footer + s02-cover (visible body); (6) phrasing error на s29 slide notes («AI accuracy ±0,5% меньше required tolerance ±0,1%» — числово абсурдно, AI tolerance больше = хуже).

**P2 issues (4):** (1) s03 lecture-map speaker notes contains логическая ошибка («десять критериев из шестого раздела» — на самом деле §5); (2) timing-маркер «15 минут» в s26 speaker notes; (3) engineer-in-loop EN в slides+chapter-part2 vs «человек в петле» в speech (partially intentional, но смешано); (4) Pfizer Vox cross-reference только в chapter, не в speech/slides — acceptable fallback Q&A material, но worth noting.

---

# Cornerstone concepts triple-match table

| Concept | Chapter | Slides | Speech | Verdict |
|---|---|---|---|---|
| **Central question / Big Idea** (на какой ступени автономии AI можно поднять процесс + где двойник обязателен) | §0.1 (chapter.md L113) + Introduction (L93-97) | deck.yaml `central_question:` + s02 cover speaker notes + s04 keystone | speech §0 [s01] L44 + [s04] L54-62 | ✓ aligned |
| **Keystone A0→A1→A2→A3 + двойник как мост** | chapter.md §0.1 table L115-120 («наблюдать/советовать/замыкать петлю/действовать автономно») | s04 keystone slide + s04 speaker notes + dividers s05/s11/s15/s19/s24 | speech §0 [s04] L54-62 («четыре ступени...») + closing [s39] L520-528 | ✓ exact terms identical |
| **Kritzinger taxonomy** (Model / Shadow / Twin) | chapter.md §1.1 L181-189 table + ГОСТ Р 57700.37 L191-195 | s06 speaker notes L14 («Цифровая модель ... Цифровая тень ... Цифровой двойник») | speech §1 [s06] L74-80 («Werner Kritzinger в 2018... Три уровня. Цифровая модель... Цифровая тень... Цифровой двойник») | ✓ identical wording |
| **10 критериев «AI не подходит»** | chapter-part3 §5.2 table L60-70 + §5.2 expanded L86-164 (Критерии 1-10) | s28 slide notes L16-34 (Один-Десять, все 10) | speech §5 [s28] L362-380 (Критерий один, два, пять, шесть, семь, восемь, десять — selected highlights) | ✓ same 10, same alternatives |
| **Worked example фарма+FDA ±0,5%/±0,1%** | chapter-part3 §5.3 L185-217 («допуск FDA — ±0,1 мг... AI ±0,5 мг») | s29 slide notes L16-22 (same numbers, USP <905>, GAMP 5) | speech §5 [s29] L386-400 («Допуск FDA — плюс-минус 0,1 миллиграмма... AI ±0,5 мг») | ✓ aligned (но s29 notes phrasing P1 — см. D6) |
| **4 career roles** | chapter-part4 §7.4 L141-167 (Роль 1-4 с детализацией) | s38 slide notes L16-22 (4 roles) | speech §7 [s38] L500-510 (4 roles) | ✓ structure aligned, but ROLE 4 NAMING DRIFT (см. D1) |
| **Bridge text к Лекции 13** («AI в логистике, цепях поставок и транспорте») | chapter-part4 §8 L210 («locked phrasing») | s39 speaker notes L20 + assertion L5 | speech §8 [s39] L534 + pre-flight L568 | ✓ exact match across 3 artifacts |
| **Roadmap 8 sections** | chapter.md §0.3 L155-167 (§1-§8) | s03 lecture-map speaker notes L14-16 (8 sections) | speech §0 [s03] L52 («Восемь разделов») | ✓ aligned (но s03 speaker notes имеют ошибку §5 vs §6 — см. D8) |
| **Southeast Asian Port $12M / 18 мес / 2024** | chapter.md §1.5 L290-313 | s09 + s27 slides (twin context + §5 intro) | speech [s09] L106-112 + [s27] L350-356 | ✓ identical numbers everywhere |
| **Yokogawa FKDPP / 35 дней / JSR / 2022** | chapter-part2 §4.2 L216-232 | s20 slide notes (alg + arch angle) + s21 (twin sandbox) | speech [s20] L262-274 + [s21] L276-290 | ✓ aligned |
| **ChatGPT MOV %M99999 / S7-1500 / M65535** | chapter-part2 §3.4 L113-156 | s17 slide notes L14 (M65535 + STOP mode) | speech [s17] L208-234 (full reproduction of failure pattern) | ✓ identical canonical example |
| **Sim-to-real T=300°C / T=315°C + поверхностные отложения** | chapter-part2 §4.4 L254-276 | s22 slide notes (T=300 vs T=315) | speech [s22] L292-302 | ✓ aligned |
| **Toyota Digit + BMW Leipzig + 3 блокера A3** | chapter-part2 §4.5 L322-386 | s25 slide notes L14-16 (7+ Digit + 3 blockers) | speech [s25] L324-340 («Toyota Digit... 7+ единиц... BMW Leipzig 2026... 3 блокера») | ✓ aligned |

---

# Numbers triple-match (sample 14)

| # | Locked number | chapter | slide | speech | Aligned? |
|---|---|---|---|---|---|
| 1 | $36,19 млрд → $180,28 млрд (DT market 2025→2030, CAGR 37,87%) | chapter.md L99 + L241 | s08 L5+L14 + deck.yaml L164 | speech L98 | ✓ |
| 2 | $155,04 млрд (AI mfg by 2030, CAGR 35,3%) | chapter.md L99 + L242 | s08 L14 | speech L98 («155 миллиардов») | ✓ |
| 3 | $17,15 млрд (OPC UA+MQTT 2026) | chapter.md L99 + L243 + part3 L294 | s08 L14 + deck.yaml L164 | speech L98 | ✓ |
| 4 | $12M / 18 мес / списан 2024 (Southeast Asian Port) | chapter.md §1.5 + part4 Q3 L226 | s09 L5+L14 + s27 L5+L16 | speech L108 + L352 | ✓ |
| 5 | 75% twin fail (data layer) | chapter.md L265 + L99 + part4 L236 | s09 + s27 + speaker notes | speech L102 («75 процентов проектов цифровых двойников») | ✓ |
| 6 | 11% O&G expected effect / 14% expectation match | chapter.md L282 + part3 L350 | s09 speaker notes (implied via 75% block) | speech L102 («11 процентов... 14 процентов») | ✓ |
| 7 | 40% Gartner agentic AI cancellation 2027 | chapter.md L286 + part3 L166 | s08 speaker + s30 slide | speech L102 + L404 | ✓ |
| 8 | 99% vision QC accuracy + 0,1-2% FP | chapter.md §2.1 L386 | s12 speaker notes | speech L146 («точность 99 процентов и выше, ложные срабатывания от 0,1 до 2 процентов») | ✓ |
| 9 | 100 годных деталей × 10 000 (cascade) | chapter.md §2.2 L415 | s12 speaker notes | speech L152 («10 000 деталей... 100 годных деталей за смену отвергнуто») | ✓ |
| 10 | PdM ROI 10:1 / cement 57× / chemical $2M | chapter.md §2.3 L443-457 | s13 speaker notes (Deloitte stats) | speech L164-168 | ✓ |
| 11 | 35 дней Yokogawa FKDPP в JSR 2022 | chapter-part2 §4.2 L224 | s20 speaker notes L16 + deck.yaml L257 | speech L266 («35 дней... 2022 году... Первый документированный») | ✓ |
| 12 | 85% PLC Copilot accuracy / 3-4 дня → 10 мин | chapter-part2 §3.3 L99-105 | s17 speaker notes L16 | speech L212 («85 процентов... 3-4 дней до десяти минут») | ✓ |
| 13 | 220+ Lighthouse Network в 35 странах + 23 новых 2026 + 90% AI + 16% EBIT | chapter-part3 §6.4 L338-342 | s35 speaker notes L14-16 | speech L466-470 («220+ заводов в 35 странах, 23 новых... 90 процентов... плюс 16 процентов EBIT») | ✓ |
| 14 | ±0,1 мг / ±0,5 мг FDA gap (5×) | chapter-part3 §5.3 L187-200 | s29 speaker notes L18-20 | speech L388-394 («плюс-минус 0,1 миллиграмма... AI ±0,5 мг... разрыв в пять раз») | ✓ |

**14/14 sample numbers triple-match.** No P0 number contradictions.

---

# Terminology drift table

| Term | chapter (форма + count) | slides (форма + count) | speech (форма) | Severity | Recommendation |
|---|---|---|---|---|---|
| **edge AI / крайний AI / ИИ на границе сети** | mixed: «edge AI» × 5 (chapter.md + part2 + part4), «крайний AI» × 10 (mostly part3), «ИИ на границе сети» × 7 | dominantly «edge AI» (s04/s13/s18/s21/s23/s25/s31/s32/s33/s34/s35/s38) | dominantly «AI на границе сети» × 4 + «крайние устройства» (no «edge AI») | **P1** | Choose ONE canonical form. Recommendation: «ИИ на границе сети (edge AI)» first mention, then «ИИ на границе сети» consistently. Avoid mixed within same paragraph. |
| **Career role 4 name** | «Крайний AI engineer» (part4 L163) + «Крайний AI engineer (edge AI engineer)» L314 | «edge AI engineer» (s38 L5 + L22 + deck.yaml L397) | «Инженер по AI на границе сети» (speech L508) | **P1** | 3 distinct names for ONE role. Sync to «Инженер по ИИ на границе сети (edge AI engineer)» canonical. |
| **safety envelope / защитная зона действия / безопасная зона** | «safety envelope» × 5 + «защитная зона» × 15 + «безопасная зона» × 8 | «safety envelope» × 2 (s04 + s25 speaker notes) | «защитная зона» × 1 + «безопасная зона» × 2 (speech) | **P1** | Term used mixed within chapter itself + drift to «safety envelope» EN in slides. Recommend canonical «защитная зона действия (safety envelope)» first use, then «защитная зона» consistently. |
| **engineer-in-loop / инженер в петле / человек в петле** | «engineer-in-loop» × 7 (part2) + «человек в петле» × 6 + «HITL» × 1 | «engineer-in-loop» × 3 (s17 + s18) — никогда не русским | «человек в петле» × 4 (no engineer-in-loop) | **P2** | Partially intentional (engineer-in-loop = специфический PLC Copilot pattern A1; человек в петле = generic). Но differing употребление в slides («engineer-in-loop» EN) vs speech («инженер в петле» RU) — recommend hybrid: «инженер в петле (engineer-in-loop)» first mention в slides. |
| **sim-to-real gap / разрыв «симуляция → реальность»** | «sim-to-real gap» × 3 (part2 + part4) + «разрыв «симуляция → реальность»» × 6 | s22 uses RU form в visible + speaker notes | speech: «разрыв «симуляция → реальность»» × 2 + «разрыв» mentions | **P2** | Acceptable; chapter mixes, speech uses RU only, slide uses RU. Minor drift. |
| **digital twin / цифровой двойник** | dominantly «цифровой двойник» (RU) + «digital twin» EN в quoted source-context | dominantly «цифровой двойник» в visible; «digital twin» в bullets occasionally | exclusively «цифровой двойник» | OK | aligned — RU primary, EN only in technical context |
| **0,001 мм vs 0,001 мкм (жёсткие допуски)** | chapter.md §2.4 L477 + L515 «0,001 мм» ✓; chapter-part3 table L65 «**± 0,001 мкм**» ❌; chapter-part3 §5.2 §Критерий 5 L120 «± 0,001 мм» ✓ | s14 L16 «одной тысячной миллиметра» ✓ + s28 L24 «±0,001 мм» ✓ | speech L178 + L370 «одна тысячная миллиметра» ✓ | **P1** | **Internal chapter inconsistency**: chapter-part3 table row 5 has «мкм» (= 1 nanometer = physically absurd); should be «мм». Fix chapter-part3 L65 «±0,001 мкм» → «±0,001 мм». Only chapter has this typo. |

---

# Orphan refs

**Orphan slide references in speech (grep `[sNN ·`):**

All 39 slide references s01-s39 in speech align to deck.yaml IDs s01-s39. **No orphans detected.** ✓

**Orphan section references (§X.Y):**

| Reference | Source | Target exists? | Verdict |
|---|---|---|---|
| s03 speaker notes: «десять критериев «AI не нужен» из **шестого раздела**» | s03 L18 | 10 criteria are in §5, not §6 | **P2** orphan/error |
| Speech [s29] L384 «Прямая отсылка к Лекции 7» | speech §5 | chapter-part3 L185 also cross-refs Lec-7 | ✓ aligned |
| Multiple «Лекция 11 §X.Y» refs (cross-section: §1.3 GE Predix / §2.1 разметка / §2.4 Tesla / §3.2 FKDPP alg / §3.4 Norsk Hydro / §3.5 Норникель / §5.3 ISA-95 + ГОСТ Р) | chapter all parts + speech §0/§5/§7 + slides s04/s20/s21/s27/s37 | All references consistent within Lec-12 (assume Lec-11 sections exist as referenced) | ✓ aligned across artifacts |
| «Лекция 13 — «AI в логистике, цепях поставок и транспорте»» | chapter-part4 §8 + s39 + speech §8 | All 3 identical locked phrasing | ✓ |
| Pfizer Vox cross-ref «см. Лекцию 11 Q&A Q12» | chapter-part4 Q5 L255 | Mentioned only in chapter, not in speech or slides | OK (Q&A backup material) |

**No orphan references to deleted slides** (deck.yaml v3 = 39 slides, all referenced).

---

# Internal-to-slide inconsistencies (NEW, identified during cross-check)

These are NOT cross-artifact drifts but **slide-internal logical/data errors** found during the consistency pass:

- **s03-lecture-map.md L18 (speaker notes):** «Применимый инструмент для кармана — десять критериев «AI не нужен» **из шестого раздела**.» — 10 criteria are in **§5**, not §6 (chapter §5, slide divider s26 «Раздел 5», speech §5). **P2**.
- **s29-pharma-fda-example.md L20:** «AI accuracy ±0,5% **меньше** required tolerance ±0,1%» — number-wise impossible (0,5 > 0,1); inverse phrasing. Should read «AI accuracy ±0,5% **превышает** required tolerance ±0,1%» or «**отстаёт от**». Chapter and speech correctly say «разрыв в 5 раз не в пользу AI». **P1**.
- **s26-section5-divider.md L14 (speaker notes):** «Densest failure bucket лекции — **15 минут**.» — timing marker in speaker notes, violates CLAUDE.md «No Timing / No Methodology in Slides» rule. **P2**.

---

# Visible-body / speaker-notes timing leaks (CLAUDE.md No Timing rule)

| Slide | Location | Content | Severity |
|---|---|---|---|
| s01-hero-hannover-messe.md | L25 (visible footer) | «Лекция 12 · **75 минут** + Q&A · Курс „Применение AI в инженерии"» | **P1** visible body timing marker |
| s02-cover.md | L11 (visible) + L18 (speaker notes) | «Модуль 2 · **75 минут** + Q&A» + «Сегодня мы посвятим **75 минут** трём вопросам» | **P1** visible body + notes |
| s26-section5-divider.md | L14 (speaker notes) | «Densest failure bucket лекции — **15 минут**» | **P2** notes only |
| Various slides | speaker_notes | no other timing leaks detected | OK |

**Recommendation:** strip «75 минут» from s01 footer and s02 visible/notes. Speech §0 already covers duration; deck.yaml + frontmatter is correct location for timing.

---

# DISCREPANCIES

### D1 — Career role 4 has 3 different names across 3 artifacts
**Severity:** P1
**Where:** chapter-part4 §7.4 L163 vs slide s38 L22 vs speech §7.4 L508
**Issue:**
- chapter: «**Крайний AI engineer**» (RU+EN hybrid)
- slide s38: «**edge AI engineer**» (pure EN)
- speech: «**Инженер по AI на границе сети**» (pure RU)
**Recommendation:** Lock canonical form across all 3. Suggested: «**Инженер по ИИ на границе сети (edge AI engineer)**» on first mention in each artifact, then short form «**инженер по ИИ на границе сети**».

### D2 — edge AI / крайний AI / ИИ на границе сети drift (system-wide)
**Severity:** P1
**Where:** all artifacts — see Terminology drift table
**Issue:** Three forms used inconsistently. Chapter mixes (5 «edge AI» + 10 «крайний AI» + 7 «ИИ на границе сети»). Slides dominantly EN. Speech exclusively RU.
**Recommendation:** Sync to «**ИИ на границе сети (edge AI)**» on first mention in each artifact, then «**ИИ на границе сети**» everywhere. Remove «крайний AI» form entirely (lexically unfortunate in Russian).

### D3 — chapter-part3 §5.2 row 5 unit error (мкм vs мм)
**Severity:** P1
**Where:** chapter-part3 L65 (table row 5)
**Issue:** Table cell reads «Жёсткие допуски **± 0,001 мкм**» (= 1 nanometer = physically absurd). Everywhere else (chapter.md §2.4 L477, chapter-part3 L120, slide s14, slide s28, speech) consistently uses «**± 0,001 мм**» (= 1 micrometer, physically correct).
**Recommendation:** Fix chapter-part3 L65: replace «± 0,001 мкм» → «± 0,001 мм». Single-character typo, but P1 because it propagates from canonical source.

### D4 — safety envelope / защитная зона drift
**Severity:** P1
**Where:** chapter mixes (×5 EN + ×15 RU + ×8 «безопасная зона»); slides dominantly EN (s04 + s25); speech dominantly RU
**Issue:** Three forms — «safety envelope», «защитная зона действия», «безопасная зона» — used interchangeably without consistent canonical choice.
**Recommendation:** Sync to «**защитная зона действия (safety envelope)**» on first mention, then «**защитная зона**» short form. Avoid «безопасная зона» (less specific).

### D5 — s29 phrasing error «AI accuracy ±0,5% меньше required tolerance ±0,1%»
**Severity:** P1
**Where:** slide s29-pharma-fda-example.md L20
**Issue:** Wording inverse: 0,5% is numerically LARGER (worse) than 0,1%, not «меньше». Reader sees «AI меньше требований» → impression that AI is more strict, opposite of correct meaning. Chapter and speech correctly say «разрыв в 5 раз не в пользу AI».
**Recommendation:** Rewrite s29 L20: «AI accuracy ±0,5% **в 5 раз шире (хуже)** required tolerance ±0,1% — несовместимо.»

### D6 — s01-hero footer + s02 cover have «75 минут» visible (timing leak)
**Severity:** P1
**Where:** s01 L25 (visible footer), s02 L11 (visible), s02 L18 (speaker notes)
**Issue:** Violates CLAUDE.md fundamental rule «No Timing / No Methodology in Slides» — visible body слайдов не должны содержать timing markers. Timing — только frontmatter / deck.yaml / iteration-log / plan files.
**Recommendation:** Strip «75 минут» from s01 footer and s02 visible/notes. Replace with: «Курс „Применение AI в инженерии" · Лекция 12».

### D7 — Role 4 specifically + engineer-in-loop EN-only in slides
**Severity:** P2
**Where:** slides s17 + s18 use «engineer-in-loop» (EN); speech uses «человек в петле» / «инженер в петле» (RU). Chapter mixes.
**Issue:** Slides have anglicism «engineer-in-loop» without RU gloss; CLAUDE.md Russification rule recommends RU primary + EN gloss on first use.
**Recommendation:** Slides s17 + s18: replace «engineer-in-loop» with «**инженер в петле (engineer-in-loop)**» on first mention, then «инженер в петле».

### D8 — s03 speaker notes logical error: «10 критериев из шестого раздела»
**Severity:** P2
**Where:** slide s03-lecture-map.md L18 speaker notes
**Issue:** «Применимый инструмент для кармана — десять критериев «AI не нужен» из **шестого раздела**.» — 10 criteria are in §5 (chapter §5.2, slide divider s26 «Раздел 5», speech §5). §6 is OT/IT architecture.
**Recommendation:** Fix s03 L18: replace «из шестого раздела» → «из пятого раздела».

### D9 — s26 speaker notes timing leak «15 минут»
**Severity:** P2
**Where:** slide s26-section5-divider.md L14
**Issue:** «Densest failure bucket лекции — **15 минут**.» — timing marker in speaker notes, violates No Timing rule.
**Recommendation:** Remove «— 15 минут». Replace with: «Densest failure bucket лекции».

### D10 — Pfizer Vox cross-reference only in chapter, not speech/slides
**Severity:** P2 (acceptable but worth noting)
**Where:** chapter-part3 L213 + chapter-part4 Q5 L255 reference Pfizer Vox; speech and slides s29/s38 don't mention
**Issue:** Acceptable as Q&A backup material (chapter Q&A backup section), but if lecturer brings up Pfizer Vox in real Q&A, slides won't have backing visual. **All Pfizer mentions in chapter have [FACT-CHECK] markers** — uncertain attribution.
**Recommendation:** Acceptable as-is for v1; no action needed unless lecturer wants Pfizer Vox in main narrative.

---

# Coverage gaps

**Concept-level coverage gaps (chapter→slides→speech):** None detected. All 8 chapter sections have corresponding section dividers + content slides. All canonical examples (Southeast Asian Port, Yokogawa FKDPP, ChatGPT MOV %M99999, T=300/315°C, фарма ±0,5%/±0,1%, Toyota Digit, 4 career roles) present in all 3 artifacts.

**Concepts in chapter but lighter in speech/slides:** acceptable trimming
- §0.2 «6 аббревиатур» (chapter L140-151) — speech mentions OPC UA/MES/SCADA/PLC/MPC/RL in passing; slides don't have a dedicated glossary slide. Acceptable; speaker can rely on Q&A backup.
- §1.3 detailed sector breakdown (chapter L246-256) — speech and slides give only aggregate market numbers. Acceptable trimming.
- §1.6 data layer audit governance owner cost (chapter L335-340) — speech mentions $20K-50K aggregate, slides don't show. Acceptable.
- §3.5 engineer-in-loop 4 этапа detailed — chapter has 4 этапа detailed; speech [s18] L238-248 covers all 4; slide s18 covers 5 stages (slight inflation but consistent). OK.

**Concepts in speech/slides but NOT in chapter:** None detected. All speech assertions backed by chapter content.

---

# Self-checks

- [x] Bridge text exact match: chapter-part4 L210 + s39 L20 + speech L534 → all three say «**AI в логистике, цепях поставок и транспорте**» verbatim.
- [x] Roadmap 8-section align: chapter §0.3 L155-167 + s03 L14-16 + speech [s03] L52 → 8 sections, same order, same labels (s03 speaker notes has §5/§6 swap error — see D8, but section count + order correct).
- [x] Cross-refs to lec-11 / lec-07 consistent: lec-11 §1.3 (GE Predix), §2.1 (разметка), §2.4 (Tesla), §3.2 (FKDPP alg), §3.4 (Norsk Hydro), §3.5 (Норникель), §5.3 (ISA-95 + ГОСТ Р) — all 7 cross-refs present in chapter + slides (where relevant) + speech (where relevant). lec-07 cross-ref (FDA/HITL) present in chapter-part3 §5.3 L185 + L211 and speech [s29] L384.
- [x] No orphan slide refs in speech: speech references s01-s39, all 39 IDs exist in deck.yaml. ✓
- [x] Keystone A0→A3 + двойник как мост presented identically across artifacts. ✓
- [x] All 14 sampled locked numbers triple-match. ✓
- [x] Kritzinger 3-level taxonomy identical (Digital Model / Digital Shadow / Digital Twin) in chapter §1.1 + s06 + speech [s06]. ✓
- [x] ГОСТ Р 57700.37-2021 quoted formulation identical (cross-reference §7 ↔ §1.1 within chapter; speech reproduces; slide s06 mentions). ✓
- [x] 10 criteria — same 10 entries, same alternatives, in chapter §5.2 + s28 + speech [s28]. ✓
- [x] Worked example фарма ±0,1 мг allowed vs ±0,5 мг AI accuracy — same numbers across all 3 artifacts. ✓
- [x] 4 career roles structurally aligned (AI/ML + DT engineer + MES integration + edge AI) — but Role 4 NAMING DRIFTS — see D1.
- [x] No P0 factual contradictions detected.

---

# Топ-N фиксов (per artifact)

**Chapter (chapter-part3.md):**
1. **L65 (D3):** Fix unit «±0,001 **мкм**» → «±0,001 **мм**». Single-character typo.
2. (Optional) Decide canonical form: «защитная зона действия (safety envelope)» first mention + RU short form thereafter. Sweep through all parts.
3. (Optional) Decide canonical form «ИИ на границе сети (edge AI)»; sweep edges of «крайний AI» × 10 (mostly chapter-part3).

**Slides:**
1. **s29 L20 (D5):** Fix phrasing «AI accuracy ±0,5% **меньше** required tolerance ±0,1%» → «AI accuracy ±0,5% **в 5 раз шире (хуже)** required tolerance ±0,1%».
2. **s01 L25 (D6):** Remove «75 минут» from visible footer.
3. **s02 L11 + L18 (D6):** Remove «75 минут» from visible + speaker notes.
4. **s03 L18 (D8):** Fix «из шестого раздела» → «из пятого раздела» (10 criteria are in §5).
5. **s26 L14 (D9):** Remove «— 15 минут» timing marker from speaker notes.
6. **s38 L5 + L22 + deck.yaml L397 (D1):** Replace «edge AI engineer» → «инженер по ИИ на границе сети (edge AI engineer)» canonical form.
7. **s17 + s18 (D7):** Replace bare «engineer-in-loop» with «инженер в петле (engineer-in-loop)» on first mention.

**Speech:**
1. **L508 (D1):** Already uses RU «Инженер по AI на границе сети» — closest to recommended canonical; consider adding «(edge AI engineer)» gloss for parallel with chapter+slide.
2. Otherwise speech is the most consistent of 3 artifacts. No P1 fixes required.

---

# Метрики consistency

| Метрика | Значение | Verdict |
|---|---|---|
| Cornerstone concepts triple-matched | 13/13 | APPROVE |
| Locked numbers triple-matched | 14/14 | APPROVE |
| Orphan slide refs in speech | 0 / 39 | APPROVE |
| Orphan section refs (cross-artifact) | 0 | APPROVE |
| Bridge text exact match (Lec-13) | ✓ all 3 | APPROVE |
| Roadmap 8 sections aligned | ✓ (but s03 speaker notes typo §5→§6) | POLISH |
| Terminology drift detected | 4 terms (edge AI / safety envelope / role 4 / engineer-in-loop) | POLISH |
| Visible-body timing leaks | 2 (s01 footer + s02 cover) | POLISH |
| Internal slide errors (logic/data) | 3 (s03 notes §5/§6 swap; s29 phrasing inverse; s26 timing in notes) | POLISH |
| chapter-internal unit error | 1 (мкм vs мм в chapter-part3 table) | POLISH |

---

**Конечный verdict: APPROVE-WITH-POLISH.**

Триадная согласованность по cornerstone concepts и locked numbers — **отличная**. Все 39 slide-ссылок в speech существуют. Все bridge texts triple-match. P0 factual contradictions нет.

P1 issues (6) — это **косметика плюс одно структурное** (chapter-part3 unit мкм vs мм + slide s29 phrasing inverse + Role 4 naming drift + timing leaks на cover/hero). Все исправимы быстрыми точечными правками (≤15 минут total).

P2 issues (4) — minor polish (s03 §5/§6 swap + s26 timing in notes + engineer-in-loop EN drift + Pfizer cross-ref scope).

Рекомендация orchestrator'у: apply D1-D6 fixes (P1) before USER GATE C; D7-D10 (P2) — optional polish or carry into post-gate iteration.
