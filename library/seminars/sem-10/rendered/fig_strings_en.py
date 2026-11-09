"""English captions for Seminar 10 diagrams (issue #322, EN track).

Key — the Russian string exactly as it stands in `make_figures_sem10.py`
(or in `N8N_DISCLAIMER`, imported from `n8n_canvas_kit.py` and drawn
identically on all four n8n-style schemes); value — the English string as it
goes onto the canvas. Mechanics and the reason the dictionary is its own
file, not a second drawing script, are in `tools/seminar-build/
fig_toolkit.py`'s own docstring. Order follows draw order, figure by figure
(the same order `make_figures_sem10.py`'s own `if __name__ == "__main__"`
block calls its ten drawing functions in); `BY_FIG` below says which string
belongs to which figure (used by `fig_toolkit.report()` to tell "key never
reached the canvas" apart from "key belongs to another figure"). Edited by
hand.

This file covers ALL TEN of sem-10's programmatically-drawn figures in one
pass — the four "-shema-postanovka" scene-setting schemes (Cases 1–4), the
four n8n-style pipeline schemes (Cases 1–4, sharing the one `N8N_DISCLAIMER`
caption), `case3-biencoder-vs-crossencoder.png`, and `case2-razryv-metriki.png`.
The other figures this seminar's slides reference (`*-real.png`) are actual
n8n screenshots already in English and are not drawn by this script — out
of scope for this dictionary.

English terms follow the locked glossary (`library/seminars/sem-10/
glossary.en.yaml`) wherever a figure's own string names a glossary concept —
"chunk", "knowledge base", "vector store", "embedding", "chunking",
"hybrid search", "reranker / LLM reranker", "bi-encoder", "cross-encoder",
"Reciprocal Rank Fusion (RRF)" all carry the glossary's own chosen English
word, not a fresh per-figure translation. "хранилище" standalone (Cases 1–2,
once Case 1 has built it) renders as "vector store" per the glossary's
"vector store / vector database" entry, not a generic "storage". "стенд"
renders as "stend" throughout, matching the glossary's own usage
("this stend's OpenRouter catalog") rather than "test bench" or "rig".

Numbers are carried over unchanged in value; only the decimal/thousands
punctuation is re-set to English convention (RU "1,5" → EN "1.5", RU
"24 000" → EN "24,000"), the same adjustment `fig_toolkit.py`'s own
docstring already documents for sem-06's figures — the measured quantity
itself never changes. So here: "score=0,590" → "score=0.590", "12,5%" →
"12.5%", "+1,6–1,9с" → "+1.6–1.9s" (seconds), "cosine=1,0" → "cosine=1.0".
Multiplication signs ("300×450"), percent/ratio symbols, and the ≥/≠ glyphs
are not locale-dependent and pass through unchanged.

Model/field/API identifiers (`gpt-4o-mini`, `text-embedding-3-small`,
`amazon/titan-embed-image-v1`, `voyage-multimodal-3`, `chunk_size`,
`predefinedCredentialType: openRouterApi`, `cosine(qvec, doc.embedding)`,
n8n stock node names like `Simple Vector Store`, `HTTP Request`) are already
English in the source — they carry no Cyrillic and so never need a
dictionary entry; where they're embedded inside a Cyrillic sentence (e.g.
inside a callout body), only the surrounding RU prose gets a translated
key, the identifier is kept verbatim inside it.

Proper nouns stay as the glossary's own notes say: "Ольга" is "Olga"
(unchanged in English text, so it never needs a dictionary entry here).

A miss (Cyrillic with no entry here) is never silent: `fig_toolkit.report()`
prints the list. An unused key is reported too — a typo in the key, or a
string the drawing script no longer draws.
"""

STRINGS = {

    # ── case1-shema-postanovka.png ──────────────────────────────────────────
    "Где в потоке ответа встанет поиск нужного куска":
        "Where in the answer flow the search for the needed chunk will sit",
    "форма и вызов модели уже работают — вопрос в том, что займёт место узла "
    "«весь справочник целиком», когда база вырастет":
        "the form and the model call already work — the question is what "
        "will take the place of the node ‘The whole knowledge base at "
        "once’ when the base grows",
    "Вопрос обратившегося":
        "The requester's question",
    "форма, как на прошлом занятии":
        "a form, like in the last session",
    "Весь справочник целиком":
        "The whole knowledge base at once",
    "текст базы — в промт целиком":
        "base text — straight into the prompt",
    "Модель отвечает":
        "The model answers",
    "gpt-4o-mini, вся база в промте":
        "gpt-4o-mini, whole base in the prompt",
    "Строим сегодня:":
        "Building today:",
    "хранилище + поиск куска":
        "vector store + chunk search",

    # ── case1-n8n-vector-scheme.png ─────────────────────────────────────────
    "Кейс 1 · хранение базы знаний":
        "Case 1 · Knowledge Base Storage",
    "Вопрос + корпус с векторами":
        "Query + corpus with vectors",
    "Simple Vector Store (поиск)":
        "Simple Vector Store (search)",
    "top-1 из N документов, score=0,590":
        "top-1 of N documents, score=0.590",
    "Чего нет на этом холсте — узла «эмбеддинг через OpenRouter» в каталоге n8n 2.42.7":
        "What's missing from this canvas — an ‘embed via OpenRouter’ "
        "node in the n8n 2.42.7 catalog",
    "и шаг эмбеддинга, и финальный вызов модели собраны обычным узлом HTTP Request":
        "both the embedding step and the final model call are built with a "
        "plain HTTP Request node",
    "с предустановленным типом учётных данных (predefinedCredentialType: openRouterApi)":
        "with a preset credential type (predefinedCredentialType: openRouterApi)",
    "вопрос «При каком давлении удалось получить кристаллы гелия?» → найден кусок":
        "question ‘At what pressure was it possible to obtain helium "
        "crystals?’ → the chunk is found",
    "needle-1 (score 0,590, «…применив давление выше 35 атм…») → ответ верный":
        "needle-1 (score 0.590, ‘…applying pressure above 35 atm…’) "
        "→ the answer is correct",

    # ── case2-shema-postanovka.png ──────────────────────────────────────────
    "Где в пути документа встаёт разбиение на куски":
        "Where in the document's path chunking sits",
    "эмбеддинг и хранилище уже работают с прошлого занятия — "
    "вопрос в том, что происходит до них":
        "the embedding and the vector store already work from the last "
        "session — the question is what happens before them",
    "Документ":
        "Document",
    "база знаний, Кейс 1":
        "knowledge base, Case 1",
    "Разбиение на куски":
        "Chunking",
    "строим в этом кейсе":
        "built in this case",
    "Эмбеддинг куска":
        "Chunk embedding",
    "уже работает, Кейс 1":
        "already works, Case 1",
    "Хранилище":
        "Vector store",

    # ── case2-n8n-splitter-scheme.png ───────────────────────────────────────
    "Кейс 2 · разбиение документа на части — Text Splitter перед эмбеддингом":
        "Case 2 · Splitting a Document into Chunks — Text Splitter before embedding",
    "Документ базы знаний":
        "Knowledge base document",
    "Set · текст регламента/FAQ":
        "Set · regulation/FAQ text",
    'v1: Character Text Splitter, chunkSize=180, separator="" (посимвольно)':
        'v1: Character Text Splitter, chunkSize=180, separator="" (character by character)',
    'v2: Recursive Splitter, separator="по предложению", chunkSize=180':
        'v2: Recursive Splitter, separator="by sentence", chunkSize=180',
    "Simple Vector Store (запись)":
        "Simple Vector Store (write)",
    "Разница версии 1 и версии 2 — один параметр узла, не новая цепочка":
        "The difference between version 1 and version 2 — one node parameter, not a new chain",
    "v1 (separator «посимвольно», chunk_size=180): доля разорванных ответов 12,5% (9 из 72)":
        "v1 (separator ‘character by character’, chunk_size=180): "
        "share of broken answers 12.5% (9 of 72)",
    "v2 (separator «по предложению», тот же chunk_size=180): доля разорванных ответов 1,4% (1 из 72)":
        "v2 (separator ‘by sentence’, the same chunk_size=180): "
        "share of broken answers 1.4% (1 of 72)",
    "остальная цепочка (эмбеддинг, запись в хранилище) не меняется ни одним узлом":
        "the rest of the chain (embedding, writing to the vector store) doesn't change by a single node",
    "60 документов SberQuAD (≥500 символов), 72 вопроса — stend/raw/case2-results.json":
        "60 SberQuAD documents (≥500 characters), 72 questions — stend/raw/case2-results.json",

    # ── case2-razryv-metriki.png ────────────────────────────────────────────
    "кусок N":
        "chunk N",
    "«…часть ответа»":
        "‘…part of the answer’",
    "кусок N+1":
        "chunk N+1",
    "«ответа…»":
        "‘answer…’",
    "разрез куска":
        "chunk cut",

    # ── case3-shema-postanovka.png ──────────────────────────────────────────
    "Где в потоке ответа встаёт поиск нужного куска":
        "Where in the answer flow the search for the needed chunk sits",
    "вопрос и ответ уже работают, база уже нарезана по смыслу (Кейс 2) — "
    "вопрос в том, какой кусок из сотен увидит модель":
        "the question and the answer already work, the base is already "
        "chunked by meaning (Case 2) — the question is which chunk out of "
        "hundreds the model will see",
    "форма, как и раньше":
        "a form, same as before",
    "База нарезана по смыслу":
        "The base is chunked by meaning",
    "готово с прошлого кейса":
        "done, from the previous case",
    "Ответ по найденному куску":
        "Answer based on the found chunk",
    "модель видит только переданное":
        "the model sees only what's passed to it",
    "Строим сегодня: найти самый нужный кусок из сотен":
        "Building today: find the best chunk out of hundreds",
    "до того, как положить его в промт":
        "before putting it into the prompt",

    # ── case3-n8n-hybrid-rerank-scheme.png ──────────────────────────────────
    "Кейс 3 · чем искать нужный кусок — гибрид + необязательный LLM-реранкер":
        "Case 3 · Choosing a Search Method — hybrid + optional LLM reranker",
    "Вопрос":
        "Question",
    "top-10 по смыслу":
        "top-10 by meaning",
    "Keyword-фильтр":
        "Keyword filter",
    "Code: пересечение токенов":
        "Code: token overlap",
    "top-10 по словам":
        "top-10 by words",
    "Слияние (RRF, k=60)":
        "Fusion (RRF, k=60)",
    "LLM-реранкер (необязательно)":
        "LLM reranker (optional)",
    "gpt-4o-mini, top-10 в промте":
        "gpt-4o-mini, top-10 in the prompt",
    "top-1 → промт":
        "top-1 → prompt",
    "Реранкер — дополнительный узел после слияния, тот же credential, новой инфраструктуры нет":
        "The reranker — an extra node after fusion, the same credential, no new infrastructure",
    "recall@1: keyword 0,74 → vector 0,86 → hybrid(RRF) 0,84 → hybrid+реранкер 0,96":
        "recall@1: keyword 0.74 → vector 0.86 → hybrid(RRF) 0.84 → hybrid+reranker 0.96",
    "у OpenRouter нет отдельного rerank-эндпоинта — это обычный chat-completions, которому":
        "OpenRouter has no separate rerank endpoint — it's a plain chat-completions call that's",
    "передают top-10 кандидатов и просят вернуть порядок по релевантности вопросу":
        "given the top-10 candidates and asked to return their order by relevance to the question",
    "цена шага реранка: ~$0,00033 на вопрос, +1,6–1,9с — больше, чем весь пайплайн Кейса 1":
        "cost of the rerank step: ~$0.00033 per question, +1.6–1.9s — more than Case 1's entire pipeline",

    # ── case3-biencoder-vs-crossencoder.png ─────────────────────────────────
    "Би-энкодер и кросс-энкодер: почему совместное чтение точнее":
        "Bi-encoder and cross-encoder: why reading together is more accurate",
    "слева — обычный векторный поиск; справа — реранкер (кросс-энкодер)":
        "left — ordinary vector search; right — the reranker (cross-encoder)",
    "Би-энкодер (векторный поиск)":
        "Bi-encoder (vector search)",
    "Кросс-энкодер (реранкер)":
        "Cross-encoder (reranker)",
    "Запрос":
        "Query",
    "текст вопроса":
        "the question's text",
    "текст кандидата":
        "the candidate's text",
    "Кодировщик":
        "Encoder",
    "вектор запроса":
        "the query's vector",
    "вектор документа — заранее":
        "doc vector — precomputed",
    "Сравнение векторов":
        "Vector comparison",
    "косинусное сходство двух готовых чисел":
        "cosine similarity of two ready-made numbers",
    "Запрос и документ кодируются ОТДЕЛЬНО, в разное время":
        "The query and the document are encoded SEPARATELY, at different times",
    "Единый вход":
        "Single input",
    "запрос и документ — один текст, не два вектора":
        "query and document — one text, not two vectors",
    "Модель оценивает релевантность":
        "The model scores relevance",
    "один проход, отдельных векторов нет":
        "one pass, no separate vectors",
    "Запрос и документ читаются ВМЕСТЕ, одним вызовом модели":
        "The query and the document are read TOGETHER, in one model call",
    "Почему совместное чтение точнее":
        "Why reading together is more accurate",
    "слева векторы считаются заранее, до вопроса — слова запроса и документа":
        "on the left the vectors are computed in advance, before the question — the words of the query and the document",
    "никогда не встречаются напрямую, только их сжатый числовой итог":
        "never meet directly, only their compressed numeric summary does",
    "справа модель получает оба текста одним входом и сопоставляет конкретные":
        "on the right the model receives both texts as one input and matches specific",
    "слова запроса со словами документа внутри одного прохода — поэтому реранкер":
        "words of the query against words of the document within a single pass — which is why the reranker",
    "иногда точнее там, где сравнение готовых векторов путает похожие документы":
        "is sometimes more accurate exactly where comparing ready-made vectors confuses similar documents",

    # ── case4-n8n-mm-scheme.png ─────────────────────────────────────────────
    "Кейс 4 · поиск по изображениям":
        "Case 4 · Image Search",
    "Скан бланка (data URL)":
        "Form scan (data URL)",
    "Находка, не ожидание плана: ответ приходит без ошибки и всё равно не работает":
        "A finding, not what the plan expected: the answer comes back with no error and still doesn't work",
    "voyage-multimodal-3 не найден на OpenRouter этого стенда ни под одним написанием id":
        "voyage-multimodal-3 is not found on this stend's OpenRouter under any spelling of the id",
    "amazon/titan-embed-image-v1 существует, вектор приходит — НО на реальном разрешении":
        "amazon/titan-embed-image-v1 exists, a vector comes back — BUT at the real resolution",
    "скана (300×450) он битово ОДИНАКОВЫЙ для любых двух разных картинок (cosine=1,0)":
        "of the scan (300×450) it is bit-for-bit IDENTICAL for any two different images (cosine=1.0)",
    "«отвечает без ошибки» ≠ «использует вход» — проверено подачей двух разных входов":
        "‘answers with no error’ ≠ ‘uses the input’ — verified by feeding it two different inputs",

    # ── case4-shema-postanovka.png ──────────────────────────────────────────
    "Где в потоке поиска встанет сравнение самой картинки":
        "Where in the search flow comparing the image itself will sit",
    "подпись и текстовый поиск уже работают — вопрос в том, можно ли пропустить":
        "captioning and text search already work — the question is whether it's possible to skip",
    "шаг «превратить картинку в текст» и сравнивать саму картинку":
        "the step ‘turn the picture into text’ and compare the picture itself",
    "Скан бланка или чека":
        "Scan of a form or receipt",
    "в заявке Ольге":
        "in a request to Olga",
    "Подпись: OCR → текст":
        "Caption: OCR → text",
    "картинка пересказана словами":
        "the picture retold in words",
    "Текстовый поиск находит похожий":
        "Text search finds a similar one",
    "Кейсы 1–3 этого занятия":
        "Cases 1–3 of this session",
    "Пробуем сегодня:":
        "Trying today:",
    "сравнивать саму картинку в её числовом представлении":
        "comparing the image itself in its numeric representation",
    "— без шага «превратить в текст»":
        "— without the step ‘turn it into text’",

    # ── shared: N8N_DISCLAIMER (n8n_canvas_kit.py), drawn identically on all
    # four n8n-style schemes (case1/2/3/4-n8n-*-scheme.png) ─────────────────
    "Программно нарисованная схема в духе n8n — холст недостижим в этой среде "
    "([#233-8]); имена узлов и значения — настоящие, со стенда.":
        "A programmatically-drawn schematic in n8n's visual style — the "
        "canvas is unreachable in this environment ([#233-8]); node names "
        "and values are real, from the stend.",
}

BY_FIG = {
    "case1-shema-postanovka.png": [
        "Где в потоке ответа встанет поиск нужного куска",
        "форма и вызов модели уже работают — вопрос в том, что займёт место узла "
        "«весь справочник целиком», когда база вырастет",
        "Вопрос обратившегося",
        "форма, как на прошлом занятии",
        "Весь справочник целиком",
        "текст базы — в промт целиком",
        "Модель отвечает",
        "gpt-4o-mini, вся база в промте",
        "Строим сегодня:",
        "хранилище + поиск куска",
    ],

    "case1-n8n-vector-scheme.png": [
        "Кейс 1 · хранение базы знаний",
        "Вопрос + корпус с векторами",
        "Simple Vector Store (поиск)",
        "top-1 из N документов, score=0,590",
        "Чего нет на этом холсте — узла «эмбеддинг через OpenRouter» в каталоге n8n 2.42.7",
        "и шаг эмбеддинга, и финальный вызов модели собраны обычным узлом HTTP Request",
        "с предустановленным типом учётных данных (predefinedCredentialType: openRouterApi)",
        "вопрос «При каком давлении удалось получить кристаллы гелия?» → найден кусок",
        "needle-1 (score 0,590, «…применив давление выше 35 атм…») → ответ верный",
        "Программно нарисованная схема в духе n8n — холст недостижим в этой среде "
        "([#233-8]); имена узлов и значения — настоящие, со стенда.",
    ],

    "case2-shema-postanovka.png": [
        "Где в пути документа встаёт разбиение на куски",
        "эмбеддинг и хранилище уже работают с прошлого занятия — "
        "вопрос в том, что происходит до них",
        "Документ",
        "база знаний, Кейс 1",
        "Разбиение на куски",
        "строим в этом кейсе",
        "Эмбеддинг куска",
        "уже работает, Кейс 1",
        "Хранилище",
    ],

    "case2-n8n-splitter-scheme.png": [
        "Кейс 2 · разбиение документа на части — Text Splitter перед эмбеддингом",
        "Документ базы знаний",
        "Set · текст регламента/FAQ",
        'v1: Character Text Splitter, chunkSize=180, separator="" (посимвольно)',
        'v2: Recursive Splitter, separator="по предложению", chunkSize=180',
        "Simple Vector Store (запись)",
        "Разница версии 1 и версии 2 — один параметр узла, не новая цепочка",
        "v1 (separator «посимвольно», chunk_size=180): доля разорванных ответов 12,5% (9 из 72)",
        "v2 (separator «по предложению», тот же chunk_size=180): доля разорванных ответов 1,4% (1 из 72)",
        "остальная цепочка (эмбеддинг, запись в хранилище) не меняется ни одним узлом",
        "60 документов SberQuAD (≥500 символов), 72 вопроса — stend/raw/case2-results.json",
        "Программно нарисованная схема в духе n8n — холст недостижим в этой среде "
        "([#233-8]); имена узлов и значения — настоящие, со стенда.",
    ],

    "case2-razryv-metriki.png": [
        "кусок N",
        "«…часть ответа»",
        "кусок N+1",
        "«ответа…»",
        "разрез куска",
    ],

    "case3-shema-postanovka.png": [
        "Где в потоке ответа встаёт поиск нужного куска",
        "вопрос и ответ уже работают, база уже нарезана по смыслу (Кейс 2) — "
        "вопрос в том, какой кусок из сотен увидит модель",
        "Вопрос обратившегося",
        "форма, как и раньше",
        "База нарезана по смыслу",
        "готово с прошлого кейса",
        "Ответ по найденному куску",
        "модель видит только переданное",
        "Строим сегодня: найти самый нужный кусок из сотен",
        "до того, как положить его в промт",
    ],

    "case3-n8n-hybrid-rerank-scheme.png": [
        "Кейс 3 · чем искать нужный кусок — гибрид + необязательный LLM-реранкер",
        "Вопрос",
        "Simple Vector Store (поиск)",
        "top-10 по смыслу",
        "Keyword-фильтр",
        "Code: пересечение токенов",
        "top-10 по словам",
        "Слияние (RRF, k=60)",
        "LLM-реранкер (необязательно)",
        "gpt-4o-mini, top-10 в промте",
        "top-1 → промт",
        "Реранкер — дополнительный узел после слияния, тот же credential, новой инфраструктуры нет",
        "recall@1: keyword 0,74 → vector 0,86 → hybrid(RRF) 0,84 → hybrid+реранкер 0,96",
        "у OpenRouter нет отдельного rerank-эндпоинта — это обычный chat-completions, которому",
        "передают top-10 кандидатов и просят вернуть порядок по релевантности вопросу",
        "цена шага реранка: ~$0,00033 на вопрос, +1,6–1,9с — больше, чем весь пайплайн Кейса 1",
        "Программно нарисованная схема в духе n8n — холст недостижим в этой среде "
        "([#233-8]); имена узлов и значения — настоящие, со стенда.",
    ],

    "case3-biencoder-vs-crossencoder.png": [
        "Би-энкодер и кросс-энкодер: почему совместное чтение точнее",
        "слева — обычный векторный поиск; справа — реранкер (кросс-энкодер)",
        "Би-энкодер (векторный поиск)",
        "Кросс-энкодер (реранкер)",
        "Запрос",
        "текст вопроса",
        "Документ",
        "текст кандидата",
        "Кодировщик",
        "вектор запроса",
        "вектор документа — заранее",
        "Сравнение векторов",
        "косинусное сходство двух готовых чисел",
        "Запрос и документ кодируются ОТДЕЛЬНО, в разное время",
        "Единый вход",
        "запрос и документ — один текст, не два вектора",
        "Модель оценивает релевантность",
        "один проход, отдельных векторов нет",
        "Запрос и документ читаются ВМЕСТЕ, одним вызовом модели",
        "Почему совместное чтение точнее",
        "слева векторы считаются заранее, до вопроса — слова запроса и документа",
        "никогда не встречаются напрямую, только их сжатый числовой итог",
        "справа модель получает оба текста одним входом и сопоставляет конкретные",
        "слова запроса со словами документа внутри одного прохода — поэтому реранкер",
        "иногда точнее там, где сравнение готовых векторов путает похожие документы",
    ],

    "case4-n8n-mm-scheme.png": [
        "Кейс 4 · поиск по изображениям",
        "Скан бланка (data URL)",
        "Находка, не ожидание плана: ответ приходит без ошибки и всё равно не работает",
        "voyage-multimodal-3 не найден на OpenRouter этого стенда ни под одним написанием id",
        "amazon/titan-embed-image-v1 существует, вектор приходит — НО на реальном разрешении",
        "скана (300×450) он битово ОДИНАКОВЫЙ для любых двух разных картинок (cosine=1,0)",
        "«отвечает без ошибки» ≠ «использует вход» — проверено подачей двух разных входов",
        "Программно нарисованная схема в духе n8n — холст недостижим в этой среде "
        "([#233-8]); имена узлов и значения — настоящие, со стенда.",
    ],

    "case4-shema-postanovka.png": [
        "Где в потоке поиска встанет сравнение самой картинки",
        "подпись и текстовый поиск уже работают — вопрос в том, можно ли пропустить",
        "шаг «превратить картинку в текст» и сравнивать саму картинку",
        "Скан бланка или чека",
        "в заявке Ольге",
        "Подпись: OCR → текст",
        "картинка пересказана словами",
        "Текстовый поиск находит похожий",
        "Кейсы 1–3 этого занятия",
        "Пробуем сегодня:",
        "сравнивать саму картинку в её числовом представлении",
        "— без шага «превратить в текст»",
    ],
}
