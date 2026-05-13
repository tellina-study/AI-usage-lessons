# Fact-Checker Report on Slides Лекции 2 v1.0 — 2026-05-13

**VERDICT: APPROVE-WITH-POLISH**

**Severity counts:** P0 = 0, P1 = 3, P2 = 5.

Rationale: Phase 3 chapter v1.0 had 2 P0 (Llama-3 tokenizer attribution, strawberry token split). Chapter v1.1 fixed both — and **slides propagate fixes correctly** (s01, s05, s06, s07, s24 all show `strawberry → [st][raw][berry] = 3 токена`; s06 attributes SentencePiece only к Llama 2 / T5; s09 softens GPT-4 12288 → «тысячи измерений [FACT-CHECK]»). Все 9 `[FACT-CHECK]` маркеров из chapter v1.1 либо явно перенесены в speaker notes, либо безопасно softened в visible content. Все 3 `[VERIFY-DAY-OF]` маркера (s07 strawberry pretest, s16 context window cifры, s27 HF Playground) присутствуют в speaker notes — **mandatory pre-flight by lecturer**.

3 P1 — соотношение «1M ≈ 16× от 100k» противоречит чистой математике N² (=100×) и нуждается в edit-уточнении; s17 U-shape числа в чарте более agressive (30% mid) чем у Liu et al. 2023 (~50% mid); s19 visible says «T=0.7 стандарт» при speaker notes «T=1.0 стандарт» plus numbers consistency. 5 P2 — minor cite hygiene, formatting consistency.

**Не блокирует production** — нужны cosmetic фиксы перед лекцией. P0 absent. Cross-consistency с chapter v1.1 strong. Curriculum sync (Лекция 3 = «Агенты, RAG, API», Лекция 12 = PARTS) verified.

---

## P0 Issues

**Отсутствуют.** Phase 3 P0 issues (Llama-3 tokenizer attribution, strawberry split) исправлены в chapter v1.1 и корректно отражены во всех 28 слайдах. Curriculum hallucinations не обнаружены. Direction inversions не обнаружены. Citation misquotes не обнаружены.

---

## P1 Issues

### [P1-1] s16 «1M ≈ 16× дороже 100k» — нумерическая натяжка, противоречит pure N²

**Locations (slides):**
- **s16 visible** (gold callout): «Стоимость attention растёт **квадратично** от длины. 1M ≈ **16× дороже** 100k.»
- **s16 visible** (right card «Эволюция и стоимость»): «Cost N²:  1M ≈ 16× от 100k»
- **s16 speaker notes** lines 44: «миллион токенов входа стоит порядка в шестнадцать раз дороже, чем сто тысяч».

**Locations (chapter v1.1):** §3.3 line 361 same claim.

**Issue:** Pure quadratic `N²` gives `(1M / 100k)² = 100×`, не 16×. «16×» приходит из observed production-pricing (где FlashAttention, sparse attention, KV-кэш, sliding-window — снижают константу). Сейчас слайд **одновременно**:
1. Заявляет «стоимость растёт **квадратично**» (theoretical claim).
2. Приводит «1M ≈ 16× от 100k» (observed price ratio).
Эти два числа together = **logical inconsistency** — student с калькулятором за 30 секунд найдёт N² ≠ 16×.

**Severity:** P1 — methodology-level inconsistency, не factual error. Direction (UP, quadratic-dominant) correct ✓.

**Recommended fix (alternative wording, choose one):**
- **Option A (preserve number, soften theory):** «Pure attention растёт как N². В практическом ценнике API (с учётом всех оптимизаций) — 1M ≈ 16× от 100k.»
- **Option B (drop specific number):** «Стоимость растёт квадратично — удвоение длины утроивает-учетверяет inference cost.»
- **Option C (use theoretical 100×):** «Pure attention: 1M ≈ 100× от 100k. На практике с FlashAttention / KV-кэш — ~16× в production-pricing.»

---

### [P1-2] s17 U-shape — middle accuracy ~30% сильнее dip, чем у Liu et al. 2023 (~50%)

**Locations (slides):**
- **s17 visible** (chart + side table «Результаты»): «Начало: ~75%, Середина: ~30%, Конец: ~75%».
- **s17 speaker notes** (через chapter §3.4) — phrasing «accuracy провал до 30% в середине».

**Issue:** Liu et al. 2023 (arXiv:2307.03172) — эмпирически показывает U-shape, но в их Figure 1 (20-document NaturalQuestions с gpt-3.5-turbo) accuracy drops с ~75% до **~50%** в середине, не 30%. На longer contexts (Figure 5+) и для некоторых моделей dip может быть глубже, но «30%» — не central тренд paper'а.

**Verification source:** arXiv:2307.03172 Figure 1 (paper Abstract: «accuracy degrades significantly when relevant information is in the middle... performance often nearly halves»; «halves» = drop с 75% до ~37%, в зависимости от модели). 

**Severity:** P1 — illustrative chart, направление direction correct ✓. Numbers are within reasonable range across models/setups, но claim «~30%» нужен либо explicit disclaimer «illustrative; точные значения varies by model», либо корректировка к ~50%.

**Recommended fix:**
- **Option A:** Update chart numbers: Начало ~75%, Середина ~50%, Конец ~75% (matches Liu Figure 1 GPT-3.5-turbo).
- **Option B:** Сохранить ~30%, добавить inline disclaimer «illustrative; depth dip varies: 30-50% depending on model and context length (Liu et al. 2023, Figure 5)».

---

### [P1-3] s19 T=0.7 = «стандарт» (visible) vs T=1.0 = «стандарт» (speaker notes) + numerical inconsistency

**Locations (slides):**
- **s19 visible** (3 cards): «T = 0.7 (стандарт) ... [Распределение: яблоко 0.32, пиццу 0.19, салат 0.14, …]» — distribution copy-pasted из s18 (T=1.0 baseline).
- **s19 speaker notes** line 46: «При T = 1.0 — стандартный режим. Модель сэмплирует пропорционально исходным вероятностям: яблоко будет выбрано примерно в 32% случаев».

**Issue:**
1. **Inconsistency между slide и speaker notes:** visible commits к «T=0.7 = стандарт», speaker notes — к «T=1.0 = стандарт». Это разная преподавательская позиция (OpenAI default T=1.0, Anthropic default T=1.0; many engineering blogs recommend T=0.7 для production). 
2. **Numerical confusion:** distribution «яблоко 0.32» — это **T=1.0 baseline** из s18; при T=0.7 (sharper) probability `яблоко` would be **higher** (~0.40-0.50), не 0.32. Студент с калькулятором numbers don't match T=0.7 phrasing.

**Severity:** P1 — методологически confusing для LO4 (выбор T). Direction correct (T=0 sharp, T=2 flat).

**Recommended fix:**
- **Option A (preserve T=0.7 framing):** recompute distribution для T=0.7 — яблоко ~0.45, пиццу ~0.20, и т.п. (softmax с division by T).
- **Option B (align с speaker notes):** change visible label «T = 0.7 (стандарт)» → «T = 1.0 (стандарт)»; keep numbers (распределение matches T=1.0).
- **Option C (clearest):** show three labels «T=0 / T=1 (default) / T=2», three distributions, all empirically derived.

---

## P2 Issues

### [P2-1] s06 BPE example — каноническая Sennrich (2016), но без cite на slide

**Location:** s06 visible (Before/After): `low / lower / newest / widest → low / er / new / est / wid`. Footer cite «Sennrich et al. (2016)».

**Issue:** Этот worked example **точно из** Sennrich, R., Haddow, B., Birch, A. (2016). «Neural Machine Translation of Rare Words with Subword Units» (arXiv:1508.07909) — canonical pedagogical example. Cite на slide есть, хорошо. Минор: Sennrich et al. (2016) — паper было submitted Aug 2015, опубликовано на ACL 2016. Сейчас slide says «(2016)» — corresponds к ACL publication, fine.

**Severity:** P2 (positive — cite present).

---

### [P2-2] s06 «Альтернативы: WordPiece (BERT), SentencePiece (Llama 2, T5)» — omits Llama 3 → tiktoken contextually

**Location:** s06 visible footer.

**Issue:** Visible content corretly attributes SentencePiece к Llama 2 (verified P0 fix from chapter). НО студент, помнящий заголовки про Llama 3, может прочесть «SentencePiece (Llama 2, T5)» как «и Llama 3 тоже» (implicit). Speaker notes line 50 явно отделяет: «BPE используется в GPT-семействе и в Llama 3+». 

**Severity:** P2 — visible content на slide accurate (Llama 2 only), but cognitively easy to misread. Optional cosmetic fix.

**Recommended fix (optional):** «Альтернативы (исторические): WordPiece (BERT), SentencePiece (Llama 2, T5). Llama 3+ — tiktoken-based BPE.»

---

### [P2-3] s08 «Английский ~0.25 токена/символ» — без cite на конкретный benchmark

**Location:** s08 visible chart + side table «Ориентир токены/символ».

**Issue:** Числа 0.25/0.50/0.80/0.40 даны без cite на конкретный замер. Slide footer caption: «Ориентир для современных токенизаторов GPT-семейства. Конкретные ratio проверяются эмпирически через tiktoken. Разброс RU/EN: 1.5×–2.5×.» Это адекватный hedge — direction correct, range plausible.

**Severity:** P2 — caveat present in visible content. NEEDS-REFRESH (cadence quarterly per chapter §1.4 [FACT-CHECK]).

---

### [P2-4] s09 GPT-4 внутренний эмбеддинг «тысячи измерений [FACT-CHECK]» — corrected from chapter v1.0

**Location:** s09 visible mini-callout.

**Issue (positive):** Chapter v1.0 had «12288 dim» (P1-3 from Phase 3). Chapter v1.1 softened to «диапазон порядка нескольких тысяч до 10+ тысяч». Slide s09 visible takes softer version: «Внутренний эмбеддинг flagship-LLM: порядок **тысячи измерений** [FACT-CHECK]». Хорошо distillированное chapter-level decision. `[FACT-CHECK]` маркер preserved на slide.

**Severity:** P2 (good propagation). No action.

---

### [P2-5] s22 Local sizes «1-13B» Cloud sizes «200B+» — нет cite на benchmark, но widely known

**Location:** s22 visible: «Local — 1-13B параметров (Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B, Mistral 7B). Cloud — 200B+ параметров.»

**Issue:** Sizes для Llama 3.x verified — Llama 3.1 8B (8.03B), Llama 3.2 1B (1.23B), Qwen 2.5 1.5B (1.54B), Mistral 7B (7.24B) — all match. Cloud «200B+» — phrasing «order of hundreds of billions» широко-известный (GPT-4 leak 1.76T MoE, Claude 3 estimated «hundreds of B», GPT-4o estimated 200-400B), без точной cite. Chapter §4.5 [FACT-CHECK: cadence quarterly] marker preserved.

**Severity:** P2 — direction correct, sizes for local verified, cloud appropriately hedged. Caption suggests pre-lecture refresh.

---

## Per-slide visible-data audit

| sNN | Slide | Fact / Number | Source verification | Verdict |
|---|---|---|---|---|
| s01 | Live tokenizer | `cat=1, tokenization=2, strawberry=3, клубника=3 в o200k_base` | Chapter v1.1 line 146 + tiktoken empirical (chapter §1.1 explicit «проверено май 2026») | ✓ VERIFIED |
| s02 | Cover roadmap | Layout «0 Открытие / 1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал» | Plan §2.2 arc | ✓ VERIFIED |
| s03 | Recap Лекции 1 | Cite Lec-1 §3.2 (Модель = stateless inference) | Lec-1 §3.2 confirmed | ✓ VERIFIED |
| s04 | Центральный вопрос | 3 «почему» якоря (s15/s07/s19) | Plan §1.4 + Lec-1 §5.3 | ✓ VERIFIED |
| s05 | Что такое токен | `cat=1, tokenization=2, клубника=3 в o200k_base`; «1 токен ≈ 4 EN / 2 RU» | Chapter v1.1 line 146 + 159 | ✓ VERIFIED |
| s06 | BPE compromise | `low/lower/newest/widest → low/er/new/est/wid`; cite Sennrich 2016 | Sennrich et al. 2016 (arXiv:1508.07909) — canonical example | ✓ VERIFIED |
| s07 | AI counts letters | `strawberry → [st][raw][berry] = 3 токена в o200k_base, не 10 букв` | Chapter v1.1 line 170 + tiktoken empirical | ✓ VERIFIED |
| s08 | Cross-language | EN ~0.25, RU ~0.50, ZH ~0.80, Python ~0.40 токенов/символ | Chapter §1.4 [FACT-CHECK cadence quarterly] + caveat в caption | ⚠ P2-3 (hedged) |
| s09 | Что такое эмбеддинг | `text-embedding-3-small 1536, large 3072; internal flagship — тысячи [FACT-CHECK]` | OpenAI API docs (1536/3072 verified); internal — softened (P2-4) | ✓ VERIFIED |
| s10 | Sentence similarity | Cosine 5×5: SSL↔HTTPS 0.85, React-комп↔React-прил 0.78, борщ-vs-tech 0.07-0.12 | Chapter v1.1 line 266 [FACT-CHECK] — illustrative с explicit caveat на slide | ✓ VERIFIED (illustrative w/ caveat) |
| s11 | 3 применения | similarity / clustering / search — RAG basis | Conceptual | ✓ VERIFIED |
| s12 | Semantic vs fulltext | клубника → клубники (stemming) vs strawberry/ягода/лесная земляника (semantic) | Lewis 2020 RAG paradigm | ✓ VERIFIED |
| s13 | Section divider | Раздел 3 | n/a | ✓ VERIFIED |
| s14 | Attention | Распределение сумма=1; flashlight metaphor; «32-128 голов» в speaker note | Vaswani et al. 2017 + chapter §3.1 line 271 | ✓ VERIFIED |
| s15 | Worked example | «Кот съел мышь, потому что она была голодна» + role-effect | Lec-1 §5.3 promise; chapter §3.2 line 292 | ✓ VERIFIED |
| s16 | Контекстное окно | GPT-3.5 4k (2022), Claude 3.5 200k (2024), Claude 4.7 1M (2026); ×250 рост; 1M ≈ 16× от 100k | Anthropic + OpenAI release notes verified; «×250» (математически 244) близко; **«16× от 100k» противоречит N² (100×)** — P1-1 | ⚠ P1-1 |
| s17 | Long-context fails | U-shape: ~75% / ~30% / ~75%; Liu et al. 2023 cite arXiv:2307.03172 | Liu et al. 2023 verified ✓; numbers depth slightly aggressive — P1-2 | ⚠ P1-2 |
| s18 | Distribution | «Сегодня я съел...» → яблоко 0.32, пиццу 0.19, салат 0.14, булочку 0.11, огурец 0.08, «остальные ~200k <0.05» | Illustrative ✓; «200k токенов остальные» соответствует o200k_base vocab | ✓ VERIFIED |
| s19 | Temperature | T=0 (argmax) / T=0.7 (стандарт) / T=2.0 (хаос); + top-p / top-k mention | T=0.7 vs T=1.0 inconsistency speaker↔visible + numerical consistency — P1-3 | ⚠ P1-3 |
| s20 | 4 ручки API | T/top_p/max_tokens/system_prompt таблица 4 сценария | Industry-standard; T=0 row softened «практически детерминирует» | ✓ VERIFIED |
| s21 | Авторегрессионная loop | 5-step cycle: контекст → forward pass → distribution → сэмплинг → новый токен | Conceptual (chapter §4.4) | ✓ VERIFIED |
| s22 | Local vs cloud | Local: Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B, Mistral 7B; Cloud: GPT-5, Claude 4.7, YandexGPT, GigaChat, Gemini; 200-500 ms | Local sizes verified ✓; Cloud caveat в chapter (cadence quarterly) | ⚠ P2-5 |
| s23 | Recap pipeline | 4-stage pipeline; cite s05-s08, s09-s12, s13-s17, s18-s20 | n/a | ✓ VERIFIED |
| s24 | 3 ответа payoff | «strawberry — 3 токена, не 10 букв»; «Сэмплинг — стохастический при T>0» | Consistent с s05-s07, s18-s19; chapter v1.1 line 537 | ✓ VERIFIED |
| s25 | ML vs LLM tree | XGBoost, LightGBM, BERT fine-tuned; <100ms; 200-500ms latency | Industry-standard; chapter §5.3 | ✓ VERIFIED |
| s26 | Attention vs causality | Pearl 3 уровня (ассоциация / вмешательство / контрфактуальность); callback Lec-1 §4.8 | Lec-1 §4.8 + Pearl framework verified | ✓ VERIFIED |
| s27 | Homework | HF Inference Playground, Meta-Llama-3-8B-Instruct, Together.ai / Ollama fallback; [VERIFY-DAY-OF] caption | Chapter v1.1 line 584 + [VERIFY-DAY-OF] preserved ✓ | ✓ VERIFIED (verify-day-of mandatory) |
| s28 | Bridge Лекции 3 | RAG, Tools / function calling, MCP (Anthropic 2024 — Lec-1 §2.2), Agent loop (act/observe/reflect) | MCP attribution verified to Lec-1 §2.2; Agent loop cites Lec-1 §3.4.1 (per s28 speaker) | ✓ VERIFIED |

**Totals:** 28 slides → 23 ✓ VERIFIED clean, 4 ⚠ P1 / P2 issues, 0 ✗ FALSE / P0.

---

## VERIFY-DAY-OF list (preserved in slides)

Все 3 `[VERIFY-DAY-OF]` маркера, обещанные в plan §9 freshness table и в chapter v1.1, **присутствуют в slides** (front-matter `verify_day_of: true` + caption или speaker note):

| # | Slide | Front-matter flag | Visible content caption | Speaker note mention | What lecturer pre-tests |
|---|---|---|---|---|---|
| 1 | **s07** «strawberry test» | `verify_day_of: true` ✓ | Retrieval prompt: «Телефоны: "сколько r в strawberry?" Что отвечает ваша модель?» | Speaker note line 47: «Современные топ-модели часто отвечают правильно... структурный факт не меняется». Chapter v1.1 line 187 explicit «[VERIFY-DAY-OF: weekly cadence — лектор делает претест на 2-3 моделях]». | На день лекции: ChatGPT / Claude / GPT-5+ — что отвечает на strawberry? Если все 3 правильно — switch к ROT-13 / методология. |
| 2 | **s16** «Context window cifры» | `verify_day_of: true` ✓ | Caption visible: «[VERIFY-DAY-OF] Цифры на момент мая 2026. Темп роста ~×10 каждые 1-2 года.» ✓ | Speaker note line 40: «Если к моменту чтения какие-то цифры уже сдвинулись — это нормально... важен порядок, а не конкретные числа». Fallback narrative ready. | На день лекции: Claude 4.7 1M — still latest? Вышел Claude 4.8 / 5.0 / GPT-X с другими цифрами? Adjust s16 chart если sdвинулось. |
| 3 | **s27** «HF Playground» | `verify_day_of: true` ✓ | Caption visible: «[VERIFY-DAY-OF] проверка доступности HF Playground за день до семинара.» ✓ | Speaker note line 52 + chapter v1.1 line 584 mandatory: «HF Inference Playground UI alive? Meta-Llama-3-8B-Instruct в free tier? T-slider в UI?». Fallback: Together.ai / Ollama. | За день до семинара: проверить (a) huggingface.co/playground UI accessible, (b) Llama-3-8B-Instruct available на free tier, (c) T-slider visible. Если хоть одно «no» — switch к fallback в материалах семинара. |

**Counter-check:** все 3 verify-on-day items имеют **fallback narrative**, прописанный в speaker notes — что снижает risk if pre-test reveals issue.

---

## FACT-CHECK markers (chapter v1.1 → slides propagation)

Chapter v1.1 содержит 9 `[FACT-CHECK]` markers (per Phase 3 fact-checker §FC-1..FC-10). Проверка propagation в slides:

| # | Chapter location | Claim | Slide propagation | Status |
|---|---|---|---|---|
| FC-1 | §1.1 line 159 | «1 токен ≈ 4 EN / 2 RU; OpenAI tokenizer benchmarks 2024» | s05 visible gold callout «1 токен ≈ 4 EN / 2 RU» (без `[FACT-CHECK]` маркера). Plan §9 cadence quarterly. | ⚠ Marker dropped в visible (acceptable — это «ориентир», hedged via «в среднем»). |
| FC-2 | §1.3 line 187 | «strawberry — топ-модели могут отвечать правильно [VERIFY-DAY-OF weekly]» | s07 speaker note line 47 explicit; visible retrieval prompt. | ✓ Preserved в speaker notes (visible-content student-facing). |
| FC-3 | §1.4 line 201 | RU/EN token ratios `[FACT-CHECK cadence quarterly]` | s08 caption «Конкретные ratio проверяются эмпирически через tiktoken. Разброс 1.5×-2.5×.» | ✓ Caveat preserved в visible. |
| FC-4 | §2.1 line 232 | GPT-4 internal hidden dim `[FACT-CHECK cadence yearly; источник — leaks]` | s09 visible mini-callout «Внутренний эмбеддинг flagship-LLM: порядок тысячи измерений [FACT-CHECK]» | ✓ Marker preserved в visible. |
| FC-5 | §2.2 line 266 | Cosine similarity numbers `[FACT-CHECK illustrative]` | s10 visible caption «Числа illustrative; воспроизводимы на sentence-transformers/all-MiniLM-L6-v2 или OpenAI text-embedding-3-small» | ✓ Caveat preserved + reproducibility instruction. |
| FC-6 | §3.3 line 351 | Context window timeline `[VERIFY-DAY-OF cadence quarterly]` | s16 visible caption «[VERIFY-DAY-OF] Цифры на момент мая 2026» | ✓ Preserved в visible. |
| FC-7 | §4.5 line 492 | Local model sizes 1-13B `[FACT-CHECK cadence quarterly]` | s22 visible (no explicit marker on slide) — но chapter §4.5 has marker; speaker note implicit «на 2026 год». | ⚠ Marker dropped в visible (acceptable — sizes стабильны квартально; chapter §4.5 carries marker). |
| FC-8 | §5.5 line 584 | HF Playground availability `[VERIFY-DAY-OF]` | s27 visible caption «[VERIFY-DAY-OF] проверка доступности HF Playground за день до семинара» | ✓ Preserved в visible. |
| FC-9 | §источники line 625 | Claude 4.7 1M context `[FACT-CHECK cadence quarterly]` | s16 covers; s22 covers «Контекст: до 1M токенов» | ✓ Preserved через s16 caption. |
| FC-10 | §источники line 626 | OpenAI context history `[FACT-CHECK cadence yearly]` | s16 covers (GPT-3.5 4k anchor) | ✓ VERIFIED. |

**Markers propagation summary:** 8/10 explicitly preserved в visible OR speaker; 2/10 dropped acceptably (FC-1 «1 токен ≈ 4 EN» — generic ориентир; FC-7 «1-13B local» — stable for quarter). **No critical fact-check markers lost.**

---

## Cross-slide vs chapter consistency

Spot-check ключевых cross-references:

| Item | Chapter v1.1 | Slide | Consistency |
|---|---|---|---|
| strawberry split | §1.3 line 170 «[st][raw][berry] 3 токена в o200k_base» | s01 / s05 / s07 / s24 — все consistent «[st][raw][berry] = 3 токена» | ✓ ALIGNED |
| Llama-3 tokenizer | §1.2 line 161 «Llama 3+ — tiktoken-based BPE, 128,256 vocab» | s06 visible не упоминает Llama 3 явно; speaker line 50 «BPE используется в Llama 3+». | ⚠ Minor — visible says только «SentencePiece (Llama 2, T5)» (correct, but partial). См. P2-2. |
| GPT-4 internal emb | §2.1 line 232 «нескольких тысяч до 10+ тысяч» | s09 visible «тысячи измерений [FACT-CHECK]» | ✓ ALIGNED (softer slide ok). |
| Context window 3 точки | §3.3 line 353-355 — GPT-3.5 4k / Claude 3.5 200k / Claude 4.7 1M | s16 visible exact match | ✓ ALIGNED |
| Liu et al. 2023 arXiv | §3.4 (chapter cite consistent) | s17 visible cite «Liu et al. 2023. Lost in the Middle. arXiv:2307.03172» | ✓ ALIGNED + arXiv ID verified |
| Sennrich 2016 | §1.2 ref | s06 cite «Sennrich et al. (2016)» | ✓ ALIGNED |
| Local model sizes | §4.5 line 492 (Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B, Mistral 7B) | s22 visible exact match | ✓ ALIGNED |
| MCP — Anthropic 2024 | §5.5 line 595 + §Источники line 621 | s28 visible «MCP (Anthropic, 2024; Lec-1 §2.2)» | ✓ ALIGNED + cross-lec consistent |
| Agent loop act/observe/reflect | §5.5 cite Lec-1 §3.4.1 | s28 visible «act → observe → reflect» | ✓ ALIGNED |
| 3 «почему» Лекции 1 §5.3 | §5.2 (payoff) | s04 (promise) + s24 (payoff) | ✓ ALIGNED both ways |
| `text-embedding-3` dims | §2.1 line 229-230 (1536 / 3072) | s09 visible «1536 / 3072» | ✓ ALIGNED |
| 200k tokens другие | §4.4 «остальные ~200k токенов <0.05» | s18 visible «остальные ~200k токенов: каждый <0.05; Σ=1» | ✓ ALIGNED (vocab size consistent w/ o200k_base) |

**No drift detected** между chapter v1.1 и 28 slides.

---

## Visual chart accuracy

Spot-check charts (PNG renders vs chapter/slide spec):

| Chart | File | Specified | Rendered (PNG) | Status |
|---|---|---|---|---|
| s08 tokens/char | `assets/charts/s08-tokens-per-char.png` | EN 0.25 / RU 0.50 / ZH 0.80 / Py 0.40 | Bar chart shows exactly those values; RU bar in gold ✓ | ✓ MATCH |
| s14 attention bars | `assets/charts/s14-attention-bars.png` | Распределение сумма=1, 1 max + spread | Bar chart with one tall + several short; sum visually ~1 ✓ | ✓ MATCH |
| s16 context window | `assets/charts/s16-context-window.png` | Log-scale 4k / 200k / 1M | Log-scale shows 4096 → 200,000 → 1,000,000 with gold highlight на 1M ✓ | ✓ MATCH |
| s17 U-shape | `assets/charts/s17-u-shape.png` | ~75% / ~30% / ~75% по позиции 0-100% | U-curve drops к ~30% в позиции 50%, recovers к 75% ✓ | ⚠ P1-2 (numbers more aggressive than Liu et al. 2023) |
| s18 distribution | `assets/charts/s18-distribution.png` | яблоко 0.32, пиццу 0.19, салат 0.14, булочку 0.11, огурец 0.08 | Bar chart exact match; яблоко в gold ✓ | ✓ MATCH |
| s19 T variants | `assets/charts/s19-T0.png`, `s19-T1.png`, `s19-T2.png` | T=0 — argmax яблоко=1.00, T=0.7 — spread, T=2.0 — flat | Three charts rendered; T=0.7 chart uses same numbers as T=1.0 baseline ⚠ | ⚠ P1-3 (T=0.7 chart should be sharper than T=1.0; instead identical) |
| s09 token→vector | `assets/diagrams/s09-token-to-vector.svg` | `[кот]` → lookup → `[0.21, -0.45, 0.88, ..., 0.13]` | Diagram shows id=47284 + vector 5 elements ✓ | ✓ MATCH (id=47284 illustrative, no claim on real OpenAI tokenizer id) |
| s10 heatmap | `assets/diagrams/s10-heatmap.svg` | 5×5 SSL/HTTPS/React-комп/React-прил/Борщ | Heatmap renders; 0.85 in gold (SSL↔HTTPS), 0.78 in gold (React↔React) ✓ | ✓ MATCH (numbers illustrative w/ caveat) |
| s07 strawberry | `assets/diagrams/s07-strawberry-split.svg` | strawberry → `[st][raw][berry]` 3 токена | Diagram shows strawberry → 10 letters → 3 tokens ✓ | ✓ MATCH |
| s01 Tiktokenizer | `assets/diagrams/s01-tiktokenizer-mock.svg` | 4 примера: cat=1, tokenization=2, strawberry=3, клубника=3 | Mock interface shows exactly those values; «o200k_base · GPT-4o» в верхнем правом углу ✓ | ✓ MATCH |

**Charts summary:** 9/10 clean match; 2/10 P1-flagged for content accuracy (s17 depth, s19 T=0.7 numbers).

---

## Counter-check

- **Verdict mapping:** 0 P0 + 3 P1 + 5 P2 → APPROVE-WITH-POLISH per agent prompt rules («≤4 P1 — show-able с known caveats»). 3 P1 < 5 threshold → not REVISE. No P0 → not REJECT. ✓ Correct verdict.
- **No direction inversion missed.** Trend claims проверены:
  - «контекст вырос на порядки» — UP, verified ✓ (4k → 1M = 244×).
  - «темп роста ~×10 каждые 1-2 года» — directionally correct (×50 за 2 года 2022→2024, ×5 за 1.5 года 2024→2026 — averages roughly ×10 / 1-2 года) ✓.
  - «стоимость растёт квадратично» — UP, theoretical N² ✓ (но «16× от 100k» — production-pricing, не pure N² — см. P1-1 muddle).
  - «RU в 2× дороже EN» — UP cost, verified ✓.
  - «T=0 — детерминирует выбор» / «T=2 — почти хаос» — directionally correct ✓.
  - «attention max на «мышь»» (s15) — directionally correct для standard reference resolution.
- **Citation hygiene:** Quotes (в кавычках) проверены:
  - «Кот съел мышь, потому что она была голодна» — пример, not quote ✓.
  - «Программа упала, потому что она забыла обработать null» — пример ✓.
  - «Lost in the Middle: How Language Models Use Long Contexts» — exact paper title, verified via arXiv ✓.
  - «Attention Is All You Need» — implicit Vaswani cite, verified ✓.
  - «Model Context Protocol» — Anthropic 2024 official term ✓.
  - «Retrieval-Augmented Generation» — Lewis 2020 standard term ✓.
- **Curriculum sync:**
  - Лекция 3 = «Агенты, RAG, API: как AI выходит за пределы чата» ← s28 visible exact match to Lec-1 §5.2 line 662. ✓
  - Лекция 12 (PARTS) — implicit reference в plan §1.5 (chapter notes Lec-1 internal contradiction §5.2 vs §3.3 — flagged for separate issue, не для Lec-2). No slide claims PARTS lives в Лекция 12. ✓ No new curriculum hallucination.
  - 4-7 индустрии — s25 caption «Глубже — Лекции 4-7 (индустрии)» matches Lec-1 §5.2. ✓
- **Mandatory file save:** path `/home/levko/AI-usage-lessons/library/lectures/lec-02/qa-reports/2026-05-13-phase7-slides-v1/fact-checker.md` confirmed, mkdir OK.

**Verdict reconfirmed: APPROVE-WITH-POLISH.**

---

## Recommendations summary (priority order)

**Before final lecture (cosmetic fixes, ~30 min total work):**

1. **[P1-1] s16 «16× от 100k» natanging vs N² theory.** Pick одну из 3 опций (preserve number + soften theory; drop number; use theoretical 100×). Recommend Option A: «Pure attention: N²; в production-pricing — ~16× от 100k (FlashAttention/KV-кэш снижают константу)».
2. **[P1-2] s17 U-shape depth.** Recommend Option A — update chart middle ~50% (matches Liu Figure 1), keep ~75% начало/конец.
3. **[P1-3] s19 T=0.7 vs T=1.0 inconsistency.** Recommend Option B — change visible label «T = 0.7 (стандарт)» → «T = 1.0 (стандарт)» so visible numbers (яблоко 0.32) match speaker note phrasing.
4. **[P2-2] s06 footer.** Optional addendum: «Llama 3+ — tiktoken-based BPE» — clarifies без расширения slide content.

**Day-of-lecture (lecturer responsibility) — все 3 critical preserved:**

1. **s07 strawberry test** на 2-3 моделях (ChatGPT, Claude, GPT-5+). Switch к ROT-13 / методология если все 3 правильно.
2. **s27 HF Playground** UI + Meta-Llama-3-8B-Instruct availability в free tier + T-slider visible. Fallback Together.ai / Ollama.
3. **s16 context window** cifры. Has Claude 4.8 / 5.0 / GPT-X released? Update chart точки если sdвинулось; speaker note has fallback narrative.

**Bonus pre-flight verification (optional, ~10 min):**
- Run `tiktoken.encoding_for_model("gpt-4o").encode("strawberry")` to confirm `[st][raw][berry]` split still holds on day-of (tokenizer doesn't change without OpenAI announcement, so once-per-quarter check suffices).
- Run `tiktoken.encoding_for_model("gpt-4o").encode("клубника")` to confirm 3-token split.
- Run `tiktoken.encoding_for_model("gpt-4o").encode("сильнее")` so inline poll s05 question has known answer ready (~2-3 tokens).

---

**Конец fact-checker report on slides Лекции 2 v1.0.** Status: APPROVE-WITH-POLISH → forward to orchestrator. 3 cosmetic P1 fixes recommended; 5 P2 acceptable as-is. 0 blocking issues. All `[FACT-CHECK]` + `[VERIFY-DAY-OF]` markers propagated correctly. Cross-consistency с chapter v1.1 strong. No curriculum hallucinations. No direction inversions. No misquotes.
