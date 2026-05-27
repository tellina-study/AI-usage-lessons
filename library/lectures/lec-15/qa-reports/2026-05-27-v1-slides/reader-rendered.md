# Reader (Rendered) Report — Лекция 15 — 2026-05-27

**VERDICT: APPROVE-WITH-POLISH**

Mode: rendered. Reading 39 PNG snapshots + speaker notes как студент-инженер ИУ6 МГТУ через 2 недели после лекции, готовлюсь к самоповторению за ~30 минут до зачёта/семинара. Лектора рядом нет, только PPTX + конспект.

Self-containedness baseline:
- **32 / 39 self-contained** (понимаю slide + notes без преподавателя)
- **5 / 39 нужна doработка notes / minor visual fix** (понимаю с трудом)
- **2 / 39 имеют визуальный/контентный leak** (LO codes, методология, VFY-маркер в visible body)

Это **84% self-contained ratio** — ниже production threshold 85%, но в рамках APPROVE-WITH-POLISH (25-32 / 39). Все 5 «затруднения» — notes-fixable; 2 leak'а — quick visible body edits (5 минут). Структурных blocker нет.

---

## 1. Verdict Justification

- ≥30/N (32/39) self-contained → APPROVE-WITH-POLISH либо APPROVE-CLEAN
- НЕ APPROVE-CLEAN: имеются 2 visible body leak'а (LO codes на s02 + (методологически) на s29 + [VFY-day-of] на s09/s39) — это P1 не P2, явные нарушения «No Methodology / Scaffold Leaks in Slides» rule из CLAUDE.md.
- НЕ REVISE: self-containedness через 2 нед сохраняется на всех 39 слайдах при минимальном patch (5 mins для visible body cleanup); content depth у speaker notes отличный, прозы 117-306 слов в каждой.

---

## 2. Self-Containedness Assessment (sample 15 of 39 slides)

| Slide | Можно восстановить через 2 нед? | Что забыл / не помню без лектора | Что в notes недостаточно |
|---|---|---|---|
| s01 Hook | **Да** | Композит AlphaFold/Galactica читается; даты в caption | — |
| s02 Cover | **Да, частично** | LO коды LO4/LO5/LO6/LO8 на слайде ничего мне не говорят без glossary | LO коды должны быть в frontmatter, не в visible body |
| s03 Lecture-map | **Да** | Шесть ступеней + cyclical хорошо читаемые | — |
| s04 Glossary | **Да** | Таблица 15 терминов с примерами — лучшая часть самоповторения | — |
| s05 Central Q | **Да** | 5-step framework предъявлен; «§5» footer мне понятен как chapter reference | — |
| s07 WE-1 Grant | **Да** | 6-шаговое дерево с ясными шагами; baseline counter-claim в notes | — |
| s09 Coscientist vs Co-Scientist | **Да, частично** | Имена путаются через 2 нед — но slide прямо предупреждает «Не путать» | **[VFY-day-of]** в visible body — недопустимо |
| s10 Sakana cherry-pick | **Да** | Funnel 100→3→1 + 4 структурные проблемы — крепкая визуализация | — |
| s11 BO+GP альтернатива | **Да** | Чарт + дата 1989/1998 + урок — компактно | — |
| s14 AlphaFold DB scale | **Да** | 200M vs 200K — впечатляющий контраст | — |
| s17 Палгрейв критика | **Да** | Donut «35 из 36 проблем» + 3 типа ошибок + урок | — |
| s22 Allen MICrONS | **Да** | 1 мм³ = 84k нейронов; ground truth = U-Net + transformer | — |
| s25 WE-TESS | **Да** | 5-шаговая рамка universal для любой Analyse-фазы | — |
| s28 WE-2 bibliography | **Да** | 4 шага проверки + decision tree | «Стоимость: X мин» — это task-cost, не lecture timing, но «мин» сбивает с толку |
| s29 Frontiers «крыса» | **Да, частично** | «PROTEMNS», «ZXPENS», «CELLLS» (cut-off!) на figure | **(методологически)** в visible body label + текст «CELLLS» обрезан |
| s30 NeurIPS fake | **Да** | 21,575 → 5,290 → 100+ fake — strong stats | Chart legend показывает `undefined` — мелочь |
| s31 ICMJE policies | **Да** | Comparison matrix journals — straight read | — |
| s33 4 категории | **Да** | Когда AI не нужен — quadrant с примерами | — |
| s34 WE-3 catalyst | **Да** | Cascading workflow GP-BO → DFT → лаба | Slide визуально мелкий (см. §6) |
| s35 5 альтернатив | **Да** | BO+GP, DFT+MD, классическая статистика, OR — десятки лет работают | — |
| s36 3 вопроса | **Да** | Vendor questionnaire — практический artifact | — |
| s37 RU контекст | **Да** | AIRI, Sber, Yandex + Указ 490/124 | — |
| s38 Q&A | **Да** | Recap лестницы + reality summary | — |
| s39 Closing hero | **Да, частично** | AlphaFold DB hero + bridge к Лекции 16 | **[VFY-day-of]** в visible body assertion |

---

## 3. Speaker Notes Contract Check (sample 10 of 39)

| Slide | Word count | Connected prose? | Scaffold leak? | Derived from chapter, не bullets? |
|---|---|---|---|---|
| s01 | 163 | ✓ readable narrative | 0 | ✓ derives chapter §0.2 hook |
| s05 | 194 | ✓ | 0 | ✓ |
| s08 | 196 | ✓ | 0 | ✓ |
| s13 | 179 | ✓ | 0 | ✓ |
| s17 | 222 | ✓ | 0 | ✓ — strong failure deep-dive |
| s22 | 259 | ✓ | 0 | ✓ |
| s25 | 262 | ✓ | 0 | ✓ — WE walked example |
| s30 | 277 | ✓ | 0 | ✓ |
| s33 | 276 | ✓ | 0 | ✓ |
| s39 | 225 | ✓ | 0 | ✓ closing |

**Sweep across all 39 notes:**
- Total notes word count: 8,668 words (median 220/slide, range 117-306)
- 0 «Лектору» / 0 «На этом этапе» / 0 «методически» в notes
- 0 timing markers «(5 мин)», «75 минут» в notes
- 0 layout descriptions («слева donut, справа bar»)
- Каждое заметка — readable connected prose, derived from chapter, не slide bullets rephrased

**Speaker notes contract: EXCELLENT.** Это лучшая часть deck.

---

## 4. Structural Blockers vs Notes-Fixable

### Notes-Fixable (none required for self-containedness — все 5 «частично» через 2 нед — visible body fixes ≤5min)

Actually нет slides требующих «add 150-200 слов в notes». Все 39 notes уже 150-306 words.

### Visible-Body P1 Leaks (5 minute edits each)

**Critical (P1, must fix):**
1. **s02:** «LO4 — назвать инструменты AI-в-науке по шести ступеням лестницы / LO5 — отличить прорыв от фабрики статей; LO6 — диагностировать конкретный кейс / LO8 — сформулировать "когда AI не нужен" и предложить альтернативу» — **LO коды видны студенту**. Через 2 нед эти коды для меня — шум. Replace с plain text целями: «После лекции вы умеете: назвать инструменты AI-в-науке по шести ступеням; отличить прорыв от фабрики статей; диагностировать конкретный кейс; сформулировать "когда AI не нужен"».
2. **s02 cover:** «Модуль 3 · **75 минут**» — TIMING на cover слайде запрещён по CLAUDE.md «No Timing / No Methodology in Slides». Replace на «Модуль 3» либо «Модуль 3 · Прикладные применения».
3. **s09:** «Nature submission **[VFY-day-of]**» — verification marker visible. Replace на «Nature submission (черновик в работе на момент лекции, см. свежие данные)» либо просто убрать.
4. **s29:** «Что произошло **(методологически)**:» — METHODOLOGY mark в visible body. Replace на «Что произошло:» без квалификатора.
5. **s39:** «**200 миллионов+ структур** [VFY-day-of] для всего UniProt» — verification marker on closing hero. Cleanup.

**Minor (P2, polish):**
- **s28:** «Стоимость: 5 мин / 15 мин / 5 мин / 20 мин» — task-cost (effort to do verification step) использует слово «мин». Семантически это content (не lecture timing), но через 2 нед я могу спутать с лекционным таймингом. Suggestion: rename «Усилие: ~5 / ~15 / ~5 / ~20 минут» либо просто «5/15/5/20 минут».
- **s29:** ««PROTEMNS» «ZXPENS» «CELLLS»» — последнее слово обрезано / выходит за границу box. Visual fix — увеличить box или уменьшить font size.
- **s30:** Chart legend показывает `undefined` (вместо подписи) — QuickChart artifact, fix label.
- **s27:** Chart bottom — категории подписаны мелким шрифтом, но через 2 нед я их игнорирую — графики дублируют масштаб карточек выше; в принципе ОК.

### Structural Cuts

**None recommended.** Все 39 слайдов содержат значимый контент. Failure cluster §4 (5 слайдов s27-s31) — overwhelming в первый раз, но через 2 нед самоповторения digestible.

---

## 5. 30-Minute Reading Test — 5 Headline Learnings

Прохожу deck за 30 мин. Что я бы извлёк как top-5 learnings:

1. **Научный цикл — это шесть ступеней (Hypothesis → Design → Experiment → Analyse → Write → Review), и AI работает на каждой по-разному**: расширение на 1-2; нобелевский прорыв на 3; зрелое узкое ML на 4; расширение с проверкой на 5; запрещён для финального решения на 6. Эта лестница цикл, не прямая.

2. **AlphaFold 2024 Нобель ≠ Galactica 2022 retraction.** Та же базовая технология. Прорыв или фабрика статей зависит от: закрытый/открытый мир + наличие эталонной разметки + готовность человека в петле.

3. **Sakana AI Scientist v2: 100 черновиков → человек отбирает 3 → рецензент пропускает 1. Это не автономная наука — это AI-augmented черновик с тяжёлым человеческим фильтром.** 4 структурные проблемы: cherry-picking, галлюцинированные ссылки, фальсифицированные результаты, преувеличенная новизна.

4. **5-шаговая рамка решения «применять / не применять AI» + 3 вопроса к поставщику** = универсальный artifact: классифицируй задачу (открытый/закрытый мир) → проверь покрытие обучающего распределения → спроектируй шлюзы человека в петле → проверь до публикации (DOI / GPTZero / запрос исходных) → раскрой использование (ICMJE compliance).

5. **«AI не нужен» — 4 категории + 5 зрелых альтернатив**: открытый мир без эталона / недопредставлен в обучении / нельзя проверить независимо / этический риск. Альтернативы: BO+GP (40 лет), DFT+MD (60 лет), классическая статистика (век), OR/Simplex (78 лет), peer review. Эти методы — основные, не «запасные».

**Bonus learning извлекаемое (если читаю медленнее):** «Walked examples» WE-1 (грант), WE-TESS (экзопланеты), WE-2 (LLM-библиография соавтора), WE-3 (катализатор) — это шаблоны, применимые к любой моей задаче в магистратуре. WE-2 особенно ценный — описывает социально неудобный, но профессионально критический сценарий.

---

## 6. Hero Slides Accessibility

### s01 (hook, AlphaFold + Galactica composite)
- **Работает self-contained.** Composite side-by-side читается визуально: левая половина — Нобелевская церемония 10 декабря 2024 (Hassabis, Jumper, Baker); правая — заголовок MIT Tech Review 18 ноября 2022 «Why Meta's Galactica only survived three days online».
- Bridging assertion ниже: «AlphaFold взял Нобель. Galactica прожила три дня. Различать — задача инженера.»
- Дата выходит за box (caption attribution), но в notes 163 слова narrative — full context.
- **Через 2 нед я помню**: «было два события 2022 и 2024, оба важны, инженер должен различать». ✓

### s39 (closing, AlphaFold DB hero)
- **Работает, но с P1 leak.** Hero — alphafold.ebi.ac.uk screenshot ≥40% area. Caption «200 миллионов структур». Bridge к Лекции 16: нефтегаз = частично закрытый (геофизика) + частично открытый (резервуар).
- **Leak:** «200 миллионов+ структур [VFY-day-of]» — VFY-маркер видно.
- **Через 2 нед я помню**: «AlphaFold DB — отправная точка, не конец; финальная карта далека. Следующая лекция — нефтегаз». ✓

### s01 vs s39 как visual anchor pair
Парность работает: открываем с тезиса «различить два класса» (AlphaFold vs Galactica) → закрываем с тезиса «AlphaFold DB — отправная точка, мост в нефтегаз». Эмоциональная арка читается.

---

## 7. Walked Examples Re-Traceability (через 2 нед)

| WE | Slide | Steps | Re-traceable solo? |
|---|---|---|---|
| WE-1 Grant idea | s07 | 6 шагов: classify → coverage → verification → ethics → HITL → submission | **Да** — flow diagram + numbered cards читается без лектора |
| WE-TESS Exoplanets | s25 | 5 шагов: data overlap → label availability → GPU cost → AUC baseline → held-out validation | **Да** — конкретные numbers (8000+ Kepler labels, 1976 BLS baseline 78%) — easy recall |
| WE-2 Bibliography | s28 | 4 шага: DOI-resolve → relevance → GPTZero → request sources + decision tree | **Да** — самый эмоционально якорный пример (соавтор-старший); decision tree читается |
| WE-3 Catalyst | s34 | Cascading: GP-BO 5000 → DFT 50 → лаба 3 → 4 месяца vs год | **Частично** — slide визуально мелкий (zoomed-out layout); чтобы понять каскад, мне нужно перечитать notes 288 слов; визуал недостаточно self-explanatory |

WE-3 — единственный walked example где slide визуальный сам по себе слабее. Notes спасают. Если бы я скипнул notes — потерял бы 5000 → 50 → 3 cascade structure.

---

## 8. Failure Cluster §4 Digestibility (Write+Review)

Раздел §4 содержит 5 failure-heavy slides s27-s31 (NotebookLM расширение / WE-2 bibliography / Frontiers крыса / NeurIPS fake citations / ICMJE policies). 

**Через 2 нед reading test:** этот блок читается за 8-10 мин и оставляет clear take-away — «AI в Write фазе работает с проверкой каждой ссылки, в Review фазе финально запрещён». Не overwhelming благодаря:
- WE-2 (s28) как actionable artifact (4 шага проверки)
- Frontiers + NeurIPS (s29, s30) как vivid examples
- ICMJE matrix (s31) как cleanup summary

**Один блокер:** s29 visual artifact «CELLLS» обрезан + label «(методологически)» в visible body. Мелочи, но через 2 нед именно эти артефакты мне будут резать глаз.

---

## 9. Vocabulary Check (через 2 нед)

15 терминов в s04 glossary table — отлично, я могу back-reference сюда из любого slide. **Это core asset deck.** Tерм first-appearance в slide должен быть definable из glossary, и так и есть для:
- foundation model, RAG, hallucination, peer review, reproducibility crisis, closed/open world, IDP, ground truth, CASP, DFT/MD, BO/GP, ECMWF, FrontierMath, ICMJE, IMO, paper mill, HITL — всё в s04.

**Что вне glossary, но используется в visible body deck:**
- s28: «GPTZero» — не в glossary, defined inline («детектор LLM-стилистики»)
- s23: «conformal prediction» — defined inline на slide
- s09: «multi-agent debate» — на slide есть архитектура, but термин не unpacked. Если я через 2 нед смотрю только s09 — мне непонятно «generator + critic + ranker» что значит. Но в notes 182 слова это раскрыто.

**Vocabulary score: STRONG.** s04 glossary — лучший asset курса для self-study.

---

## 10. Top 5 Polish Recommendations

1. **s02 cleanup (P1, ~2 min)**: убрать `LO4/LO5/LO6/LO8` коды из visible body «Цели лекции», replace на plain-text formulations. Убрать `75 минут` из meta. Это два nearby violations CLAUDE.md «No Timing / No Methodology / No LO codes in visible body».

2. **s29 cleanup (P1, ~2 min)**: «(методологически)» → убрать parenthetical. Replace «Что произошло (методологически):» на просто «Что произошло:» или «Что произошло — что было раскрыто и где сбой:». Fix box width / font size чтобы «CELLLS» не обрезалось.

3. **s09 + s39 [VFY-day-of] cleanup (P1, ~1 min each)**: убрать `[VFY-day-of]` markers из visible body на обоих слайдах. Это leak из frontmatter в визуальный layer — несоответствует «No Extra Content / Scaffold Leaks» rule. Если число действительно volatile — replace «200M+ структур» (без даты), либо «200M+ по состоянию на момент лекции».

4. **s30 chart label (P2, ~3 min)**: legend показывает `undefined` — fix QuickChart series name. Сейчас выглядит как unfinished rendering artifact.

5. **s28 «мин» wording (P2, ~3 min)**: «Стоимость: 5 мин / 15 мин / 5 мин / 20 мин» формально не нарушает rule (task-cost, не lecture timing), но через 2 нед сбивает. Replace «5/15/5/20 минут» либо «Усилие ~X минут».

**Cumulative cleanup time: ~12-15 минут** для всех 5 P1+P2 polish items. Никакого revise; никаких rerenders.

---

## 11. Сводка

- **Слайдов self-contained: 32 / 39** (через 2 нед PNG + notes без лектора)
- **Self-containedness ratio: 82%** (ниже 85% production threshold, но в diapasone APPROVE-WITH-POLISH 25-32/N)
- **Слайдов нужна доработка: 5** (s02, s09, s28, s29, s39 — все visible body leak fixes, 0 нужно перестраивать структуру)
- **Структурных cuts: 0**
- **Speaker notes quality: EXCELLENT** — 39/39 в 117-306 words connected prose, 0 scaffold leaks, derived from chapter
- **Walked examples re-traceability: 3/4 strong, 1/4 (WE-3) частично notes-dependent**
- **Vocabulary coverage: STRONG** — s04 glossary 15 терминов как core self-study artifact
- **Hero slides accessibility: PAIR WORKS** — s01 + s39 как opening/closing anchors с emotional bridging arc; minor [VFY-day-of] leak на s39

**Final verdict: APPROVE-WITH-POLISH.** Deck is showable; 12-15 min polish lift к APPROVE-CLEAN. После cleanup s02/s09/s29/s30/s39 я как студент через 2 нед перечитываю deck за 30 минут, extract 5+ headline learnings, могу применить 5-step framework к собственной магистерской задаче. Это успешный self-study artifact.

---

## Annexe — Vocabulary Issues Per CLAUDE.md Check

- 0 terms without inline definition в visible body что мне нужно искать elsewhere (s04 glossary покрывает 15 core; inline defs для GPTZero, conformal prediction, multi-agent debate в notes)
- 0 «как мы обсудили / как я сказал» отсылок к utratchennoj live speech
