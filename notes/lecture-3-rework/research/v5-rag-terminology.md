---
title: "RAG terminology — precise answers to owner's technical questions (v5)"
lecture: lec-03
purpose: >
  Точные, со ссылками, ответы на 4 технических вопроса владельца по терминологии
  поиска/RAG. Для каждого: корректная картина 2026 + одна фраза-корректор,
  которую лектор может произнести, чтобы аккуратно снять misconception.
date: 2026-09-15
volatility_note: >
  Помечено [VFY-day-of] всё, что зависит от версий движков/бенчмарков —
  проверять в день лекции.
---

# RAG-терминология: точные ответы на вопросы владельца

Общая рамка на все 4 вопроса: **лексический (sparse) и семантический (dense)
поиск — два в значительной мере независимых семейства**, а не «одно построено на
другом». Современные системы их **сливают (fuse)**, а не наследуют. Три из четырёх
вопросов владельца — это варианты одной и той же неточности: «семантика построена
на BM25». Она не построена; она — параллельная ветка, которую к лексике
**добавили**.

---

## 1. «Семантический поиск построен на BM25»? — Нет.

### Что спросил владелец
«Почему BM25 в классическом поиске, ведь на нём строится семантический?»

### Точный ответ
Это **инвертированная зависимость**. Семантический (dense) поиск **не построен на
BM25**. Это два разных механизма релевантности:

| | Классический лексический IR | Семантический / dense retrieval |
|---|---|---|
| Что сопоставляет | совпадение **токенов/термов** (буквально слова) | совпадение **смысла** в непрерывном пространстве |
| Представление | sparse-вектор над словарём (десятки тыс. измерений, почти все нули) | dense-вектор (напр. 384/768/1024 float, все ненулевые) |
| Структура данных | **инвертированный индекс** | **ANN-индекс** (HNSW, IVF) над эмбеддингами |
| Скоринг | TF-IDF → **BM25** (частота терма × редкость × нормировка длины) | косинус/скалярное произведение векторов |
| Появилось | 1970-90-е (TF-IDF), BM25 ~1994 (Okapi) | 2018-2020 (BERT → **DPR**, Karpukhin 2020) |

**Реальная родословная (lineage):**
1. **Лексический IR пришёл первым и остаётся «хребтом» (backbone).** Инвертированный
   индекс + TF-IDF/BM25 — быстрый, интерпретируемый, дешёвый (запрос <1 мс).
   Именно он до сих пор питает крупномасштабный поиск.
2. **Dense retrieval добавил слой смысла** поверх — как отдельная параллельная
   техника, чтобы закрыть «vocabulary gap» (запрос «automobile» не находил
   документ со словом «car»). Первым массовым каналом внедрения был **re-ranking**:
   BM25 достаёт кандидатов из инвертированного индекса → нейросеть **пере-ранжирует**
   их по смыслу. Здесь dense буквально работает *после* BM25 — но это не «построен
   на», это «добавлен рядом».
3. **Современные системы их сливают** (hybrid, RRF) — не заменяют одно другим.

Историческая точность: BM25 не «фундамент» для dense — dense-модели (DPR, BERT-би-энкодеры)
обучаются **с нуля на контрастивной цели**, у них нет BM25 внутри. Единственная
связь — **learned sparse** модели (SPLADE/ELSER, см. §2) сознательно возвращаются к
инвертированному индексу и по духу родственны BM25; но это отдельная третья ветка,
а не «классический семантический».

### Откуда путаница (назвать явно)
Три вещи создают иллюзию зависимости:
- BM25 часто **стоит первой ступенью** пайплайна (retrieve → re-rank), поэтому
  визуально dense «идёт после» → ложно читается как «на основе».
- BM25 — это **тоже вектор** (sparse), поэтому в учебниках оба рисуют «векторным
  поиском» → сливаются в один образ.
- В hybrid они физически соседствуют в одном запросе.

### Фраза-корректор для лектора
> «BM25 — это не фундамент семантического поиска, а его старший независимый
> родственник. Лексический поиск считает совпадение слов, семантический — совпадение
> смысла; это две разные ветки, выросшие из разных идей и в разные годы. Мы не
> строим семантику *на* BM25 — мы ставим их рядом и складываем результаты. То, что
> BM25 в пайплайне часто идёт первым, — это про порядок ступеней, а не про
> наследование.»

Sources:
- [The Evolution of Information Retrieval: From Lexical to Neural (iPullRank)](https://ipullrank.com/ai-search-manual/ir-evolution)
- [The Past and Present of Sparse Retrieval (HuggingFace)](https://huggingface.co/blog/yjoonjang/the-past-and-present-of-sparse-retrieval)
- [Implementing Hybrid Semantic-Lexical Search in RAG (MachineLearningMastery)](https://machinelearningmastery.com/implementing-hybrid-semantic-lexical-search-in-rag/)
- [A Survey of Model Architectures in Information Retrieval (arXiv 2502.14822)](https://arxiv.org/pdf/2502.14822)

---

## 2. Dense vs sparse векторы — определения (перед словом «hybrid»)

Это определение **обязано быть на слайде ДО** появления слова «hybrid» — иначе
«гибрид чего с чем» повисает.

### Sparse-вектор (разреженный, term-based)
Вектор **размерности = размер словаря** (десятки тысяч измерений), где **почти все
значения = 0**, ненулевые — только у термов, реально встретившихся в тексте. Каждое
измерение = конкретное слово словаря → **интерпретируемо** (видно, какие слова дали
вес). Хранится и ищется через **инвертированный индекс**, запрос <1 мс.

Два подвида sparse:
- **Классический (statistical) sparse** — **TF-IDF, BM25**. Вес = функция от частоты
  и редкости терма. Никакого обучения, «понимает» только буквальные совпадения.
- **Learned sparse (LSR)** — **SPLADE**, **ELSER** (Elastic). Использует
  bi-encoder на базе BERT: MLM-голова **расширяет** термы (добавляет
  контекстно-связанные слова — синонимы), сохраняя sparse-форму. Итог: «скорость и
  интерпретируемость инвертированного индекса, как у BM25 + семантическое
  расширение, как у dense». ELSER — house-модель Elastic на идеях SPLADE.

### Dense-вектор (плотный, embedding)
Вектор фиксированной **низкой размерности** (типично 384 / 768 / 1024), где **все
значения ненулевые** float. Порождается нейросетью-энкодером (BERT-би-энкодер, DPR и
преемники), кодирует **смысл**. Ищется приближённо через **ANN-индекс** (HNSW/IVF),
метрика — косинус / скалярное произведение. Латентность ANN ~10-100 мс на масштабе.
**Не интерпретируем** (измерения не соответствуют словам).

### Одна таблица для слайда
| Свойство | Sparse (BM25 / SPLADE) | Dense (embeddings) |
|---|---|---|
| Размерность | ~словарь (10⁴+), почти нули | 384-1024, все ненулевые |
| Что ловит | точные слова (+ расширение у SPLADE) | смысл, перефразы |
| Индекс | инвертированный | ANN (HNSW/IVF) |
| Латентность | <1 мс | ~10-100 мс |
| Интерпретируемость | да | нет |

### Фраза-корректор
> «Sparse-вектор — это почти все нули и по одному числу на слово словаря; dense —
> это несколько сотен чисел, все ненулевые, и ни одно не привязано к конкретному
> слову. BM25 — sparse. Эмбеддинги — dense. SPLADE — тоже sparse, но „умный“:
> инвертированный индекс плюс расширение синонимами.»

Sources:
- [Sparse vs Dense Vectors: How Lexical and Semantic Search Actually Work (BigDataBoutique)](https://bigdataboutique.com/blog/sparse-vs-dense-vectors-how-lexical-and-semantic-search-actually-work)
- [SPLADE for Sparse Vector Search Explained (Pinecone)](https://www.pinecone.io/learn/splade/)
- [Sparse embeddings: Dense vs. sparse vector (Elasticsearch Labs)](https://www.elastic.co/search-labs/blog/sparse-vector-embedding)
- [Understanding SPLADE and Sparse Vectors (Qdrant)](https://qdrant.tech/articles/sparse-vectors/)
- [Dense vs. Sparse Retrieval (SearchAtlas)](https://searchatlas.com/blog/dense-vs-sparse-retrieval/)

---

## 3. «Hybrid = семантика + строгие фильтры»? — Термин перегружен.

### Что сказал владелец
«Гибрид = семантика + строгие фильтры.» — Это **одно из** валидных значений, но не
основное в RAG-контексте. Слово «hybrid» перегружено; надо развести.

### Три вещи, которые называют «hybrid» (все легитимны, разное значение)

**(a) Лексика + dense fusion — ГЛАВНОЕ значение в RAG.**
Слить результаты **BM25 (или sparse)** и **dense embeddings** в один ранжированный
список. Ключевое слово — **fusion**, обычно **RRF (Reciprocal Rank Fusion)**:
`score(d) = Σ 1/(k + rank_i(d))` — складывает **позиции** в списках, не сырые
скоры (поэтому не нужна калибровка шкал). Альтернатива — **Relative Score Fusion**
(min-max нормировка скоров) и параметр **alpha** (0 = чистый keyword, 1 = чистый
вектор). Это то, что имеют в виду в 90% RAG-статей под «hybrid search».

**(b) Семантика + метаданные/атрибутивные фильтры — то, что назвал владелец.**
Dense-поиск **плюс структурные фильтры** по метаданным (`author = X`, `year >
2023`, `dept = legal`). Фильтр **сужает пул кандидатов**, чтобы нерелевантный
документ не мог занять слот. Это **ортогональный рычаг**: он **композируется** с
(a) — можно одновременно делать BM25+dense fusion И фильтровать по метаданным.
Строго говоря, «vector + filter» — это не «fusion двух ранкеров», а «поиск с
предикатом»; называть это «hybrid» распространено (особенно у вендоров), но это
другое явление, чем (a).

**(c) Sparse + dense** — частный случай/подмножество (a), где «лексику» дают не
BM25, а learned sparse (SPLADE/ELSER) + dense. Иногда «hybrid» = именно это.

### Дисциплина именования (для слайда)
- «Hybrid» **сам по себе неоднозначен** — всегда уточнять, **что** сливается:
  full-text (BM25) + dense / sparse + dense / keyword-filter + dense.
- **RRF — это метод слияния, а не синоним hybrid.** (Частая ошибка.)
- **Metadata filtering — это отдельный рычаг**, который сочетается со всеми
  вариантами, а не тип поиска.

### Фраза-корректор
> «„Гибрид“ — перегруженное слово. В RAG по умолчанию это про слияние двух ранкеров:
> BM25 по словам и эмбеддинги по смыслу, сведённые через RRF. То, что вы называете
> „семантика плюс строгие фильтры“ — тоже валидно, но это другой рычаг: фильтр по
> метаданным сужает пул до ранжирования и накладывается поверх любого поиска. То
> есть можно иметь и fusion, и фильтры одновременно — это не альтернативы.»

Sources:
- [Hybrid Search Explained (Weaviate)](https://weaviate.io/blog/hybrid-search-explained)
- [Hybrid Search Overview (Pinecone Docs)](https://docs.pinecone.io/guides/search/hybrid-search)
- [Hybrid Search for RAG: Combining BM25 and Dense Vector Search — 2026 Guide (Denser.ai)](https://denser.ai/blog/hybrid-search-for-rag/)
- [A Complete Guide to Filtering in Vector Search (Qdrant)](https://qdrant.tech/articles/vector-search-filtering/)

---

## 4. Elastic и OpenSearch — это векторные БД? — Да, с оговоркой позиционирования.

### Что спросил владелец
«Почему Elastic/OpenSearch не среди векторных БД? они же хранят эмбеддинги.»

### Точный ответ: ДА, оба — полноценные vector stores.
- **Elasticsearch:** тип поля **`dense_vector`** + kNN-поиск через **HNSW** (движок
  Lucene). С 8.12 — `int8_hnsw` со **scalar quantization** (−75% памяти). Делает
  hybrid (BM25 + kNN) нативно. `[VFY-day-of]` версии/квантизация эволюционируют.
- **OpenSearch** (форк Elasticsearch): **k-NN plugin** с выбором движка — **Lucene
  / FAISS / nmslib**; алгоритмы **HNSW и IVF**; квантизация PQ (с 2.10) и SQ. В
  **OpenSearch 3.0 (май 2025)** vector-движок ускорен до ~9.5× vs старые версии + GPU
  на индексации. `[VFY-day-of]` — цифра 9.5× вендорская, из релиз-нот.

Так что они **безусловно принадлежат ландшафту vector stores**. Правильное
позиционирование — **«поисковый движок, который ещё умеет вектора»**, в отличие от
**vector-native** движков (Qdrant / Milvus / Weaviate), которые строились вокруг
векторов с нуля.

### Чем отличаются от purpose-built (Qdrant/Milvus/Weaviate)

| Ось | Elastic / OpenSearch (search-engine-first) | Qdrant / Milvus / Weaviate (vector-native) |
|---|---|---|
| Происхождение | текстовый/лог-поиск, **вектора добавлены** | построены вокруг ANN с первого дня |
| Full-text / BM25 | зрелый, «из коробки», hybrid нативно | есть, но не главная сила |
| Фильтрация по метаданным | есть; Lucene-движок даёт «smart filtering» | **filterable HNSW** (Qdrant): фильтр внутри обхода графа, single-stage, а не pre/post |
| Квантизация | SQ/PQ (нагоняют) | 4 метода (Qdrant), зрелая компрессия | 
| Multi-vector / late-interaction | ограниченно | активно (ColBERT-подобное, Qdrant/Weaviate) |
| Payload с вектором | да, но модель «документ+поля» | JSON-payload на вектор — first-class |
| Ops / когда брать | **когда нужен и обычный поиск того же масштаба** | greenfield vector-нагрузки, ниже операционные накладные |
| Стоимость/лицензия | OpenSearch — Apache 2.0 (чище для self-host) | разные (Qdrant Apache 2.0 и т.д.) |

**Ключевой критерий выбора:** если у вас **уже** есть текстовый/лог-поиск того же
масштаба — Elastic/OpenSearch дают вектора «бесплатно» рядом и сильный hybrid.
Для чистой vector-нагрузки с нуля purpose-built обычно проще операционно и мощнее
по vector-специфичным фичам (filterable HNSW, multi-vector, зрелая квантизация).
Замечание: «чистый» **FAISS** (библиотека, а не БД) хранит только вектора без
payload и фильтрации — это не то же, что OpenSearch с FAISS-движком.

### Фраза-корректор
> «Elasticsearch и OpenSearch — да, это векторные хранилища: оба держат
> `dense_vector`, ищут через HNSW и делают hybrid нативно. Их просто честнее
> ставить в ландшафт как „поисковый движок, который научился в вектора“, а не как
> vector-native вроде Qdrant или Milvus. Отсюда и выбор: нужен и обычный поиск того
> же масштаба — берите Elastic/OpenSearch; чистая векторная нагрузка с нуля —
> purpose-built обычно проще и богаче по vector-фичам.»

Sources:
- [Vector Search in OpenSearch vs. Elasticsearch (Opster)](https://opster.com/guides/elasticsearch/machine-learning/vector-search-in-opensearch-vs-elasticsearch/)
- [Methods and engines — k-NN (OpenSearch Docs)](https://docs.opensearch.org/latest/mappings/supported-field-types/knn-methods-engines/)
- [Amazon OpenSearch Service's vector database capabilities explained (AWS)](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/)
- [Pre-Filtering vs Post-Filtering (and Why Qdrant Does Neither) (Qdrant)](https://qdrant.tech/blog/pre-filtering-vs-post-filtering/)
- [Best Vector Databases in 2026: A Complete Comparison Guide (Firecrawl)](https://www.firecrawl.dev/blog/best-vector-databases)
- [Choosing the Right Vector Database (Medium / E. Anderson)](https://medium.com/@elisheba.t.anderson/choosing-the-right-vector-database-opensearch-vs-pinecone-vs-qdrant-vs-weaviate-vs-milvus-vs-037343926d7e)

---

## Сводка правок к framing владельца (одним взглядом)

| Framing владельца | Точнее |
|---|---|
| «Семантика строится на BM25» | Нет: две независимые ветки; лексика — backbone, dense **добавлен** рядом; сливаются, не наследуются |
| (перед hybrid) dense/sparse не различены | Sparse = term-based, ~словарь, почти нули (BM25, SPLADE); dense = эмбеддинг, 384-1024, все ненулевые |
| «Hybrid = семантика + строгие фильтры» | Это (b) из трёх смыслов; основной в RAG — (a) BM25+dense fusion через RRF; фильтр — ортогональный рычаг |
| «Elastic/OpenSearch — не векторные БД» | Векторные: `dense_vector`+HNSW / k-NN plugin; позиционировать как «search engine that also does vectors» |

`[VFY-day-of]`: версии движков (Elastic `int8_hnsw`, OpenSearch 3.0 «9.5×», квантизация PQ/SQ), любые бенчмарк-числа NDCG/latency — проверять в день лекции.
