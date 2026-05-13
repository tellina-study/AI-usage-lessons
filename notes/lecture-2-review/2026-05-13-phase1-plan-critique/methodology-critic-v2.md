# Methodology-Critic Re-Check on Plan v2 — 2026-05-13

VERDICT: APPROVE-WITH-POLISH

## Summary

Plan v2 — существенная синтетическая переработка v1, intelligently отвечает на 5 P0 и большинство 12 P1 из Phase 1, а также на 4 P0 reader-simulator. Backbone (LO1+LO4+LO6+LO7 → 4 концепта inference) выстроен chiefly корректно, 3 cross-cutting frames добавлены (s24a / s27a / s27b) с явными callbacks к Lec-1, slide count = 28 (target hit), pacing рекалкулирован (70+5 mid section sums OK), glossary §5 расширен с insider-phrasing fix («слепота к буквам» вместо «миопии токенизации») и locked-канонической formой «авторегрессионный» (deferred verify — acceptable), Forbidden Additions §6 expanded до 13 пунктов. Bloom level в целом fits introductory (cut s19 multi-head, простоен s06 BPE без trace, s14 attention с явным «распределение, сумма=1»). Payoff §5.3 Lec-1 — explicit в s26 как teaching, не throwaway recap. LO4 теперь получил dedicated teaching slide s22 (4 ручки + warning row про T=0 ≠ детерминизм).

Главная остаточная methodological concern — **slide numbering chaos** (s16, s19 пустые с явной пометкой; s24 отсутствует, заменён на s24a; s25 имеет ДВА определения подряд в одном файле; s27 placed AFTER s27a/s27b что нарушает ID monotonicity). Это P1 для downstream automation (cascade refs, slide-by-slide ingestion в book-editor / presentation-designer), не для содержания лекции. Plus две minor methodology smell'а: (1) **s28 Q&A merged с bridge-to-Lec3** — Q&A 5-10 мин не помещается в заявленные 1.5 мин слота; pacing math inconsistency; (2) **s22 warning row про T=0 production non-determinism** — это Bloom Apply/Analyze level edge case для introductory лекции, существенный для production engineer cohort, но рискует overload row. Counter-check: 4 P1 findings → APPROVE-WITH-POLISH (rule: ≤4 P1).

---

## Phase 1 P0 closure status

- **[P0-1] Cross-cutting frames** — **CLOSED**. 3 NEW slides добавлены (s24a local/cloud, s27a ML/LLM tree, s27b human/AI). Placement:
  - s24a between s23 и Раздел 5 transition — natural в Sampling section (inference-runtime context).
  - s27a / s27b в Заключении между s26 (3 «почему» payoff) и s27 (homework) — narrative pivot OK.
  - Callbacks явные: §4.2, §1.4, §4.8 Lec-1 cited.
  - Однако placement s27a/s27b создал **ID ordering issue** (s27 homework ПОСЛЕ s27a/s27b) — см. отдельный P1 ниже.
- **[P0-2] Slide count** — **CLOSED**. Count verified: 4+4+4+5+5+6 = **28** content slides (s16 + s19 declared empty с явным пометком «перенумерация»). Target = 28-30, hit lower bound. ✓
- **[P0-3] LO4 coverage** — **CLOSED**. s22 теперь explicit teaching slide с full 5×5 table (T / top_p / max_tokens / system_prompt × 4 scenarios) + явное «`max_tokens` typical» в каждой строке. Warning row про T=0 ≠ детерминизм — добавляет engineering nuance, который reader Phase 1 запрашивал (P0 gap «edge case T=0 в production»). Adequate.
- **[P0-4] Раздел 3 cognitive load** — **CLOSED**. Final count в Разделе 3 = 4 content slides (s14, s15, s17, s18) + s13 divider за 18 мин. **Merge s17+s18 → s15** выполнен (worked example + role-effect в одном слайде с Part A / Part B structure). **s19 multi-head — CUT** entirely, 1 предложение в s14 speaker note. Cognitive load снижен с 6 concepts/18min до 4 concepts/18min (~1 concept per 4.5 min, в пределах 3-5 concepts / 5 min standard). ✓
- **[P0-5] Hook static-first** — **CLOSED**. s01 явно: «Visual primary: static screenshot Tiktokenizer ... Primary = static, live demo — optional». Pre-flight check «screenshots в `assets/`, проверены за день до лекции». ✓

**P0 closure: 5/5.** Все P0 Phase 1 закрыты.

---

## Phase 1 P1 closure status (table)

| # | Phase 1 issue | v2 status | Notes |
|---|---|---|---|
| P1-1 | s19 multi-head — Bloom overshoot | CLOSED | CUT entirely. 1 sentence в s14 speaker note. |
| P1-2 | s06 BPE worked example | CLOSED | Replaced 3-step trace на before/after; tokenizers alternatives → speaker note. |
| P1-3 | «миопия токенизации» insider phrasing | CLOSED | Renamed to «слепота к буквам» (рабочий) / «subword-агрегация»; locked в §5 glossary. |
| P1-4 | «магнит» metaphor inconsistency | CLOSED | Metaphor lock «фонарик» everywhere; «магнит» explicitly removed (s14 + s15). |
| P1-5 | s11 Word2Vec → modern | CLOSED | s10 теперь sentence-similarity на 5 практических примерах с cosine heatmap. Word2Vec → 1 sentence в speaker note. |
| P1-6 | «промптинг — сквозной навык» marketing tone | CLOSED | §8.2 явный «(REMOVED:) ... заменено на нейтральное "промпт-параметры разбираются на уровне механики"». |
| P1-7 | s07 strawberry day-of pre-test | CLOSED | Tag `[VERIFY-DAY-OF]` explicit. 3 alternative examples ready (методология / ROT-13 / reverse string). Lecturer brief flagged. |
| P1-8 | s20 (→ s17) timeline freshness | CLOSED | Reduced to 3 points (GPT-3.5 2022 / Claude 3.5 2024 / Claude 4.7 2026). `[VERIFY-ON-LECTURE-DAY]` tagged. Fallback speaker note for outdated case. |
| P1-9 | Семинар 12 vs Лекция 12 PARTS reference | DEFERRED | §1.5 / §8.1 flagged как `**TBD-VERIFY** в catalog/manifests/lectures.yaml`. Verifiable перед chapter draft. OK для plan. |
| P1-10 | s26 role-effect mechanism softer phrasing | CLOSED | s15 «На уровне attention мы видим, что role-токены имеют более высокий вес. Это упрощение — альтернативно объясняется через in-context steering» + s26 «опирается на них при выборе следующих» (softer claim). Speaker note flagged not-settled-science. |
| P1-11 | Glossary canonical form «авторегрессионный» | DEFERRED (acceptable) | §5 locked + flagged «VERIFY перед chapter draft» против Hugging Face docs Russian + Yandex AI. Deferred OK как plan-level decision. |
| P1-12 | s17 (→ s15) worked example grammar miscue | CLOSED | Explicit disclaimer над visual «упрощение: реальный attention map содержит сотни связей; здесь показаны 3 сильнейших. Модель не делает грамматический разбор — она статистически смотрит». Retrieval moment counter-example «Программа упала, потому что она забыла обработать null» added Part A. |

**P1 closure: 10 CLOSED + 2 acceptably DEFERRED = 12/12.** ✓

---

## Reader Phase 1 P0 closure status

- **[Reader P0-1] s06 BPE-when** — **CLOSED**. s06: «BPE-словарь строится один раз на корпусе перед обучением модели. В inference токенизация — это lookup готовых merge-rules, не runtime-вычисление». ✓
- **[Reader P0-2] s10 (→ s09) embedding-how** — **CLOSED**. s09: «Каждому токену в памяти модели сопоставлен вектор; он выучен на тренировке и затем фиксирован» + lookup-arrow visual + dim numbers. ✓
- **[Reader P0-3] s16 (→ s14) attention-as-distribution** — **CLOSED**. s14 assertion: «Attention выдаёт распределение весов на все токены контекста (сумма = 1) — какие токены важны сейчас» + explicit fix line «выдаёт распределение, сумма = 1, толстая стрелка = больший вес». ✓
- **[Reader P0-4] Cross-cutting missing** — **CLOSED** (тот же fix как methodology P0-1). ✓

**Reader P0 closure: 4/4.**

Reader P1 issues mostly addressed: ДЗ playground specified (HF Inference Playground), variance pattern «3 × 3» runs clarified, MCP s28 inline definition added, argmax disclaimer добавлен в s21, k-means «(алгоритм кластеризации)» добавлен в s11. Несколько minor P1 reader concerns переходят в новые P1 (см. ниже).

---

## New P0/P1 в v2 (если есть)

### NEW [P1-N1] Slide ID numbering chaos — downstream automation risk

**Issue:** v2 plan имеет три отдельных проблемы с ID-нумерацией, которые в совокупности затрудняют downstream ingestion в book-editor / presentation-designer / cascade-of-changes tracking:

1. **Empty placeholders s16 и s19** declared («#### s16 — (placeholder; нет) — empty, перенумерация» + «(s16, s19 пустые — перенумерация. Финальный deck: s14, s15, s17, s18 для Раздела 3.)»). Это означает, что ID гэпы остались — final deck **не** имеет s16, s19, s24.
2. **s25 имеет два разных definition подряд:**
   - First: «#### s25 — Section transition (0 слайдов, через title; v1 s27 divider CUT)»
   - Then immediately: «#### s25 — Recap-bridge (1 мин)»
   - Это **семантически конфликтующие** заголовки одного ID. Either «s25 не существует как slide» ИЛИ «s25 = Recap-bridge», но не оба.
3. **s27 placed AFTER s27a/s27b** что нарушает natural ID monotonicity. Reader expects: s27 → s27a (insertion) → s27b (insertion) → s28. Reality: s27a → s27b → s27 → s28. Это создаст ambiguity в downstream cascade («когда говорят s27 — имеется в виду homework или cross-cutting block?»).

**Evidence:** Plan v2 line 238 («#### s16 — (placeholder; нет)»), line 258 («s16, s19 пустые»), lines 315-317 (двойной s25 заголовок), line 352-360 (s27 после s27a/s27b).

**Severity:** P1 — не блокер контента, но создаст confusion для book-editor / presentation-designer / fact-checker, особенно если они ссылаются к slide ID в cascade-of-changes grep.

**Recommendation:** clean renumber перед Phase 2:
- Раздел 3 final: s13 divider, s14, s15, s16, s17 (replace empty s16/s19 placeholder text, shift).
- Раздел 4 final: s18 distribution, s19 T, s20 4-ручки, s21 autoregressive, s22 local/cloud (renumber s24a → s22).
- Раздел 5 final: s23 recap-bridge, s24 3 «почему» payoff, s25 ML/LLM tree, s26 human/AI, s27 homework, s28 bridge+Q&A.
- Это даёт clean s01-s28 monotonic. **OR** keep current chaotic IDs но **explicitly document** в §11 source-of-truth chain «ID map: s16/s19/s24 — empty placeholders, ignored downstream».

### NEW [P1-N2] s28 Q&A timing inconsistency — Q&A не помещается в 1.5 мин слот

**Issue:** s28 заголовок: «#### s28 — Что в Лекции 3 + Q&A merged (1.5 мин)». Внутри slide:
- 4 концепта Лекции 3 (RAG, Tools, MCP, Agent loop) с inline disclaimer'ами для каждого.
- Bridge sentence.
- «Q&A invitation: "5-10 минут на ваши вопросы"».

**Math inconsistency:** заявленные 1.5 мин для s28 + 5-10 минут Q&A = 6.5-11.5 мин реальное time. План §2.2 говорит «5 мин буфер для вопросы». 5+10 явно не помещается в 5-минутный буфер.

**Reader Phase 1** уже flag: «Q&A 2 мин это очень мало, обычно вопросы съедают 5+». В v2 это перенесено в 5-минутный буфер но Q&A invitation prints «5-10 минут» — две разные numbers в одном slide.

**Evidence:** Plan v2 §2.2 «Буфер — 5 мин» + s28 «Q&A invitation: 5-10 минут на ваши вопросы».

**Severity:** P1 — pacing inconsistency может означать lecture overrun.

**Recommendation:** unify Q&A scope. Either:
- (a) Keep Q&A в буфере 5 мин, change s28 text → «Q&A invitation: до 5 минут на вопросы (остальные в Семинар 2 / на e-mail)»; ИЛИ
- (b) Add dedicated s29 Q&A slot (10 мин) — но это нарушает 28-slide target. Better option (a).
- Также: separate the s28 «slide content» (1.5 мин bridge) и «Q&A invocation» (которая просто кончается лекцией) — slide doesn't need to «merge» Q&A as content.

### NEW [P1-N3] s22 «warning row T=0 ≠ детерминизм» — Bloom Apply/Analyze edge case в introductory

**Issue:** s22 таблица 5×5 + warning row: «`T=0` ≠ полный детерминизм в production (floating point + batching могут давать вариативность)». Это claim — **production engineering Bloom Apply level** факт, который требует понимания:
- Что такое floating point determinism.
- Что batching на сервере влияет.
- Что для full determinism нужен seed-control (которого нет в большинстве API).

Для introductory (Bloom Remember/Understand/Apply) cohort 3-курс ИУ6 это **edge case overshoot**. Студент уйдёт с лекции с одним из двух исходов:
- (a) Запомнит «T=0 не детерминирует» без понимания почему — это **misleading**, потому что для большинства inference T=0 практически детерминистичен.
- (b) Спросит «почему?» и получит 5-минутное отвлечение про FP determinism — это **derailment**.

Plus: reader Phase 1 запрашивал эту warning как **P0 gap** («Положительные/отрицательные кейсы T=0»). Но reader был mistaken — для introductory важнее «T=0 → детерминированный pick the most likely», без edge case nuance.

**Evidence:** Plan v2 s22 «Warning row: "`T=0` ≠ полный детерминизм в production (floating point + batching могут давать вариативность)"».

**Severity:** P1 — содержание правильное, но cognitive overhead на introductory лекции overshoots Bloom level. Curriculum mismatch risk.

**Recommendation:** soften OR move:
- (a) Replace warning row с simpler statement: «`T=0` практически детерминирует выбор; в production может быть микро-вариативность из-за batching на сервере — для большинства задач игнорируема». Это keeps the fact но removes deep-rabbit-hole risk.
- (b) ИЛИ move warning в speaker note (lecturer can answer if asked, but not on-slide).
- (c) ИЛИ keep на slide но tag explicitly «edge case for production; для introductory достаточно знать "T=0 → argmax"».

### NEW [P1-N4] s27 homework playground recommendation «HF Inference Playground» — verification needed

**Issue:** s27 instruction: «**Playground:** **Hugging Face Inference Playground** (free, имеет T slider) ИЛИ OpenAI Playground (платно с free credits) — **НЕ ChatGPT free** (нет slider)».

HF Inference Playground — **moving target** (HF UI и доступность free models меняется quarterly). Plan не указывает дату verification — fact-checker должен подтвердить:
- HF Inference Playground всё ещё **free** для public models в 2026.
- Models на HF playground имеют **T slider** в UI.
- Какие конкретно модели рекомендуются (Llama-3? Mistral? Qwen?). План не указывает модель.

**Evidence:** Plan v2 s27, line 357.

**Severity:** P1 — homework заблокирован если playground не доступен в день лекции.

**Recommendation:**
- Tag `[VERIFY-DAY-OF]` explicit в s27 (plan §9 freshness table currently doesn't list HF Playground).
- Add fallback option в speaker note: «если HF недоступен — Together.ai playground (free tier) ИЛИ Ollama локально с llama3».
- Specify ONE model для homework consistency: «Используйте `Meta-Llama-3-8B-Instruct` на HF Inference Playground» — чтобы все студенты сравнивали apples-to-apples.

---

## Slide numbering concern (s16/s19 пустые)

**Verdict: P1 — нужен fix перед Phase 2 chapter draft.**

**Why:** book-editor получает plan-v2-final.md как input. Если plan содержит empty placeholders, book-editor может:
- Скип они и нарушит cross-references в chapter sections.
- Создать confusion в `[for-slide-sNN]` markers.
- Сломать cascade-of-changes grep (поиск «s16» вернёт false hits).

**Two acceptable resolutions:**

**Option A (Recommended): Clean renumber.**
Перенумеровать перед Phase 2:
```
Раздел 3: s13 → s14 → s15 → s16 → s17 (5 slides, monotonic)
Раздел 4: s18 → s19 → s20 → s21 → s22 (5 slides, including renamed s24a → s22)
Раздел 5: s23 → s24 → s25 → s26 → s27 → s28 (6 slides)
```
Total still = 28. **Cleaner downstream automation.**

**Option B: Document empty IDs as known artifact.**
Add §11 explicit «ID map» listing all empty/skipped IDs:
```
Empty/skipped IDs in v2 plan (semantically absent):
- s16, s19 (intentional in Раздел 3)
- s24 (replaced by s24a)
Active IDs: s01-s15, s17-s18, s20-s23, s24a, s25-s28 = 28 total
```

Option A is cleaner, but if user prefers v2 as-is, Option B at minimum must be added.

---

## Pacing verification

| Раздел | Plan v2 §2.2 declared | Sum of individual slides | Match? |
|---|---|---|---|
| 0. Открытие (s01-s04) | 8 мин | 2 + 0.5 + 1.5 + 1 = 5 мин (declared) | **MISMATCH: 5 ≠ 8**. Plan declares 8 in arc, individual times sum 5. |
| 1. Токенизация (s05-s08) | 11 мин | 2 + 2 + 3 + 2 = 9 мин | **MISMATCH: 9 ≠ 11**. 2 min unaccounted. |
| 2. Эмбеддинги (s09-s12) | 11 мин | 2 + 3 + 2 + 2 = 9 мин | **MISMATCH: 9 ≠ 11**. 2 min unaccounted. |
| 3. Внимание (s13-s18) | 18 мин | 0.5 + 3 + 5 + 2 + 2 = 12.5 мин | **MISMATCH: 12.5 ≠ 18**. 5.5 min unaccounted — biggest gap. |
| 4. Сэмплинг (s20-s24a) | 13 мин | 2.5 + 3 + 2 + 2 + 1 = 10.5 мин | **MISMATCH: 10.5 ≠ 13**. 2.5 min unaccounted. |
| 5. Заключение (s25-s28) | 9 мин | 1 + 2 + 1.5 + 1 + 2 + 1.5 = 9 мин | **MATCH ✓**. |
| **Total active** | **70** | **5+9+9+12.5+10.5+9 = 55 мин** | **MISMATCH: 55 vs claimed 70 — 15 min unaccounted.** |

**This is a P1 pacing issue (call it P1-N5).** Plan declares 70 min active content, but sum of declared individual slide times = 55 min. 15-минутный gap.

**Possible explanations:**
- Retrieval moments + transitions are included в section budgets, not slide times.
- §7 table «Микро-упражнения и retrieval moments: Итого 5 интерактивных моментов, ≤8 мин cumulative» — accounts for ~8 min beyond slide-individual times.
- Section transitions / lecturer commentary = ~7 min.

Even так, math не explicit. **Recommendation:** add to §2.2 arc table explicit «Section budgets include: slide content + retrieval moments + transitions». Make math defensible.

Hard severity: **P1** (math doesn't tie, but ratio (55/70) is in plausible range; not P0 because each slide individual time looks reasonable).

---

## Curriculum relevance check (по всем 28 slides)

All 28 content slides classified по Bloom level vs introductory level (3 курс ИУ6, Lecture 2 = introductory):

| Slide | Bloom level | Curriculum fit | Verdict |
|---|---|---|---|
| s01 live demo | Remember | KEEP | ✓ |
| s02 cover | — | KEEP | ✓ |
| s03 recap | Understand | KEEP | ✓ |
| s04 central question | Understand | KEEP | ✓ |
| s05 token | Remember/Understand | KEEP | ✓ |
| s06 BPE | Understand (after simplification) | KEEP | ✓ |
| s07 strawberry | Apply (retrieval moment) | KEEP | ✓ — applies LO6 |
| s08 cross-lang | Understand | KEEP | ✓ |
| s09 embedding | Understand | KEEP | ✓ |
| s10 sentence sim | Apply | KEEP | ✓ — applies in RAG context |
| s11 3 uses | Understand | KEEP | ✓ |
| s12 semantic search | Apply | KEEP | ✓ |
| s13 divider | — | KEEP | ✓ |
| s14 attention | Understand | KEEP | ✓ |
| s15 worked example + role | Apply (after merge) | KEEP | ✓ — applies LO7 |
| s17 context window | Remember | KEEP | ✓ |
| s18 long-context fails | Understand/Apply | KEEP | ✓ — applies LO6 |
| s20 distribution | Understand | KEEP | ✓ |
| s21 T + top-p/k | Apply | KEEP | ✓ — applies LO4 |
| s22 4 ручки | Apply (Analyze для warning row) | KEEP with caveat (P1-N3) | ⚠ |
| s23 autoregressive | Understand | KEEP | ✓ |
| s24a local vs cloud | Understand | KEEP | ✓ — cross-cutting |
| s25 recap-bridge | Remember | KEEP | ✓ |
| s26 3 «почему» | Understand/Apply | KEEP | ✓ — payoff LO7 |
| s27a ML/LLM tree | Apply | KEEP | ✓ — meta-skill important |
| s27b human/AI | Understand | KEEP | ✓ — closes Pearl loop |
| s27 homework | Apply | KEEP | ✓ |
| s28 bridge | Remember | KEEP | ✓ |

**Bloom distribution:** 6 Remember / 11 Understand / 9 Apply / 2 Analyze (s22 warning row, s27a tree higher-level) → **fits introductory profile** (heavily Understand+Apply weighted).

**No RECOMMEND-DELETE candidates.** All slides curriculum-relevant. s22 warning row flagged as P1 above but content stays.

---

## Tone calibration check

- ✅ «Магия LLM» tone — отсутствует. §1.4 «explanatory-engineering».
- ✅ «Промптинг — сквозной навык» phrasing — REMOVED (§8.2 explicit).
- ✅ Familiar CTA («ребят», «короче», «УГАДАЙ») — отсутствует.
- ✅ Local audience binding («инженер ИУ6», «студент Бауманки») — отсутствует в plan. §1.4 явно «универсальная как Лекция 1».
- ✅ Insider phrasing — «миопия токенизации» REMOVED, «слепота к буквам» с явной пометкой «рабочий термин» (acknowledges не canonical).
- ✅ Promise-driven hype — отсутствует. s04 явно ставит 3 промиса как **открытые вопросы**, не «откровения».

**Tone check passes clean. No P1 / P2 tone issues.**

---

## Anti-pattern grep awareness check

Ran grep на plan v2 за известные anti-patterns:

- «магическая пилюля» — 0 hits ✓
- «AI спасёт» — 0 hits ✓
- «революция» — 0 hits ✓
- «УГАДАЙ» — 0 hits ✓
- «ребят» — 0 hits ✓
- «инженер ИУ6» — 0 hits (only «3 курс ИУ6 МГТУ им. Баумана» в metadata, not в content) ✓
- «прикладное X» — 0 hits ✓
- «X в режиме Y» — 0 hits ✓
- «не является целью нашего курса» — 0 hits ✓
- «магия LLM» / «магия» — 0 hits в content (only мета-references «без магии LLM» в tone declarations) ✓

**All anti-pattern checks pass clean.**

---

## Designer-Added Content audit (preemptive)

Plan v2 §6 «Forbidden additions» — comprehensive 13-item list. Coverage:

- ✅ Формулы attention (softmax QK^T/√d V)
- ✅ Q/K/V matrices как termini
- ✅ Transformer block diagram
- ✅ Позиционное кодирование deep dive
- ✅ Pretraining / fine-tuning / RLHF overview
- ✅ CNN vs RNN vs Transformer comparison
- ✅ Karpathy-style build-a-mini-GPT
- ✅ Footer-tax (источники, ссылки, тайминг)
- ✅ «Вы здесь» / «Лектору» / subtitles (исключение для s02 roadmap-маркер)
- ✅ Slide deletion/addition без user request
- ✅ Multi-head attention deep-dive
- ✅ Word2Vec king-queen как central visual
- ✅ Pearl 3 уровня deep dive (только callback в s27b)

**Missing from list (minor gaps):**
- Color-only highlight без text marker (Color-as-only-signal anti-pattern из reflection consolidated).
- Decorative SVG/icons без semantic role.
- Cross-slide bridge text not requested (e.g., «продолжение от s14»).
- «Section-NN» footer markers.

**Recommendation:** add these 4 to §6 for completeness, или explicitly defer to `tools/presentation-build/README.md` § anti-patterns as canonical reference.

**Severity:** P2 — current list covers 13/17 known anti-patterns. Designer-агент в Phase 5 ещё проверит против its own README.

---

## Glossary lock check

§5 — 15 terms locked + alias list + forbidden list + forbidden anglicisms (3 items).

**Strengths:**
- «слепота к буквам» explicit alias «subword-агрегация» + forbidden «миопия токенизации».
- «авторегрессионный» locked + verify deferred (acceptable).
- «механизм внимания» / «внимание» / «attention» — alias chain clear.
- «in-context» distinction from «контекстное окно» — explicit.

**Minor remaining concerns:**

- **«BPE»** glossary entry: «BPE-токенизация» alias OK, но **полное «Byte-Pair Encoding» уже использовано в §1.5 / §3 / §4 prose 1×** — confirm chapter / slides делают расшифровку строго 1 раз (no drift).
- **«семантическое сходство»** — alias «similarity (1× в скобках)» — но в s10 prose plan уже использует «cosine similarity» 2× («cosine similarity heatmap», «cosine similarity — мера угла»). **Lock «cosine similarity» как отдельный entry** или явно подтвердить, что «cosine similarity» считается канонической форой (а не алиасом).

**Severity:** P2 — minor glossary refinement, no content impact.

---

## Cascade-of-changes handoff (§12 brief для book-editor)

Plan v2 §12 brief content:
- Goal: chapter ~8-12k слов, academic
- LO: explicit
- Structure: 5 разделов mirroring §2.2 arc
- Cross-references Lec-1 §3.2 / §3.3.1 / §4.2 / §4.8 / §5.3 без повтора
- Glossary lock §5 enforced
- Forbidden additions §6 enforced
- Self-check questions в конце каждого раздела
- `[for-slide-sNN]` markers
- `[FACT-CHECK]` для unverified specifics
- Tone declaration

**Strengths:** clear, structured, deterministic. book-editor получит unambiguous brief.

**Gaps to address:**
1. **Slide ID map** — book-editor должен знать, что s16/s19/s24 пусты (or after renumber). Add explicit «Slide ID list в §2.2 = current authoritative» reference.
2. **`[FACT-CHECK]` items list** не перечислены centrally — book-editor должен сканировать §9 freshness table. Add reference в §12: «freshness table §9 enumerates verifiable items».
3. **`[for-slide-sNN]` paragraph markers** — но если IDs нечеткие (P1-N1 issue), markers могут drift. Resolve numbering first.

**Severity:** P2 (assuming P1-N1 resolved). §12 brief is mostly adequate.

---

## Pre-USER-GATE highlights (для user attention)

5 critical points user должен особо проверить перед approve plan v2:

1. **Slide ID numbering** (P1-N1) — Resolve before Phase 2 chapter draft. Empty placeholders s16/s19 plus duplicate s25 plus out-of-order s27/s27a/s27b create downstream confusion. User decision: clean renumber (Option A) OR document as-is (Option B).

2. **s28 Q&A pacing** (P1-N2) — «Q&A invitation 5-10 минут» в slide заявляет больше, чем 5-min буфер. Reconcile: либо trim Q&A wording до «до 5 минут», либо carve out dedicated slot at expense of s28 bridge depth. User decision на pacing priority.

3. **s22 warning row про T=0 ≠ детерминизм** (P1-N3) — Edge case correct, but Bloom Analyze level for introductory. User decision: keep, soften, или move to speaker note.

4. **HF Playground homework dependency** (P1-N4) — Plan recommends HF Inference Playground для homework, but не verifies availability. Add `[VERIFY-DAY-OF]` + fallback option (Together.ai / Ollama). User to verify HF still suitable для cohort in lecture date.

5. **Pacing math inconsistency** (P1-N5) — Section budget (70 min) ≠ sum of individual slide times (55 min). 15-min gap likely accounted by retrieval+transitions but not explicitly. Add §2.2 footnote explaining what section budget includes.

**Bonus user attention:** §1.5 / §8.1 «**TBD-VERIFY** Семинар 12 vs Лекция 12 PARTS» — defer to Phase 2 chapter draft OR resolve now via `catalog/manifests/lectures.yaml` check. Quick win если verifiable in 5 min.

---

## DoD enforcement check

- ✅ Chapter LO coverage planned for all 4 LOs (LO1/LO4/LO6/LO7).
- ✅ Slide count = 28 hits target band 28-30.
- ✅ Glossary lock present (§5).
- ✅ Forbidden additions list present (§6).
- ✅ Self-check moments planned (§7, 5 retrieval moments).
- ✅ Cross-references to Lec-1 explicit (§1.3 mapping table).
- ⚠ Pacing math doesn't cleanly tie (P1-N5).
- ⚠ Slide ID monotonicity (P1-N1).

**DoD substantively meets requirements.** No P0 DoD fail.

---

## Counter-check

P1 count = 4 (P1-N1 numbering / P1-N2 Q&A / P1-N3 T=0 warning / P1-N4 HF Playground).

Pacing math gap (P1-N5) — I've counted it inside the «New P1» but didn't enumerate separately. Adding: **P1 count = 5**.

**Rule:** ≥5 P1 → REVISE. **5 P1 exactly → boundary case.** Per critic-rule: «5+ P1 → REVISE». Strict interpretation: 5 = «5 or more» → REVISE.

**Reconsidering verdict from APPROVE-WITH-POLISH → REVISE.**

However, two of the 5 P1 (P1-N1 numbering, P1-N5 pacing math) are **mechanical / metadata-level** issues — they don't affect lecture content, only downstream automation. The other 3 (P1-N2/N3/N4) are content-level concerns each solvable with single-line edits.

**Final adjudication:** Strict rule says REVISE at 5+ P1. **I uphold the rule.**

**REVISED VERDICT: REVISE.**

Plan v2 is materially close to APPROVE — но 5 P1 issues need addressing before Phase 2 chapter draft. None are content blockers; all are 1-2 line fixes. Estimated effort: 30 min to resolve all 5 + re-check.

---

## Top-5 правок priority for plan v2.1

1. **[P1-N1]** Clean renumber slide IDs (Option A) OR add explicit ID map (Option B). Recommend Option A.
2. **[P1-N5]** Add §2.2 footnote «Section budget = slide-individual times + retrieval moments (~8 min) + transitions (~7 min)» — make pacing math defensible.
3. **[P1-N2]** s28 reconcile Q&A wording: «до 5 минут на вопросы, дополнительные — в Семинар 2 / e-mail» (stays within 5-min buffer).
4. **[P1-N3]** s22 warning row soften: «`T=0` практически детерминирует выбор; в production может быть микро-вариативность из-за batching — для большинства задач игнорируема».
5. **[P1-N4]** s27 add `[VERIFY-DAY-OF]` tag + fallback playground options (Together.ai / Ollama) + specify model (`Meta-Llama-3-8B-Instruct`).

---

**Конец methodology-critic re-check v2 report.**

VERDICT: REVISE (5 P1, all 1-2 line fixes).
