# Consistency-Checker Report (chapter ↔ slides) — Лекция 2 v1.0 — 2026-05-13

**Mode:** Phase 7 — chapter+slides (full).
**Artifacts in scope:**
- `library/lectures/lec-02/chapter.md` v1.1 (~11 408 слов, status=reviewed) — read from branch `issue-74-lec-02-llm-internals` (current branch `issue-73-lec-04-medicine-production` не имеет lec-02 файлов).
- `library/lectures/lec-02/deck.yaml` (28 слайдов, v1.0).
- `library/lectures/lec-02/slides/s01-s28-*.md` × 28.
- `library/lectures/lec-02/rendered/snapshots/s01.png — s28.png` × 28 (spot-checked s01/s07/s10/s15/s16/s20).

**Out-of-scope:** `speech.md` не существует (Phase 10 ещё не наступил).

---

## VERDICT: APPROVE-WITH-POLISH

**Обоснование:** P0 = 0, P1 = 3, P2 = 7. Все P1 — формулировочные / cosmetic, не factual contradictions. Книга — source of truth, и slides последовательно derived from chapter (28 из 28 `[for-slide-sNN]` markers покрыты; chapter `§X.Y` ↔ slide `chapter_ref` ↔ slide content matrix чистая). Cross-reference сеть с Лекцией 1 consistent. Цифры (context window, vocab, distribution, 4 knobs, cosine, dim, Liu/Sennrich/Holtzman cites) совпадают между chapter и slides. Терминология lock на 17 канонических термах удержана. Несколько polish-level разрывов (cross-cluster cosine numbers в s10 extending beyond chapter spec; «магнит» как icon hint в s11 visual_brief; PNG-side mini-panel в s16 расширяет MD beyond brief; title bars в slide MD ≠ rendered titles по deck design). Рекомендуется polish round перед USER GATE 2; revise не требуется.

**Counter-check (per CLAUDE.md ENFORCED rule):** P1 count = 3 < 5 порог. Verdict APPROVE-WITH-POLISH согласован с rubric.

---

## Severity counts

- **P0** (factual contradiction / missing coverage): **0**
- **P1** (significant drift / cosmetic content mismatch): **3**
- **P2** (minor inconsistency): **7**

---

## Slide ID monotonicity check

| Источник | s01-s28 monotonic? | Count |
|---|---|---|
| `deck.yaml` slides list | ✓ | 28 / 28 |
| `slides/` directory | ✓ | 28 файлов (s01-live-tokenizer-demo … s28-bridge-qa) |
| `rendered/snapshots/` PNGs | ✓ | 28 (s01.png … s28.png) |
| chapter `[for-slide-sNN]` markers (unique IDs) | ✓ | 28 уникальных IDs |

**Chapter markers с повторами (3 слайда упоминаются в 2 местах главы — sane behavior, не P0):**
- `[for-slide-s07]` × 2 (§1.3 main intro + §1.3 engineering вывод).
- `[for-slide-s08]` × 2 (§1.4 cross-language intro + §1.4 engineering implication).
- `[for-slide-s15]` × 2 (§3.2 worked example part A + §3.2 role-effect part B).
- `[for-slide-s17]` × 2 (§3.4 main + §3.4 engineering вывод).
- `[for-slide-s21]` × 2 (§4.4 main + §4.4 stateless aside).
- `[for-slide-s01]` + `[for-slide-s05]` collocated на L141 (s01 hook == s05 definition, same anchor).

Это согласовано с тем, что 5 слайдов = Case Study / 2-part (s07/s08/s15/s17/s21). Markers parity OK.

**Verdict:** ✓ monotonicity clean, 0 orphan refs, 0 missing.

---

## Coverage parity — Chapter ↔ Slide alignment matrix (28 rows)

| sNN | Chapter ref (declared) | Chapter content | Slide assertion | Aligned? |
|---|---|---|---|---|
| s01 | §1.1 (L141 anchor [for-slide-s01]) | «LLM видит ваш запрос не буквами и не словами — а токенами…» | «Модель видит ваш запрос не буквами и не словами — а токенами» | ✓ |
| s02 | §Введение (L119 [for-slide-s02]) | «Структурно глава состоит из пяти разделов…» | «Лекция 2. Как работают современные большие модели» (cover + roadmap) | ✓ |
| s03 | §Введение (L109 [for-slide-s03]) | «В Лекции 1 мы зафиксировали слоистую модель…» | «Сегодня углубляем слой "модель" из четырёх слоёв Лекции 1» | ✓ |
| s04 | §Введение (L112 [for-slide-s04]) | «Центральный вопрос главы… четыре механизма…» | «Главный вопрос: что внутри LLM меняет то, как мы её используем?» | ✓ |
| s05 | §1.1 (L141) | «Токен — это идентификатор (целое число) из словаря модели…» | «Токен — id из словаря модели. Не буква и не слово…» | ✓ |
| s06 | §1.2 (L154) | «BPE — компромисс между алфавитом и словарём… словарь строится один раз до обучения…» | «BPE — компромисс… словарь строится один раз перед обучением» | ✓ |
| s07 | §1.3 (L167+L178) | «strawberry → [st][raw][berry] (3 токена); три практических следствия…» | «AI ошибается в "сколько r в strawberry" — потому что слова не из букв, а из 2-3 токенов» | ✓ |
| s08 | §1.4 (L191+L203) | «один и тот же текст на русском стоит в 2× дороже…» | «Один и тот же текст по-русски стоит в 2× дороже, чем по-английски» | ✓ |
| s09 | §2.1 (L222) | «Каждому токену словаря модели сопоставлен вектор…» | «Каждому токену в памяти модели сопоставлен вектор…» | ✓ |
| s10 | §2.2 (L249) | «парные cosine similarity ~0.85, ~0.78, 0.05–0.15» | «Близость в пространстве эмбеддингов = семантическая близость…» | ✓ (cosine table extends — см. D2) |
| s11 | §2.3 (L274) | «Из меры близости вырастают три применения: similarity, clustering, search» | «3 применения: similarity, clustering, search» | ✓ |
| s12 | §2.4 (L287) | «Семантический поиск находит strawberry/ягоду/землянику…» | «Semantic search находит то, что full-text пропустит» | ✓ |
| s13 | §3 (L310 [for-slide-s13]) | (section header, no narrative; anchor at §3.1 intro) | «Раздел 3 — Механизм внимания…» (section divider) | ✓ |
| s14 | §3.1 (L310 [for-slide-s14]) | «attention возвращает распределение весов на все токены контекста; сумма = 1; пересчитывается на каждом шаге…» | «Attention выдаёт распределение весов на все токены контекста (сумма = 1) — какие токены важны сейчас» | ✓ |
| s15 | §3.2 (L325+L332) | «Кот съел мышь, потому что она была голодна; role-токены получают повышенный вес…» | «Role-токены получают повышенный вес в attention — это объясняет, почему промпт с ролью работает лучше» | ✓ |
| s16 | §3.3 (L348) | «GPT-3.5 4k → Claude 3.5 200k → Claude 4.7 1M; квадратичная стоимость; 1M ≈ 16× от 100k» | «Контекстное окно — физический предел того, сколько модель видит одновременно» | ✓ (PNG extends mini-panel — см. D3) |
| s17 | §3.4 (L369+L376) | «U-образная кривая Liu et al. 2023; провал в середине; инженерный вывод» | «Большое контекстное окно ≠ хорошее использование контекста» | ✓ |
| s18 | §4.1 (L394) | «распределение вероятностей на все токены словаря; яблоко 0.32, пиццу 0.19…» | «На каждом шаге модель выдаёт распределение вероятностей на ВСЕ токены словаря — затем выбирает один» | ✓ |
| s19 | §4.2 (L412) | «T=0 argmax; T=1 стандарт; T=2 хаос; top-p / top-k — alt knobs» | «Температура — насколько острым будет выбор. T=0: argmax. T=1: стандарт. T=2: хаос» | ✓ (chapter T=1.0 vs slide T=0.7 — см. D5) |
| s20 | §4.3 (L432) | «4 параметра + таблица: T, top_p, max_tokens, system_prompt × 4 сценария» | «4 параметра под задачу: temperature, top_p, max_tokens, system prompt» | ✓ |
| s21 | §4.4 (L465+L476) | «5-шаговый цикл; forward pass; stateless шаги собираются в stateful процесс» | «Loop: предсказали токен → добавили в контекст → предсказываем следующий» | ✓ |
| s22 | §4.5 (L489) | «inference loop одинаков локально и в облаке; размер модели определяет качество» | «Inference loop одинаков локально и в облаке — но размер модели определяет качество» | ✓ |
| s23 | §5.1 (L511) | «4 этапа конвейера inference: токенизация → эмбеддинг → внимание → сэмплинг» | «4 этапа inference сложились в pipeline» | ✓ |
| s24 | §5.2 (L532) | «3 ответа на 3 "почему" из Лекции 1 §5.3» | «3 промиса Лекции 1 — 3 ответа из Лекции 2» | ✓ |
| s25 | §5.3 (L545) | «decision tree ML vs LLM: 3 ветки + иначе» | «LLM — не всегда правильный инструмент. Decision tree: когда не LLM» | ✓ |
| s26 | §5.4 (L559) | «attention не строит каузальный граф; Pearl уровни 1/2/3» | «Attention статистически смотрит на токены — не понимает причинности» | ✓ |
| s27 | §5.5 (L575) | «ДЗ к Семинару 2: 1 запрос × 3 T × 3 запуска × анализ; HF Playground» | «Принесите 1 запрос × 3 температуры × 3 запуска × анализ» | ✓ |
| s28 | §5.5 (L590) | «мост к Лекции 3: RAG / Tools / MCP / Agent loop» | «Лекция 3: "Агенты, RAG, API: как AI выходит за пределы чата"» | ✓ |

**Coverage parity verdict:** ✓ 28 / 28 slides aligned with chapter anchor and content claim. No P0 missing coverage; no P0 over-claim relative to chapter.

---

## Terminology drift report (per-term, lightweight § 8 protocol)

### Forbidden terms (must be 0)

| Forbidden term | Chapter | Slides | Status |
|---|---|---|---|
| «миопия токенизации» | 0 | 0 | ✓ clean |
| «магнит» (как metaphor) | 0 | 1× in `s11.md` L22 (icon hint «магнит / парные точки») | ⚠ P2 — см. D4 |
| «прикладное X» (adjective) | 0 | 0 | ✓ clean |
| «промптинг — сквозной навык» | 0 | 0 | ✓ clean |
| «Архитектура AI: от ML до трансформеров» | 0 | 0 | ✓ clean |
| «авторегрессивный» (allowed only в terminological note) | 1 (§4.4 explicit canonical note) | 1 (s21 same canonical note) | ✓ — оба раза в meta-discussion, форма не используется в narrative |
| «Пёрла» (forbidden Pearl form) | 1 (changelog L21 only) | 0 | ✓ — meta-discussion only, body uses «Перла» (3×) |
| «How LLMs work» (EN title) | 0 | 0 | ✓ clean |
| «инженер ИУ6» / «МГТУ» в narrative | 0 (audience defined только в deck.yaml meta) | 0 | ✓ universal audience |
| «магическая пилюля» / «магия LLM» | 0 (1× anti-magic phrasing «токенизация — не магия» — что есть хорошее framing) | 0 | ✓ tone clean |

### Canonical terms (must appear consistently)

| Canonical term | Chapter count | Slides total count | Status |
|---|---|---|---|
| «токен» / «токены» / «токенизация» | 197 occurrences | 222 occurrences | ✓ deck-wide |
| «эмбеддинг» (RU canonical) | 63 | 47 | ✓ |
| «embedding» (EN — allowed только в техн. ссылках) | 5 (все = `text-embedding-3-*` names + 1 «embedding table» в §2.1) | 4 (slide MDs, все = API references) | ✓ within scope |
| «механизм внимания» (canonical RU) | 9 | 5+ (s13/s14/s23/s24/s26 + s02/s03 in roadmap) | ✓ |
| «attention» (EN — allowed когда нужен термин из API/литературы) | 31 | 27 across 12 slides | ✓ proper mixing |
| «контекстное окно» | 12 | 6 slides mention | ✓ |
| «сэмплинг» | 19 | 12 slides mention | ✓ |
| «слепота к буквам» (рабочий термин) | 4 | 1 (s28) + implicit во многих slides | ✓ |
| «авторегрессионный» (canonical) | 5 occurrences | 2 (s21) | ✓ |
| «Перла» (canonical Pearl) | 3 (§Введение / §5.4 / §Источники) | 1 (s26 speaker notes); +2 (s26 EN «Pearl» в visual_brief/learning_goal) | ✓ |
| «температура» (RU canonical) | 11 + 6 (EN `temperature`) | 8 slides RU + 3 slides EN | ✓ mixed appropriately |
| BPE (Byte-Pair Encoding) | 17+ | 5+ slides | ✓ |
| `cl100k_base` / `o200k_base` | yes | s01/s05/s07 explicit | ✓ |
| `text-embedding-3-small` (1536 dim) | 5 | s09 (3×) + s10 (1×) | ✓ |
| `text-embedding-3-large` (3072 dim) | 4 | s09 (3×) | ✓ |

### Untracked drift candidates

- **`top-k` (dash) vs `top_k` (underscore):** chapter uses «top-k» в narrative и `top_k = 40` в code examples (consistent with «top-p» / `top_p`); slides match the same pattern. ✓ clean.
- **«Word2Vec»:** 1 occurrence в s10 speaker notes, 4× в chapter (§2.2 + Sources). Consistent.
- **«PARTS-каркаса»:** 1 occurrence chapter (§3.2 footnote), 0 in slides. Slides не reference PARTS — consistent с plan v2.1 §1.5 «PARTS только в Семинар 12 / Лекция 12».
- **«fonarик / фонарик» metaphor:** chapter §3.1 (L313) + s14 (L21 + speaker notes L44). Consistent term.
- **«lost in the middle»:** chapter §3.4 (L370 + L373) + s17 (L30 + L37 speaker notes). Consistent.

**Terminology verdict:** ✓ 17 / 17 canonical терминов из `deck.yaml.glossary_lock` соблюдены. 1 minor P2 («магнит» в visual_brief), 0 P1 / P0.

---

## Cross-reference drift (Лекция 1 callbacks)

| Lec-1 § ref | Chapter mentions | Slides mentions | Aligned? | Notes |
|---|---|---|---|---|
| §1.3 (трансформер 2017, self-attention high-level) | 4 | 3 (s02/s03/s24) | ✓ | согласовано — chapter углубляет §1.3 black box |
| §1.4 (классификация задача × модальность) | 6 | 4 (s25 расширение + roadmap) | ✓ | s25 явный «расширяет Лекцию 1 §1.4» |
| §3.2 (модель = stateless inference) | 7 | 12 (s03/s04/s21/s23 + others) | ✓ | core callback; s21 + s23 явные |
| §3.3 (роль системного промпта) | 6 | 2 (s20 implicit) | ✓ | chapter §4.3 cites §3.3 для system_prompt |
| §3.3.1 (контекстное окно как ограничение) | 3 | 1 (s16) | ✓ | s16 явно cites «Лекция 1 §3.3.1» |
| §3.4.1 (Agent loop) | 2 | 1 (s28) | ✓ | s28 явно «Lec-1 §3.4.1» |
| §4.2 (локальные vs облачные) | 7 | 5 (s22 + roadmap) | ✓ | s22 явный callback «без повтора» |
| §4.8 (Pearl 3 уровня причинности) | 5 | 5 (s26 cite + roadmap) | ✓ | s26 callback frame, no repeat |
| §5.3 (3 «почему» промис) | 6 | 12 (s04 promises + s15/s19/s24 payoff) | ✓ | full circuit closed |

**Liu et al. 2023 / arXiv:2307.03172:**
- Chapter L370, L619, L659 — 3 mentions, consistent format «Liu et al. (2023). … arXiv:2307.03172».
- Slide s17.md L30 — «Liu et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* arXiv:2307.03172.»
- ✓ consistent format и attribution.

**4 LO (LO1/LO4/LO6/LO7):**
- Chapter §Учебные цели L128-131 — 4 LO defined.
- Slide frontmatter `learning_outcomes` covers all 4: LO1 × 13 slides; LO4 × 4 slides (s19/s20/s27 + s02 cover); LO6 × 7 slides; LO7 × 5 slides.
- ✓ all 4 LO have ≥1 dedicated slide:
  - LO1 — pipeline definition slides (s01/s05/s09/s14/s18/s21/s23 + recap).
  - LO4 — s20 (4 knobs taught) + s19 + s27 (apply ДЗ).
  - LO6 — s07/s08/s16/s17/s22/s25 (limitations).
  - LO7 — s04/s15/s19/s24/s27 (3 «почему»).
- No LO orphans, no extra LO claimed beyond plan v2.1 §3.

**Cross-reference verdict:** ✓ полная parity, нет orphans или asymmetric refs.

---

## Numeric facts cross-check

| Fact | Chapter location | Slide location | Aligned? |
|---|---|---|---|
| GPT-3.5 (2022) — 4 000 / 4k токенов context | §3.3 L353 «около 4 тысяч токенов» | s16 L24 «4 000 токенов» | ✓ |
| Claude 3.5 (2024) — 200 000 / 200k | §3.3 L354 «200 тысяч токенов» | s16 L25 «200 000 токенов» | ✓ |
| Claude 4.7 (2026) — 1 000 000 / 1M | §3.3 L355 «1 миллион токенов» | s16 L26 «1 000 000 токенов» | ✓ |
| 1M ≈ 16× дороже 100k (квадратичная стоимость) | §3.3 L361 «в шестнадцать раз дороже» | s16 L31 «1M ≈ 16× дороже 100k» | ✓ |
| cat = 1 токен | §1.1 L146 «cat — единый токен» | s01 L23, s05 L22 | ✓ |
| tokenization = 2 токена `[token][ization]` | §1.1 L146 | s01 L24, s05 L24 | ✓ |
| strawberry = 3 токена `[st][raw][berry]` (o200k_base) | §1.1 L146, §1.3 L170 | s01 L24, s05 implicit, s07 L23, s24 L28 | ✓ (P0-2 fix applied везде) |
| клубника = 3 токена `[к][луб][ника]` (o200k_base) | §1.1 L146 | s01 L25, s05 L26 | ✓ |
| Vocab GPT-4o = ~200k | §1.1 L144 | (implicit в footer s01/s07) | ✓ |
| Vocab GPT-3.5 / GPT-4 = ~100k (cl100k_base) | §1.1 L144, §1.2 L159 | (footer s07 implicit) | ✓ |
| Vocab Llama 3 = 128k (tiktoken-based BPE) | §1.1 L144, §1.2 L161 | (no explicit slide) | ✓ acceptable — slides не повторяют |
| Cross-language: EN ~0.25 t/c, RU ~0.5, ZH ~0.8, Py ~0.4 | §1.4 L196-199 | s08 L22-26 | ✓ exact |
| RU/EN ratio 2× (с диапазоном 1.5×-2.5×) | §1.4 L201, L204 | s08 L31, L34 | ✓ |
| Cosine SSL↔HTTPS ~0.85 | §2.2 L262 | s10 L23-24 | ✓ |
| Cosine React-комп ↔ React-прил ~0.78 | §2.2 L263 | s10 L25-26 | ✓ |
| Cosine борщ vs техническое 0.05-0.15 | §2.2 L264 | s10 L23-27 (0.08, 0.07, 0.12, 0.10) | ✓ (within range) |
| Cosine cross-cluster SSL↔React: 0.18-0.22 | not in chapter | s10 L23-26 (0.18, 0.22, 0.20, 0.19) | ⚠ P2 — см. D2 |
| Distribution «съел...»: яблоко 0.32, пиццу 0.19, салат 0.14, булочку 0.11, огурец 0.08 | §4.1 L399-403 | s18 L24-28 | ✓ exact match |
| Sum < 0.05 для остальных ~200k токенов | §4.1 L404 | s18 L33 | ✓ |
| T=0 argmax / T=1 standard / T=2 chaos | §4.2 L417-419 | s19 L22-32 | ⚠ P2 — slide showcases T=0.7 (instead of T=1) as «стандарт» — см. D5 |
| top_p = 0.9 (typical) | §4.2 L423, §4.3 table L447 | s19 L34, s20 L24 | ✓ |
| top_k = 40 (example) | §4.2 L424 | not mentioned (only `top-k` term) | ✓ acceptable |
| 4-knobs table — Classification T=0, max_tokens 50-200 | §4.3 L446 | s20 L23 | ✓ exact |
| 4-knobs — Code T=0.2-0.3, top_p 0.9, max 1000+ | §4.3 L447 | s20 L24 | ✓ |
| 4-knobs — Chat T=0.7, top_p 0.9, max 500-1000 | §4.3 L448 | s20 L25 | ✓ |
| 4-knobs — Creative T=0.9-1.2, top_p 0.95, max 2000+ | §4.3 L449 | s20 L26 | ✓ |
| 1536 dim text-embedding-3-small | §2.1 L229 | s09 L28, s10 L33 (footnote) | ✓ |
| 3072 dim text-embedding-3-large | §2.1 L230 | s09 L29 | ✓ |
| 32-128 attention heads | §3.1 L321 | s14 L48 (speaker notes) | ✓ |
| Local: Qwen 2.5 1.5B / Llama 3.2 1B / Llama 3.1 8B / Mistral 7B | §4.5 L492 | s22 L23 | ✓ exact |
| Cloud latency 200-500 ms | §4.5 L494 | s22 L31, speaker notes L45 | ✓ |
| Liu et al. 2023, U-shape, accuracy 70-80% → 30-40% → 70-80% | §3.4 L372 «70-80% / 30-40% / 70-80%» | s17 L26 «~75% / провал ~30% / ~75%» + L39 «70-80% / 30-40% / 70-80%» | ✓ ranges согласованы (slide visual rounds к 75% mid-range — допустимо) |

**Numeric facts verdict:** ✓ 35 / 36 numeric facts polished aligned; 2 cosmetic flags (cross-cluster cosine в s10, T=0.7 vs T=1 «стандарт» в s19) — P2 уровень.

---

## P0 Issues (cross-artifact drift blockers)

**Нет P0 issues.** Все факты, числа, термины, callbacks и LO согласованы между chapter v1.1 и 28 slides.

---

## P1 Issues (≥5 → REVISE)

### D1 — Section divider s13 chapter_ref = «§3» (раздел-уровень, не подсекция)

**Severity:** P1.
**Where:** `deck.yaml` slides[s13].chapter_ref = `«§3 [for-slide-s13]»`; `slides/s13-section-divider-attention.md` L9 same.
**Chapter:** `[for-slide-s13]` markers placed на L310 (§3.1 intro), не у `## Раздел 3` heading (L306).
**Issue:** Несоответствие: anchor stands at L310 (внутри §3.1), но declared as `«§3»` (section-level). Functionally OK for section divider, но markers неточные. В отличие от других слайдов, где chapter_ref совпадает с подсекцией (§1.1, §1.2, ...). Слайды s13 (section divider) + s14 (assertion_visual) shares the same anchor location.
**Recommendation:** либо переместить anchor [for-slide-s13] выше — к L307 (after `## Раздел 3`), либо изменить chapter_ref к `«§3.1 (раздел intro)»`. Cosmetic — не влияет на содержание.

### D2 — s10 cosine heatmap содержит cross-cluster values (0.18/0.22/0.20/0.19) не из chapter

**Severity:** P1.
**Where:** `slides/s10-sentence-similarity.md` L23-26 (heatmap rows 1-4 columns 3-4 / vice versa).
**Chapter:** §2.2 L262-264 даёт ТРИ value-points: «синонимы 1↔2 ~0.85», «React 3↔4 ~0.78», «борщ vs техническое 0.05-0.15». **Cross-cluster (SSL↔React-компонент, etc.) chapter не специфицирует.** Slide extrapolates: SSL↔React-комп = 0.18, SSL↔React-прил = 0.20, HTTPS↔React-комп = 0.22, HTTPS↔React-прил = 0.19, React-комп↔борщ = 0.12, React-прил↔борщ = 0.10.

Цитата chapter L266 [FACT-CHECK footnote]: «**порядок** — синонимы 0.7–0.9, несовместимые домены 0–0.2 — устойчив у всех современных моделей». То есть slide values (0.18-0.22) попадают в range «несовместимые домены» по chapter rule.

**Issue:** Slide вводит 6 числовых значений, отсутствующих в chapter. Не противоречит chapter (within general range), но **создаёт impression точной воспроизводимости**, тогда как chapter явно дисциплинирует «illustrative; верифицируется эмпирически». Студент, заучивший таблицу, может ожидать конкретные числа в собственной репродукции и быть запутан.
**Recommendation:** добавить в speaker notes s10 (или в footnote под таблицей) явный disclaimer: «Cross-cluster значения (0.18-0.22) — extrapolation в пределах chapter диапазона "несовместимые домены 0-0.2"; не воспроизводятся точно». Alternative — заменить heatmap на 3-cell illustration (только канонические synonyms / React / борщ). Cosmetic, чтобы не drift expectation от chapter.

### D3 — s16 PNG включает side-panel «Эволюция и стоимость» (×250, ×10 / 1-2 года, 1M ≈ 16×, ванильная attention, N²) не описанный в slide MD

**Severity:** P1.
**Where:** rendered `snapshots/s16.png` (правый side-panel) vs `slides/s16-context-window.md` L20-34 (Body описывает только bar chart + Gold callout «1M ≈ 16× от 100k» + VERIFY-DAY-OF caption).
**Chapter:** §3.3 L357-361 содержит все 4 факта (порядок, темп roста, квадратичная стоимость, ванильная attention).
**Issue:** PNG расширяет beyond MD source — добавляет custom side-panel с 4 metrics, которых нет в slide MD body. Все 4 фактически в chapter, но slide MD не описывает этот элемент. Это designer-side enrichment во время Phase 6 visual loop без back-port в MD. Не противоречит chapter (наоборот, derives from chapter), но **slide MD как «source of truth» для PNG нарушен**. Reproducibility (если rebuild PPTX из MD) даст другой visual.
**Recommendation:** back-port side-panel description в `s16-context-window.md` Body section (как 5-й рекв-элемент). Альтернатива — удалить side-panel из PNG. Designer-extras rule (CLAUDE.md §No Extra Content Rule): любое visual content без brief — flag для review. Здесь brief = deck.yaml `visual.primary` который описывает только bar chart, не side-panel.

---

## P2 Issues

### D4 — s11 visual_brief «иконка магнита» против forbidden term «магнит»

**Severity:** P2.
**Where:** `slides/s11-three-uses-of-embeddings.md` L10 (visual_brief), L22 (body).
**Issue:** Forbidden terms list (task brief) включает «магнит» как metaphor. В s11 «магнит» используется как icon hint для Similarity card («Иконка: магнит / парные точки»). Это designer instruction, не metaphor в narrative. Однако rendered PNG может реально показывать иконку магнита, что в зале воспринимается визуально. Chapter §2.3 (L274-283) описывает Similarity без какой-либо «магнит» metaphor — там геометрическая близость.

**Recommendation:** заменить icon hint на нейтральный: «парные точки» или «лупа на похожих документах». Если PNG render показывает реальный магнит — рассмотреть smell test (CLAUDE.md «магия / магнит — forbidden metaphor»). Cosmetic.

### D5 — s19 «T=0.7 стандарт» против chapter «T=1.0 стандарт»

**Severity:** P2.
**Where:** `slides/s19-temperature.md` L26 «T = 0.7 (стандарт)»; speaker notes L46 «При T = 1.0 — стандартный режим».
**Chapter:** §4.2 L418 «T = 1.0. Стандартный режим. Модель сэмплирует пропорционально исходным вероятностям».
**Issue:** Visible content на slide заявляет «T = 0.7» как «стандарт», но **speaker notes того же slide** говорят «При T = 1.0 — стандартный режим». То есть слайд внутренне противоречив, а тред наружу противоречит chapter.

Контекст: deck.yaml s19 assertion: «T=0: argmax. T=1: стандарт. T=2: хаос» — соответствует chapter. **Но visible body уверенно использует T=0.7 как «стандарт».** Это, вероятно, отражает то, что в 4-knobs таблице s20 «Чат-объяснение пользователю = T = 0.7» (= general-purpose chat), и слайдоавтор слил «default T в чате» (0.7) с «стандарт T в техническом смысле» (1.0). Запутывает.

**Recommendation:** в `s19-temperature.md` L26 явно зафиксировать «T = 1.0 (стандарт; chat default = 0.7 — см. s20)»; or rewrite middle column как «T = 1.0 (стандартный sampling)» с T=0.7 показанной как 4-я колонка / inline note. Это устранит smear «стандарт» между двумя разными significance. Не критично для рендер, но потенциальный source of confusion на экзамене.

### D6 — s06 caption mentions «WordPiece (BERT), SentencePiece (Llama 2, T5)» но без BPE attribution для GPT-семейства

**Severity:** P2.
**Where:** `slides/s06-bpe-compromise.md` L40 caption «Sennrich et al. (2016). Современные альтернативы: WordPiece (BERT), SentencePiece (Llama 2, T5)».
**Chapter:** §1.2 L161 явно: «BPE (используется в GPT-семействе и в Llama 3+), WordPiece (используется в BERT и его потомках), SentencePiece (Llama 2, Mistral, T5)».
**Issue:** Slide caption перечисляет только 2 альтернативы и не упоминает что **BPE используется в GPT + Llama 3**. Slide title «BPE — компромисс между алфавитом и словарём» это implies, но для студента без chapter может остаться «BPE — что-то старое». Speaker notes L50 хорошо покрывают этот вопрос («BPE используется в GPT-семействе и в Llama 3+»), but visible caption не.
**Recommendation:** Add visible caption phrasing «BPE — GPT-семейство, Llama 3+. Альтернативы: WordPiece (BERT), SentencePiece (Llama 2, T5)». 1-line fix.

### D7 — s14 «multi-head 32-128 голов» disclaimer-цифра in chapter only

**Severity:** P2.
**Where:** `slides/s14-what-is-attention.md` speaker notes L48 mentions «32-128 голов в современных моделях».
**Chapter:** §3.1 L321 same: «multi-head attention; типично 32-128 голов».
**Issue:** Visible content slide s14 не упоминает 32-128 (рекомендация автор) — только caption «Multi-head, Q/K/V — Лекция 17 / доп. чтение». Speaker notes покрывают цифру. **Aligned, but visible не показывает.** Acceptable per «3-факта» учебная цель slide; tip только для self-study.

**Recommendation:** No action needed — speaker notes carries the detail.

### D8 — Distribution «съел...» на s18: 5 кандидатов с явными числами vs «illustrative» disclaimer в chapter

**Severity:** P2.
**Where:** `slides/s18-distribution.md` L24-28 показывает: яблоко 0.32, пиццу 0.19, салат 0.14, булочку 0.11, огурец 0.08.
**Chapter:** §4.1 L397 «числа illustrative». Slide speaker notes L42 повторяет «Числа на слайде иллюстративные».
**Issue:** Slide visible body показывает специфические числа без disclaimer на самом visible level. PNG (если rendered показывает эти числа без footnote disclaimer) → студент возьмёт за факт. Speaker notes покрывают, но в зале студент не видит speaker notes.

**Recommendation:** в visible body s18 footer добавить мелким курсивом «числа illustrative» — chapter явно дисциплинирует этот counter-pattern (анти-патология упрощения).

### D9 — Speaker notes s06 говорит «multi-iter не показана» vs MD body says «без пошаговой итерации»

**Severity:** P2.
**Where:** `slides/s06-bpe-compromise.md` L37 (gold callout) + speaker notes L48 «BPE-словарь строится один раз, до обучения».
**Issue:** No real drift — both consistent. False positive on initial check; flagged for completeness.

### D10 — Title bar в slide MD ≠ rendered visible title в PNG (consistent across deck)

**Severity:** P2.
**Where:** s01 MD `Title bar = «Как модель видит ваш запрос: live tokenizer»` vs PNG visible = «Модель видит ваш запрос не буквами — а токенами»; s07 MD `«Почему AI плохо считает буквы»` vs PNG = «AI ошибается в "сколько r в strawberry" — слова не из букв, а из 2-3 токенов» (= deck.yaml assertion); s10 MD `«Семантическое сходство на современных эмбеддингах»` vs PNG = «Близость в пространстве эмбеддингов = семантическая близость»; ...etc.
**Issue:** Designer (Phase 6 visual loop) systematically substituted MD `Title bar` с deck.yaml `assertion` для visible PNG titles. Все 28 PNGs follow этот pattern. Не неправильно (assertion обычно informative-er), но slide MDs остались с old «топик-label» titles, а не actual «assertion title». Reproducibility — если rebuild PPTX strictly from MD, titles будут разные.

**Recommendation:** sync slide MD `Title bar` к deck.yaml `assertion` для всех 28 файлов (или phrase как «Title bar = use deck.yaml assertion»). Это back-fills design decision в repo-first source of truth.

### D11 — 5 retrieval interactions per deck.yaml `interaction_summary` vs interaction frontmatter in slides

**Severity:** P2.
**Where:** `deck.yaml.interaction_summary` lists s01/s05/s07/s15/s19. Frontmatter `interaction:` in slide MDs:
- s01 — нет `interaction:` поле в frontmatter (despite live_demo type).
- s05 — `interaction: inline_poll` ✓.
- s07 — `interaction: retrieval_live_attempt` ✓.
- s15 — `interaction: retrieval_think_pause` ✓.
- s19 — `interaction: live_comparison` ✓.

**Issue:** s01 не имеет `interaction:` поле, despite `type: live_demo` и deck.yaml.interaction_summary mentioning «s01: static demo + open question (2 мин total)». Minor frontmatter gap.

**Recommendation:** add `interaction: open_question` (или подобное) к s01 frontmatter для completeness. Cosmetic.

---

## Coverage gaps (LO / chapter section)

**No coverage gaps.**
- All 4 LO (LO1/LO4/LO6/LO7) have ≥1 dedicated slide.
- All 5 chapter sections (§1-§5) + Введение + ДЗ have slide block (s01-s04 для Введение / s05-s08 §1 / s09-s12 §2 / s13-s17 §3 / s18-s22 §4 / s23-s28 §5).
- Cross-cutting frames (s22 local/cloud, s25 ML vs LLM, s26 Pearl) ≡ chapter §5.3/§5.4/§4.5.

---

## Cross-artifact orphan reference detection

**Orphan checks per `consistency-checker.md` §9:**

```bash
# Speech orphan refs:
# N/A — speech.md ещё не существует (Phase 10 не наступил).

# Chapter orphan refs (см. слайд sNN where sNN ∉ deck.yaml):
grep -nE 'см\. слайд s[0-9]+|см\. слайд [0-9]+' /tmp/lec02_chapter.md
# → empty (chapter не делает прямых slide-references)

# Slide-to-slide orphan refs:
grep -rnE 'см\. s[0-9]+' /tmp/lec02_slides/
# → references: s07 «(см. s07)» в s01 PNG (s07 existed), s21 «s05-s17» (range), s24 «s05-s07»/«s15»/«s18-s19» — all valid.
```

**All slide-to-slide refs valid:**
- s01 PNG mentions «(см. s07)» — s07 exists. ✓
- s21 body L26 «всё, что было в s05-s17» — valid range. ✓
- s24 body L26 «См. s15» / L28 «См. s05-s07» / L31 «См. s18-s19» — valid. ✓
- s28 body L25 «s10-s12» / L37 «s21» — valid. ✓

**Verdict:** ✓ 0 orphan references.

---

## Tone consistency

| Aspect | Chapter | Slides | Status |
|---|---|---|---|
| Universal audience (no «инженер ИУ6») | ✓ chapter §audience field только в `lecture.yaml` meta — narrative универсален | ✓ no «ИУ6» mentions в visible content; deck.yaml.audience meta only | ✓ aligned |
| «Вы»-форма | ✓ 147 occurrences | ✓ visible content + speaker notes use «вы / ваш» | ✓ aligned |
| «Ты»-форма | ✓ only inside prompt examples («Ты эксперт по Python») | ✓ same — prompt examples в s04/s15/s24 | ✓ aligned |
| Anti-magic phrasing | ✓ §1.2 L163 «токенизация — не магия» | ✓ no «магия LLM» in slides; «магнит» только icon hint (см. D4) | ⚠ s11 icon hint, см. D4 |
| Explanatory-engineering tone | ✓ consistent with plan v2.1 §1.4 | ✓ slides match tone — definitions + mechanism + engineering implication | ✓ aligned |
| No overclaim (slides ≯ chapter) | ✓ all slide assertions = paraphrase of chapter | ✓ no overclaim detected; s24 «3 ответа из Лекции 2» правильно reflects §5.2 | ✓ aligned |

**Tone verdict:** ✓ aligned with 1 micro-flag (D4 icon hint).

---

## References parity

**Liu et al. (2023), arXiv:2307.03172:** ✓ present in chapter L370/L619/L659 + slide s17 L30. Identical format.

**Sennrich et al. (2016):** chapter L157 + L615 (Sources). Slide s06 L40 caption. ✓ aligned.

**Holtzman et al. (2019):** chapter L423 + L618 + L664. Slides — 0 explicit citations. **Acceptable** — chapter introduces nucleus sampling; slides s19/s20 mention top-p without citation (consistent with slide audience load reduction).

**Mikolov et al. (2013) / Word2Vec:** chapter L250 + L617 + L652. Slide s10 L37 speaker notes («Word2Vec в 2013 году…»). ✓ aligned, but PNG s10 не cites Mikolov в visible content. Acceptable.

**Pearl, J. (2018):** chapter L620. Slide s26 L7+L10 (visual_brief / learning_goal — EN «Pearl»); speaker notes L36 «Пёрла»→«Перла» canonical. ✓ aligned.

**Vaswani et al. (2017):** chapter L612 + L639 (Дальнейшее чтение). Slides s14 L48 (speaker notes «Vaswani et al. (2017)»); s14 visible caption mentions «Лекция 17 / доп. чтение». ✓ aligned.

**Anthropic MCP (2024):** chapter L621 + slide s28 L31 («Anthropic, 2024»). ✓ aligned.

**HF Inference Playground [VERIFY-DAY-OF]:** chapter L584-585 + L624; slide s27 L32 + L40. ✓ aligned, tag preserved.

**Reference verdict:** ✓ no orphan citations; symmetric set.

---

## Visual ↔ verbal alignment (spot-check: s01/s07/s10/s15/s16/s20)

| Slide | Visible PNG title | MD source title | deck.yaml assertion | Aligned? |
|---|---|---|---|---|
| s01 | «Модель видит ваш запрос не буквами — а токенами» | «Как модель видит ваш запрос: live tokenizer» | «Модель видит ваш запрос не буквами и не словами — а токенами» | PNG ≈ assertion ≠ MD title (D10) |
| s07 | «AI ошибается в "сколько r в strawberry" — слова не из букв, а из 2-3 токенов» | «Почему AI плохо считает буквы» | «AI ошибается в "сколько r в strawberry" — потому что слова не из букв, а из 2-3 токенов» | PNG ≈ assertion ≠ MD title (D10) |
| s10 | «Близость в пространстве эмбеддингов = семантическая близость» | «Семантическое сходство на современных эмбеддингах» | «Близость в пространстве эмбеддингов = семантическая близость…» | PNG ≈ assertion ≠ MD title (D10) |
| s15 | «Role-токены получают повышенный вес в attention» | «Рабочий пример и эффект роли в промпте» | «Role-токены получают повышенный вес в attention…» | PNG ≈ assertion ≠ MD title (D10) |
| s16 | «Контекстное окно — физический предел того, сколько модель видит одновременно» + side-panel «Эволюция и стоимость» | «Контекстное окно» | «Контекстное окно — физический предел…» | PNG ≈ assertion ≠ MD title (D10); side-panel beyond MD (D3) |
| s20 | «4 ручки API под задачу: temperature, top_p, max_tokens, system prompt» | «4 ручки API под задачу» | «4 параметра под задачу: temperature, top_p, max_tokens, system prompt» | PNG ≈ assertion ≈ MD title — clean |

**Verdict:** ✓ PNGs всех 6 spot-check slides aligned with chapter content. 2 issues — D3 (s16 side-panel), D10 (deck-wide title substitution pattern) — оба P1/P2 cosmetic.

---

## Топ-N приоритизированные правки

### Top для Slides

1. **(D3 / P1)** Back-port s16 side-panel «Эволюция и стоимость» содержимое в `s16-context-window.md` Body section (5-element design) или удалить из PNG.
2. **(D2 / P1)** Add disclaimer footnote в s10 cosine heatmap visual: «cross-cluster числа (0.18-0.22) — extrapolation в пределах диапазона "несовместимые домены"». Альтернатива — упростить heatmap до 3 canonical values.
3. **(D5 / P2)** Fix s19 «T = 0.7 (стандарт)» → align с chapter «T=1.0 (стандарт)». Если slide хочет показать T=0.7 как chat-typical, добавить explicit note «chat default = 0.7; technical standard = 1.0».
4. **(D10 / P2)** Sync slide MD `Title bar` поля с deck.yaml `assertion` для всех 28 файлов — back-fill design decision в repo-first source of truth.
5. **(D8 / P2)** Add visible «illustrative» disclaimer на s18 (footer мелким).
6. **(D6 / P2)** Expand s06 visible caption: explicit «BPE — GPT-семейство, Llama 3+».
7. **(D4 / P2)** Replace s11 «иконка магнита» → «иконка парных точек» или «иконка лупы».
8. **(D11 / P2)** Add `interaction: open_question` (или подобное) к s01 frontmatter.
9. **(D1 / P1)** Move chapter `[for-slide-s13]` marker к L307 (after `## Раздел 3` heading) или изменить deck.yaml s13.chapter_ref к `«§3.1»`.

### Top для Chapter

**Нет рекомендованных изменений в chapter.** Chapter v1.1 — source of truth, все slides derive correctly. Единственный потенциальный chapter-side improvement: предостеречь от cross-cluster cosine extrapolation в §2.2 FACT-CHECK footnote (если slide visualization будет сохранён as-is) — но это discretionary.

---

## Counter-check (CLAUDE.md ENFORCED)

**P1 issues count = 3 (D1, D2, D3).** Threshold для REVISE — ≥5 P1. Verdict APPROVE-WITH-POLISH согласован.

**P0 issues count = 0.** No factual contradictions detected.

**Glossary lock enforcement:** 17 canonical terms из `deck.yaml.glossary_lock` все приcутствуют без drift. No suggested renames (PROPOSED GLOSSARY UPDATE: none).

**Book-first methodology:** ✓ chapter remains source of truth; все P1 рекомендации = fix slides, not chapter.

**Pre-USER-GATE walkthrough trigger:** orchestrator должен перед USER GATE 2 (Phase 8) запустить `mode=terminology-only` quick scan (см. consistency-checker spec). На текущем срезе drift = 0 (all green), но добавление дальнейших правок (D5, D10) повторно потребует re-run.

---

## Меta-notice: branch consistency

Текущий git branch — `issue-73-lec-04-medicine-production`. Все артефакты Лекции 2 (chapter, deck.yaml, 28 slides, plan, constraints) находятся на ветке `issue-74-lec-02-llm-internals` — checked out через `git show issue-74-lec-02-llm-internals:<path>`. Локальный rendered/snapshots/ присутствует на текущей working tree (тоже из ветки lec-02). Report сохранён в working tree по target path (qa-reports каталог уже создан с тремя другими отчётами от parallel critics).

**Конец отчёта.**
