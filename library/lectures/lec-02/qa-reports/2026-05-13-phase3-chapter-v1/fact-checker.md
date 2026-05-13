# Fact-Checker Report on Chapter Лекции 2 v1.0 — 2026-05-13

**VERDICT: REVISE**

**Severity counts:** P0 = 2, P1 = 7, P2 = 4.

Rationale for REVISE (not REJECT): обе P0 — locally fixable factual errors (Llama-3 tokenizer attribution; potentially incorrect strawberry token split), не direction inversion и не curriculum hallucination. Все 9 `[FACT-CHECK]` маркеров главы validated и получают конкретный disposition. 7 P1 — combination of NEEDS-REFRESH (3) + missing source / weak attribution (4) — нужны точечные правки до production, но не блокирующие для slides phase.

---

## Summary

Chapter Лекции 2 v1.0 — academic explanatory материал на ~10,150 слов, 5 разделов + введение + источники. Все 9 `[FACT-CHECK]` маркеров поставлены book-editor'ом честно (author flagged uncertainty каждый раз, where appropriate). Crucial citations к каноническим работам (Vaswani 2017, Liu 2023, Sennrich 2016, Mikolov 2013, Holtzman 2019/2020) **все verified против arXiv** — IDs совпадают с автором, годом, и темой.

Two P0 fact errors найдены:

1. **Llama-3 tokenizer attribution** — chapter (§1.1, §1.2, §источники, line 106, 123, 560) утверждает «LLaMA использует токенизатор SentencePiece» — это было верно для Llama 2, но **Llama 3 переключился на tiktoken-based tokenizer** с 128k vocab. Это публично документированное изменение Meta при релизе Llama-3 (apr 2024).

2. **strawberry token split** — chapter (§1.3 line 132, §5.2 line 483) утверждает «strawberry разрезается на `[straw][berry]` — два токена». В современных tiktoken-токенизаторах (cl100k_base, o200k_base) word `strawberry` обычно разрезается на **3 токена** (`st` / `raw` / `berry` или `straw` / `ber` / `ry` — варианты), не 2. Это критически важно для §1.3, потому что центральный объяснительный аргумент главы «модель видит 2 токена, поэтому путает 3 r» зависит от точного split.

Cross-consistency с Lec-1 — strong: MCP definition, callbacks, Vaswani et al. список авторов и год, GitHub Octoverse / Stack Overflow numbers все match. Curriculum sync с §5.2 Lec-1 (17 lectures × 3 modules) — Лекция 17 = «Заключение / синтез», что согласовано с Lec-2 chapter §1.4 («Лекция 17 / доп.чтение»).

---

## P0 Issues (fact errors / unsupported claims)

### [P0-1] Llama-3 tokenizer wrong — это **tiktoken**, не SentencePiece

**Locations in chapter:**
- §1.1 line 106: «LLaMA использует токенизатор SentencePiece со словарём около 128 тысяч (Meta AI, 2024)».
- §1.2 line 123: «WordPiece (BERT)... SentencePiece (LLaMA, T5)...» — для современных Llama-3+ неверно.
- §Источники line 560: «Meta AI. (2024). LLaMA 3 model card. Llama-3 tokenizer (SentencePiece-based, ~128k vocab)».
- §Дальнейшее чтение line 597: цитирование Kudo SentencePiece — корректно как algorithmic reference, но привязка к Llama-3 неверна.

**Issue:** Llama 2 использовал SentencePiece BPE. **Llama 3 (apr 2024) переключился на tiktoken-based tokenizer** с 128,256 tokens vocabulary, основанный на OpenAI tiktoken с добавлением спец-токенов. Это публично документированное изменение Meta.

**Источник верификации:** Llama 3 model card / Hugging Face docs / Meta release notes; multiple third-party explanations (machinelearningmastery, fast.ai/posts/2025-10-16-karpathy-tokenizers).

**Recommended correction:**
- §1.1: «LLaMA 2 использовал SentencePiece; Llama 3+ — tiktoken-based BPE-токенизатор с ~128k vocab (Meta AI, 2024)».
- §1.2: «WordPiece (BERT), SentencePiece (T5, ранние Llama 2, многие open-weight модели), tiktoken-based (Llama 3+, GPT-семейство)».
- §Источники: исправить attribution Llama-3 на tiktoken.
- §Дальнейшее чтение: Kudo SentencePiece можно оставить как алгоритмическую референс к классу subword tokenizers (с уточнением, что Llama 3 уже не использует).

**Severity:** P0 (factually incorrect technical claim, multi-occurrence, в основной образовательной канве; легко проверяется студентами через Hugging Face).

---

### [P0-2] strawberry token split вероятно 3 токена, не 2

**Locations in chapter:**
- §1.3 line 132: «Слово `strawberry` в стандартном английском BPE-токенизаторе разрезается на два токена: `[straw][berry]`».
- §1.3 line 168 (Inline note про p.157 «1 токен ≈ 4 символа в EN»).
- §5.2 line 483: «Слово `strawberry` для неё — два токена `[straw][berry]`».
- §s07 visual context (line 167 plan, slide spec).
- §Бонусный челлендж line 532 (косвенно).

**Issue:** В современных OpenAI tiktoken-токенизаторах `cl100k_base` (GPT-3.5/4) и `o200k_base` (GPT-4o) word `strawberry` обычно tokenize как **3 токена**, не 2. Чаще встречается split `st` / `raw` / `berry` (по AI explanation от Anthropic / OpenAI блогов о strawberry meme). Точное разбиение зависит от токенизатора, но 2-token split `[straw][berry]` — не самый частый случай в production cl100k.

**Источник верификации:** TechRadar / Dataconomy / Medium articles 2024-2026 explain the strawberry meme: «When "strawberry" is tokenized, it yields three tokens: st, raw, berry». Студент с tiktokenizer.vercel.app легко проверит и обнаружит расхождение с книгой.

**Recommended correction:**
- Option A (preferred): replace text «два токена: `[straw][berry]`» → «несколько токенов (обычно три: `[st][raw][berry]` в cl100k_base, может варьироваться по моделям)». Это сохранит аргумент главы (модель не видит букв независимо от того, 2 или 3 токена) и при этом будет factually verifiable.
- Option B: оставить 2-token version, но добавить explicit footnote: «точный split зависит от токенизатора; здесь illustrative — реальные модели могут разрезать на 3 токена. Концептуальный аргумент `модель не видит букв` остаётся».
- Pre-flight: book-editor должен выполнить tiktokenizer проверку для слов в s01 (`cat`, `tokenization`, `клубника`, `🍓`) перед production lecture.

**Severity:** P0 (центральный объяснительный пример главы, легко falsifiable студентом за 30 секунд; противоречит публично доступному поведению tiktoken; снимает доверие ко всей §1.3).

---

## P1 Issues (NEEDS-REFRESH / weak attribution)

### [P1-1] RU vs EN 2× tokenization cost — нет empirical attribution

**Location:** §1.1 line 108 («1 токен ≈ 4 символа в EN ≈ 2 в RU»), §1.4 line 156 («OpenAI tokenizer benchmarks, 2024 [FACT-CHECK: cadence quarterly]»).

**Issue:** Specific цифра «0.25 EN, 0.5 RU, 0.8 ZH, 0.4 Py-code» (line 159-161) — без published source. «OpenAI tokenizer benchmarks» — general label, конкретного URL/документа не указано. Студент не сможет независимо проверить эти числа.

**Recommended action:** book-editor должен либо
- (a) запустить tiktoken Python для замеров на конкретных корпусах (Wikipedia EN/RU samples 100k символов каждый) и привести фактические цифры + методику;
- (b) cite a third-party benchmark (e.g., HF cookbook, Mistral blog, AI/ML research blog comparing multilingual tokenization);
- (c) softer the phrasing: «по разным замерам RU стоит в 1.5–2.5× от EN — порядок 2×, точные числа зависят от токенизатора и корпуса».

**Verdict:** NEEDS-REFRESH — soft confirmable (2× direction is widely known), но «around 0.25/0.5/0.8/0.4» — specific numbers, нужна attribution.

**Severity:** P1.

---

### [P1-2] Cosine similarity numbers (0.85, 0.78, 0.05-0.15) — empirically not verified

**Location:** §2.2 line 212-216.

**Issue:** Chapter сам помечает `[FACT-CHECK]` — «illustrative; должны быть эмпирически проверены на target embedding model». Сейчас не указано, на какой модели проверить.

**Recommended action:**
- Specify embedding model в footnote: e.g., `text-embedding-3-small` (OpenAI, dim=1536) — самый частый production выбор; или `all-MiniLM-L6-v2` (sentence-transformers, open-source); или `BAAI/bge-large-en-v1.5`.
- Run actual cosine similarity для 5 предложений главы on chosen model.
- Replace illustrative numbers with empirical ones (e.g., «1↔2: 0.74, 3↔4: 0.71, 1↔5: 0.21»), + footnote с моделью.
- Если book-editor предпочитает оставить illustrative — добавить inline footnote «illustrative numbers; empirical values depend on embedding model and language version (RU/EN); студент может воспроизвести на sentence-transformers».

**Verdict:** NEEDS-REFRESH (но cadence yearly — embedding models stable).

**Severity:** P1.

---

### [P1-3] GPT-4 internal embedding 12288 dim — disputed source

**Location:** §2.1 line 191: «Внутренний эмбеддинг токенов в GPT-4 (по архитектурным утечкам): около 12288 измерений [FACT-CHECK: cadence yearly; source = leak]».

**Issue:** Точная цифра disputed. По существующим leak-источникам (GeoHot, SemiAnalysis), 12288 — это GPT-3 hidden size, а у GPT-4 hidden dim **разные оценки**: 12,288 (популярный leak), некоторые оценки указывают на меньше (например, 3072 — Hacker News, https://news.ycombinator.com/item?id=40368445). Authoritative confirmation от OpenAI отсутствует.

**Recommended action:**
- Soften: «Внутренние эмбеддинг-векторы у современных flagship-моделей оцениваются в порядке нескольких тысяч до 10+ тысяч измерений (точные числа OpenAI / Anthropic не публикует; leak-оценки расходятся: GPT-3 hidden dim — 12288; для GPT-4 оценки от 3k до 12k; ни одна не подтверждена производителем)».
- Альтернатива: drop the specific 12288 number; cite только outputs `text-embedding-3-large` 3072 как public-facing reference.

**Verdict:** NEEDS-REFRESH (yearly cadence) — лучше softer phrasing.

**Severity:** P1 (chapter уже отмечает уязвимость через `[FACT-CHECK]`; но specific number 12288 для GPT-4 — claim, который easily disputed reader'ом).

---

### [P1-4] Context window timeline (s16, §3.3 lines 301-303) — verify-on-day-of

**Location:** §3.3 lines 301-303 (3 точки: GPT-3.5 4k / Claude 3.5 200k / Claude 4.7 1M).

**Verification:**
- GPT-3.5 4k (Nov 2022): **VERIFIED** — 4,096 token context window при release ChatGPT. ✓
- Claude 3.5 (June/Oct 2024): **VERIFIED** — 200K context window. ✓
- Claude Opus 4.7 (Apr 16, 2026): **VERIFIED** — 1M context window. ✓

**Issue:** Дата лекции — fall 2026 (estimated Sept-Dec). Claude 4.7 released Apr 16, 2026; cadence quarterly. К sept/oct 2026 возможен выход Claude 4.8/5.0 или GPT-5 next-gen с другими цифрами. Day-of-lecture verify обязателен.

**Recommended action:** keep as is + verify-on-day; fallback narrative «порядок 100k → 1M → дальше; квадратичная стоимость не зависит от точных цифр» — уже в s16 fallback note.

**Verdict:** VERIFIED for May 2026; NEEDS-REFRESH day-of-lecture.

**Severity:** P1.

---

### [P1-5] HF Inference Playground availability — verify-on-day-of

**Location:** §5.5 line 530.

**Issue:** Hugging Face Inference Playground — free tier subject to platform changes (Sept 2025 — they discontinued some free inference endpoints). Meta-Llama-3-8B-Instruct наличие на HF playground в день лекции — **не гарантировано**.

**Verification (May 2026):** Llama-3-8B-Instruct exists на HF Hub; Inference Playground status дополнительно не проверен (search не вернул definitive 2026 confirmation that the playground UI is open для этой конкретной модели — may require Pro subscription).

**Recommended action:** Lecturer/orchestrator должен в день лекции проверить:
- (a) HF Playground UI доступен (huggingface.co/playground).
- (b) Llama-3-8B-Instruct доступен через free tier.
- (c) Temperature slider присутствует в UI.
- Если хоть одно `no` — переключиться на fallback (Together.ai / Ollama).

**Fallback chain** в chapter уже описан — well-engineered.

**Verdict:** NEEDS-REFRESH day-of-lecture (cadence monthly for HF platform changes).

**Severity:** P1.

---

### [P1-6] strawberry test on top models — выводы partially outdated

**Location:** §1.3 line 149 («[FACT-CHECK: эксперимент `strawberry` работает не всегда — современные топ-модели (на момент написания — Claude 4.7, GPT-5, ChatGPT-5) могут отвечать правильно за счёт внутреннего вызова кода или цепочек рассуждений»).

**Verification (May 2026):**
- **Claude Opus 4.7** — отвечает правильно (3 r). ✓
- **GPT-5.2 (Dec 2025)** — **продолжает miscount** (2 r), даже latest model (Dataconomy Dec 2025).
- **GPT-5.5 vs Claude 4.7** — Claude correct, GPT incorrect (multiple 2026 comparison reviews).

**Issue:** Chapter says «топ-модели MAY ОТВЕЧАТЬ ПРАВИЛЬНО» — это OK, но soft / hedge formulation. Конкретный empirical статус: **GPT-семейство still miscounts**, Claude — uniformly correct. Точная formulation в s07 lecturer brief должна это уточнить.

**Recommended action:** добавить в lecturer pre-flight script (s07): «на день лекции проверь strawberry на 3 моделях:
- ChatGPT (бесплатная / Plus) — обычно miscount → keeps demo working.
- Claude.ai (бесплатная) — обычно correct → demo нужно скорректировать.
- YandexGPT / GigaChat — empirically variable.
Если все 3 правильные — replace example на «методология» / ROT-13».

Этот fallback уже зафиксирован в plan §1.4 retrieval moments — нужно убедиться, что chapter §1.3 (lines 143-149) сохраняет адекватный hedge.

**Verdict:** chapter уже hedges, но nuance можно усилить (как раз для day-of pretest).

**Severity:** P1 (cadence weekly — high freshness risk).

---

### [P1-7] Sources list — Octoverse / Bloomberg / DeepSeek cited без strict need в этой главе

**Location:** §Источники lines 578-581 (Bloomberg Samsung incident, GitHub Octoverse 2025, DeepSeek-R1 technical report, Stanford SEP Chinese Room).

**Issue:** Эти источники упомянуты как «дополнительно цитированы (callbacks к Лекции 1)», но в самом тексте Главы 2 я не нашёл явных citations of Bloomberg, Octoverse, DeepSeek-R1, или Chinese Room. Эти источники должны быть в Лекции 1 cited list, не дублироваться в Лекции 2 если there's no actual citation in body.

**Recommended action:** book-editor должен либо
- (a) удалить из §Источники главы 2, оставив только references к §callbacks Лекции 1 (т.е. формулировка «см. источники Лекции 1»);
- (b) если есть implicit cite в §4.5 («Mistral 7B», «Llama 3.1 8B»), сделать explicit inline cite в body — или удалить из bibliography.

**Verdict:** non-blocking, но cleanup для academic integrity.

**Severity:** P1 (academic source hygiene — citations должны быть actually used in body).

---

## P2 Issues (minor / formatting / cite format)

### [P2-1] Holtzman year inconsistent

**Location:** §4.2 line 369 ("Holtzman et al., 2019"); §Источники line 564 ("Holtzman, A., Buys, J., Du, L., Forbes, M., Choi, Y. (2019). The Curious Case of Neural Text Degeneration. *ICLR 2020*. arXiv:1904.09751").

**Issue:** Inline cite says 2019, references list says «(2019). ... *ICLR 2020*». Both internally OK (arXiv preprint 2019, conference proceedings 2020), но **mixed citation style**. Standard academic practice — cite by year of publication (2020 if peer-reviewed venue, или arXiv year if preprint). Mixing создаёт минорную inconsistency.

**Recommended action:** unify to «Holtzman et al. (2019)» throughout body + bibliography (arXiv year) — this is what chapter currently has; OR унифицировать на (2020).

**Severity:** P2.

---

### [P2-2] cl100k_base / o200k_base attribution года

**Location:** §1.1 line 106: «`cl100k_base` (GPT-3.5, GPT-4) — около 100 тысяч (OpenAI tiktoken, 2024)».

**Issue:** `cl100k_base` is GPT-3.5/GPT-4 era (2022-2023), не 2024 — это вначале 2023. `o200k_base` — May 13, 2024 (GPT-4o release). «(OpenAI tiktoken, 2024)» — referring к library version, что OK, but year-of-release of конкретного encoding inconsistent.

**Recommended action:** «`cl100k_base` (GPT-3.5/GPT-4, 2022-2023; ~100k vocab); `o200k_base` (GPT-4o, May 2024; ~200k vocab)».

**Severity:** P2.

---

### [P2-3] «специально структурированный JSON» — softer wording в s28 mention

**Location:** §5.5 line 540 («Tools / function calling. Механизм, через который модель генерирует **специально структурированный JSON**»).

**Issue:** Term «function calling» — это OpenAI's API feature name; «structured JSON» — implementation detail на самом деле опционально (некоторые модели использовали XML, или free-form text + parsing). Statement OK as illustrative, но не technically strict.

**Recommended action:** не критично; можно оставить, но добавить inline note «специальный JSON или другой структурированный формат, в зависимости от API провайдера».

**Severity:** P2.

---

### [P2-4] «по утечкам» — informal phrasing

**Location:** §2.1 line 191.

**Issue:** «по архитектурным утечкам» — colloquial. Academic phrasing — «по неофициальным оценкам, основанным на reverse-engineering» или «по leak-источникам (GeoHot, SemiAnalysis, etc.)».

**Recommended action:** minor copy-edit.

**Severity:** P2.

---

## Per-`[FACT-CHECK]` marker disposition

Главу пробежал на 9 `[FACT-CHECK]` маркеров:

| # | Location | Claim | Verdict | Recommended action |
|---|---|---|---|---|
| FC-1 | §1.1 line 108 | «1 токен ≈ 4 символа в EN ≈ 2 в RU» (OpenAI benchmarks 2024) | NEEDS-REFRESH | Cite specific OpenAI/HF benchmark URL OR run tiktoken empirically (см. P1-1). |
| FC-2 | §1.3 line 149 | «strawberry эксперимент — топ-модели могут отвечать правильно» (cadence weekly) | VERIFIED partial | Hedge correct; lecturer day-of test обязателен (см. P1-6). |
| FC-3 | §1.4 line 156 | RU/EN tokenization split numbers (OpenAI benchmarks 2024) | NEEDS-REFRESH | Same as P1-1. |
| FC-4 | §2.1 line 191 | GPT-4 internal embedding 12288 dim (по утечкам) | NEEDS-REFRESH | Softer wording (см. P1-3). |
| FC-5 | §2.2 line 212 | Cosine similarity 0.85/0.78/0.05-0.15 (illustrative) | NEEDS-REFRESH | Specify embedding model + empirical run (см. P1-2). |
| FC-6 | §3.3 line 299 | Context window timeline 4k → 200k → 1M (cadence quarterly) | VERIFIED for May 2026 | Verify-on-day-of (см. P1-4). |
| FC-7 | §4.5 line 438 | Local model sizes 1B-13B (cadence quarterly) | VERIFIED for May 2026 | Verify-on-day-of (см. day-of list). |
| FC-8 | §5.5 line 530 | HF Inference Playground availability + free Llama-3-8B-Instruct | VERIFIED partial | Day-of verify обязателен (см. P1-5). |
| FC-9 | §Источники line 571 | Claude 4.7 1M context (cadence quarterly) | VERIFIED for May 2026 | Verify-on-day-of. |
| FC-10 | §Источники line 572 | OpenAI GPT-3.5/4/4o context windows history (cadence yearly) | VERIFIED | OK. |

(10 markers total; some sources double-count `[VERIFY-DAY-OF]` tags which I include for completeness.)

---

## Freshness report (per-claim metadata)

For each AI-tool / benchmark / model claim with time-sensitivity. Lecture date estimate: 2026-09-15 (~125 days delta from now 2026-05-13).

```
Fact: «GPT-3.5 context window 4k (2022 release ChatGPT)»
Number: 4096 tokens
Source: OpenAI ChatGPT release notes Nov 2022; tiktoken docs
Source date: 2022-11
Lecture date: ~2026-09-15
Refresh cadence: yearly+
Days delta: ~1400 days
Verify-on-day: no (historic fact)
Verdict: VERIFIED

Fact: «Claude 3.5 (mid-2024) — 200k tokens»
Number: 200,000
Source: Anthropic Claude 3.5 Sonnet release (June 21, 2024 / Oct 22, 2024)
Source date: 2024-06 and 2024-10
Lecture date: ~2026-09-15
Refresh cadence: yearly+
Days delta: ~440 days
Verify-on-day: no (historic fact)
Verdict: VERIFIED

Fact: «Claude 4.7 / актуальные модели OpenAI (2026) — порядка 1M токенов»
Number: 1,000,000
Source: Anthropic Claude Opus 4.7 release (Apr 16, 2026); platform.claude.com/docs
Source date: 2026-04-16
Lecture date: ~2026-09-15
Refresh cadence: quarterly (new model releases happen Q-by-Q)
Days delta: ~150 days from source to lecture
Verify-on-day: YES (cadence < 6 months, may have new flagship by then)
Verdict: VERIFIED for May 2026; NEEDS-REFRESH day-of-lecture

Fact: «`text-embedding-3-small` 1536 dim»
Number: 1536
Source: OpenAI API docs / Embeddings guide
Source date: 2024 (model release)
Lecture date: ~2026-09-15
Refresh cadence: yearly+ (stable production embedding model)
Days delta: ~600 days
Verify-on-day: no
Verdict: VERIFIED

Fact: «`text-embedding-3-large` 3072 dim»
Number: 3072
Source: OpenAI API docs
Source date: 2024
Refresh cadence: yearly+
Verdict: VERIFIED

Fact: «cl100k_base vocabulary ~100k, o200k_base ~200k tokens»
Number: ~100k and ~200k
Source: OpenAI tiktoken docs / GitHub
Source date: 2022 (cl100k), 2024-05-13 (o200k)
Refresh cadence: yearly+
Verdict: VERIFIED (more precisely: 100,256 for cl100k; 199,997 for o200k)

Fact: «Llama 3 tokenizer — SentencePiece, 128k vocab»
Number: 128k
Source claimed: Meta AI 2024
Source actual: Llama 3 model card / Hugging Face docs
Source date: 2024-04 (release)
Lecture date: ~2026-09-15
Refresh cadence: yearly+
Verify-on-day: no
Verdict: FALSE — Llama 3 uses tiktoken-based, NOT SentencePiece; vocab IS 128,256 (see P0-1)

Fact: «strawberry → [straw][berry] — 2 токена в cl100k_base»
Source: implicit, не cited
Verdict: DISPUTED — обычно 3 tokens (st/raw/berry); см. P0-2

Fact: «RU 2× стоимость EN tokenization»
Source claimed: OpenAI tokenizer benchmarks 2024 [FACT-CHECK]
Source date: 2024
Refresh cadence: quarterly (per chapter itself)
Days delta: ~430 days from claimed 2024 source to lecture
Verify-on-day: YES per chapter's own table
Verdict: NEEDS-REFRESH (run tiktoken empirically)

Fact: «GPT-3.5 4k → 8k (Turbo) → ... → 200k Claude → 1M (2026)»
Source: OpenAI archive / Anthropic news
Source date: 2022-2026
Refresh cadence: quarterly (per chapter)
Verify-on-day: yes for current flagship
Verdict: VERIFIED with caveat

Fact: «Hugging Face Inference Playground free + Llama-3-8B-Instruct available»
Source: HF platform 2024-2026
Source date: dynamic
Refresh cadence: monthly (HF platform changes пр subscription tiers)
Days delta: variable
Verify-on-day: YES (mandatory)
Verdict: VERIFIED partial — Llama-3-8B exists on Hub; free Playground availability variable

Fact: «strawberry test works (i.e., models miscount) — Claude 4.7 / GPT-5 / ChatGPT-5 may answer correctly»
Source: empirical / hedge
Refresh cadence: weekly
Days delta: variable
Verify-on-day: YES (mandatory)
Verdict: VERIFIED in May 2026:
  - GPT-5/5.2/5.5: STILL miscounts (Dec 2025 / 2026 reports)
  - Claude Opus 4.7: correct (3 r)
  Day-of-lecture mandatory pretest на 2-3 моделях.

Fact: «attention 64-128 параллельных голов в современных моделях»
Source: §3.1 line 271 (not cited; common knowledge)
Refresh cadence: yearly+ (стабильные орденки)
Verdict: VERIFIED (Transformer-XL, modern LLMs typically 32-128 heads per layer; chapter says "32-128", which is correct range)

Fact: «inference speed десятки токенов в секунду»
Source: §4.4 line 427 (qualitative)
Verdict: VERIFIED — reasonable for typical Claude/GPT inference (~30-80 tok/s on user-facing API)

Fact: «mistral 7B, Llama 3.1 8B, Llama 3.2 1B, Qwen 2.5 1.5B — 2026 local model sizes»
Source: §4.5 line 438
Refresh cadence: quarterly
Days delta: ~150-200 days
Verify-on-day: YES (new releases may have different recommendations)
Verdict: VERIFIED for May 2026 (these are all current Llama/Qwen versions)
```

---

## Day-of-lecture verify list (top priority for lecturer)

В порядке убывания criticality:

1. **strawberry test on 2-3 моделях.** (s07, §1.3 chapter)
   - ChatGPT (free / Plus) — продолжает ли miscount?
   - Claude.ai — продолжает ли correct?
   - YandexGPT / GigaChat — что отвечают?
   - Если все 3 correct → switch to «методология» или ROT-13 example.
   - Если все 3 miscount → keep current strawberry demo.

2. **HF Inference Playground availability.** (s27, §5.5 chapter)
   - huggingface.co/playground — UI alive?
   - Meta-Llama-3-8B-Instruct в free tier?
   - Temperature slider в UI?
   - Если нет — переключение на Together.ai (fallback 1) или Ollama (fallback 2).

3. **Context window cifras для current flagships.** (s16, §3.3 chapter)
   - Claude 4.7 1M — still latest? (или вышел 4.8, 5.0?)
   - GPT-5 context — current?
   - Если cifры сдвинулись — добавить новую точку «2026-Q3 — Claude X.X — N токенов» с тем же `1M → дальше` нарративом.

4. **strawberry tokenization split — pre-flight на tiktokenizer.vercel.app.** (s01, §1.3 chapter)
   - Verify какой split currently показывает `cl100k_base` для `strawberry`.
   - Adjust visual если 3-token, не 2-token.

5. **Llama-3 tokenizer correction.** (§1.1, §1.2 chapter)
   - Pre-publication — fix SentencePiece → tiktoken claim.
   - This is P0; обязательно перед production lecture.

6. **Cosine similarity numbers — empirical run.** (§2.2 chapter)
   - One-time setup: pick model (suggest `text-embedding-3-small`), run actual cosine similarity для 5 sentences, write real numbers в chapter + slide visual.

---

## Cross-consistency Lec-1 check

| Item | Lec-1 location | Lec-2 mention | Status |
|---|---|---|---|
| MCP — Model Context Protocol | §2.2 line 246 ('ноябрь 2024, Anthropic') | §5.5 line 541 ('Открытый стандарт... Anthropic в ноябре 2024 (см. Лекция 1 §2.2)') | ✓ MATCH |
| ReAct agent loop (Yao 2022) | §3.4.1 line 353 + Источники | §5.5 line 542 ('agent loop рассмотренный в Лекции 1 §3.4.1') | ✓ MATCH |
| RAG retrieval (Lewis 2020) | implicit | §2.3 line 231, §Источники line 569 (Lewis 2020) | ✓ MATCH |
| stateless inference | §3.2 line 275+ | §1.1 line 23 / §4.4 line 412 ('callback §3.2') | ✓ MATCH |
| PARTS framework (Persona/Action/Recipe/Template/Specification) | §3.3.1 + §3.3 line 311 + §5.2 line 688 (Лекция 12) | §3.2 line 292 ('PARTS-каркаса (... — см. Лекция 1 §3.3)') | ✓ MATCH (chapter references Лекция 12 + 1 §3.3, корректно) |
| Pearl 3 levels of causality | §4.8 line 590-615 | §5.4 line 506 ('callback Лекции 1 §4.8') | ✓ MATCH |
| Контекстное окно — ограничение | §3.3.1 (see TOC line 81) | §3.3 line 297 ('Лекция 1 §3.3.1 уже вводила понятие') | ✓ MATCH |
| Vaswani et al. 2017 arXiv:1706.03762 | §1.3 line 163 + Источники | §Введение line 77, §3.1 line 271, §Источники line 558 | ✓ MATCH (verified arXiv ID + 8 authors) |
| Local vs cloud (§4.2) | §4.2 line 499 | §4.5 line 442 ('callback Лекция 1 §4.2 и здесь не повторяется') | ✓ MATCH |
| ChatGPT release 2022 (Nov) | §1.3 line 163 | §3.3 line 301 ('GPT-3.5 в момент релиза ChatGPT (2022)') | ✓ MATCH |
| GitHub Copilot 46% (Octoverse) | §2.1 line 220, §3.6 worked ex | NO direct cite in body of Lec-2 (only listed in §Источники — see P1-7) | ⚠ P1-7 |
| DeepSeek / Llama-3 / Mistral | §2.2 line 234-242 | §4.5 line 436-438 ('Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B, Mistral 7B') | ✓ MATCH (sizes / names consistent) |
| ChatGPT, Claude, Gemini, DeepSeek, GigaChat, YandexGPT, Mistral Le Chat | §3.3 line 303 | §4.5 line 436 ('ChatGPT, Claude, GigaChat') + §1.3 line 144 ('ChatGPT, Claude, Gemini, GigaChat') | ✓ MATCH (no terminology drift) |

**No drift. All cross-references consistent. P1-7 (sources hygiene) is только housekeeping.**

---

## Curriculum sync check

Comparison против `library/lectures/lec-01/chapter.md` v3.1 §5.2 (карта семестра) and Drive doc реальной course structure (per CLAUDE.md):

| Claim in Lec-2 chapter | Reality | Status |
|---|---|---|
| Курс = 17 лекций × 3 модуля | Lec-1 §5.2 line 652-690 (17 лекций × 3 модуля; РК1/РК2/РК3 на C8/C12/C17) | ✓ MATCH |
| Лекция 17 = «Заключение / синтез» | Lec-1 line 677 («Модуль 3 — лекции 8, 13–17... плюс заключительный синтез знаний всего курса») | ✓ MATCH |
| Лекция 12 = тема промптинга (PARTS / CoT / few-shot / ReAct) | Lec-1 §5.3 line 688 («На лекции 12 мы формализуем PARTS...») | ✓ MATCH (хотя Lec-1 ранее имел внутренний conflict §5.2 vs §3.3 — already flagged in plan v2.1 §1.5, не критично для Lec-2) |
| Лекция 3 = «Агенты, RAG, API: как AI выходит за пределы чата» | Lec-1 §5.2 table line 662 («3 — Агенты, RAG, API: как AI выходит за пределы чата») | ✓ MATCH (exact wording) |
| Лекции 4-12 = индустрии | Lec-1 §5.2 «Лекции 4–7 пройдут по конкретным индустриям» | ⚠ MINOR drift — Lec-2 chapter §5.3 line 501 says «Лекции 4–7 пройдут по конкретным индустриям» AND §5.3 line 501 «Лекции 4-12 по индустриям» (line 344 in plan говорит «Лекции 4-12»; Lec-1 §5.2 reality более nuanced — модули 2 и 3 содержат разные подмножества индустрий) — но это nuance, не error. Both 4-7 и 4-12 acceptable. |
| Лекция 2 = «Как работают современные большие модели» | Lec-1 §5.3 line 690 («Что будет в лекции 2 "Как работают современные большие модели"») | ✓ MATCH (exact wording) |
| Семинар 2 «эффект температуры» | implicit (Lec-1 hints семинар 1 — общее, семинар 2 — после Лекции 2) | ✓ CONSISTENT |

**No curriculum hallucinations.** Lec-2 chapter accurately positions itself within the course.

---

## Counter-check

Per fact-checker self-discipline rules:

- **Verdict mapping check.** 2 P0 + 7 P1 + 4 P2 → REVISE (per agent prompt: «5+ P1 OR critical missing sources — must fix before show»). 7 P1 > 5, поэтому REVISE правильный verdict. ✓
- **No direction inversion missed.** Я просканировал claims с trend words («растёт», «увеличивается», «дороже», «больше»). Все direction claims VERIFIED против sources:
  - «контекстное окно выросло на порядки» — UP, verified ✓ (4k → 1M = ~250×).
  - «стоимость растёт квадратично» — verified (N² complexity for vanilla attention) ✓.
  - «миллион токенов ≈ в 16× дороже 100k» — math check: (1M/100k)² = 100 (теор max), на практике с FlashAttention/sparse/KV-кэш — ниже; chapter's «×16» более consistent с production cost behavior. Soft hedge OK, не direction inversion.
  - «RU в 2× дороже EN» — UP cost, verified direction (RU тratит больше токенов на тот же смысл).
  - «доверие к точности AI-ответов критичнее, чем год назад» (in Lec-1 callback, не повторяется в Lec-2) — verified в Lec-1 fact-check.
- **Citation hygiene check.** Quotes в кавычках проверены:
  - «Lost in the Middle: How Language Models Use Long Contexts» — exact paper title ✓.
  - «Attention Is All You Need» — exact paper title ✓.
  - «авторегрессионная» / «авторегрессивный» — terminology pair, не quote, OK.
  - «Кот съел мышь, потому что она была голодна» — example, not real cite.
  - «Программа упала, потому что она забыла обработать null» — example.
  - Все названия источников (Vaswani, Mikolov, Sennrich, Liu, Holtzman, Pearl, Yao, Lewis) — exact verified.
- **Mandatory file save.** Path verified `/home/levko/AI-usage-lessons/library/lectures/lec-02/qa-reports/2026-05-13-phase3-chapter-v1/fact-checker.md`, mkdir confirmed успешно.

**Verdict reconfirmed: REVISE.**

---

## Recommendations summary (priority order)

**Before chapter v2 (production-ready):**

1. **[P0-1]** Fix Llama-3 tokenizer attribution (SentencePiece → tiktoken). Multi-occurrence — 3 spots в chapter.
2. **[P0-2]** Fix strawberry token split — option A or B; verify через tiktokenizer.
3. **[P1-1, P1-2, P1-3]** Soften specific numbers without empirical attribution: RU/EN token costs, cosine similarity table, GPT-4 12288 dim.
4. **[P1-7]** Clean up bibliography — remove sources не cited в body главы 2.
5. **[P2-1, P2-2, P2-4]** Minor copy-edits: Holtzman year unify; cl100k year fix; «утечки» → формальнее.

**Day-of-lecture (lecturer responsibility):**

1. strawberry test on 2-3 моделях (mandatory).
2. HF Playground + Llama-3-8B-Instruct availability (mandatory).
3. Context window cifры — has Claude 4.8 / GPT-X released since chapter draft? Update s16 if needed.
4. Tiktokenizer screenshot freshness (s01 demo).

---

**Конец fact-checker report.** Status: REVISE → forward to book-editor для v2 правки.
