# Presentation Critic Report — Лекция 15 «AI в научных исследованиях» — slides v1 — 2026-05-27

VERDICT: **REVISE**

## Severity counts

- **P0 (blocking):** 4
- **P1 (should-fix):** 18
- **P2 (polish):** 9

## Executive summary

Содержательно deck сильный: keystone «лестница цикла» (s03) cyclical
работает; canonical numbers integrity 8/8 PASS; Russian-language failure
deep-dives (Sakana s10, Palgrave s17, NeurIPS s30, Frontiers s29)
методически выстроены; walked examples s07/s25/s28/s34 пятиступенчатые;
рамки s33/s35/s36 хороши; ICMJE matrix s31 — образцовая.

**Но v1 имеет четыре структурных проблемы, блокирующих USER GATE B:**

1. **Top progress bar c английскими лейблами + LO codes + «75 минут» в
   visible body на cover/dividers** — прямое нарушение «No Timing /
   Methodology in Slides» (CLAUDE.md ENFORCED, фундаментальное правило)
   + Lec-N-1 pattern deviation (Lec-13/14 не имеют top progress bar
   нигде).
2. **Footers с methodology meta-comments на 4 dividers** («самый
   сильный раздел лекции», «самые предсказуемые применения», «самый
   острый раздел этики», «Самая важная часть лекции — про осознанный
   отказ от AI») + «Что произошло (методологически):» на s29 — прямое
   нарушение «No Timing / Methodology» правила.
3. **Массовый Russification leak**: ~140 narrative-body
   non-whitelist Latin tokens; критические — step labels
   «Hypothesis/Design/Experiment/Analyse/Write/Review» на s03+dividers
   (даже когда есть russian gloss мелким курсивом, английский
   доминирует); «Data overlap / Label availability / GPU cost / AUC
   baseline / Held-out validation» на s25 WE-TESS; «HITL design /
   Pre-publication verify» на s36; «Timeline:», «applicable artefact»,
   «academic adoption», «cherry-pick», «Acceptance rate», «augmented»,
   «light curves», «open-source», «multi-agent debate», «editorial».
4. **Section divider tag-strip overflow**: s12 has 6 tags (only 3
   render visible); s20/s26/s32 have 5 tags (4 visible, 5th cut). Plus
   «VFY-day-of» visible в body на s09 — designer-extras scaffold leak.

Дополнительно — **chart legend bug** «undefined» на s27 + s30 (persist
из iter-1 несмотря на iter-3 claim «fixed»). Overflow «CELLLS» поверх
timeline box на s29 (third anatomy term cut into next box).

Hero check: s01 acceptable substitute (Nobel + text-card Galactica per
iter-2 fix); s39 — composite weak (mostly AlphaFold ribbon repeat from
s14), not real DB screenshot. Designer log honest about Tier 1-6
failures.

Canonical numbers integrity: 8/8 PASS (A-Lab 41/58 ✓, Palgrave 35/36
✓, Nobel 9 окт 2024 ✓, NeurIPS 21 575/5 290/24,52% ✓, GNoME 6 раундов
✓, AlphaProof P1/P2/P6 solved + P3/P5 unsolved ✓, Recursion-Roche
дек 2021 / 40 / $300M / $12B ✓, Указ 490 + 124 ✓).

**Counter-check:** 4 P0 + 18 P1 ≫ 5 P1 threshold → REVISE confirmed.

---

## P0 findings (blocking — must fix до USER GATE B)

### P0-1. Top progress bar c English labels + LO codes + «75 минут» на cover/dividers (s02 + s06 + s12 + s20 + s26 + s32 + s38?)

**Issue:** На cover s02 (visible body): «Модуль 3 · 75 минут» + «LO4 / LO5 /
LO6 / LO8» — прямое нарушение CLAUDE.md «No Timing in Slides» правила
(timing в visible body запрещено, exempt только в frontmatter / deck.yaml
/ iteration-log).

На всех 6 section dividers (s06/s12/s20/s26/s32 + s02 cover) — top
progress bar с английскими лейблами «1. Введение / 2. Hypothesis+Design
/ 3. Experiment / 4. Analyse / 5. Write+Review / 6. Замыкание». Это:
- Lec-N-1 pattern deviation (Lec-13/14 не имеют top progress bar
  нигде — ни на cover, ни на dividers, ни на content slides). Подтверждено
  via s05+s12 lec-14 rendered snapshots.
- Прецедент Лекция 2 R2: user explicit «нахрена этот хедер сверху
  везде?» — те же English-label labels у L2 → 4 sub-iterations to fix.
- LO codes на cover (LO4/5/6/8) запрещены в visible body per
  [[no-timing-no-methodology-in-slides]] (фундаментальное правило
  CLAUDE.md). Должны быть в frontmatter только.

**Visual evidence:**
- s02 snapshot: top bar «1. Введение» highlighted gold + 5 others grey
  English. Body card: «Модуль 3 · 75 минут», «LO4 — назвать инструменты...»
- s06/s12/s20/s26/s32: identical top bar visible at section index.

**Recommendation:**
1. Remove top progress bar entirely на cover + всех dividers
   (or move к speaker-notes-only).
2. Remove «75 минут» из s02 body (move в frontmatter).
3. Remove LO codes из s02 body. Replace «Цели лекции» card с
   plain-text version без LO-кодов.
4. If progress bar нужен — only на section dividers (Lec-1 pattern), но
   с **Russian labels** «Гипотеза + План», «Эксперимент», «Анализ»,
   «Текст + Рецензия», «Замыкание». НЕ на cover.

### P0-2. Methodology meta-comments на 4 dividers + s29 + s32

**Issue:** Прямое нарушение «No Methodology in Slides» правила
(CLAUDE.md фундаментальное, ENFORCED 2026-05-21). Хиты:

- s12 footer: «Лестница цикла · ступень 3 · **самый сильный раздел
  лекции**»
- s20 footer: «Лестница цикла · ступень 4 · **самые предсказуемые
  применения**»
- s26 footer: «Лестница цикла · ступени 5 и 6 · **самый острый раздел
  этики**»
- s32 footer: «**Самая важная часть лекции** — про осознанный отказ от AI»
- s29 right card: «Что произошло **(методологически)**:»
- s03 footnote: «Отличие от лекций 13 и 14: научный цикл итеративный, не
  последовательный.» — designer-extras meta-comment о структуре курса.
- s05 footnote: «Возвращаемся к рамке в **§5** и применяем в разобранном
  примере **WE-3** (катализатор)» — visible §-references + WE-codes.
- s33 footnote: «Это диагностический вопросник. Любое срабатывание —
  пауза + рассмотрение альтернативы.»
- s11 footer: «Урок: «AI» в науке — не один путь...» — meta about
  «lesson for engineer».
- s10 footer: «Урок для инженера: используйте Sakana как мозговой
  штурм...»
- s36 footnote: «Применима к любой задаче из любого раздела лекции.
  Распечатайте и держите в кармане.» — designer-extras self-reference.

**Visual evidence:** все 4 dividers + footers visible во всех PNG snapshots.

**Recommendation:**
1. Remove footers с methodology meta-comments на всех dividers (replace
   с tags-only or remove completely).
2. Strip «(методологически)» из s29; replace на «Что произошло:».
3. Strip «§5 / WE-3» mentions из s05; replace на «Эту рамку соберём в
   конце лекции».
4. Remove «Отличие от лекций 13 и 14» из s03 (course-scaffold meta).
5. Convert «Урок для инженера:» / «Урок:» footers в s10/s11 в plain
   takeaway sentence без слова «урок» / «для инженера».
6. Remove s36 footnote «Применима к любой задаче...» — keep slide
   self-contained.

### P0-3. Russification critical leak (~140 non-whitelist English tokens в visible body)

**Issue:** Memory rule [[russification]] + CLAUDE.md «anti-anglicism
mandate» violated. Critical narrative-body anglicisms (не brand / acronym /
case-name):

| Slide | English in visible body | Recommendation |
|---|---|---|
| s03 | «Hypothesis / Design / Experiment / Analyse / Write / Review» as primary labels (Russian gloss secondary courier); «augment+verify» tag; «зрелое ML» tag (mix) | Russian primary: «Гипотеза / Планирование / Эксперимент / Анализ / Текст / Рецензия» — English мелким курсивом или вообще убрать |
| s06/s12/s20/s26 dividers | English «Hypothesis + Design», «Experiment», «Analyse», «Write + Review» as h1 title | Russian primary |
| s07 | «Раскрытие AI» step OK; rest OK | — |
| s08 | «augmented черновик», «cherry-picking», «ICLR workshop» | «расширенный черновик», «отбор лучшего» |
| s09 | «multi-agent debate (generator + critic + ranker)»; «palladium-catalysed coupling»; «drug repurposing, gene therapy»; «[VFY-day-of]» visible | «мульти-агентный спор (генератор + критик + ранкер)»; «синтез связей с палладиевым катализатором»; «перепрофилирование лекарств, генная терапия»; STRIP `[VFY-day-of]` |
| s10 | «cherry-pick», «cherry-picking» | «отбор лучшего из множества» |
| s14 | «Open-source ladder» если visible | Russian translit |
| s15 | «Timeline:»; «в academic adoption» | «Хронология:»; «в академическом внедрении» |
| s17 footer | «Главный урок: …» — keep как `Урок` removable | — |
| s18 | «Atmospheric model schematic» caption | «Схема атмосферной модели» (per iter-4 fix log; verify rendered) |
| s19 | «Reinforcement learning + formal Lean theorem prover»; «LLM + symbolic solver» | «Обучение с подкреплением + формальный Lean-верификатор»; «LLM + символьный решатель» |
| s23 | «conformal prediction» repeated | «конформное предсказание» |
| s24 | «pLDDT score», «mitigation» if visible | brand acronym OK; «mitigation» → «снижение риска» |
| s25 WE-TESS | step labels: «Data overlap / Label availability / GPU cost / AUC baseline / Held-out validation»; «Pre-trained CNN»; «BLS алгоритм 1976»; «light curves TESS» в headline | «Перекрытие данных / Доступность разметки / Стоимость GPU / Эталон AUC / Проверка на отложенной выборке»; «Предобученный CNN»; «алгоритм BLS» |
| s27 | «academic adoption»; «editorial»; «metaанализы» mix | «академическое внедрение»; редакторская — но Russian-first |
| s29 | «(методологически)»; «peer review»; «figures»; «paper» | strip метод; «коллегиальное рецензирование»; «фигуры»; «статье» |
| s30 | «undefined» chart legend; «Acceptance rate»; «GPTZero Research»; «Это около 1% acceptance rate статей содержат прямые фейки» — mixed Ru-En | fix chart label «Количество статей»; «Доля принятых 24,52%»; «GPTZero Research» as brand OK |
| s35 | «Peer review» row name (other 4 alternatives — full Russian) | «Рецензирование (peer review)» |
| s36 | step 4 «HITL design»; step 5 «Pre-publication verify»; title «applicable artefact для кармана» | «HITL-планирование» (HITL acronym OK с inline gloss); «Проверка до публикации»; «практический артефакт для кармана» |
| s38 | recap list OK после iter-3 fix per log; verify | — |

**Visual evidence:** see Russification deep-scan results в § 11 of this
report (185 unique non-whitelist tokens в visible body, ~140 critical
narrative-body anglicisms).

**Recommendation:** Russify all step labels / tags / cards / footers.
Apply established acronym keep-list (LLM / RAG / GPU / CPU / CNN / GNN /
NMR / DFT / MD / BO / GP / DOI / AUC / pLDDT / HITL / ICMJE / NSF / IMO /
NeurIPS / ICLR — все с inline gloss при первом появлении). Brand names
(AlphaFold / Sakana / Coscientist / Boltz / GNoME / A-Lab / Aurora /
ECMWF / NotebookLM / Elicit / Consensus / TESS / Kepler / LIGO / IDP /
PDB / Wikipedia / Microsoft / DeepMind / etc) keep verbatim.

**Pre-USER-GATE B mandate:** `unique - whitelist = ∅` для narrative body
обязательно per CLAUDE.md.

### P0-4. Section divider tag-strip overflow (s12 / s20 / s26 / s32)

**Issue:** Tag rows на dividers cut off right edge. PNG render shows
only 3-4 tags visible из 5-6 в source. Это сильно нарушает читаемость +
теряет логику «что я узнаю в этом разделе».

| Slide | Tags в source | Видно в PNG | Cut off |
|---|---|---|---|
| s06 | 4 (WE-1 / Sakana / Coscientist / BO+GP) | ~3 fully + Coscientist cut | 1 |
| s12 | **6** (AlphaFold / Boltz / GNoME / Palgrave / Aurora / AlphaProof) | 3 (AlphaFold + Boltz + GNoME) | **3 cut** |
| s20 | 5 (CNN экзо / MICrONS / LIGO / IDP / WE-TESS) | 3 fully | 2 cut |
| s26 | 5 (NotebookLM / WE-2 / Frontiers / NeurIPS / ICMJE) | 3 fully | 2 cut |
| s32 | 5 (4 критерия / WE-3 / 5 альтернатив / 3 вопроса / RU) | 3 visible | 2 cut |

**Visual evidence:**
- s12 PNG: only «AlphaFold + Нобель», «Boltz открытый», «GNoME / A-Lab»
  visible; «Палгрейв критика», «Aurora 5000×», «AlphaProof IMO» **cut off**.
- s20: «CNN экзопланеты», «MICrONS connectome», «LIGO conformal» visible;
  «AlphaFold IDP трещина», «WE-TESS пример» **cut off**.

**Recommendation:**
1. Reduce font size of tags by ~30% (12pt → 8pt) OR
2. Wrap tags в 2 rows on dividers OR
3. Limit tags к maximum 4 per divider (drop optional ones) OR
4. Remove tags entirely — оставить только section number + main statement.

Best: option 3 (limit к 4 tags max, keep most representative) +
Russification.

---

## P1 findings (should-fix before GATE B)

### P1-1. «undefined» chart legend persistent bug (s27 + s30)

Iter-3 log claims «Regenerated charts with proper labels (no
"undefined" legend leak)». **Bug persists in current render**:
- s27: bar chart bottom: legend reads "undefined" с teal swatch.
- s30: NeurIPS bar chart: legend reads "undefined" с teal swatch.

**Visual evidence:** s27 PNG (bottom chart) + s30 PNG (left chart) — both
have «undefined» legend.

**Recommendation:** Regenerate QuickChart с explicit `label` field в
dataset config. Verify rendered PNG визуально перед commit.

### P1-2. s29 «CELLLS» overflow поверх timeline box

**Issue:** На s29 Frontiers крыса: typography callout «PROTEMNS» /
«ZXPENS» / «**CELLLS**» — третий term is **cut off and overlapping**
the timeline box below. Это структурный layout bug.

**Visual evidence:** s29 PNG — «CELLLS» visible partially under «Timeline:»
box top edge.

**Recommendation:** Reduce font size of typography callouts OR limit к
2 terms (drop «CELLLS» since «Protemns» + «Zxpens» already make the point;
chapter mentions all three but slide can show 2).

### P1-3. s09 «[VFY-day-of]» visible scaffold

**Issue:** Designer-extras scaffold marker «[VFY-day-of]» visible на
s09 Co-Scientist card (right side, italic gray). Должно быть в speaker
notes only.

**Recommendation:** Strip `[VFY-day-of]` из visible body. Replace на
plain text «Nature submission ожидается» или just remove.

### P1-4. s37 RU context — real brand logos claimed но не видны в render

**Issue:** Iteration log claims Tier 2 Wikimedia images acquired для
AIRI / Sber / Yandex (assets/images/s37-yandex.jpg + s37-sber.jpg). В
PNG render s37 — три text-only cards без visible logos / images.

**Visual evidence:** s37 PNG — три карточки «AIRI / Sber AI Lab / Yandex
Research» — text only, no embedded images.

**Recommendation:** Verify python-pptx builder for s37 включает
add_picture() calls для acquired images. Если pictures были built но
malformed — regenerate. Если pictures были intentionally omitted —
document как mock-fallback decision в iteration-log.md и flag как
acceptable substitute.

### P1-5. s01 hero — Galactica side weak after iter-2 substitution

**Issue:** s01 hero composite v1 had Galactica spacebears image
(misleading); iter-2 replaced с text-card «Why Meta's Galactica only
survived three days online» — MIT Technology Review headline. Это
acceptable substitute (fair-use editorial headline screenshot) но
visually weak vs Nobel ceremony photo on left.

**Visual evidence:** s01 PNG — left half: Stockholm Konserthuset photo
(Nobel side) ✓ real. Right half: white card с red «RETRACTED — отозвано»
banner + small text headline screenshot — looks like text-card mockup,
not real screenshot.

**Recommendation:**
1. Если возможно — acquire real MIT Technology Review article screenshot
   (Tier 6 fair-use) с visible headline + photo.
2. Если Tier 6 failed — current text-card acceptable, но make it more
   visually balanced с Nobel side: add red overlay frame, ensure visual
   weight ≥40% as required for hero.
3. Current «9 октября 2024» + «17 ноября 2022» dates ниже композита OK.

### P1-6. s39 closing hero — substitute weak (AlphaFold ribbon repeat)

**Issue:** s39 — AlphaFold DB screenshot was Tier 1-6 failure per log;
substitute is AlphaFold 2 ribbon composite. Это:
- Visually repeats s14 imagery (s14 also shows AlphaFold ribbon)
- Not actually AlphaFold DB (database website) — это protein structure
  visualization
- Lacks bridge-to-Lec-16 (нефтегаз) signaling

**Visual evidence:** s39 PNG — composite of AlphaFold ribbons + benchmark
chart fragments + protein cluster diagram. Caption «AlphaFold DB — 200
миллионов структур · alphafold.ebi.ac.uk».

**Recommendation:**
1. Try Tier 6 again: Wayback Machine snapshot of alphafold.ebi.ac.uk
   home page (Internet Archive crawl from 2024).
2. If still failed — composite better: use 1 representative ribbon (not
   3) + URL + bridge-to-lec-16 visual element (oil rig icon или earth
   subsurface schematic).
3. Document Tier 6 attempt in iteration-log.md per [[no-mock-fallbacks]].

### P1-7. s03 lecture-map — cyclical arrow weak

**Issue:** Per assertion «Cyclical, не sequential» — но в render cyclical
arrow shown only via small gold curl icon в bottom-right of orange-callout
box. Easy to miss. Differentiation от Lec-13/14 (sequential ladders)
weakened.

**Visual evidence:** s03 PNG — 6 boxes in row, gold cycle icon ~30×30 px
в углу — barely visible.

**Recommendation:** Add explicit curved arrow Review (box 6) → Hypothesis
(box 1) returning over the top. Make arrow line ≥3 pt teal-color thick.
This is the keystone-axis defining differentiator — must be visually
unmissable.

### P1-8. s35 «Peer review» row anglicism

**Issue:** s35 5 alternatives matrix — 4 row labels Russian («BO+GP»
brand + «DFT + MD» brand + «Классич. статистика» + «OR-Tools / Simplex»
brand). 5th row: «Peer review» — pure English. Inconsistent.

**Recommendation:** Replace на «Коллегиальное рецензирование» or
«Рецензирование (peer review)».

### P1-9. s05 §5 / WE-3 reference visible

Already covered в P0-2. Restated for completeness: «Возвращаемся к
рамке в §5 и применяем в разобранном примере WE-3» — section + walked-
example codes visible в visible body.

### P1-10. s28 «Стоимость: 5 мин / 15 мин / 5 мин / 20 мин» — borderline

**Issue:** Timing visible в visible body — но это subject-matter timing
(per-step verification cost), not lecture pacing. CLAUDE.md «No Timing»
правило applies к lecture pacing markers только. **Acceptable as content.**

**Recommendation:** Keep as is. (Flagged для transparency.)

### P1-11. s07/s09/s11 footers с «Урок:» / «Главный приём:» — borderline meta

**Issue:** Footers с «Урок для инженера:», «Главный приём:», «Что это
значит:» — borderline methodology meta-comments.

**Recommendation:** Replace на plain takeaway без слова «урок» /
«приём». Например, «Используйте Sakana как мозговой штурм с человеческим
фильтром» вместо «Урок для инженера: используйте Sakana...».

### P1-12. Cross-slide redundancy: AlphaFold appears на 6 slides (s01/s13/s14/s15/s24/s39)

**Issue:** AlphaFold doman dominates lecture (correctly — самый сильный
case). Но:
- s01 hero + s13 timeline + s14 DB + s15 Boltz comparison + s24 IDP
  failure + s39 closing — 6 slides с AlphaFold ribbon imagery.
- Visual fatigue + некоторая redundancy.

**Recommendation:** Differentiate s14 (DB scale) vs s39 (closing bridge)
visually — use DIFFERENT AlphaFold ribbon image (or one structure type vs
multiple). Currently s14 + s39 use SAME AlphaFold_2.png from Wikimedia.

### P1-13. s23 LIGO body density

**Issue:** s23 LIGO control room photo + waveform chart + dense body
с «calibrated 95% interval» / «matched filtering» / «conformal
prediction» / «Wiener 1949, 80 лет наследия» — dense, hard to teach в
2 min.

**Recommendation:** Trim body к 2 key points: (1) conformal prediction =
калиброванный 95% interval (схема), (2) ML дополняет matched filter,
не заменяет (timeline 1949-2025).

### P1-14. s34 WE-3 catalyst — composite layout dense

**Issue:** Multiple images + flow diagram + text — at thumbnail very
busy. 5-step framework + comparison block.

**Recommendation:** Simplify image strip к 1 representative catalyst
photo + larger 5-step flow.

### P1-15. s27 NotebookLM/Elicit/Consensus — no real UI screenshots

**Issue:** Per iteration log no Tier 1-6 screenshots acquired для
NotebookLM / Elicit / Consensus UI. Three text-only cards + bar chart
substitute. Acceptable per memory rule (Tier 6 failure documented), но
hero-quality demanded for mature tool showcase.

**Recommendation:** Try Tier 6 again: take real screenshots of
notebooklm.google.com home page + elicit.com home page + consensus.app
home page (fair-use educational excerpts). Add к assets/images/. Replace
text cards с screenshots + brand callout. If failed — current substitute
acceptable.

### P1-16. s13 image composition — Hassabis + Baker portraits OK but small

**Issue:** s13 has 2 real Nobel laureate portraits (Hassabis, Baker)
+ AlphaFold 3 layer-by-layer first-frame. All real images ✓. But
composition — 3 mini-images + text-heavy right column + bottom caption
— heavy.

**Recommendation:** Trim text. Keep 2 portraits + 1 ribbon = 3 images
maximum. Move «Каскад нобелевской премии: AlphaFold...» к concise 2-line
takeaway.

### P1-17. s24 AlphaFold IDP body — no baseline for «22% галлюцинаций»

**Issue:** «22% галлюцинаций в IDP-регионах» — measurable claim. Inline
baseline для «from what reference rate?» отсутствует. Per CLAUDE.md
Baseline Mandate — каждое measurable claim ОБЯЗАНО иметь base или
counterfactual.

**Visual evidence:** s24 PNG — pLDDT thresholds 90/70/50 are shown, но
это mitigation thresholds, не baseline against which 22% measured.

**Recommendation:** Add inline baseline: «22% галлюцинаций в IDP-регионах
**vs <2% в well-folded PDB benchmark**» or similar comparative.

### P1-18. s22 Allen MICrONS — composite of 4 images

**Issue:** Per designer log s22 uses composite: Allen Institute building
+ mouse brain + connectome MRI + visual cortex. Это 4 images stacked —
visual fatigue + dilutes focus on canonical claim «84k neurons / 500M
synapses / 4km axons».

**Recommendation:** Use 1 dominant connectome visualization (most striking
visual representation) + retreat building/anatomy к small attribution
strip.

---

## P2 findings (polish)

### P2-1. s04 glossary — 15 rows dense, but readable
Acceptable — reference slide doesn't need 5-sec teach test.

### P2-2. s11 BO+GP convergence chart — Y-axis label could be clearer
«Loss / Error» or «Расстояние до оптимума» would clarify.

### P2-3. s15 Boltz chart — 4th metric «Антитело-антиген» bar для AlphaFold 3 only (Boltz-1 не tested)
Could add note «Boltz-2 готовит» or grey-out.

### P2-4. s10 Sakana chart — 3 bars label «Принято / Отобрано / Истинная автономия»
Bar labels are wrapped — could be cleaner. Y-axis 0-35 OK.

### P2-5. s17 Palgrave pie chart — small
Pie wedges hard to distinguish. Could enlarge OR convert в horizontal stacked bar.

### P2-6. s31 ICMJE matrix — 4 publishers × 5 criteria
Headers «Springer / Elsevier / Frontiers / Nature/ICMJE» OK. «Запрещено» / «Обязательно» color coding red/gold strong ✓.

### P2-7. Gold accent presence
Verified gold accent on s01 (Galactica retraction red), s03 (gold step 3 keystone), s05 (gold question card), s07/s28 (gold step 6/5), s08/s10/s16/s19 (gold chart elements), s15 (gold Boltz bars), s17 (gold pie wedge), s27 (cards), s28 (step 4), s30 (gold «100+»), s31 (gold cells), s33 (gold step 4), s35 (gold col), s37 (gold Указ year), s38 (gold ✓). Most slides have ≥1 gold accent ✓.

### P2-8. Section divider letterforms «§N»
«§1», «§2», «§3», «§4», «§5» large display — strong identity ✓. s06 has teal §1, s12 has gold §2 (Experiment), s20 has teal §3, s26 has red §4, s32 has teal §5. Color choices match section vibe (s12 gold = highest impact, s26 red = ethics).

### P2-9. s38 Q&A dedicated slide pattern
Strong recap «Реальные прорывы» list + «Лестница цикла — краткое повторение». Lec-N-1 pattern compliant ✓.

---

## § 7. Visual sweep table — 39 slides

Legend: ✓ pass · ⚠ minor · ✗ fail

| Slide | 5-sec teach | Hierarchy | Palette+Gold | Media: real/sub/mock | Designer-extras |
|---|---|---|---|---|---|
| s01 hero | ⚠ Galactica text-card weak | ✓ | ✓ | sub (Galactica = text-card, Nobel = real Stockholm) | ⚠ — |
| s02 cover | ⚠ | ✓ | ✓ | n/a | ✗ «75 минут» + «LO4-8» visible |
| s03 lecture-map | ⚠ cyclical arrow weak | ✓ | ✓ | n/a (custom shapes) | ✗ «Отличие от лекций 13/14» + Eng labels |
| s04 glossary | ✓ (reference) | ✓ | ✓ | n/a | ✓ |
| s05 central-q | ✓ | ✓ | ✓ | n/a | ✗ «§5 + WE-3» refs |
| s06 §1 divider | ⚠ tags cut | ✓ | ✓ | n/a | ✗ top bar Eng + footer methodology |
| s07 WE-1 | ✓ | ✓ | ✓ | n/a (custom) | ✓ |
| s08 Sakana | ✓ | ✓ | ✓ | real ✓ Sakana logo | ⚠ «augmented / cherry-pick» |
| s09 Coscientist vs | ⚠ text-heavy | ✓ | ✓ | mock (text-only, Tier 1-6 fail documented) | ✗ «[VFY-day-of]» |
| s10 Sakana cherry | ✓ | ✓ | ✓ | chart (custom) | ⚠ «cherry-picking» + «Урок» |
| s11 BO+GP | ✓ | ✓ | ✓ | chart (custom) | ⚠ «Урок:» footer |
| s12 §2 divider | ✗ 6 tags overflow | ✓ | ✓ | n/a | ✗ top bar Eng + footer «самый сильный» |
| s13 AlphaFold timeline | ⚠ dense | ✓ | ✓ | real ✓ Hassabis + Baker + ribbon | ⚠ |
| s14 AlphaFold DB | ⚠ dense | ⚠ | ✓ | real ✓ ribbon | ⚠ |
| s15 Boltz | ✓ | ✓ | ✓ | chart custom + real Boltz GitHub | ⚠ «Timeline / academic adoption» |
| s16 GNoME/A-Lab | ✓ | ✓ | ✓ | chart custom | ✓ |
| s17 Palgrave | ✓ | ✓ | ✓ | chart + ChemRxiv ref | ✓ |
| s18 Aurora | ⚠ dense | ⚠ | ✓ | real ✓ atmospheric + ECMWF logo | ⚠ |
| s19 AlphaProof | ✓ | ✓ | ✓ | real IMO logo + chart | ⚠ Eng tech terms |
| s20 §3 divider | ✗ 5 tags overflow | ✓ | ✓ | n/a | ✗ top bar + footer methodology |
| s21 Exoplanet | ✓ | ✓ | ✓ | real TESS + Kepler + chart | ⚠ Eng |
| s22 Allen MICrONS | ⚠ 4-image composite | ⚠ | ✓ | real (composite 4) | ✓ |
| s23 LIGO | ⚠ dense | ✓ | ✓ | real LIGO + black holes + chart | ⚠ «conformal prediction» |
| s24 AlphaFold IDP | ⚠ | ✓ | ✓ | real protein structure + diagram | ⚠ no baseline for 22% |
| s25 WE-TESS | ⚠ step labels Eng | ✓ | ✓ | n/a (custom) | ✗ «Data overlap / Label availability / GPU cost / AUC baseline / Held-out validation» |
| s26 §4 divider | ✗ 5 tags overflow | ✓ | ✓ | n/a | ✗ top bar + footer methodology |
| s27 NotebookLM/Elicit | ⚠ no UI screenshots | ⚠ chart «undefined» | ✓ | mock-fallback (text-only) | ⚠ Eng |
| s28 WE-2 | ✓ | ✓ | ✓ | n/a (custom) | ⚠ «Стоимость X мин» (acceptable as content) |
| s29 Frontiers крыса | ✗ «CELLLS» overflow | ⚠ | ✓ | mock (text-only typography, Tier 6 fail) | ✗ «методологически» + «peer review» |
| s30 NeurIPS fake | ⚠ chart «undefined» | ✓ | ✓ | chart custom | ⚠ «Acceptance rate» |
| s31 ICMJE matrix | ✓ | ✓ | ✓ | n/a (custom table) | ✓ |
| s32 §5 divider | ⚠ 5 tags overflow | ✓ | ✓ | n/a | ✗ top bar + footer «Самая важная часть» |
| s33 Four criteria | ✓ | ✓ | ✓ | n/a (custom) | ⚠ «Это диагностический вопросник» |
| s34 WE-3 catalyst | ⚠ dense composite | ✓ | ✓ | real catalyst + custom | ⚠ |
| s35 Alternatives | ✓ | ✓ | ✓ | n/a (table) | ⚠ «Peer review» row |
| s36 Vendor framework | ✓ | ✓ | ✓ | n/a (custom) | ⚠ «applicable artefact для кармана» + «HITL design / Pre-publication verify» |
| s37 RU context | ⚠ no logos visible | ✓ | ✓ | claimed real but logos missing | ✓ |
| s38 Q&A | ✓ | ✓ | ✓ | n/a (custom) | ✓ |
| s39 closing hero | ⚠ ribbon repeat | ⚠ | ✓ | sub (AlphaFold ribbon, not DB screenshot — Tier 6 fail documented) | ✓ |

**Aggregate:**
- 5-sec teach: 18 ✓, 16 ⚠, 5 ✗ (s12, s20, s25, s26, s29)
- Hierarchy: 33 ✓, 6 ⚠
- Palette+Gold: 39 ✓
- Media real: 13 real ✓ · 4 acceptable substitute (s01 Galactica /
  s09 / s27 / s29 / s39) · 2 mock-fallback documented · rest n/a
  (custom schemas)
- Designer-extras: 14 ✗ critical + 17 ⚠ minor (high count → reflect P0/P1)

---

## § 8. Hero check — s01 + s39

### s01 — Side-by-side AlphaFold Nobel + Galactica retraction

**Status:** ⚠ acceptable substitute, ≥40% area met, но Galactica side visually weak.

- LEFT (Nobel side): Stockholm Konserthuset photo (Tier 2 Wikimedia)
  + 9 октября 2024 date + «Нобель по химии за AlphaFold» — real
  identifiable visual ✓.
- RIGHT (Galactica side): Iteration-2 fix replaced misleading
  spacebears with white card showing red «RETRACTED — отозвано» banner
  + small MIT Technology Review headline screenshot («Why Meta's
  Galactica only survived three days online · Will Douglas Heaven · 18
  ноября 2022») + «48 ans untuk crash...» small Russian gloss. This is
  text-card with header screenshot — acceptable mock-substitute per
  designer log (Tier 6 fair-use educational excerpt available).
- BOTTOM caption: «AlphaFold взял Нобель. Galactica прожила три дня.
  Различать — задача инженера» — strong assertion ✓.

**Verdict:** Acceptable but visually unbalanced. Nobel side has photo;
Galactica side is text-card-on-white. Better balance possible с real
MIT TR article screenshot OR equivalent Meta press visual.

### s39 — AlphaFold DB closing hero

**Status:** ⚠ substitute weak, designer log honest about Tier 1-6
failure.

- Composite: AlphaFold 2 ribbon (Wikimedia) + benchmark chart fragments
  + protein cluster diagram.
- Caption: «AlphaFold DB — 200 миллионов структур · alphafold.ebi.ac.uk»
- Title: «Биология теперь чуть больше известна. Финальная карта далека.»
- Bridge text: «AlphaFold показал: закрытые задачи доступны AI. Лекция
  16 — нефтегаз: частично закрытый (геофизика) + частично открытый
  (резервуар).»

**Verdict:** Acceptable as substitute per [[no-mock-fallbacks]] memory
rule (Tier 6 documented failure for AlphaFold DB website hero). BUT:
1. Repeats s14 ribbon imagery — visually weak as closing hero.
2. No real bridge-to-Lec-16 visual element — bridge is text-only.
3. Could improve composition даже без new image acquisition: enlarge
   single dominant ribbon + add subsurface schematic icon for Lec-16
   bridge.

**Recommendation:** Try once more Wayback Machine snapshot of
alphafold.ebi.ac.uk circa 2024 (Internet Archive). If failed —
acceptable, но improve composition.

---

## § 9. Schema slides assessment

| Slide | Schema type | 5-sec teach | Quality |
|---|---|---|---|
| s03 lecture-map | 6-step ladder + cyclical arrow | ⚠ cyclical weak | Strong layout, weak differentiator |
| s07 WE-1 | 6-step decision tree | ✓ | Good after iter-2 Russification |
| s25 WE-TESS | 5-step framework | ✗ English step labels | Russify required |
| s28 WE-2 | 4-step verification | ✓ | Strong (Russian labels) |
| s31 ICMJE matrix | 4 publishers × 5 criteria | ✓ | Strong, color-coded |
| s33 Four criteria | 4-quadrant matrix | ✓ | Strong |
| s34 WE-3 | 5-step pipeline | ⚠ dense | Could simplify image strip |
| s35 Alternatives | 5×4 table | ✓ | Strong (1 English row to fix) |
| s36 Vendor framework | 3 + 5 dual schema | ✓ | English step labels to fix |

---

## § 10. Mock vs real image detailed audit

**Real images acquired (per iteration log claim):**

| Slide | Image | Real ✓ / Mock ✗ / Sub ⚠ | Notes |
|---|---|---|---|
| s01 Nobel | Stockholm Konserthuset | ✓ Tier 2 Wikimedia | Real concert hall photo |
| s01 Galactica | text-card with headline | ⚠ Sub | Iter-2 fix; was misleading spacebears; acceptable text substitute per fair-use |
| s08 Sakana | sakana.ai logo + fish | ✓ Tier 1 og:image | Real brand identity |
| s13 Hassabis | portrait Wikimedia | ✓ Tier 2 | Real Nobel portrait |
| s13 Baker | portrait Wikimedia | ✓ Tier 2 | Real Nobel portrait |
| s13 AlphaFold 3 ribbon | Wikimedia animated GIF first frame | ✓ Tier 2 | Real |
| s14 AlphaFold | ribbon Wikimedia | ✓ Tier 2 | Real, but same image repeated on s39 |
| s15 Boltz | GitHub og:image | ✓ Tier 1 | Real |
| s18 Aurora atmospheric model | Wikimedia atmospheric model schematic | ⚠ Sub | Generic atmospheric schematic, not actual Aurora press image; ECMWF logo OK |
| s18 ECMWF | Wikimedia logo | ✓ Tier 2 | Real logo |
| s19 IMO | Wikimedia logo SVG | ✓ Tier 2 | Real IMO logo |
| s21 TESS | Wikimedia NASA TESS | ✓ Tier 2 | Real |
| s21 Kepler | Wikimedia Kepler Space Telescope | ✓ Tier 2 | Real |
| s22 Allen building | Wikimedia | ✓ Tier 2 | Real but not MICrONS-specific |
| s22 mouse brain | Wikimedia | ✓ Tier 2 | Real generic anatomical |
| s22 connectome | Wikimedia MRI Tractography | ⚠ Sub | Generic tractography, not actual MICrONS image |
| s22 visual cortex | Wikimedia Brodmann areas | ⚠ Sub | Generic anatomy diagram |
| s23 black holes | Wikimedia Caltech-MIT-LIGO | ✓ Tier 2 | Real |
| s23 LIGO control | Wikimedia LLO_Control_Room | ✓ Tier 2 | Real |
| s24 protein structure | Wikimedia | ✓ Tier 2 | Real |
| s27 NotebookLM/Elicit/Consensus | text-only cards | ⚠ Mock-fallback | No UI screenshots acquired (per log) |
| s29 Frontiers крыса | text-only typography | ⚠ Mock-fallback | Per log: «iconic image was the retracted figure itself, paywalled» — text substitute documented |
| s34 catalysts | Wikimedia | ✓ Tier 2 | Real catalyst photo |
| s37 AIRI/Sber/Yandex | claimed but not visible in render | ✗ Render bug | Iter log claims Yandex office + Sber city acquired, но render показывает text-only cards |
| s39 AlphaFold DB | AlphaFold 2 ribbon | ⚠ Sub repeat | Tier 1-6 fail documented; repeats s14 |

**Tier 1-6 failure documented (acceptable per [[no-mock-fallbacks]]):**
- AlphaFold DB direct hero (s39) — documented ✓
- Allen MICrONS press image (s22) — documented, composite used ✓
- Microsoft Aurora press image (s18) — documented, schematic used ✓
- Frontiers rat anatomy (s29) — documented, typography used ✓
- Coscientist CMU lab photo (s09) — documented, diagram used ✓
- NotebookLM/Elicit/Consensus UI (s27) — **NOT documented as Tier 6
  failure**, just absent. Should attempt 6-tier or document why skipped.

**Sample size verified:** 25 real images claimed + ~6 documented substitutes
(documented Tier 1-6 failures per [[no-mock-fallbacks]] rule), ~3 acceptable
text substitutes (s09 / s29 / partial s27). No mock-fallbacks disguised as
real screenshots detected. Per memory rule baseline met.

**Mock-fallback violations:** 1 (s27 NotebookLM/Elicit/Consensus
should have Tier 1-6 attempt documented).

**Verdict:** Designer-extras claim of 25/16 real images mostly stands;
honest Tier 6 failure logging is acceptable.

---

## § 11. Russification deep scan results

**Method:** Extracted PPTX visible body (excluding speaker notes) — split
on `=== Slide N ===` headers, regex'd all Latin tokens length ≥3, applied
whitelist (brand / acronym / case-name).

**Numbers:**
- 364 unique Latin tokens in visible body
- 185 unique non-whitelist (potential anglicisms)
- ~140 critical narrative-body anglicisms (after subtracting borderline /
  abbreviation cases)

**Top critical categories:**

| Category | Examples | Count |
|---|---|---|
| Step labels in schemas | Hypothesis, Design, Experiment, Analyse, Write, Review, Data overlap, Label availability, GPU cost, AUC baseline, Held-out validation, HITL design, Pre-publication verify | ~25 |
| Body narrative English | augmented, cherry-pick, cherry-picking, conformal, peer review, paper, figures, retraction, online, days, baseline, transfer, learning, formal, theorem, prover, solver, symbolic, debate, generator, critic, ranker, ground truth, multi-agent, light curves, design, science, surveys, citations, gene therapy, drug repurposing, palladium-catalysed, coupling, applicable, artefact, academic, adoption, editorial, fair-use, ranking, rate, acceptance, custom, validation, verify, augment+verify | ~80 |
| Designer scaffold leak | VFY-day-of, Timeline:, ai-scientist-v2, CC-BY-SA, CC-PD | ~5 |
| Mixed brand+English | TESS+Kepler, Caltech-MIT-LIGO, GP-BO, BO+GP (brand+English) | ~5 |
| Iteration-residual case typography | PROTEMNS, ZXPENS, CELLLS, RETRACTED | 4 (acceptable as iconic «несуществующие термины» — these ARE the case story; transliterated would lose meaning) |

**Deep scan verdict:** ~140 critical narrative-body anglicisms ≫ threshold
per [[russification]] + CLAUDE.md (>5 critical = P0 anti-anglicism mandate
violated). **Pre-USER-GATE B mandate `unique - whitelist = ∅` NOT met.**

---

## § 12. Cascade canonical numbers spot-check (8 numbers — ALL PASS ✓)

| Claim | Spot value | Expected (chapter v2.2) | Status |
|---|---|---|---|
| A-Lab synthesis | 41 из 58 | 41/58 (NOT 36/57) | ✓ canonical |
| Palgrave critique | 35 из 36 | 35/36 | ✓ canonical |
| Nobel date | 9 октября 2024 | 9 окт 2024 | ✓ canonical |
| NeurIPS scale | 21 575 / 5 290 / 24,52% | 21,575 / 5,290 / 24.52% | ✓ canonical |
| GNoME rounds | 6 раундов активного обучения | 6 (NOT 22) | ✓ canonical |
| AlphaProof IMO | P1, P2, P6 solved + P3, P5 unsolved + P4 by AlphaGeometry 2 | P1/P2/P6 AlphaProof + P4 AlphaGeometry + P3/P5 unsolved | ✓ canonical |
| Recursion-Roche | декабрь 2021 / 40 программ / >$300M / до $12B | дек 2021 / 40 prog / $300M+ / $12B | ✓ canonical |
| Указ № 490 + № 124 | № 490 10 октября 2019 / № 124 15 февраля 2024 | 10.10.2019 / 15.02.2024 | ✓ canonical |

**Canonical integrity:** 8/8 PASS ✓ — нет drift'a.

---

## § 13. Top 5 priorities для Phase 8 revision

### Priority 1 (BLOCKING) — Strip top progress bar + LO codes + timing from cover/dividers
- Remove top progress bar (с английскими labels) на cover s02 + на всех 5
  section dividers s06/s12/s20/s26/s32.
- Remove «75 минут» from s02 body.
- Remove «LO4 / LO5 / LO6 / LO8» codes from s02 body. Replace «Цели
  лекции» list с Russian plain-text version без LO кодов.
- **Why blocking:** CLAUDE.md ENFORCED [[no-timing-no-methodology-in-slides]]
  + memory rule «user правил в каждой L1-L10» + Lec-N-1 pattern deviation
  prevented by Pre-USER-GATE check.

### Priority 2 (BLOCKING) — Russify step labels + body anglicisms (~140 critical hits)
- Apply per-slide Russification per § 11 table.
- Especially: s03 / s06 / s12 / s20 / s26 / s32 (English division titles
  «Hypothesis / Design / Experiment / Analyse / Write / Review» → Russian
  primary).
- s25 WE-TESS step labels → Russian.
- s36 framework step labels → Russian.
- Strip «applicable artefact для кармана» → «практический артефакт».
- Strip «[VFY-day-of]» from s09.
- Apply established acronym keep-list + brand allowlist; everything else
  Russified.

### Priority 3 (BLOCKING) — Strip methodology meta-comments
- s12 footer: «самый сильный раздел лекции» → just tag-strip + tag «3
  working cases · 2 трещины» format.
- s20 footer: «самые предсказуемые применения» → strip.
- s26 footer: «самый острый раздел этики» → strip.
- s32 footer: «Самая важная часть лекции — про осознанный отказ от AI»
  → strip OR replace с tag-strip «4 critеria · WE-3 · 5 alternatives ·
  3 vendor questions · RU context».
- s29 «(методологически)» → strip.
- s03 footnote «Отличие от лекций 13 и 14» → strip.
- s05 «§5 / WE-3» refs → reword без § и WE codes.

### Priority 4 (BLOCKING) — Fix divider tag overflow + chart bugs
- Reduce tag count к ≤4 per divider OR shrink font к 8pt OR wrap к 2 rows.
- Regenerate s27 + s30 charts with explicit `label` (fix «undefined»
  legend).
- Fix s29 «CELLLS» overflow поверх timeline box (reduce font OR drop to 2
  terms).
- Verify s37 logos render (python-pptx add_picture() call check).

### Priority 5 (P1 polish) — Hero improvements + s24 baseline
- s01 hero: balance Galactica side visually с Nobel side (add red overlay
  frame or attempt real MIT TR screenshot).
- s39 closing hero: try Wayback Machine for alphafold.ebi.ac.uk OR improve
  composition + add Lec-16 bridge visual.
- s03 cyclical arrow: make explicit curved arrow visible (≥3pt teal).
- s24 baseline: add inline «22% галлюцинаций vs <2% в well-folded PDB»
  for measurable claim per CLAUDE.md Baseline Mandate.

---

## Closing

**Verdict:** REVISE. 4 P0 (timing/LO/methodology/overflow + Russification
+ divider overflow + chart bugs) → cannot proceed to USER GATE B без
revision.

Структурно deck сильный: keystone cyclical, canonical numbers integrity
8/8, walked examples 4 шт. сбалансированы, failure deep-dives 5 шт.
методически выстроены, ICMJE matrix s31 + Four criteria s33 + 5
alternatives s35 + Vendor questions s36 — образцовые. Hero substitutes
honest per [[no-mock-fallbacks]] rule. 25 real images acquired vs 0
mock-fallbacks-disguised-as-real.

Но v1 strictly fails:
1. No-timing/methodology rule (фундаментальное)
2. Russification mandate
3. Lec-N-1 pattern (top bar present, Lec-13/14 не имеют)
4. Layout overflow (5 dividers)

**Estimated revision effort:** 1 producer session (presentation-designer)
с focused Phase 8 prompt targeting Priority 1-4. Priority 5 (heroes +
baseline) — second sub-iteration.

После revision — re-spawn presentation-critic + run pre-gate walkthrough
+ open USER GATE B.
