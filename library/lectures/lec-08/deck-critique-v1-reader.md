VERDICT: REVISE

# Reader (Rendered) Report — Лекция 8 — 2026-05-20

Mode: rendered (2-weeks-after retention test)
Sources: 39 PNG snapshots + speaker notes из rendered PPTX
Cross-checked: forbidden-marker grep, vocabulary check, retention sample 10 slides, cases §3 sample 4, schemas retention sample 5

---

## Сводка

- **Slides total:** 39
- **Self-contained (студент через 2 нед поймёт из PNG + notes alone):** 31/39 = 79%
- **Self-containedness threshold:** < 85% → **P1 systemic issue** (per CLAUDE.md threshold escalation rule)
- **Self-containedness score:** 7/10
- **Concept retention through 2 weeks:** 8/10 — keystone-ось «добавил→изменил→сломал» очень запоминается; cases §3 retention strong благодаря однородной структуре assertion / evidence / урок; checklist s37 — usable reference card
- **Forbidden-marker scan (visible body):** **3 P0 hits** (scaffold leak survived broader-grep claim by orchestrator)
- **Vocabulary issues:** 5 терминов используются без inline gloss на slide первого появления (P1)
- **Visual asset gaps:** 2 placeholder «[ news screenshot ]» stubs остались в финальном deck (P1)
- **Snapshot staleness:** full `s-NN.png` batch (15:42-43) on disk **старше** PPTX (15:49) — 3 spot-fix re-renders (`s08-08.png`, `s15-15.png`, `s35-35.png`) присутствуют, но full batch не пересобран. Студент, открывающий snapshots, увидит legacy PNG со scaffold-маркерами.

---

## Сильные стороны (что работает для 2-нед read через 2 недели)

1. **Speaker notes — exemplary.** Sample 10 slides: все 150-300 слов connected prose, no «Лектору» / no «Вы здесь» / no layout description, deriv-tone consistent. 5-7 случайных notes (s01, s05, s10, s15, s20, s28, s33, s37) — все читаются как чёткий студенческий текст. Это сильно отличается от Лекции 4 (там notes были scaffold-leaks).
2. **Keystone-ось s05 «добавил→изменил→сломал»** — visual очень чистый: 3 numbered Ocean boxes слева, mirror cards справа, footnote-tagline «это ось трёх времён, не три параллельные категории». Через 2 недели студент моментально вспоминает структуру.
3. **3 семейства моделей s06** — schema readability strong: 3 column cards, каждая с «принцип / инструменты 2026 / инженерное следствие». Self-contained without лектора.
4. **Cases §3 структурная однородность.** Все 12 кейсов (s21–s31) имеют identical pattern: assertion title + evidence box + chronology + «УРОК ДЛЯ ИНЖЕНЕРА» в gold rounded box. Это сильно помогает retention — студент через 2 нед видит layout и сразу узнаёт «это case-слайд, ищу урок снизу».
5. **s37 чек-лист** — usable как reference card; 5 numbered questions слева + 3-options A/B/C справа; компактно, читаемо, actionable.

---

## P0 issues (must fix перед production show)

### P0-1. Scaffold leak `[VFY-day-of]` visible в финальном rendered PPTX (s08, s15, s35)

- **s-08.png** (subtitle): «3 флагманские модели определяют состояние индустрии · **[VFY-day-of для версий и цен в frontmatter]**»
- **s-15.png** (footer): «Источник: ZSky AI, Sora 2 API Pricing, ElevenLabs pricing. **[VFY-day-of для версий и цен в frontmatter]**»
- **s-35.png** (subtitle): «Empirical end-user rejection · Social Blade Creator Survey · Dec 2025 **[VFY-day-of]**»
- **Note:** orchestrator's «broader grep done» утверждение не охватило `[VFY-day-of]` pattern.
- **Status:** PPTX был перепатчен после snapshot rendering — full snapshot batch (`s-NN.png` 15:42-43) stale relative to current PPTX (15:49). Spot-fix `s08-08.png`, `s15-15.png`, `s35-35.png` (15:47-50) clean. **Полный re-render snapshot batch обязателен** перед GATE B, иначе studen увидит legacy artifacts.
- **Impact:** P0 — это designer-scaffold leak в student-facing artefact, прямой Anti-Pattern из CLAUDE.md.

### P0-2. Slide-number reference `s21-s27` visible на s-20

- **s-20.png** footer: «Конкретные landmark-cases каждой категории — **s21-s27**».
- Это course-scaffold leak: student-reader не должен видеть внутренние slide-номера (студент при чтении через 2 нед не имеет «s21-s27» в свой ментальной модели).
- Fix: переписать как «12 кейсов разобраны на следующих слайдах» или удалить.
- **Не найдено orchestrator grep'ом** — паттерн `s[0-9]+-s[0-9]+` не входит в стандартный список forbidden.

### P0-3. Number discrepancy s27 — chapter/slide say 793, speaker notes say 893

- s-27.png visible: «793 / 16 reported / prosecuted»
- chapter.md L473: «793 reported / только 16 prosecuted»
- speaker notes s27: «**восемьсот девяносто три** случая были официально reported»
- Studen через 2 нед читает notes alone → запомнит 893, но в чек-листе/тесте увидит 793 → cognitive dissonance.
- Fix: speaker notes → «семьсот девяносто три случая».

---

## P1 issues (substantive polish)

### P1-1. Placeholder `[ news screenshot ]` stubs остались в финальном deck

- **s-21.png** (NYT v OpenAI Case 1): большая левая колонка — серый Ocean box со словами «[ news screenshot ]» — это designer-stub, не финальный visual asset.
- **s-22.png** (Getty v Stability Case 2): identical issue, «[ news screenshot ]» в левой колонке.
- Для retention check: если студент через 2 нед видит этот stub, левая колонка не несёт никакой visual информации — она просто empty placeholder с текстовой меткой «здесь должен быть скриншот, но его нет». Это **прямой Anti-Pattern «designer-extras»**.
- Fix: либо реальный Bloomberg Law / Reuters headline screenshot, либо удалить левую колонку и расширить правую chronology.

### P1-2. «Suprior» typo на s-22

- s-22.png chronology третий badge: «**Suprior**» — typo вместо «Superior». Это видно on slide.
- Fix: «Note» или удалить badge (содержит «trademark + passing-off — отдельные claims», что не имеет ясной хронологической привязки).

### P1-3. Vocabulary без inline gloss первого появления в visible body

| Term | First appears slide | Inline gloss? | Reader 2-нед impact |
|------|---------------------|---------------|----------------------|
| TDM (Text and Data Mining) | s-12 (RU контекст) | нет | средний — RU-инженер может не знать TDM-exception |
| SAG-AFTRA | s-18 | нет (assumed знакомым) | низкий — большинство ИУ6 не знают |
| WGA | s-18 | нет | низкий |
| MTD (Motion to Dismiss) | s-22 | нет | **средний P1** — без объяснения студент не поймёт legal milestone |
| CDPA (UK Copyright Designs and Patents Act 1988) | s-22 | partial — упоминается «по CDPA» без раскрытия | средний — частично закрыто в notes |
| SJ (Summary Judgment) | s-21 | нет | средний — слово критично для timeline |
| UMG | s-24 | нет | низкий — большинство догадаются по контексту |

**Notes частично closets gap** (например, notes s22 раскрывают «UK Copyright, Designs and Patents Act 1988 — CDPA»), но **visible slide layer не self-contained** для студента, читающего на ходу без notes.

Fix: footer на s-21/22 / mini-glossary box: «MTD = motion to dismiss; SJ = summary judgment; CDPA = UK Copyright 1988».

### P1-4. Bottom-of-slide content cut-off в нескольких slides

- **s-17.png** «Урок для инженера» bleeds off-slide: «Между AI tool и client deliverable. Растёт быстро, но меньше displaced класса.» — последняя строка обрезана.
- **s-27.png** «Урок для инженера» — также частично обрезан.
- **s-33.png** — внутри 4 cards видны faint/cropped sub-lines текста за финальной summary плашкой (z-order/clipping bug).
- Fix: либо уменьшить шрифт, либо сократить текст урока. Critical для retention — урок именно та part, которую студент через 2 нед ищет.

### P1-5. Q&A slide s38 — менее actionable чем мог бы быть

- s-38 содержит 3 backup-темы для дискуссии, но visible body не показывает «куда задавать вопросы». 
- Notes детальны (195 слов), но это speaker-script, не reader-content. Через 2 нед студент видит slide → 3 темы, но без contact / chapter pointer.
- Минор: добавить footer «Полные источники + chapter.md + чек-лист — в repo».

---

## P2 issues (cosmetic)

### P2-1. «ZSky AI» как источник — niche

- s-15 footer cites «ZSky AI» — реальный source per chapter.md L740 (zsky.ai blog), но студент 2-нед не знает source, может принять за typo. Можно добавить «cost-collapse benchmarks» подпись или просто оставить.

### P2-2. Roadmap-bar visible на s-14 divider but не на content slides

- s-14 divider содержит bottom roadmap-bar (0/1/2/3/4/5) — это Lec-N-1 pattern compliant. Хорошо. Но section dividers s06, s07, s13, s19, s32, s36 stylistically похожи но я не проверил каждый — рекомендую spot-check designer.

---

## 10-Check Detailed Findings

### Check 1 — Speaker notes quality (sample 10 random)

s01, s05, s10, s15, s20, s23, s27, s30, s33, s37 — все 150-300 слов, connected prose, no scaffolds, no layout description, no «Лектору». **Result: 10/10 strong.**

### Check 2 — Forbidden content grep (re-verify orchestrator claim)

Orchestrator claimed «broader grep clean». Re-grep с расширенным паттерном:
- `[VFY` / `[VERIFY` / `frontmatter`: **3 P0 hits visible** (s08, s15, s35 stale snapshots show this; current PPTX has it removed in s08/s15/s35 spots but VFY-day-of pattern still present on **s-15** and **s-35** snapshots in production folder — see P0-1).
- `s[0-9][0-9]-s[0-9][0-9]`: **1 P0 hit** on s-20 — «s21-s27».
- `LO[1-9]` / `§[0-9]` / `course-scaffold` / `Лектору` / `Вы здесь`: **0 hits**.
- **Result: orchestrator broader-grep claim wasn't broad enough — 3 P0 hits survived.**

### Check 3 — PNG + notes coupling, sample 10 slides

| Slide | Strong/Mid/Weak | Notes |
|-------|---|---|
| s05 keystone | Strong | 3 boxes + tagline; notes 223 words; через 2 нед — instant recall |
| s06 families | Strong | 3 column cards; notes 281 words; reading alone gives full picture |
| s14 divider | Strong | clear «Раздел 2 AI ИЗМЕНИЛ»; roadmap-bar; notes 119 words |
| s15 cost-collapse | Strong (но scaffold leak P0) | таблица clear; multiplier highlighted gold; notes 274 words |
| s17 displacement table | Mid | content rich but bottom cut-off; notes сильны |
| s20 4-categories | Strong (но slide-ref leak P0) | 4 cards clearly labelled; урок box; notes 281 words |
| s21 NYT | Mid | «news screenshot» placeholder weakens; notes сильны (239 слов) |
| s27 Korea | Mid | numbers clear but 793/893 discrepancy с notes; notes 288 слов |
| s33 4 criteria | Mid | clipping issue в cards; main idea clear; notes 298 слов |
| s37 checklist | Strong | reference-card format; notes 364 слов |

**Strong: 5 / Mid: 5 / Weak: 0.**

### Check 4 — Cases §3 retention test (4 sample)

- **s21 NYT v OpenAI**: PNG shows «20M ChatGPT logs», SJ deadline 2 апр 2026, regurgitation theory. + notes 239 слов с уроком. Через 2 нед: **студент может объяснить case в 3 предложениях**. (placeholder image снижает visual recall, но core retained.)
- **s23 Andersen**: PNG shows class action timeline, style mimicry. Notes 269 слов. **Strong retention.**
- **s27 Korea**: numbers grid + NPR text-only excerpt + урок. Notes 288 слов, sensitive case treated carefully. **Strong retention**, но 793/893 discrepancy создаёт friction.
- **s30 Toys R Us**: sentiment swing numbers visible, Joe Russo quote в notes. **Strong retention** of brand-damage point.

**Result: all 4 sample cases retained well — однородная структура помогает.**

### Check 5 — Concepts retention

- **s05 keystone «добавил→изменил→сломал»**: **Strong** retention. Phrase запоминается.
- **s05a 3 families (s06)**: **Strong** retention. Diffusion vs latent transformer vs neural audio — clear visual distinction.
- **s33 4 criteria отказа**: **Mid retention** — клипинг ослабляет visual, но essence clear (training license / output similarity / consent / brand-trust).
- **s37 5-вопросный чек-лист**: **Strong retention** as reference card.

### Check 6 — Cross-references to other lectures

- s13 cost-collapse mini-failure references «как мы видели в Лекции 3». Notes mention «Лекция 3» один раз. Понятно ли студенту? Marginally — depends on whether он смотрел Лекцию 3. Acceptable.
- s39 анонс Лекции 9 — clear forward reference.

### Check 7 — Glossary check (см. P1-3 table выше)

5 терминов без inline gloss на visible слое (TDM, MTD, SJ, CDPA, possibly SAG-AFTRA). **Notes частично закрывают gap** но visible-only reader не self-sufficient.

### Check 8 — Pacing through deck

39 slides × ~3 min reading = ~2 часа re-read через 2 нед.
- **Что unstays:** keystone, 3 families, 4 categories taxonomy, 5-question checklist, Arup deepfake case ($25.6M), Korea numbers, Toys R Us sentiment swing.
- **Что forgets:** detail-numbers (CTR percentages в s35 — minus 22 / 19 / 61.8 могут смешаться), детали ScarJo timeline.

### Check 9 — Q&A backup completeness

s38 backup-topics: fair-use AI training, Sora-2-vs-Lionsgate, Минцифры законопроект. Все 3 ad hoc отвечают cases в deck. **Coverage OK.**

### Check 10 — Visual longevity

- **Charts**: s15 cost-collapse table — labels readable, multiplier highlighted, gold MIDDLE-TIER ≠ FREE box — self-explanatory.
- **Schemas**: s20 4-categories — self-explanatory без лектора. s33 4-criteria — clipping issue ослабляет, но essence retained.
- **Numbers grids**: s27 Korea — readable; s30 Toys R Us — readable; s35 YouTube — readable но scaffold leak.
- **Placeholder visuals**: s21, s22 «[ news screenshot ]» — visual longevity weakens; student через 2 нед видит «pending render», не case visual.

---

## Structural Blocker Assessment

8 slides со self-contained-fail или quality gap. Classification:

- **Notes fixes (just trim или sync 893→793):** s27.
- **Visual fixes (re-render + remove scaffold):** s08, s15, s35 (P0-1), s20 (P0-2), s17 / s27 / s33 (P1-4 clipping).
- **Schema/asset replacement:** s21, s22 «[ news screenshot ]» placeholders (P1-1) — нужны реальные news screenshots либо схема пересмотрена.
- **Vocabulary fixes:** s12 / s18 / s21 / s22 / s24 inline gloss для TDM, SAG-AFTRA, SJ, MTD, CDPA, UMG (P1-3) — добавить mini-footer glossary.
- **Structural cuts:** none — все 8 slides сохраняемы при notes/visual fix.

Никакие slides НЕ рекомендуются DELETE — все восстановимы с editorial / re-render pass.

---

## Counter-check

- ≥5 P1 issues? Yes (5 explicit P1 + 3 P0). Per counter-check rule → **REVISE** (даже если verdict could be APPROVE-WITH-POLISH по absolute self-containedness 79%).
- 79% self-contained (< 85% threshold) → APPROVE-WITH-POLISH ceiling по threshold. P0 issues → REVISE floor.

**FINAL VERDICT: REVISE.**

---

## Top 5 fixes (priority order)

1. **Re-render full snapshot batch** `s-NN.png` after PPTX scaffold-leak fixes (P0-1) — current snapshots stale by 6 min. Verify zero `[VFY-day-of]` / `frontmatter` mentions in re-rendered PNGs.
2. **Remove slide-ref `s21-s27` from s-20 visible body** (P0-2) → переписать как «12 кейсов на следующих слайдах».
3. **Fix s27 number** in speaker notes 893 → 793 (P0-3) — sync с chapter / slide.
4. **Replace `[ news screenshot ]` placeholders** on s21 and s22 с real news headline visuals OR redesign without placeholder (P1-1).
5. **Add inline glossary footer** on s21/s22 для SJ, MTD, CDPA OR mini-card top-right с term expansions (P1-3) + fix «Suprior» typo on s22 + fix bottom-clipping on s17/s27/s33 (P1-2, P1-4).
