# Лекция 2 — Reference registry (перед добавлением ссылок на слайды)

**Дата:** 2026-08-30 · **Исследователь:** research subagent (direct, no sub-agents) · **Лекция:** «Как работают современные большие модели» (МГТУ ИУ6, 3-й курс, RU, 2026).
**Цель:** (1) инвентарь утверждений/цифр/терминов по слайдам, требующих источника; (2) реестр `SLIDE_REFS` + `URLS` в формате lec-04; (3) оценка состояния speaker_notes.
**Access date для всех URL:** **2026-08-30**. `[VFY-day-of]` = volatile (модель/версия/бенчмарк/платформа) — перепроверить в день лекции. Канонические arXiv/vendor URL верифицированы WebSearch этой сессией; непроверенные помечены `[VFY]`. **URL не выдумывались.**

**Источники синтеза:** `chapter.md` §Источники + §Дальнейшее чтение (строки 634–698); `qa-reports/2026-05-13-phase3-chapter-v1/fact-checker.md`; `qa-reports/2026-05-13-phase7-slides-v1/fact-checker.md` (per-slide visible-data audit, строки 137–170); сами `slides/*.md`.

---

## Резюме

**Слайдов всего:** 35 файлов (нумерация s01–s29 + a-варианты дивайдеров/врезок). Из них **~18 слайдов несут атрибутируемое утверждение/цифру/термин**, требующее источника; остальные — концептуальные/навигационные (cover, lecture-map, section dividers, recap, payoff) без внешних claim.

**Ключевые источники (все верифицированы этой сессией, exact author+title match):** Vaswani 2017 (attention), Sennrich 2016 (BPE), Mikolov 2013 (word2vec), Holtzman 2019/ICLR2020 (nucleus/top-p), Liu 2023 (Lost-in-the-Middle), Lewis 2020 (RAG), Yao 2022 (ReAct), «Counting Ability» 2410.19730 (арифметика/токенизация), Anthropic MCP (Nov 25 2024), OpenAI tiktoken + Embeddings API.

**Рефактор нот:** **НЕ требуется.** speaker_notes уже связные нарративы 150–300 слов с вплетёнными inline-цитатами («Liu et al. (2023)», «Sennrich et al.», «в 2023 году группа из Stanford и UC Berkeley…»). Формат — student-facing текст, не layout-описание. Достаточно точечной сверки (см. §5).

---

## 1. Инвентарь утверждений по слайдам (что требует источника)

| sNN | Slide | Claim / цифра / термин | Источник (глава/QA) | Тип |
|---|---|---|---|---|
| s01 | Live tokenizer | `cat=1, tokenization=2, strawberry=3, клубника=3` (o200k_base, май 2026) | tiktoken empirical + гл. §1.1 | tiktoken `[VFY-day-of]` |
| s05 | Что такое токен | split + «1 токен ≈ 4 EN / 2 RU» | tiktoken + гл. §1.1/§1.4 | эвристика (hedged) |
| s06 | BPE compromise | `low/lower/newest/widest → low/er/new/est/wid`; альтернативы WordPiece/SentencePiece | **Sennrich 2016** (канон. пример) | primary paper |
| s07 | Почему AI не считает буквы | `strawberry → [st][raw][berry] = 3 токена`; арифметика 59%/4%/0% | tiktoken + **2410.19730** | primary + `[VFY-day-of]` (strawberry pretest) |
| s08 | Cross-language cost | EN 0.25 / RU 0.50 / ZH 0.80 / Py 0.40 токена/символ | tiktoken empirical, гл. §1.4 `[FACT-CHECK]` | эвристика (hedged, `[VFY]`) |
| s09 | Что такое эмбеддинг | `text-embedding-3-small 1536 / large 3072`; internal flagship «тысячи» | **OpenAI Embeddings API**; internal = leak (softened) | vendor doc + `[FACT-CHECK]` |
| s10 | Sentence similarity | cosine 5×5 (SSL↔HTTPS 0.85 и т.д.) | illustrative, гл. §2.2 `[FACT-CHECK]`; воспр. на all-MiniLM-L6-v2 / text-embedding-3-small | illustrative (caveat) |
| s12 | Semantic vs fulltext | RAG-парадигма (semantic vs stemming) | **Lewis 2020** (RAG) | primary paper |
| s14 | Что такое attention | распределение Σ=1; «32–128 голов» (notes) | **Vaswani 2017** + гл. §3.1 | primary paper |
| s16 | Контекстное окно | GPT-3.5 4k (2022) / Claude 3.5 200k (2024) / Claude 4.7 1M (2026); ×250; «1M ≈ 16× 100k» | Anthropic + OpenAI release notes | `[VFY-day-of]` (P1: 16× vs N²) |
| s17 | Long-context fails | U-shape ~75/50/75% | **Liu 2023** (2307.03172) | primary paper |
| s18 | Distribution | «Сегодня я съел…» → яблоко 0.32 и т.д. | illustrative (o200k vocab ~200k) | illustrative |
| s19 | Temperature | T=0 / T=1 (стандарт) / T=2; top-p / top-k | **Holtzman 2019** (top-p); гл. §4.2 | primary (P1: T=0.7 vs T=1.0) |
| s20 | 4 ручки API | T / top_p / max_tokens / system_prompt | industry-standard + OpenAI/Anthropic API docs | vendor doc |
| s21 | Авторегрессионный цикл | 5-step loop | conceptual (гл. §4.4) | — |
| s22 | Local vs cloud | Qwen 2.5 1.5B / Llama 3.2 1B / Llama 3.1 8B / Mistral 7B; cloud 200B+ | HF model cards; Mistral release | vendor `[VFY-day-of]` |
| s25 | ML vs LLM tree | XGBoost / LightGBM / BERT fine-tuned; latency <100ms vs 200–500ms | industry-standard | — (weak-cite) |
| s26 | Attention vs causality | Pearl 3 уровня причинности | **Pearl 2018** (Book of Why); callback Lec-1 §4.8 | primary book |
| s27 | Homework | HF Inference Playground, Meta-Llama-3-8B-Instruct; fallback Together.ai/Ollama | HF platform | `[VFY-day-of]` (mandatory) |
| s28 | Bridge Лекции 3 | RAG (Lewis 2020), MCP (Anthropic Nov 2024), Agent loop (Yao 2022 ReAct) | callbacks Lec-1 §2.2/§3.4.1 | primary papers |

**Навигационные/концептуальные без внешнего claim:** s02, s02a, s03, s04, s04a, s04b, s08a, s09a, s13, s13a, s15, s17a, s22a, s23, s24, s29.

---

## 2. Реестр ссылок — `URLS` (формат lec-04)

```python
URLS = {
    # --- Канонические первичные статьи (все verified 2026-08-30, exact author+title) ---
    "vaswani": "https://arxiv.org/abs/1706.03762",          # Attention Is All You Need (Vaswani et al. 2017)
    "sennrich_bpe": "https://arxiv.org/abs/1508.07909",     # NMT of Rare Words w/ Subword Units — BPE (Sennrich 2016)
    "mikolov_w2v": "https://arxiv.org/abs/1301.3781",       # Efficient Estimation of Word Repr. — word2vec (Mikolov 2013)
    "holtzman_topp": "https://arxiv.org/abs/1904.09751",    # Curious Case of Neural Text Degeneration — nucleus/top-p (Holtzman 2019/ICLR2020)
    "liu_lost_middle": "https://arxiv.org/abs/2307.03172",  # Lost in the Middle (Liu et al. 2023 / TACL 2024)
    "lewis_rag": "https://arxiv.org/abs/2005.11401",        # Retrieval-Augmented Generation (Lewis et al. 2020, NeurIPS)
    "yao_react": "https://arxiv.org/abs/2210.03629",        # ReAct (Yao et al. 2022 / ICLR 2023)
    "counting_tok": "https://arxiv.org/abs/2410.19730",     # Counting Ability of LLMs & Impact of Tokenization (Zhang et al. 2024)
    "sentence_bert": "https://arxiv.org/abs/1908.10084",    # Sentence-BERT (Reimers & Gurevych 2019) [дальнейшее чтение] [VFY]
    "kudo_sp": "https://arxiv.org/abs/1808.06226",          # SentencePiece (Kudo 2018) [дальнейшее чтение] [VFY]
    "fan_topk": "https://arxiv.org/abs/1805.04833",         # Hierarchical Neural Story Generation — top-k (Fan 2018) [VFY]
    "tay_eff_tf": "https://arxiv.org/abs/2009.06732",       # Efficient Transformers: A Survey (Tay 2022) [дальнейшее чтение] [VFY]

    # --- Vendor / tooling docs ---
    "tiktoken": "https://github.com/openai/tiktoken",       # OpenAI tiktoken (cl100k_base / o200k_base)
    "openai_embeddings": "https://platform.openai.com/docs/guides/embeddings",  # 1536/3072 dims (301→developers.openai.com/api/docs/guides/embeddings) [VFY]
    "mcp": "https://www.anthropic.com/news/model-context-protocol",  # MCP (Anthropic, 25 Nov 2024)
    "hf_playground": "https://huggingface.co/playground",   # HF Inference Playground (homework) [VFY-day-of]
    "hf_tokenizers": "https://huggingface.co/docs/tokenizers",  # HF Tokenizers docs [VFY]
    "mistral_7b": "https://mistral.ai/news/announcing-mistral-7b",  # Mistral 7B release [VFY]

    # --- Книги / общеучебные ---
    "pearl_why": "https://en.wikipedia.org/wiki/The_Book_of_Why",   # Pearl, Book of Why (2018) — 3 уровня причинности
    "illustrated_tf": "https://jalammar.github.io/illustrated-transformer/",  # Alammar — Illustrated Transformer [дальнейшее чтение]
    "karpathy_gpt": "https://www.youtube.com/watch?v=kCc8FmEb1nY",  # Karpathy «Let's build GPT» [дальнейшее чтение] [VFY]

    # --- Российский контекст ---
    "yandexgpt": "https://yandex.cloud/ru/services/yandexgpt",
    "gigachat": "https://developers.sber.ru/portal/products/gigachat-api",
}
```

---

## 3. Реестр ссылок — `SLIDE_REFS` (формат lec-04: (номер, подпись, ключ-URL, фраза-раскрытие[, gold]))

```python
SLIDE_REFS = {
    "s06": [
        ("1", "Sennrich et al. (2016) — NMT of Rare Words / BPE", "sennrich_bpe",
         "BPE — компромисс: словарь из частых подпоследовательностей, не букв и не слов"),
    ],
    "s07": [
        ("1", "Counting Ability of LLMs & Impact of Tokenization (2024)", "counting_tok",
         "GPT-4 без калькулятора: 59%/4%/0% на 3-/4-/5-значном умножении — тот же tokenizer-cut механизм",
         True),
    ],
    "s09": [
        ("1", "OpenAI — Embeddings API", "openai_embeddings",
         "публичные эмбеддинги: text-embedding-3-small 1536, large 3072 измерения"),
        ("2", "Mikolov et al. (2013) — word2vec", "mikolov_w2v",
         "исторический контекст: геометрическая близость = смысловая близость"),
    ],
    "s10": [
        ("1", "воспроизводимо: all-MiniLM-L6-v2 / text-embedding-3-small", "openai_embeddings",
         "числа illustrative; cosine близость — статистика употребления, не семантический справочник"),
    ],
    "s12": [
        ("1", "Lewis et al. (2020) — RAG", "lewis_rag",
         "эмбеддинг ловит смысл, а не строку: основа semantic search / RAG"),
    ],
    "s14": [
        ("1", "Vaswani et al. (2017) — Attention Is All You Need", "vaswani",
         "attention выдаёт распределение весов на токены контекста (Σ=1); 32–128 голов на слой"),
    ],
    "s16": [
        ("1", "Anthropic — контекстное окно моделей Claude", "mcp",
         "рост окна 4k→200k→1M; порядок важнее точной цифры", True),
    ],
    "s17": [
        ("1", "Liu et al. (2023) — Lost in the Middle", "liu_lost_middle",
         "U-shape: точность проседает в середине окна; важное — в начало/конец промпта"),
    ],
    "s19": [
        ("1", "Holtzman et al. (2019) — nucleus sampling (top-p)", "holtzman_topp",
         "температура и top-p управляют формой распределения при сэмплинге"),
    ],
    "s22": [
        ("1", "Mistral AI — Mistral 7B", "mistral_7b",
         "локальные open-weight модели 1–13B vs cloud 200B+", True),
    ],
    "s26": [
        ("1", "Pearl (2018) — The Book of Why", "pearl_why",
         "attention ловит ассоциацию, не причинность (3 уровня причинной лестницы)"),
    ],
    "s27": [
        ("1", "Hugging Face — Inference Playground", "hf_playground",
         "домашнее задание: пронаблюдать эффект температуры; fallback Together.ai / Ollama",
         True),
    ],
    "s28": [
        ("1", "Lewis et al. (2020) — RAG", "lewis_rag",
         "как AI выходит за пределы чата: retrieval-augmented generation"),
        ("2", "Anthropic — Model Context Protocol (25 ноя 2024)", "mcp",
         "открытый стандарт подключения инструментов к LLM"),
        ("3", "Yao et al. (2022) — ReAct", "yao_react",
         "agent loop: act → observe → reflect", True),
    ],
}
```

---

## 4. Верификация URL (статус)

| Ключ | Статус | Примечание |
|---|---|---|
| vaswani / sennrich_bpe / mikolov_w2v / holtzman_topp / liu_lost_middle / lewis_rag / yao_react / counting_tok | ✅ verified | exact author+title+год совпали (WebSearch 2026-08-30) |
| mcp | ✅ verified | Anthropic, объявлен **25 ноября 2024** |
| tiktoken / openai_embeddings | ✅ / ⚠️ | tiktoken repo OK; embeddings **301→ developers.openai.com/api/docs/guides/embeddings** — обновить канонич. URL day-of `[VFY]` |
| hf_playground / hf_tokenizers | ⚠️ `[VFY-day-of]` | доступность free-tier + Llama-3-8B-Instruct — mandatory pretest перед семинаром |
| mistral_7b / yandexgpt / gigachat | ⚠️ `[VFY]` | vendor pages по конвенции; spot-check day-of |
| sentence_bert / kudo_sp / fan_topk / tay_eff_tf | ⚠️ `[VFY]` | «Дальнейшее чтение», arXiv ID из главы, не переверифицированы этой сессией |
| pearl_why / illustrated_tf / karpathy_gpt | ⚠️ `[VFY]` | book/blog/YT по конвенции |

**Непроверенные этой сессией (не выдавать за certain):** sentence_bert, kudo_sp, fan_topk, tay_eff_tf, karpathy_gpt (YT id), illustrated_tf, российский контекст. arXiv-ID взяты дословно из §Дальнейшее чтение главы.

---

## 5. Состояние speaker_notes (оценка)

**Вердикт: рефактор НЕ нужен.** Ноты уже соответствуют правилу (150–300 слов связного student-facing текста, derived from chapter).

- **Связные нарративы:** да. Пример s17 — полный абзацный рассказ про эксперимент Lost-in-the-Middle с inline-цитатой «Liu et al. (2023)» и инженерным выводом. s06 — 4 связных абзаца про BPE с «Sennrich».
- **Inline-ссылки:** уже вплетены как автор-год в текст нот («в 2023 году группа из Stanford и UC Berkeley…», «Sennrich et al.»). Явных URL в нотах нет — и не нужно; URL-реестр (§2/§3) добавляется на visible-layer как caption/footer, per lec-04 паттерн.
- **Не layout-описания:** ноты — читаемый текст, не «слева donut, справа bar». ✓
- **Точечная сверка перед рендером (из slides fact-checker):** три P1 не блокируют, но желательны до финала:
  1. **s16** «1M ≈ 16× от 100k» противоречит чистому N² (=100×) — уточнить формулировку (production-pricing vs теория).
  2. **s17** U-shape — уже обновлён до ~50% середина (совпадает с Liu Fig.1). ✓
  3. **s19** T=0.7 vs T=1.0 «стандарт» — visible/notes рассинхрон; выровнять на T=1.0 (default OpenAI/Anthropic).

**Day-of-lecture verify (из fact-checker, mandatory):** (1) strawberry pretest на 2–3 моделях (s07); (2) HF Playground + Llama-3-8B-Instruct free-tier (s27); (3) context-window цифры — вышел ли Claude 4.8/5.0/GPT-X (s16).

---

**Конец reference-registry Лекции 2.**
